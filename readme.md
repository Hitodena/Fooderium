## Fooderium

Fooderium - сайт с красивым и гибким интерфейсом, который имеет всевозможные кулинарные рецепты с пошаговой инструкцией, а также статьи, посвященные содержанию нутриентов в продуктах и их полезных свойств.

## TODO

- [x] **Configure Project**
  - [x] Set basic settings for static file storage, media files uploaded by users, timezone, etc.
  - [x] Install PostgreSQL
  - [x] Set up backend email
  - [x] Store all secrets in .env files
  - [x] Clean up project hierarchy
- [x] **Create website layout using AI/Manually (Figma)**
  - [x] Create palette for Day/Night
  - [ ] Use a framework (React, Vue, Next)
  - [x] Integrate fonts and icons
  - [x] Understand JS, buttons, and all that
  - [ ] Make it responsive for devices
- [x] **Create own API**
- [x] **Understand REST API, Django Rest Framework**
- [ ] **Create user profile application**
- [x] **Create recipes apllication**.
  - [x] Create a model about recipe in django.
  - [x] Create tags, nested tags and connect it.
  - [x] Provide all needed data via API.
  - [x] Search via name of recipe and tag.
  - [x] Connect a author of recipe with recipe.
- [ ] **Create articles application**
- [ ] **Create comments and notifications application**
- [ ] **Understand testing**
- [ ] **Customize the admin panel**
- [ ] **Make multilanguage support**
- [ ] **Deploy on hosting**
  - [ ] Connect caching, Redis or MemCached
  - [ ] Distribute load between applications on multiple servers (Microservices)
  - [ ] To secure the system from unforeseen situations, create replicas for applications and databases
  - [ ] Connect Load Balancer (NGINX, Apache)
  - [ ] Connect message broker (Kafka)
  - [ ] Explore NoSQL (MongoDB)
  - [ ] Connect Object Storage for media files, then for caching CDN
  - [ ] Create logs, analyze them using Kibana + ElasticSearch
  - [ ] Create metrics using Prometheus and Grafana

## Troubles

Relations with recipes, because they dont unique.
