---
layout: cv
title: "CV"
permalink: /cv/
author_profile: false
lang: en
lang_url: /zh/cv/
redirect_from:
  - /resume
---

<div class="cv-header">
  <h1>Ying-Chun Lee</h1>
  <div class="cv-header__subtitle">M.S. in Electrical and Computer Engineering @ University of Washington</div>
  <div class="cv-header__contact">
    <a href="mailto:thomas910829@gmail.com"><i class="fas fa-envelope"></i> thomas910829@gmail.com</a>
    <a href="https://github.com/thomas0829"><i class="fab fa-github"></i> GitHub</a>
    <a href="https://www.linkedin.com/in/thomas0829/"><i class="fab fa-linkedin"></i> LinkedIn</a>
    <a href="tel:+12065791447"><i class="fas fa-phone"></i> (206) 579-1447</a>
  </div>
  <div class="cv-header__download">
    <a href="#" onclick="openResumeModal();return false;"><i class="fas fa-download"></i> Download Resume</a>
  </div>
</div>

<div class="cv-section">
  <h2>Education</h2>
  <div class="cv-edu-grid">
    <div class="cv-edu-card">
      <div class="cv-edu-card__degree">M.S. in Electrical and Computer Engineering</div>
      <div class="cv-edu-card__school">University of Washington, Seattle, WA</div>
      <div class="cv-edu-card__date">Sep 2025 — Mar 2027 (Expected)</div>
      <div class="cv-edu-card__gpa">GPA: 3.95 / 4.0</div>
    </div>
    <div class="cv-edu-card">
      <div class="cv-edu-card__degree">B.S. in Electrical Engineering</div>
      <div class="cv-edu-card__school">Yuan Ze University, Taoyuan, Taiwan</div>
      <div class="cv-edu-card__date">Sep 2020 — Jun 2024</div>
      <div class="cv-edu-card__gpa">GPA: 3.73 / 4.0 &middot; Major: 3.94 / 4.0</div>
    </div>
  </div>
</div>

