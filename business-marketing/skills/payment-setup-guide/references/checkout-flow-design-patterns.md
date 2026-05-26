# Checkout Flow Design Patterns

Professional checkout patterns for high conversion rates in Vietnamese market.

## Single-Page vs Multi-Step Checkout

### Single-Page Checkout
**Pros:**
- Faster completion (fewer clicks)
- Better for mobile users
- Lower abandonment rate for simple products
- Full process visibility

**Cons:**
- Overwhelming for complex orders
- Harder to validate step-by-step
- Slower page load with all elements

**Best for:** Digital products, single-item purchases, mobile-first audiences

### Multi-Step Checkout
**Pros:**
- Clear progress indication
- Better validation per step
- Less cognitive load
- Professional appearance

**Cons:**
- More clicks required
- Higher risk of abandonment between steps
- Requires good back navigation

**Best for:** Multiple items, shipping required, complex product configurations

## Mobile-First Checkout for Vietnamese Market

### Key Requirements
1. **Large touch targets** (minimum 44x44px)
2. **Auto-focus inputs** (reduce keyboard switches)
3. **Numeric keyboards** for phone/amount fields
4. **Minimal form fields** (name, phone, email only)
5. **Sticky CTA button** at bottom
6. **Progress indicator** (Step 1/3)

### Vietnamese-Specific Optimizations
- Phone number first (primary contact method)
- Facebook/Zalo login integration
- Bank logo recognition (trust factor)
- Vietnamese language toggle
- Province/district selection (not free text)

## VietQR Scan Flow UX

### Optimal Flow
```
Cart Review → Select VietQR → Generate QR Code → Display Instructions
→ User Scans with Banking App → Auto-Confirm → Success Page
```

### QR Display Best Practices
1. **Large QR code** (300x300px minimum on mobile)
2. **Clear instructions** in Vietnamese
   - "Mở ứng dụng ngân hàng"
   - "Quét mã QR"
   - "Xác nhận thanh toán"
3. **Amount display** above QR (large, bold)
4. **Order ID visible** (for manual transfer reference)
5. **Timer indicator** (15-minute validity)
6. **Auto-refresh** check every 5 seconds

### Confirmation Flow
- **Pending state:** "Đang chờ thanh toán..." (animated)
- **Success state:** Green checkmark + "Thanh toán thành công!"
- **Timeout state:** "Hết hạn. Vui lòng thử lại."
- **Failed state:** "Thanh toán thất bại. Liên hệ hỗ trợ."

## Trust Signals

### Essential Elements
1. **Bank logos** (Vietcombank, Techcombank, MBBank, etc.)
2. **Security badges**
   - SSL certificate indicator
   - "Thanh toán an toàn" text
   - Payment gateway logo (SePay, VNPay)
3. **Refund policy** link (visible, clear)
4. **Contact information** (phone, Facebook, Zalo)
5. **Customer count** ("15,000+ khách hàng tin dùng")

### Placement Strategy
- Bank logos: Below payment method selection
- Security text: Next to CTA button
- Refund policy: Footer of checkout
- Contact: Sticky help button
- Social proof: Near total amount

## Cart Abandonment Reduction

### Exit Intent Triggers
1. **Discount popup** (5-10% off if complete now)
2. **Timer urgency** ("Giá này chỉ còn 10 phút")
3. **Live chat offer** ("Cần hỗ trợ?")
4. **Simplification** ("Chỉ còn 2 bước nữa")

### Urgency Techniques
- **Limited stock** ("Chỉ còn 3 suất")
- **Limited time** ("Ưu đãi kết thúc sau 15:30")
- **Others viewing** ("5 người đang xem sản phẩm này")

### Simplification Strategies
- Remove optional fields
- Social login (Facebook)
- Skip account creation
- One-click payment methods

## Payment Confirmation Page Design

### Essential Elements
1. **Order number** (large, copyable)
2. **Payment status** (clear visual indicator)
3. **Next steps**
   - When to expect delivery/access
   - How to contact support
   - Where to check order status
4. **Product summary** (what was purchased)
5. **Receipt download** link

### Vietnamese Market Standards
- **Confirmation message via Zalo/Telegram** option
- **Add to calendar** button (for webinar/course start date)
- **Share on Facebook** (for social proof collection)
- **Invoice download** (VAT invoice if applicable)

## Error State Handling

### Timeout (15+ minutes)
**Message:** "Hết thời gian thanh toán. Mã QR đã hết hạn."
**CTA:** "Tạo mã mới" (regenerate QR)
**Design:** Yellow warning icon, retry button prominent

