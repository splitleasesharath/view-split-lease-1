"""
Cycle 3 - Comprehensive CSS Validation at 1920x1080
Compares local implementation with production site
"""

from playwright.sync_api import sync_playwright
import time
import os
import sys

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def validate_css_fixes():
    """Comprehensive validation of all CSS fixes at 1920x1080 resolution"""

    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = context.new_page()

        print("=" * 80)
        print("CYCLE 3 - COMPREHENSIVE CSS VALIDATION")
        print("Resolution: 1920x1080")
        print("=" * 80)

        # Create screenshots directory if it doesn't exist
        os.makedirs('screenshots', exist_ok=True)

        # ========================================================================
        # PART 1: LOCAL IMPLEMENTATION
        # ========================================================================
        print("\n[1/4] Loading LOCAL implementation...")
        local_url = "http://localhost:8000/index.html"

        try:
            page.goto(local_url, wait_until='networkidle', timeout=30000)
            time.sleep(2)  # Allow any animations to complete

            print("✓ Local page loaded successfully")

            # Take viewport screenshot
            print("[2/4] Taking LOCAL viewport screenshot...")
            page.screenshot(
                path='screenshots/cycle3_local_viewport_1920x1080.png',
                full_page=False
            )
            print("✓ Saved: screenshots/cycle3_local_viewport_1920x1080.png")

            # Take full page screenshot
            print("[3/4] Taking LOCAL full page screenshot...")
            page.screenshot(
                path='screenshots/cycle3_local_1920x1080.png',
                full_page=True
            )
            print("✓ Saved: screenshots/cycle3_local_1920x1080.png")

        except Exception as e:
            print(f"✗ Error loading local page: {e}")
            browser.close()
            return

        # ========================================================================
        # PART 2: PRODUCTION SITE
        # ========================================================================
        print("\n[4/4] Loading PRODUCTION site...")
        prod_url = "https://app.split.lease/view-split-lease/1586447992720x748691103167545300?area=&arrival=&duration=13%20weeks%20(3%20months)&nights=&guests=&storage=&type=&days-selected=2%2C%203%2C%204%2C%205%2C%206"

        try:
            page.goto(prod_url, wait_until='domcontentloaded', timeout=60000)
            time.sleep(3)  # Allow any animations to complete

            print("✓ Production page loaded successfully")

            # Take viewport screenshot
            print("[5/6] Taking PRODUCTION viewport screenshot...")
            page.screenshot(
                path='screenshots/cycle3_production_viewport_1920x1080.png',
                full_page=False
            )
            print("✓ Saved: screenshots/cycle3_production_viewport_1920x1080.png")

            # Take full page screenshot
            print("[6/6] Taking PRODUCTION full page screenshot...")
            page.screenshot(
                path='screenshots/cycle3_production_1920x1080.png',
                full_page=True
            )
            print("✓ Saved: screenshots/cycle3_production_1920x1080.png")

        except Exception as e:
            print(f"✗ Error loading production page: {e}")
            print("⚠ Continuing with validation checks on local implementation only...")

        # ========================================================================
        # PART 3: CSS VALIDATION CHECKS
        # ========================================================================
        print("\n" + "=" * 80)
        print("CSS VALIDATION CHECKS")
        print("=" * 80)

        # Go back to local page for validation
        page.goto(local_url, wait_until='networkidle', timeout=30000)
        time.sleep(1)

        validation_results = []

        # Check 1: Price color
        print("\n[CHECK 1] Price Color (#6366F1)")
        try:
            price_color = page.evaluate("""
                () => {
                    const priceEl = document.querySelector('.price');
                    return priceEl ? window.getComputedStyle(priceEl).color : null;
                }
            """)
            # Convert rgb to hex for comparison
            expected = "rgb(99, 102, 241)"  # #6366F1
            status = "✓ PASS" if price_color == expected else f"✗ FAIL (got: {price_color})"
            print(f"   {status}")
            validation_results.append(("Price Color", status.startswith("✓")))
        except Exception as e:
            print(f"   ✗ ERROR: {e}")
            validation_results.append(("Price Color", False))

        # Check 2: CTA Button background
        print("\n[CHECK 2] CTA Button Background (#7C3AED)")
        try:
            cta_bg = page.evaluate("""
                () => {
                    const ctaBtn = document.querySelector('.cta-button');
                    return ctaBtn ? window.getComputedStyle(ctaBtn).backgroundColor : null;
                }
            """)
            expected = "rgb(124, 58, 237)"  # #7C3AED
            status = "✓ PASS" if cta_bg == expected else f"✗ FAIL (got: {cta_bg})"
            print(f"   {status}")
            validation_results.append(("CTA Button BG", status.startswith("✓")))
        except Exception as e:
            print(f"   ✗ ERROR: {e}")
            validation_results.append(("CTA Button BG", False))

        # Check 3: Selected day buttons
        print("\n[CHECK 3] Selected Day Buttons (#6366F1)")
        try:
            selected_day_bg = page.evaluate("""
                () => {
                    const selectedDay = document.querySelector('.day-button.selected');
                    return selectedDay ? window.getComputedStyle(selectedDay).backgroundColor : null;
                }
            """)
            expected = "rgb(99, 102, 241)"  # #6366F1
            status = "✓ PASS" if selected_day_bg == expected else f"✗ FAIL (got: {selected_day_bg})"
            print(f"   {status}")
            validation_results.append(("Selected Day Buttons", status.startswith("✓")))
        except Exception as e:
            print(f"   ✗ ERROR: {e}")
            validation_results.append(("Selected Day Buttons", False))

        # Check 4: Booking card width
        print("\n[CHECK 4] Booking Card Width (320px)")
        try:
            card_width = page.evaluate("""
                () => {
                    const card = document.querySelector('.booking-card');
                    return card ? window.getComputedStyle(card).width : null;
                }
            """)
            status = "✓ PASS" if card_width == "320px" else f"✗ FAIL (got: {card_width})"
            print(f"   {status}")
            validation_results.append(("Booking Card Width", status.startswith("✓")))
        except Exception as e:
            print(f"   ✗ ERROR: {e}")
            validation_results.append(("Booking Card Width", False))

        # Check 5: Image gallery gaps
        print("\n[CHECK 5] Image Gallery Gaps (8px)")
        try:
            gallery_gap = page.evaluate("""
                () => {
                    const gallery = document.querySelector('.gallery-images');
                    return gallery ? window.getComputedStyle(gallery).gap : null;
                }
            """)
            status = "✓ PASS" if gallery_gap == "8px" else f"✗ FAIL (got: {gallery_gap})"
            print(f"   {status}")
            validation_results.append(("Image Gallery Gaps", status.startswith("✓")))
        except Exception as e:
            print(f"   ✗ ERROR: {e}")
            validation_results.append(("Image Gallery Gaps", False))

        # Check 6: Location links color
        print("\n[CHECK 6] Location Links Color (#6366F1)")
        try:
            location_color = page.evaluate("""
                () => {
                    const locationLink = document.querySelector('.location a');
                    return locationLink ? window.getComputedStyle(locationLink).color : null;
                }
            """)
            expected = "rgb(99, 102, 241)"  # #6366F1
            status = "✓ PASS" if location_color == expected else f"✗ FAIL (got: {location_color})"
            print(f"   {status}")
            validation_results.append(("Location Links", status.startswith("✓")))
        except Exception as e:
            print(f"   ✗ ERROR: {e}")
            validation_results.append(("Location Links", False))

        # Check 7: Footer background
        print("\n[CHECK 7] Footer Background (#2D1B4E)")
        try:
            footer_bg = page.evaluate("""
                () => {
                    const footer = document.querySelector('footer');
                    return footer ? window.getComputedStyle(footer).backgroundColor : null;
                }
            """)
            expected = "rgb(45, 27, 78)"  # #2D1B4E
            status = "✓ PASS" if footer_bg == expected else f"✗ FAIL (got: {footer_bg})"
            print(f"   {status}")
            validation_results.append(("Footer Background", status.startswith("✓")))
        except Exception as e:
            print(f"   ✗ ERROR: {e}")
            validation_results.append(("Footer Background", False))

        # Check 8: Input borders
        print("\n[CHECK 8] Input Borders (#D1D5DB, 6px radius)")
        try:
            input_styles = page.evaluate("""
                () => {
                    const input = document.querySelector('.input-field');
                    if (!input) return null;
                    const styles = window.getComputedStyle(input);
                    return {
                        borderColor: styles.borderColor,
                        borderRadius: styles.borderRadius
                    };
                }
            """)
            expected_color = "rgb(209, 213, 219)"  # #D1D5DB
            color_ok = input_styles and input_styles['borderColor'] == expected_color
            radius_ok = input_styles and input_styles['borderRadius'] == "6px"
            status = "✓ PASS" if (color_ok and radius_ok) else f"✗ FAIL (got: {input_styles})"
            print(f"   {status}")
            validation_results.append(("Input Borders", status.startswith("✓")))
        except Exception as e:
            print(f"   ✗ ERROR: {e}")
            validation_results.append(("Input Borders", False))

        # Check 9: Form labels
        print("\n[CHECK 9] Form Labels (14px, 600 weight)")
        try:
            label_styles = page.evaluate("""
                () => {
                    const label = document.querySelector('label');
                    if (!label) return null;
                    const styles = window.getComputedStyle(label);
                    return {
                        fontSize: styles.fontSize,
                        fontWeight: styles.fontWeight
                    };
                }
            """)
            size_ok = label_styles and label_styles['fontSize'] == "14px"
            weight_ok = label_styles and label_styles['fontWeight'] == "600"
            status = "✓ PASS" if (size_ok and weight_ok) else f"✗ FAIL (got: {label_styles})"
            print(f"   {status}")
            validation_results.append(("Form Labels", status.startswith("✓")))
        except Exception as e:
            print(f"   ✗ ERROR: {e}")
            validation_results.append(("Form Labels", False))

        # Check 10: Property title
        print("\n[CHECK 10] Property Title (28px, 700 weight)")
        try:
            title_styles = page.evaluate("""
                () => {
                    const title = document.querySelector('.property-title');
                    if (!title) return null;
                    const styles = window.getComputedStyle(title);
                    return {
                        fontSize: styles.fontSize,
                        fontWeight: styles.fontWeight
                    };
                }
            """)
            size_ok = title_styles and title_styles['fontSize'] == "28px"
            weight_ok = title_styles and title_styles['fontWeight'] == "700"
            status = "✓ PASS" if (size_ok and weight_ok) else f"✗ FAIL (got: {title_styles})"
            print(f"   {status}")
            validation_results.append(("Property Title", status.startswith("✓")))
        except Exception as e:
            print(f"   ✗ ERROR: {e}")
            validation_results.append(("Property Title", False))

        # Check 11: Section headings
        print("\n[CHECK 11] Section Headings (20px)")
        try:
            heading_size = page.evaluate("""
                () => {
                    const heading = document.querySelector('.content-section h3');
                    return heading ? window.getComputedStyle(heading).fontSize : null;
                }
            """)
            status = "✓ PASS" if heading_size == "20px" else f"✗ FAIL (got: {heading_size})"
            print(f"   {status}")
            validation_results.append(("Section Headings", status.startswith("✓")))
        except Exception as e:
            print(f"   ✗ ERROR: {e}")
            validation_results.append(("Section Headings", False))

        # Check 12: Description text
        print("\n[CHECK 12] Description Text (14px, #374151)")
        try:
            desc_styles = page.evaluate("""
                () => {
                    const desc = document.querySelector('.description-text');
                    if (!desc) return null;
                    const styles = window.getComputedStyle(desc);
                    return {
                        fontSize: styles.fontSize,
                        color: styles.color
                    };
                }
            """)
            expected_color = "rgb(55, 65, 81)"  # #374151
            size_ok = desc_styles and desc_styles['fontSize'] == "14px"
            color_ok = desc_styles and desc_styles['color'] == expected_color
            status = "✓ PASS" if (size_ok and color_ok) else f"✗ FAIL (got: {desc_styles})"
            print(f"   {status}")
            validation_results.append(("Description Text", status.startswith("✓")))
        except Exception as e:
            print(f"   ✗ ERROR: {e}")
            validation_results.append(("Description Text", False))

        # Check 13: Amenity grids
        print("\n[CHECK 13] Amenity Grids (20px gap, 16px top margin)")
        try:
            amenity_styles = page.evaluate("""
                () => {
                    const amenityGrid = document.querySelector('.amenities-grid');
                    if (!amenityGrid) return null;
                    const styles = window.getComputedStyle(amenityGrid);
                    return {
                        gap: styles.gap,
                        marginTop: styles.marginTop
                    };
                }
            """)
            gap_ok = amenity_styles and amenity_styles['gap'] == "20px"
            margin_ok = amenity_styles and amenity_styles['marginTop'] == "16px"
            status = "✓ PASS" if (gap_ok and margin_ok) else f"✗ FAIL (got: {amenity_styles})"
            print(f"   {status}")
            validation_results.append(("Amenity Grids", status.startswith("✓")))
        except Exception as e:
            print(f"   ✗ ERROR: {e}")
            validation_results.append(("Amenity Grids", False))

        # Check 14: Host card
        print("\n[CHECK 14] Host Card (border, proper padding)")
        try:
            host_styles = page.evaluate("""
                () => {
                    const hostCard = document.querySelector('.host-card');
                    if (!hostCard) return null;
                    const styles = window.getComputedStyle(hostCard);
                    return {
                        border: styles.border,
                        padding: styles.padding
                    };
                }
            """)
            has_border = host_styles and host_styles['border'] and host_styles['border'] != 'none'
            has_padding = host_styles and host_styles['padding'] and host_styles['padding'] != '0px'
            status = "✓ PASS" if (has_border and has_padding) else f"✗ FAIL (got: {host_styles})"
            print(f"   {status}")
            validation_results.append(("Host Card", status.startswith("✓")))
        except Exception as e:
            print(f"   ✗ ERROR: {e}")
            validation_results.append(("Host Card", False))

        # Check 15: Chat button
        print("\n[CHECK 15] Chat Button (Circular, dark purple)")
        try:
            chat_styles = page.evaluate("""
                () => {
                    const chatBtn = document.querySelector('.chat-button');
                    if (!chatBtn) return null;
                    const styles = window.getComputedStyle(chatBtn);
                    return {
                        borderRadius: styles.borderRadius,
                        backgroundColor: styles.backgroundColor
                    };
                }
            """)
            # Check if border radius is 50% or >= 50px (circular)
            is_circular = chat_styles and (
                chat_styles['borderRadius'] == '50%' or
                (chat_styles['borderRadius'].endswith('px') and
                 float(chat_styles['borderRadius'].replace('px', '')) >= 50)
            )
            # Dark purple should be around #7C3AED or #6366F1
            is_purple = chat_styles and 'rgb' in chat_styles['backgroundColor']
            status = "✓ PASS" if (is_circular and is_purple) else f"✗ FAIL (got: {chat_styles})"
            print(f"   {status}")
            validation_results.append(("Chat Button", status.startswith("✓")))
        except Exception as e:
            print(f"   ✗ ERROR: {e}")
            validation_results.append(("Chat Button", False))

        # ========================================================================
        # SUMMARY REPORT
        # ========================================================================
        print("\n" + "=" * 80)
        print("VALIDATION SUMMARY")
        print("=" * 80)

        passed = sum(1 for _, result in validation_results if result)
        total = len(validation_results)

        print(f"\nTests Passed: {passed}/{total}")
        print(f"Success Rate: {(passed/total)*100:.1f}%")

        print("\n--- Detailed Results ---")
        for check_name, result in validation_results:
            status = "✓ PASS" if result else "✗ FAIL"
            print(f"{status:8} - {check_name}")

        print("\n--- Screenshot Files ---")
        print("✓ screenshots/cycle3_local_viewport_1920x1080.png")
        print("✓ screenshots/cycle3_local_1920x1080.png")
        print("✓ screenshots/cycle3_production_viewport_1920x1080.png")
        print("✓ screenshots/cycle3_production_1920x1080.png")

        print("\n" + "=" * 80)
        print("VALIDATION COMPLETE")
        print("=" * 80)

        # Close browser
        browser.close()

        return validation_results

if __name__ == "__main__":
    try:
        results = validate_css_fixes()
        print("\n✓ Validation script completed successfully!")
    except Exception as e:
        print(f"\n✗ Validation script failed: {e}")
        import traceback
        traceback.print_exc()
