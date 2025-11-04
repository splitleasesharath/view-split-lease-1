-- =====================================================
-- LISTING DETAIL PAGE - SQL QUERIES
-- =====================================================
-- Listing ID: 1586447992720x748691103167545300
-- Created: 2025-11-04
-- =====================================================

-- =====================================================
-- QUERY 1: Main Listing Data
-- =====================================================
-- This query retrieves all essential listing information
-- for the detail page display

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

-- =====================================================
-- QUERY 2: Listing Photos
-- =====================================================
-- This query retrieves all photos for the listing
-- ordered by SortOrder for proper display sequence

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
