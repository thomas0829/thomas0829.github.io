---
layout: cv
title: "履歷"
permalink: /zh/cv/
author_profile: false
lang: zh
lang_url: /cv/
---

<div class="cv-header">
  <h1>李英群</h1>
  <div class="cv-header__subtitle">華盛頓大學 電機與電腦工程碩士</div>
  <div class="cv-header__contact">
    <a href="mailto:thomas910829@gmail.com"><i class="fas fa-envelope"></i> thomas910829@gmail.com</a>
    <a href="https://github.com/thomas0829"><i class="fab fa-github"></i> GitHub</a>
    <a href="https://www.linkedin.com/in/thomas0829/"><i class="fab fa-linkedin"></i> LinkedIn</a>
    <a href="tel:+12065791447"><i class="fas fa-phone"></i> (206) 579-1447</a>
  </div>
  <div class="cv-header__download">
    <a href="#" onclick="openResumeModal();return false;"><i class="fas fa-download"></i> 下載履歷</a>
  </div>
</div>

<div class="cv-section">
  <h2>學歷</h2>
  <div class="cv-edu-grid">
    <div class="cv-edu-card">
      <div class="cv-edu-card__degree">電機與電腦工程碩士</div>
      <div class="cv-edu-card__school">華盛頓大學（University of Washington）<br/>西雅圖，美國</div>
      <div class="cv-edu-card__date">2025 年 9 月 — 2027 年 3 月（預計）</div>
      <div class="cv-edu-card__gpa">GPA：3.95 / 4.0</div>
    </div>
    <div class="cv-edu-card">
      <div class="cv-edu-card__degree">電機工程學士</div>
      <div class="cv-edu-card__school">元智大學<br/>桃園，臺灣</div>
      <div class="cv-edu-card__date">2020 年 9 月 — 2024 年 6 月</div>
      <div class="cv-edu-card__gpa">GPA：3.73 / 4.0 &middot; 主修：3.94 / 4.0</div>
    </div>
  </div>
</div>

<div class="cv-section">
  <h2>經歷</h2>
  <div class="cv-timeline">

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Software Development Engineer Intern <span class="cv-tag cv-tag--upcoming">Upcoming</span></span>
        <span class="cv-timeline__date">2026 年 6 月 — 9 月</span>
      </div>
      <div class="cv-timeline__org">Amazon — 西雅圖</div>
    </div>

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Research Collaborator</span>
        <span class="cv-timeline__date">2025 年 10 月 — 至今</span>
      </div>
      <div class="cv-timeline__org">PRIOR Team, Allen Institute for AI（Ai2）— 西雅圖</div>
      <ul class="cv-timeline__details">
        <li>在 3 個機器人平台（Franka FR3、SO-100/SO-101（LeRobot）、YAM）上實現即時 imitation learning 部署，將每 100 episode 的資料採集時間從 4 小時縮短至約 100 分鐘</li>
        <li>Fine-tune 並部署 &pi;<sub>0</sub>、&pi;<sub>0.5</sub>、&pi;<sub>0</sub>-FAST、ACT、SmolVLA 及 Diffusion Policy，加入 joint position/velocity action 支援與 Franka FR3 即時 inference</li>
        <li>建構端到端 data collection pipeline，涵蓋 calibration、錄製、驗證及 LeRobot 相容 dataset 轉換</li>
        <li>開發 GELLO teleoperation 系統（適用 Franka FR3 與 YAM）；整合 Meta Quest 2 Cartesian-delta 控制（FR3 透過 Polymetis、YAM 透過 SDK）</li>
      </ul>
    </div>

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Project Lead — <a href="https://github.com/thomas0829/Seattle-Source-Ranker">Seattle Source Ranker</a></span>
        <span class="cv-timeline__date">2025 年 9 月 — 至今</span>
      </div>
      <div class="cv-timeline__org">華盛頓大學 — 西雅圖</div>
      <ul class="cv-timeline__details">
        <li>設計 distributed pipeline，涵蓋 40 萬以上 GitHub repo，透過 GraphQL/REST 混合策略、Redis、Celery 及 multi-token rotation 將採集時間從 5 小時縮短至 40 分鐘（87%）</li>
        <li>建構二次驗證層來清理 raw API data，偵測 HTTP 451 legal block 並修正約 2% dataset 的 metric 不一致問題</li>
        <li>交付分層評分系統與 React 前端，支援即時篩選（&lt;100ms）、client-side pagination 及 URL state persistence</li>
      </ul>
    </div>

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Robotics Software Engineer</span>
        <span class="cv-timeline__date">2025 年 9 月 — 2026 年 4 月</span>
      </div>
      <div class="cv-timeline__org">Husky Robotics Team, 華盛頓大學 — 西雅圖</div>
      <ul class="cv-timeline__details">
        <li>為自主火星探測車開發即時 perception stack，整合 OpenCV、ArUco solvePnP 及 OWL-ViT，達成 pose-aware navigation 與約 90% object detection 準確度</li>
        <li>建構 OWL-ViT fine-tuning pipeline，準確辨識 University Rover Challenge（URC）指定的 3 項物件</li>
        <li>整合 Intel RealSense depth sensing，讓探測車能即時估算物體距離</li>
        <li>以 C++ 開發 camera calibration 與 perception-to-navigation 整合模組</li>
      </ul>
    </div>

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Robotics Engineer Intern</span>
        <span class="cv-timeline__date">2025 年 7 月 — 8 月</span>
      </div>
      <div class="cv-timeline__org">長春集團 — 資訊中心，臺北</div>
      <ul class="cv-timeline__details">
        <li>為 ALOHA VX300S 機械手臂建構端到端 imitation learning 訓練平台，在 35–65 cm workspace 達成 100% 模擬抓取成功率</li>
        <li>開發 ROS2–Isaac Sim digital twin 與 Transformer-based ACT++ control pipeline，搭配三階段 trajectory planner</li>
        <li>實作自動轉換為標準 ACT++ HDF5 dataset 格式</li>
      </ul>
    </div>

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Research Assistant</span>
        <span class="cv-timeline__date">2022 年 6 月 — 2024 年 6 月</span>
      </div>
      <div class="cv-timeline__org">DRES Lab, University of Illinois at Urbana-Champaign（UIUC）— <a href="https://experts.illinois.edu/en/persons/yih-kuen-jan/">Prof. Yih-Kuen Jan</a> &amp; <a href="https://scholars.ncu.edu.tw/en/persons/chih-yang-lin/">Prof. Chih-Yang Lin</a></div>
      <ul class="cv-timeline__details">
        <li>研究醫學影像辨識技術，實作 U-Net、Mask R-CNN 及 DeepLab V3+ 進行肩部超音波影像軟組織自動 segmentation</li>
        <li>以第一作者發表論文於 IEEE Access（2024）</li>
        <li>開發結合 VGG 與 ANN 的 deep learning model，從肩部超音波影像分類脊髓損傷（SCI）</li>
        <li>獲選教育部海外實習計畫獎學金（2022 及 2023）</li>
      </ul>
    </div>

  </div>
