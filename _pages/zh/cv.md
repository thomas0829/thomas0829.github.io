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
  <div class="cv-header__subtitle">華盛頓大學 ECE 碩士</div>
  <div class="cv-header__contact">
    <a href="mailto:thomas910829@gmail.com"><i class="fas fa-envelope"></i> thomas910829@gmail.com</a>
    <a href="https://github.com/thomas0829"><i class="fab fa-github"></i> GitHub</a>
    <a href="https://www.linkedin.com/in/thomas0829/"><i class="fab fa-linkedin"></i> LinkedIn</a>
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
        <span class="cv-timeline__role">研究合作</span>
        <span class="cv-timeline__date">2025 年 10 月 — 2026 年 5 月</span>
      </div>
      <div class="cv-timeline__org">與 Jiafei Duan 及 Ai2 PRIOR 研究人員合作</div>
      <ul class="cv-timeline__details">
        <li>參與 <a href="https://arxiv.org/abs/2602.11337">MolmoSpaces</a>（RSS 2026）、<a href="https://arxiv.org/abs/2603.16861">MolmoB0T</a> 與 <a href="https://arxiv.org/abs/2602.19313">TOPReward</a> 相關的 robot-learning research；主要建置真實機器人 policy deployment、data collection、teleoperation 與 evaluation infrastructure</li>
        <li>在 3 個真實機器人平台上建立即時 imitation-learning deployment（Franka FR3、SO-100/SO-101 via LeRobot、YAM），將每 100 episode 的資料採集時間從約 4 小時降到約 100 分鐘</li>
        <li>Fine-tune 並在真機上跑 VLA 與 imitation-learning policies，包括 &pi;<sub>0</sub>、&pi;<sub>0.5</sub>、&pi;<sub>0</sub>-FAST、ACT、SmolVLA 及 Diffusion Policy；加入 joint position/velocity action 支援與 Franka FR3 即時 inference</li>
        <li>建立 data collection 流程，包含 calibration、錄製、驗證與 LeRobot-compatible dataset 轉換</li>
        <li>實作 Franka FR3 與 YAM 的 GELLO teleoperation，並整合 Meta Quest 2 Cartesian-delta control（Polymetis 與 direct SDK）</li>
      </ul>
    </div>

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Software Systems Project Lead — <a href="https://github.com/thomas0829/Seattle-Source-Ranker">Seattle Source Ranker</a></span>
        <span class="cv-timeline__date">2025 年 9 月 — 至今</span>
      </div>
      <div class="cv-timeline__org">華盛頓大學 — 西雅圖</div>
      <ul class="cv-timeline__details">
        <li>建置涵蓋 40 萬以上 GitHub repo 的 distributed pipeline，透過 GraphQL/REST、Redis、Celery 與 multi-token rotation 將採集時間從 5 小時降到 40 分鐘（87%）</li>
        <li>加入 raw API data 驗證層，處理 HTTP 451 legal block 與約 2% dataset 的 metric 不一致問題</li>
        <li>做出分層評分系統與 React 前端，支援即時篩選（&lt;100ms）、client-side pagination 與 URL state persistence</li>
      </ul>
    </div>

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Robotics Software Engineer</span>
        <span class="cv-timeline__date">2025 年 9 月 — 2026 年 4 月</span>
      </div>
      <div class="cv-timeline__org">Husky Robotics Team, 華盛頓大學 — 西雅圖</div>
      <ul class="cv-timeline__details">
        <li>為自主火星探測車開發即時 perception stack，整合 OpenCV、ArUco solvePnP 與 OWL-ViT，達成 pose-aware navigation 與約 90% object detection 準確度</li>
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
        <li>為 ALOHA VX300S 機械手臂建 imitation learning 訓練平台，在 35-65 cm workspace 達到 100% 模擬抓取成功率</li>
        <li>開發 ROS2-Isaac Sim digital twin 與 Transformer-based ACT++ control pipeline，搭配三階段 trajectory planner</li>
        <li>加入自動轉換成標準 ACT++ HDF5 dataset 的流程，方便重複訓練</li>
      </ul>
    </div>

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Undergraduate Researcher</span>
        <span class="cv-timeline__date">2022 年 6 月 — 2024 年 6 月</span>
      </div>
      <div class="cv-timeline__org">肩部超音波影像 segmentation — <a href="https://experts.illinois.edu/en/persons/yih-kuen-jan/">Prof. Yih-Kuen Jan</a>（UIUC DRES Lab）與 <a href="https://scholars.ncu.edu.tw/en/persons/chih-yang-lin/">Prof. Chih-Yang Lin</a> 指導</div>
      <ul class="cv-timeline__details">
        <li>主導肩部超音波影像軟組織 segmentation 研究，實作 U-Net、Mask R-CNN 與 DeepLab V3+；成果以第一作者發表於 <a href="https://doi.org/10.1109/ACCESS.2024.3432691">IEEE Access</a></li>
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
        <li>使用 ROS Noetic、Gazebo、C++ 與 LiDAR 建置並測試自主四輪配送機器人</li>
        <li>使用 gmapping、amcl 與 costmap 完成 SLAM、localization、path planning 與避障</li>
      </ul>
    </div>

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">智慧物聯網門鎖系統</span>
        <span class="cv-timeline__date">2023 年 9 月 — 2024 年 1 月</span>
      </div>
      <div class="cv-timeline__org">Raspberry Pi 4 &amp; Flask — 元智大學</div>
      <ul class="cv-timeline__details">
        <li>用 Raspberry Pi 4、RFID 讀取器與 Flask 做網路控制門鎖系統</li>
        <li>加入自動上鎖功能，避免電磁鎖長時間通電而過熱</li>
      </ul>
    </div>

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">機器學習手勢控制系統</span>
        <span class="cv-timeline__date">2022 年 2 月 — 6 月</span>
      </div>
      <div class="cv-timeline__org">電腦視覺 — 元智大學</div>
      <ul class="cv-timeline__details">
        <li>做出即時 gesture recognition 與背景替換系統，五種手勢達到 99% accuracy</li>
        <li>用 MediaPipe 擷取 522 個 body landmarks，並比較 Random Forest、Gradient Boosting 等四種 classifier</li>
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
        <li>協助課程管理、批改作業與考試行政作業</li>
        <li>個別輔導學生 LC3 組合語言、二補數與二進位運算</li>
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
      Yejin Kim, Wilbert Pumacay, Omar Rayyan, Max Argus, Winson Han, ..., <span class="pub-me">Ying-Chun Lee</span>, ..., Ali Farhadi, Dieter Fox, and Ranjay Krishna, "MolmoSpaces: Large-Scale Open Ecosystem for Robot Manipulation and Navigation," <em>RSS 2026</em>. <a href="https://arxiv.org/abs/2602.11337">arXiv</a> | <a href="https://github.com/allenai/molmospaces">Code</a>
    </li>
    <li>
      Shirui Chen, Cole Harrison, <span class="pub-me">Ying-Chun Lee</span>, Angela Jin Yang, Zhongzheng Ren, Lillian J. Ratliff, Jiafei Duan, Dieter Fox, and Ranjay Krishna, "TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics," <em>arXiv preprint</em>, 2026. <a href="https://arxiv.org/abs/2602.19313">arXiv</a> | <a href="https://github.com/TOPReward/TOPReward">Code</a>
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
    <h3>Robotics / VLA / AI</h3>
    <div class="cv-tags">
      <span class="cv-tag">VLA</span>
      <span class="cv-tag">Robot Learning</span>
      <span class="cv-tag">Reinforcement Learning</span>
      <span class="cv-tag">Reward Modeling</span>
      <span class="cv-tag">Imitation Learning</span>
      <span class="cv-tag">LeRobot</span>
      <span class="cv-tag">ROS2</span>
      <span class="cv-tag">Polymetis</span>
      <span class="cv-tag">NVIDIA Isaac Sim</span>
      <span class="cv-tag">PyTorch</span>
      <span class="cv-tag">TensorFlow</span>
      <span class="cv-tag">OpenCV</span>
      <span class="cv-tag">OWL-ViT</span>
      <span class="cv-tag">Diffusion Policy</span>
    </div>
  </div>

  <div class="cv-skills-group">
    <h3>Software Systems</h3>
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
      <span class="cv-tag">GitHub GraphQL/REST</span>
    </div>
  </div>

  <div class="cv-skills-group">
    <h3>Data & Analysis</h3>
    <div class="cv-tags">
      <span class="cv-tag">pandas</span>
      <span class="cv-tag">NumPy</span>
      <span class="cv-tag">SciPy</span>
      <span class="cv-tag">Matplotlib</span>
      <span class="cv-tag">Jupyter</span>
      <span class="cv-tag">Git</span>
    </div>
  </div>
</div>
