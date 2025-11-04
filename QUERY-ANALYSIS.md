# Listing Detail Page - SQL Query Analysis

**Date:** 2025-11-04
**Listing ID:** `1586447992720x748691103167545300`
**Listing Name:** One Platt | Studio

---

## Executive Summary

I've created and tested comprehensive SQL queries to retrieve all data needed for the listing detail page. The queries successfully retrieved data for the specified listing, but several important findings emerged regarding data structure and lookup requirements.

---

## Query 1: Main Listing Data

### SQL Query
```sql
SELECT
    _id,
    "Name",
    "Description",
    "Description - Neighborhood",
    "Features - Qty Bedrooms",
    "Features - Qty Bathrooms",
    "Features - Qty Beds",
    "Features - Qty Guests",
    "Kitchen Type",
    "Location - Address",
    "neighborhood (manual input by user)",
    "host name",
    "💰Nightly Host Rate for 4 nights",
    "💰Nightly Host Rate for 2 nights",
    "💰Nightly Host Rate for 3 nights",
    "💰Nightly Host Rate for 5 nights",
    "💰Nightly Host Rate for 7 nights",
    "💰Weekly Host Rate",
    "💰Monthly Host Rate",
    "💰Cleaning Cost / Maintenance Fee",
    "💰Damage Deposit",
    "Days Available (List of Days)",
    " First Available",
    "Last Available",
    "Features - Amenities In-Unit",
    "Features - Safety",
    "Features - House Rules",
    "Features - Type of Space",
    "Features - Parking type",
    "Cancellation Policy",
    "Minimum Nights",
    "Maximum Nights",
    "NEW Date Check-in Time",
    "NEW Date Check-out Time",
    "Active",
    "Complete",
    "Location - City",
    "Location - State",
    "Location - Zip Code",
    "Location - Borough",
    "Location - Hood",
    "Features - SQFT Area",
    "Preferred Gender",
    "Features - Amenities In-Building"
FROM listing
WHERE _id = '1586447992720x748691103167545300';
```

### Key Data Retrieved

#### Basic Information
- **Name:** "One Platt | Studio"
- **Description:** Full description with 3 paragraphs about location, amenities, and nearby attractions
- **Host Name:** "Robert"
- **Neighborhood (Manual):** "Civic Center"

#### Property Features
- **Bedrooms:** 0 (Studio)
- **Bathrooms:** 1
- **Beds:** 1
- **Guests:** 2
- **Kitchen Type:** "Kitchenette"
- **Square Footage:** null (not provided)
- **Preferred Gender:** "No Preference"

#### Location Data
```json
{
  "lat": 40.7074363,
  "lng": -74.0060178,
  "address": "1 Platt St, New York, NY 10038, USA"
}
```
- **State:** "New York"
- **Zip Code:** "10038"
- **City ID:** "1534371744298x293622290249913900" (requires lookup)
- **Borough ID:** "1607041299687x679479834266385900" (requires lookup)
- **Hood ID:** "1686665230141x755924307821723600" (requires lookup)

#### Pricing Structure
- **4 Nights Rate:** $350/night
- **3 Nights Rate:** $437.50/night
- **5 Nights Rate:** $218.75/night
- **7 Nights Rate:** $156.26/night
- **2 Nights Rate:** $0 (likely not available)
- **Monthly Rate:** $2,678/month
- **Cleaning Fee:** $100
- **Damage Deposit:** $800

#### Availability
- **Days Available:** ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
- **First Available:** "2024-04-22T04:00:00.000Z"
- **Last Available:** "2049-12-31T16:00:00.000Z"
- **Minimum Nights:** 3
- **Maximum Nights:** 5
- **Check-in Time:** "2:00 pm"
- **Check-out Time:** "11:00 am"

#### Features (REQUIRE LOOKUP TABLES)

**Amenities In-Unit (5 items - IDs only):**
1. `1558470368024x124705598302821140`
2. `1555340850683x868929351440588700`
3. `1555340851282x193736739492841540`
4. `1555340855187x816189646717209200`
5. `1555340856469x472364328782922900`

**Safety Features (3 items - IDs only):**
1. `1555343668134x731801591789591700`
2. `1555343669006x402120568105726100`
3. `1555343667837x829435456336909600`

**House Rules (1 item - ID only):**
1. `1556151848468x314854653954062850`

**Other ID-based Fields:**
- **Type of Space:** `1569530331984x152755544104023800`
- **Parking Type:** `1642428637379x970678957586007000`
- **Cancellation Policy:** `1665431440883x653177548350901500`

---

## Query 2: Listing Photos

### SQL Query
```sql
SELECT
    _id,
    "Listing",
    "Name",
    "Caption",
    "Photo",
    "Photo (thumbnail)",
    "URL",
    "SortOrder",
    "Type",
    "Active",
    "toggleMainPhoto",
    "GPT Description"
FROM listing_photo
WHERE "Listing" = '1586447992720x748691103167545300'
ORDER BY "SortOrder" ASC;
```

