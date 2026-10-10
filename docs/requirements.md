# SWE573 Indigenous Crafts – Requirements v0.2

## 1. Project Overview

**Indigenous Crafts** is a domain-specific web application where users can discover, search, and contribute information about indigenous crafts.

The application will support user-created craft entries, flexible craft types and tags, location information, craft characteristics, and basic social interactions.

The system will be implemented using Python and Flask and will include a database, API, Docker support, and online deployment.

---

# 2. User Types

## Visitor

Visitors shall be able to:

- Browse crafts
- View craft details
- Search for crafts

Registration shall not be required for browsing or searching.

## Registered User

Registered users shall be able to:

- Create and manage a profile
- Create craft entries
- Edit and delete their own craft entries
- Upload craft images
- Add craft types and tags
- Follow crafts
- Follow other users
- Report incorrect craft information

## Administrator

The administrator shall be able to manage application data and review reported content when necessary.

---

# 3. Functional Requirements

## FR-01 – User Registration and Login

The system shall allow users to register using an email address and password.

Registered users shall be able to log in and log out.

---

## FR-02 – User Profile

The system shall provide a profile page for each registered user.

The profile shall include an About section and may display crafts contributed by the user.

---

## FR-03 – Create Craft

Registered users shall be able to create craft entries.

A craft entry shall include at least:

- Name
- Craft type
- Description
- Location

Craft type and location shall not be empty.

---

## FR-04 – Craft Information

Users shall be able to provide additional information about a craft, including:

- Material
- Production method
- Story or background
- Tools or cultural information
- Colors
- Pattern
- Distinguished features
- Measurements
- Images

These fields may be optional depending on the craft.

---

## FR-05 – User-Contributed Craft Type

Registered users shall be able to define the craft type while creating a craft.

Craft types shall not require administrator approval before submission.

---

## FR-06 – Tags

Registered users shall be able to add one or more tags to a craft.

Tags may be used to describe characteristics such as material, style, region, or technique.

---

## FR-07 – Measurements

The system shall allow users to define measurements using:

- Measurement name
- Value
- Unit

Examples of units may include:

- cm
- m
- inch

---

## FR-08 – Location

Each craft shall include location information.

The system shall store or display geolocation information.

Displaying a map pin is not mandatory for the initial version.

---

## FR-09 – Edit and Delete Craft

Registered users shall be able to edit and delete craft entries they created.

---

## FR-10 – Craft Images

Registered users shall be able to upload one or more images for a craft.

---

## FR-11 – Browse Crafts

Visitors and registered users shall be able to browse available crafts.

---

## FR-12 – Search Crafts

Visitors and registered users shall be able to search for crafts.

Search may use information such as:

- Name
- Craft type
- Tags
- Material
- Location
- Description

---

## FR-13 – Craft Detail

The system shall provide a detail page for each craft.

The page shall display the available information associated with the craft.

---

## FR-14 – Similar Crafts

The system shall support displaying crafts that are similar to a selected craft.

The exact similarity logic will be finalized during design and implementation.

---

## FR-15 – Follow Craft

Registered users shall be able to follow or save crafts they are interested in.

The exact follow behavior will be finalized during design.

---

## FR-16 – Follow User

Registered users shall be able to follow other registered users.

---

## FR-17 – Report Craft

Registered users shall be able to report craft entries containing incorrect or inappropriate information.

The administrator shall be able to review reported content.

---

## FR-18 – API

The application shall provide a developer-created API for accessing craft-related data and application functionality.

---

# 4. Non-Functional Requirements

## NFR-01 – Web Application

The system shall operate as a web application accessible through a standard web browser.

---

## NFR-02 – Backend Technology

The backend shall be implemented using Python and Flask.

---

## NFR-03 – Database

The application shall use a database to persist user and craft information.

---

## NFR-04 – Docker

The application shall be containerized using Docker.

---

## NFR-05 – Deployment

The application shall be deployed to an online environment.

---

## NFR-06 – GitHub

The project source code and development history shall be maintained in GitHub.

Development activities shall be tracked using GitHub Issues.

---

# 5. Mandatory Project Deliverables

The project shall include:

- Requirements
- User stories
- Use cases
- Wireframes or interface sketches
- Functional Flask application
- Database integration
- API
- Docker configuration
- Deployed application
- GitHub issue and development history

---

# 6. Initial Prototype Scope

The initial prototype should demonstrate the basic system flow.

The prototype should include at least:

- Basic user registration and login
- Craft creation
- Craft storage in the database
- Craft listing
- Craft detail page
- Search
- Basic API
- Basic interface
- Docker support
- Initial deployed version

The initial prototype is targeted for approximately two weeks after the latest requirement update.

---

# 7. Open Design Decisions

The following decisions will be finalized during design:

## Follow Behavior

Determine whether following a craft only saves it to a personal list or also provides updates.

## Similarity Logic

Determine how similar crafts will be identified using attributes such as:

- Craft type
- Tags
- Material
- Location
- Production method

---

# 8. Requirements Validation

Requirements shall later be validated against:

- User stories
- Use cases
- Wireframes
- Implemented functionality

Each important requirement should be traceable to at least one user story or use case.
