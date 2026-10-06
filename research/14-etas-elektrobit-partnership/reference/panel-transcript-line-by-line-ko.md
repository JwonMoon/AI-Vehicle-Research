# ETAS × Elektrobit 패널 토론 — 한 줄씩 해석

**읽는 법:** 인용 블록(>)이 원문, 그 아래가 한국어 해석입니다. 원문은 받은 전사본 그대로 두었고, 해석에는 전사 오류를 바로잡은 용어를 썼습니다. 화자는 문맥으로 추정해 표시했습니다.

**참석자 (전사 표기 → 추정 표기)**
- 사회자: Anton (Elektrobit 소속, 끝인사에서는 "Hunter"로 전사됨)
- Björn Reistel — ETAS 에코시스템·오픈소스 커뮤니티 매니저
- Isaac Trebs (전사: "Masek") — Elektrobit 제품 매니저
- Subhash Sindhya — ETAS Chief Product Manager
- Moritz (전사: "Mobex Naukishman", "Mohd", "more days") — Elektrobit HPC·SDV 사업 책임

**주요 전사 오류 정리:** ETAs / Ethers / ATOS → ETAS · ElectraBit / ElectroBuild / Electroby → Elektrobit(EB) · EDAS / Adidas / ADOS / Addis → ADAS · Corbus / Corvus / core boss → EB corbos Linux for Safety Applications · S-Core / ESCO / escrow / storage → Eclipse S-CORE · NECLIPSE → Eclipse 재단 · EBMS → EDMS

---

## 1. 자기소개

**[Björn]**

> for sure. Welcome everybody, happy to see you.

네, 물론이죠. 여러분 모두 환영합니다. 만나서 반갑습니다.

> My name is Björn Reistel, I'm part of ETAs, holding the role of an ecosystem and open source community manager.

저는 Björn Reistel이고, ETAS에서 에코시스템 및 오픈소스 커뮤니티 매니저를 맡고 있습니다.

> Being here to figure out why we believe collaborating is key to success on the one hand side and doing this in open source is a second factor as well in it.

한편으로는 왜 협업이 성공의 열쇠라고 믿는지, 또 그것을 오픈소스로 하는 것이 왜 또 하나의 핵심 요소인지 이야기하려고 이 자리에 나왔습니다.

**[사회자]**

> Thank you. Thanks a lot. Masek, you're next.

감사합니다. 다음은 Isaac 차례입니다.

**[Isaac]**

> Hi everyone, I'm Isaac Trebs, I'm a product manager at ElectraBit.

안녕하세요, 저는 Elektrobit의 제품 매니저 Isaac Trebs입니다.

> I've been with ElectraBit for three years working on our Linux for safety application solution and I'm here because I think that this partnership with ETAs really levels up what our Linux for safety applications can do for potential customers.

Elektrobit에서 3년째 'Linux for Safety Applications' 솔루션을 담당하고 있고, ETAS와의 이번 파트너십이 우리 제품이 잠재 고객에게 해 줄 수 있는 일을 한 단계 끌어올린다고 생각해서 이 자리에 나왔습니다.

**[사회자]**

> Thanks a lot Isaac. Now over to you Subhash.

고맙습니다, Isaac. 이제 Subhash 차례입니다.

**[Subhash]**

> Thanks Anton and also a very warm welcome from my end.

고마워요, Anton. 저도 여러분을 진심으로 환영합니다.

> My name is Subhash Sindhya, so I'm responsible at ETAs as the Chief Product Manager.

저는 Subhash Sindhya이고, ETAS에서 Chief Product Manager를 맡고 있습니다.

> Basically responsible for the entire portfolio from the compute side.

기본적으로 컴퓨트(차량 컴퓨팅) 측면의 전체 포트폴리오를 책임지고 있습니다.

> I'm really glad that we've got this cooperation set up with Electrobit and also provide insights to you.

Elektrobit과 이번 협력을 성사시키고, 여러분께 그 내용을 공유할 수 있어서 정말 기쁩니다.

> So I'm excited to do this together.

함께하게 되어 설렙니다.

> It's a wonderful team.

정말 훌륭한 팀입니다.

**[사회자]**

> Now last one by you is Mobex.

마지막으로 Moritz입니다.

**[Moritz]**

> Hi, my name is Mobex Naukishman, I'm responsible for HPC and SDV business a bit after a bit.

안녕하세요, 저는 Moritz이고 Elektrobit에서 HPC(고성능 컴퓨터)와 SDV(소프트웨어 정의 차량) 사업을 맡고 있습니다.

> I'm really psyched about this because it actually shows how communities coming together to build SDV programs successfully together, getting the most relevant technology together in an open fashion.

이번 일이 정말 신나는 이유는, 여러 커뮤니티가 모여 가장 중요한 기술들을 개방적인 방식으로 결합해 SDV 프로그램을 함께 성공시키는 모습을 실제로 보여 주기 때문입니다.

---

## 2. 업계 큰 그림

**[사회자]**

> Okay, thanks a lot.

네, 감사합니다.

> Now let's start a bit with the big picture, that is what I wanted to say.

이제 큰 그림부터 시작해 보죠. 그게 제가 드리고 싶었던 말입니다.

> And while we're sticking to focus on what do you think of the current PC and industry and how they have changed?

지금의 SDV 업계를 어떻게 보시는지, 그리고 어떻게 변해 왔다고 생각하시나요?

**[Moritz]**

> I think we've seen SDE programs turn around a bit, getting to more realism, also putting a lot more emphasis now on collaboration building solutions together.

SDV 프로그램들이 방향을 조금 틀어서 더 현실적으로 바뀌었고, 이제는 솔루션을 함께 만드는 협업에 훨씬 더 큰 비중을 두고 있다고 봅니다.

> At the same time, still we have full throttle on re-architecting platforms going towards zonal architectures is still very much in progress.

동시에 존(zonal) 아키텍처로 플랫폼을 재설계하는 작업은 여전히 전속력으로 진행 중입니다.

> And we also see bigger investments in industries that are based on the other, so when you look at physical AI for instance.

그리고 이와 맞닿은 다른 산업들, 예컨대 피지컬 AI 같은 분야에 더 큰 투자가 이뤄지는 것도 보입니다.

> So what we see as a big trend, aside from the open source perspective, is convergence of technologies.

그래서 오픈소스 관점 외에 저희가 보는 큰 흐름은 '기술의 융합'입니다.

> Does it make sense to really bring technologies together that are already well established in other industries?

다른 산업에서 이미 자리 잡은 기술을 가져와 결합하는 게 말이 되느냐는 것이죠.

> So for instance looking at using Linux for automotive as well as robotics, also for safety critical workloads.

예를 들어 리눅스를 자동차와 로보틱스 모두에, 그것도 안전이 중요한(safety-critical) 작업에까지 쓰는 것처럼요.

> And really getting these solutions together, really building an ecosystem where we connect functionality ecosystems to build great solutions.

그리고 이런 솔루션들을 한데 모아, 기능별 생태계를 연결해 훌륭한 솔루션을 만드는 생태계를 구축하는 것입니다.

> This is what this partnership is for us about, actually getting the best available solutions in the industry together to build something compelling.

저희에게 이번 파트너십이 바로 그런 의미입니다. 업계 최고의 솔루션들을 모아 설득력 있는 무언가를 만드는 것이죠.

