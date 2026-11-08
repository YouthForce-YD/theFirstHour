function initIcons() {
    if (window.lucide) {
        window.lucide.createIcons();
    }
}

document.addEventListener('DOMContentLoaded', () => {
    initIcons();

    const htmlElement = document.documentElement;
    const langButtons = document.querySelectorAll('[data-set-lang]');
    const srAnnouncer = document.getElementById('srAnnouncer');
    const savedLangMode = localStorage.getItem('firstHourLangMode') || 'both';

    function announceStatus(messageText) {
        if (srAnnouncer) {
            srAnnouncer.textContent = messageText;
        }
    }

    function applyLanguageMode(mode, shouldAnnounce) {
        htmlElement.setAttribute('data-lang-mode', mode);
        htmlElement.setAttribute('lang', mode === 'en' ? 'en' : 'bn');
        localStorage.setItem('firstHourLangMode', mode);

        langButtons.forEach((buttonElement) => {
            const isSelected = buttonElement.getAttribute('data-set-lang') === mode;
            buttonElement.setAttribute('aria-pressed', isSelected ? 'true' : 'false');
            if (isSelected) {
                buttonElement.classList.add('bg-brand-gold', 'text-brand-dark');
                buttonElement.classList.remove('text-brand-gold/80');
            } else {
                buttonElement.classList.remove('bg-brand-gold', 'text-brand-dark');
                buttonElement.classList.add('text-brand-gold/80');
            }
        });

        if (shouldAnnounce) {
            const modeLabel = mode === 'bn' ? 'বাংলা ভাষা চালু হয়েছে' : mode === 'en' ? 'English language activated' : 'বাংলা এবং ইংরেজি উভয় ভাষা চালু হয়েছে';
            announceStatus(modeLabel);
        }
    }

    applyLanguageMode(savedLangMode, false);

    langButtons.forEach((buttonElement) => {
        buttonElement.addEventListener('click', () => {
            const selectedMode = buttonElement.getAttribute('data-set-lang');
            applyLanguageMode(selectedMode, true);
        });
    });

    const situationTriggers = document.querySelectorAll('.situation-trigger');

    situationTriggers.forEach((triggerElement) => {
        triggerElement.addEventListener('click', () => {
            const isExpanded = triggerElement.getAttribute('aria-expanded') === 'true';
            const panelId = triggerElement.getAttribute('aria-controls');
            const panelElement = document.getElementById(panelId);

            triggerElement.setAttribute('aria-expanded', !isExpanded ? 'true' : 'false');
            if (panelElement) {
                panelElement.classList.toggle('hidden', isExpanded);
            }
        });
    });

    const selectSituationLinks = document.querySelectorAll('[data-select-situation]');
    const situationSelectEl = document.getElementById('situationId');

    selectSituationLinks.forEach((linkElement) => {
        linkElement.addEventListener('click', () => {
            const targetId = linkElement.getAttribute('data-select-situation');
            if (situationSelectEl && targetId) {
                situationSelectEl.value = targetId;
                situationSelectEl.focus();
            }
        });
    });

    const quickExitBtn = document.getElementById('quickExitBtn');
    let lastEscapeTimestamp = 0;

    function triggerQuickExit() {
        const safeProtocol = 'https://';
        const safeHost = 'www.google.com';
        window.location.replace(safeProtocol + safeHost);
    }

    if (quickExitBtn) {
        quickExitBtn.addEventListener('click', triggerQuickExit);
    }

    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape') {
            const currentTimestamp = Date.now();
            if (currentTimestamp - lastEscapeTimestamp < 600) {
                triggerQuickExit();
            }
            lastEscapeTimestamp = currentTimestamp;
        }
    });
});

window.addEventListener('load', initIcons);
