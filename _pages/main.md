---
layout: single
permalink: /
redirect_from:
  - /about/
author_profile: true
classes: wide
description: "Chanho Kim (김찬호) is an M.S./Ph.D. student at UNIST AIGS and a researcher at the UNIST Vision and Learning Lab, focusing on 3D human and hand reconstruction, pose estimation, and vision-language-action models."
---
<div class="home" markdown="0">
<section id="about">
<h2>About Me</h2>
<div class="about-card">
<p class="lead">
I am a combined <strong>M.S./Ph.D.</strong> student at the
<a href="https://aigs.unist.ac.kr/">Artificial Intelligence Graduate School (AIGS)</a>,
<strong>Ulsan National Institute of Science and Technology (UNIST)</strong>,
working in the <a href="https://vision.unist.ac.kr/">UNIST Vision and Learning Lab (UVLL)</a>
under <a href="https://sites.google.com/site/bsrvision00/">Prof. Seungryul Baek</a>.
</p>
<p>
My research focuses on <strong>3D computer vision</strong>, in particular fast methods that reconstruct animatable 3D hands and humans from as little as a single image. I am also interested in vision-language models and vision-language-action learning.
</p>
<p>
I received my <strong>B.S.</strong> in <a href="https://computer.knu.ac.kr/">Computer Science and Engineering</a> from <strong>Kyungpook National University</strong>.
</p>
<div class="interests">
  <span class="interests-label">Research interests</span>
  <ul class="interest-grid">
    <li>3D Human &amp; Hand Reconstruction</li>
    <li>3D Pose &amp; Mesh Estimation</li>
    <li>Vision-Language Models</li>
    <li>Vision-Language-Action Models</li>
  </ul>
</div>
<!-- On phones the sidebar links are folded behind "Follow"; this row shows them inline there -->
<div class="about-links">
  <a href="mailto:coolho1129@unist.ac.kr">{% include social-icon.html name="email" %}Email</a>
  <a href="https://scholar.google.com/citations?user=SW-_ah8AAAAJ&amp;hl=ko">{% include social-icon.html name="scholar" %}Google Scholar</a>
  <a href="https://github.com/coolho1129">{% include social-icon.html name="github" %}GitHub</a>
  <a href="https://www.linkedin.com/in/chanho-kim-891a542a2">{% include social-icon.html name="linkedin" %}LinkedIn</a>
  <a href="/files/Chanho_Kim_CV.pdf">{% include social-icon.html name="cv" %}CV</a>
</div>
</div>
</section>
<section id="news">
<h2>News</h2>
<ul class="news">
<li><span class="date">Sep 2026</span><span class="news-text">🎉 Our paper <strong>"InstantHand: Feed-Forward 3D Gaussian Splatting for Animatable Hand Avatar Reconstruction from a Single Image"</strong> has been accepted to <span class="nowrap"><span class="venue-pill venue-pill--intl">NeurIPS 2026</span>.</span></span></li>
<li><span class="date">Sep 2025</span><span class="news-text">🎓 Started the combined M.S./Ph.D. program at <strong>UNIST AIGS</strong>.</span></li>
</ul>
</section>
<section id="publications">
<h2>Publications</h2>
<h3>International Conferences</h3>
<article class="pub pub--featured">
  <a class="pub-thumb" href="https://coolho1129.github.io/InstantHand-page/" tabindex="-1">
    <img src="/images/pubs/instanthand.webp" loading="lazy" width="960" height="280" alt="A single input hand image, one forward pass, and the reconstructed canonical 3D Gaussian hand avatar rotating.">
  </a>
  <div class="pub-body">
    <div class="pub-meta"><span class="venue-pill venue-pill--intl">NeurIPS 2026</span><span class="pub-when"><span class="pub-place">{% include social-icon.html name="pin" %}Sydney, Australia</span><span class="pub-date">Dec 2026</span></span></div>
    <h4 class="pub-title"><a href="https://coolho1129.github.io/InstantHand-page/">InstantHand: Feed-Forward 3D Gaussian Splatting for Animatable Hand Avatar Reconstruction from a Single Image</a></h4>
    <p class="pub-authors"><strong>Chanho Kim</strong>, Muhammad Salman Ali, Kyeonghwan Gwak, Muhammad Shaheryar, Incheol Park, Jeongwan On, Seungryul Baek*</p>
    <div class="pub-links">
      <!-- When the paper is public, turn this span into a link: change <span ... aria-disabled="true"> to <a class="pub-btn" href="PAPER_URL">, drop "is-pending" and the <small>, and close with </a>. -->
      <span class="pub-btn is-pending" aria-disabled="true">{% include social-icon.html name="paper" %}Paper <small>soon</small></span>
      <a class="pub-btn" href="https://coolho1129.github.io/InstantHand-page/">{% include social-icon.html name="globe" %}Project</a>
      <a class="pub-btn" href="https://github.com/coolho1129/InstantHand">{% include social-icon.html name="github" %}Code</a>
    </div>
  </div>