**[Subhash]**

> Absolutely. So thanks, Mohd.

전적으로 동의합니다. 고마워요, Moritz.

> I think maybe I could then pick up and also once again resonate on that.

제가 이어받아서 그 말에 다시 한번 공감을 보태 보겠습니다.

> One of the things I think we've been seeing in the market is that customers are really looking at all sorts of solutions, which goes beyond just problems that were solved in the automotive.

시장에서 보이는 현상 중 하나는, 고객들이 자동차 업계 안에서 해결된 문제를 넘어 온갖 종류의 솔루션을 살펴보고 있다는 점입니다.

> Perhaps this has been solved elsewhere, but it's already highlighted in other ecosystems as well.

어떤 문제는 다른 곳에서 이미 해결됐고, 다른 생태계에서도 이미 부각된 것일 수 있죠.

> And what we see is that they're also looking for partners who've probably done this groundwork already for them.

그리고 고객들은 그런 기초 작업을 이미 해 둔 파트너를 찾고 있습니다.

> So you're looking at other solutions that are available in the market and what's slowing down certain programs.

즉 시장에 나와 있는 다른 솔루션은 무엇인지, 어떤 요인이 특정 프로그램을 더디게 만드는지를 살피는 거죠.

> How can this be reused into automotive context as well?

그걸 어떻게 자동차 맥락에서도 재사용할 수 있을까 하는 겁니다.

> So this is what customers and partners are looking for.

이게 바로 고객과 파트너들이 찾고 있는 것입니다.

> And this is, I think, the value of this partnership where we want to show how we've done this groundwork for our customers, for the ecosystem and provide this value to our automotive customers as well.

그리고 이것이 이번 파트너십의 가치라고 봅니다. 저희가 고객과 생태계를 위해 이 기초 작업을 어떻게 해 왔는지 보여 주고, 그 가치를 자동차 고객에게도 제공하려는 것이죠.

---

## 3. 왜 경쟁사와 손잡았나

**[사회자]**

> Thanks a lot.

감사합니다.

> I'm working for Electrobit and when I first thought about this partnership, it seems like why are we now joining a partnership with a competitor?

저는 Elektrobit에서 일하는데, 이 파트너십 얘기를 처음 들었을 때 '왜 우리가 경쟁사와 손을 잡지?' 싶었습니다.

> I mean, it is right, Subhash, can you comment on that?

실제로 그렇잖아요. Subhash, 여기에 대해 한마디 해 주시겠어요?

**[Subhash]**

> Sure, of course.

네, 물론이죠.

> I think in the last few years the co-operative landscape has increased and also intensified.

지난 몇 년 사이 협력의 판도가 넓어지고 또 깊어졌다고 봅니다.

> We see collaboration, of course, on layers and on topics which complement each other.

서로를 보완하는 레이어와 주제에서 협업이 이뤄지고 있죠.

> So we clearly see that together with Electrobit we have complementing assets.

그리고 Elektrobit과 저희는 분명히 서로 보완되는 자산을 갖고 있습니다.

> For example, combining your core boss nuts for safety applications with our ADAS capability.

예를 들면 귀사의 EB corbos Linux for Safety Applications와 저희의 ADAS 역량을 결합하는 것이죠.

> So EDAS is leading with the ADAS capability in the market and combining these two assets would mean that there's a joint offering and a joint value proposition for our customers.

ETAS는 시장에서 ADAS 역량을 앞세우고 있고, 두 자산을 합치면 고객에게 공동 제품과 공동 가치 제안을 내놓을 수 있다는 뜻입니다.

> So yes, on the one hand side we do compete on certain areas, but on areas where we see where we can complement, especially looking at open source and collaboration areas.

네, 한편으로 특정 분야에서는 분명히 경쟁합니다. 하지만 서로 보완할 수 있는 분야, 특히 오픈소스와 협업 영역에서는 다릅니다.

> This is something where we really have a joint value to our customers as well.

이런 영역에서 저희는 고객에게 진정한 공동의 가치를 줄 수 있습니다.

**[사회자]**

> Thanks a lot.

감사합니다.

> I mean, not the counter position, but maybe the same position from the other perspective, Moritz.

반대 입장이라기보다는, 같은 입장을 반대편 시각에서 들어 보죠, Moritz.

> What do you think?

어떻게 생각하세요?

> What's in 4Electroby?

Elektrobit에는 어떤 이득이 있나요?

**[Moritz]**

> This is the position obviously is very similar.

당연히 입장은 아주 비슷합니다.

> Otherwise, we wouldn't have a serious discussion at this point in time.

그렇지 않았다면 지금 이렇게 진지하게 논의하고 있지 않겠죠.

> No, but seriously, looking at things, I mean, EB Corbus limits for safety applications is basic software that does base enablement.

농담은 그만하고 진지하게 보면, EB corbos Linux for Safety Applications는 기반을 마련해 주는 기본 소프트웨어입니다.

> But obviously when you want to start developing functionality, there's a lot of domain specifics on top.

하지만 실제 기능을 개발하려고 하면 그 위에 도메인 특화 요소가 많이 필요합니다.

> And when we now look at Adidas' ADA solution with EBMS, this is something that comes very naturally as a complementary solution towards EB Corvus Manus for Safety Applications.

그런데 ETAS의 ADAS 솔루션인 EDMS를 보면, EB corbos Linux for Safety Applications를 보완하는 솔루션으로 아주 자연스럽게 들어맞습니다.

> This is for us the rationale to bring solutions together that we really would expect to see in the fields together.

현장에서 함께 쓰일 거라고 예상되는 솔루션들을 묶는 것, 이게 저희의 근거입니다.

> especially now when we look at both companies, yes, in some parts we are in competition for these two offerings, we obviously aren't.

특히 두 회사를 보면, 네, 일부 분야에서는 경쟁하지만 이 두 제품에 관해서는 분명히 경쟁 관계가 아닙니다.

> And getting this together just makes a whole lot of sense in that perspective.

그런 관점에서 이걸 합치는 건 아주 타당합니다.

> Also, when we look at it, especially in the ADAS, where we see a whole lot of bespoke solutions right now, where we say, okay, get into something more standardized, more repeatable, that is not necessarily bound to buying a specific piece of hardware as well.

또 특히 ADAS 분야는 지금 맞춤형(bespoke) 솔루션이 넘쳐나는데, 이제는 더 표준화되고 반복 적용 가능하며 특정 하드웨어 구매에 묶이지 않는 방향으로 가자는 겁니다.

> That makes a whole lot of sense for us.

저희에게는 그게 아주 타당합니다.

> So you really thought, okay, get into something more standardized, more repeatable, that is not necessarily bound to buying a specific piece of hardware as well.

(전사 중복) 더 표준화되고, 반복 가능하며, 특정 하드웨어에 묶이지 않는 방향으로 가자는 생각이었죠.

> an ADOS framework with safety requirements together with Corvus Linux for safety applications.

안전 요구사항을 갖춘 ADAS 프레임워크를 EB corbos Linux for Safety Applications와 함께 쓰는 것.

> It's just a very natural fit for us.

저희에게는 정말 자연스러운 조합입니다.

> And then of course also once we started interacting, we also felt that from a cultural perspective it is a very good fit.

그리고 실제로 교류를 시작해 보니 문화적으로도 아주 잘 맞는다고 느꼈습니다.