### Photos Retrieved (7 total)

**Photo 1 (Main Photo):**
- **ID:** `1586449175258x277452762350092300`
- **Full Size:** `https://s3.amazonaws.com/appforest_uf/f1586449174807x724103464553312000/255489_1_6782894-650-570.jpg`
- **Thumbnail:** `https://s3.amazonaws.com/appforest_uf/f1610585943168x562944750334587000/small_255489_1_6782894-650-570.jpg`
- **SortOrder:** 1
- **toggleMainPhoto:** true
- **Active:** true

**Photos 2-7:**
All have:
- **SortOrder:** null (not specified)
- **toggleMainPhoto:** null or false
- **Active:** true
- Full size and thumbnail URLs available

---

## Critical Findings

### 1. Lookup Tables Required

The following fields contain IDs that require additional queries to resolve to human-readable values:

#### High Priority Lookups:
- **Amenities In-Unit** (5 IDs) - Essential for display
- **Safety Features** (3 IDs) - Essential for display
- **House Rules** (1 ID) - Essential for display
- **Type of Space** - Important for categorization
- **Parking Type** - Important feature
- **Cancellation Policy** - Critical for booking

#### Location Lookups:
- **City** - Can fallback to "New York" from address
- **Borough** - Can infer from address
- **Hood** - Already have manual input "Civic Center"

### 2. Photo Ordering Issue

Only the first photo has `SortOrder = 1`. The remaining 6 photos have `SortOrder = null`. This could cause ordering issues. Recommendations:
- Sort by `SortOrder` first, then by `_id` or `Created Date`
- Use `toggleMainPhoto = true` to identify the primary photo
- Photos without SortOrder may need manual ordering or default to creation date

### 3. Missing Data Fields

Some fields returned `null`:
- `Description - Neighborhood` (but we have manual input)
- `Features - SQFT Area`
- `💰Weekly Host Rate`
- Most photo `Caption`, `Name`, and `GPT Description` fields

### 4. Pricing Structure Anomaly

The 2-night rate is $0, suggesting it may not be available. The pricing decreases as nights increase, which is a standard volume discount pattern.

---

## Next Steps Required

### 1. Create Lookup Queries

You'll need to identify and query the following lookup tables:
- `amenity` or similar table for amenities
- `safety_feature` or similar for safety items
- `house_rule` or similar for rules
- `space_type` or similar for type of space
- `parking_type` lookup table
- `cancellation_policy` lookup table

### 2. Handle Photo Ordering

Implement logic to:
```javascript
// Pseudo-code for photo sorting
photos.sort((a, b) => {
  // Primary photo first
  if (a.toggleMainPhoto) return -1;
  if (b.toggleMainPhoto) return 1;

  // Then by SortOrder (nulls last)
  if (a.SortOrder !== null && b.SortOrder === null) return -1;
  if (a.SortOrder === null && b.SortOrder !== null) return 1;
  if (a.SortOrder !== null && b.SortOrder !== null) {
    return a.SortOrder - b.SortOrder;
  }

  // Fallback to ID or creation date
  return a._id.localeCompare(b._id);
});
```

### 3. Data Mapping to HTML

Based on your existing HTML structure, here's the mapping:

| HTML Element | Database Field |
|-------------|----------------|
| Listing Title | `Name` |
| Description | `Description` |
| Neighborhood | `neighborhood (manual input by user)` |
| Bedrooms | `Features - Qty Bedrooms` |
| Bathrooms | `Features - Qty Bathrooms` |
| Beds | `Features - Qty Beds` |
| Guests | `Features - Qty Guests` |
| Kitchen | `Kitchen Type` |
| Address | `Location - Address.address` |
| Host Name | `host name` |
| Base Price | `💰Nightly Host Rate for 4 nights` |
| Photo Gallery | `listing_photo` table results |

---

## Files Created

1. **C:\Users\Split Lease\splitleaseteam\!Agent Context and Tools\SL18\view-split-lease-1\listing-detail-queries.sql**
   - Contains both SQL queries ready to use

2. **C:\Users\Split Lease\splitleaseteam\!Agent Context and Tools\SL18\view-split-lease-1\listing-detail-data-structure.json**
   - Complete JSON representation of the data returned

3. **C:\Users\Split Lease\splitleaseteam\!Agent Context and Tools\SL18\view-split-lease-1\QUERY-ANALYSIS.md**
   - This comprehensive analysis document

---

## Recommendations

1. **Immediate:** Create lookup queries for amenities, safety, house rules, and policy fields
2. **Important:** Implement proper photo sorting logic
3. **Consider:** Adding fallback values for null fields
4. **Future:** Consider denormalizing frequently accessed lookup data for better performance

Would you like me to:
- Create the lookup queries for the ID-based fields?
- Build a JavaScript data mapping function?
- Investigate the database schema for the lookup tables?
