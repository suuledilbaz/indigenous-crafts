# SWE573 Indigenous Crafts – Wireframes v0.1

These wireframes represent the initial interface sketches for the main user stories and use cases.

---

## WF-01 – Register / Login

Related User Stories:
- US-01 – Register
- US-02 – Login

Related Use Case:
- UC-01 – Register and Login

```text
+------------------------------------------+
|            INDIGENOUS CRAFTS             |
+------------------------------------------+
|                                          |
| Email                                    |
| [____________________________________]   |
|                                          |
| Password                                 |
| [____________________________________]   |
|                                          |
|              [ Login ]                   |
|                                          |
| Don't have an account?                   |
|              [ Register ]                |
|                                          |
+------------------------------------------+
```

---

## WF-02 – Create Craft

Related User Stories:
- US-03 – Create Craft
- US-04 – Add Craft Information
- US-05 – Add Tags
- US-06 – Add Measurements
- US-07 – Add Location
- US-08 – Upload Craft Images

Related Use Case:
- UC-02 – Create Craft

Validation Example:
Kete (bag), Riria Smith, Ahipara, New Zealand

+------------------------------------------------------------+
|                       CREATE CRAFT                         |
+------------------------------------------------------------+
|                                                            |
| Craft Name *                                               |
| [ Kete (bag)___________________________________________ ]  |
|                                                            |
| Craft Type *                                               |
| [ Kete / Woven Bag ▼ ]                                     |
| [ Other / Add New Craft Type ]                             |
|                                                            |
| Culture / Community *                                      |
| [ Māori ▼ ]                                                |
| [ Other / Add New Community ]                              |                                                          
|                                                            |
| Location *                                                 |
| [ Ahipara, New Zealand_________________________________ ]  |
|                                                            |
| Description                                                |
| [ Woven kete with a flat base and flap.________________ ] |
| [______________________________________________________ ] |
|                                                            |
| MATERIALS                                                  |
|                                                            |
| [ Harakeke × ] [ Muka × ] [ Wood × ] [ Cotton × ]         |
|                                                            |
| [ + Add Material ▼ ]                                       |
| [ View material information ]                              |
| [ Other / Add New Material ]                               |
|                                                            |
| TECHNIQUES / PRODUCTION METHODS                            |
|                                                            |
| [ Raranga × ] [ Braiding × ] [ Sewing × ]                  |
|                                                            |
| [ + Add Technique ▼ ]                                      |
| [ View technique information ]                             |
| [ Other / Add New Technique ]                              |
|                                                            |
| TOOLS                                                      |
|                                                            |
| [ Select Tool ▼ ] [ + Add Tool ]                           |
| [ View tool information ]                                  |
| [ Other / Add New Tool ]                                   |
|                                                            |
| Story / Background                                         |
| [______________________________________________________ ] |
| [______________________________________________________ ] |
|                                                            |
| Cultural Information                                      |
| [______________________________________________________ ] |
| [______________________________________________________ ] |
|                                                            |
| TAGS                                                       |
|                                                            |
| [ Māori × ] [ weaving × ] [ kete × ] [ + Add Tag ]        |
|                                                            |
| COLORS                                                     |
|                                                            |
| Color Family                                               |
| [ Green ▼ ]                                                |
|                                                            |
| Shade                                                      |
| [ Not specified ▼ ]                                        |
|                                                            |
| [ + Add Color ] [ Other / Add Custom Shade ]               |
|                                                            |
| PATTERN                                                    |
|                                                            |
| [ Takitahi ▼ ]                                             |
| [ View pattern information ]                               |
| [ Other / Add New Pattern ]                                |
|                                                            |
| Distinguished Features                                    |
| [ Flat base____________________________________________ ] |
| [ Flap with wooden button______________________________ ] |
| [ Braided muka handle__________________________________ ] |
| [ Green cotton lining__________________________________ ] |
|                                                            |
| MEASUREMENTS                                               |
|                                                            |
| [ Width  ] [ 260    ] [ mm ▼ ]                             |
| [ Height ] [ 185    ] [ mm ▼ ]                             |
| [ Weight ] [ 159.07 ] [ g  ▼ ]                             |
|                                                            |
| [ + Add Measurement ]                                      |
|                                                            |
| IMAGES                                                     |
|                                                            |
| [ Upload Image ] [ + Add Another Image ]                   |
|                                                            |
|                       [ Create Craft ]                     |
|                                                            |
+------------------------------------------------------------+

