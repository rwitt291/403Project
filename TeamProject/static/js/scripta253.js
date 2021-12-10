var people = document.getElementById('people');
var thousand = document.getElementById('thousand');
var counter = document.getElementById('counter');
var title = document.getElementById('title');
var html = document.getElementsByTagName('html');
var curve_wrapper_outer = document.getElementById('curve-wrapper-outer');
var url_params = new URLSearchParams(window.location.search);
var mute = url_params.get('mute');
var unscroll = url_params.get('unscroll');
var scroll_count = 0;

if (mute) {
  html[0].classList.add('mute')
}
if (unscroll) {
  html[0].classList.add('unscroll')
}

if (!mute) {
  var citations = document.querySelectorAll('.citation');
  citations.forEach(function(citation, i){
    citation.innerHTML = i+1;
  })

  var observer = new IntersectionObserver(function(entries){
    entries.forEach(function(entry){
      if (entry.isIntersecting || entry.intersectionRatio > 0) {
        html[0].classList = (unscroll) ? "unscroll" : "";
        html[0].classList.add(entry.target.dataset.background);
      }
    })
  })
  document.querySelectorAll('[data-background]').forEach(function(target){
    observer.observe(target);
  });

  var until_recently_shown = false;
  var since_it_began_shown = false;
  
  function toggleExpand(outer, inner) {
    var outerEl = document.getElementById(outer);
    var innerEl = document.getElementById(inner);
    var offset = Math.abs(outerEl.offsetTop - innerEl.offsetTop);
    innerEl.style.top = offset + 'px';
    outerEl.classList.add('expanded')
  }

  function showTooltip(e) {
    var tooltip = e.parentElement.getElementsByClassName('tooltip')[0]
    tooltip.classList.add('open')
  }
  function closeTooltip(e) {
    e.parentElement.classList.remove('open');
  }
}

window.addEventListener('scroll', function(e) {
  scroll_count = getScrollCount();
  if (scroll_count > 2000) {
    counter.innerHTML = scroll_count.toLocaleString();
  }
  else {
    counter.innerHTML = '';
  }
});

function getScrollCount() {
  var body = document.documentElement || document.body;
  var total_height = people.clientHeight;
  var scroll_percent = (body.scrollTop - people.offsetTop + body.clientHeight) / total_height;
  var count = Math.floor(scroll_percent * 217985);
  return count;
}

function setHeight() {
  var browser_width = window.innerWidth || document.body.clientWidth;
  var icons_per_card = 200;
  var pixel_height_per_card = 500;
  var pixel_width_per_card = 400;

  var cards_per_row = browser_width / pixel_width_per_card;
  var icons_per_row = icons_per_card * cards_per_row;
  var number_of_rows = 215000/icons_per_row;

  var height = Math.floor(number_of_rows * pixel_height_per_card);
  people.style.height = height + "px";

  if (!mute) {
    var thousand_height = Math.floor((1000/icons_per_row) * pixel_height_per_card);
    thousand.style.height = thousand_height + "px";
  }
}
setHeight();
window.addEventListener("orientationchange", setHeight);
window.addEventListener("resize", setHeight);