</div>

<div class="cv-section">
  <h2>專案</h2>
  <div class="cv-timeline">

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role"><a href="https://github.com/thomas0829/Ros_Final_Project">自主配送機器人模擬</a></span>
        <span class="cv-timeline__date">2024 年 2 月 — 6 月</span>
      </div>
      <div class="cv-timeline__org">ROS &amp; Gazebo — 元智大學</div>
      <ul class="cv-timeline__details">
        <li>使用 ROS Noetic、Gazebo、C++ 及 LiDAR 建構並測試自主四輪配送機器人</li>
        <li>實作 gmapping 做 SLAM mapping、amcl 做 localization、costmap 做即時 path planning 與避障</li>
      </ul>
    </div>

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">智慧物聯網門鎖系統</span>
        <span class="cv-timeline__date">2023 年 9 月 — 2024 年 1 月</span>
      </div>
      <div class="cv-timeline__org">Raspberry Pi 4 &amp; Flask — 元智大學</div>
      <ul class="cv-timeline__details">
        <li>使用 Raspberry Pi 4、RFID 讀取器及 Flask 網頁介面開發網路控制門鎖系統</li>
        <li>透過實作自動上鎖功能解決電磁鎖過熱問題，防止長時間通電</li>
      </ul>
    </div>

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">機器學習手勢控制系統</span>
        <span class="cv-timeline__date">2022 年 2 月 — 6 月</span>
      </div>
      <div class="cv-timeline__org">電腦視覺 — 元智大學</div>
      <ul class="cv-timeline__details">
        <li>開發即時 gesture recognition 與背景替換系統，五種手勢達成 99% accuracy</li>
        <li>透過 MediaPipe 擷取 522 個 body landmarks，最佳化四種 classifier（Random Forest、Gradient Boosting 等）</li>
      </ul>
    </div>

  </div>
</div>

<div class="cv-section">
  <h2>教學</h2>
  <div class="cv-timeline">

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">教學助理 — 計算機概論</span>
        <span class="cv-timeline__date">2023 年 9 月 — 2024 年 6 月</span>
      </div>
      <div class="cv-timeline__org">元智大學</div>
      <ul class="cv-timeline__details">
        <li>協助教授進行課程管理、批改作業及考試行政作業</li>
        <li>提供學生 LC3 組合語言、二補數及二進位運算等個別輔導</li>
      </ul>
    </div>

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Arduino 講師 — 機器人社</span>
        <span class="cv-timeline__date">2022 年 1 月 — 2 月</span>
      </div>
      <div class="cv-timeline__org">元智大學</div>
      <ul class="cv-timeline__details">
        <li>教授大學生 Arduino 開發與 C++ 基礎，並為高中生舉辦工作坊</li>
      </ul>
    </div>

  </div>
</div>