> We kick a like and I think this really is one key ingredient to actually make this a successful partnership here.

서로 생각이 잘 통했고, 이게 파트너십을 성공시키는 핵심 요소 중 하나라고 생각합니다.

---

## 4. 고객에게 주는 실질적 가치

**[사회자]**

> Cool, thanks a lot.

좋네요, 감사합니다.

> This sounds really, really great.

정말 멋지게 들립니다.

> Now, we looked at the industry, we looked at our partnership,

지금까지 업계와 저희 파트너십을 살펴봤는데요,

> Now, looking at the customers, Isaac, what do you think?

이제 고객 쪽을 보죠. Isaac, 어떻게 생각하세요?

> How does this now translate into a practical solution for our customers?

이게 고객에게 실제로 어떤 솔루션으로 이어지나요?

**[Isaac]**

> Yeah, so by putting EDMS on top of Linux, that makes the developer's life a lot easier and is going to lower the development effort as well as increase the time to market.

네, EDMS를 리눅스 위에 올리면 개발자의 삶이 훨씬 편해지고, 개발 공수가 줄며 출시 기간도 단축됩니다.

> The first reason is, I mean, you could have gotten EDMS before and used Linux before, but now Electrobit and ATOS are saying, hey, our solutions work together now.

첫째 이유는, 예전에도 EDMS를 구하고 리눅스를 쓸 수는 있었지만, 이제는 Elektrobit과 ETAS가 '우리 솔루션은 함께 동작한다'고 보증한다는 점입니다.

> This isn't a problem that you as a developer need to solve.

개발자인 여러분이 직접 풀어야 할 문제가 아니라는 거죠.

> And then by having Linux as the basis for it,

그리고 리눅스를 기반으로 하기 때문에,

> um developers can use the tools and the knowledge that they know and love

개발자들이 익숙하고 좋아하는 도구와 지식을 그대로 쓸 수 있습니다.

> there are people developers generally are coming from a linux background from from college university or even before

개발자들은 대개 대학 시절이나 그 이전부터 리눅스 배경을 갖고 있습니다.

> they know how to work with linux they know all the tools docker they know the compilers they know the debuggers gdb etc etc

리눅스로 작업하는 법을 알고, Docker 같은 도구, 컴파일러, gdb 같은 디버거 등을 다 알죠.

> and then they get into the industry and then they have to switch gears to the proprietary operating system and ramp up on that and learn all new tools

그런데 업계에 들어오면 독점(상용) 운영체제로 갈아타고, 그걸 새로 익히고, 도구도 전부 새로 배워야 합니다.

> and those those tools as well probably for a proprietary solution or proprietary operating system are probably not going to be as good and mature as ones you get from Linux which is being developed by an open community of Millions, right?

게다가 독점 솔루션이나 독점 OS용 도구는 수백만 명의 오픈 커뮤니티가 개발하는 리눅스 도구만큼 좋고 성숙하지도 않을 가능성이 크죠.

> So for the developer, it's going to be a lot easier experience and it also helps you to avoid another paradigm that we've seen often in the industry is develop on Linux

그래서 개발자에게는 훨씬 쉬운 경험이 되고, 업계에서 자주 보던 또 다른 패턴, 즉 '일단 리눅스에서 개발한다'는 패턴의 함정도 피할 수 있습니다.

> because Developing and prototyping on Linux is easy because of all the reasons I mentioned before

앞서 말한 이유들 때문에 리눅스에서 개발하고 프로토타이핑하는 건 쉽거든요.

> In addition Linux is also the operating system that you're going to get from from an SOC vendor

게다가 리눅스는 SoC(반도체) 공급사로부터 기본으로 받게 되는 운영체제이기도 합니다.

> It's a very easy to get

구하기가 아주 쉽죠.

> Linux so you'll probably start your development and prototyping on Linux and then you get to a point near your started production and that's when you say oh well now we need functional safety so now we're going to pivot to some proprietary operating system away from Linux for the final push into SOP

그래서 리눅스에서 개발과 프로토타이핑을 시작했다가 양산 직전에 이르러서야 '아, 이제 기능 안전이 필요하네' 하고 SOP(양산 개시)를 위한 마지막 단계에서 리눅스를 버리고 독점 OS로 방향을 틀게 됩니다.

> but this of course is a huge risk and a huge disruption

하지만 이건 당연히 엄청난 리스크이자 큰 혼란입니다.

> you know you can say well there are you know common interfaces that the operating systems offer so so everything should just work

운영체제들이 공통 인터페이스를 제공하니까 전부 그냥 잘 돌아갈 거라고 말할 수도 있겠죠.

> but we all know from for being engineers that things that should just work never actually do just work right

하지만 엔지니어라면 다 알잖아요. '그냥 잘 돌아가야 하는' 것은 실제로는 절대 그냥 돌아가지 않는다는 걸요.

> so it's a huge risk and a huge disruption and it's going to cost you effort and it's going to to hurt your time to market

그래서 큰 리스크이고 큰 혼란이며, 공수가 들고 출시 일정에도 타격을 줍니다.

> so by just sticking with Linux from the beginning, you're allowing developers to use what they know and love from the beginning until the end without any disruptions, including all of the tooling, compilers, all the things that they know and love.

처음부터 끝까지 리눅스를 고수하면, 개발자들은 도구·컴파일러 등 익숙하고 좋아하는 모든 것을 처음부터 끝까지 중단 없이 쓸 수 있습니다.

---

## 5. 벤더 종속(lock-in)은 없는가

**[사회자]**

> Okay.

네.

> By the way, I see from time to time raising hands in the participants.

그런데 참석자 중에 가끔 손을 드시는 분들이 보이네요.

> If you have a question, please feel free to raise them in the Q&A section.

질문이 있으시면 Q&A 창에 편하게 남겨 주세요.

> We will collect the questions and then work on them after our discussions.

질문을 모아서 토론이 끝난 뒤 답변하겠습니다.

> We reserved some extra time in it.

이를 위해 여유 시간을 따로 잡아 두었습니다.

> And to give you a heads up, we are already good in time.

미리 말씀드리면, 지금 시간은 넉넉합니다.

> So we are pretty sure, or I'm pretty sure that we also have some time to answer these afterwards.

그래서 나중에 답변할 시간도 충분할 거라고 확신합니다.

> Isaac, apologies, now I interrupted you a bit.

Isaac, 말을 끊어서 죄송합니다.

> You were talking a lot about Linux.

리눅스 얘기를 많이 하셨는데요.

> That means there is no real vendor login.

그 말은 사실상 벤더 종속(lock-in)이 없다는 뜻인가요?

> Like we see this in other systems or how is it?

다른 시스템에서 보던 것처럼요, 아니면 어떤가요?

**[Isaac]**

> Essentially from the operating system, yes.

운영체제 측면에서는 본질적으로 그렇습니다.

> First of all, Linux provides a very good POSIX implementation, which is generally the standard.

우선 리눅스는 사실상 표준인 POSIX를 아주 잘 구현하고 있습니다.

> So EDMS is also built on top of POSIX.

EDMS도 POSIX 위에 만들어져 있죠.

> So, you know, you can easily swap out the operating system underneath.

그래서 그 아래의 운영체제를 쉽게 교체할 수 있습니다.

