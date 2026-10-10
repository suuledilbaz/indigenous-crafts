# SWE573 Indigenous Crafts – Database Design v0.1

## 1. Overview

The Indigenous Crafts application will use **PostgreSQL** as its relational database.

The database will store users, craft entries, tags, measurements, images, and the relationships between them.

The initial design focuses on the core prototype requirements and may be extended later.

---

## 2. User

The `User` entity represents a registered user of the application.

### Fields

- `id` – unique identifier
- `email` – user email address
- `password` – user password information
- `about` – optional profile information

### Relationship

One user can create multiple crafts.

`User 1 ---- N Craft`

---

## 3. Craft

The `Craft` entity represents an indigenous craft entry created by a registered user.

### Fields

- `id` – unique identifier
- `name` – craft name
- `craft_type` – user-contributed craft type
- `description` – craft description
- `material` – material information
- `production_method` – information about how the craft is produced
- `story` – optional story or background information
- `cultural_information` – optional tools or cultural context
- `pattern` – optional pattern information
- `location` – geographical or cultural location
- `user_id` – identifies the user who created the craft

### Relationship

Each craft belongs to one user.

A user may create multiple crafts.

`User 1 ---- N Craft`

---

## 4. Tag

The `Tag` entity represents descriptive tags added to crafts.

### Fields

- `id` – unique identifier
- `name` – tag name

Examples:

- wool
- handmade
- geometric
- traditional
- anatolia
- pottery

### Relationship

A craft may have multiple tags.

A tag may be used by multiple crafts.

`Craft N ---- N Tag`

This is a many-to-many relationship.

---

## 5. Measurement

The `Measurement` entity represents a physical measurement associated with a craft.

### Fields

- `id` – unique identifier
- `name` – measurement type
- `value` – measurement value
- `unit` – measurement unit
- `craft_id` – identifies the related craft

Examples:

- Width – 120 – cm
- Length – 200 – cm
- Diameter – 35 – inch

### Relationship

One craft may have multiple measurements.

Each measurement belongs to one craft.

`Craft 1 ---- N Measurement`

---

## 6. Craft Image

The `CraftImage` entity represents an image uploaded for a craft.

### Fields

- `id` – unique identifier
- `image_path` – path or reference to the uploaded image
- `craft_id` – identifies the related craft

### Relationship

One craft may have multiple images.

Each image belongs to one craft.

`Craft 1 ---- N CraftImage`

---

## 7. Initial Relationships

User  
↓ creates  
Craft  
├── has Tag(s)  
├── has Measurement(s)  
└── has Image(s)

Detailed relationship model:

- `User 1 -------- N Craft`
- `Craft N ------- N Tag`
- `Craft 1 ------- N Measurement`
- `Craft 1 ------- N CraftImage`

---

## 8. Primary Keys

Each main database table will contain an `id` field.

The `id` field will act as the **primary key**.

A primary key uniquely identifies each record in a table.

Example:

| id | name |
|---|---|
| 1 | Anatolian Kilim |
| 2 | Clay Pot |
| 3 | Wooden Bowl |

The `id` values allow the application to distinguish between individual craft records.

---

## 9. Foreign Keys

Foreign keys are used to connect related tables.

Example User record:

| id | email |
|---|---|
| 1 | user@example.com |

Example Craft record:

| id | name | user_id |
|---|---|---|
| 12 | Anatolian Kilim | 1 |

The value `user_id = 1` means that the craft was created by the user whose `id` is `1`.

Other planned foreign keys include:

- `Measurement.craft_id`
- `CraftImage.craft_id`

---

## 10. Future Extensions

The following entities may be added later if required:

- Followed Craft
- User Follow
- Report
- Similar Craft relationships

These are not required for the first database prototype.
