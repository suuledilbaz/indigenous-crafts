
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
-