### Failed Payment
**Message:** "Thanh toán thất bại. Vui lòng kiểm tra số dư hoặc thử lại."
**CTA:** "Thử lại" or "Chọn phương thức khác"
**Design:** Red error icon, alternative payment methods visible

### Pending Payment
**Message:** "Đang xác nhận thanh toán... Vui lòng đợi trong giây lát."
**CTA:** None (auto-refresh every 5s)
**Design:** Animated spinner, estimated wait time

### Network Error
**Message:** "Mất kết nối. Vui lòng kiểm tra mạng và tải lại."
**CTA:** "Tải lại trang"
**Design:** Gray icon, preserve form data

## 5 Checkout Layout Patterns

### Pattern 1: Vertical Single-Page
```
[Header: Logo + Cart Icon]
[Progress: You're almost done!]
[Form: Name, Phone, Email (vertical stack)]
[Payment Method: Radio buttons with icons]
[Order Summary: Product + Price (collapsed)]
[Total: Large, bold]
[CTA: XÁC NHẬN THANH TOÁN (full width, green)]
[Trust: Bank logos + Refund policy]
```
**Best for:** Mobile users, single product, quick checkout

### Pattern 2: Two-Column Desktop
```
Left Column:              Right Column:
- Contact info            - Order summary (sticky)
- Payment method          - Product image
- Billing details         - Price breakdown
                          - Coupon code
                          - Total (large)
                          - CTA button
                          - Trust signals
```
**Best for:** Desktop users, multiple products, detailed review needed

### Pattern 3: Progressive Disclosure (Accordion)
```
Step 1: Thông tin [Expanded]
  Name, Phone, Email
  [TIẾP TỤC button]

Step 2: Thanh toán [Collapsed until Step 1 complete]
  Payment method selection
  [TIẾP TỤC button]

Step 3: Xác nhận [Collapsed until Step 2 complete]
  Order review
  [XÁC NHẬN button]
```
**Best for:** Complex products, new users, step-by-step guidance

### Pattern 4: Modal Overlay
```
[Dimmed background: Product page visible]
[Modal:
  Close X button
  Checkout form (simplified)
  Instant payment (VietQR only)
  Trust signals
  CTA: THANH TOÁN NGAY
]
```
**Best for:** Low-cost digital products, impulse purchases, landing pages

### Pattern 5: Embedded Cart + Instant Pay
```
[Product page with embedded cart]
[Quantity selector]
[Add to cart → Instant checkout button]
[Slide-up panel:
  Quick form (Phone only)
  Payment method
  Instant QR display
]
```
**Best for:** Single-product pages, webinar registrations, course enrollment

## Mobile vs Desktop Optimization

### Mobile-Specific
- Vertical layout only
- Sticky footer CTA
- Auto-advance to next field
- Minimal text input
- Large tap targets (60px)

### Desktop-Specific
- Two-column layout
- Sidebar order summary
- Hover states for trust badges
- Breadcrumb navigation
- Keyboard shortcuts (Tab, Enter)

## Conversion Optimization Checklist

- [ ] Form fields < 5 (fewer is better)
- [ ] Primary CTA color contrasts with page
- [ ] Trust signals visible without scrolling
- [ ] Mobile load time < 3 seconds
- [ ] Payment icons recognizable (Vietnamese banks)
- [ ] Error messages in Vietnamese
- [ ] Auto-save form data (localStorage)
- [ ] Guest checkout available
- [ ] Refund policy linked
- [ ] Support contact visible (Zalo/phone)

## Vietnamese Market Cultural Considerations

1. **Phone number priority** (more trusted than email)
2. **Bank transfer familiarity** (older than card payments)
3. **QR code adoption** (COVID-19 accelerated usage)
4. **Facebook integration** (primary social platform)
5. **Zalo messaging** (preferred over email for receipts)
6. **Lunar calendar awareness** (holidays affect delivery expectations)
7. **Group buying** (sharing links common)
8. **Invoice needs** (VAT invoices for business purchases)

## Testing Recommendations

1. **A/B test:** Single-page vs multi-step
2. **Heatmap analysis:** Click patterns on payment methods
3. **Session recordings:** Identify friction points
4. **Conversion funnel:** Track drop-off by step
5. **Mobile vs desktop:** Separate optimization
6. **Payment method performance:** Which converts best
7. **Error rate tracking:** Failed payments by type