<div class="cv-section">
  <h2>Experience</h2>
  <div class="cv-timeline">

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Software Development Engineer Intern <span class="cv-tag cv-tag--upcoming">Upcoming</span></span>
        <span class="cv-timeline__date">Jun 2026 — Sep 2026</span>
      </div>
      <div class="cv-timeline__org">Amazon — Seattle, WA</div>
    </div>

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Research Collaborator</span>
        <span class="cv-timeline__date">Oct 2025 — Present</span>
      </div>
      <div class="cv-timeline__org">PRIOR Team, Allen Institute for AI (Ai2) — Seattle, WA</div>
      <ul class="cv-timeline__details">
        <li>Enabled real-time imitation-learning deployment across 3 robotic platforms (Franka FR3, SO-100/SO-101 via LeRobot, YAM), cutting data-collection time from 4 hours to ~100 minutes per 100 episodes</li>
        <li>Fine-tuned and deployed &pi;<sub>0</sub>, &pi;<sub>0.5</sub>, &pi;<sub>0</sub>-FAST, ACT, SmolVLA, and Diffusion Policy on real hardware, adding joint-position/velocity action support and real-time inference on the Franka FR3</li>
        <li>Built an end-to-end data collection pipeline covering calibration, recording, validation, and LeRobot-compatible dataset conversion for scalable policy training</li>
        <li>Engineered GELLO teleoperation for the Franka FR3 and YAM; integrated Meta Quest 2 Cartesian-delta control for the FR3 via Polymetis and for the YAM via direct SDK interface</li>
      </ul>
    </div>

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Project Lead — <a href="https://github.com/thomas0829/Seattle-Source-Ranker">Seattle Source Ranker</a></span>
        <span class="cv-timeline__date">Sep 2025 — Present</span>
      </div>
      <div class="cv-timeline__org">University of Washington — Seattle, WA</div>
      <ul class="cv-timeline__details">
        <li>Architected a distributed pipeline spanning 400K+ repositories, reducing collection time by 87% (5 hours to 40 mins) with hybrid GitHub GraphQL/REST strategy, Redis, Celery, and multi-token rotation</li>
        <li>Engineered a secondary validation layer to sanitize raw API data, ensuring integrity by detecting legal blocks (HTTP 451) and correcting metric inconsistencies for ~2% of the dataset</li>
        <li>Delivered a tiered scoring system and React interface with instant filtering (&lt;100ms), client-side pagination, and URL state persistence</li>
      </ul>
    </div>

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Robotics Software Engineer</span>
        <span class="cv-timeline__date">Sep 2025 — Apr 2026</span>
      </div>
      <div class="cv-timeline__org">Husky Robotics Team, University of Washington — Seattle, WA</div>
      <ul class="cv-timeline__details">
        <li>Delivered a real-time perception stack for an autonomous Mars rover, enabling pose-aware navigation and ~90% object-detection accuracy by integrating OpenCV, ArUco solvePnP, and OWL-ViT</li>
        <li>Built a fine-tuning pipeline for OWL-ViT to accurately detect three designated objects in the University Rover Challenge (URC), improving recall on domain-specific targets</li>
        <li>Integrated Intel RealSense depth sensing into the perception stack, enabling the rover to estimate object distance in real time for autonomous approach and manipulation</li>
        <li>Architected camera calibration and perception-to-navigation integration in C++ for low-latency real-time control</li>
      </ul>
    </div>

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Robotics Engineer Intern</span>
        <span class="cv-timeline__date">Jul 2025 — Aug 2025</span>
      </div>
      <div class="cv-timeline__org">Chang Chun Group — Information Center, Taipei, Taiwan</div>
      <ul class="cv-timeline__details">
        <li>Created an end-to-end imitation-learning training platform for the ALOHA VX300S robotic arm, achieving 100% grasp success in simulation across a 35–65 cm workspace</li>
        <li>Developed a ROS2–Isaac Sim digital twin and Transformer-based ACT++ control pipeline with a three-stage trajectory planner</li>
        <li>Implemented automated conversion to standard ACT++ HDF5 datasets for scalable training</li>
      </ul>
    </div>

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Research Assistant</span>
        <span class="cv-timeline__date">Jun 2022 — Jun 2024</span>
      </div>
      <div class="cv-timeline__org">DRES Lab, University of Illinois at Urbana-Champaign (UIUC) — <a href="https://experts.illinois.edu/en/persons/yih-kuen-jan/">Prof. Yih-Kuen Jan</a> &amp; <a href="https://scholars.ncu.edu.tw/en/persons/chih-yang-lin/">Prof. Chih-Yang Lin</a></div>
      <ul class="cv-timeline__details">
        <li>Researched medical image recognition techniques; implemented U-Net, Mask R-CNN, and DeepLab V3+ for automated shoulder soft tissue segmentation from ultrasound images</li>
        <li>Published first-author paper in IEEE Access (2024)</li>
        <li>Developed a deep learning model combining VGG and ANN for spinal cord injury (SCI) classification from shoulder ultrasound images</li>
        <li>Selected as Scholarship Recipient through Taiwan Ministry of Education Overseas Internship Program (2022 &amp; 2023)</li>
      </ul>
    </div>

  </div>
</div>

<div class="cv-section">
  <h2>Projects</h2>
  <div class="cv-timeline">

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role"><a href="https://github.com/thomas0829/Ros_Final_Project">Autonomous Delivery Robot Simulation</a></span>
        <span class="cv-timeline__date">Feb 2024 — Jun 2024</span>
      </div>
      <div class="cv-timeline__org">ROS &amp; Gazebo — Yuan Ze University</div>
      <ul class="cv-timeline__details">
        <li>Built and tested an autonomous four-wheeled delivery robot using ROS Noetic, Gazebo, C++, and LiDAR</li>
        <li>Implemented gmapping for SLAM-based mapping, amcl for localization, and costmap for real-time path planning and obstacle avoidance</li>
      </ul>
    </div>

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Smart IoT Door Lock System</span>
        <span class="cv-timeline__date">Sep 2023 — Jan 2024</span>
      </div>
      <div class="cv-timeline__org">Raspberry Pi 4 &amp; Flask — Yuan Ze University</div>
      <ul class="cv-timeline__details">
        <li>Developed a web-controlled door lock system using Raspberry Pi 4, RFID reader, and a Flask web interface</li>
        <li>Resolved electromagnetic lock overheating by implementing an auto-lock feature to prevent prolonged current flow</li>
      </ul>
    </div>

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">ML-Powered Gesture Control System</span>
        <span class="cv-timeline__date">Feb 2022 — Jun 2022</span>
      </div>
      <div class="cv-timeline__org">Computer Vision — Yuan Ze University</div>
      <ul class="cv-timeline__details">
        <li>Developed a real-time gesture recognition and background replacement system achieving 99% accuracy across five gestures</li>
        <li>Extracted 522 body landmarks via MediaPipe; optimized four classifiers including Random Forest and Gradient Boosting</li>
      </ul>
    </div>

  </div>