> And also within the Linux world, there is a plethora of offerings, right?

또 리눅스 세계 안에도 선택지가 아주 많습니다.

> Generally, when you choose a Linux, your most important concern will be, of course, ease of working with it and configurability.

리눅스를 고를 때 가장 중요한 건 당연히 다루기 쉬운지, 그리고 설정 유연성이겠죠.

> But another huge topic is going to be cybersecurity maintenance, especially in the, you know, the network centralized architectures that the automotive industry is moving towards, right?

하지만 또 하나의 큰 주제는 사이버보안 유지보수입니다. 특히 자동차 업계가 향하고 있는 네트워크 중심의 중앙집중형 아키텍처에서는요.

> So you're going to need cybersecurity maintenance.

그러니 사이버보안 유지보수가 반드시 필요합니다.

> So you may choose which Linux you want to use based on the cybersecurity maintenance offering.

그래서 사이버보안 유지보수 서비스를 기준으로 어떤 리눅스를 쓸지 고를 수도 있습니다.

> And by using Linux, again, you have a huge offering.

리눅스를 쓰면, 다시 말하지만, 선택지가 매우 넓습니다.

> There's a bunch of people out there who offer Linux and Electrobit Safety Solution works with any Linux.

리눅스를 제공하는 곳은 많고, Elektrobit의 안전 솔루션은 어떤 리눅스와도 함께 동작합니다.

> So that really helps you out.

그게 정말 큰 도움이 되죠.

> And again, as I mentioned, you're also getting a solution that is pre-integrated, so it is going to help you to have your productivity, but without the vendor lock-in on the operating system side.

그리고 앞서 말했듯 사전 통합된 솔루션을 받기 때문에 생산성은 높이면서도 운영체제 쪽 벤더 종속은 피할 수 있습니다.

> I guess also ATOS is open sourcing a lot of what they have.

또 ETAS도 자사 기술의 상당 부분을 오픈소스로 공개하고 있는 걸로 압니다.

> They're very active in S-Core along with Electrobit.

Elektrobit과 함께 Eclipse S-CORE에서 매우 활발히 활동하고 있죠.

> So there is also a move for the ATOS back moving towards open source.

그러니 ETAS 쪽 스택도 오픈소스로 옮겨 가는 흐름이 있습니다.

> So essentially you're getting the advantages with this solution of open source with being able to change various components out to suit your needs while maintaining functional safety.

결국 이 솔루션으로 기능 안전은 유지하면서, 필요에 따라 여러 구성 요소를 교체할 수 있는 오픈소스의 장점을 누리게 됩니다.

> And we have proof points already for functional safety regarding our safety solution for Linux.

그리고 저희 리눅스용 안전 솔루션은 기능 안전에 관한 실증 사례도 이미 갖추고 있습니다.

> So you can be certain that you are not going to have problems

그러니 문제가 없을 거라고 확신하셔도 됩니다.

> regarding ISO 26262 functional safety assessments.

ISO 26262 기능 안전 평가와 관련해서 말이죠.

---

## 6. ETAS가 Eclipse S-CORE에 뛰어든 이유

**[사회자]**

> You mentioned SCORE and ETAS contributing to SCORE and for sure developed EDMS.

S-CORE와, ETAS가 S-CORE에 기여하고 EDMS를 개발했다는 얘기가 나왔는데요.

> Subhash, why did ETAS decided to go into this storage?

Subhash, ETAS는 왜 이 전략을 택했나요?

**[Subhash]**

> Sure, so maybe I can jump in and then Bjorn would also, you know, add much better from the community perspective.

네, 제가 먼저 말씀드리고, 커뮤니티 관점은 Björn이 훨씬 잘 보충해 줄 겁니다.

> So I think when we started this activity last year, in the middle of last year, you know, we were looking at fundamentally on the compute side, we still see the market fragmented.

작년 중반에 이 활동을 시작했을 때, 근본적으로 컴퓨트 쪽 시장이 여전히 파편화돼 있다고 봤습니다.

> Yeah, there's a bunch of solutions out there.

네, 솔루션이 너무 많죠.

> There's still no consolidation that really happened in the last seven to eight years since

지난 7~8년 동안 실질적인 통합은 여전히 일어나지 않았습니다.

> and now HPCs have been introduced.

HPC가 도입된 이후로도 말이죠.

> And we've been discussing with customers, beat customers, how can we get to a point where we can say, okay, where is the shared cost, where can we have shared investment?

그래서 고객들과 '어디서 비용을 나누고, 어디에 공동 투자를 할 수 있을까?'를 논의해 왔습니다.

> And this layer, of course, always has been coming up.

그때마다 항상 이 레이어(미들웨어 기반층)가 거론됐습니다.

> And it's more or less the trigger for the introduction and also seeding of the ESCO initiative itself with the NECLIPSE.

그게 사실상 Eclipse 재단에서 S-CORE 이니셔티브를 시작하고 씨앗을 뿌리게 된 계기입니다.

> NECLIPSE, of course, brings its advantages around governance and so on.

Eclipse는 물론 거버넌스 등에서 장점이 있고요.

> And of course, first as a way of introducing

또 우선은 도입하는 방법으로서,

> development and getting developers on boarded and so on and so forth.

개발을 시작하고 개발자를 끌어들이는 등의 측면에서도 그렇습니다.

> At the same time, we've seen that with ADAS programs, I think the domain knowledge that we have then together, developing that together with Bosch, you know, what's around determinism around data, a throughput and so on.

동시에 ADAS 프로그램에서는 저희가 Bosch와 함께 개발하며 쌓은 도메인 지식, 즉 데이터 처리의 결정성(determinism)이나 처리량 같은 것들이 있다는 걸 봤습니다.

> These specific ADAS kind of capabilities and challenges, we felt it's important to address that in a separate product offering in the market, because the rest of it, which is of course being developed in ESCO and open source, is what we provide through a general purpose profile.

이런 ADAS 특유의 역량과 과제는 별도 제품으로 시장에 내놓는 게 중요하다고 판단했습니다. 나머지, 즉 S-CORE와 오픈소스로 개발되는 부분은 범용 프로파일로 제공하고요.

> So you can also run high performance gateways, body computers with this.

그래서 이걸로 고성능 게이트웨이나 바디 컴퓨터도 구동할 수 있습니다.

> But with the ADAS capability, we wanted to add what's specific to ADAS challenges.

하지만 ADAS 역량 쪽에는 ADAS 과제에 특화된 것을 더하고 싶었습니다.

> they're also you know coming together with electrobit uh we like as more has already mentioned i think uh the cultural aspect that both of us believe in this sort of you know open collaboration this is also really the driver where we said we need to come together and make this into a joint value proposition

그리고 Elektrobit과 함께하게 된 것도, Moritz가 말했듯 두 회사 모두 개방형 협업을 믿는 문화적 측면이 있었고, 이게 '함께 모여 공동 가치 제안으로 만들자'고 한 진짜 원동력이었습니다.

> yeah maybe beyond you can add a little bit more on the community what's uh how is that resonated there

Björn, 커뮤니티 쪽 이야기를 조금 더 해 줄 수 있을까요? 거기서는 반응이 어땠나요?

**[Björn]**

> yeah yeah i think thank you for handing over

네, 넘겨줘서 고맙습니다.

> um a lot of those aspects already mentioned now by isaac and and so i would like to add a few topics in there

