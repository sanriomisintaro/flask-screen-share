// Jalankan setelah halaman dimuat
window.onload = function () {
    const socket = io();

    // Terhubung ke server, mulai stream
    socket.on('connect', () => {
        socket.emit('start_stream');
    });

    // Terima frame dari server dan tampilkan di <img>
    socket.on('frame', function (data) {
        const img = document.getElementById('screen');
        if (!img) return;

        img.src = 'data:image/jpeg;base64,' + data.image;
    });

    // Tombol fullscreen
    const fullscreenBtn = document.getElementById('fullscreenBtn');
    fullscreenBtn.addEventListener('click', () => {
        const elem = document.getElementById('screen');
        if (elem.requestFullscreen) {
            elem.requestFullscreen();
        } else if (elem.webkitRequestFullscreen) {
            elem.webkitRequestFullscreen();
        } else if (elem.msRequestFullscreen) {
            elem.msRequestFullscreen();
        }
    });
};
