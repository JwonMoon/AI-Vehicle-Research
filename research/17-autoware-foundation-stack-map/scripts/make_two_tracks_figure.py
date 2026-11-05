#!/usr/bin/env python3
# 사용: python3 -I scripts/make_two_tracks_figure.py images/02-two-tracks-explained.svg
# 그림 2 '두 갈래 관계도'를 생성한다. 내용은 본문의 출처 있는 사실만 사용한다(자체 작성 도식).
W, H = 1500, 960
INK, MUTED, LINE = "#1f2328", "#59636e", "#d1d9e0"
BLUE, BLUE_BG = "#2563eb", "#eff6ff"
ORG, ORG_BG = "#c2410c", "#fff7ed"
GRN, GRN_BG = "#047857", "#ecfdf5"
GRAY_BG = "#f3f4f6"
o = []
def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
def T(x,y,s,sz=13,c=INK,w="normal",a="start"): o.append(f'<text x="{x}" y="{y}" font-size="{sz}" fill="{c}" font-weight="{w}" text-anchor="{a}">{esc(s)}</text>')
def R(x,y,w,h,f="#fff",s=LINE,rx=10,sw=1.4,d=None): o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{f}" stroke="{s}" stroke-width="{sw}"'+(f' stroke-dasharray="{d}"' if d else "")+'/>')
def P(d,c=MUTED,sw=1.8,dash=None,m="a"): o.append(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{sw}"'+(f' stroke-dasharray="{dash}"' if dash else "")+(f' marker-end="url(#{m})"' if m else "")+'/>')
def L(x1,y1,x2,y2,c=MUTED,sw=1.8,m="a"): P(f"M{x1},{y1} L{x2},{y2}",c,sw,None,m)
def tw(s,sz): return sum(sz*(1.0 if ord(ch)>0x1100 else 0.58) for ch in s)
def chips(x,y,items,maxx):
    bx,by=x,y
    for f in items:
        w=tw(f,11.5)+16
        if bx+w>maxx: bx,by=x,by+28
        R(bx,by,w,22,"#fff",MUTED,11,1.1); T(bx+8,by+15.5,f,11.5,INK); bx+=w+6
    return by
def wrap(x,y,text,maxw,sz=11.5,c=INK):
    line=""
    for wd in text.split(" "):
        cand=(line+" "+wd).strip()
        if tw(cand,sz)>maxw: T(x,y,line,sz,c); y+=17; line=wd
        else: line=cand
    if line: T(x,y,line,sz,c)

T(W/2,38,"Autoware 재단의 두 갈래 — 무엇이 어디에 들어가나 (2026-10)",21,INK,"bold","middle")
T(W/2,62,"왼쪽은 '자율주행 플랫폼'과 그 안에 꽂을 AI 부품들, 오른쪽은 '혼자 도는 운전 보조 프로그램'이다",14,MUTED,"normal","middle")

# ================= LEFT: robotaxi track
R(24,80,930,656,"#fbfdff",BLUE,16,2); R(24,80,930,46,BLUE,BLUE,16,2); R(24,110,930,16,BLUE,BLUE,0,0)
T(44,110,"① 로보택시 · 무인 셔틀 트랙  —  플랫폼: Autoware 2.0",17,"#fff","bold")
T(44,152,"Autoware = 차가 '보고 → 위치를 알고 → 길을 정하고 → 조작하는' 전 과정을 담은 큰 소프트웨어 묶음 (ROS 2 패키지 수백 개)",13,INK)
for x,h1,a,b in [(44,"① 보기","카메라·LiDAR·레이더","사람·차·신호등 인식"),(214,"② 내 위치","고정밀 지도","위치 추정")]:
    R(x,180,150,110,"#fff",BLUE,10,1.6); T(x+75,210,h1,15,BLUE,"bold","middle"); T(x+75,236,a,12.5,INK,"normal","middle"); T(x+75,258,b,12.5,INK,"normal","middle")
L(194,235,212,235); L(364,235,382,235)
# planning: generator slot (bottom) -> selector (top) -> control
R(384,166,330,256,BLUE_BG,BLUE,12,2.4)
T(549,192,"③ 갈 길 정하기 (계획)",15,BLUE,"bold","middle")
R(400,204,298,52,"#fff",LINE,8,1.2,"4 3")
T(549,225,"검사·선택기 (Selector)",12.5,MUTED,"bold","middle"); T(549,245,"후보 경로를 안전 검사 후 고름 — 아직 꺼져 있음",11.5,MUTED,"normal","middle")
L(549,286,549,259,BLUE,1.6,"ab")
R(400,288,298,124,"#fff",BLUE,10,1.6,"6 4")
T(549,307,"경로 생성기 '자리' — 2.0에서 교체 가능해짐",12.5,BLUE,"bold","middle")
R(412,317,274,34,GRAY_BG,LINE,8); T(549,339,"규칙 기반 플래너 (기본값)",13,INK,"bold","middle")
R(412,359,274,44,"#dbeafe",BLUE,8,1.6); T(549,378,"Diffusion Planner (AI)",13,BLUE,"bold","middle"); T(549,395,"이미 내장 · 실행 옵션 하나로 선택",11.5,INK,"normal","middle")
L(714,230,734,230)
R(736,180,100,110,"#fff",BLUE,10,1.6); T(786,215,"④ 조작",15,BLUE,"bold","middle"); T(786,240,"핸들·페달",12.5,INK,"normal","middle"); T(786,260,"제어",12.5,INK,"normal","middle")
L(836,235,856,235)
R(858,200,80,70,GRAY_BG,LINE,10); T(898,241,"차량",14,INK,"bold","middle")

cards = [
 (44,"OnePlanner","LiDAR + 벡터 지도를 보고 경로를 내는 AI","보는 것: LiDAR 점군, Lanelet2 지도, 경로, 신호등",["ROS 2 노드(C++)","가중치: HF"],"Autoware Core 위에서 실행. README: 'Autoware 경로 검사 뒤에 연결하라'"),
 (348,"LatentDrive","앞 카메라 영상만 보고 경로를 내는 AI","보는 것: 전방 카메라 1·3대 + 경로점",["C++ 라이브러리","재생용 ROS 2 노드","가중치: HF"],"Autoware 개발 이미지에서 실행. 녹화 재생으로 계획을 그리기만 함"),
 (652,"AutoE2E","카메라 6대로 주변을 보고 경로를 내는 AI","보는 것: 서라운드 카메라 6대 (+지도 선택)",["AI 모델 코드(Python)","가중치: HF"],"Robotaxi WG가 개발. 저장소에 ROS·Autoware 연결 코드나 설명이 없음"),
]
for x,*_ in cards:
    P(f"M{x+144},478 C{x+144},452 549,452 549,415", BLUE, 1.6, "6 5", "ab")
R(140,432,680,28,"#fbfdff","#fbfdff",6,0)
T(480,451,"경로(궤적)를 내는 AI 모델 3개 — 공식 문서의 '생성기' 정의에 해당, 2.0.0에는 미장착",13.5,INK,"bold","middle")
for x,name,one,see,forms,rel in cards:
    R(x,478,288,240,"#fff",BLUE,12,1.6)
    T(x+16,507,name,17,BLUE,"bold"); T(x+16,531,one,12.5,INK,"bold"); T(x+16,556,see,12,INK)
    T(x+16,583,"제공 형태",11.5,MUTED,"bold")
    by=chips(x+16,592,forms,x+280)
    T(x+16,by+44,"Autoware와의 관계",11.5,MUTED,"bold")
    wrap(x+16,by+63,rel,256)

# ================= RIGHT: ADAS track
X0=978
R(X0,80,498,656,"#fffcf7",ORG,16,2); R(X0,80,498,46,ORG,ORG,16,2); R(X0,110,498,16,ORG,ORG,0,0)
T(X0+20,110,"② 운전 보조(ADAS) · 개인차량 트랙",17,"#fff","bold")
T(X0+20,152,"Autoware 부품이 아닌, 혼자 도는 완성 프로그램",13,INK,"bold")
R(X0+20,166,458,346,ORG_BG,ORG,12,2.2)
T(X0+40,196,"Vision Pilot",18,ORG,"bold")
T(X0+40,218,"차선 유지 · 앞차 따라가기 · 긴급 제동 (레벨 2)",12.5,INK)
steps=[("카메라 1대 · 지도 없음","sensing"),("AI 모델 3개","models"),("안전 융합·계획 (Safety Guardian)","safety_guardian"),("핸들·페달 (CAN)","vehicle_interface")]
yy=232
ymid={}
for i,(st,mod) in enumerate(steps):
    R(X0+40,yy,300,40,"#fff",ORG if i==1 else LINE,8,1.8 if i==1 else 1.2)
    T(X0+54,yy+25,st,13,ORG if i==1 else INK,"bold"); T(X0+330,yy+25,mod,10.5,MUTED,"normal","end")
    ymid[i]=yy+20
    if i<3: L(X0+190,yy+40,X0+190,yy+52,ORG,1.6,"ao")
    yy+=54
T(X0+40,yy+12,"제공 형태",11.5,MUTED,"bold")
chips(X0+40,yy+20,["단독 C++ 프로그램",".deb 설치 파일","Docker","ROS 2는 선택"],X0+470)
T(X0+20,540,"안에 들어간 AI 모델 — 각각 별도 저장소(학습 코드 + 가중치)",13,INK,"bold")
for i,(n,d) in enumerate([("AutoSteer","갈 길(경로) 예측"),("AutoSpeed","앞의 차·장애물 찾기"),("AutoDrive","곡률·앞차 거리 (E2E)")]):
    x=X0+20+i*156
    R(x,566,146,74,"#fff",ORG,10,1.6); T(x+73,594,n,14.5,ORG,"bold","middle"); T(x+73,618,d,11.5,INK,"normal","middle")
    P(f"M{x+73},566 L{x+73},554",ORG,1.4,None,None)
P(f"M{X0+93},554 L{X0+488},554",ORG,1.4,None,None)
P(f"M{X0+488},554 L{X0+488},{ymid[1]} L{X0+344},{ymid[1]}",ORG,1.6,None,"ao")
T(X0+360,ymid[1]-8,"들어 있음",11.5,ORG,"bold")
T(X0+20,668,"· 카메라 1대 + 저가 칩(3–5 TOPS) 목표, 지도 불필요",12.5,INK)
T(X0+20,692,"· AutoE2E는 Vision Pilot에 들어 있지 않다 (코드 확인)",12.5,INK)
T(X0+20,716,"· 최신 1.2 (2026-08), 1.3·안전 인증 작업 중",12.5,INK)

# ================= bottom shared
R(24,752,1452,150,GRN_BG,GRN,14,1.8)
T(44,780,"두 트랙이 같이 쓰는 기반",15,GRN,"bold")
for i,(h,a,b) in enumerate([("Hugging Face (AI 모델 보관소)","Autoware 내장 AI 모델, OnePlanner,","LatentDrive, AutoE2E 가중치를 버전별로 공개"),
                            ("Autoware Index (패키지 목록)","Autoware 밖 패키지를 등록·검증.","Vision Pilot = 첫 '레퍼런스 디자인'으로 등록"),
                            ("Open AD Kit (배포 묶음)","컨테이너로 묶어 배포하는 도구.","v2.0 Autoware → v2.1 Vision Pilot (예정)")]):
    x=44+i*480
    R(x,794,460,92,"#fff",GRN,10,1.3); T(x+16,820,h,14,GRN,"bold"); T(x+16,844,a,12.5,INK); T(x+16,866,b,12.5,INK)
ly=936
P(f"M44,{ly-4} L84,{ly-4}",BLUE,1.8,"6 5","ab"); T(92,ly,"생성기 정의에 해당, 아직 미장착",12.5,MUTED)
P(f"M320,{ly-4} L360,{ly-4}",ORG,1.6,None,"ao"); T(368,ly,"이미 들어 있음",12.5,MUTED)
T(500,ly,"HF = Hugging Face(AI 모델 공개 사이트) · 근거: 각 저장소 README, Autoware 2.0 문서, Vision Pilot 소스 코드 (2026-10-30 확인)",12,MUTED)

defs=('<defs>'+"".join(f'<marker id="{i}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>' for i,c in (("a",MUTED),("ab",BLUE),("ao",ORG)))+'</defs>')
svg=(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Pretendard, \'Apple SD Gothic Neo\', \'Noto Sans KR\', \'Malgun Gothic\', sans-serif">'
     +defs+f'<rect width="{W}" height="{H}" fill="#ffffff"/>'+"\n".join(o)+'</svg>')
import sys, pathlib
out = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path('images/02-two-tracks-explained.svg')
out.write_text(svg, encoding='utf-8')
print('wrote', out)