많은 부분은 Isaac 등이 이미 말했으니, 몇 가지만 덧붙이겠습니다.

> so we're collaborating and we're doing open source not for the sake of fun of it but for sure we want to generate significant business out of it

저희가 협업하고 오픈소스를 하는 건 재미 삼아서가 아니라, 분명히 의미 있는 사업을 만들어 내기 위해서입니다.

> so no open source greenwashing and saying hey everything is open and everything is is freely accessible

그러니 '전부 공개, 전부 무료'라고 말하는 오픈소스 그린워싱은 아닙니다.

> no the core elements the basic elements that are on a joint foundation these are the things we are sharing in the open source

공동 기반 위에 놓인 핵심·기본 요소, 이것들을 오픈소스로 공유하는 겁니다.

> real being it um electric ElectroBuild putting things on top of a Linux distribution and on top of a Linux operating system, as well as Ethers putting things on top of Eclipse S core as becoming more and more part of our platform and our core product.

Elektrobit이 리눅스 배포판과 리눅스 OS 위에 무언가를 얹고, ETAS가 Eclipse S-CORE 위에 무언가를 얹는 식이죠. S-CORE는 점점 저희 플랫폼과 핵심 제품의 일부가 되고 있습니다.

> So the idea is clear.

그러니 개념은 명확합니다.

> We are having a solid foundation and we are putting additions that differentiates us from others on top of it.

탄탄한 기반을 두고, 그 위에 남들과 차별화되는 요소를 얹는 겁니다.

> And this is what we bring together now as ElectroBuild offering the ground layer and Ethers as offering middleware solutions in this market will

그리고 지금 Elektrobit이 바닥 레이어를, ETAS가 미들웨어 솔루션을 제공하며 이 둘을 합치는 것이,

> created a significant benefit for customers pre-integrated and already already in and running existence

이미 사전 통합되어 실제로 돌아가는 형태로 고객에게 상당한 이점을 만들어 냅니다.

> so we started with edms as the first use case and showcase we show we brought together now but we are extending this

EDMS를 첫 사용 사례이자 쇼케이스로 시작했지만, 이걸 확장해 나가고 있습니다.

> so we see the involvement of eclipse score in the open source project swapping into programs for serious production sooner uh yeah in the moment and coming on the roadmap.

오픈소스 프로젝트인 Eclipse S-CORE가 실제 양산 프로그램에 적용되는 모습이 지금 보이고 있고, 로드맵상으로도 다가오고 있습니다.

> And this is like the headwind that we're taking now and the direction we're taking.

이게 지금 저희가 받고 있는 순풍이자 나아가는 방향입니다.

> So there will be more elements available.

그러니 앞으로 더 많은 요소가 나올 겁니다.

> One of those crucial points, I think, that showed us how this partnership can work is ElectroBits step into S-Core as well.

이 파트너십이 통할 수 있다는 걸 보여 준 결정적 계기 중 하나는 Elektrobit도 S-CORE에 참여했다는 점입니다.

> So nobody was pulling.

누가 억지로 끌어당긴 게 아니었습니다.

> Same goes for the other ones doing operating systems as well.

운영체제를 만드는 다른 회사들도 마찬가지고요.

> But there seems to be a significant benefit of doing so.

그렇게 하는 데 상당한 이점이 있다고 본 거죠.

> So the value proposition of runs on and runs with different solutions in this market is definitely one that is of relevance for the automotive market still and will stay there.

다양한 솔루션 '위에서 돌아가고(runs on), 함께 돌아간다(runs with)'는 가치 제안은 자동차 시장에서 여전히 중요하고, 앞으로도 그럴 겁니다.

---

## 7. 기여와 이득 (Give and Take)

**[사회자]**

> Okay, so this contributing to this escrow, to this open source is a bit of a given tape, right?

그러니까 S-CORE, 즉 오픈소스에 기여하는 건 일종의 주고받기(give and take)라는 거죠?

> As far as I understood it.

제가 이해한 바로는요.

> So this contributing to the product ecosystem.

제품 생태계에 기여하는 거고요.

> Moritz, can you elaborate this a bit more maybe?

Moritz, 조금 더 자세히 설명해 주시겠어요?

> What are we contributing?

우리는 무엇을 기여하고 있나요?

> What is our gain for?

그리고 우리가 얻는 건 뭔가요?

**[Moritz]**

> So when we look at DB's contribution towards escrow, for instance, we are working heavily on Linux as one of the reference operating systems of escrow because we generally feel that

EB의 S-CORE 기여를 예로 들면, 저희는 리눅스를 S-CORE의 레퍼런스 운영체제 중 하나로 만드는 데 집중하고 있습니다. 왜냐하면

> this piece of middleware should run on the best-in-class operating system for safety solutions.

이 미들웨어는 안전 솔루션을 위한 최고 수준의 운영체제 위에서 돌아가야 한다고 보기 때문입니다.

> So it's very natural for us to bring these things together.

그러니 이 둘을 합치는 건 저희에게 아주 자연스럽습니다.

> And at the same time, we always need to look at solutions that we build for our customers as a holistic thing.

동시에 고객을 위해 만드는 솔루션은 항상 전체적인 관점으로 봐야 합니다.

> So when we think ecosystems as Electrobit, especially in the scope of Linux, well, next thing is, okay, what's the chip support for these things?

Elektrobit이 리눅스 범위에서 생태계를 생각하면, 다음 질문은 '이걸 지원하는 칩은 뭐지?'입니다.

> This is where we are heavily investing actually in making attractive solutions that come without a whole lot of

그래서 저희는 큰 수고 없이 쓸 수 있는 매력적인 솔루션을 만드는 데 많이 투자하고 있습니다.

> work for our customers.

고객 입장에서 일이 많이 들지 않도록요.

> Going towards how do we span the gap between different functional domains, I mean when we look at okay, can something like Corvus Linux for Safe Applications work for cockpit safety or for tail failure rendering for instance without needing to do yet another switch.

또 서로 다른 기능 도메인 간의 간극을 어떻게 메울지도 고민합니다. 예를 들어 EB corbos Linux for Safety Applications가 또 다른 전환 없이 콕핏 안전 기능이나 경고등(telltale) 렌더링에도 쓰일 수 있을까 하는 것이죠.

> So we try to connect these solutions together for whatever our customers really need to have in the market.

그래서 고객이 시장에서 실제로 필요로 하는 것을 위해 이런 솔루션들을 연결하려 합니다.

> So as Bjorn rightfully said it's connecting, it's a works-on works-with perspective to build a compelling overall solution.

Björn이 정확히 말했듯이, 핵심은 연결이고, 설득력 있는 전체 솔루션을 만들기 위한 'works-on, works-with' 관점입니다.

> So what is an offering that we can offer not only to the automotive market but also where is it attractive and adjacent market with similar requirements.

자동차 시장뿐 아니라 요구사항이 비슷한 인접 시장에서도 매력적인 제품이 무엇인지 보는 거죠.

> And this is where we still feel that that

그리고 바로 이 지점에서 저희는 여전히

> ecosystem connection is extremely important for any activity to bring such a solution to the market.

그런 솔루션을 시장에 내놓으려면 생태계 간 연결이 무엇보다 중요하다고 느낍니다.

---

## 8. 단기 전망

**[사회자]**

