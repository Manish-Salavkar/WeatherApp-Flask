function updateClock(timezone) {
    const now = new Date();
    const options = { timeZone: timezone, hour: '2-digit', minute: '2-digit', second: '2-digit' };
    const formattedTime = now.toLocaleTimeString(undefined, options);
    document.getElementById('clock').textContent = formattedTime;
}

function handleTimezoneChange() {
    const selectedTimezone = document.getElementById('timezone-select').value;
    if (selectedTimezone === 'local') {
        updateClock();
    } else {
        updateClock(selectedTimezone);
    }
}

function padZero(num) {
    return num.toString().padStart(2, '0');
}

setInterval(handleTimezoneChange, 1000); // Update the clock every second
handleTimezoneChange(); // Initial call to update the clock immediately

document.getElementById('timezone-select').addEventListener('change', handleTimezoneChange);



const boundary = 300; // Set the boundary position in pixels

const widgets = document.querySelectorAll('.widget');

window.addEventListener('scroll', () => {
    const scrollPosition = window.scrollY;

    widgets.forEach(widget => {
        const widgetTop = widget.getBoundingClientRect().top;

        if (widgetTop > boundary) {
            widget.classList.remove('beyond-boundary');
        } else {
            widget.classList.add('beyond-boundary');
        }
    });
});

const forecastWidgets = document.querySelectorAll('.forecast-widget');

forecastWidgets.forEach(widget => {
    widget.addEventListener('mouseenter', () => {
        const widgetBack = widget.querySelector('.widget-back');
        widgetBack.style.transform = 'translateY(0)';
    });

    widget.addEventListener('mouseleave', () => {
        const widgetBack = widget.querySelector('.widget-back');
        widgetBack.style.transform = 'translateY(100%)';
    });
});
