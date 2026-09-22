/* alloc_counter.c — LD_PRELOAD 힙 할당 카운터
 *
 * bench 가 측정 구간에서 실제로 몇 번, 몇 바이트를 heap 에 요청하는지 센다.
 * Cap'n Proto 의 MallocMessageBuilder 는 malloc/calloc 을 직접 쓰고,
 * Protobuf 는 operator new 를 거치므로, 둘을 공평하게 잡으려면
 * C 런타임 레벨(malloc)에서 가로채야 한다.
 *
 * dlsym(RTLD_NEXT, ...) 부트스트랩 문제를 피하려고 glibc 의
 * __libc_malloc 계열을 직접 호출한다.
 *
 * 빌드:  gcc -O2 -fPIC -shared -o alloc_counter.so alloc_counter.c
 * 사용:  LD_PRELOAD=./alloc_counter.so ./bench
 *
 * 주의: 이 라이브러리를 얹으면 할당 경로가 느려지므로 시간 측정과
 *       같은 실행에서 재지 않는다. run.sh 가 두 번 나눠 돌린다.
 */
#define _GNU_SOURCE
#include <stddef.h>

extern void *__libc_malloc(size_t);
extern void *__libc_calloc(size_t, size_t);
extern void *__libc_realloc(void *, size_t);
extern void __libc_free(void *);

static unsigned long long g_count = 0;
static unsigned long long g_bytes = 0;
static int g_on = 0;

/* bench 가 weak symbol 로 참조한다 */
void ac_reset(void) { g_count = 0; g_bytes = 0; g_on = 1; }
void ac_stop(void) { g_on = 0; }
unsigned long long ac_count(void) { return g_count; }
unsigned long long ac_bytes(void) { return g_bytes; }
int ac_present(void) { return 1; }

void *malloc(size_t n) {
    if (g_on) { g_count++; g_bytes += n; }
    return __libc_malloc(n);
}

void *calloc(size_t a, size_t b) {
    if (g_on) { g_count++; g_bytes += a * b; }
    return __libc_calloc(a, b);
}

void *realloc(void *p, size_t n) {
    if (g_on) { g_count++; g_bytes += n; }
    return __libc_realloc(p, n);
}

void free(void *p) { __libc_free(p); }
