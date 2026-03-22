---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* **M.S. in Electrical and Computer Engineering**, University of Washington, Seattle, WA (Sep 2025 — Mar 2027 Expected)
  * GPA: 3.95 / 4.0
* **B.S. in Electrical Engineering**, Yuan Ze University, Taoyuan, Taiwan (Sep 2020 — Jun 2024)
  * Overall GPA: 3.73 / 4.0, Major GPA: 3.94 / 4.0

Technical Experience
======
* **Research Collaborator** — PRIOR Team, Allen Institute for AI (Ai2), Seattle, WA (Oct 2025 — Present)
  * Enabled real-time imitation-learning deployment across 3 robotic platforms, cutting data-collection time from 4 hours to ~100 minutes per 100 episodes
  * Trained and deployed ACT and pi0 policies on real robots, adding joint-position/velocity action support and real-time inference on the Franka arm
  * Engineered a Gello teleoperation, data-collection, and replay pipeline with Oculus Cartesian-delta compatibility

* **Project Lead** — Seattle Source Ranker, Seattle, WA (Sep 2025 — Present)
  * Architected a distributed pipeline spanning 400K+ repositories, reducing collection time by 87% with hybrid GitHub GraphQL/REST strategy, Redis, Celery, and multi-token rotation
  * Engineered a secondary validation layer to sanitize raw API data, ensuring integrity by automatically detecting legal blocks (HTTP 451) and correcting metric inconsistencies
  * Delivered a tiered scoring system and React interface with instant filtering (<100ms)

* **Robotics Software Engineer** — Husky Robotics Team, University of Washington (Sep 2025 — Apr 2026)
  * Delivered a real-time perception stack for an autonomous Mars rover, enabling pose-aware navigation and ~90% object-detection accuracy
  * Architected camera calibration and perception-to-navigation integration in C++ for low-latency real-time control

* **Robotics Engineer Intern** — Chang Chun Group, Taipei, Taiwan (Jul 2025 — Aug 2025)
  * Created an end-to-end imitation-learning training platform for the ALOHA VX300S robotic arm, achieving 100% grasp success in simulation
  * Developed a ROS2–Isaac Sim digital twin and Transformer-based ACT++ control pipeline
  * Implemented automated conversion to standard ACT++ HDF5 datasets for scalable training

Skills
======
* **Programming:** Python, C, C++, JavaScript, HTML, CSS, SQL
* **Tools & Frameworks:** ROS2, PyTorch, TensorFlow, Keras, OpenCV, NumPy, Matplotlib, Docker, AWS, GCP
* **Coursework:** ROS, Self Driving Car, Software Development, Embedded Systems, Smart Systems, AI, Deep Learning, Computer Vision, IoT, Cloud Computing

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