> Thanks a lot.

감사합니다.

> Now a bit of a small future, maybe near future outlook.

이제 가까운 미래를 조금 내다보죠.

> Where do you think is this partnership taking place?

이 파트너십은 어디로 향하고 있다고 보세요?

> Where do you see us in the next months?

앞으로 몇 달 안에 우리는 어디에 있을까요?

**[Björn]**

> Actually the overall support from market or pull from market or recognition on the market and on this partnership is really incredible.

사실 이 파트너십에 대한 시장의 전반적인 지지, 수요, 관심은 정말 놀라울 정도입니다.

> So we launched communication about this at the JSAE in Tokyo a few months ago and

몇 달 전 도쿄의 JSAE(자동차기술전)에서 이 소식을 처음 발표했는데,

> and it was like really, what?

반응이 '진짜? 뭐라고?' 하는 식이었습니다.

> Why are they, one of those headlines was a partnership that shouldn't exist, something was written in Japanese, I think.

'왜 저 두 회사가?' 하는 반응이었고, 어떤 헤드라인은 일본어로 '존재해서는 안 될 파트너십' 같은 말을 썼던 걸로 기억합니다.

> And this is exactly the fun part about it.

바로 그게 재미있는 부분입니다.

> So I think showing this world of frenemies and cooperation in our days and in real life scenarios is where we were heading to.

오늘날의 '프레너미(친구이자 적)'와 협력의 세계를 실제 시나리오로 보여 주는 것, 그게 저희가 지향한 바입니다.

> We started with EDMS, which is our solution for the ADAS, AD profile.

저희는 ADAS·자율주행(AD) 프로파일용 솔루션인 EDMS로 시작했습니다.

> with capabilities for deterministic recompute solutions as one of those topics.

결정적(deterministic) 연산 기능 같은 것이 그 주제 중 하나고요.

> We're clearly heading to further integration on the S-Core-based platform we are developing, which is the biggest of a platform suite, where this profile on a basic level is going deeper.

저희는 개발 중인 S-CORE 기반 플랫폼, 즉 더 큰 플랫폼 제품군과의 추가 통합을 분명히 지향하고 있고, 이 프로파일은 기본 수준에서 더 깊어질 겁니다.

> And we are having, based on JSAE and further communication, a lot of customer discussions right now.

그리고 JSAE 발표와 이후 홍보 덕분에 지금 고객 논의가 아주 많습니다.

> So what are you doing?

'뭘 하는 건가요?

> How can you deliver?

어떻게 공급하나요?

> Who is there?

누가 참여하나요?

> Who is in lead for doing so?

누가 주도하나요?' 같은 질문들이죠.

> So this is really like something we are now bringing to the market together, pitching together to customers for future success.

그래서 이건 지금 저희가 함께 시장에 내놓고, 앞으로의 성공을 위해 고객에게 함께 제안하고 있는 것입니다.

> So hopefully on the road would be the answer that I would love to give sooner than later as goal for this partnership.

이 파트너십의 목표로 제가 하루빨리 드리고 싶은 답은 '실제 도로 위에 있다'입니다.

> But coming from EDMS and ADAS AD use cases in the beginning, we are extending to further domains and further integration with

다만 처음엔 EDMS와 ADAS·AD 사용 사례에서 출발해, 더 많은 도메인으로, 그리고

> our different offerings this would be the crisp answer.

저희의 다른 제품들과의 추가 통합으로 확장하고 있다, 이게 간단한 답입니다.

**[사회자]**

> Thanks a lot. Do you want to add something there?

감사합니다. 덧붙이실 말씀 있나요?

**[Moritz]**

> I think it sums it up pretty well.

잘 정리됐다고 생각합니다.

> I mean in the end the resonance from the announcement this fall has been enormous and we actually got the same kind of response that that element of the price thing okay why the hell you too

결국 이번 가을 발표에 대한 반향은 엄청났고, 저희도 똑같은 놀라움의 반응, '대체 왜 당신들 둘이?' 같은 반응을 받았습니다.

> but I think as we've discussed here today it's actually a natural

하지만 오늘 이야기했듯 이건 사실 자연스러운 일입니다.

> yes we are in competition for some fields and obviously don't collaborate on these.

네, 일부 분야에서는 경쟁하고 있고, 그 분야에서는 당연히 협업하지 않습니다.

> But for the ones where we have complimentary offering, it's natural to actually offer the best available solution to a customer.

하지만 서로 보완적인 제품이 있는 분야라면, 고객에게 가능한 최고의 솔루션을 제공하는 게 자연스럽죠.

> So it shouldn't really come as too much of a surprise in the market, because we essentially look at, okay, what good data solutions platform, software for data solutions is available, what attractive choices in the context of going towards more openness, more collaboration, more open source in terms of operating systems.

그러니 시장이 그렇게 놀랄 일은 아닙니다. 결국 저희가 보는 건 '좋은 ADAS 솔루션 플랫폼과 소프트웨어는 무엇인가, 그리고 운영체제 측면에서 더 개방적이고 협업적이며 오픈소스로 가는 흐름 속에서 매력적인 선택지는 무엇인가'이니까요.

> So Linux is the obvious choice.

그렇다면 리눅스는 당연한 선택입니다.

> And this is where it just comes fairly natural actually to have started this conversation here for the next steps, clearly next step SOP.

그래서 이 대화를 시작한 건 꽤 자연스러운 일이었고, 다음 단계는 분명히 SOP입니다.

**[사회자]**

> I'm happy to see this, knowing that it is a bit stressful to bring a project into an SOP, especially a multi-party project, but always a challenge looking forward to it.

프로젝트를 SOP까지, 특히 여러 회사가 참여하는 프로젝트를 끌고 가는 게 꽤 스트레스라는 걸 알지만, 그래도 이런 모습을 보니 기쁩니다. 늘 기대되는 도전이죠.

---

## 9. 5년 뒤 ADAS 플랫폼 전망

**[사회자]**

> Now, this is kind of the future we want to control, right?

이건 우리가 통제하고 싶은 미래 이야기였죠?

> What is our offering?

우리 제품이 뭐고,

> How do we go?

어떻게 나아갈지.

> But how do you think that the market is developing?

그런데 시장은 어떻게 발전할 거라고 보시나요?

> Subhash, what do you think an Addis platform looks like in five years?

Subhash, 5년 뒤 ADAS 플랫폼은 어떤 모습일까요?

> And I mean, you can only be wrong, right?

뭐, 틀릴 수밖에 없는 질문이긴 하죠?

> We all know this, but let's hear it from now.

다들 알지만, 그래도 지금 시점의 생각을 들어 보죠.

**[Subhash]**

> Subhash can be right.

(웃으며) 저는 맞힐 수도 있습니다.

> I think since I started in this area almost a decade ago in urban artists, and most of the time, at least what we've seen, it's been true with just a time shift delay of maybe two years.

거의 10년 전 이 분야(ADAS)를 시작한 이후로, 적어도 저희가 본 바로는 예측이 대부분 맞았습니다. 다만 2년 정도 늦게 실현됐을 뿐이죠.

> So I think that still fits to at least the prognosis.

그러니 예측 자체는 여전히 들어맞는다고 봅니다.

> But I think, let's start with some basics.

기본부터 시작해 보죠.

> I think one of the things that you're seeing right now is

지금 보이는 현상 중 하나는