</div>

<div class="cv-section">
  <h2>Teaching</h2>
  <div class="cv-timeline">

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Teaching Assistant — Introduction to Computer Science</span>
        <span class="cv-timeline__date">Sep 2023 — Jun 2024</span>
      </div>
      <div class="cv-timeline__org">Yuan Ze University</div>
      <ul class="cv-timeline__details">
        <li>Assisted professor with coursework management, grading, and exam logistics</li>
        <li>Provided one-on-one support for students on LC3 assembly language, two's complement, and binary operations</li>
      </ul>
    </div>

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Arduino Instructor — Robotics Club</span>
        <span class="cv-timeline__date">Jan 2022 — Feb 2022</span>
      </div>
      <div class="cv-timeline__org">Yuan Ze University</div>
      <ul class="cv-timeline__details">
        <li>Taught Arduino development and C++ fundamentals to university students and conducted workshops for high school students</li>
      </ul>
    </div>

  </div>
</div>

<div class="cv-section">
  <h2>Publications</h2>
  <ol class="cv-pub-list">
    <li>
      Abhay Deshpande, Maya Guru, Rose Hendrix, Snehal Jauhri, Ainaz Eftekhar, ..., <span class="pub-me">Ying-Chun Lee</span>, ..., Georgia Chalvatzaki, Dhruv Shah, and Ranjay Krishna, "MolmoB0T: Large-Scale Simulation Enables Zero-Shot Manipulation," <em>arXiv:2603.16861</em>, 2026. <a href="https://arxiv.org/abs/2603.16861">arXiv</a>
    </li>
    <li>
      Yejin Kim, Wilbert Pumacay, Omar Rayyan, Max Argus, Winson Han, ..., <span class="pub-me">Ying-Chun Lee</span>, ..., Ali Farhadi, Dieter Fox, and Ranjay Krishna, "MolmoSpaces: Large-Scale Open Ecosystem for Robot Manipulation and Navigation," <em>Submitted to RSS 2026</em>. <a href="https://arxiv.org/abs/2602.11337">arXiv</a>
    </li>
    <li>
      Shirui Chen, Cole Harrison, <span class="pub-me">Ying-Chun Lee</span>, Angela Jin Yang, Zhongzheng Ren, Lillian J. Ratliff, Jiafei Duan, Dieter Fox, and Ranjay Krishna, "TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics," <em>Submitted to ICML 2026</em>. <a href="https://arxiv.org/abs/2602.19313">arXiv</a>
    </li>
    <li>
      <span class="pub-me">Ying-Chun Lee</span>, Chih-Yang Lin, Chia-Chun Hsiao, Pu-Chun Mo, Jiaqi Guo, and Yih-Kuen Jan, "Using Deep Learning-Based Methods for Automated Segmentation of Soft Tissues from Shoulder Ultrasound Images," <em>IEEE Access</em>, Vol. 12, pp. 111,481-111,492, July 2024. <a href="https://doi.org/10.1109/ACCESS.2024.3432691">DOI</a>
    </li>
  </ol>
</div>

<div class="cv-section">
  <h2>Awards</h2>
  <div class="cv-timeline">
    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Taiwan Ministry of Education Overseas Internship Scholarship</span>
        <span class="cv-timeline__date">2022 &amp; 2023</span>
      </div>
      <div class="cv-timeline__org">Selected to conduct research at UIUC</div>
    </div>
    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Merit Award — Lab Course Project Competition (ROS Group)</span>
        <span class="cv-timeline__date">2024</span>
      </div>
      <div class="cv-timeline__org">Yuan Ze University</div>
    </div>
    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Excellence Award — Lab Course Project Competition (CV Group)</span>
        <span class="cv-timeline__date">2022</span>
      </div>
      <div class="cv-timeline__org">Yuan Ze University</div>
    </div>
    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">1st Place — Campus Maker Competition (Robot Battle)</span>
        <span class="cv-timeline__date">2021</span>
      </div>
      <div class="cv-timeline__org">Yuan Ze University — 1st out of 10 in Finals</div>
    </div>
    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Top 8 Finalist — National Biped Robot Competition</span>
        <span class="cv-timeline__date">2020</span>
      </div>
      <div class="cv-timeline__org">Taiwan — 8th out of 36 teams</div>
    </div>
  </div>
</div>

<div class="cv-section">
  <h2>Skills</h2>

  <div class="cv-skills-group">
    <h3>Programming</h3>
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

