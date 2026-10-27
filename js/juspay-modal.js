/**
 * Juspay Hypercheckout Orchestration & Express Payment Simulation
 * Graffeine Tales Atelier Edition
 */
class JuspayCheckoutModal {
  constructor() {
    this.modalBackdrop = document.getElementById('juspayModalBackdrop');
    this.closeBtn = document.getElementById('btnCloseJuspay');
    this.payTabs = document.querySelectorAll('.pay-tab-btn');
    this.payPanels = document.querySelectorAll('.pay-panel');
    this.btnSubmitPay = document.getElementById('btnSubmitPayment');
    this.processingState = document.getElementById('juspayProcessingState');
    this.bodyState = document.getElementById('juspayModalBody');
    this.successCard = document.getElementById('orderSuccessCard');

    this.currentOrder = null;
    this.selectedMethod = 'UPI';

    this.initListeners();
  }

  initListeners() {
    if (this.closeBtn) {
      this.closeBtn.addEventListener('click', () => this.close());
    }

    if (this.modalBackdrop) {
      this.modalBackdrop.addEventListener('click', (e) => {
        if (e.target === this.modalBackdrop) this.close();
      });
    }

    this.payTabs.forEach(btn => {
      btn.addEventListener('click', () => {
        this.payTabs.forEach(b => b.classList.remove('active'));
        this.payPanels.forEach(p => p.classList.remove('active'));

        btn.classList.add('active');
        const targetTab = btn.getAttribute('data-tab');
        const targetPanel = document.getElementById(targetTab);
        if (targetPanel) targetPanel.classList.add('active');

        this.selectedMethod = btn.getAttribute('data-method') || 'UPI';
      });
    });

    // UPI App Cards selection
    const upiCards = document.querySelectorAll('.upi-app-card');
    upiCards.forEach(card => {
      card.addEventListener('click', () => {
        upiCards.forEach(c => c.classList.remove('selected'));
        card.classList.add('selected');
      });
    });

    if (this.btnSubmitPay) {
      this.btnSubmitPay.addEventListener('click', () => this.submitPayment());
    }
  }

  open(cartState, customer = {}) {
    if (!cartState || !cartState.line_items || cartState.line_items.length === 0) {
      alert('Your cart is empty. Please add items to proceed!');
      return;
    }

    const orderNum = 'GTB_' + Math.floor(100000 + Math.random() * 900000);
    const amount = cartState.authoritative_totals.final_payable_amount || cartState.authoritative_totals.items_subtotal || 699;

    this.currentOrder = {
      order_id: orderNum,
      amount: amount,
      items: cartState.line_items,
      customer: customer
    };

    const orderIdEl = document.getElementById('juspayOrderIdText');
    const amountDueEl = document.getElementById('juspayAmountDueText');
    const submitAmountEl = document.getElementById('juspaySubmitAmount');

    if (orderIdEl) orderIdEl.textContent = this.currentOrder.order_id;
    if (amountDueEl) amountDueEl.textContent = `₹${this.currentOrder.amount.toFixed(2)}`;
    if (submitAmountEl) submitAmountEl.textContent = `₹${this.currentOrder.amount.toFixed(2)}`;

    // Reset views
    if (this.processingState) this.processingState.style.display = 'none';
    if (this.successCard) this.successCard.style.display = 'none';
    if (this.bodyState) this.bodyState.style.display = 'flex';

    if (this.modalBackdrop) {
      this.modalBackdrop.classList.add('active');
    }
  }

  close() {
    if (this.modalBackdrop) {
      this.modalBackdrop.classList.remove('active');
    }
  }

  submitPayment() {
    if (this.bodyState) this.bodyState.style.display = 'none';
    if (this.processingState) this.processingState.style.display = 'flex';

    setTimeout(() => {
      if (this.processingState) this.processingState.style.display = 'none';
      if (this.successCard) this.successCard.style.display = 'flex';

      // Update Receipt Details
      const rOrder = document.getElementById('receiptOrderId');
      const rMethod = document.getElementById('receiptMethod');
      const rTotal = document.getElementById('receiptTotal');
      const rDate = document.getElementById('receiptDate');

      if (rOrder && this.currentOrder) rOrder.textContent = this.currentOrder.order_id;
      if (rMethod) rMethod.textContent = this.selectedMethod;
      if (rTotal && this.currentOrder) rTotal.textContent = `₹${this.currentOrder.amount.toFixed(2)}`;
      if (rDate) rDate.textContent = new Date().toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit' });

      // Trigger Confetti Celebration!
      if (window.cartApp && window.cartApp.confetti) {
        window.cartApp.confetti.burst(3);
      }

      // Clear Cart from localStorage upon completed order
      localStorage.removeItem('gtb_cart');
      if (window.cartApp) {
        window.cartApp.cartItems = [];
        window.cartApp.appliedCouponCode = null;
        window.cartApp.recalculateCart();
      }
    }, 1300);
  }
}

window.juspayModal = new JuspayCheckoutModal();