> that the introduction of centralized vehicle architecture itself is being delayed.

중앙집중형 차량 아키텍처의 도입 자체가 늦어지고 있다는 점입니다.

> So this is clearly due to cost pressure.

이건 분명히 비용 압박 때문입니다.

> OEMs want to still hang on to their existing E-architectures to still try and get the best out of it.

완성차(OEM)들은 기존 전기·전자(E/E) 아키텍처를 붙들고 최대한 활용하려 합니다.

> But at the same time have a managed transition.

동시에 관리된 방식으로 전환하려 하고요.

> So the whole big bang revamping of E-architectures, we've seen examples in the market.

E/E 아키텍처를 한 번에 확 갈아엎는 '빅뱅' 방식의 사례도 시장에 있었지만,

> This has really not taken off.

그건 제대로 자리 잡지 못했습니다.

> Greenfield happens, but Greenfield really happens.

완전히 새로 시작하는(그린필드) 경우도 있지만, 정말 드뭅니다.

> These are the exceptions to the rule.

예외적인 경우죠.

> So this is one trend or one, let's say, boundary condition that's impacting what the future trend looks like.

이게 미래 트렌드에 영향을 주는 하나의 흐름, 혹은 전제 조건입니다.

> The second thing is I think ADAS is slowly getting more and more democratized.

두 번째는 ADAS가 점점 대중화되고 있다는 점입니다.

> So this is, I think, something which, and this is perhaps also one of the trends,

이것도 아마 트렌드 중 하나인데,

> why we see this partnership supporting this ADAS democratization, which means it has to reach mass market, the adoption of L2, L2++ systems eventually.

저희가 이 파트너십이 ADAS 대중화를 뒷받침한다고 보는 이유입니다. 대중화란 결국 대중 시장에 도달해 L2, L2++ 시스템이 널리 채택된다는 뜻이죠.

> So we see this partnership and the solution that we have to offer together within the next various operating system and the necessary ADAS capabilities will support this sort of adoption as well.

이 파트너십과, 운영체제 및 필요한 ADAS 역량을 묶어 함께 제공하는 솔루션이 이런 채택을 뒷받침할 거라고 봅니다.

> The third aspect is of course regionalization.

세 번째는 물론 지역화입니다.

> So this is depending on how this gets adopted in various regions.

지역마다 어떻게 채택되느냐에 따라 달라지죠.

> Of course there are leaders right now in the global landscape, technology leaders but also adoption leaders.

현재 글로벌 판도에는 기술을 선도하는 곳도 있고, 채택을 선도하는 곳도 있습니다.

> So that's the difference as well where adoption takes place first and where maybe technology is driving more or less state of the art definition.

즉 채택이 먼저 일어나는 곳과, 기술이 최신 기준을 정의하는 곳이 다를 수 있다는 차이죠.

> So these are some aspects which we are looking at.

이런 측면들을 보고 있습니다.

> I mean it is the three things that I could see right now where we see this going into the future.

지금 제가 볼 수 있는 미래의 방향은 이 세 가지입니다.

> What we are looking for is, of course, the first proof point, as Moritz already mentioned, to show this with an SOP.

저희가 기대하는 건 물론 Moritz가 말한 대로 SOP로 증명하는 첫 실증 사례입니다.

> And frankly, you know, in the past, OEMs have sometimes asked us, why don't you collaborate with X, Y, and Z?

솔직히 예전에 OEM들이 '왜 X, Y, Z와 협업하지 않느냐'고 묻곤 했습니다.

> Now when we go and tell them, you'll be actually collaborating with Electrobit, they are quite surprised.

이제 '저희 Elektrobit과 협업합니다'라고 말하면 꽤 놀라더군요.

> Okay, what's happening there and what are you doing?

'무슨 일이 있는 거냐, 뭘 하는 거냐' 하고요.

> So this is, I think, an effect which we also want to carry forward.

이 효과를 계속 이어 가고 싶습니다.

> And as Dion already highlighted, we start with the data side, but there's no reason why we should stop and not go ahead with our general purpose profile into other HPC areas as well.

그리고 Björn이 강조했듯 ADAS 쪽부터 시작하지만, 거기서 멈추지 않고 범용 프로파일로 다른 HPC 영역까지 나아가지 않을 이유가 없습니다.

---

## 10. 경쟁 관계에 대한 Q&A, 공동 데모

**[사회자]**

> I mean, this this point also we have this as a question, right?

이 부분은 질문으로도 들어왔네요.

> The competitive competition between electromedinators and now they are working close together.

Elektrobit과 ETAS는 경쟁 관계인데 이제 긴밀히 협력한다는 점이요.

> So this is really seems like astonishing people.

사람들이 정말 놀라는 것 같습니다.

> I think we've we've already commented on that fairly enough.

이미 충분히 이야기한 것 같지만,

> If someone wants to comment on it again, please feel free.

다시 한마디 하실 분이 있으면 편하게 해 주세요.

> I know that there is also a joint demo plan, something right?

공동 데모 계획도 있다고 알고 있는데, 맞죠?

**[Subhash]**

> If you allow me, maybe I just want to comment on that question as well, because I think it's it's rightly recognized.

괜찮다면 그 질문에 한마디 하고 싶습니다. 아주 정확한 지적이라서요.

> So firstly, thank you for recognizing that our parent companies are basically competitors, very fierce competitors.

먼저, 저희 모회사들이 사실상 경쟁사, 그것도 아주 치열한 경쟁사라는 점을 짚어 주셔서 감사합니다.

> I think that's also the sort of

그런데 그게 또한

> the freedom we have, both the software companies within the respective groups, we have this freedom to also address the rest of the market, right?

저희가 가진 자유이기도 합니다. 각 그룹 안의 소프트웨어 회사로서, 두 회사 모두 그룹 밖의 나머지 시장까지 공략할 자유가 있죠.

> So we also provide our solutions, not just in this case, you know, what we're talking about, but also the rest of our portfolio from ETAs.

그래서 지금 얘기하는 이 건뿐 아니라 ETAS의 나머지 포트폴리오도 시장에 공급합니다.

> We supply this also to Bosch's competitors and I'm sure E-electrobit does this also likewise in the market, right?

Bosch의 경쟁사에도 공급하고, Elektrobit도 분명 시장에서 마찬가지로 하고 있을 겁니다.

> And in this case, we decided that on the compute side, like I said, the market has not yet consolidated on a certain platform.

이번 경우에는, 말씀드린 것처럼 컴퓨트 쪽 시장이 아직 특정 플랫폼으로 통합되지 않았다고 판단했습니다.

> And right now we still see the opportunity and the gap where we can bundle our assets, Electrobits, Linux for safety applications and our EDAs capabilities on the middleware side.

그리고 지금은 Elektrobit의 Linux for Safety Applications와 저희의 미들웨어 측 ADAS 역량을 묶을 수 있는 기회와 빈틈이 여전히 있다고 봅니다.

> These are the two complementary assets we are bringing together and offering to the market jointly.

이 두 보완적 자산을 합쳐 시장에 공동으로 내놓는 것입니다.

**[사회자 / 패널]**

> Very cool.

아주 좋네요.

> Of course, yes, we will demo this.

물론 데모도 합니다.

> So we'll be at ETAS Connections on the 20th of October in Stuttgart, showcasing joint solutions.