</article>

<h3>Domestic Journals</h3>
<div class="card">
<article class="pub-row" id="pub-vtc-journal">
  <div class="pub-meta"><span class="venue-pill">KCI</span><span class="pub-date">Oct 2024</span></div>
  <h4 class="pub-title">도로교통량 조사를 위한 12종 차종 분류 방법</h4>
  <p class="pub-en">Vehicle Type Classification Method for Road Traffic Surveys</p>
  <p class="pub-authors">Mi-Seon Kang, <strong>Chan-Ho Kim</strong>, Pyong-Kun Kim*</p>
  <p class="pub-venue"><em>IEMEK Journal of Embedded Systems and Applications</em>, Vol. 19, No. 5, pp. 227–234</p>
  <p class="pub-related">Conference version at <a href="#pub-vtc-iset">ISET 2024</a> <span class="award-tag"><span aria-hidden="true">🏆</span> Best Paper Presentation Award</span></p>
  <div class="pub-links">
    <a class="pub-btn" href="https://doi.org/10.14372/IEMEK.2024.19.5.227">{% include social-icon.html name="paper" %}Paper</a>
    <a class="pub-btn" href="https://github.com/coolho1129/Vehicle-Type-Classification-Method-for-Road-Traffic-Surveys">{% include social-icon.html name="github" %}Code</a>
  </div>
</article>
</div>

<h3>Domestic Conferences</h3>
<div class="card">
<article class="pub-row">
  <div class="pub-meta"><span class="venue-pill">IPIU 2026</span><span class="pub-date">Feb 2026</span></div>
  <h4 class="pub-title">실시간 손 메시 복원을 위한 미분 가능한 고속 해석적 병렬 역기구학 모듈의 설계 및 최적화</h4>
  <p class="pub-en">Design and Optimization of a Fast, Differentiable, and Parallel Analytical Inverse Kinematics Module for Real-Time Hand Mesh Reconstruction</p>
  <p class="pub-authors"><strong>Chanho Kim</strong>, Seungryul Baek*</p>
</article>
<article class="pub-row">
  <div class="pub-meta"><span class="venue-pill">KICS 2024</span><span class="pub-date">Jun 2024</span></div>
  <h4 class="pub-title">비전 기술을 활용한 의료용 침대 낙상 방지 기법</h4>
  <p class="pub-en">Fall Prevention Techniques for Medical Beds Using Vision Technology</p>
  <p class="pub-authors"><strong>Chan-Ho Kim</strong>, Eunji Kim, Jaehyeon Ha, Chaewon Moon, Dongkyun Kim*</p>
</article>
<article class="pub-row" id="pub-vtc-iset">
  <div class="pub-meta"><span class="venue-pill">ISET 2024</span><span class="award-tag"><span aria-hidden="true">🏆</span> Best Paper Presentation Award</span><span class="pub-date">May 2024</span></div>
  <h4 class="pub-title">도로교통량 조사를 위한 12종 차종 분류 방법</h4>
  <p class="pub-en">Vehicle Type Classification Method for Road Traffic Surveys</p>
  <p class="pub-authors"><strong>Chan-Ho Kim</strong><sup>†</sup>, Mi-Seon Kang<sup>†</sup>, Pyong-Kun Kim*</p>
  <p class="pub-related">Conference version of the <a href="#pub-vtc-journal">KCI journal paper</a></p>
</article>
<article class="pub-row">
  <div class="pub-meta"><span class="venue-pill">CEIC 2023</span><span class="pub-date">Dec 2023</span></div>
  <h4 class="pub-title">메타버스를 위한 실감형 미디어 기반 데이터셋의 리타겟팅 적용 연구</h4>
  <p class="pub-en">A Study on Retargeting Via Realistic Media-based Datasets for Metaverse</p>
  <p class="pub-authors">Dong-hwi Kim, Aro Kim, Dong-hun Lee, <strong>Chanho Kim</strong>, Eunji Kim, Chaewon Moon, Geonah Kim, Sang-hyo Park*</p>
</article>
</div>
<p class="pub-legend">* Corresponding author&nbsp;&nbsp;&nbsp;† Equal contribution</p>
</section>
<section id="education">
<h2>Education</h2>
<div class="orgs">
<div class="org">
  <div class="org-logo"><img src="/images/logos/unist.png" alt="UNIST logo" width="240" height="240"></div>
  <div class="org-main">
    <div class="org-name">Ulsan National Institute of Science and Technology (UNIST)</div>
    <div class="org-role">M.S./Ph.D. in Artificial Intelligence<span class="org-sep">·</span>Ulsan, South Korea</div>
    <div class="org-detail">Artificial Intelligence Graduate School (AIGS)</div>
  </div>
  <div class="org-date">Sep 2025 – Present</div>
