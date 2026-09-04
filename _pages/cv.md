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
  <div class="cv-header__subtitle">M.S. in ECE, University of Washington</div>
  <div class="cv-header__contact">
    <a href="mailto:thomas910829@gmail.com"><i class="fas fa-envelope"></i> thomas910829@gmail.com</a>
    <a href="https://github.com/thomas0829"><i class="fab fa-github"></i> GitHub</a>
    <a href="https://www.linkedin.com/in/thomas0829/"><i class="fab fa-linkedin"></i> LinkedIn</a>
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
      <div class="cv-edu-card__gpa">GPA: 3.98 / 4.0</div>
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
        <span class="cv-timeline__role">Software Development Engineer Intern</span>
        <span class="cv-timeline__date">Jun 2026 — Sep 2026</span>
      </div>
      <div class="cv-timeline__org">Amazon — Seattle, WA</div>
      <ul class="cv-timeline__details">
        <li>Built and launched a self-service risk-labeling system for an enterprise platform, replacing recurring schema migrations and code deployments with configuration-driven classification management</li>
        <li>Designed and shipped 18 REST API operations for Java 17 services deployed on AWS Lambda using Smithy, Hibernate/JPA, and Amazon Aurora PostgreSQL</li>
        <li>Strengthened record-scoped authorization and concurrent-write reliability by deriving access decisions from persisted records and implementing idempotent writes with explicit transaction handling, constraint translation, and post-transaction reads</li>
        <li>Engineered keyset-batched bulk labeling for up to 500 risks per request with item-level outcomes and partial-success handling, allowing valid records to proceed when others were skipped or unchanged</li>
        <li>Developed a React 18/TypeScript governance and reporting interface using the Cloudscape Design System and TanStack Query, with filtering, grouping, usage drill-downs, change history, and formula-injection-safe CSV/XLSX exports</li>
        <li>Reduced grouped-report API calls from 10 to 1 (90%), lowering data-fetch latency by approximately 80%</li>
      </ul>
    </div>

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Research Collaboration</span>
        <span class="cv-timeline__date">Oct 2025 — May 2026</span>
      </div>
      <div class="cv-timeline__org">with Jiafei Duan and collaborators from Ai2 PRIOR</div>
      <ul class="cv-timeline__details">
        <li>Contributed to robot-learning research associated with <a href="https://arxiv.org/abs/2605.02881">MolmoAct2</a>, <a href="https://arxiv.org/abs/2603.16861">MolmoB0T</a>, and <a href="https://arxiv.org/abs/2602.19313">TOPReward</a> (CoRL 2026), and <a href="https://roboticsconference.org/program/papers/91/">MolmoSpaces</a> (RSS 2026); built infrastructure for real-robot policy deployment, teleoperation, evaluation, and control tooling</li>
        <li>Set up real-time imitation-learning deployment infrastructure on 3 robot platforms (Franka FR3, SO-100/SO-101 via LeRobot, YAM), improving 100-episode rollout throughput from ~4 hours to ~100 minutes</li>
        <li>Fine-tuned and ran VLA and imitation-learning policies including &pi;<sub>0</sub>, &pi;<sub>0.5</sub>, &pi;<sub>0</sub>-FAST, ACT, SmolVLA, and Diffusion Policy on real hardware; added joint-position/velocity action support and real-time FR3 inference</li>
        <li>Built platform tooling around calibration, recording, validation, and LeRobot-compatible conversion to make policy deployment and evaluation reproducible</li>
        <li>Implemented GELLO teleoperation for Franka FR3 and YAM, plus Meta Quest 2 Cartesian-delta control through Polymetis and direct SDK integrations</li>
      </ul>
    </div>

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Software Systems Project Lead — <a href="https://github.com/thomas0829/Seattle-Source-Ranker">Seattle Source Ranker</a></span>
        <span class="cv-timeline__date">Sep 2025 — May 2026</span>
      </div>
      <div class="cv-timeline__org">University of Washington — Seattle, WA</div>
      <ul class="cv-timeline__details">
        <li>Built a distributed pipeline over 400K+ GitHub repositories, cutting collection time by 87% (5 hours to 40 minutes) with GraphQL/REST, Redis, Celery, and multi-token rotation</li>
        <li>Added a validation layer for raw API data, including HTTP 451 legal blocks and metric inconsistencies affecting ~2% of the dataset</li>
        <li>Built a tiered scoring system and React interface with instant filtering (&lt;100ms), client-side pagination, and URL state persistence</li>
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
        <span class="cv-timeline__role">Robotics Software Engineer Intern</span>
        <span class="cv-timeline__date">Jul 2025 — Aug 2025</span>
      </div>
      <div class="cv-timeline__org">Chang Chun Group — Information Center, Taipei, Taiwan</div>
      <ul class="cv-timeline__details">
        <li>Built an imitation-learning training platform for the ALOHA-ViperX 300S robotic arm, achieving 100% grasp success across 30 simulation trials within a 35-65 cm workspace</li>
        <li>Integrated a ROS 2/NVIDIA Isaac Sim digital twin with a transformer-based ACT++ control pipeline and a three-stage trajectory planner</li>
        <li>Added automated conversion to standard ACT++ HDF5 datasets for repeatable training runs</li>
      </ul>
    </div>

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Undergraduate Researcher</span>
        <span class="cv-timeline__date">Jun 2022 — Jun 2024</span>
      </div>
      <div class="cv-timeline__org">Shoulder ultrasound medical image segmentation — guidance from <a href="https://experts.illinois.edu/en/persons/yih-kuen-jan/">Prof. Yih-Kuen Jan</a> (UIUC DRES Lab) &amp; <a href="https://scholars.ncu.edu.tw/en/persons/chih-yang-lin/">Prof. Chih-Yang Lin</a></div>
      <ul class="cv-timeline__details">
        <li>Led first-author research on soft-tissue segmentation in shoulder ultrasound medical images, implementing U-Net, Mask R-CNN, and DeepLab V3+; published in <a href="https://doi.org/10.1109/ACCESS.2024.3432691">IEEE Access</a></li>
        <li>Developed a deep learning model combining VGG and ANN for spinal cord injury (SCI) classification from shoulder ultrasound medical images</li>
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
        <li>Built and tested an autonomous four-wheeled delivery robot in ROS Noetic and Gazebo with C++ and LiDAR</li>
        <li>Used gmapping, amcl, and costmap for SLAM, localization, path planning, and obstacle avoidance</li>
      </ul>
    </div>

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Smart IoT Door Lock System</span>
        <span class="cv-timeline__date">Sep 2023 — Jan 2024</span>
      </div>
      <div class="cv-timeline__org">Raspberry Pi 4 &amp; Flask — Yuan Ze University</div>
      <ul class="cv-timeline__details">
        <li>Built a web-controlled door lock system with Raspberry Pi 4, an RFID reader, and Flask</li>
        <li>Fixed electromagnetic lock overheating by adding auto-lock behavior to prevent prolonged current flow</li>
      </ul>
    </div>

    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">ML-Powered Gesture Control System</span>
        <span class="cv-timeline__date">Feb 2022 — Jun 2022</span>
      </div>
      <div class="cv-timeline__org">Computer Vision — Yuan Ze University</div>
      <ul class="cv-timeline__details">
        <li>Built a real-time gesture recognition and background replacement system with 99% accuracy across five gestures</li>
        <li>Extracted 522 body landmarks with MediaPipe and compared four classifiers, including Random Forest and Gradient Boosting</li>
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
        <li>Helped manage coursework, grading, and exam logistics</li>
        <li>Supported students one-on-one with LC3 assembly, two's complement, and binary operations</li>
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
      Shirui Chen, Cole Harrison, <span class="pub-me">Ying-Chun Lee</span>, Angela Jin Yang, Zhongzheng Ren, Lillian J. Ratliff, Jiafei Duan, Dieter Fox, and Ranjay Krishna, "TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics," <em class="pub-venue--published">CoRL 2026</em>. <a href="https://topreward.github.io/webpage/">Project</a> | <a href="https://arxiv.org/abs/2602.19313">arXiv</a> | <a href="https://github.com/TOPReward/TOPReward">Code</a>
    </li>
    <li>
      Abhay Deshpande, Maya Guru, Rose Hendrix, Snehal Jauhri, Ainaz Eftekhar, ..., <span class="pub-me">Ying-Chun Lee</span>, ..., Georgia Chalvatzaki, Dhruv Shah, and Ranjay Krishna, "MolmoB0T: Large-Scale Simulation Enables Zero-Shot Manipulation," <em class="pub-venue--published">CoRL 2026</em>. <a href="https://allenai.github.io/MolmoBot/">Project</a> | <a href="https://arxiv.org/abs/2603.16861">arXiv</a> | <a href="https://github.com/allenai/MolmoBot">Code</a>
    </li>
    <li>
      Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, ..., Winson Han, <span class="pub-me">Ying-Chun Lee</span>, ..., Ali Farhadi, Dieter Fox, and Ranjay Krishna, "MolmoAct2: Action Reasoning Models for Real-world Deployment," <em class="pub-venue--published">CoRL 2026</em>. <a href="https://allenai.org/blog/molmoact2">Project</a> | <a href="https://arxiv.org/abs/2605.02881">arXiv</a> | <a href="https://github.com/allenai/molmoact2">Code</a>
    </li>
    <li>
      Yejin Kim, Wilbert Pumacay, Omar Rayyan, Max Argus, Winson Han, ..., <span class="pub-me">Ying-Chun Lee</span>, ..., Ali Farhadi, Dieter Fox, and Ranjay Krishna, "MolmoSpaces: Large-Scale Open Ecosystem for Robot Manipulation and Navigation," <em class="pub-venue--published">RSS 2026</em>. <a href="https://allenai.org/blog/molmospaces">Project</a> | <a href="https://www.roboticsproceedings.org/rss22/p091.pdf">PDF</a> | <a href="https://github.com/allenai/molmospaces">Code</a>
    </li>
    <li>
      <span class="pub-me">Ying-Chun Lee</span>, Chih-Yang Lin, Chia-Chun Hsiao, Pu-Chun Mo, Jiaqi Guo, and Yih-Kuen Jan, "Using Deep Learning-Based Methods for Automated Segmentation of Soft Tissues from Shoulder Ultrasound Images," <em class="pub-venue--published">IEEE Access</em>, Vol. 12, pp. 111,481-111,492, July 2024. <a href="https://doi.org/10.1109/ACCESS.2024.3432691">DOI</a>
    </li>
  </ol>