* Required field

Design Notes

Craft Type uses controlled options but allows user-contributed types through Other / Add New.

Culture / Community is explicitly recorded because cultural association is important for an indigenous craft application.

Materials are multiple-select rather than a single value.

Techniques are multiple-select because one craft may use several techniques.

Materials, techniques, tools, and patterns have explanatory information available to the user.

Unknown terms can be contributed using an Other / Add New option.

Colors support a color family and a more specific shade.

Measurements are dynamic and support different measurement names and units.

Description, Story / Background, Cultural Information, and Distinguished Features remain flexible text fields.

Images support multiple uploads.
---

## WF-03 – Browse and Search Crafts

Related User Stories:
- US-11 – Browse Crafts
- US-12 – Search Crafts

Related Use Cases:
- UC-04 – Browse Crafts
- UC-05 – Search Crafts

```text
+------------------------------------------------+
|              INDIGENOUS CRAFTS                 |
+------------------------------------------------+
|                                                |
| Search                                         |
| [_______________________________] [ Search ]   |
|                                                |
+------------------------------------------------+
|                                                |
| CRAFTS                                         |
|                                                |
| +--------------------+  +--------------------+ |
| |      [Image]       |  |      [Image]       | |
| |                    |  |                    | |
| | Craft Name         |  | Craft Name         | |
| | Craft Type         |  | Craft Type         | |
| | Location           |  | Location           | |
| |                    |  |                    | |
| | [ View Details ]   |  | [ View Details ]   | |
| +--------------------+  +--------------------+ |
|                                                |
| +--------------------+  +--------------------+ |
| |      [Image]       |  |      [Image]       | |
| | Craft Name         |  | Craft Name         | |
| | Craft Type         |  | Craft Type         | |
| | Location           |  | Location           | |
| | [ View Details ]   |  | [ View Details ]   | |
| +--------------------+  +--------------------+ |
|                                                |
+------------------------------------------------+
```

---

## WF-04 – Craft Detail

Related User Stories:
- US-13 – View Craft Details
- US-14 – View Similar Crafts
- US-15 – Follow Craft

Related Use Case:
- UC-06 – View Craft Details

+------------------------------------------------------------+
|                       CRAFT DETAIL                         |
+------------------------------------------------------------+
|                                                            |
| Kete (bag)                                                 |
|                                                            |
| [                      Main Image                      ]   |
|                                                            |
| [ Image 2 ] [ Image 3 ]                                    |
|                                                            |
| Craft Type                                                 |
| Kete / Woven Bag                                           |
|                                                            |
| Culture / Community                                        |
| Māori                                                      |
|                                                            |                                             
|                                                            |
| Location                                                   |
| Ahipara, New Zealand                                       |
|                                                            |
+------------------------------------------------------------+
| MATERIALS                                                  |
|                                                            |
| Harakeke     [ What is this? ]                             |
| Muka         [ What is this? ]                             |
| Wood         [ What is this? ]                             |
| Cotton       [ What is this? ]                             |
|                                                            |
+------------------------------------------------------------+
| TECHNIQUES                                                 |
|                                                            |
| Raranga      [ What is this? ]                             |
| Braiding     [ What is this? ]                             |
| Sewing       [ What is this? ]                             |
|                                                            |
+------------------------------------------------------------+
| TOOLS                                                      |
|                                                            |
| Not specified                                              |
|                                                            |
+------------------------------------------------------------+
| TAGS                                                       |
|                                                            |
| [ Māori ] [ weaving ] [ kete ]                             |
|                                                            |
+------------------------------------------------------------+
| COLORS                                                     |
|                                                            |
| Green                                                      |
| Shade: Not specified                                       |
|                                                            |
+------------------------------------------------------------+
| PATTERN                                                    |
|                                                            |
| Takitahi          [ What is this? ]                        |
|                                                            |
+------------------------------------------------------------+
| DESCRIPTION                                                |
|                                                            |
| Woven kete with a flat base and flap.                      |
|                                                            |
+------------------------------------------------------------+
| STORY / BACKGROUND                                         |
|                                                            |
| No additional story provided.                              |
|                                                            |
+------------------------------------------------------------+
| CULTURAL INFORMATION                                       |
|                                                            |
| No additional cultural information provided.               |
|                                                            |
+------------------------------------------------------------+
| DISTINGUISHED FEATURES                                     |
|                                                            |
| • Flat base                                                |
| • Flap closure                                             |
| • Wooden button                                            |
| • Braided muka handle with decorative tassels              |
| • Green cotton lining                                      |
|                                                            |
+------------------------------------------------------------+
| MEASUREMENTS                                               |
|                                                            |
| Width:   260 mm                                            |
| Height:  185 mm                                            |
| Weight:  159.07 g                                          |
|                                                            |
+------------------------------------------------------------+
| Contributed by: User                                       |
|                                                            |
| [ Follow Craft ]                                           |
|                                                            |
+------------------------------------------------------------+
|                      SIMILAR CRAFTS                        |
|                                                            |
| [ Craft Card ]   [ Craft Card ]   [ Craft Card ]           |
|                                                            |
---