</div>
<div class="org">
  <div class="org-logo"><img src="/images/logos/knu.png" alt="Kyungpook National University logo" width="240" height="240"></div>
  <div class="org-main">
    <div class="org-name">Kyungpook National University</div>
    <div class="org-role">B.S. in Computer Science and Engineering<span class="org-sep">·</span>Daegu, South Korea</div>
  </div>
  <div class="org-date">Mar 2021 – Feb 2025</div>
</div>
</div>
</section>
<section id="experience">
<h2>Research Experience</h2>
<div class="orgs">
<div class="org">
  <div class="org-logo"><img src="/images/logos/unist.png" alt="UNIST logo" width="240" height="240"></div>
  <div class="org-main">
    <div class="org-name">UNIST Vision and Learning Lab (UVLL)</div>
    <div class="org-role">Graduate Researcher / Assistant Researcher<span class="org-sep">·</span>Ulsan, South Korea</div>
    <div class="org-detail">Advisor: <a href="https://sites.google.com/site/bsrvision00/">Prof. Seungryul Baek</a></div>
  </div>
  <div class="org-date">May 2025 – Present</div>
</div>
<div class="org">
  <div class="org-logo"><img src="/images/logos/etri.png" alt="ETRI logo" width="240" height="240"></div>
  <div class="org-main">
    <div class="org-name"><a href="https://www.etri.re.kr/kor/sub6/sub6_01020101.etri?departCode=150&amp;departInfoCode=265">AI Infrastructure Lab</a>, ETRI</div>
    <div class="org-role">Research Intern<span class="org-sep">·</span>Daegu, South Korea</div>
    <div class="org-detail">Mentor: <a href="https://scholar.google.com/citations?user=5xetTUwAAAAJ">Pyong-Kun Kim</a></div>
  </div>
  <div class="org-date">Jan 2024 – Feb 2024</div>
</div>
<div class="org">
  <div class="org-logo"><img src="/images/logos/knu.png" alt="Kyungpook National University logo" width="240" height="240"></div>
  <div class="org-main">
    <div class="org-name"><a href="https://sites.google.com/view/k-vislab">Vision &amp; Intelligent Systems Lab (VIS Lab)</a>, Kyungpook National University</div>
    <div class="org-role">Undergraduate Researcher<span class="org-sep">·</span>Daegu, South Korea</div>
    <div class="org-detail">Advisor: <a href="https://sites.google.com/site/jongtaeklee/">Prof. Jong Taek Lee</a></div>
  </div>
  <div class="org-date">Jul 2023 – Dec 2023</div>
</div>
</div>
</section>
<section id="awards">
<h2>Awards &amp; Honors</h2>
<div class="orgs">
<div class="org">
  <div class="award-icon"><span aria-hidden="true">🏆</span></div>
  <div class="org-main">
    <div class="org-name">Best Paper Presentation Award</div>
    <div class="org-role">The 19th IeMeK Symposium on Embedded Technology (ISET 2024)</div>
    <div class="org-detail">Institute of Embedded Engineering of Korea (IeMeK)</div>
  </div>
  <div class="org-date">May 2024</div>
</div>
<div class="org">
  <div class="award-icon"><span aria-hidden="true">🥈</span></div>
  <div class="org-main">
    <div class="org-name">Excellence Award</div>
    <div class="org-role">Daegyeong SW Industry-Academia Project Competition</div>
    <div class="org-detail">Software Education Institute, Kyungpook National University</div>
  </div>
  <div class="org-date">Dec 2023</div>
</div>
<div class="org">
  <div class="award-icon"><span aria-hidden="true">🥉</span></div>
  <div class="org-main">
    <div class="org-name">Encouragement Award</div>
    <div class="org-role">Daegyeong University Student AI Programming Competition</div>
    <div class="org-detail">Software Education Institute, Kyungpook National University</div>
  </div>
  <div class="org-date">Dec 2023</div>
</div>
<div class="org">
  <div class="award-icon"><span aria-hidden="true">🥇</span></div>
  <div class="org-main">
    <div class="org-name">Top Excellence Award</div>
    <div class="org-role">School of Computer Science and Engineering Startup Achievement Competition</div>
    <div class="org-detail">School of Computer Science and Engineering, Kyungpook National University</div>
  </div>
  <div class="org-date">Nov 2022</div>
</div>
</div>
</section>
</div>