</div>

<div class="cv-section">
  <h2>Awards</h2>
  <div class="cv-timeline">
    <div class="cv-timeline__item">
      <div class="cv-timeline__header">
        <span class="cv-timeline__role">Engineering Capstone Team MVP Award</span>
        <span class="cv-timeline__date">2026</span>
      </div>
      <div class="cv-timeline__org">University of Washington</div>
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
        <span class="cv-timeline__role">Taiwan Ministry of Education Overseas Internship Scholarship</span>
        <span class="cv-timeline__date">2022 &amp; 2023</span>
      </div>
      <div class="cv-timeline__org">Selected to conduct research at UIUC</div>
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
    <h3>Relevant Coursework</h3>
    <div class="cv-tags">
      <span class="cv-tag">ROS</span>
      <span class="cv-tag">Self-Driving Cars</span>
      <span class="cv-tag">Software Development</span>
      <span class="cv-tag">Embedded Systems</span>
      <span class="cv-tag">Smart Systems</span>
      <span class="cv-tag">Artificial Intelligence</span>
      <span class="cv-tag">Deep Learning</span>
      <span class="cv-tag">Computer Vision</span>
      <span class="cv-tag">Internet of Things</span>
      <span class="cv-tag">Cloud Computing</span>
    </div>
  </div>

  <div class="cv-skills-group">
    <h3>Programming</h3>
    <div class="cv-tags">
      <span class="cv-tag">Python</span>
      <span class="cv-tag">C</span>
      <span class="cv-tag">C++</span>
      <span class="cv-tag">Java</span>
      <span class="cv-tag">TypeScript</span>
      <span class="cv-tag">React</span>
      <span class="cv-tag">HTML</span>
      <span class="cv-tag">CSS</span>
      <span class="cv-tag">SQL</span>
    </div>
  </div>

  <div class="cv-skills-group">
    <h3>Tools &amp; Frameworks</h3>
    <div class="cv-tags">
      <span class="cv-tag">ROS 2</span>
      <span class="cv-tag">NVIDIA Isaac Sim</span>
      <span class="cv-tag">Omniverse USD</span>
      <span class="cv-tag">PyTorch</span>
      <span class="cv-tag">OpenCV</span>
      <span class="cv-tag">NumPy</span>
      <span class="cv-tag">PIL</span>
      <span class="cv-tag">Docker</span>
      <span class="cv-tag">AWS</span>
      <span class="cv-tag">GCP</span>
    </div>
  </div>
</div>