## WF-05 – Edit Craft

Related User Story:
- US-09 – Edit Own Craft

Related Use Case:
- UC-03 – Edit or Delete Own Craft

```text
+------------------------------------------------+
|                   EDIT CRAFT                   |
+------------------------------------------------+
|                                                |
| Craft Name                                     |
| [Existing value____________________________]   |
|                                                |
| Craft Type                                     |
| [Existing value____________________________]   |
|                                                |
| Location                                       |
| [Existing value____________________________]   |
|                                                |
| Description                                    |
| [Existing value____________________________]   |
| [__________________________________________]   |
|                                                |
| Tags                                           |
| [Existing tags] [ + Add Tag ]                  |
|                                                |
| Measurements                                   |
| [Existing measurements]                        |
| [ + Add Measurement ]                          |
|                                                |
| Images                                         |
| [Existing images] [ Upload Image ]             |
|                                                |
|                 [ Save Changes ]               |
|                                                |
+------------------------------------------------+
```

---

## WF-06 – User Profile

Related User Stories:
- US-16 – Follow User
- US-15 – Follow Craft

Related Use Case:
- UC-07 – Follow Craft or User

```text
+------------------------------------------------+
|                  USER PROFILE                  |
+------------------------------------------------+
|                                                |
| User Name                                      |
|                                                |
| About                                          |
| [__________________________________________]   |
| [__________________________________________]   |
|                                                |
|              [ Follow User ]                   |
|                                                |
+------------------------------------------------+
|                USER'S CRAFTS                   |
|                                                |
| [Craft Card]   [Craft Card]   [Craft Card]     |
|                                                |
+------------------------------------------------+
|               FOLLOWED CRAFTS                  |
|                                                |
| [Craft Card]   [Craft Card]                    |
|                                                |
+------------------------------------------------+
```

---

## WF-07 – Report Craft

Related User Stories:
- US-17 – Report Craft
- US-18 – Manage Reported Content

Related Use Cases:
- UC-08 – Report Craft
- UC-09 – Review Reported Content

Priority:
- Should Have

```text
+------------------------------------------+
|              REPORT CRAFT                |
+------------------------------------------+
|                                          |
| Craft: Example Craft                     |
|                                          |
| Reason for Report                        |
| [____________________________________]   |
| [____________________________________]   |
| [____________________________________]   |
|                                          |
|          [ Submit Report ]               |
|                                          |
+------------------------------------------+
```

---

## WF-08 – Admin Report Review

Related User Story:
- US-18 – Manage Reported Content

Related Use Case:
- UC-09 – Review Reported Content

Priority:
- Should Have

```text
+------------------------------------------------+
|               REPORTED CONTENT                 |
+------------------------------------------------+
|                                                |
| Reported Craft: Example Craft                  |
| Reported By: User                              |
|                                                |
| Reason                                         |
| [__________________________________________]   |
|                                                |
| [ View Craft ]                                 |
|                                                |
| [ Edit Content ]                               |
| [ Remove Content ]                             |
| [ Mark as Reviewed ]                           |
|                                                |
+------------------------------------------------+
```

---

# Notes

- These wireframes are low-fidelity interface sketches.
- Their purpose is to show the main user interactions and screen structure.
- Visual styling, colors, fonts, and final layout will be decided during frontend implementation.
- Report functionality is classified as **Should Have** and is not required for the initial prototype.
