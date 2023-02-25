function typing (element, words) {
    var i = 0;
    var text = words;
    var speed = 100;
    var e = element;
    typeWriter();

    function typeWriter() {
        if (i < text.length) {
          e.innerText += text.charAt(i);
          i++;
          setTimeout(typeWriter, speed);
        }  
        if (i == text.length) {
            document.getElementById('cursor').innerText = '';
        }  
      }
}