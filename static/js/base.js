function openDevisModal() {
    document.getElementById('devisModal').classList.remove('hidden');
    document.body.style.overflow = 'hidden';
}

function closeDevisModal() {
    document.getElementById('devisModal').classList.add('hidden');
    document.body.style.overflow = '';
}

function submitDevis(e) {
    e.preventDefault();
    const nom = document.getElementById('devis_nom').value;
    const tel = document.getElementById('devis_tel').value;
    const service = document.getElementById('devis_service').value;
    const message = document.getElementById('devis_message').value;

    // Check if configuration exists
    const whatsappNumber = (window.SHABAKA_CONFIG && window.SHABAKA_CONFIG.whatsappNumber)
                           ? window.SHABAKA_CONFIG.whatsappNumber
                           : '212600000000'; // Fallback

    let whatsappMessage = `Bonjour Shabaka Invest,\n\n`;
    whatsappMessage += `Je suis *${nom}*\n`;
    whatsappMessage += `Téléphone: ${tel}\n`;
    if (service) {
        whatsappMessage += `Service souhaité: ${service}\n`;
    }
    if (message) {
        whatsappMessage += `\nMessage: ${message}\n`;
    }
    whatsappMessage += `\nJe souhaite demander un devis. Merci de me recontacter.`;

    const encodedMessage = encodeURIComponent(whatsappMessage);
    window.open(`https://wa.me/${whatsappNumber}?text=${encodedMessage}`, '_blank');
    closeDevisModal();
    document.getElementById('devisForm').reset();
}

document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', function() {
            document.getElementById('mobile-menu').classList.toggle('hidden');
        });
    }

    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') closeDevisModal();
    });

    setTimeout(function() {
        document.querySelectorAll('.flash-message').forEach(function(el) {
            el.style.opacity = '0';
            setTimeout(function() { el.remove(); }, 300);
        });
    }, 5000);
});
