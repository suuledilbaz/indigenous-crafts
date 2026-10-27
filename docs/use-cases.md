# SWE573 Indigenous Crafts – Use Cases v0.1

## UC-01 – Register and Login

**Primary Actor:** Visitor / Registered User

### Preconditions

- The user is not logged in.

### Main Flow

1. The visitor opens the registration page.
2. The system displays the registration form.
3. The visitor enters an email address and password.
4. The visitor submits the form.
5. The system creates the user account.
6. The user opens the login page.
7. The user enters valid credentials.
8. The system authenticates the user.
9. The system logs the user in.

### Alternative Flow

- If required registration fields are empty, the system displays a validation message.
- If login information is invalid, the system does not grant access.

### Postconditions

- A user account exists.
- The user can log in to the application.

---

## UC-02 – Create Craft

**Primary Actor:** Registered User

### Preconditions

- The user is registered.
- The user is logged in.

### Main Flow

1. The user opens the Create Craft page.
2. The system displays the craft creation form.
3. The user enters the craft name.
4. The user enters the craft type.
5. The user enters a description.
6. The user enters location information.
7. The user optionally enters additional craft information.
8. The user optionally adds tags.
9. The user optionally adds measurements.
10. The user optionally uploads one or more craft images.
11. The user submits the form.
12. The system validates the required fields.
13. The system stores the craft information in the database.
14. The system displays the created craft.

### Alternative Flow

- If the craft type is empty, the system displays a validation message.
- If the location is empty, the system displays a validation message.
- If other required fields are missing, the system asks the user to complete them.

### Postconditions

- A new craft record exists in the database.
- Uploaded images and additional information are associated with the craft.

---

## UC-03 – Edit or Delete Own Craft

**Primary Actor:** Registered User

### Preconditions

- The user is logged in.
- The craft belongs to the user.

### Main Flow – Edit

1. The user opens one of their craft entries.
2. The user selects Edit.
3. The system displays the existing craft information.
4. The user modifies one or more fields.
5. The user submits the changes.
6. The system saves the updated information.
7. The updated craft is displayed.

### Main Flow – Delete

1. The user opens one of their craft entries.
2. The user selects Delete.
3. The system asks for confirmation.
4. The user confirms deletion.
5. The system removes the craft from normal user access.

### Alternative Flow

- If the craft does not belong to the user, edit and delete actions are not available.

### Postconditions

- The craft is either updated or removed.

---

## UC-04 – Browse Crafts

**Primary Actor:** Visitor / Registered User

### Preconditions

- None.

### Main Flow

1. The user opens the craft listing page.
2. The system displays available crafts.
3. The user browses the available entries.
4. The user selects a craft.
5. The system opens the craft detail page.

### Postconditions

- The user can access publicly available craft information.

---

## UC-05 – Search Crafts

**Primary Actor:** Visitor / Registered User

### Preconditions

- None.

### Main Flow

1. The user opens the search function.
2. The user enters a search term.
3. The user submits the search.
4. The system searches craft data.
5. The system displays matching results.
6. The user selects a result.
7. The system opens the selected craft.

### Searchable Information May Include

- Craft name
- Craft type
- Tags
- Material
- Location
- Description

### Alternative Flow

- If no crafts match the search, the system displays a message indicating that no results were found.

### Postconditions

- Matching crafts are displayed to the user.

---

## UC-06 – View Craft Details

**Primary Actor:** Visitor / Registered User

### Preconditions

- The selected craft exists.

### Main Flow

1. The user selects a craft.
2. The system opens the craft detail page.
3. The system displays available craft information.
4. The system displays available images.
5. The system displays location information.
6. The system displays the contributing user where appropriate.
7. The system may display similar crafts.

### Postconditions

- The user can view detailed information about the craft.

---

## UC-07 – Follow Craft or User

**Primary Actor:** Registered User

### Preconditions

- The user is logged in.

### Main Flow – Follow Craft

1. The user opens a craft.
2. The user selects Follow or Save.
3. The system creates a relationship between the user and the craft.
4. The craft becomes available in the user's followed craft list.

### Main Flow – Follow User

1. The user opens another user's profile.
2. The user selects Follow.
3. The system stores the follower relationship.
4. The followed user becomes associated with the current user's account.

### Alternative Flow

- Visitors who are not logged in are asked to log in before following.

### Postconditions

- The follow relationship is stored in the database.

---

## UC-08 – Report Craft

**Primary Actor:** Registered User

### Preconditions

- The user is logged in.
- The craft exists.

### Main Flow

1. The user opens the craft detail page.
2. The user selects Report.
3. The system displays a report form.
4. The user enters a reason for the report.
5. The user submits the report.
6. The system stores the report.
7. The report becomes available for administrator review.

### Alternative Flow

- If the report reason is empty, the system asks the user to provide a reason.

### Postconditions

- A report associated with the craft exists in the system.

---

## UC-09 – Review Reported Content

**Primary Actor:** Administrator

### Preconditions

- The administrator is authenticated.
- At least one report exists.

### Main Flow

1. The administrator opens the reported content list.
2. The system displays submitted reports.
3. The administrator selects a report.
4. The system displays the related craft and report reason.
5. The administrator reviews the content.
6. The administrator may edit, correct, or remove problematic content.
7. The administrator completes the review.

### Postconditions

- Reported content has been reviewed by the administrator.