10월 20일 슈투트가르트에서 열리는 ETAS Connections에서 공동 솔루션을 선보일 예정입니다.

> So if you're around, if you want to travel to Stuttgart precisely for that, which I could very well understand, please register, come over and let's have a discussion on this.

근처에 계시거나, 바로 이걸 보러 슈투트가르트까지 오실 생각이라면(충분히 이해합니다) 등록하시고 오셔서 함께 이야기 나눠요.

> So we'd really like to see this and just discuss the details with you.

꼭 직접 보시고 세부 사항을 함께 논의하고 싶습니다.

> I think it will be on site to be very precise.

정확히 말하면 현장에서 진행될 겁니다.

> So you will meet known faces.

그러니 아는 얼굴들을 만나실 거예요.

> So much will be around as well.

Subhash도 그 자리에 있을 겁니다.

> So take the chance.

기회를 잡으세요.

> I just repeat, it's the ETAs Connections or how is it called?

다시 말하면, 행사 이름이 ETAS Connections, 맞나요?

> ETAs Connections, 20th of October in Stuttgart. Exactly.

ETAS Connections, 10월 20일, 슈투트가르트. 맞습니다.

> Alright, people should be able to Google it and then click through the agenda.

좋아요, 검색하시면 아젠다를 확인하실 수 있을 겁니다.

---

## 11. 라이트닝 라운드 (마무리 한마디)

**[사회자]**

> Perfect. Thanks a lot guys.

좋습니다. 모두 감사합니다.

> Coming a bit closer to the end now, I would love to have a bit of a lightning round from each of you.

이제 마무리에 가까워졌으니, 한 분씩 짧게 한마디씩 듣고 싶습니다.

> I'm not daring to tell you we have some more time, so please still keep it a bit short, although we have a bit time.

시간이 조금 남았다고 말하긴 조심스럽네요. 시간은 있지만 그래도 짧게 부탁드립니다.

> I don't know who wants to start. Volunteers first, please.

누가 먼저 하실까요? 자원자 먼저요.

**[Björn]**

> Yeah, we start by.

네, 제가 시작하죠.

> I think so, cooperation and non-exclusivity is the new standard that we all have to face and deal with.

협력과 비독점성(non-exclusivity)이 우리 모두가 마주하고 다뤄야 할 새로운 표준이라고 생각합니다.

> And if we do this even in open source, then I'm more than happy on the development.

그걸 오픈소스로까지 한다면, 저는 이 흐름이 더없이 반갑습니다.

**[Isaac]**

> Yeah, so I mean for me this whole thing is super exciting because you know when bringing up the Linux for safety applications it really was the first operating system coming from open source that you could use for functional safety in automotive.

저에게 이 모든 게 아주 흥미로운 이유는, Linux for Safety Applications를 내놓았을 때 그것이 자동차 기능 안전에 쓸 수 있는 최초의 오픈소스 기반 운영체제였기 때문입니다.

> It's something the industry had been asking for for years so it was really kind of a holy grail.

업계가 몇 년 동안 요구해 온 것이라, 정말 '성배' 같은 것이었죠.

> But of course as more had said before an operating system is just that right and what customers really want is is.

하지만 Moritz가 말했듯 운영체제는 운영체제일 뿐이고, 고객이 진짜 원하는 건

> have the functionality for their application they want to have a whole stack

애플리케이션에 필요한 기능, 즉 전체 스택입니다.

> so really putting putting edms there to make the stack complete is is a really is a really great thing from from electrobids point of view and from my point of view

그래서 EDMS를 얹어 스택을 완성하는 건 Elektrobit 입장에서도, 제 개인적으로도 정말 훌륭한 일입니다.

**[Moritz]**

> thanks a lot more days i think uh this partnership is actually really about um getting the attention of our customers back on the topics that they really care about creating good functionality

(사회자: 고마워요. Moritz?) 이 파트너십은 결국 고객의 관심을 그들이 진짜 중요하게 여기는 주제, 즉 좋은 기능을 만드는 일로 되돌려 놓는 것이라고 봅니다.

> We don't want our customers to spend a whole lot of time on integrating things, for carrying the risk for integrating things where they may not be sure whether they actually fit together or not, but actually focus on differentiating software.

고객이 통합 작업에 많은 시간을 쓰거나, 서로 맞을지 확신도 없는 것들을 통합하는 리스크를 떠안기보다, 차별화 소프트웨어에 집중하길 바랍니다.

> And they also typically don't want to get into a lock-in.

그리고 고객들은 대개 종속(lock-in)되는 것도 원하지 않죠.

> So this is why we really feel that building on top of open solutions is the way to go, so that they can actually appreciate the benefits of pre-integration, but still really focus on the functionality with an ease of mind.

그래서 개방형 솔루션 위에 구축하는 게 맞는 길이라고 봅니다. 사전 통합의 이점을 누리면서도 마음 편히 기능에 집중할 수 있으니까요.

> And this is for me really the key point.

저에게는 이게 핵심입니다.

> innovation into automotive out quickly without getting into any traps

어떤 함정에도 빠지지 않고 자동차에 혁신을 빠르게 내놓는 것.

**[Subhash]**

> i'll rob it up so yeah i think from my side i mean the market is extremely uh tight on budgets

제가 마무리하죠. 제 입장에서 보면 시장은 예산이 극도로 빠듯합니다.

> i think every i'm sure everybody who's talking to oems knows what this uh what sort of discussion that conversation we are having

OEM과 이야기해 본 분이라면 다들 어떤 대화가 오가는지 아실 겁니다.

> um and i think you know the the oems are looking for partners who will still exist at SOP and beyond.

그리고 OEM들은 SOP 시점과 그 이후에도 살아남아 있을 파트너를 찾고 있습니다.

> Yeah, and I think this is one of the main drivers also why we've come together to put together those complementary assets and show the show and demonstrate this, let's say, joint force to our customers and make sure that those SOPs are not endangered.

이게 저희가 보완적 자산을 하나로 모아 고객에게 이른바 '연합 전력'을 보여 주고, 그들의 SOP가 위태로워지지 않도록 하려는 주된 이유 중 하나입니다.

**[사회자]**

> Perfect. Thanks a lot, guys.

완벽합니다. 모두 감사합니다.

> This seems like kind of a perfect word of an ending, right?

마무리로 딱 좋은 말이네요.

> So, gentlemen, if you don't mind, I would say it's a wrap.

여러분, 괜찮으시다면 여기서 마치겠습니다.

> Thanks a lot for this nice conversation.

좋은 대화 감사합니다.

> Thanks a lot for all of you contributing to it.

참여해 주신 모든 분께 감사드립니다.

> We gained a bit of a time.

시간이 조금 남았네요.

> We are faster than expected.

예상보다 빨리 끝났습니다.

> That is definitely not something I did expect, but I'm really looking into this partnership.

정말 예상 못 했지만, 이 파트너십이 정말 기대됩니다.

> Let's see you then at the demo in Stuttgart.

슈투트가르트 데모에서 뵙겠습니다.

> Thanks a lot, everyone. Bye.

모두 감사합니다. 안녕히 계세요.

**[패널]**

> Thank you. Thank you, Hunter. Thank you for joining us. Thank you.

감사합니다. 고마워요, Anton. 참석해 주셔서 감사합니다. 감사합니다.