<div class="cv-section">
  <h2>論文發表</h2>
  <ol class="cv-pub-list">
    <li>
      Abhay Deshpande, Maya Guru, Rose Hendrix, Snehal Jauhri, Ainaz Eftekhar, ..., <span class="pub-me">Ying-Chun Lee</span>, ..., Georgia Chalvatzaki, Dhruv Shah, and Ranjay Krishna, "MolmoB0T: Large-Scale Simulation Enables Zero-Shot Manipulation," <em>arXiv:2603.16861</em>, 2026. <a href="https://arxiv.org/abs/2603.16861">arXiv</a> | <a href="https://github.com/allenai/MolmoBot">Code</a>
    </li>
    <li>
      Yejin Kim, Wilbert Pumacay, Omar Rayyan, Max Argus, Winson Han, ..., <span class="pub-me">Ying-Chun Lee</span>, ..., Ali Farhadi, Dieter Fox, and Ranjay Krishna, "MolmoSpaces: Large-Scale Open Ecosystem for Robot Manipulation and Navigation," <em>已投稿至 RSS 2026</em>. <a href="https://arxiv.org/abs/2602.11337">arXiv</a> | <a href="https://github.com/allenai/molmospaces">Code</a>
    </li>
    <li>
      Shirui Chen, Cole Harrison, <span class="pub-me">Ying-Chun Lee</span>, Angela Jin Yang, Zhongzheng Ren, Lillian J. Ratliff, Jiafei Duan, Dieter Fox, and Ranjay Krishna, "TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics," <em>已投稿至 ICML 2026</em>. <a href="https://arxiv.org/abs/2602.19313">arXiv</a> | <a href="https://github.com/TOPReward/TOPReward">Code</a>
    </li>
    <li>
      <span class="pub-me">Ying-Chun Lee</span>, Chih-Yang Lin, Chia-Chun Hsiao, Pu-Chun Mo, Jiaqi Guo, and Yih-Kuen Jan, "Using Deep Learning-Based Methods for Automated Segmentation of Soft Tissues from Shoulder Ultrasound Images," <em>IEEE Access</em>，第 12 卷，頁 111,481–111,492，2024 年 7 月. <a href="https://doi.org/10.1109/ACCESS.2024.3432691">DOI</a>
    </li>
  </ol>
</div>

<div class="cv-section">
  <h2>獲獎</h2>
  <div class="cv-timeline">
    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">教育部海外實習計畫獎學金</span>
        <span class="cv-timeline__date">2022 及 2023</span>
      </div>
      <div class="cv-timeline__org">獲選赴 UIUC 進行研究</div>
    </div>
    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">佳作獎 — 實驗課程專題競賽（ROS 組）</span>
        <span class="cv-timeline__date">2024 年</span>
      </div>
      <div class="cv-timeline__org">元智大學</div>
    </div>
    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">優等獎 — 實驗課程專題競賽（電腦視覺組）</span>
        <span class="cv-timeline__date">2022 年</span>
      </div>
      <div class="cv-timeline__org">元智大學</div>
    </div>
    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">第一名 — 校園創客競賽（機器人格鬥）</span>
        <span class="cv-timeline__date">2021 年</span>
      </div>
      <div class="cv-timeline__org">元智大學 — 決賽 10 隊中第 1 名</div>
    </div>
    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">全國雙足機器人競賽八強</span>
        <span class="cv-timeline__date">2020 年</span>
      </div>
      <div class="cv-timeline__org">臺灣 — 36 隊中第 8 名</div>
    </div>
  </div>
</div>

<div class="cv-section">
  <h2>技能</h2>

  <div class="cv-skills-group">
    <h3>程式語言</h3>
    <div class="cv-tags">
      <span class="cv-tag">Python</span>
      <span class="cv-tag">C</span>
      <span class="cv-tag">C++</span>
      <span class="cv-tag">JavaScript</span>
      <span class="cv-tag">HTML</span>
      <span class="cv-tag">CSS</span>
      <span class="cv-tag">SQL</span>
      <span class="cv-tag">MATLAB</span>
    </div>
  </div>

  <div class="cv-skills-group">
    <h3>Robotics & AI</h3>
    <div class="cv-tags">
      <span class="cv-tag">ROS2</span>
      <span class="cv-tag">PyTorch</span>
      <span class="cv-tag">TensorFlow</span>
      <span class="cv-tag">Keras</span>
      <span class="cv-tag">OpenCV</span>
      <span class="cv-tag">NumPy</span>
      <span class="cv-tag">Matplotlib</span>
      <span class="cv-tag">PIL</span>
      <span class="cv-tag">NVIDIA Isaac Sim</span>
    </div>
  </div>

  <div class="cv-skills-group">
    <h3>Web & Cloud</h3>
    <div class="cv-tags">
      <span class="cv-tag">React</span>
      <span class="cv-tag">Node.js</span>
      <span class="cv-tag">Flask</span>
      <span class="cv-tag">Docker</span>
      <span class="cv-tag">Kubernetes</span>
      <span class="cv-tag">AWS</span>
      <span class="cv-tag">GCP</span>
      <span class="cv-tag">Redis</span>
      <span class="cv-tag">Celery</span>
    </div>
  </div>

  <div class="cv-skills-group">
    <h3>Data & Analysis</h3>
    <div class="cv-tags">
      <span class="cv-tag">pandas</span>
      <span class="cv-tag">SciPy</span>
      <span class="cv-tag">Jupyter</span>
      <span class="cv-tag">Git</span>
    </div>
  </div>
</div>

