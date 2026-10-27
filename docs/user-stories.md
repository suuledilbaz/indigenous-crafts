# SWE573 Indigenous Crafts – User Stories v0.1

## US-01 – Register

**As a visitor,**  
I want to create an account,  
so that I can contribute crafts and use registered-user features.

### Acceptance Criteria

- The user can register with an email address and password.
- Required fields cannot be left empty.
- After successful registration, the account is created.

---

## US-02 – Login

**As a registered user,**  
I want to log in to the application,  
so that I can access my account and contribute content.

### Acceptance Criteria

- The user can log in using their registered credentials.
- Invalid login information does not grant access.
- A logged-in user can log out.

---

## US-03 – Create Craft

**As a registered user,**  
I want to create a craft entry,  
so that I can contribute information about an indigenous craft.

### Acceptance Criteria

- Only registered users can create craft entries.
- The user can enter a craft name.
- The user can define the craft type.
- The user can enter a description.
- The user can provide location information.
- Craft type and location cannot be empty.
- The craft is stored in the database after successful submission.

---

## US-04 – Add Craft Information

**As a registered user,**  
I want to add descriptive information about a craft,  
so that other users can understand its characteristics and cultural context.

### Acceptance Criteria

The user can optionally provide information such as:

- Material
- Production method
- Story or background
- Tools or cultural information
- Colors
- Pattern
- Distinguished features

---

## US-05 – Add Tags

**As a registered user,**  
I want to add tags to a craft,  
so that the craft can be described and discovered more easily.

### Acceptance Criteria

- A craft can have one or more tags.
- Users can enter their own tags.
- Tags are associated with the craft after submission.

---

## US-06 – Add Measurements

**As a registered user,**  
I want to define measurements for a craft,  
so that its physical properties can be documented.

### Acceptance Criteria

- The user can define a measurement name.
- The user can enter a measurement value.
- The user can select or enter a measurement unit.
- Multiple measurements can be added to one craft.

Examples:

- Width – 120 – cm
- Length – 200 – cm
- Diameter – 25 – inch

---

## US-07 – Add Location

**As a registered user,**  
I want to provide location information for a craft,  
so that users can understand where the craft originates from or is associated with.

### Acceptance Criteria

- Location information must be provided when creating a craft.
- Location information is stored with the craft.
- Geolocation information can be displayed.
- A map pin is not mandatory for the initial version.

---

## US-08 – Upload Craft Images

**As a registered user,**  
I want to upload images of a craft,  
so that other users can visually identify it.

### Acceptance Criteria

- The user can upload one or more craft images.
- Uploaded images are associated with the relevant craft.
- Images can be displayed on the craft detail page.

---

## US-09 – Edit Own Craft

**As a registered user,**  
I want to edit a craft that I created,  
so that I can correct or improve its information.

### Acceptance Criteria

- A user can edit their own craft entries.
- A user cannot normally edit another user's craft.
- Updated information is saved to the database.

---

## US-10 – Delete Own Craft

**As a registered user,**  
I want to delete a craft that I created,  
so that I can remove content that is no longer relevant or correct.

### Acceptance Criteria

- A user can delete their own craft entries.
- A user cannot normally delete another user's craft.
- Deleted crafts are removed from normal user access.

---

## US-11 – Browse Crafts

**As a visitor,**  
I want to browse available crafts,  
so that I can discover indigenous crafts without creating an account.

### Acceptance Criteria

- Registration is not required.
- Available crafts can be displayed in a list or similar interface.
- The user can open a craft detail page.

---

## US-12 – Search Crafts

**As a visitor,**  
I want to search for crafts,  
so that I can quickly find crafts related to my interests.

### Acceptance Criteria

- Registration is not required for search.
- The user can enter a search term.
- The system displays matching crafts.
- Search may consider information such as:
  - Craft name
  - Craft type
  - Tags
  - Material
  - Location
  - Description

---

## US-13 – View Craft Details

**As a visitor,**  
I want to view the details of a craft,  
so that I can learn more about it.

### Acceptance Criteria

- The craft detail page displays the available craft information.
- Available images can be displayed.
- Location information can be displayed.
- The contributing user can be identified where appropriate.

---

## US-14 – View Similar Crafts

**As a user,**  
I want to see crafts similar to the craft I am viewing,  
so that I can discover related crafts.

### Acceptance Criteria

- The system can display related or similar crafts.
- Similarity may use attributes such as:
  - Craft type
  - Tags
  - Material
  - Location
  - Production method
- The exact similarity logic can be refined during implementation.

---

## US-15 – Follow Craft

**As a registered user,**  
I want to follow a craft,  
so that I can easily access crafts that interest me later.

### Acceptance Criteria

- Only registered users can follow crafts.
- Followed crafts are associated with the user's account.
- The user can view their followed crafts.

**Open Decision:**  
Whether following also provides updates will be finalized later.

---

## US-16 – Follow User

**As a registered user,**  
I want to follow another user,  
so that I can easily find contributors whose crafts interest me.

### Acceptance Criteria

- Registered users can follow other registered users.
- The follower relationship is stored by the system.
- A user can access information about users they follow.

---

## US-17 – Report Craft

**As a registered user,**  
I want to report incorrect or inappropriate craft information,  
so that problematic content can be reviewed.

### Acceptance Criteria

- A registered user can report a craft.
- The report is associated with the relevant craft.
- The administrator can review submitted reports.

---

## US-18 – Manage Reported Content

**As an administrator,**  
I want to review reported craft content,  
so that I can correct or remove problematic information when necessary.

### Acceptance Criteria

- The administrator can view reported crafts.
- The administrator can review the report reason.
- The administrator can correct, manage, or remove content when necessary.

---

# Initial Priority

## Must Have

- US-01 Register
- US-02 Login
- US-03 Create Craft
- US-04 Add Craft Information
- US-05 Add Tags
- US-06 Add Measurements
- US-07 Add Location
- US-08 Upload Craft Images
- US-09 Edit Own Craft
- US-10 Delete Own Craft
- US-11 Browse Crafts
- US-12 Search Crafts
- US-13 View Craft Details

## Should Have

- US-14 View Similar Crafts
- US-15 Follow Craft
- US-16 Follow User
- US-17 Report Craft
- US-18 Manage Reported Content
