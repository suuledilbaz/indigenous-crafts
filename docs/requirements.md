# SWE573 Indigenous Crafts – Requirements v0.1

## 1. Project Overview

**Indigenous Crafts** is a domain-specific, informative web application for people who are interested in crafts.

The platform will allow users to discover different types of crafts, search for craft-related content, find similar crafts, follow crafts, and follow other users.

The application is intended to support different types of crafts rather than focusing on a single craft category.

Each craft entry will contain descriptive and domain-specific information such as:

- Name
- Description
- Category
- Material
- Production method
- Location
- Measurements and units
- Images

The system will be developed as a web application with a frontend, backend, database, API, containerization, and deployment environment.

---

# 2. Target Users

## 2.1 Visitor

A visitor is a user who accesses the platform without registering or logging in.

Visitors shall be able to:

- Browse crafts
- View craft details
- Search for crafts

Registration shall not be required for browsing or searching.

---

## 2.2 Registered User

A registered user is a person who creates an account using an email address and password.

Registered users shall be able to:

- Create and manage their profile
- Upload crafts
- Edit crafts they uploaded
- Delete crafts they uploaded
- Upload craft images
- Browse crafts
- Search for crafts
- Follow crafts
- Follow other users
- Discover similar crafts

---

## 2.3 Administrator

The system shall include an administrator role.

For the scope of the course project, the developer of the system may act as the administrator.

The administrator will be responsible for basic system administration and content management when necessary.

Uploaded crafts do not require administrator approval before being published.

---

# 3. Functional Requirements

## FR-01 – User Registration

The system shall allow users to create an account using:

- Email address
- Password

---

## FR-02 – User Authentication

The system shall allow registered users to log in using their email address and password.

The system shall allow logged-in users to log out.

---

## FR-03 – User Profile

The system shall provide a profile page for each registered user.

A user profile shall include at least:

- User identity information
- An About section

The profile may also display crafts uploaded by the user.

---

## FR-04 – Browse Crafts

The system shall allow visitors and registered users to browse crafts available on the platform.

Registration shall not be required for browsing crafts.

---

## FR-05 – Craft Detail Page

The system shall provide a detail page for each craft.

The detail page shall display available information associated with the selected craft.

---

## FR-06 – Craft Description

Each craft shall contain a textual description.

---

## FR-07 – Craft Material

The system shall allow the material used in a craft to be specified.

Examples may include:

- Wool
- Cotton
- Clay
- Wood
- Metal
- Stone

---

## FR-08 – Production Method

The system shall allow information about how a craft was produced to be recorded.

Examples may include:

- Handwoven
- Hand-carved
- Molded
- Painted
- Embroidered
- Hand-built

---

## FR-09 – Craft Location

The system shall allow a geographical location to be associated with a craft.

---

## FR-10 – Craft Type / Category

The system shall allow crafts to be categorized.

The platform shall support multiple types of crafts.

---

## FR-11 – Craft Measurement

The system shall support physical measurements associated with a craft.

Measurements may vary according to the type of craft.

For example, a kilim may have:

- Width
- Length

Measurement values shall be stored together with their units.

Examples of units may include:

- cm
- m
- mm

---

## FR-12 – Upload Craft

The system shall allow registered users to create and upload craft entries.

A user must be authenticated before creating a craft entry.

---

## FR-13 – No Approval Required for Craft Upload

A craft uploaded by a registered user shall not require administrator approval before becoming available on the platform.

---

## FR-14 – Search Crafts

The system shall provide search functionality for finding crafts.

Both visitors and registered users shall be able to use search functionality.

Search may use information such as:

- Craft name
- Category
- Material
- Location
- Description

---

## FR-15 – Find Similar Crafts

The system shall allow users to discover crafts similar to a selected craft.

Similarity may be determined using one or more craft properties such as:

- Category
- Material
- Location
- Production method

The exact similarity logic will be finalized during the design phase.

---

## FR-16 – Follow Crafts

The system shall allow registered users to follow crafts they are interested in.

The exact behavior of following a craft will be finalized during the design phase.

---

## FR-17 – Follow Users

The system shall allow registered users to follow other registered users.

---

## FR-18 – View User Contributions

The system shall allow users to view crafts contributed by a particular registered user.

---

## FR-19 – Backend API

The system shall provide an API for accessing application functionality and craft-related data.

The API shall be implemented as part of the project.

---

## FR-20 – Administration

The system shall provide basic administrative functionality.

---

## FR-21 – Craft Images

The system shall allow registered users to upload one or more images for a craft.

Craft images shall be displayed on the craft detail page.

---

## FR-22 – Edit Craft

The system shall allow registered users to edit craft entries they previously uploaded.

Users shall not be able to edit crafts uploaded by other users through normal user functionality.

---

## FR-23 – Delete Craft

The system shall allow registered users to delete craft entries they previously uploaded.

Users shall not be able to delete crafts uploaded by other users through normal user functionality.

---

# 4. Non-Functional Requirements

## NFR-01 – Web-Based Application

The application shall operate as a web application accessible through a standard web browser.

---

## NFR-02 – Backend Technology

