## Fooderium

Fooderium - сайт с красивым и гибким интерфейсом, который имеет всевозможные кулинарные рецепты с пошаговой инструкцией, а также статьи, посвященные содержанию нутриентов в продуктах и их полезных свойств.

## TODO

- [x] **Configure Project**
  - [x] Set basic settings for static file storage, media files uploaded by users, timezone, etc.
  - [x] Install PostgreSQL
  - [x] Set up backend email
  - [x] Store all secrets in .env files
  - [x] Clean up project hierarchy
- [ ] **Create website layout using AI/Manually (Figma)**
  - [ ] Create palette for Day/Night
  - [ ] Use a framework (React, Vue, Next)
  - [ ] Integrate fonts and icons
  - [ ] Understand JS, buttons, and all that
  - [ ] Make it responsive for devices
- [ ] **Create user profile application**
  - [ ] Create a database for user profiles (built into Django) that includes username, photo, articles, recipes, description
  - [ ] Implement registration with login, login, logout
  - [ ] Implement profile editing, password reset via email
  - [ ] Implement email messaging
- [ ] **Create recipe application**
  - [ ] Create a database for recipes that includes the creator (user), recipe ingredients (in the `articles` app), tags, creation date, title, comments, etc.
  - [ ] Create a database for recipe tags, including subtags (tags within main tags)
  - [ ] Implement recipe upload from CSV, output, edit, delete using class methods
  - [ ] Implement search by composition, macronutrients, pagination
- [ ] **Create articles application**
  - [ ] Create a database for articles, which can be just facts about products/different cuisines, but also every product from a recipe, if there is an article about it; it will include nutrients and interesting facts, as well as tags and article creator. Articles about products will be unique; there cannot be two articles about the same product since one article will be its description, nutrient composition, and useful information. It can only be supplemented, like in Wikipedia, and comments can be added.
  - [ ] Create a database for article tags and subtags
  - [ ] Implement article upload from CSV, output, edit, delete using class methods
  - [ ] Implement search, pagination
- [ ] **Create comments and notifications application**
  - [ ] Create a database for comments, which include the user who left them, time, the comment itself, etc., and what they are related to (recipe or article)
- [ ] **Understand testing**
- [ ] **Customize the admin panel**
- [ ] **Create own API and understand REST**
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