The backend shall be implemented in **Python**.

The planned backend framework is **Django**.

---

## NFR-03 – Frontend Technology

The system shall contain a web-based frontend.

The frontend technology may be selected by the developer.

---

## NFR-04 – Database

The application shall use a database to persist application data.

The final database technology will be selected during the design phase.

---

## NFR-05 – API Architecture

The application shall provide a developer-created API.

---

## NFR-06 – Containerization

The application shall be containerized using Docker.

---

## NFR-07 – Deployment

The application shall be deployed to an online hosting environment.

A free or student-friendly deployment platform may be used.

---

## NFR-08 – Version Control

The source code shall be maintained in GitHub.

Git shall be used for source control.

---

## NFR-09 – Issue Tracking

Development tasks shall be tracked through GitHub Issues.

---

## NFR-10 – Development Traceability

Project progress should be visible through:

- Commits
- Issues
- Issue history
- Branches where appropriate
- Pull requests where appropriate
- Project backlog

---

## NFR-11 – Basic Functionality

The application is not required to provide production-level completeness.

However, the fundamental functionality defined in the project requirements shall be demonstrable.

---

## NFR-12 – Maintainability

The source code shall be organized into understandable modules and components.

---

# 5. Project Constraints

## PC-01 – Course Deadline

The project shall be completed by **December 12**.

## PC-02 – Backend Language

The backend shall be implemented using Python.

## PC-03 – Docker

Docker shall be used as part of the project.

## PC-04 – Deployment

The final application shall have a deployed version.

## PC-05 – GitHub Development

Development shall be maintained and documented through GitHub.

## PC-06 – API Requirement

The application shall include an API created as part of the project.

---

# 6. Domain Model Candidates

## User

Possible attributes:

- ID
- Email
- Password
- About
- Registration date

## Craft

Possible attributes:

- ID
- Name
- Description
- Category
- Material
- Production method
- Location
- Measurement value
- Measurement unit
- Owner / contributor
- Creation date

## Craft Image

Possible attributes:

- ID
- Image
- Craft
- Upload date

## Craft Category

Possible attributes:

- ID
- Name
- Description

## Material

Possible attributes:

- ID
- Name
- Description

## Location

Possible attributes:

- ID
- Country
- Region
- City or locality

## Followed Craft

Relationship between:

- User
- Craft

## User Follow

Relationship between:

- Follower
- Followed user

---

# 7. Initial Relationships

```text
User
 |
 | uploads
 v
Craft
 |
 +---- has Category
 |
 +---- uses Material
 |
 +---- associated with Location
 |
 +---- has Production Method
 |
 +---- has Measurement
 |
 +---- has Image(s)
```

User interaction relationships:

```text
User ---- follows ----> User

User ---- follows ----> Craft
```

---

# 8. Initial MVP Scope

The first working version of the application should contain:

1. User registration
2. User login
3. User logout
4. User profile
5. About section
6. Create craft
7. Edit own craft
8. Delete own craft
9. Upload craft image(s)
10. View craft list
11. View craft details
12. Craft categories
13. Material information
14. Production method information
15. Location information
16. Craft measurement and unit
17. Craft search
18. Follow craft
19. Follow user
20. Similar craft functionality
21. Basic administrator functionality
22. Backend API
23. Database persistence
24. Docker containerization
25. Online deployment

---

# 9. Requirements That Need Further Clarification

## OQ-01 – Follow Definition

What should following a craft mean?

Possible options:

### Option A – Saved / Followed Craft List

Following a craft adds it to the user's personal followed crafts list.

### Option B – Updates

Following a craft means receiving updates related to the craft.

**Status:** To be finalized.

---

## OQ-02 – Similarity Logic

How will the system determine that two crafts are similar?

Possible criteria include:

- Same material
- Same category
- Same location
- Same production method

**Status:** To be finalized during the design phase.

---

# 10. Initial Requirement Priorities

## Must Have

- User registration
- Authentication
- User profile
- Craft creation
- Craft editing
- Craft deletion
- Craft images
- Craft listing
- Craft detail
- Craft categories
- Material
- Production method
- Location
- Measurements and units
- Search
- API
- Database
- GitHub development
- Docker
- Deployment

## Should Have

- Follow crafts
- Follow users
- View user contributions
- Similar crafts

## Could Have / Future Enhancement

- More advanced similarity
- Advanced filtering
- More detailed craft metadata
- Ontology or controlled vocabulary

---

# 11. Initial Project Success Criteria

The project will be considered technically successful when:

- The application can be accessed as a web application.
- Visitors can browse and search crafts without registering.
- A user can register and log in.
- A registered user can create craft records.
- A registered user can edit crafts they created.
- A registered user can delete crafts they created.
- A registered user can upload images for a craft.
- Craft information can be stored in a database.
- Craft details can be displayed.
- User profiles are available.
- Users can follow crafts and users.
- Similar crafts can be displayed.
- The application exposes a working API.
- The application can run using Docker.
- The application has a deployed version.
- Development history is documented in GitHub.
- GitHub contains an actively maintained backlog and issue history.
