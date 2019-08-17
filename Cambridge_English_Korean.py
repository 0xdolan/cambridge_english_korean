import requests
from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

headers = {"User-Agent": "Mozilla/5.0"}
# main_url = "https://dictionary.cambridge.org/dictionary/english-korean/"
main_url = "https://dictionary.cambridge.org/ko/%EC%82%AC%EC%A0%84/%EC%98%81%EC%96%B4-%ED%95%9C%EA%B5%AD%EC%96%B4/"
word = input("\r\n")
url = requests.get(main_url + word, headers=headers).text
soup = BeautifulSoup(url, "lxml")
css = """<style type="text/css">
img,legend {
  border: 0;
}

legend,td,th {
  padding: 0;
}

html {
  font-family: sans-serif;
}

body {
  margin: 0;
}

article,aside,details,figcaption,figure,footer,header,hgroup,main,menu,nav,section,summary {
  display: block;
}

audio,canvas,progress,video {
  display: inline-block;
  vertical-align: baseline;
}

audio:not([controls]) {
  display: none;
  height: 0;
}

[hidden],template {
  display: none;
}

a {
  background-color: transparent;
}

a:active,a:hover {
  outline: 0;
}

abbr[title] {
  border-bottom: 1px dotted;
}

b,optgroup,strong {
  font-weight: 700;
}

dfn {
  font-style: italic;
}

h1,.h1 {
  font-size: 2em;
  margin: .67em 0;
}

mark {
  background: #ff0;
  color: #000;
}

small {
  font-size: 80%;
}

sub,sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}

sup {
  top: -.5em;
}

sub {
  bottom: -.25em;
}

svg:not(:root) {
  overflow: hidden;
}

figure {
  margin: 1em 40px;
}

hr {
  box-sizing: content-box;
  height: 0;
}

pre,textarea {
  overflow: auto;
}

code,kbd,pre,samp {
  font-family: monospace,monospace;
  font-size: 1em;
}

button,input,optgroup,select,textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}

button {
  overflow: visible;
}

button,select {
  text-transform: none;
}

button,html input[type=button],input[type=reset],input[type=submit] {
  -webkit-appearance: button;
  cursor: pointer;
}

button[disabled],html input[disabled] {
  cursor: default;
}

button::-moz-focus-inner,input::-moz-focus-inner {
  border: 0;
  padding: 0;
}

input {
  line-height: normal;
}

input[type=checkbox],input[type=radio] {
  box-sizing: border-box;
  padding: 0;
}

input[type=number]::-webkit-inner-spin-button,input[type=number]::-webkit-outer-spin-button {
  height: auto;
}

input[type=search] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}

input[type=search]::-webkit-search-cancel-button,input[type=search]::-webkit-search-decoration {
  -webkit-appearance: none;
}

fieldset {
  border: 1px solid silver;
  margin: 0 2px;
  padding: .35em .625em .75em;
}

* {
  box-sizing: border-box;
  -webkit-font-smoothing: antialiased;
}

body {
  background: #fff;
  color: #292929;
  font-size: .9em;
  text-align: left;
  font-family: Arial,Helvetica,sans-serif;
}

body.home_layout {
  padding-top: 48px;
}

body.dataset_layout {
  padding-top: 125px;
}

body.nav-active {
  overflow: hidden;
}

@media screen and (min-width:600px) {
  body {
    font-size: 1em;
  }
}

table {
  width: 100%;
  margin: 0 0 20px;
  border-spacing: 0;
  border-collapse: collapse;
}

th {
  padding: 15px;
  border: 1px solid #292929;
  background: #292929;
  line-height: 1.3em;
  font-weight: 700;
  color: #fff;
}

td {
  padding: 15px;
  border: 1px solid #e5e5e5;
  background: #fff;
  line-height: 1.3em;
  border-width: 1px;
}

tfoot td {
  border-width: 0;
  font-size: .875em;
}

tfoot td:first-child {
  padding-left: 0;
}

tr:nth-child(even) td {
  background: #fafafa;
}

thead td {
  border-color: #ccc;
}

tr.row--alt td {
  background: #eef1f6;
}

tr.row--standout td {
  background: #d0a44c;
  color: #111;
}

tr.row--standout .btn--impact {
  background: #fff;
  color: #111;
}

tr.row--disabled td {
  color: #ccc;
}

caption {
  caption-side: bottom;
  padding-top: 10px;
  color: #777;
  font-size: .8em;
  text-align: left;
  text-transform: uppercase;
}

h1,h2,h3,h4,h5,h6,.h1,.h2,.h3,.h4,.h5,.h6 {
  margin: 0 0 15px;
  line-height: 1.2em;
  font-weight: 400;
  font-size: 1em;
}

h1,h2,h3,h4,.h1,.h2,.h3,.h4 {
  color: #292929;
}

h1,.h1 {
  font-size: 2em;
}

h2,.h2 {
  font-size: 1.25em;
  font-weight: 700;
}

h3,.h3 {
  font-size: 1.063em;
}

h1 .fcdo,.h1 .fcdo {
  color: #9a9a9a;
}

p {
  margin: 0 0 15px;
  line-height: 1.5em;
}

a.a--normal,a,a.a--norm {
  text-decoration: underline;
  color: #234b9a;
}

a .fcdo {
  color: inherit;
}

.a--b a {
  font-weight: 700;
}

a.a--normal:hover,a:hover,.a--rev a,.a--none a,a.a--norm:hover {
  text-decoration: none;
}

.a--rev a:hover {
  text-decoration: underline;
}

a.img {
  display: inline-block;
  width: 100%;
}

a.img:hover {
  opacity: .8;
}

a.img img {
  width: 100%;
}

img {
  vertical-align: bottom;
  max-width: 100%;
  height: auto;
}

hr {
  margin: 30px 0;
  height: 1px;
  border: 0;
  border-top: 1px solid #e6e6eb;
}

address {
  margin: 0 0 20px;
  line-height: 1.5em;
  font-style: normal;
}

small {
  font-size: .875em;
}

sub,sup {
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}

sup {
  top: -.5em;
}

sub {
  bottom: -.25em;
}

figure {
  margin: 0 0 30px;
}

figcaption {
  padding-top: 10px;
  color: #777;
  font-size: .875em;
}

blockquote:before {
  content: "“";
  position: absolute;
  top: -3px;
  left: -3px;
  line-height: 1em;
  color: #234b9a;
  font-family: georgia,serif;
  font-size: 38px;
  font-style: normal;
  font-weight: 700;
}

blockquote {
  position: relative;
  margin: 0;
  padding-left: 20px;
  color: #292929;
  font-size: 18px;
  font-style: italic;
}

ul,ol {
  margin: 0 0 20px 15px;
  padding: 0;
  line-height: 1.5em;
}

li {
  margin: 0 0 10px;
}

li ul,li ol {
  margin-top: 10px;
  margin-left: 20px;
  list-style-type: circle;
}

ol {
  margin-left: 18px;
}

li ol {
  list-style-type: lower-latin;
}

dl {
  margin: 0 0 30px;
  line-height: 1.5em;
}

dt {
  color: #111;
  font-weight: 700;
}

dd {
  margin: 0 0 20px;
}

.inline {
  margin-left: 0;
  list-style: none;
}

.inline li {
  display: inline;
  margin: 0 15px 0 0;
}

.unstyled,.unstyled-nest li ul {
  margin-left: 0;
  padding: 0;
  list-style: none;
}

.unstyled li {
  margin: 0 0 5px 0;
}

.unstyled-nest li ul {
  margin-top: 5px;
}

.link-list {
  margin: 5px 0 10px;
}

.link-list a {
  font-weight: 700;
  text-decoration: none;
}

.link-list a:hover {
  text-decoration: underline;
}

.divided li {
  margin: 0;
  padding: 20px 5px;
  border-bottom: solid 1px #e3e3e8;
}

.divided li:first-child {
  padding-top: 10px;
}

.divided li:last-child {
  border-width: 0;
}

.tiles__tile {
  float: left;
  width: 50%;
  padding: 0 2px;
}

.tiles__tile label {
  float: left;
  width: 100%;
  margin-bottom: 10px;
  padding: 10px 0;
  background: #fff;
  text-align: center;
  border: solid 3px #e0e0e5;
  cursor: pointer;
  position: relative;
}

.tiles__tile input[type="radio"],.tiles__tile input[type="checkbox"] {
  display: none;
}

.tiles__tile input[type="radio"]:checked+label,.tiles__tile input[type="checkbox"]:checked+label {
  background: #d0a44c;
  border-color: #d0a44c;
}

.tiles__tile input[type="radio"]:checked+label:before,.tiles__tile input[type="checkbox"]:checked+label:before {
  content: "\f00c";
  font-weight: 300;
  font-family: cdoicons;
  padding-right: 7px;
  color: #fff;
  font-size: .9em;
}

.form .tiles {
  margin-bottom: 0;
}

@media screen and (min-width:1080px) {
  .tiles {
    margin: 0 -5px;
  }

  .tiles__tile {
    width: 33.3333333%;
    padding: 0 5px;
  }

  .tiles__tile label {
    padding: 20px 0;
  }

  .tiles--4 {
    margin: 0 -5px;
  }

  .tiles--4 .tiles__tile {
    width: 25%;
    padding: 0 5px;
  }
}

.msg {
  margin: 0 0 20px;
  padding: 20px;
  border: solid 1px #dde2f0;
  background: #dde2f0;
  color: #292929;
}

.msg li {
  margin-bottom: 5px;
}

.msg p,.msg ul,.msg ul li:last-child {
  margin-bottom: 0;
}

.msg a:not(.btn),.msg__close .fcdo {
  color: #fff;
}

.msg a:hover {
  text-decoration: none;
}

.msg__close {
  display: block;
  cursor: pointer;
  padding-top: 20px;
}

.msg--err {
  background: #e84d54;
  border-color: #d84046;
  color: #fff;
}

.msg--imp {
  background: #3b436d;
  border-color: #242b4e;
  color: #fff;
}

.msg--success {
  background: #a1c897;
  border-color: #7caa70;
  color: #fff;
}

.msg--assist {
  background: #dfdfdf;
  border-color: #cdcdcd;
}

.pagination {
  margin: 0 0 20px;
}

.pagination li {
  display: inline;
}

.pagination li.det {
  padding-right: 10px;
  font-size: .875em;
}

.pagination li a {
  display: inline-block;
  padding: 6px 12px;
  background: #234b9a;
  color: #fff;
  font-weight: 700;
  text-decoration: none;
}

.pagination li a:hover {
  background: rgba(35,75,154,.9);
}

.pagination li a.on {
  background: #e84427;
}

.med-obj,.med-obj__cont {
  overflow: hidden;
}

.med-obj__thumb {
  float: left;
  margin: 0 20px 0 0;
  max-width: 40%;
}

.med-obj__thumb--tight {
  margin-right: 15px;
}

.med-obj__thumb img {
  display: block;
  max-width: 100%;
}

.med-objs {
  margin: 0;
  list-style: none;
}

.med-objs li {
  margin: 0 0 40px;
  padding: 0 0 20px;
  border-bottom: 1px solid #ccc;
}

.med-objs li,.med-objs__cont {
  overflow: hidden;
}

.med-objs__thumb {
  float: left;
  margin: 0 20px 0 0;
}

.med-objs__thumb--tight {
  margin-right: 15px;
}

.med-objs__thumb img {
  display: block;
  max-width: 100%;
}

.med-objs li h2,.med-objs li .h2,.medObjs li p {
  margin-bottom: 10px;
}

.med-obj--alt,.med-objs--alt li {
  background: #f0f1f3;
}

.med-obj--spaced {
  margin-bottom: 10px;
}

.with-el {
  position: relative;
}

.with-el__el {
  position: absolute;
  top: 0;
  right: 0;
}

.with-el__el--l {
  right: auto;
  left: 0;
}

.with-el__el--b {
  top: auto;
  bottom: 0;
}

.with-el__el--icons {
  top: -5px;
  vertical-align: 0;
}

.with-icons__content {
  display: inline-block;
  padding: 5px 0;
}

.with-icons__icons {
  float: right;
}

.trend {
  position: relative;
  display: inline-block;
  vertical-align: 1px;
  color: rgba(36,46,78,.65);
  text-transform: uppercase;
  font-weight: 700;
  font-size: .6em;
}

.trend i {
  color: #0096ac;
  font-size: 1.75em;
}

.trend--down i {
  color: #e84427;
}

.prefix {
  display: inline-block;
  margin-right: 5px;
  width: 40px;
  color: #a9b3d0;
  font-size: 2em;
  vertical-align: -8px;
  text-align: center;
}

.divided .prefix {
  margin-left: -5px;
}

.prefix-float .prefix {
  float: left;
  display: block;
}

.prefix-float .prefix-item {
  overflow: hidden;
  display: block;
}

.prefix-block>* {
  position: relative;
  margin: 0 0 5px;
  padding: 10px 10px 10px 50px;
  background: #eef1f5;
}

.prefix-block .prefix {
  position: absolute;
  top: 0;
  left: 0;
  padding-top: 10px;
  height: 100%;
  font-size: 1em;
  color: #fff;
  background: #0096ab;
}

.progress {
  position: relative;
  width: 95px;
  height: 95px;
}

.progress svg {
  position: absolute;
  top: 0;
  left: 0;
}

.progress__indicator {
  position: relative;
  border: solid 8px #ccd2e1;
  width: 100%;
  height: 100%;
  -webkit-border-radius: 50%;
  -moz-border-radius: 50%;
  border-radius: 50%;
}

.progress__indicator__done {
  background: #d0a44c;
}

.progress__label {
  position: absolute;
  top: 50%;
  left: 50%;
  height: 40px;
  line-height: 40px;
  width: 65px;
  margin: -20px 0 0 -32.5px;
  text-align: center;
  font-size: 1.5em;
  color: #848fae;
}

.cycler {
  position: relative;
  padding: 0 20px;
  background: #11326f;
  color: #fff;
}

.cycler>div {
  overflow: hidden;
  width: 100%;
  padding: 0 20px 10px;
}

.cycler__nav {
  position: absolute;
  top: 10px;
  left: 7px;
  height: 40px;
  line-height: 32px;
  padding: 0 15px;
  text-align: center;
  color: #fff;
  font-size: 2.5em;
}

.cycler__nav--next {
  left: auto;
  right: 7px;
}

.cycler__items {
  overflow: hidden;
  white-space: nowrap;
  width: 100%;
}

.cycler__items>* {
  white-space: normal;
  display: inline-block;
  width: 20%;
  text-align: center;
}

.cycler__items.unstyled>li {
  margin: 0;
}

.cycler__items a {
  color: #acb7c5;
  font-size: 2.8125em;
  line-height: 1.3em;
}

.cycler__items a.on,.cycler__items .on a,.cycler__items a:hover {
  color: #fff;
}

.contain {
  max-width: 1340px;
  min-width: 300px;
  margin: 0 10px;
}

.contain--pad {
  padding: 15px 0;
}

.nocontain {
  margin: 0 -10px;
}

@media screen and (min-width:762px) {
  .contain {
    width: 728px;
    margin: 0 auto;
  }

  .nocontain {
    margin: 0;
  }
}

@media screen and (min-width:960px) {
  .contain {
    width: 900px;
  }
}

@media screen and (min-width:1080px) {
  .contain {
    width: 1024px;
  }
}

@media screen and (min-width:1280px) {
  .contain {
    width: 1240px;
  }
}

@media screen and (min-width:1380px) {
  .contain {
    width: 1340px;
  }
}

.cdo-hdr {
  background: #292929;
  color: #fff;
  position: fixed;
  z-index: 6;
  top: 0;
  left: 0;
  width: 100%;
}

.cdo-hdr__pre {
  background: #3d3d3d;
  padding: 0 20px;
}

.cdo-hdr #cdo-lang-opt,.cdo-hdr #cdo-user-opt {
  z-index: 6;
}

.cdo-logo {
  float: left;
  height: 53px;
  width: 168px;
  background: url(/ko/external/images/logo.png?version=4.0.94) no-repeat left top;
  background-size: cover;
  margin: 0 30px 0 0;
}

.cdo-logo-grammar {
  float: left;
  height: 53px;
  width: 168px;
  background: url(/ko/external/images/logo.png) no-repeat left top;
  background-size: cover;
  margin: 0 30px 0 0;
}

.cdo-logo--rev {
  background-image: url(/ko/external/images/logo-pos.png?version=4.0.94);
  background-size: cover;
  margin: 3px 30px 0 0;
}

.cdo-logo--sml {
  height: 30px;
  width: 95px;
  margin: 10px 0 0 0;
}

.cdo-logo--hero {
  background: url(/ko/external/images/logo-lrg.png?version=4.0.94);
  background-size: cover;
  float: none;
  margin-bottom: 15px;
}

.cdo-hero--light .cdo-logo--hero {
  background-image: url(/ko/external/images/logo-pos-lrg.png?version=4.0.94);
  background-size: cover;
}

.cdo-hdr__pre .dropdown__box a:before {
  content: "\f054";
  padding-right: 7px;
  vertical-align: -1px;
  font-size: 12px;
  font-weight: 300;
  font-family: cdoicons;
  color: rgba(35,75,154,.47);
}

@media screen and (min-width:762px) {
  .cdo-logo--sml {
    margin-right: 30px;
  }

  .cdo-logo--hero {
    height: 85px;
    width: 269px;
    background-size: cover;
  }
}

@media screen and (min-width:960px) {
  .cdo-hdr__pre {
    padding: 0 30px;
  }

  .cdo-logo--sml {
    display: none;
  }
}

@media screen and (min-width:1080px) {
  .cdo-logo--hero {
    height: 102px;
    width: 323px;
  }
}

.overlay {
  display: none;
  position: fixed;
  z-index: 1000000;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  height: 100%;
  width: 100%;
  background: #dde2ed;
  background: rgba(221,226,237,.9);
}

.overlay--active {
  display: block;
}

.nav-active .overlay {
  background: #000;
  background: rgba(0,0,0,.5);
}

.modal {
  display: none;
  position: absolute;
  z-index: 1000001;
  top: 0;
  right: 0;
  left: 0;
  margin: 20px auto 0;
  width: 90%;
  max-width: 830px;
  min-height: 380px;
  background: #fff;
  box-shadow: 0 0 8px rgba(0,0,0,.05);
}

.modal.open {
  display: block;
}

.modal__sidebar .h2,.modal__sidebar .h3 {
  color: inherit;
  font-weight: 700;
}

.modal__spacer {
  padding: 15px;
}

.modal__close {
  background: #e84526;
  position: absolute;
  top: -8px;
  right: -8px;
  color: #fff;
  height: 32px;
  line-height: 30px;
  width: 32px;
  text-align: center;
  border-radius: 100%;
  cursor: pointer;
}

.modal__close .fcdo {
  color: inherit;
  font-size: 1.3em;
}

.modal--myd {
  background: #fff;
}

.modal--myd .modal__sidebar {
  background: #222 url(/ko/external/images/modal-bg.jpg?version=4.0.94) no-repeat right top;
  color: #fff;
}

.modal--wide {
  max-width: 959px;
}

@media screen and (min-width:762px) {
  .modal__spacer {
    padding: 30px 45px 45px;
  }
}

@media screen and (min-width:1080px) {
  .modal {
    margin-top: 50px;
  }

  .modal__main {
    float: left;
    width: 55%;
  }

  .modal__sidebar {
    position: absolute;
    top: 0;
    right: 0;
    height: 100%;
    width: 45%;
  }

  .modal--wide .modal__main {
    width: 63%;
  }

  .modal--wide .modal__sidebar {
    width: 37%;
  }
}

h1.hw,.h1.hw {
  margin-bottom: 10px;
  font-size: 1em;
  font-weight: 700;
}

.superentry h1,h1.superentry {
  font-weight: normal;
}

.superentry h1 strong,h1.superentry strong {
  font-size: 1.2em;
}

.definition-src {
  margin-bottom: 40px;
}

@media screen and (min-width:762px) {
  h1.hw,.h1.hw {
    margin-bottom: .5em;
  }
}

.cloud {
  margin-bottom: 15px;
}

.cloud.txt-block {
  padding-right: 0;
  background: #eff1f6;
}

.cloud ul {
  margin-bottom: 10px;
  text-align: center;
  line-height: 1.8em;
}

.cloud li {
  display: inline-block;
  margin-right: 25px;
}

.cloud li a {
  color: #234b9a;
  font-weight: 700;
}

.cloud li a i {
  font-style: normal;
}

.cloud li a .pos {
  font-style: italic;
}

.cloud li a.odd {
  color: #11326f;
}

.cloud .topic_0 {
  font-size: .9em;
}

.cloud .topic_2 {
  font-size: 1.15em;
}

.cloud .topic_3 {
  font-size: 1.5em;
}

.cloud .topic_4 {
  font-size: 1.8em;
}

.nav-entry-mob {
  width: 100%;
  border-bottom: solid 1px #e0e0e5;
}

.nav-entry-mob ul {
  margin-bottom: 0;
}

.nav-entry-mob__datasets {
  float: left;
}

.nav-entry-mob__datasets .btn {
  padding: 11px 28px 10px 0;
  background: #fff;
  color: #e84427;
  font-weight: 700;
  border-width: 0;
}

.nav-entry-mob__datasets .btn:after {
  content: "\f107";
  color: #e84427;
  font-size: 18px;
  right: 5px;
}

.nav-entry-mob__datasets .btn.on:after {
  content: "\f106";
}

.di {
  margin-bottom: 10px;
}

.entrybox .txt-block--shallow {
  padding-left: 30px;
}

.entry-body .txt-block {
  border-radius: 2px;
}

.entry-body .pos-header,.entry-body .pos-body,.entry-body .normal-entry-body,.entry-body .normal-entry.di-head,.entry-body .pv-block {
  padding-right: 25px;
}

.entry-body .normal-entry-body .pos-body {
  padding-right: 0;
}

.entry-box__el,.entry-body__el {
  min-height: 240px;
  padding: 15px;
  margin: 0 0 20px;
  border: 1px solid #e6e6eb;
}

@media screen and (max-width:761px) {
  .superentry .entry-body__el {
    padding: 0;
    border: 0;
  }
}

.superentry .entry-body .pos-header,.superentry .entry-body .pos-body,.superentry .entry-body .idiom-block {
  padding-right: 0;
}

.entry-body__el--smalltop {
  padding-top: 10px;
}

.entry-box__el:last-child,.entry-body__el:last-child {
  margin-bottom: 10px;
}

.mod.entry h3,.mod.entry .h3 {
  font-size: 1em;
}

.di-head {
  padding: 12px 20px;
  background: #eff1f6;
  border-left: solid 1px #e6e6eb;
  border-right: solid 1px #e6e6eb;
}

.di-head h2,.di-head .h2 {
  font-size: 1.4em;
  margin: 10px;
}

.di-head .see-all-translations {
  margin-left: 1px;
  display: table;
  line-height: 22px;
}

.di-title {
  font-size: 1em;
  line-height: 2em;
}

.normal-entry .di-title {
  line-height: 1.3em;
}

.di-head.normal-entry {
  position: relative;
  background: #fff;
  margin-bottom: 20px;
  padding: 0;
  border-width: 0;
}

.di .pos-header {
  position: relative;
  margin: 5px 0 15px;
  color: rgba(17,50,111,.91);
}

.di .irreg-infls,.di .inf {
  color: #292929;
  display: inline-block;
}

.di .share {
  position: absolute;
  top: -10px;
  right: -35px;
}

.di .pos-head .pos-info {
  margin: 0 0 20px;
}

.cdo-section-title-hw {
  display: inline;
  word-wrap: break-word;
}

.cdo-section-title-hw .headword,.di-head.normal-entry .cdo-section-title-hw {
  display: block;
  margin: 5px 0 10px;
  font-size: 2.5em;
  line-height: 1.075em;
  font-weight: 700;
}

.di-head.normal-entry .cdo-section-title-hw {
  margin: 0;
}

.cdo-section-title-hw .posgram,.di-head.normal-entry .posgram,.pos-head .pos-info .posgram,.HeadwordCtn .GeographicalUsage {
  font-style: italic;
  font-size: 1.25em;
  color: #444;
}

.gcs {
  vertical-align: -1px;
}

.cdo-section-title-hw .posgram.ico-bg:after,.di-head.normal-entry .posgram.ico-bg:after,.pos-head .pos-info .posgram.ico-bg:after {
  font-family: cdoicons;
  content: "\F111";
  font-size: 4px;
  vertical-align: 4px;
  line-height: 1em;
  font-style: normal;
}

.pos-head .pos-info .posgram {
  margin-right: 5px;
}

.pos-head .pos-info .pron,.di-head.normal-entry .pron {
  margin-left: 5px;
}

.entry-body .pos-header {
  padding-right: 25px;
}

.entry-body .irreg-infls .inf {
  font-weight: 700;
}

.entry-body .gram {
  font-style: normal;
  font-size: .8em;
}

.entry-body .gram a {
  color: inherit;
  text-decoration: none;
}

.entrybox .freq,.entrybox .epp-xref {
  margin-right: 3px;
  padding: 2px 5px;
  color: #fff;
  font-weight: 700;
  font-size: .8em;
  min-width: 14px;
  text-align: center;
  background-color: #444;
  -webkit-border-radius: 8px;
  -moz-border-radius: 8px;
  border-radius: 8px;
}

.entrybox .freq {
  display: none;
}

.entrybox .cdo-topic {
  font-weight: 700;
}

.entry-body .normal-entry-body,.entry-body .pos-body--nohw {
  padding-top: 20px;
  border-top: solid 3px #234b9a;
}

.entry-body .pos-body .tabs .txt-block,.entry-body .pos-body h4.txt-block {
  padding: 11px 20px;
}

.entry-body .pos-body .tabs .txt-block .hw,.entry-body .pos-body h4.txt-block .hw,.entry-body .pos-body .tabs .txt-block .pos,.entry-body .pos-body h4.txt-block .pos {
  font-size: 1.125em;
}

.entry-body .pos-body>div {
  margin-top: 20px;
}

.entry-body .pos-body>div.cols {
  margin-top: 30px;
}

.entry-body .pos-body>div:first-child {
  margin-top: 0;
}

.normal-entry-body a,.entry-body .pos-body a,.entry-body .pv-body a,.entry-body .idiom-body a,.extraexamps a {
  text-decoration: none;
}

.normal-entry-body .def-head a,.normal-entry-body .def-body a,.entry-body .def-head a,.entry-body .def-body a,.entry-body .extraexamps a {
  color: inherit;
}

.entry-body .extraexamps li[class="eg"] {
  position: relative;
  padding-left: 5px;
  padding-right: 30px;
}

.entry-body .extraexamps li[class="eg"]:hover {
  background: #eff1f6;
}

.entry-body .extraexamps .DiscoveryReaders {
  color: rgba(183,58,28,.6);
  position: absolute;
  right: 0;
  top: 0;
  line-height: 24px;
}

.entry-body .extraexamps .Gutenberg {
  color: rgba(38,71,165,.4);
  position: absolute;
  right: 0;
  top: 0;
  line-height: 24px;
}

.entry-body .extraexamps .DiscoveryReaders:hover,.entry-body .extraexamps .Gutenberg:hover {
  text-decoration: none;
}

.normal-entry-body .def-head a.circle-btn,.normal-entry-body .def-body a.circle-btn,.entry-body .def-head a.circle-btn,.entry-body .def-body a.circle-btn,.entry-body .extraexamps a.circle-btn {
  color: #fff;
}

.normal-entry-body a:hover,.entry-body .pos-body a:hover,.entry-body .pv-body a:hover {
  text-decoration: underline;
}

.entry-body .txt-block--shallow {
  color: #242b4e;
}

.entry-body .pos-body .irreg-infls {
  color: #4b5e86;
  font-size: .875em;
}

.entry-body .pos-body .irreg-infls .inf {
  font-weight: 700;
}

.entry-body .def-block,.entry-body .phrase-block,.entry-body .runon {
  margin-bottom: 20px;
}

.entry-body .phrase-head,.entry-body .runon-head,.entry-body .runon-body,.entry-body .phrase-body,.entry-body .phrase-body>.def-block {
  position: relative;
}

.entry-body .runon-head:before {
  color: #234b9a;
}

.entry-body .phrase-title,.entry-body .runon-title {
  display: inline-block;
  margin: 0 0 10px;
  font-size: 1.1em;
  font-weight: 700;
  color: #234b9a;
}

.entry-body .runon-title {
  color: #234b9a;
}

.entry-body .phrase-body:before,.entry-body .runon-body:before {
  content: " ";
  position: absolute;
  top: 0;
  left: 15px;
  height: 100%;
  width: 3px;
  background: #eff1f6;
}

.entry-body .phrase-body .def-head,.entry-body .runon-body .def-head {
  padding-top: 2px;
  margin: 0 0 5px;
}

.entry-body .phrase-body .def-body,.entry-body .runon-body .def-body {
  margin: 0 0 10px;
}

.entry-body .xref {
  line-height: 1.5em;
}

.entry-body .xref.grammar a {
  font-weight: 400;
  color: #111;
}

.entry-body .xref.grammar a:hover {
  text-decoration: none;
}

.entry-body .xref.grammar .x-h {
  display: block;
  color: #234b9a;
  font-weight: 700;
}

.entry-body .xref.grammar a:hover .x-h {
  color: #3661b4;
}

.entry-body .xref.grammar .x-h .obj {
  font-style: italic;
}

.entry-body .xref .txt-block {
  margin-bottom: 10px;
}

.entry-body .xref .item {
  margin-bottom: 10px;
}

.entry-body .see_also a {
  color: #234b9a;
}

.entry-body .domain {
  display: inline-block;
  margin: 3px 0;
  padding: 1px 4px;
  background: #e8e8ed;
  border: 1px solid #e0e0e5;
}

.entry-body .examp {
  margin: 0 0 5px 0;
  line-height: 1.5em;
}

.entry-body a.Ref {
  color: #234b9a;
}

.runon-info .posgram .pos {
  color: #555;
}

.entrybox .i {
  font-style: italic;
}

.entrybox .lab,.entrybox .x-lab {
  display: inline;
  font-variant: small-caps;
  font-size: 1.1em;
  font-weight: normal;
}

.entrybox .lab .region,.entrybox .x-lab .region,.entrybox .x-lab .usage {
  text-transform: lowercase;
  font-style: normal;
}

.entrybox .lu {
  font-weight: 700;
}

.entry-body b.def {
  font-size: 1.125rem;
  line-height: 1.3rem;
}

.entry-body .xref a {
  color: #234b9a;
  display: inline-block;
  padding-left: 20px;
  font-weight: 700;
}

.entry-body .xref .x-lab {
  margin-left: 5px;
}

.entry-body .xref .x-at {
  color: #000;
}

.entry-body .x-lab .region,.entry-body .x-lab .usage {
  cursor: pointer;
}

.entry-body span.b {
  font-weight: 700;
}

.uk,.us,.superentry .irreg-infls {
  margin-left: 5px;
}

.uk>.region,.us>.region {
  text-transform: uppercase;
  color: #e84427;
  font-size: 1em;
  font-weight: 700;
}

.superentry .pron {
  font-size: 1.063em;
}

.sense-block .hw,.sense-block .phrase {
  font-weight: 700;
  font-size: 1.1em;
}

.sense-block .pos {
  font-style: italic;
}

.gram {
  color: #555;
  margin-right: 3px;
}

.sense-block .guideword {
  margin-left: 8px;
  font-weight: 700;
}

.sense-block .guideword span {
  vertical-align: -1px;
}

.emphasized .gram {
  font-style: normal;
}

.entry-body .posgram .pos {
  font-style: italic;
}

.entry-body .x-pos {
  font-style: italic;
  font-weight: normal;
  color: #000;
}

.entry-body .usagenote .eg {
  font-style: italic;
  display: block;
  margin-left: 8px;
}

.entry-body .txt-block--alt2 .gram,.entry-body .txt-block--alt2 .gram a {
  color: #fff;
}

.entry-body .txt-block--alt2 .gram .gcs {
  vertical-align: middle;
}

.pos-head .pos-info .fcdo {
  font-size: 14px;
  vertical-align: -2px;
}

.entrybox .fav-entry {
  width: 22px;
  height: 22px;
}

.entrybox .fav-entry .fcdo {
  line-height: 22px;
}

.def-block {
  position: relative;
}

.def-block .fav-entry {
  position: absolute;
  top: 2px;
  left: 0;
}

.phrase-block .def-block .fav-entry {
  top: 4px;
}

.entry-divide {
  position: relative;
  border-top: solid 1px #e6e6eb;
  border-bottom: solid 1px #e6e6eb;
  height: 20px;
}

.def-body .trans {
  display: block;
  margin: 5px 0;
  font-style: normal;
  font-size: 1.125rem;
  line-height: 1.3rem;
  color: #0096ab;
  font-style: normal;
  font-weight: 700;
}

.cdo-smartt .pos {
  display: none;
}

@media screen and (max-width:449px) {
  .entry-body .pos-body .cols__col {
    margin-bottom: 15px;
  }
}

@media screen and (min-width:450px) {
  .entry-box__el,.entry-body__el {
    min-height: 325px;
  }

  .entry-body .pos-header,.entry-body .pos-body,.entry-body .normal-entry-body,.entry-body .normal-entry.di-head,.entry-body .pv-block {
    padding-right: 70px;
  }

  .di .share {
    top: 10px;
    right: 0;
  }

  .entry-body .pos-body>div {
    margin-top: 40px;
  }

  .entry-body .normal-entry-body .pos-body {
    padding-right: 0;
  }
}

@media screen and (min-width:762px) {
  .tabs-entry {
    min-height: 420px;
  }
}

.results.link-list a {
  font-weight: 400;
}

.results.link-list em {
  font-style: italic;
  color: #242b4e;
}

.results.link-list a:hover {
  text-decoration: none;
}

.results.link-list a:hover b {
  text-decoration: underline;
}

.feature-w,.feature-w-big {
  font-size: 1.25em;
  line-height: 1em;
  font-weight: 400;
}

.feature-w-big {
  font-size: 2.2em;
  line-height: .9em;
}

.txt-block {
  display: block;
  padding: 13px 20px;
  background: #eff1f6;
  font-weight: 400;
  box-sizing: border-box;
  text-decoration: none;
}

.txt-block--shallow {
  padding: 4px 20px;
}

.txt-block--padder {
  padding: 15px 20px;
}

.txt-block--alt,.txt-block--alt2 {
  background: #234b9a;
  color: #fff;
}

.txt-block--alt3 {
  background: #e84427;
  color: #fff;
}

.txt-block--impact {
  background: #d0a44c;
  color: #111;
}

.txt-block--alt .fcdo,.txt-block--alt2 .fcdo {
  color: #fff;
}

.txt-block--padl {
  padding-left: 70px;
}

.txt-block--padr {
  padding-right: 70px;
}

.resp {
  display: none;
}

.resp.open {
  display: block;
}

.oflow-hide {
  overflow: hidden;
}

@media screen and (min-width:600px) {
  .resp--sml {
    display: block;
  }

  .resp--sml-i {
    display: inline;
  }

  .resp-hide--sml {
    display: none;
  }
}

@media screen and (min-width:762px) {
  .resp--med {
    display: block;
  }

  .resp--med-i {
    display: inline;
  }

  .resp-hide--med {
    display: none;
  }
}

@media screen and (min-width:960px) {
  .resp--lrg {
    display: block;
  }

  .resp--lrg-i {
    display: inline;
  }

  .resp-hide--lrg {
    display: none;
  }
}

@media screen and (min-width:1080px) {
  .resp--xl {
    display: block;
  }

  .resp-hide--xl {
    display: none;
  }

  .float-xl {
    float: left;
    padding-right: 30px;
  }
}

.center {
  text-align: center;
}

.left {
  text-align: left;
}

.right {
  text-align: right;
}

.lower {
  text-transform: lowercase;
}

.upper {
  text-transform: uppercase;
}

.clr {
  clear: both;
}

.clr-left {
  clear: left;
}

.clr-right {
  clear: right;
}

.f-left {
  float: left;
}

.f-right {
  float: right;
}

.title {
  padding-bottom: 5px;
  border-bottom: solid 1px #e6e6eb;
}

.fade {
  opacity: .7;
}

.hide {
  display: none;
}

.hide.open {
  display: block;
}

.hide-txt {
  text-indent: 100%;
  white-space: nowrap;
  overflow: hidden;
}

.hidden {
  visibility: hidden;
}

.flush,div.flush {
  margin-bottom: 0;
}

.tight,.semi-flush {
  margin-bottom: 5px;
}

.nudge-top {
  margin-top: 2px;
}

.normal-top {
  margin-top: 15px;
}

.normal-base {
  margin-bottom: 15px;
}

.space-top {
  margin-top: 5px;
}

.space-base {
  margin-bottom: 10px;
}

.space-both {
  margin-top: 5px;
  margin-bottom: 10px;
}

.spaced {
  margin-bottom: 20px;
}

.spaced-top {
  margin-top: 20px;
}

.spaced-out {
  margin: 5px 0 25px;
}

.spaced-big {
  margin-bottom: 30px;
}

.spaced-big-top {
  margin-top: 30px;
}

.pad {
  padding: 0 5px;
}

.pad-indent {
  padding-left: 30px;
}

.pad-indent-both {
  padding-left: 30px;
  padding-right: 30px;
}

.pad-all {
  padding: 35px;
}

.pad-all-sml {
  padding: 20px;
}

.pad-extra {
  padding: 0 20px;
}

.pad-l-flush {
  padding-left: 0;
}

.pad-l-sml {
  padding-left: 5px;
}

.pad-l {
  padding-left: 10px;
}

.pad-l-lrg {
  padding-left: 15px;
}

.pad-r-flush {
  padding-right: 0;
}

.pad-r-sml {
  padding-right: 5px;
}

.pad-r {
  padding-right: 10px;
}

.pad-r-lrg {
  padding-right: 15px;
}

.pad-t-flush {
  padding-top: 0;
}

.pad-t-sml {
  padding-top: 5px;
}

.pad-t {
  padding-top: 10px;
}

.pad-t-lrg {
  padding-top: 15px;
}

.pad-b-flush {
  padding-bottom: 0;
}

.pad-b-sml {
  padding-bottom: 5px;
}

.pad-b {
  padding-bottom: 10px;
}

.pad-b-lrg {
  padding-bottom: 15px;
}

.pad-sides {
  padding-left: 10px;
  padding-right: 10px;
}

.pad-sides-sml {
  padding-left: 5px;
  padding-right: 5px;
}

.underline {
  text-decoration: underline;
}

.fig-frame {
  width: 100%;
  text-align: center;
}

.fig-frame img {
  border: solid 6px #fff;
}

.leader {
  font-size: 1.25em;
  line-height: 1.4em;
}

.meta {
  color: #686868;
}

.emphasized {
  font-style: italic;
}

.standout {
  color: #242e4e;
}

.pointer {
  cursor: pointer;
}

.small {
  font-size: .875em;
}

.smaller {
  font-size: .8em;
}

.bigger {
  font-size: 1.125em;
}

.light {
  color: #888;
}

.bg-h:after {
  content: " ";
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 0;
  z-index: 1;
}

.accessibility {
  overflow: hidden;
  position: absolute;
  top: -9999px;
  left: -9999px;
  float: none;
  width: auto;
  margin: 0;
  padding: 0;
}

.contain:before,.clrd:before,.tabs:before,.cdo-search:before,.stacks:before,.tiles:before,.tabs__content>.block-wrap:before {
  content: " ";
  display: table;
}

.contain:after,.clrd:after,.tabs:after,.cdo-search:after,.stacks:after,.tiles:after,.tabs__content>.block-wrap:after {
  content: " ";
  display: table;
  clear: both;
}

.dropdown__box {
  z-index: 9000;
}

.site-msg {
  z-index: 9999;
}

.english-french .pad-indent .runon.pad-indent,.french-english .pad-indent .runon.pad-indent {
  margin-left: -30px;
}

.english-french .runon-body.pad-indent,.french-english .runon-body.pad-indent {
  margin-left: -20px;
}

.relativDiv {
  position: relative;
}

.divBlock {
  display: block;
}

.img-thumb {
  margin-bottom: 10px;
}

.hooks {
  width: 100%;
  padding-bottom: .5em;
}

.hook {
  padding-right: 1em;
  text-decoration: none;
  font-weight: bold;
}

@media screen and (max-width:425px) {
  .hooks {
    display: flex;
  }

  .hook {
    padding: 0 3px;
    display: block;
    flex: 1;
  }

  .hook:first-child {
    padding-left: 0;
  }

  .hook:last-child {
    padding-right: 0;
  }
}

.x-num {
  font-size: .9em;
}

@font-face {
  font-family:'cdoicons';src:url('/ko/external/fonts/cdoicons.eot?1135p5&version=4.0.94');src:url('/ko/external/fonts/cdoicons.eot?1135p5#iefix&version=4.0.94') format('embedded-opentype'),url('/ko/external/fonts/cdoicons.ttf?1135p5&version=4.0.94') format('truetype'),url('/ko/external/fonts/cdoicons.woff?1135p5&version=4.0.94') format('woff'),url('/ko/external/fonts/cdoicons.svg?1135p5#cdoicons&version=4.0.94') format('svg');font-weight:normal;font-style:normal;
}

.fcdo {
  speak: none;
  display: inline-block;
  font: normal normal normal 14px/1 cdoicons;
  font-size: .875em;
  color: #292929;
  vertical-align: middle;
  text-rendering: auto;
  webkit-font-smoothing: antialiased;
  moz-osx-font-smoothing: grayscale;
}

.fcdo:before {
  speak: none;
}

.fcdo-lg {
  font-size: 1.33333333em;
  line-height: .75em;
  vertical-align: -15%;
}

.fcdo-2x {
  font-size: 2em;
}

.fcdo-3x {
  font-size: 3em;
}

.fcdo-4x {
  font-size: 4em;
}

.fcdo-5x {
  font-size: 5em;
}

.fcdo-fw {
  width: 1.28571429em;
  text-align: center;
}

.fcdo-s16 {
  font-size: 16px;
}

.fcdo-s18 {
  font-size: 18px;
}

.fcdo-s20 {
  font-size: 20px;
}

.fcdo-s25 {
  font-size: 25px;
}

.fcdo--zero {
  vertical-align: 0;
}

.fcdo--nudge {
  vertical-align: -1px;
}

.fcdo--nudge2 {
  vertical-align: -2px;
}

.fcdo--lh0 {
  line-height: 0;
}

.fcdo-s25.fcdo--lh0 {
  vertical-align: -5px;
}

.fcdo-trending-down:before {
  content: "\e900";
}

.fcdo-trending-up:before {
  content: "\e901";
}

.fcdo-quiz:before {
  content: "\e902";
}

.fcdo-dataset:before {
  content: "\e903";
}

.fcdo-switch:before {
  content: "\e904";
}

.fcdo-diigo:before {
  content: "\e906";
}

.fcdo-search:before {
  content: "\f002";
}

.fcdo-star:before {
  content: "\f005";
}

.fcdo-user:before {
  content: "\f007";
}

.fcdo-check:before {
  content: "\f00c";
}

.fcdo-check:empty:before {
  content: "\f00c";
}

.fcdo-close:before {
  content: "\f00d";
}

.fcdo-close:empty:before {
  content: "\f00d";
}

.fcdo-refresh:before {
  content: "\f021";
}

.fcdo-lock:before {
  content: "\f023";
}

.fcdo-volume-up:before {
  content: "\f028";
}

.fcdo-book:before {
  content: "\f02d";
}

.fcdo-pencil:before {
  content: "\f040";
}

.fcdo-chevron-right:before {
  content: "\f054";
}

.fcdo-arrow-left:before {
  content: "\f060";
}

.fcdo-arrow-right:before {
  content: "\f061";
}

.fcdo-arrow-up:before {
  content: "\f062";
}

.fcdo-arrow-down:before {
  content: "\f063";
}

.fcdo-plus:before {
  content: "\f067";
}

.fcdo-minus:before {
  content: "\f068";
}

.fcdo-chevron-up:before {
  content: "\f077";
}

.fcdo-chevron-down:before {
  content: "\f078";
}

.fcdo-twitter:before {
  content: "\f099";
}

.fcdo-facebook:before {
  content: "\f09a";
}

.fcdo-feed:before {
  content: "\f09e";
}

.fcdo-rss:before {
  content: "\f09e";
}

.fcdo-globe:before {
  content: "\f0ac";
}

.fcdo-chain:before {
  content: "\f0c1";
}

.fcdo-link:before {
  content: "\f0c1";
}

.fcdo-copy:before {
  content: "\f0c5";
}

.fcdo-files-o:before {
  content: "\f0c5";
}

.fcdo-bars:before,.fcdo-navicon:before,.fcdo-reorder:before {
  content: "\f0c9";
}

.fcdo-caret-right:before {
  content: "\f0da";
}

.fcdo-envelope:before {
  content: "\f0e0";
}

.fcdo-linkedin:before {
  content: "\f0e1";
}

.fcdo-exchange:before {
  content: "\f0ec";
}

.fcdo-angle-left:before {
  content: "\f104";
}

.fcdo-angle-right:before {
  content: "\f105";
}

.fcdo-angle-up:before {
  content: "\f106";
}

.fcdo-angle-down:before {
  content: "\f107";
}

.fcdo-circle:before {
  content: "\f111";
}

.fcdo-keyboard-o:before {
  content: "\f11c";
}

.fcdo-unlock:before {
  content: "\f13e";
}

.fcdo-tumblr:before {
  content: "\f173";
}

.fcdo-share-alt:before {
  content: "\f1e0";
}

.fcdo-trash:before {
  content: "\f1f8";
}

.fcdo-reddit-alien:before {
  content: "\f281";
}

.fcdo-upload:before {
  content: "\f093";
}

.fcdo-comment-o:before {
  content: "\f0e5";
}

.fcdo-caret-down:before {
  content: "\f0d7";
}

.fcdo-caret-up:before {
  content: "\f0d8";
}

.fcdo-question:before {
  content: "?";
  font-weight: bold;
}

.fcdo-fast-forward:before {
  content: "\f050";
}

a.a--b {
  font-weight: bold!important;
}

a.a--rev,a.a--none {
  text-decoration: none!important;
}

a.a--rev:hover {
  text-decoration: underline!important;
}

.cdo-hdr {
  z-index: 999999!important;
}

label,.label {
  display: block;
  margin: 0;
  padding: 11px 0;
  font-weight: bold;
}

input[type=text],input[type=email],input[type=password],input.text,textarea,select {
  padding: 11px;
  width: 100%;
  border: 1px solid #ddd;
  background: #f1f1f1;
  box-sizing: border-box;
  border-radius: 2px;
  box-shadow: inset 1px 1px 2px 0 rgba(0,0,0,0.1);
  color: #444;
}

input[type=text],input[type=email],input[type=password],input.text {
  height: 44px;
}

.input-wrap {
  display: inline-block;
  width: 100%;
  vertical-align: bottom;
}

.form div em {
  display: block;
  margin: 5px 0 20px;
  color: #666;
}

.form>div {
  clear: both;
  margin-bottom: 10px;
}

.form input.btn {
  margin: 20px 0 10px;
}

.form__inline label {
  float: none;
  display: inline;
  padding: 0 10px 0 0;
  width: auto;
  font-weight: normal;
}

.form__inline input {
  float: left;
  clear: left;
  margin: 3px 5px 5px 0;
  width: auto;
  border: 0 none;
}

.form__list {
  display: inline-block;
  line-height: 1.3em;
  padding-top: 11px;
}

.form--restrict input[type=text],.form--restrict input[type=email],.form--restrict input[type=password],.form--restrict input.text,.form--restrict textarea,.form--restrict select {
  max-width: 450px;
}

@media screen and (min-width:600px) {
  label {
    float: left;
    width: 25%;
  }

  input[type=text],input[type=email],input[type=password],input.text,textarea,select,.input-wrap {
    width: 75%;
  }

  .input-wrap input.text,.input-wrap textarea,.input-wrap select {
    width: 100%;
  }

  .form div em {
    margin-left: 25%;
  }

  .form--stacked label,.form--stacked input[type=text],.form--stacked input[type=email],.form--stacked input[type=password],.form--stacked input.text,.form--stacked textarea,.form--stacked select,.form--stacked .input-wrap {
    width: 100%;
  }
}

@media screen and (min-width:762px) {
  .form .form__split {
    float: left;
    width: 48%;
    clear: none;
  }

  .form .form__split--last {
    float: right;
  }
}

.text--ico-key input.text,.text--ico-key textarea,.text--ico-key select {
  padding-right: 40px;
}

.csstransforms3d .point {
  display: block!important;
  position: absolute;
  top: 0;
  left: 0;
  height: 10px;
  width: 10px;
  background: #fff;
  -moz-transform: rotate(45deg);
  -webkit-transform: rotate(45deg);
  transform: rotate(45deg);
}

.csstransforms3d .tiles--pointer input[type="radio"]:checked+label:after {
  content: "";
  position: absolute;
  bottom: -8px;
  left: 50%;
  height: 16px;
  width: 16px;
  margin-left: -8px;
  background: #d0a44c;
  -moz-transform: rotate(45deg);
  -webkit-transform: rotate(45deg);
  transform: rotate(45deg);
}

.btn {
  display: inline-block;
  padding: 10px 12px;
  text-align: center;
  background: #234b9a;
  border: solid 1px #234b9a;
  color: #fff;
  text-decoration: none;
  line-height: 1em;
  cursor: pointer;
  -webkit-border-radius: 2px;
  -moz-border-radius: 2px;
  border-radius: 2px;
}

.btn--impact {
  background: #caa54c;
  border-color: #caa54c;
  color: #111;
  font-weight: bold;
}

.btn--impact:hover {
  background: #b79441;
}

.btn--impact2 {
  padding: 11px 13px;
  border-width: 0;
  background: rgba(0,0,0,0.34);
  font-weight: bold;
}

.btn--impact2:hover {
  background: rgba(0,0,0,0.45);
}

.btn--alt {
  background: #dde2f0;
  border-color: #dde2f0;
}

.btn--alt:hover {
  background: #c7cee2;
}

.btn--white {
  background: #fff;
  border-color: #fff;
}

.btn--white:hover {
  background: #f4f4f4;
}

.btn--white,.btn--alt,.btn--alt2 {
  color: #292929;
}

.btn--blue {
  color: #234b9a;
}

.btn--big {
  font-size: 1.1em;
}

.btn--lrg {
  font-size: 1.1em;
  font-weight: bold;
  padding: 12px 20px;
}

.btn--small {
  font-size: .875em;
}

.btn--bold,input.btn {
  font-weight: bold;
}

.btn--dropdown {
  padding-right: 30px;
}

.btn--dropdown-pad {
  padding-right: 40px;
}

.btn--dropdown:after {
  position: absolute;
  content: "\f078";
  top: 50%;
  right: 10px;
  margin-top: -8px;
  font-size: 16px;
  line-height: 1em;
  color: #d0a44c;
  font-weight: 300;
  font-family: cdoicons;
}

.btn--dropdown.on:after {
  content: "\f077";
}

.btn--options {
  font-size: .8em;
  padding: 10px 30px 10px 10px;
  background: #dde2f0;
  color: #292929;
  border: 0;
  border-radius: 0;
}

.btn--options:hover {
  background: #dde2f0;
}

.btn--options:after {
  font-size: .9em;
  margin-top: -5px;
  color: #234b9a;
}

.btn--plus.on {
  border-radius: 2px 2px 0 0;
}

.btn--plus.on .fcdo:before {
  content: "\f068";
}

.btn--input {
  height: 44px;
  padding: 12px 16px;
  border-radius: 0 2px 2px 0;
}

.btn--input--nudge {
  padding-bottom: 13px;
}

.btn--translate:before {
  content: " ";
  position: absolute;
  background: url(/ko/external/images/sprite1.png?version=4.0.94) 100px 100px no-repeat;
}

.btn--translate {
  position: relative;
  padding: 12px 12px 12px 43px;
}

.btn--translate:before {
  width: 31px;
  height: 31px;
  top: 4px;
  left: 10px;
  background-position: -550px 0;
}

.btn--shop {
  padding: 18px 25px;
}

.btn .fcdo {
  color: inherit;
}

.btn--alt .fcdo {
  color: #354da5;
}

.btn--small .fcdo {
  font-size: 1.14286em;
}

.btn--ico-l {
  position: relative;
  padding-left: 33px;
}

.btn--ico-l--extra-pad {
  padding-left: 40px;
}

.btn--ico-l .fcdo {
  position: absolute;
  top: 50%;
  left: 10px;
  height: 100%;
  margin-top: -12px;
  line-height: 100%;
  font-size: 22px;
}

.btn--ico-l .fcdo-quiz {
  left: 10px;
  margin-top: -13px;
  font-size: 26px;
}

body .btn--forbidden,body .btn--forbidden:hover {
  background-color: #999;
  border-color: #999;
  color: #111;
  cursor: not-allowed;
}

.cols,.cols__col {
  float: left;
  width: 100%;
  box-sizing: border-box;
}

.cols .cols__col:first-child {
  margin-left: 0;
}

.cols--icons .cols__col {
  padding: 70px 0 20px;
}

@media screen and (max-width:761px) {
  .cols--quarters .cols__col:nth-child(2n+1) {
    margin-left: 0;
    clear: both;
  }
}

@media screen and (min-width:450px) {
  .cols--half .cols__col,.cols--half-alt .cols__col,.cols--quarters .cols__col {
    margin-left: 6%;
    width: 47%;
  }

  .cols--half-alt .cols__col:first-child {
    width: 64%;
  }

  .cols--half-alt .cols__col:last-child {
    width: 30%;
  }

  .cols--half .cols__col:nth-child(2n+1),.cols--half-alt .cols__col:nth-child(2n+1) {
    margin-left: 0;
    clear: both;
  }
}

@media screen and (min-width:600px) {
  .cols--third .cols__col {
    margin-left: 2%;
    width: 32%;
  }

  .cols--third .cols__col:nth-child(3n+1) {
    margin-left: 0;
    clear: both;
  }
}

@media screen and (min-width:762px) {
  .cols--quarters .cols__col {
    margin-left: 2%;
    width: 23.5%;
  }

  .cols--quarters .cols__col:nth-child(4n+1) {
    margin-left: 0;
    clear: both;
  }
}

@media screen and (max-width:449px) {
  .cols--half .divided--notfirst {
    padding-top: 10px;
    border-top: solid 1px #e3e3e8;
  }
}

.txt-block {
  display: block;
  padding: 13px 20px;
  background: #eff1f6;
  font-weight: normal;
  box-sizing: border-box;
  text-decoration: none;
}

.txt-block--shallow {
  padding: 4px 20px;
}

.txt-block--padder {
  padding: 15px 20px;
}

.txt-block--alt,.txt-block--alt2 {
  background: #234b9a;
  color: #fff;
}

.txt-block--alt3 {
  background: #e84427;
  color: #fff;
}

.txt-block--impact {
  background: #d0a44c;
  color: #111;
}

.txt-block--alt .fcdo,.txt-block--alt2 .fcdo {
  color: #fff;
}

.txt-block--padl {
  padding-left: 70px;
}

.txt-block--padr {
  padding-right: 70px;
}

.txt-block--alt h2,.txt-block--alt h3,.txt-block--alt h4,.txt-block--alt h5,.txt-block--alt2 h2,.txt-block--alt2 h3,.txt-block--alt2 h4,.txt-block--alt2 h5,.txt-block--alt .h2,.txt-block--alt .h3,.txt-block--alt .h4,.txt-block--alt .h5,.txt-block--alt2 .h2,.txt-block--alt2 .h3,.txt-block--alt2 .h4,.txt-block--alt2 .h5 {
  color: inherit;
}

.txt-block--alt h3 span,.txt-block--alt .h3 span {
  color: #a7b5c9;
}

a.txt-block:hover span {
  text-decoration: underline;
}

a.txt-block {
  font-weight: bold;
}

a.txt-block--alt,a.txt-block--alt .fcdo,a.txt-block--alt2,a.txt-block--alt2 .fcdo {
  color: #fff;
}

a.txt-block--impact .fcdo {
  color: #303076;
}

a.txt-block:hover {
  opacity: .9;
}

.txt-block .with-el__el {
  top: 13px;
  right: 20px;
}

.txt-block .with-el__el--icons {
  top: 8px;
}

.txt-block.with-icons {
  padding: 8px 20px;
}

.txt-block.item-tag {
  position: relative;
}

.txt-block.item-tag h2,.txt-block.item-tag h3,.txt-block.item-tag h4,.txt-block.item-tag h5,.txt-block.item-tag .h2,.txt-block.item-tag .h3,.txt-block.item-tag .h4,.txt-block.item-tag .h5,.txt-block.item-tag p {
  margin-bottom: 0;
}

.txt-block .item-tag__tag {
  background: #aeb9c9;
}

.txt-block--alt .item-tag__tag {
  background: #12326f;
}

.txt-block--alt2 .item-tag__tag {
  background: #242b4e;
}

.txt-block .item-tag__tag--clear {
  background: transparent;
}

.dropdown {
  display: inline-block;
  position: relative;
}

.dropdown .btn {
  position: relative;
}

.dropdown__box {
  display: none;
  position: absolute;
  top: 100%;
  z-index: 2;
  background: #fff;
  color: #292929;
  min-width: 230px;
  max-width: 500px;
  font-size: .875em;
  box-shadow: 0 0 8px rgba(0,0,0,0.2);
}

.dropdown__box>* {
  margin-bottom: 0;
}

.dropdown__box li:first-child {
  margin-top: 5px;
}

.dropdown__box li:last-child {
  margin-bottom: 5px;
}

.dropdown__box.open {
  display: block;
}

.dropdown__box__none {
  padding: 10px 15px;
}

.dropdown__box a {
  display: block;
  text-decoration: none;
  color: #292929;
  line-height: 1.5em;
}

.dropdown__box a:hover {
  background: #f1f1f1;
  color: #242b4e;
}

.dropdown__box a.on {
  background: #f1f1f1;
  color: #e84427;
}

.dropdown__box a[data-disabled="1"] {
  color: #999;
}

.dropdown__box a[data-disabled="1"]:hover {
  background: transparent;
  cursor: default;
}

.dropdown--right .dropdown__box {
  left: auto;
  right: 0;
}

.dropdown--pad .dropdown__box {
  padding: 15px 20px;
}

.dropdown--pad-a .dropdown__box a {
  padding: 6px 16px;
}

.dropdown--pad-a .dropdown__box li {
  margin-bottom: 0;
}

.dropdown--pad-a .dropdown__box li:last-child {
  margin-bottom: 5px;
}

.dropdown--options .dropdown__box,.dropdown--create .dropdown__box {
  box-shadow: none;
}

.dropdown--options .dropdown__box {
  background: #dde2f0;
}

.dropdown--options .dropdown__box a {
  margin-bottom: 10px;
}

.dropdown--options .dropdown__box a:hover {
  background: 0;
  font-weight: bold;
}

.dropdown--options .dropdown__box .fcdo--dropdown,.dropdown--options .dropdown__box .fcdo--dropdown-alt {
  color: #234b9a;
  width: 22px;
}

.dropdown--options .dropdown__box .fcdo--dropdown {
  width: 40px;
  text-align: center;
}

.dropdown--options .dropdown__box .btn {
  padding: 6px 0;
}

.dropdown--options .dropdown__box .btn,.dropdown--options .dropdown__box .btn:hover {
  background: transparent;
  border-color: transparent;
}

.dropdown--options .dropdown__box .btn:hover {
  text-decoration: underline;
}

.dropdown--options .dropdown__box .btn .fcdo {
  font-size: 1.3em;
}

.dropdown--options .dropdown__box .btn .fcdo-quiz {
  font-size: 1.8em;
}

.dropdown--create .dropdown__box {
  background: #caa54c;
  color: #111;
  border-radius: 0 2px 2px 2px;
}

.dropdown--create.dropdown--right .dropdown__box {
  border-radius: 2px 0 2px 2px;
}

.dropdown--create input[type="text"] {
  float: left;
  background: #fff;
  width: 80%;
}

.dropdown--create button {
  width: 20%;
}

@media screen and (max-height:820px),screen and (max-width:599px) {
  .dropdown__box {
    max-height: 400px;
    overflow-y: auto;
  }
}

@media screen and (max-height:600px) {
  .dropdown__box {
    max-height: 300px;
    overflow-y: auto;
  }
}

.spr,.spr-b:before {
  display: inline-block;
  background: url(/ko/external/images/sprite1.png?version=4.0.94) 0 0 no-repeat;
}

.spr-b {
  position: relative;
}

.spr-b:before {
  content: " ";
  position: absolute;
  top: 0;
  left: 0;
}

.spr--logo-ftr {
  background-position: -325px 0;
  width: 205px;
  height: 42px;
}

.spr--microsoft {
  background-position: 0 -60px;
  width: 95px;
  height: 22px;
  margin-left: 15px;
  vertical-align: middle;
}

.spr--ico-close {
  background-position: -700px 0;
  width: 18px;
  height: 18px;
}

.spr--ico-fav-star {
  background-position: -579px -219px;
  width: 22px;
  height: 22px;
}

.spr--ico-fav-star-lrg {
  background-position: -579px -188px;
  width: 28px;
  height: 28px;
}

.spr--ico-user {
  background-position: -593px -31px;
  width: 22px;
  height: 22px;
}

.spr--ico-user-lrg {
  background-position: -593px 0;
  width: 28px;
  height: 28px;
}

.spr--ico-cambridge {
  background-position: -630px -31px;
  width: 22px;
  height: 22px;
}

.spr--ico-cambridge-lrg {
  background-position: -630px 0;
  width: 28px;
  height: 28px;
}

.spr--ico-community {
  background-position: -667px -31px;
  width: 22px;
  height: 22px;
}

.spr--ico-community-lrg {
  background-position: -667px 0;
  width: 28px;
  height: 28px;
}

.spr--ico-switch-lrg {
  background-position: -118px -243px;
  width: 42px;
  height: 42px;
}

.spr--ico-translate {
  background-position: -550px 0;
  width: 26px;
  height: 28px;
}

.spr--promo-widget:before {
  background-position: -100px 0;
  width: 67px;
  height: 53px;
}

.spr--promo-apps:before {
  background-position: -225px 0;
  width: 31px;
  height: 54px;
}

.spr--question-bg:before {
  background-position: -483px -59px;
  width: 235px;
  height: 105px;
}

.spr--ico-key-define:before {
  background-position: 0 -89px;
  width: 96px;
  height: 62px;
}

.spr--ico-key-examples:before {
  background-position: -127px -89px;
  width: 110px;
  height: 62px;
}

.spr--ico-key-levels:before {
  background-position: -371px -89px;
  width: 71px;
  height: 62px;
}

.spr--ico-key-levels1:before {
  background-position: -207px -234px;
  width: 71px;
  height: 62px;
}

.spr--ico-key-guidewords:before {
  background-position: -269px -89px;
  width: 62px;
  height: 62px;
}

.spr--ico-key-corpus:before {
  background-position: -290px -161px;
  width: 75px;
  height: 62px;
}

.spr--ico-key-hear:before {
  background-position: 0 -161px;
  width: 103px;
  height: 62px;
}

.spr--ico-key-useful:before {
  background-position: -390px -161px;
  width: 60px;
  height: 62px;
}

.spr--ico-key-coverage:before {
  background-position: -142px -161px;
  width: 108px;
  height: 62px;
}

.spr--ico-key-thesaurus:before {
  background-position: 0 -235px;
  width: 83px;
  height: 62px;
}

.spr--ico-key-dictionary:before {
  background-position: -471px -185px;
  width: 82px;
  height: 103px;
}

.spr--ico-fav-star-lrg--inline {
  vertical-align: -8px;
}

.ico-bg:before,.ico-bg:after,.ico-bg-abs:before,.ico-bg-abs:after {
  font-weight: 300;
  font-family: cdoicons;
  content: none;
  padding-right: 7px;
}

.ico-bg:after {
  padding: 0 0 0 7px;
}

.ico-bg-abs {
  position: relative;
}

.ico-bg-abs:before,.ico-bg-abs:after {
  position: absolute;
  padding: 0;
  top: 50%;
  left: 10px;
  margin-top: -7px;
  font-size: 14px;
}

.ico-bg-abs:after {
  left: auto;
  right: 10px;
}

.ico-bg--chevron:after {
  content: "\f078";
}

.ico-bg--chevron.on:after {
  content: "\f077";
}

.ico-bg--arrow:before {
  content: "\f061";
}

.ico-bg--arrow-end:after {
  content: "\f061";
}

.ico-bg--key:after {
  content: "\f11c";
  margin-top: -8px;
  font-size: 16px;
}

.trans-all--250 {
  -webkit-transition: all 250ms linear;
  -moz-transition: all 250ms linear;
  -ms-transition: all 250ms linear;
  -o-transition: all 250ms linear;
  transition: all 250ms linear;
}

.trans-all--1s {
  -webkit-transition: all 1s linear;
  -moz-transition: all 1s linear;
  -ms-transition: all 1s linear;
  -o-transition: all 1s linear;
  transition: all 1s linear;
}

.cdo-hero {
  position: relative;
  height: 200px;
  text-align: left;
  padding: 25px 0;
  background: url(/ko/external/images/hero.jpg?version=4.0.94) no-repeat -150px 0;
  background-size: cover;
}

.cdo-hero__caption {
  position: absolute;
  bottom: 75px;
  left: 0;
  width: 100%;
  text-align: right;
}

.cdo-hero__caption a {
  padding: 4px 7px;
  background: #000;
  color: #fff;
  background: rgba(12,12,12,0.8);
  color: rgba(255,255,255,0.8);
  text-decoration: none;
  font-size: .694em;
}

.cdo-hero__title {
  max-width: 190px;
  color: #fff;
  font-weight: normal;
  font-size: 1.39em;
}

.cdo-hero--error {
  height: auto;
  text-align: left;
}

.cdo-hero__error {
  color: #fff;
  max-width: 96%;
}

.cdo-hero__error h1 {
  margin-bottom: 10px;
  color: #fff;
  font-size: 2em;
}

.cdo-hero__error .emphasized {
  font-style: normal;
}

.cdo-hero__error .emphasized a {
  color: #d0a44c;
}

.cdo-hero--light .cdo-hero__caption a {
  background: #fff;
  color: #000;
  background: rgba(255,255,255,0.75);
  color: rgba(0,0,0,0.75);
}

.cdo-hero--light .cdo-hero__title {
  color: #111;
}

@media screen and (min-width:450px) {
  .cdo-hero {
    background-position: -100px 0;
  }

  .cdo-hero__title {
    max-width: 240px;
  }
}

@media screen and (min-width:600px) {
  .cdo-hero {
    background-position: 0 0;
  }

  .cdo-hero__title {
    max-width: 335px;
    font-size: 1.5em;
  }
}

@media screen and (min-width:762px) {
  .cdo-hero {
    background-position: center center;
  }

  .cdo-hero__title {
    max-width: 280px;
  }

  .cdo-hero__caption {
    bottom: 80px;
  }

  .cdo-hero__caption a {
    font-size: .625em;
  }
}

@media screen and (min-width:960px) {
  .cdo-hero {
    height: 350px;
    padding: 50px 0 0;
    text-align: left;
  }

  .cdo-hero__caption {
    bottom: 115px;
    text-align: right;
  }

  .cdo-hero__title {
    max-width: 340px;
    padding-left: 87px;
  }

  .cdo-hero__error {
    margin-left: 30%;
    max-width: 600px;
  }

  .cdo-hero__error h1 {
    font-size: 2.75em;
  }
}

@media screen and (min-width:1080px) {
  .cdo-hero__title {
    padding-left: 105px;
  }
}

@media screen and (min-width:1280px) {
  .cdo-hero__title {
    max-width: 500px;
  }
}

.cdo-hero--error {
  background-image: url(/ko/external/images/hero-error.jpg?version=4.0.94);
}

.cdo-hero--light {
  background-image: url(/ko/external/images/hero-light.jpg?version=4.0.94);
}

.cdo-hdr__soc {
  float: right;
  margin-left: 30px;
}

.cdo-hdr__soc ul {
  margin: 0;
}

.cdo-hdr__soc li {
  display: inline-block;
  line-height: 48px;
  margin: 0 0 0 5px;
}

.cdo-hdr__soc li:first-child {
  margin: 0 5px 0 0;
  font-size: .875em;
}

.cdo-hdr__soc a {
  color: #fff;
  display: inline-block;
  height: 26px;
  line-height: 22px;
  width: 26px;
  vertical-align: 2px;
  text-align: center;
}

.cdo-hdr__profile {
  float: right;
}

.cdo-hdr__profile .dropdown {
  margin-left: 15px;
}

.cdo-hdr__profile .dropdown:first-child {
  margin-left: 0;
}

.cdo-hdr__profile a.hdr-btn {
  display: inline-block;
  font-size: .875em;
  line-height: 48px;
  text-decoration: none;
  color: #fff;
}

.cdo-hdr__profile a.hdr-btn:after {
  display: none;
}

.cdo-hdr__profile a.hdr-btn .fcdo {
  color: #999;
  font-size: 1.6em;
  padding-right: 4px;
}

.cdo-hdr__profile a.hdr-btn:hover .fcdo,.cdo-hdr__profile a.hdr-btn.on .fcdo {
  color: #fff;
}

@media screen and (min-width:960px) {
  .cdo-hdr__profile .dropdown {
    margin-left: 30px;
  }

  .cdo-hdr__profile a.hdr-btn:after {
    color: #d0a44c;
    font-size: .8em;
    display: inline;
  }

  .cdo-hdr__profile a.hdr-btn .fcdo {
    font-size: 1.2em;
  }
}

.cdo-hdr__myDictionary {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 5px;
}

.cdo-hdr__nav ul {
  margin: 0;
  list-style: none;
}

.cdo-hdr__nav li {
  display: inline;
  margin: 0 30px 0 0;
}

.cdo-hdr__nav a {
  display: inline-block;
  line-height: 45px;
  color: inherit;
  text-decoration: none;
  padding: 0 2px;
}

.cdo-hdr__nav .active a {
  font-weight: bold;
  border-top: 3px solid #d0a44c;
}

.burger {
  float: left;
  width: 22px;
  height: 16px;
  line-height: 1em;
  margin: 16px 30px 0 0;
}

.burger span,.burger span:before,.burger span:after {
  display: block;
  height: 2px;
  background: #fff;
  position: relative;
  top: 7px;
  left: 0;
  display: block;
  content: '';
}

.burger span:before {
  top: -7px;
}

.burger span:after {
  top: 5px;
}

.off-canvas {
  position: fixed;
  top: 0;
  left: -290px;
  z-index: 1000001;
  height: 100%;
  width: 290px;
  background: #eef1f5;
  overflow-y: auto;
}

.off-canvas__close {
  position: absolute;
  top: 0;
  right: 20px;
  font-size: 1.5em;
  cursor: pointer;
}

.off-canvas__pad {
  padding: 20px;
}

.off-canvas__nav ul,.off-canvas__nav li {
  margin: 0;
}

.off-canvas__nav>ul>li {
  border-top: 1px solid #cfd1e8;
}

.off-canvas__nav li a {
  display: block;
  padding: 15px 20px;
  text-decoration: none;
  color: #242b4e;
}

.off-canvas__nav li a.hide {
  display: none;
}

.off-canvas__nav li a:hover {
  background: #e3e7ee;
}

.off-canvas__nav>ul>li>a {
  font-size: 1.125em;
}

.off-canvas__nav>ul>li>a.on {
  background: #234b9a;
  color: #fff;
}

.off-canvas__nav>ul>li>a.on:after {
  color: rgba(255,255,255,0.54);
}

.off-canvas .btn--impact {
  display: block;
  padding: 14px 12px;
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  border-radius: 5px;
}

.off-canvas .btn--impact .fcdo {
  margin-right: 5px;
  vertical-align: -2px;
  font-size: 20px;
}

.off-canvas__dropdown {
  margin: 20px 0 0;
  font-size: .875em;
}

.off-canvas__dropdown a {
  text-decoration: none;
}

.off-canvas__dropdown a.ico-bg .fcdo {
  color: rgba(36,43,78,0.60);
  margin-right: 3px;
  font-size: 20px;
  vertical-align: -3px;
}

.off-canvas__dropdown a.ico-bg:after {
  color: #1d4d97;
  font-size: 12px;
  padding-left: 5px;
}

.off-canvas__dropdown ul {
  margin: 10px 0 0 24px;
}

.off-canvas__dropdown li a:hover {
  text-decoration: underline;
}

.off-canvas__dropdown li:before {
  content: "\f054";
  padding-right: 7px;
  vertical-align: middle;
  font-size: 12px;
  font-weight: 300;
  font-family: cdoicons;
  color: rgba(35,75,154,0.47);
}

.off-canvas__nav .ico-bg-abs:after {
  right: 21px;
  margin-top: -13px;
  color: #234b9a;
}

.off-canvas__nav>ul>li>ul>li>a {
  font-weight: bold;
  background: #dde3f1;
}

.off-canvas__nav>ul>li>ul>li {
  border-bottom: solid 1px #fff;
}

.off-canvas__nav>ul>li>ul>li:last-child {
  border-bottom-width: 0;
}

.off-canvas__nav>ul>li>ul>li>a.on {
  background: #bfcce9;
}

.off-canvas__nav ul ul a {
  padding: 10px 20px;
  font-size: .875em;
}

.off-canvas__nav ul ul li a:hover {
  background: #d5dae7;
}

.off-canvas__nav ul ul li a.ico-bg-abs:after {
  color: rgba(35,75,154,0.53);
}

.off-canvas__nav ul ul li a.ico-bg-abs.on:after {
  color: #234b9a;
}

.off-canvas__nav ul ul ul li {
  padding: 7px 20px;
}

.off-canvas__nav ul ul ul a {
  display: inline;
  padding: 0;
}

.off-canvas__nav ul ul ul li:first-child {
  margin-top: 10px;
}

.off-canvas__nav ul ul ul li:last-child {
  margin-bottom: 10px;
}

.off-canvas__nav ul ul ul a:hover {
  background: transparent;
  text-decoration: underline;
}

.off-canvas__nav ul ul ul li:before {
  content: "\f054";
  padding-right: 7px;
  vertical-align: -1px;
  font-size: 12px;
  font-weight: 300;
  font-family: cdoicons;
  color: rgba(35,75,154,0.47);
}

.off-canvas__nav .pointer .fcdo {
  margin-right: 5px;
  color: #e84427;
}

.off-canvas__nav li.off-canvas__nav__section {
  padding: 15px 20px 5px;
  font-size: .875em;
}

.off-canvas__nav li.off-canvas__nav__section:before {
  content: none;
}

.off-canvas__nav li.off-canvas__nav__section:first-child {
  padding-top: 5px;
}

.nav-active .overlay {
  height: 100%;
}

.nav-active .off-canvas {
  left: 0;
}

.cdo-search {
  color: #292929;
  padding: 14px 20px 13px;
}

.cdo-search__bar {
  float: left;
  width: 100%;
  margin-right: 10px;
  position: relative;
  height: 50px;
}

.cdo-search__controls {
  float: right;
}

.cdo-search__input[type=text],.cdo-search__dataset,.cdo-search__button {
  float: left;
  position: relative;
  z-index: 5;
  height: 50px;
  padding: 0 15px;
  border: 0;
}

.cdo-search__input[type=text] {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  background: #fff;
  border: 1px solid #ddd;
  border-radius: 3px;
  box-shadow: none;
}

.cdo-search__dataset {
  background: #fff;
  border-left: solid 1px #c7c7c7;
  height: 30px;
  margin-top: 10px;
  padding-right: 35px;
  text-align: left;
}

.cdo-search__dataset .fcdo {
  color: inherit;
  font-size: 1.2em;
}

.cdo-search__dataset:after {
  font-size: .8em;
  right: 15px;
}

.cdo-search__dataset:focus {
  outline: 0;
}

.cdo-search__dataset:hover,.cdo-search__dataset.on {
  color: #234b9a;
}

.cdo-search__button {
  background: #d0a44c;
  color: #fff;
  font-size: 1.8em;
  border-top-right-radius: 3px;
  border-bottom-right-radius: 3px;
}

.cdo-search__button .fcdo {
  color: inherit;
}

.cdo-search__switches {
  padding-top: 7px;
  max-height: 53px;
  overflow: hidden;
}

.cdo-search__switches .btn {
  background: transparent;
  border-color: transparent;
  margin-bottom: 10px;
}

.cdo-search__switches .btn .fcdo {
  color: #d0a44c;
}

.cdo-search__switches .btn:hover {
  background-color: #3d3d3d;
}

.cdo-search__switches .btn--selected {
  font-weight: bold;
}

.cdo-search--mod {
  background: #11326f;
}

.cdo-search--mod .cdo-search__bar {
  float: none;
  width: auto;
  margin: 0;
}

.cdo-search--mod .cdo-search__switches {
  display: block;
  padding-top: 15px;
}

.cdo-search--mod .cdo-search__switches .btn {
  background: #334f83;
  margin-right: 5px;
}

.cdo-search--mod .cdo-search__switches .btn:hover {
  background-color: #4f6794;
}

.cdo-search--mod .cdo-search__switches .btn--selected {
  background-color: #d0a44c;
  color: #292929;
}

.cdo-search--mod .cdo-search__switches .btn--selected .fcdo {
  color: #292929;
  vertical-align: 0;
}

.cdo-search__mega-menu {
  display: none;
  position: absolute;
  z-index: 4;
  top: -8px;
  left: -8px;
  right: -8px;
  background: #eef1f5;
  padding: 80px 0 40px;
  -moz-border-radius: 3px;
  -webkit-border-radius: 3px;
  border-radius: 3px;
  box-shadow: 0 0 3px 3px rgba(0,0,0,0.15);
}

.cdo-search__mega-menu h2,.cdo-search__mega-menu .h2 {
  margin-bottom: 10px;
  color: #234b9a;
  font-size: 1.1875em;
}

.cdo-search__mega-menu h3,.cdo-search__mega-menu .h3 {
  font-weight: bold;
  font-size: 1em;
}

.cdo-search__mega-menu p {
  color: #777;
  font-size: .875em;
}

.cdo-search__mega-menu a {
  font-size: .875em;
  color: #333;
}

.cdo-search__mega-menu ul {
  margin-left: 0;
  list-style: none;
}

.cdo-search__mega-menu li {
  margin-bottom: 5px;
}

.cdo-search__mega-menu li:before {
  content: "\f054";
  padding-right: 7px;
  vertical-align: middle;
  font-size: 12px;
  font-weight: 300;
  font-family: cdoicons;
  color: rgba(35,75,154,0.47);
}

.cdo-search__mega-menu li .fcdo {
  margin-right: 5px;
  color: #e84427;
}

.cdo-search__mega-menu__foot {
  position: absolute;
  top: 60px;
  right: 0;
  width: 60px;
  padding: 8px 15px;
  text-align: right;
}

.cdo-search__mega-menu__foot .fcdo {
  color: rgba(35,75,154,0.40);
  font-size: 1.125em;
}

.cdo-search__mega-menu.open {
  display: block;
}

.home_layout .cdo-search__controls .ico-bg-abs:after {
  margin-top: -10px;
}

.home_layout .cdo-search__mega-menu__foot {
  top: 73px;
}

@media screen and (min-width:600px) {
  .cdo-search__bar {
    width: 70%;
  }
}

@media screen and (min-width:768px) {
  .cdo-search__dataset .fcdo {
    display: none;
  }
}

@media screen and (min-width:960px) {
  .cdo-search {
    padding: 14px 30px 13px;
  }

  .cdo-search--mod {
    padding: 20px;
    margin-bottom: 0;
  }

  .cdo-search--mod .cdo-search__bar {
    height: 67px;
  }

  .cdo-search--mod .cdo-search__input[type=text],.cdo-search--mod .cdo-search__dataset,.cdo-search--mod .cdo-search__button {
    height: 67px;
    padding: 0 22px;
  }

  .cdo-search--mod .cdo-search__input[type=text] {
    font-size: 1.2em;
  }

  .cdo-search--mod .cdo-search__dataset {
    height: 47px;
    font-size: 1.2em;
    padding: 0 40px 0 22px;
  }

  .cdo-search__bar {
    width: 50%;
  }

  .cdo-search__dataset {
    min-width: 230px;
  }
}

@media screen and (max-height:1020px) {
  .cdo-search__mega-menu__canvas {
    max-height: 600px;
    overflow-y: auto;
  }
}

@media screen and (max-height:920px) {
  .cdo-search__mega-menu__canvas {
    max-height: 550px;
    overflow-y: auto;
  }
}

@media screen and (max-height:820px),screen and (max-width:599px) {
  .cdo-search__mega-menu__canvas {
    max-height: 500px;
    overflow-y: auto;
  }
}

@media screen and (max-height:720px) {
  .cdo-search__mega-menu__canvas {
    max-height: 400px;
    overflow-y: auto;
  }
}

@media screen and (max-height:600px) {
  .cdo-search__mega-menu__canvas {
    max-height: 300px;
    overflow-y: auto;
  }
}

@media screen and (max-width:1079px) {
  .cdo-search__mega-menu {
    top: 0;
    left: 0;
    right: 0;
    padding: 50px 0 0;
    font-size: .9375em;
    background: transparent;
  }

  .cdo-search__mega-menu .pad-extra {
    padding: 0;
    background: #fff;
  }

  .cdo-search__mega-menu h2,.cdo-search__mega-menu .h2 {
    margin-bottom: 1px;
    padding: 15px 15px;
    color: #fff;
    font-weight: normal;
    background: #12326f;
    cursor: pointer;
  }

  .cdo-search__mega-menu__col2 h2,.cdo-search__mega-menu__col2 .h2 {
    margin-bottom: 0;
  }

  .cdo-search__mega-menu__links {
    display: none;
    padding: 20px;
  }

  .cdo-search__mega-menu__links>*:last-child {
    margin-bottom: 0;
  }

  .cdo-search__mega-menu__links.open {
    display: block;
  }

  .cdo-search__mega-menu__foot {
    display: none;
  }

  .cdo-search__mega-menu p {
    display: none;
  }

  .cdo-search__mega-menu .h2 {
    position: relative;
  }

  .cdo-search__mega-menu .h2:after {
    position: absolute;
    content: "\f078";
    right: 20px;
    top: 50%;
    margin-top: -12px;
    font-size: 12px;
    font-weight: 300;
    font-family: cdoicons;
    color: #f74f31;
  }

  .cdo-search__mega-menu .h2.on {
    background: #244b9a;
  }

  .cdo-search__mega-menu .h2.on:after {
    content: "\f077";
  }
}

@media screen and (max-width:599px) {
  .cdo-search__mega-menu {
    font-size: 1em;
  }
}

@media screen and (min-width:1080px) {
  .cdo-search__mega-menu {
    padding-top: 100px;
  }

  .cdo-search__mega-menu__col1,.cdo-search__mega-menu__col2 {
    float: left;
    width: 47%;
  }

  .cdo-search__mega-menu__col2 {
    margin-left: 6%;
  }

  .home_layout .cdo-search__mega-menu {
    padding-top: 110px;
  }
}

@media screen and (min-width:1280px) {
  .cdo-search__mega-menu__col1 {
    width: 245px;
  }

  .cdo-search__mega-menu__col2 {
    float: none;
    width: auto;
    margin-left: 275px;
  }
}

@media screen and (min-width:1380px) {
  .cdo-search__mega-menu__col1 {
    width: 205px;
  }

  .cdo-search__mega-menu__col2 {
    margin-left: 235px;
  }

  .cdo-search__mega-menu__col2 ul {
    float: left;
    width: 100%;
  }

  .cdo-search__mega-menu__col2 li {
    float: left;
    width: 50%;
  }
}

@media screen and (min-width:1380px) and (max-width:1549px) {
  .cdo-search__mega-menu {
    font-size: .875em;
  }

  .cdo-search__mega-menu .fcdo {
    font-size: 14px;
  }
}

@media screen and (min-width:1550px) {
  .cdo-search__mega-menu__col1 {
    width: 245px;
  }

  .cdo-search__mega-menu__col2 {
    margin-left: 275px;
  }
}

.cdo-hdr__blocks {
  position: relative;
  margin-top: -65px;
}

.cdo-hdr__blocks--home .mod {
  display: none;
}

@media screen and (min-width:960px) {
  .cdo-hdr__blocks {
    margin-top: -95px;
  }

  .cdo-hdr__blocks--home .cdo-search {
    float: left;
    width: 600px;
  }

  .cdo-hdr__blocks--home .mod {
    display: block;
    float: right;
    width: 280px;
  }
}

@media screen and (min-width:1080px) {
  .cdo-hdr__blocks--home .cdo-search {
    width: 725px;
  }
}

@media screen and (min-width:1280px) {
  .cdo-hdr__blocks--home .cdo-search {
    width: 920px;
  }

  .cdo-hdr__blocks--home .mod {
    width: 300px;
  }

  .cdo-hdr__blocks--int .cdo-search {
    float: none;
    width: auto;
    margin-right: 320px;
  }
}

@media screen and (min-width:1380px) {
  .cdo-hdr__blocks--home .cdo-search {
    width: 1020px;
  }
}

.ftr {
  padding: 35px 0 56px;
  background: #1e1e1e;
  color: #888;
}

.ftr__nav {
  float: left;
}

.ftr nav>ul {
  margin-bottom: 0;
}

.ftr nav>ul>li {
  clear: both;
  margin: 0 20px 15px 0;
}

.ftr nav>ul>li:last-child {
  margin-right: 0;
}

.ftr nav>ul>li>a {
  color: #fff;
  font-size: 1.25em;
}

.ftr nav>ul>li>ul {
  display: none;
}

.ftr nav a {
  text-decoration: none;
  color: #888;
}

.ftr nav a:hover {
  text-decoration: underline;
}

.ftr .cols__col {
  width: auto;
  margin-right: 25px;
}

.ftr .cols__col:last-child {
  margin-right: 0;
}

.ftr__follow {
  float: right;
}

.ftr__follow .btnfeat {
  margin-left: 10px;
  margin-right: 0;
}

.ftr__copy {
  float: left;
  width: 100%;
  margin-top: 20px;
  text-align: center;
  font-size: .8125em;
}

.ftr__copy a {
  margin: 0 0 10px;
}

@media screen and (max-width:599px) {
  .ftr__nav {
    width: 50%;
  }

  .ftr nav>ul>li>ul {
    margin-bottom: 0;
  }

  .ftr .ico-bg-abs {
    padding-right: 25px;
  }

  .ftr .ico-bg-abs:after {
    content: "\f107";
    margin-top: -8px;
  }

  .ftr .ico-bg-abs.open:after {
    content: "\f106";
  }
}

@media screen and (min-width:600px) {
  .ftr nav>ul>li {
    clear: none;
  }

  .ftr nav a {
    font-size: .875em;
  }

  .ftr nav>ul>li>a {
    font-size: 1.125em;
  }

  .ftr nav>ul>li>ul {
    display: block;
  }

  .ftr nav>ul>li li {
    max-width: 150px;
  }

  .ftr nav>ul>li:after {
    content: none;
  }
}

@media screen and (min-width:762px) {
  .ftr .cols__col {
    margin-right: 60px;
  }

  .ftr .cols__col:last-child {
    margin-right: 20px;
  }

  .ftr nav>ul>li li {
    max-width: 225px;
  }

  .ftr__copy {
    clear: right;
    float: right;
    width: auto;
    margin-top: 0;
    text-align: right;
  }
}

@media screen and (min-width:960px) {
  .ftr__copy {
    margin-top: 20px;
  }
}

@media screen and (max-width:1079px) {
  .ftr .btnfeat {
    display: block;
  }
}

@media screen and (min-width:1280px) {
  .ftr nav>ul>li li {
    max-width: 260px;
  }

  .ftr .cols__col {
    margin-right: 90px;
  }

  .ftr__copy {
    margin-top: 50px;
  }
}

.cdo-tpl__z {
  width: 100%;
  max-width: 100%;
  margin-bottom: 15px;
}

.cdo-tpl__z .mod.flush {
  margin-bottom: 0;
}

.cdo-tpl__z .mod.semi-flush {
  margin-bottom: 5px;
}

.cdo-tpl-basic {
  margin-top: 15px;
  margin-bottom: 30px;
}

.cdo-tpl-basic>.cdo-tpl__z {
  margin-top: 15px;
}

.cdo-tpl-main {
  margin-top: 15px;
  margin-bottom: 30px;
}

.cdo-tpl-main__z1 {
  display: none;
}

.cdo-tpl-main__z3 {
  float: none;
  margin: 0 auto;
  width: 100%;
}

.cdo-tpl-main__z3 .am--medrect {
  margin-left: auto;
  margin-right: auto;
}

.cdo-tpl-main__z3 .am {
  margin-bottom: 20px;
}

@media screen and (max-width:761px) {
  .cdo-tpl-main__z2 {
    margin-bottom: 0;
  }
}

@media screen and (min-width:762px) {
  .cdo-tpl-main__zwA>.cdo-tpl__z,.cdo-tpl-main__zwA .imageQuiz {
    margin-top: 15px;
  }

  .cdo-tpl-main__z2 {
    float: left;
    width: 408px;
  }

  .cdo-tpl-main__z2 .mod {
    margin-bottom: 30px;
  }

  .cdo-tpl-main__z2 .mod.flush {
    margin-bottom: 0;
  }

  .cdo-tpl-main__z2 .mod.tight {
    margin-bottom: 5px;
  }

  .cdo-tpl-main__z3 {
    float: right;
    width: 300px;
  }
}

@media screen and (min-width:960px) {
  .cdo-tpl-main__z2 {
    width: 580px;
  }
}

@media screen and (min-width:1080px) {
  .cdo-tpl-main__z2 {
    width: 704px;
  }
}

@media screen and (min-width:1280px) {
  .cdo-tpl-main__z1 {
    display: block;
    float: left;
    width: 160px;
  }

  .cdo-tpl-main__zwA {
    float: left;
    width: 1080px;
    padding-left: 20px;
  }

  .cdo-tpl-main__z2 {
    width: 745px;
  }
}

@media screen and (min-width:1380px) {
  .cdo-tpl-main__zwA {
    width: 1180px;
  }

  .cdo-tpl-main__z2 {
    width: 845px;
  }
}

.cdo-tpl-home {
  margin: 15px 0 30px;
}

.cdo-tpl-home>.cdo-tpl__z {
  margin-top: 15px;
}

.cdo-tpl-alt {
  margin-bottom: 30px;
  margin-top: 15px;
}

.cdo-tpl-alt__z2 {
  margin-top: 15px;
}

.cdo-tpl-alt__z2 .am--medrect {
  margin-left: auto;
  margin-right: auto;
}

.cdo-tpl-alt__z2 .am {
  margin-bottom: 20px;
}

@media screen and (min-width:762px) {
  .cdo-tpl-alt__z1 {
    float: left;
    width: 408px;
    margin-top: 15px;
  }

  .cdo-tpl-alt__z2 {
    float: right;
    width: 300px;
  }
}

@media screen and (min-width:960px) {
  .cdo-tpl-alt__z1 {
    width: 580px;
  }
}

@media screen and (min-width:1080px) {
  .cdo-tpl-alt__z1 {
    width: 704px;
  }
}

@media screen and (min-width:1280px) {
  .cdo-tpl-alt__z1 {
    float: left;
    width: 905px;
  }

  .cdo-tpl-alt__z2--retract {
    position: relative;
    margin-top: -262px;
  }
}

@media screen and (min-width:1380px) {
  .cdo-tpl-alt__z1 {
    width: 1005px;
  }
}

@media screen and (max-width:530px) {
  .cdo-tpl-alt__z2>.cols>.cols__col,.cdo-tpl-main__z3>.cols>.cols__col {
    width: 100%;
    margin-left: 0;
  }
}

@media screen and (min-width:762px) {
  .cdo-tpl-alt__z2>.cols>.cols__col,.cdo-tpl-main__z3>.cols>.cols__col {
    width: 100%;
    margin-left: 0;
  }
}

@media screen and (min-width:762px) and (max-width:959px) {
  .cdo-tpl-alt__z2>.cols--third .cols__col,.cdo-tpl-main__z2 .cols--third .cols__col {
    margin-left: 0;
    width: 100%;
  }
}

.mod {
  margin: 0 0 20px;
  border-radius: 3px;
  box-sizing: content-box;
}

.mod p:last-child {
  margin-bottom: 2px;
}

.mod p.flush:last-child {
  margin-bottom: 0;
}

.mod .btn {
  margin-right: 5px;
}

.mod .f-right .btn {
  margin-right: 0;
}

.mod>img {
  width: 100%;
}

.mod .alt {
  color: #1d4ea6;
}

.mod h2,.mod .h2,.mod h3,.mod .h3,.mod h4,.mod .h4 {
  font-weight: normal;
}

.mod h3,.mod .h3 {
  font-size: 1.25em;
}

.mod .txt-block {
  clear: left;
}

.mod p.txt-block {
  line-height: 1.125em;
}

.mod--main h2,.mod--main .h2 {
  font-weight: 700;
}

.mod--flush {
  margin: 0;
}

.mod--border {
  border: solid 1px #e0e0e5;
}

.mod>.pad {
  padding: 15px 20px;
}

.mod>.pad-lrg {
  padding: 20px 30px;
}

.mod>.pad-vlrg {
  padding: 35px 20px;
}

.mod>.pad--tight-base {
  padding-bottom: 10px;
}

.mod>.pad--flush-base {
  padding-bottom: 0;
}

.mod>.pad--flush-l {
  padding-left: 0;
}

.mod>.pad--flush-r {
  padding-right: 0;
}

.mod--padl>.pad {
  padding-left: 70px;
}

.mod--padr>.pad {
  padding-right: 70px;
}

.mod--dark,.mod--dark a:not(.btn),.mod--dark a .fcdo,.mod--dark a.txt-block,.mod--dark .meta,.mod--dark h2,.mod--dark h3,.mod--dark h4,.mod--dark .h2,.mod--dark .h3,.mod--dark .h4 {
  color: #fff;
}

.mod--dark .alt {
  color: #ddd;
}

.mod--dark .dropdown a {
  color: #292929;
}

.mod--dark .dropdown a:hover {
  color: #e84427;
}

.mod--dark a.helper {
  color: #234b9a;
}

.mod--style1 {
  background: #d0a44c;
  color: #111;
}

.mod--style1 .bg-h:after,.mod--style1 .txt-block {
  background: #bb9445;
}

.mod--style1 a.txt-block,.mod--style1 .txt-block a {
  color: #111;
}

.mod--style1 .txt-block .circle-btn {
  background: #fff;
}

.mod--style1 .txt-block .circle-btn .fcdo {
  color: #bb9445;
}

.mod--style1 .alt {
  color: #fff;
}

.mod--style1 .progress__indicator {
  border-color: #e5ca85;
}

.mod--style1 .progress__indicator__done {
  background: #4f4733;
}

.mod--style1 .progress__label {
  color: #765d2d;
}

.mod--style1 .btn--impact {
  background: #fff;
  border-color: #fff;
  color: #292929;
}

.mod--style1 .btn--impact:hover {
  background: #f4f4f4;
}

.mod--style1 .btn--s13 {
  font-size: 13px;
}

.mod--style2 {
  background: #e84427;
  color: #fff;
}

.mod--style2 .alt {
  color: #f3bab3;
}

.mod--style2 .bg-h:after,.mod--style2 .txt-block {
  background: #b7371e;
}

.mod--style2 .txt-block .circle-btn,.mod--style2 .progress__indicator__done {
  background: #fff;
}

.mod--style2 .txt-block .circle-btn .fcdo {
  color: #b7371e;
}

.mod--style2 .progress__indicator {
  border-color: #9d2e1a;
}

.mod--style2 .progress__label {
  color: #8b2411;
}

.mod--style3 {
  background: #0096ab;
  color: #fff;
}

.mod--style3 .alt {
  color: #acd3db;
}

.mod--style3 .bg-h:after,.mod--style3 .txt-block {
  background: #007889;
}

.mod--style3 .txt-block .circle-btn,.mod--style3 .progress__indicator__done {
  background: #fff;
}

.mod--style3 .txt-block .circle-btn .fcdo {
  color: #007889;
}

.mod--style3 .progress__indicator {
  border-color: #1d386e;
}

.mod--style3 .progress__label {
  color: #fff;
}

.mod--style4 {
  background: #eff1f6;
}

.mod--style4 .bg-h:after,.mod--style4 .txt-block {
  background: #dfe1e6;
  color: #234b9a;
}

.mod--style4 .txt-block--alt {
  background: #2a4596;
  color: #fff;
}

.mod--style4 .txt-block--alt3 {
  background: #e84427;
  color: #fff;
}

.mod--style4 .txt-block .circle-btn {
  background: #234b9a;
}

.mod--style4 .txt-block .circle-btn .fcdo {
  color: #dfe1e6;
}

.mod--style5 {
  background: #234c9b;
}

.mod--style5 .bg-h:after,.mod--style5 .txt-block {
  background: #12326f;
}

.mod--style5 .txt-block .circle-btn {
  background: #fff;
}

.mod--style5 .txt-block .circle-btn .fcdo {
  color: #12326f;
}

.mod--style5 .progress__indicator {
  border-color: #1d386e;
}

.mod--style5 .progress__indicator__done {
  background: #bfcce9;
}

.mod--style5 .progress__label {
  color: #bfcce9;
}

.mod-quiz .txt-block>h3,.mod-quiz .txt-block>.h3 {
  padding-right: 120px;
}

.mod-quiz .txt-block p {
  padding-right: 60px;
}

.mod-quiz .txt-block h3 span,.mod-quiz .txt-block .h3 span {
  display: inline-block;
}

.mod-quiz .input-wrap {
  max-width: 320px;
}

@media screen and (max-width:599px) {
  .mod-quiz .btn,.mod-quiz .input-wrap {
    margin-bottom: 5px;
    border-radius: 2px;
  }
}

.mod-pronounce>a {
  overflow: hidden;
  padding-left: 65px;
  padding-right: 65px;
}

.mod-pronounce>a:before {
  content: "\f028";
  left: -11px;
  top: 30%;
  font-size: 65px;
  color: #886112;
}

.mod-pronounce>a:after {
  content: "\f061";
  right: 25px;
  top: 50%;
  margin-top: -11px;
  font-size: 20px;
}

.mod-pronounce.float-xl {
  float: none;
  padding-right: 0;
}

.mod-define>a:before {
  content: "\e903";
}

.mod-define-short>a {
  overflow: hidden;
  padding-left: 65px;
}

.mod-define-short>a:before {
  content: "\e903";
  left: -11px;
  top: 30%;
  font-size: 65px;
  color: #886112;
}

.mod-browser {
  height: 250px;
  font-weight: bold;
}

.mod-browser__title,.mod-browser .scroller {
  float: left;
  height: 100%;
  width: 25%;
}

.mod-browser .scroller {
  width: 75%;
}

.mod-translate__lang {
  display: inline-block;
  width: 100%;
}

.mod-translate__tool p {
  font-size: .8125em;
}

.mod-translate h3,.mod-translate .h3 {
  font-size: 1.2em;
}

.mod-translate .dropdown,.mod-translate .helper {
  float: left;
  width: 100%;
}

.mod-translate .dropdown {
  margin-right: 15px;
}

.mod-translate .dropdown .btn {
  width: 100%;
  background: #fff;
  color: #292929;
  text-align: left;
  font-size: .9em;
}

.mod-translate .helper {
  margin-bottom: 10px;
}

.mod-translate .btn-translate {
  margin-top: 2px;
}

@media screen and (min-width:1080px) {
  .mod-translate__lang {
    width: 65%;
  }

  .mod-translate__tool {
    position: relative;
    float: right;
    width: 35%;
    z-index: 2;
  }
}

@media screen and (min-width:1280px) {
  .mod-translate__lang {
    width: 72%;
  }

  .mod-translate__tool {
    width: 28%;
  }

  .mod-translate .dropdown {
    width: auto;
  }

  .mod-translate .helper {
    width: 280px;
    margin-top: 0;
  }

  .mod-translate .helper .point {
    top: 50%;
    left: -5px;
    margin-left: 0;
  }

  .mod-translate .dropdown .btn {
    width: 195px;
  }
}

.mod-bloglist .pad {
  overflow: hidden;
}

@media screen and (max-width:599px),screen and (min-width:762px) and (max-width:959px) {
  .mod-bloglist .img {
    float: left;
    width: 40%;
  }
}

.mod-mdq {
  border: solid 3px #e0e0e5;
  padding-bottom: 30px;
  position: relative;
}

.mod-mdq .pad {
  position: relative;
}

.mod-mdq:before {
  content: "";
  height: 104px;
  width: 236px;
  position: absolute;
  bottom: 0;
  left: 50%;
  margin-left: -118px;
  background: url(/ko/external/images/sprite1.png?version=4.0.94) no-repeat -483px -60px;
}

.mod-mdq .btn {
  margin: 0;
}

@media screen and (min-width:1280px) {
  .mod-mdq__topic {
    min-height: 80px;
  }
}

.mod-promobox {
  background: #eef1f5;
}

.mod-promobox .col {
  vertical-align: middle;
}

.mod-promobox .col.img {
  background: url(/ko/external/images/mobile-promo-cdoenar.png?version=4.0.94) no-repeat center;
  background-size: cover;
  width: 100%;
}

.mod-promobox .ar {
  text-align: right;
  direction: rtl;
  font-size: 1.4em;
}

.mod-promobox .badge {
  vertical-align: middle;
  text-align: center;
}

.mod-promobox .badge a {
  text-decoration: none;
}

.mod-promobox .badge-apple {
  height: 45px;
  margin: 10px;
}

.mod-promobox .badge-google {
  height: 66px;
}

@media screen and (max-width:959px) {
  .mod-promobox .col {
    display: block;
    width: 100%;
  }

  .mod-promobox .col.img {
    height: 300px;
  }
}

@media screen and (min-width:960px) {
  .mod-promobox .col.img {
    height: 360px;
  }
}

@media screen and (min-width:1280px) {
  .mod-promobox .col {
    display: inline-block;
    max-width: 50%;
  }

  .mod-promobox .col.img {
    height: 500px;
  }
}

.mod-browse .scroller {
  float: left;
  width: 100%;
  height: 300px;
  padding: 0 0 0 10px;
}

.mod-browse--tall .scroller {
  height: 400px;
}

.mod-browse .txt-block--alt {
  background: #11326f;
}

@media screen and (min-width:600px) and (max-width:761px),screen and (min-width:1080px) {
  .mod-browse--split .scroller {
    width: 50%;
  }
}

.stacks__stack {
  float: left;
  width: 100%;
  padding: 0 0 20px 0;
}

.stacks--sml .stacks__stack {
  padding-bottom: 10px;
}

.stacks__stack>div {
  position: relative;
}

.stacks__stack>*:last-child {
  margin-bottom: 0;
}

@media screen and (min-width:600px) {
  .stacks--landing {
    margin: 0 -10px;
  }

  .stacks--landing .stacks__stack {
    padding-left: 10px;
    padding-right: 10px;
  }

  .stacks--landing .stacks__stack--size2 {
    width: 50%;
  }
}

@media screen and (min-width:762px) {
  .stacks--landing .stacks__stack--size1 {
    width: 50%;
  }

  .stacks--landing .stacks__stack--size2 {
    width: 25%;
  }
}

.stacks--error {
  margin-top: 30px;
}

@media screen and (min-width:600px) {
  .stacks--error {
    margin-left: -10px;
    margin-right: -10px;
  }

  .stacks--error .stacks__stack {
    padding-left: 10px;
    padding-right: 10px;
  }

  .stacks--error .stacks__stack--size2 {
    width: 50%;
  }
}

@media screen and (min-width:762px) {
  .stacks--error .stacks__stack--size1 {
    width: 50%;
  }
}

@media screen and (min-width:762px) and (max-width:1079px) {
  .stacks--error .stacks__wrap {
    float: right;
    width: 50%;
  }

  .stacks--error .stacks__stack--size2 {
    width: 100%;
  }
}

@media screen and (min-width:1080px) {
  .stacks--error .stacks__stack--size2 {
    width: 25%;
  }
}

@media screen and (min-width:1280px) {
  .stacks--quiz {
    margin: 0 -10px 5px;
  }

  .stacks--quiz .stacks__stack {
    width: 33.3333333%;
    padding: 0 10px;
  }
}

.stacks--def-cols2 .stacks__stack {
  padding-bottom: 10px;
}

@media screen and (min-width:600px) and (max-width:761px),screen and (min-width:1080px) {
  .stacks--def-cols2 {
    margin: 0 -5px;
  }

  .stacks--def-cols2 .stacks__stack {
    width: 50%;
    padding: 0 5px 10px 5px;
  }

  .stacks--def-cols2 .stacks__stack:nth-child(2n+1) {
    clear: both;
  }
}

@media screen and (min-width:600px) and (max-width:761px),screen and (min-width:960px) {
  .stacks--def-cols3 {
    margin: 0 -10px;
  }

  .stacks--def-cols3 .stacks__stack {
    width: 50%;
    padding-left: 5px;
    padding-right: 5px;
  }

  .stacks--def-cols3 .stacks__stack:nth-child(2n+1) {
    clear: both;
  }
}

@media screen and (min-width:1280px) {
  .stacks--def-cols3 {
    margin: 0 -10px 5px;
  }

  .stacks--def-cols3 .stacks__stack {
    clear: none;
    width: 33.3333333%;
  }

  .stacks--def-cols3 .stacks__stack:nth-child(2n+1) {
    clear: none;
  }

  .stacks--def-cols3 .stacks__stack:nth-child(3n+1) {
    clear: both;
  }
}

#ad_btmslot_a {
  text-align: center;
  margin-bottom: 20px;
}

.mod-browsepage #ad_btmslot_a {
  text-align: left;
  margin-bottom: 0;
}

#ad_houseslot_a,#ad_houseslot_b {
  width: 300px;
  height: 250px;
  margin: 0 auto 20px auto;
}

#ad_rightslot {
  text-align: center;
  margin-bottom: 20px;
}

#ad_rightslot.am-default,#ad_rightslot.am-testads {
  width: 300px;
  height: 250px;
}

#ad_topslot_a {
  width: 320px;
  height: 50px;
}

#ad_topslot_a.am-default,#ad_topslot_a.am-testads {
  margin: 5px auto 0 auto;
}

#ad_topslot_a.am-home {
  margin: 0 auto;
}

#ad_topslot_b {
  width: 728px;
  height: 90px;
}

#ad_topslot_b.am-home {
  margin: 0 auto;
}

.contentslot {
  width: 100%;
  min-width: 320px;
  display: table;
  margin: 5px auto 20px auto;
  text-align: center;
}

.pad-indent .contentslot {
  margin: 0 0 0 -30px;
}

@media screen and (max-width:370px) {
  .contentslot {
    margin: 0 0 20px -13px;
    text-align: center;
  }
}

@media screen and (max-width:332px) {
  #ad_btmslot_a {
    margin-left: -10px;
  }

  .contentslot {
    margin: 0 0 20px -26px;
    text-align: center;
  }

  .cpegs .egs .contentslot {
    margin: 0 0 20px -11px;
    text-align: center;
  }

  .entry-body .runon-body.pad-indent .contentslot {
    margin: 0 0 0 -53px;
  }

  .entry-body .runon-body:before {
    z-index: -1;
  }
}

@media screen and (max-width:761px) {
  #ad_btmslot_b.am-home {
    text-align: center;
  }

  #ad_topslot_b {
    display: none;
  }
}

@media screen and (min-width:762px) {
  #ad_topslot_a {
    display: none;
  }
}

@media screen and (min-width:762px) and (max-width:959px) {
  #ad_btmslot_a.am-home {
    float: right;
  }
}

@media screen and (min-width:960px) and (max-width:1079px) {
  #ad_btmslot_a.am-home {
    float: right;
  }
}

@media screen and (min-width:600px) {
  .ad-row--medrect3 .ad-row__ad {
    float: right;
  }

  .ad-row--medrect3 .ad-row__ad--alt {
    display: block;
  }

  .ad-row--medrect3 .ad-row__item {
    float: left;
    width: 50%;
  }

  .ad-row--medrect3 .ad-row__item[data-itemno="1"] {
    padding-right: 10px;
  }

  .ad-row--medrect3 .ad-row__item[data-itemno="2"] {
    padding-left: 10px;
  }
}

@media screen and (min-width:600px) and (max-width:1079px) {
  .ad-row--medrect3 .ad-row__ad--def {
    display: none;
  }

  .ad-row--medrect3 .ad-row__item[data-itemno="3"] {
    float: none;
    clear: left;
    width: auto;
    padding: 0;
    margin-right: 320px;
  }
}

@media screen and (min-width:960px) and (max-width:1079px) {
  .ad-row--medrect3 .ad-row__item[data-itemno="3"] .mod>img {
    float: left;
    width: 40%;
  }

  .ad-row--medrect3 .ad-row__item[data-itemno="3"] .mod>.pad {
    overflow: hidden;
  }
}

@media screen and (min-width:1080px) {
  .ad-row--medrect3 .ad-row__ad--alt {
    display: none;
  }

  .ad-row--medrect3 .ad-row__sibling {
    margin-right: 320px;
  }

  .ad-row--medrect3 .ad-row__item {
    width: 33.333333%;
  }

  .ad-row--medrect3 .ad-row__item[data-itemno="2"] {
    padding-right: 10px;
  }

  .ad-row--medrect3 .ad-row__item[data-itemno="3"] {
    padding-left: 10px;
  }
}

.ad-row {
  margin: 20px 0;
}

.ad-row--flush {
  margin: 0;
}

.ad-row__ad--alt {
  display: none;
  clear: both;
}

@media screen and (max-width:599px) {
  .ad-row__ad {
    clear: both;
  }
}

#cmp-container-id {
  z-index: 100000000!important;
  top: auto!important;
  height: 0;
}

#cmp-container-id>iframe {
  bottom: 5px;
  left: 50%;
  height: 120px;
  margin: auto!important;
  width: 100%;
  max-width: 980px;
  -webkit-transform: translateX(-50%);
  -ms-transform: translateX(-50%);
  transform: translateX(-50%);
}

.qc-cmp-persistent-link {
  display: none!important;
}

.qc-cmp-main-messaging {
  text-align: justify;
}

.qc-cmp-ui>.qc-cmp-publisher-logo {
  display: none;
}

.qc-cmp-ui-content>.qc-cmp-title {
  font-size: 24px;
  line-height: normal;
}

.qc-cmp-ui.qc-cmp-showing,.qc-cmp-ui-container.qc-cmp-showing,.qc-cmp-ui-content {
  overflow-y: hidden!important;
}

table.qc-cmp-table td {
  background-color: transparent;
}

.qc-cmp-sub-title,.qc-cmp-bold-messaging {
  color: #FFF;
  font-weight: bold;
}

ul.accord>li {
  margin: 0;
}

ul.accord>li>a {
  position: relative;
  display: block;
  padding: 12px 20px 12px 40px;
  background: #11326f;
  border-bottom: solid 1px #fff;
  color: #fff;
  text-decoration: none;
}

ul.accord>li>a:before {
  position: absolute;
  content: "+";
  top: 50%;
  margin-top: -12px;
  left: 20px;
  font-size: 140%;
  color: #fa6043;
}

ul.accord>li>a:hover {
  background: #183d81;
}

ul.accord>li>a em {
  font-size: 1.1em;
}

ul.accord>li.changing>a {
  border-width: 0;
}

ul.accord>li.open>a {
  background: #234b9a;
  color: #fff;
  border-width: 0;
}

ul.accord>li.open>a:before {
  content: "\2013";
  margin-top: -14px;
}

ul.accord>li.open>ul {
  display: block;
}

ul.accord>li>ul {
  display: none;
  margin: 0;
  padding: 4px 0;
  border: solid 1px #e0e0e5;
}

ul.accord>li>ul li {
  margin: 0 20px;
}

ul.accord>li>ul li a {
  display: block;
  padding: 8px 0;
  border-bottom: solid 1px #e0e0e5;
  color: #234b9a;
  font-weight: bold;
  text-decoration: none;
}

ul.accord>li>ul li a:hover span:first-child {
  text-decoration: underline;
}

ul.accord>li>ul li a span.alt {
  margin-left: 5px;
  color: #292929;
  text-transform: uppercase;
  font-size: .8em;
}

ul.accord>li>ul li a span.alt span {
  vertical-align: middle;
}

ul.accord>li>ul li:last-child a {
  border-width: 0;
}

.accord-basic {
  position: relative;
  cursor: pointer;
  padding: 5px 5px 5px 30px;
  background: #bfcce9;
  color: #111;
}

.accord-basic:before {
  position: absolute;
  content: "+";
  top: 50%;
  margin-top: -12px;
  left: 10px;
  font-size: 140%;
  color: #e84427;
}

.accord-basic.open:before {
  content: "\2013";
  margin-top: -14px;
}

.accord-basic--alt {
  background: #dfe1e6;
  padding-left: 30px;
  margin-bottom: 5px;
}

.accord-basic--alt.open {
  background: #244b9a;
  color: #fff;
}

.accord-basic--alt.open:before {
  color: inherit;
}

.accord-basic--shallow {
  line-height: 1.125em;
}

.accord-basic--shallow:before {
  margin-top: -10px;
}

.accord-basic--shallow.open:before {
  margin-top: -12px;
}

.accord-basic.bigger {
  padding-top: 13px;
  padding-bottom: 13px;
  line-height: 1.125em;
}

.accord-basic.bigger:before {
  left: 15px;
  margin-top: -10px;
}

.accord-basic.bigger.open:before {
  margin-top: -12px;
}

.accord-basic--alt.bigger {
  padding-left: 40px;
}

.accord-moreless {
  display: block;
  position: relative;
  padding: 25px 0 0;
  text-align: center;
  color: #6b6b6b;
  background: #fff;
  font-size: .85em;
}

.accord-moreless:before {
  content: " ";
  top: 10px;
  left: 0;
  height: 2px;
  width: 100%;
  background: #eef1f6;
}

.accord-moreless:before,.accord-moreless:after {
  margin-top: 0;
}

.accord-moreless.open:before {
  content: " ";
  margin: 0;
}

.accord-moreless:after {
  content: "\F107";
  position: absolute;
  top: -2.5px;
  left: 50%;
  width: 27px;
  height: 27px;
  line-height: 27px;
  margin-left: -13.5px;
  background: #e8e6f1;
  color: #e84427;
  font-size: 1.8em;
  -webkit-border-radius: 50%;
  -moz-border-radius: 50%;
  border-radius: 50%;
}

.accord-moreless.open:after {
  content: "\F106";
  line-height: 24px;
}

.share {
  float: right;
  margin-top: -10px;
  text-align: right;
}

.share p {
  padding: 0 5px;
  font-size: .85em;
}

.share a {
  margin-bottom: 5px;
  width: 33px;
  height: 33px;
  line-height: 30px;
}

.share a .fcdo {
  line-height: 100%;
  color: #fff;
}

.share *:last-child {
  margin-bottom: 0;
}

.share .circle {
  display: none;
}

.share .circle.circle-btn,.share .bg--fb,.share .bg--tw,.share .bg--more {
  display: inline-block;
}

.entry-body .share {
  float: none;
  width: 55px;
  margin: 0;
  padding: 15px 0;
  border: solid 1px #eaeaef;
  background: #fff;
  text-align: center;
}

.entry-body .share .point {
  display: none;
  left: -5px;
  top: 20px;
  border-left: solid 1px #eaeaef;
  border-bottom: solid 1px #eaeaef;
}

@media screen and (min-width:762px) {
  .share .circle {
    display: inline-block;
  }

  .share .bg--more {
    display: none;
  }
}

.cdo-promo {
  float: left;
  width: 100%;
  border-top: solid 1px #e5e4e9;
}

.cdo-promo .cols {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}

.cdo-promo .cols__col {
  position: relative;
  padding: 20px 0;
  border-bottom: solid 1px #e5e4e9;
}

.cdo-promo .cols__col:last-child {
  border-bottom-width: 0;
}

.cdo-promo h4,.cdo-promo .h4 {
  margin-bottom: 5px;
  font-size: 1.125em;
}

.cdo-promo a:hover h4,.cdo-promo a:hover .h4 {
  color: #d0a44c;
}

.cdo-promo p {
  font-size: .85em;
}

.cdo-promo a {
  display: block;
  text-decoration: none;
  color: #292929;
}

.cdo-promo .spr-b a {
  padding-left: 120px;
}

.cdo-promo .spr-b:before {
  top: 20px;
}

.cdo-promo .spr--promo-apps:before {
  left: 20px;
}

@media screen and (min-width:600px) {
  .cdo-promo .cols__col {
    width: 33.333333%;
    margin: 20px 0;
    padding: 0 30px;
    border-bottom-width: 0;
    border-right: solid 1px #e5e4e9;
  }

  .cdo-promo .cols__col:first-child {
    padding-left: 0;
    padding-right: 30px;
  }

  .cdo-promo .cols__col:last-child {
    padding-left: 30px;
    padding-right: 0;
    border-right-width: 0;
  }

  .cdo-promo .spr-b:before {
    top: 0;
  }

  .cdo-promo .spr--promo-widget:before {
    left: 15px;
  }

  .cdo-promo .spr--promo-apps:before {
    left: 60px;
  }
}

@media screen and (min-width:960px) {
  .cdo-promo .cols__col {
    margin: 30px 0;
  }

  .cdo-promo .spr--promo-widget:before {
    left: 28px;
  }
}

@media screen and (min-width:600px) and (max-width:761px) {
  .cdo-promo .spr-b a {
    padding: 65px 0 0 0;
  }

  .cdo-promo .spr--promo-apps:before {
    left: 30px;
  }
}

.sect {
  margin: 15px 0;
  padding: 30px 0;
}

.sect--bg {
  padding: 15px 0 30px;
  background: #eef1f5;
}

.sect--border {
  border-top: solid 1px #e5e4e9;
}

.caro {
  position: relative;
}

.caro__mask {
  overflow: hidden;
  width: 100%;
}

.caro__holder {
  white-space: nowrap;
  width: 100%;
}

.caro__el {
  display: inline-block;
  white-space: normal;
  width: 48.5%;
  margin: 0 2.95% 0 0;
  text-align: center;
}

.caro__el:last-child {
  margin-right: 0;
}

.caro__el>* {
  display: block;
  background: #fff;
}

.caro__el__lbl {
  display: table;
  width: 100%;
  padding: 0 15px;
  font-size: 1.25em;
}

.caro__el__lbl>span {
  display: table-cell;
  vertical-align: middle;
  height: 76px;
}

.caro__nav {
  position: absolute;
  top: 50%;
  left: 13px;
  margin: -22.5px 0 0 -22.5px;
}

.caro__nav--next {
  left: auto;
  right: 13px;
  margin: -22.5px -22.5px 0 0;
}

.caro__nav,.circle-btn.caro__nav {
  display: none;
}

.caro__pages {
  display: block;
  margin: 20px 0 0;
  text-align: center;
}

.caro__pages a {
  display: inline-block;
  height: 9px;
  width: 9px;
  margin: 0 0 0 5px;
  background: #bec6d3;
}

.caro__pages a.on {
  background: #60748d;
}

@media screen and (min-width:600px) {
  .caro__el {
    width: 32.5%;
    margin-right: 1.3%;
  }

  .caro__el:last-child {
    margin-right: 0;
  }
}

@media screen and (min-width:960px) {
  .caro__el {
    width: 24%;
    margin-right: 1.35%;
  }

  .caro__el:last-child {
    margin-right: 0;
  }

  .caro__nav {
    left: 0;
  }

  .caro__nav--next {
    left: auto;
    right: 0;
  }
}

@media screen and (min-width:1280px) {
  .caro__el {
    width: 19%;
    margin-right: 1.25%;
  }

  .caro__el:last-child {
    margin-right: 0;
  }
}

.item-tag {
  position: relative;
}

.item-tag__tag {
  position: absolute;
  top: 0;
  right: 0;
  height: 100%;
  padding: inherit;
}

.item-tag__tag--left {
  right: auto;
  left: 0;
}

.item-tag__tag>* {
  display: block;
}

.scroller {
  position: relative;
  height: 300px;
}

.scroller__nav {
  display: none;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 4;
}

.scroller__nav--down {
  top: auto;
  bottom: 5px;
}

.scroller__nav .fcdo {
  color: #e84427;
}

.scroller__ind {
  position: relative;
  float: left;
  width: 25px;
  height: 100%;
  padding-right: 5px;
}

.scroller__ind__bar {
  display: none;
  position: absolute;
  top: 25px;
  left: 6px;
}

.scroller__ind__bar span {
  display: block;
  width: 3px;
  height: 1px;
  background: #e84427;
}

.scroller__content {
  position: relative;
  height: 100%;
  padding: 0 35px 0 0;
  overflow-y: scroll;
}

.scroller__content>* {
  margin-bottom: 0;
  padding-bottom: 15px;
}

.scroller__mask {
  position: absolute;
  top: 0;
  right: 0;
  height: 99.9%;
  width: 50px;
  background: #fff;
  z-index: 3;
}

.scroller--blur:before,.scroller--blur:after {
  content: " ";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 25px;
  z-index: 2;
}

.scroller--blur:after {
  top: auto;
  bottom: 0;
}

.scroller--blur .scroller__content {
  padding-top: 20px;
  z-index: 1;
}

.scroller--blur .scroller__nav {
  top: 20px;
}

.scroller--blur .scroller__nav--down {
  top: auto;
  bottom: 25px;
}

.scroller--blur .scroller__ind__bar {
  top: 45px;
}

.scroller--ind-r .scroller__ind__bar {
  top: 25px;
}

.scroller--ind-r .scroller__nav {
  left: auto;
  right: 20px;
}

.scroller--style1 {
  background: #234b9a;
  color: #fff;
}

.scroller--style1 a,.scroller--style1 a:hover {
  color: #fff;
}

.scroller--style1 a em {
  color: #f1f1f1;
}

.scroller--style1 a:hover {
  text-decoration: underline;
}

.scroller--style1 .scroller__mask {
  background: #234b9a;
}

.scroller--style1 .scroller__ind__bar {
  background: #7b93c2;
}

.scroller--style1 .scroller__ind__bar span {
  background: #fff;
}

.scroller--style1 .scroller__nav .fcdo {
  color: #fff;
}

.scroller--style2 {
  background: #eef1f5;
}

.scroller--style2 a em {
  color: #3b5998;
}

.scroller--style2 a:hover {
  text-decoration: underline;
}

.scroller--style2 .scroller__mask {
  background: #eef1f5;
}

.scroller--style2 .scroller__ind__bar {
  background: #b5bdcc;
}

.scroller--style2 .scroller__ind__bar span {
  background: #e84427;
}

.scroller--style2 .scroller__nav .fcdo {
  color: #96a3b5;
}

.tool__counter {
  position: absolute;
  bottom: 6px;
  left: 40px;
  padding: 7px 10px 5px;
  font-size: .75em;
}

.tool__msg-disabled {
  display: none;
  position: absolute;
  top: 1px;
  left: 1px;
  bottom: 1px;
  right: 1px;
  padding: 20px;
  font-weight: bold;
  color: #e84427;
  background: #fff;
}

.tool--disabled .btn,.tool--disabled .circle-btn {
  background: #ddd;
  border-color: #ddd;
  color: #777;
}

.tool--disabled .btn:before,.tool--disabled .btn:after {
  color: #777;
}

.tool--disabled .tool__counter {
  color: #555;
}

.tool--disabled .tool__msg-disabled {
  display: block;
}

.tabs__tabs ul {
  float: left;
  width: 100%;
  margin: 0;
  padding: 0;
  list-style: none;
  box-sizing: border-box;
}

.tabs__tabs li {
  float: left;
  margin: 0;
  text-align: center;
}

.tabs__tabs a {
  display: block;
  padding: 4px 15px;
  color: #8795ae;
  font-weight: bold;
  border-bottom: solid 3px #d5dae3;
  text-decoration: none;
  box-sizing: border-box;
  min-height: 55px;
}

.tabs__tabs a.on {
  color: #e84427;
  border-color: #e84427;
}

.tabs__content {
  display: none;
  float: left;
  width: 100%;
}

.tabs__content.on {
  display: block;
}

.tabs__content>.pad {
  padding: 10px 0;
}

.tabs__content>.block-wrap {
  padding: 10px 30px 30px;
}

.tabs--block .tabs__tabs ul {
  background: #2a4596;
  padding: 0 20px;
}

.tabs--block .tabs__tabs a {
  margin-right: 20px;
  padding: 5px 0;
  color: rgba(255,255,255,0.56);
  border-color: #2a4596;
}

.tabs--block .tabs__tabs a.on {
  color: #fff;
  border-color: #e84427;
}

.tabs--block .tabs__content>.pad {
  padding: 10px 20px;
}

ul[data-tabs-count="1"] li {
  width: 100%;
}

ul[data-tabs-count="2"] li {
  width: 50%;
}

ul[data-tabs-count="3"] li {
  width: 33.3333333%;
}

ul[data-tabs-count="4"] li {
  width: 25%;
}

ul[data-tabs-count="5"] li {
  width: 20%;
}

ul[data-tabs-count="6"] li {
  width: 16.666667%;
}

ul[data-tabs-count="7"] li {
  width: 14.285714%;
}

div[id*='dataset-']:before {
  display: block;
  clear: both;
  content: "";
}

@media screen and (min-width:450px) {
  .tabs__tabs a {
    min-height: 0;
  }
}

.translate-tool {
  position: relative;
}

.translate-tool .dropdown {
  width: 100%;
}

.translate-tool .dropdown__box {
  white-space: nowrap;
  min-width: 0;
  max-width: none;
  z-index: 5;
}

.translate-tool__switch,.translate-tool__from,.translate-tool__to {
  float: left;
  width: 100%;
}

.translate-tool__switch {
  width: 35px;
}

.translate-tool__from__keyboard-trig {
  position: absolute;
  bottom: 1px;
  left: 1px;
  width: 55px;
  height: 32px;
  background: #fff;
  color: #234b9a;
  border-width: 0;
  cursor: pointer;
}

.translate-tool__from__keyboard-trig:after {
  right: auto;
  left: 20px;
  margin-top: -12px;
}

.translate-tool__select-trig {
  position: relative;
  width: 100%;
  text-align: left;
}

.translate-tool__select-trig:after {
  color: #fff;
  font-size: 14px;
}

.translate-tool__select {
  visibility: hidden;
  width: 100%;
}

.translate-tool__from__input {
  width: 100%;
  height: 80px;
  padding: 15px 20px;
  margin: 0;
  vertical-align: bottom;
  font-size: 1.25em;
  background: #fff;
  color: #777;
  border-color: #ddd;
  vertical-align: bottom;
}

.translate-tool__clear {
  display: none;
  position: absolute;
  top: 10px;
  right: 10px;
}

.translate-tool__button-translate {
  margin: 5px 0 0;
}

.translate-tool__loader {
  display: none;
  margin: 15px 10px 14px 0;
}

.translate-tool__process {
  position: absolute;
  right: 5px;
  bottom: 5px;
}

.translate-tool__credit {
  position: absolute;
  right: 10px;
  bottom: 5px;
  font-size: .8em;
  text-decoration: none;
  border: none!important;
}

.translate-tool__output {
  position: relative;
  width: 100%;
  padding: 15px 20px 45px 15px;
  background: #bfcce9;
  font-size: 1.25em;
}

.translate-tool__output a {
  border-bottom: dashed 1px;
  text-decoration: none;
}

.translate-tool__output a:hover {
  border-bottom: solid 1px;
  text-decoration: none;
}

.translate-tool__result {
  width: 100%;
}

.translate-tool__copy {
  position: absolute;
  bottom: 10px;
  left: 20px;
  color: rgba(34,34,34,0.70);
  font-size: .8125em;
  cursor: pointer;
}

.translate-tool__copy:hover {
  color: #222;
}

.translate-tool__copy .fcdo {
  margin-right: 3px;
  color: #234b9a;
  font-size: 1.2308em;
}

.translate-tool__word-list a {
  display: block;
  text-decoration: none;
  padding: 10px 0 10px 30px;
  color: inherit;
  line-height: 1.5em;
  border-bottom: solid 1px #aaa;
  position: relative;
  font-size: 1.25em;
}

.translate-tool__word-list a:before {
  content: '\f054';
  font-family: cdoicons;
  position: absolute;
  left: 0;
  color: #95acda;
}

.translate-tool__word-list a .tlabel {
  color: #234b9a;
  font-weight: bold;
}

.translate-tool__word-list .pos {
  font-style: italic;
  color: #292929;
  font-weight: normal;
}

.translate-tool .virtualKeyboard {
  position: absolute;
  top: 248px;
  left: 0;
  width: 100%;
  z-index: 1000;
}

.mod .translate-tool__button-translate {
  margin-right: 0;
}

.translate-tool__header {
  background: #234b9a;
  text-align: center;
}

.translate-tool__header .dropdown {
  display: inline-block;
  width: auto;
}

.translate-tool__header .translate-tool__select {
  width: auto;
}

.translate-tool__header .js-translator-switchds {
  color: #fff;
  text-decoration: none;
  padding: 10px;
}

.translate-tool--disabled .translate-tool__from__keyboard-trig {
  color: #777;
}

.translate-tool--disabled .translate-tool__result,.translate-tool--disabled .translate-tool__output {
  background: #eee;
  color: #eee;
}

.translate-tool--disabled .translate-tool__copy,.translate-tool--disabled .translate-tool__credit,.translate-tool--disabled .translate-tool__from__keyboard-trig {
  display: none;
}

.translate-tool--disabled .translate-tool__button-translate,.translate-tool--disabled .circle-btn,.translate-tool--disabled .btn--dropdown {
  background: #ddd;
  border-color: #ddd;
  color: #787878;
}

.translate-tool--disabled .translate-tool__select-trig:after {
  color: #787878;
}

.translate-tool--disabled .tool__msg-disabled {
  display: block;
}

.translate-tool--disabled__btn,.translate-tool--disabled__btn:hover {
  background-color: #999;
  border-color: #999;
  color: #111;
  cursor: not-allowed;
}

@media screen and (min-width:600px) and (max-width:761px),screen and (min-width:960px) {
  .translate-tool .dropdown__box {
    width: auto;
  }

  .translate-tool__select-trig {
    padding-right: 45px;
  }

  .translate-tool .dropdown {
    width: auto;
  }

  .translate-tool__from,.translate-tool__to {
    width: 44%;
  }

  .translate-tool__switch {
    width: 12%;
    margin: 40px 0 0;
    text-align: center;
  }

  .translate-tool__button-switch {
    margin-top: 60px;
  }

  .translate-tool__output {
    height: 150px;
    padding: 15px 20px;
  }

  .translator_layout .translate-tool__from__input {
    height: 119px;
  }

  .translator_layout .with-el {
    border: 1px solid #ddd!important;
  }

  .translate-tool__result {
    height: 100px;
  }
}

@media screen and (min-width:1080px) {
  .translate-tool__from,.translate-tool__to {
    width: 47%;
  }

  .translate-tool__switch {
    width: 6%;
  }
}

@media screen and (max-width:960px) {
  .recaptcha-container {
    margin-left: 10px;
  }
}

.grecaptcha-badge {
  visibility: hidden;
}

.word-list {
  margin-left: 0;
  list-style: none;
}

.word-list .fcdo {
  font-size: 1.3em;
}

.word-list .circle .fcdo {
  font-size: .875em;
}

.word-list .fcdo-quiz {
  font-size: 1.8em;
}

.word-list__row,.wordlist-create-your-own {
  border: 3px solid #eff1f6;
  border-left-width: 4px;
  padding: 12px 20px 12px 44px;
  margin-bottom: 8px;
  position: relative;
}

.word-list__row--no-tag {
  padding-left: 20px;
}

.word-list__row:before {
  content: "";
  position: absolute;
  top: 0;
  left: 12px;
  margin-top: 14px;
  height: 22px;
  width: 22px;
}

.word-list__row>p {
  padding-top: 3px;
}

.word-list__row__type {
  color: #777;
  font-size: .875em;
}

.word-list__row__controllers {
  float: right;
  margin-left: 10px;
}

.word-list__row__controllers-base {
  margin-top: 5px;
}

.word-list__row__controllers a {
  padding-left: 20px;
}

.word-list__row__controllers-base a {
  padding-right: 15px;
}

.word-list__row__controllers-icon-btn {
  vertical-align: -3px;
}

.word-list__row__controllers-icon-btn .circle {
  vertical-align: 3px;
}

.word-list__row .region {
  text-transform: uppercase;
  color: #e84427;
  font-size: 1em;
  font-weight: bold;
}

.word-list__row .trans {
  display: block;
  margin: 5px 0;
  line-height: 1.3em;
  color: #556ba4;
  font-style: normal;
  font-weight: bold;
}

.word-list__row .pos {
  font-weight: normal;
  font-style: italic;
  color: #222;
}

.word-list--mydictionary .word-list__row {
  border-left-color: #234b9a;
}

.word-list--mydictionary .word-list__row:before {
  background: url(/ko/external/images/sprite1.png?version=4.0.94) -593px -31px no-repeat;
}

.word-list--cambridge .word-list__row {
  border-left-color: #d0a44c;
}

.word-list--cambridge .word-list__row:before {
  background: url(/ko/external/images/sprite1.png?version=4.0.94) -630px -31px no-repeat;
}

.word-list--community .word-list__row {
  border-left-color: #e84427;
}

.word-list--community .word-list__row:before {
  background: url(/ko/external/images/sprite1.png?version=4.0.94) -667px -31px no-repeat;
}

.wordlist-create-your-own {
  padding: 5px 10px;
  margin: 0 0 20px;
}

@media screen and (min-width:450px) {
  .word-list__row__type {
    float: left;
    width: 150px;
  }

  .word-list__row__details {
    margin-left: 150px;
  }
}

@media screen and (min-width:762px) {
  .word-list__row {
    padding-left: 52px;
  }

  .word-list__row:before {
    height: 28px;
    width: 28px;
  }

  .word-list__row--no-tag {
    padding-left: 20px;
  }

  .word-list--mydictionary .word-list__row:before {
    background-position: -593px 0;
  }

  .word-list--cambridge .word-list__row:before {
    background-position: -630px 0;
  }

  .word-list--community .word-list__row:before {
    background-position: -667px 0;
  }
}

@media screen and (min-width:960px) {
  .word-list--fixed .word-list__row__controllers {
    width: 200px;
    text-align: right;
  }

  .word-list--fixed .word-list__row__details {
    margin-right: 200px;
  }
}

.rounded-bef:before,.rounded-aft:after,.rounded {
  border-radius: 3px;
}

.round-top-bef:before,.round-top-aft:after,.round-top {
  border-radius: 3px 3px 0 0;
}

.round-base-bef:before,.round-base-aft:after,.round-base {
  border-radius: 0 0 3px 3px;
}

.round-left-bef:before,.round-left-aft:after,.round-left {
  border-radius: 3px 0 0 3px;
}

.round-right-bef:before,.round-right-aft:after,.round-right {
  border-radius: 0 3px 3px 0;
}

.round-tl-bef:before,.round-tl-aft:after,.round-tl {
  border-radius: 3px 0 0 0;
}

.round-tr-bef:before,.round-tr-aft:after,.round-tr {
  border-radius: 0 3px 0 0;
}

.round-br-bef:before,.round-br-aft:after,.round-br {
  border-radius: 0 0 3px 0;
}

.round-bl-bef:before,.round-bl-aft:after,.round-bl {
  border-radius: 0 0 0 3px;
}

.shadow {
  box-shadow: 0 0 4px #aaa;
}

.shadow-dark {
  box-shadow: 0 0 4px #222;
}

.shadow-inside {
  box-shadow: inset 0 -7px 9px -7px rgba(0,0,0,0.8);
}

.shadow-inside-light {
  box-shadow: inset 0 -7px 9px -7px rgba(0,0,0,0.4);
}

.shadow-none {
  box-shadow: none;
}

.circle {
  border-radius: 50%;
  text-align: center;
}

.circle-btn {
  display: inline-block;
  width: 30px;
  height: 30px;
  background: #e84427;
  color: #fff!important;
  border-width: 0;
}

.circle-btn--sml {
  width: 22px;
  height: 22px;
  line-height: 20px;
  font-size: .8em;
}

.circle-btn--big {
  width: 45px;
  height: 45px;
  line-height: 43px;
}

.circle-btn--alt {
  background: #c1943b;
}

.circle-btn .fcdo {
  color: inherit;
  vertical-align: initial;
  line-height: 30px;
}

.circle-btn--sml .fcdo {
  color: inherit;
  vertical-align: initial;
  line-height: 22px;
}

.center-y {
  position: relative;
  top: 50%;
  -webkit-transform: translateY(-50%);
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
}

.grad-trans,.grad-trans-pseudo:before {
  background: -webkit-linear-gradient(top,rgba(255,255,255,1),rgba(255,255,255,0));
  background: -o-linear-gradient(bottom,rgba(255,255,255,1),rgba(255,255,255,0));
  background: -moz-linear-gradient(bottom,rgba(255,255,255,1),rgba(255,255,255,0));
  background: linear-gradient(to bottom,rgba(255,255,255,1),rgba(255,255,255,0));
}

.grad-trans--bottom,.grad-trans-pseudo:after {
  background: -webkit-linear-gradient(top,rgba(255,255,255,0),rgba(255,255,255,1));
  background: -o-linear-gradient(bottom,rgba(255,255,255,0),rgba(255,255,255,1));
  background: -moz-linear-gradient(bottom,rgba(255,255,255,0),rgba(255,255,255,1));
  background: linear-gradient(to bottom,rgba(255,255,255,0),rgba(255,255,255,1));
}

.grad-trans2-pseudo:before {
  background: -webkit-linear-gradient(top,rgba(35,75,154,1),rgba(35,75,154,0));
  background: -o-linear-gradient(bottom,rgba(35,75,154,1),rgba(35,75,154,0));
  background: -moz-linear-gradient(bottom,rgba(35,75,154,1),rgba(35,75,154,0));
  background: linear-gradient(to bottom,rgba(35,75,154,1),rgba(35,75,154,0));
}

.grad-trans2-pseudo:after {
  color: rgba(35,75,154,0.00);
  background: -webkit-linear-gradient(top,rgba(35,75,154,0),rgba(35,75,154,1));
  background: -o-linear-gradient(bottom,rgba(35,75,154,0),rgba(35,75,154,1));
  background: -moz-linear-gradient(bottom,rgba(35,75,154,0),rgba(35,75,154,1));
  background: linear-gradient(to bottom,rgba(35,75,154,0),rgba(35,75,154,1));
}

.grad-trans3-pseudo:before {
  background: -webkit-linear-gradient(top,rgba(238,241,245,1),rgba(238,241,245,0));
  background: -o-linear-gradient(bottom,rgba(238,241,245,1),rgba(238,241,245,0));
  background: -moz-linear-gradient(bottom,rgba(238,241,245,1),rgba(238,241,245,0));
  background: linear-gradient(to bottom,rgba(238,241,245,1),rgba(238,241,245,0));
}

.grad-trans3-pseudo:after {
  background: -webkit-linear-gradient(top,rgba(238,241,245,0),rgba(238,241,245,1));
  background: -o-linear-gradient(bottom,rgba(238,241,245,0),rgba(238,241,245,1));
  background: -moz-linear-gradient(bottom,rgba(238,241,245,0),rgba(238,241,245,1));
  background: linear-gradient(to bottom,rgba(238,241,245,0),rgba(238,241,245,1));
}

.error_layout .cdo-section-title-hw .headword,.error_layout .di-head.normal-entry .cdo-section-title-hw {
  font-size: 2em;
}

.error_layout .di-head {
  background: transparent;
  border-width: 0;
  padding: 0;
}

.error_layout .entry-body .pos-header,.error_layout .entry-body .pos-body,.error_layout .entry-body .normal-entry-body {
  padding-right: 0;
}

.error_layout .entry-body .pos-body .def-block,.error_layout .entry-body .normal-entry-body .def-block {
  padding-right: 30px;
}

.error_layout .cdo-section-title-hw .posgram:after,.error_layout .di-head.normal-entry .posgram:after,.error_layout .pos-head .pos-info .posgram:after {
  content: none;
}

.error_layout .cdo-section-title-hw .gram a,.error_layout .di-head .gram a,.error_layout .pos-head .gram a {
  margin-right: 10px;
  font-size: 1.125em;
  color: #555;
  text-decoration: none;
}

@media screen and (max-width:959px) {
  body.error_layout500 {
    padding-top: 45px;
  }

  body.error_layout500 .cdo-search {
    display: none;
  }

  body.error_layout500 .cdo-hdr__pre {
    height: 45px;
  }
}

@media screen and (min-width:600px) {
  .error_layout .entry-body .pos-body .def-block,.error_layout .entry-body .normal-entry-body .def-block {
    padding-right: 70px;
  }
}

.btnfeat {
  position: relative;
  display: inline-block;
  min-width: 120px;
  margin: 0 10px 10px 0;
  padding: 10px 15px 10px 60px;
  background: #333;
  color: #fff;
  text-decoration: none;
  font-size: .8125em;
  line-height: 1.1em;
  box-sizing: border-box;
}

.btnfeat:hover {
  background: #444;
}

.btnfeat span,.btnfeat em {
  display: block;
}

.btnfeat em {
  clear: both;
  font-size: 90%;
  color: #888;
  font-style: normal;
}

.btnfeat .point {
  display: none;
  top: 50%;
  left: 40px;
  margin-top: -5px;
}

.btnfeat .fcdo {
  position: absolute;
  top: 0;
  left: 0;
  width: 45px;
  height: 100%;
  padding-top: 15px;
  text-align: center;
  color: #fff;
  font-size: 1.5em;
  box-sizing: border-box;
}

.btnfeat i,.btnfeat .point {
  background: #234b9a;
}

.btnfeat--alt i,.btnfeat--alt .point {
  background: #d0a44c;
}

.btnfeat--alt2 i,.btnfeat--alt2 .point {
  background: #e84427;
}

.btnfeat--alt3 i,.btnfeat--alt3 .point {
  background: #0096ab;
}

.btnfeat--fb i,.btnfeat--fb .point {
  background: #3b5998;
}

.btnfeat--tw i,.btnfeat--tw .point {
  background: #55acee;
}

.btnfeat--gp i,.btnfeat--gp .point {
  background: #dc4e41;
}

.page-header {
  display: inline-block;
  width: 100%;
  padding-bottom: 8px;
}

@media screen and (max-width:761px) {
  .page-header {
    border-bottom: 1px solid #e6e6eb;
  }
}

.page-header .share {
  float: right;
  border: 0;
  width: auto;
  padding: 8px 0 0;
  position: inherit;
  text-align: right;
}

@media screen and (max-width:449px) {
  .di .page-header .share {
    width: auto;
    padding: 8px 0 0;
  }
}

#navigation-toc {
  display: none;
}

#navigation-toc.open {
  display: block;
}

#navigation-toc ul {
  margin: 0;
}

.nav-entry-toggle {
  font-size: 1.05em;
  min-width: 160px;
  max-width: 170px;
}

@media screen and (max-width:599px) {
  .nav-entry-toggle {
    font-size: 1em;
    min-width: 130px;
  }
}

#backtotop {
  padding: 6px;
  position: fixed;
  right: 0;
  display: none;
  bottom: 10px;
  margin: 0 20px 0 0;
  text-decoration: none;
  border: 0 none;
  background-color: #42454c;
  border-radius: 3px;
  box-shadow: inset 0 0 2px #ccc;
  box-shadow: 0 5px 10px rgba(0,0,0,0.2);
  cursor: pointer;
  z-index: 11000;
}

#backtotop .fcdo {
  color: #fff;
  font-size: 1.8em;
}

#backtotop:hover {
  background-color: #bacd43;
}

.cdo-hero--dataset {
  background-image: none;
  background-color: #292929;
}

.cdo-hero--dataset.mobile {
  background-position: bottom center;
}

.mod-browse .scroller a {
  font-weight: normal;
}

.cycler__items>*:first-child {
  width: auto;
  min-width: 20%;
}

.mod-quiz .incorrect {
  word-wrap: break-word;
}

.translate-tool--disabledTooMuch .translate-tool__button-translate,.translate-tool--disabledTooMuch .circle-btn {
  background: #ddd;
  border-color: #ddd;
  color: #787878;
}

.countToMuchText {
  font-weight: bold;
  color: #e84427;
}

.ico-bg--key--gen {
  position: absolute;
  height: 100%;
  width: 37px;
  right: 0;
  z-index: 5;
  background-color: transparent;
  border: 0;
}

.normal-entry .uk>.region,.normal-entry .us>.region {
  text-transform: uppercase;
  color: #e84427;
  font-size: 1em;
  font-weight: bold;
}

.audio_play_button {
  cursor: pointer;
}

.cols__col--product {
  position: relative;
}

.cols__col--product-img {
  height: 100px;
  margin: 0 0 15px;
  position: absolute;
  top: 0;
  left: 0;
}

.cols__col--product .cols__col--product-img {
  float: left;
  position: initial;
  margin-right: 1em;
}

.entry-body .pos-body .tabs .txt-block .pos,.entry-body .pos-body h4.txt-block .pos {
  font-size: 1em;
}

.section .smaller,ul.accord>li>ul li a span.alt {
  position: relative;
  top: -0.1em;
}

.entry-body .pos-header .gram,.sense-block .gram {
  position: relative;
  top: -2px;
}

.spr--ico-key-translation:before {
  background-position: -114px -239px;
  width: 47px;
  height: 47px;
}

.trends--egt .title {
  padding-bottom: 0;
  border-bottom: 0;
}

.circle.bg--more.open .fcdo-minus,.circle.bg--more .fcdo-plus,.share .bg--gp,.share .bg--di,.share .bg--tu,.share .bg--re,.share .bg--def,.translator_layout .share .circle,.share .bg--more {
  display: inline-block;
}

.bg--white {
  background: #fff;
}

.bg--def,.bg--more {
  background: #e84427;
}

.bg--di {
  background: #0091ff;
}

.bg--fb {
  background: #3b5998;
}

.bg--gp {
  background: #dc4e41;
}

.bg--re {
  background: #ff4500;
}

.bg--tu {
  background: #36465d;
}

.bg--tw {
  background: #55acee;
}

.helper {
  background: #bfcdea;
  padding: 20px;
  margin-top: 15px;
  color: #111;
  -webkit-border-radius: 3px;
  -moz-border-radius: 3px;
  border-radius: 3px;
  font-size: .875em;
}

.helper .point {
  display: none;
  background: #bfcdea;
  top: 0;
  left: 50%;
  margin: -5px 0 0 -5px;
}

a.helper {
  display: block;
  padding: 11px 30px 11px 20px;
  text-decoration: none;
  color: #234b9a;
  font-weight: bold;
  cursor: pointer;
}

a.helper p {
  overflow: hidden;
  margin: 0;
  white-space: nowrap;
  line-height: 1em;
  text-overflow: ellipsis;
}

a.helper:hover,a.helper:hover .point {
  background: #b2c0de;
}

.circle.bg--more .fcdo-minus,.circle.bg--more.open .fcdo-plus,.translator_layout .content2,.translator_layout .content1 {
  display: none;
}

.translator_layout .translate-tool .virtualKeyboard {
  z-index: 5;
}

.kernerman-copyright-img {
  height: 20px;
  margin-right: 5px;
}

.translator_layout .dropdown[data-selectbox-id='languageTo'] .dropdown__box {
  right: 0;
}

.translator_layout .cdo-tpl-alt {
  margin-top: 5px;
}

.translator_layout .with-el {
  border: solid 5px #234b9a;
  border-top: 0;
}

.translator_layout .translate-tool__from__input {
  border: 0;
  resize: none;
  margin-bottom: 30px;
  outline: 0;
}

.translator_layout .translate-tool__from__keyboard-trig {
  background: transparent;
}

.translator_layout .translate-tool__from__keyboard-trig {
  bottom: 0;
}

@media screen and (min-width:450px) {
  .translator_layout .content2,.translator_layout .content1 {
    display: inherit;
  }
}

.cdo-search__button,.cdo-search__dataset {
  float: right;
}

.cdo-hdr__blocks--home .cdo-search.cdo-search-centered {
  float: none;
  width: 100%;
}

.cdo-hdr__profile a.hdr-btn .fcdo {
  opacity: .85;
  color: #fff;
}

.cdo-hdr__profile a.hdr-btn:hover .fcdo,.cdo-hdr__profile a.hdr-btn.on .fcdo {
  opacity: 1;
  color: inherit;
}

.mod-browser .pos {
  color: gray;
  font-style: italic;
}

.sense-block .pos {
  color: rgba(255,255,255,0.8);
}

.sense-block .cdo-cloud-content .pos {
  color: inherit;
}

.dropdown--options .dropdown__box .btn {
  text-align: inherit;
  font-weight: inherit;
}

.dropdown--options .dropdown__box a {
  margin-bottom: 5px;
}

.entry-body a.query {
  text-decoration: none;
}

.modal-confirm {
  max-width: 400px;
  min-height: 0;
}

a {
  cursor: pointer;
}

.entry-body a.query {
  text-decoration: none;
}

.mod-quiz .incorrect {
  color: #F00;
}

.mod-quiz .correct {
  color: #2e8b57;
}

.mod-quiz .virtualKeyboard {
  margin-top: 1em;
}

.mod-quiz .fcdo {
  color: inherit;
  vertical-align: top;
  font-size: 1.33333333em;
  line-height: .75em;
}

.mod-quiz .circle .fcdo {
  vertical-align: middle;
  font-size: inherit;
  line-height: inherit;
}

.mod-quiz .back {
  background: #aeb9c9;
  padding: 13px 20px;
  display: block;
}

#informational-content .circle-btn--sml {
  line-height: 22px;
}

#informational-content .txt-block {
  padding: 11px 20px;
}

#informational-content .txt-block--alt4 {
  background: #bfcce9;
  padding: 5px 20px;
}

#informational-content pre.linktous {
  white-space: normal;
  word-break: break-word;
  overflow: hidden;
  background-color: #f0f0f0;
  font-size: 1.2em;
  padding: .5em;
  margin: .25em 1px;
}

#informational-content .fcdo-quiz {
  font-size: 1.8em;
  color: #234b9a;
}

.mod-quiz .questionary-resume-item {
  background: #eff1f6;
  padding: 10px 20px;
  margin-bottom: 1em;
}

.mod-quiz .questionary-resume {
  text-align: left;
}

.di.english-chinese-simplified .trans,.di.english-chinese-traditional .trans {
  font-weight: normal;
}

div.entry_title .results .pos {
  font-style: italic;
  font-size: 95%;
}

.mod-define>a:before {
  content: "\e903";
}

.pronunciation-english.entry-body__el {
  min-height: 0;
}

.pronunciation-english .pronunciation-item {
  margin-bottom: 10px;
}

.pronunciation-english .sound {
  display: inline-block;
  background: #e84427;
  color: #fff;
  border-radius: 3px;
  padding: 2px 10px 0;
  text-transform: uppercase;
  font-weight: bold;
  margin-right: 5px;
}

.pronunciation-english .sound .fcdo {
  font-size: 1.5em;
  display: inline-block;
  margin: 0 5px 3px 0;
}

.pronunciation-english .sound .fcdo:before {
  color: rgba(255,255,255,0.8);
  text-shadow: 1px 4px 8px #e84427,0 0 0 #fff,1px 4px 8px #e84427;
}

.pronVideos {
  max-width: 560px;
  margin: 0 auto 20px auto;
}

.pronVideo {
  width: 100%;
  height: 315px;
  margin-bottom: 10px;
}

@media screen and (min-width:1080px) and (max-width:1280px) {
  .pronVideos {
    max-width: 463px;
  }

  .pronVideo {
    height: 260px;
  }
}

@media screen and (min-width:980px) and (max-width:1079px) {
  .pronVideos {
    max-width: 363px;
  }

  .pronVideo {
    height: 204px;
  }
}

@media screen and (min-width:761px) and (max-width:959px) {
  .pronVideos {
    max-width: 366px;
  }

  .pronVideo {
    height: 205px;
  }
}

@media screen and (min-width:500px) and (max-width:620px) {
  .pronVideos {
    max-width: 440px;
  }

  .pronVideo {
    height: 247px;
  }
}

@media screen and (min-width:400px) and (max-width:499px) {
  .pronVideos {
    max-width: 360px;
  }

  .pronVideo {
    height: 203px;
  }
}

@media screen and (min-width:361px) and (max-width:399px) {
  .pronVideos {
    max-width: 320px;
  }

  .pronVideo {
    height: 180px;
  }
}

@media screen and (max-width:360px) {
  .pronVideos {
    max-width: 300px;
  }

  .pronVideo {
    height: 168px;
  }
}

#browseGroups div {
  display: inline;
}

.caro__el img {
  min-width: 100%;
}

.entry-body .xref {
  margin-top: 20px;
}

#mobEntryDictName {
  text-transform: capitalize;
}

@media screen and (min-width:980px) {
  .cdo-tpl-main__z2 {
    width: 604px;
  }

  .cdo-tpl-main__z1 {
    display: block;
    float: left;
    width: 160px;
    min-height: 600px;
  }

  .cdo-tpl-main__zwA {
    float: left;
    width: 740px;
    padding-left: 20px;
  }

  .cdo-tpl-main__z2 {
    width: 405px;
  }
}

@media screen and (min-width:1080px) {
  .cdo-tpl-main__z2 {
    width: 704px;
  }

  .cdo-tpl-main__z1 {
    display: block;
    float: left;
    width: 160px;
  }

  .cdo-tpl-main__zwA {
    float: left;
    width: 840px;
    padding-left: 20px;
  }

  .cdo-tpl-main__z2 {
    width: 505px;
  }

  .float-xl {
    float: none;
    padding-right: 0;
  }
}

@media screen and (min-width:1280px) {
  .cdo-tpl-main__z1 {
    display: block;
    float: left;
    width: 160px;
  }

  .cdo-tpl-main__zwA {
    float: left;
    width: 1080px;
    padding-left: 20px;
  }

  .cdo-tpl-main__z2 {
    width: 745px;
  }

  .float-xl {
    float: left;
    padding-right: 30px;
  }
}

@media screen and (min-width:1380px) {
  .cdo-tpl-main__zwA {
    width: 1180px;
  }

  .cdo-tpl-main__z2 {
    width: 845px;
  }
}

body {
  padding-top: 111px;
}

.default_layout .cdo-search,.translator_layout .cdo-search {
  padding: 7px 20px 6px;
}

@media screen and (min-width:960px) {
  .default_layout .cdo-search,.translator_layout .cdo-search,.dataset_layout .cdo-search {
    padding: 7px 30px 6px;
  }
}

.cdo-search__switches {
  max-height: 50px;
  white-space: normal;
}

.wordlist-popup * {
  box-sizing: border-box;
}

.wordlist-popup {
  position: absolute;
  bottom: 25px;
  right: -10px;
  width: 270px;
  margin: 10px 0;
  z-index: 6;
  background: #fff;
  border: 1px solid #c5c5c5;
  box-shadow: 0 0 15px rgba(0,0,0,.18);
  font-size: 14px;
  text-align: left;
}

.wordlist-popup:before {
  content: '';
  display: inline-block;
  position: absolute;
  right: 11px;
  width: 0;
  height: 0;
  border-style: solid;
  bottom: -10px;
  border-width: 10px 10px 0 10px;
  border-color: #c5c5c5 transparent transparent transparent;
}

.wordlist-popup.under {
  top: 25px;
  bottom: auto;
}

.wordlist-popup.right {
  right: auto;
  left: 0;
}

.wordlist-popup.right:before {
  right: auto;
  left: 0;
}

.wordlist-popup.under:before {
  bottom: auto;
  top: -10px;
  border-width: 0 10px 10px 10px;
  border-color: transparent transparent #c5c5c5 transparent;
}

.wordlist-popup ul {
  max-height: 200px;
  overflow-y: auto;
  overflow-x: hidden;
  margin: 0;
}

.wordlist-popup li,.clear {
  margin: 0;
  clear: both;
}

.wordlist-popup .title,.wordlist-popup .login-button {
  text-decoration: underline;
}

.wordlist-popup .title {
  font-weight: bold;
  padding: 8px;
  border-bottom: 0;
  margin: 0;
  display: block;
}

.wordlist-popup .intro-txt {
  list-style-type: none;
  padding: 0 8px 8px 8px;
  color: #111;
  font-weight: normal;
  font-size: .9em;
  cursor: default;
  border-bottom: 1px solid #c5c5c5;
}

.wordlist-popup .spinner {
  display: table;
  margin: 30px auto;
}

.wordlist-popup .name {
  float: left;
  display: block;
  padding: 8px;
  text-overflow: ellipsis;
  width: 180px;
  overflow: hidden;
  white-space: nowrap;
}

.wordlist-popup .name:hover {
  background: #d8d8ff;
  text-decoration: underline;
}

.wordlist-popup .add {
  margin: 3px 5px;
  float: right;
}

.wordlist-popup .error {
  padding: 8px;
  background: #a22f1b;
  color: #fff;
  font-size: 14px;
}

.wordlist-popup .info {
  padding: 8px;
  background: #bfcce9;
  color: #11326f;
  text-overflow: ellipsis;
  width: 270px;
  overflow: hidden;
  font-size: 14px;
}

.wordlist-popup .circle i {
  font-size: 1.2em;
  line-height: 1.9rem;
}

.wordlist-popup form {
  position: relative;
  border-top: solid 1px #c5c5c5;
  padding: 2px 0;
}

.wordlist-popup form input {
  border: 0;
}

.wordlist-popup form input[type='submit'] {
  float: right;
  line-height: 24px;
}

.wordlist-popup form input[type='text'] {
  width: 100%;
  margin: 3px;
  margin-right: 0;
  outline: 0;
  padding: 8px;
  background: 0;
  box-shadow: none;
  margin: 0;
}

.word-list {
  word-wrap: break-word;
  -webkit-line-break: after-white-space;
}

.cdo-search__input[type=text] {
  outline: 0;
}

.tiles__tile {
  text-transform: capitalize;
}

@media screen and (max-width:959px) {
  .entry-body .phrase-block.pad-indent,.entry-body .runon.pad-indent {
    padding-left: 15px;
  }

  .entry-body .phrase-body.pad-indent,.entry-body .runon-body.pad-indent {
    padding-left: 12px;
  }

  .entry-body .phrase-head:before,.entry-body .runon-head:before,.entry-body.british-grammar .panel-head:before {
    top: 0!important;
    left: -18px!important;
  }

  .entry-body .phrase-body:before,.entry-body .runon-body:before,.entry-body.british-grammar .panel-body.pad-indent:before {
    left: 0!important;
  }
}

.ipa {
  display: inline-block;
  padding: 0 2px 0 1px;
}

@media screen and (max-width:320px) {
  .js-share-toggle {
    display: none;
  }
}

@media screen and (max-height:600px) {
  .js-share-toggle {
    display: none;
  }
}

@media screen and (min-width:321px) and (min-height:601px) {
  .js-share .bg--more {
    display: none;
  }
}

.entry-body .share-container {
  position: relative;
}

.entry-body .idiom-block,.entry-body .share-pad {
  padding-right: 25px;
}

@media screen and (min-width:450px) {
  .entry-body .idiom-block,.entry-body .share-pad {
    padding-right: 70px;
  }
}

.cycler__items a {
  white-space: nowrap;
}

.scroller__mask {
  z-index: 2;
}

.scroller__nav {
  z-index: 3;
}

.virtualKeyboard {
  moz-user-drag: none;
  moz-user-select: none;
  webkit-user-select: none;
  webkit-user-drag: none;
  padding: 5px;
  display: none;
  background: #10326f;
  font-size: .875em;
}

.virtualKeyboard .selector a,.virtualKeyboard .data a {
  color: inherit;
  display: inline-block;
  margin: 3px;
  padding: 10px 15px;
  background: #4d6593;
  color: #fff;
  border-radius: 4px;
  box-shadow: 1px 2px 3px rgba(0,0,0,.4);
  cursor: pointer;
  text-decoration: none;
}

.virtualKeyboard .data a {
  background: #f0eff4;
  color: #000;
}

.virtualKeyboard .selector a {
  padding: 3px 5px;
}

.virtualKeyboard .data .keyboard-arabic a {
  font-size: 1.5em;
  padding: 6px 11px;
}

.virtualKeyboard .selector a.current,.virtualKeyboard .selector a:hover,.virtualKeyboard .data a.current,.virtualKeyboard .data a:hover {
  color: #fff;
  background: #cea54b;
}

.questionary-playground .js-keyboard {
  position: absolute;
  top: 0;
  right: 0;
  width: 40px;
  text-decoration: none;
  padding: 11px;
}

.questionary-playground .head-word {
  color: #234b9a;
  font-weight: bold;
}

.questionary-playground .result {
  margin-top: 20px;
}

.questionary-playground .questionary-congratulation {
  margin-top: 20px;
  font-weight: bold;
  font-size: 1.25em;
}

@media screen and (max-height:600px) {
  .virtualKeyboard .data .keyboard-arabic a {
    font-size: 1.2em;
  }

  .virtualKeyboard .data .keyboard-russian a {
    font-size: .85em;
  }

  .virtualKeyboard .data a {
    padding: 3px 6px!important;
    margin: 2px;
  }
}

header {
  white-space: nowrap;
}

@media screen and (max-width:761px) {
  .resp-show--med {
    display: none;
  }
}

.cdo-hdr__profile a.hdr-btn .btn {
  line-height: 22px;
  padding: 6px 12px;
}

@media screen and (max-width:959px) {
  .cdo-hdr__profile a.hdr-btn .fcdo {
    padding-right: 0;
  }
}

.pron {
  white-space: nowrap;
}

.superentry .region+.pron {
  margin-left: 5px;
}

.mod .am-default,.mod .am-testads {
  text-align: center;
}

#quizAnswerWord {
  padding-right: 40px;
}

#cdo-dataset {
  white-space: normal;
}

.cdo-tpl-home__z1 .ad-row__item {
  max-width: 340px;
  margin: 0 auto;
}

@media screen and (min-width:600px) and (max-width:1059px) {
  .cdo-tpl-home__z1 .ad-row__item {
    max-width: 400px;
  }
}

@media screen and (min-width:960px) and (max-width:1079px) {
  .cdo-tpl-home__z1 .ad-row--medrect3 .ad-row__item[data-itemno="3"] .mod>img {
    float: none;
    width: 100%;
  }
}

@media screen and (max-width:1079px) {
  .cdo-tpl-home__z1 .ad-row__sibling,.cdo-tpl-home__z1 .ad-row__wrapper {
    max-width: 680px;
    margin: 0 auto;
  }
}

.i {
  font-style: italic;
}

.gl {
  font-style: normal;
}

.lex {
  text-transform: none;
  font-style: italic;
}

.b {
  font-weight: bold;
}

.sp,.nu {
  font-size: 66%;
  position: relative;
  bottom: .5em;
}

.sb,.dn {
  font-size: 66%;
  position: relative;
  top: .3em;
}

.cle-xeg,.xeg {
  text-decoration: line-through;
}

.u {
  text-decoration: underline;
}

@media screen and (max-width:449px) {
  .di .share {
    right: -25px;
    width: 45px;
    padding: 8px 0;
  }

  .di .share .circle {
    position: relative;
  }
}

.email-form {
  text-align: center;
}

.tiles__tile label {
  padding: 20px 0;
}

.tiles__tile input[type="radio"]:checked+label:before,.tiles__tile input[type="checkbox"]:checked+label:before {
  padding: 1px 3px 2px 2px;
  position: absolute;
  top: 0;
  left: 0;
  color: #000;
  background: rgba(255,255,255,0.8);
  border-radius: 0 0 8px 0;
}

.wordlist-panel h1,.wordlist-panel .breadcrumb {
  font-size: 1.5em;
  color: #234b9a;
}

.wordlist-panel h1.breadcrumb,.wordlist-panel div.breadcrumb {
  font-size: 1em;
}

.wordlist-panel h1 a,.wordlist-panel div a,.breadcrumb a {
  text-decoration: none;
}

.wordlist-panel h1 a:hover,.breadcrumb a:hover {
  text-decoration: underline;
}

.entrybox .fav-entry .fcdo.fcdo-plus {
  line-height: 31px;
}

.entrybox .fav-entry .intro-txt .fcdo.fcdo-plus {
  line-height: 24px;
  margin-top: 0;
}

.sect.sect--bg h2 {
  margin-bottom: 15px;
  font-size: 1.35em;
  font-weight: normal;
}

h1.cdo-hero__title span {
  color: #d0a44c;
}

.margin-bottom {
  margin-bottom: 50px;
}

#browseResults .title {
  padding: 0;
  border: 0 none;
}

.padding-15 {
  padding: 15px 0;
}

.margin-top-15 {
  margin-top: 15px;
}

.txt-block--alt a,.txt-block--alt2 a {
  color: #fff;
  text-decoration: none;
}

.txt-block--alt a:hover,.txt-block--alt2 a:hover {
  text-decoration: underline;
}

.trans[lang="ar"] {
  font-size: 2em;
  font-weight: normal;
  unicode-bidi: -webkit-plaintext;
}

.rv+.rv:before {
  content: ' / ';
}

.img-thumb ~ .extraexamps,.img-thumb ~ .smartt {
  clear: both;
}

.sense-body:after {
  content: '';
  display: table;
  clear: both;
}

.img-thumb {
  position: relative;
  border: 1px solid #bfcce9;
  display: inline-block;
}

.img-thumb .img-copyright,.imageContainer .img-copyright {
  border-radius: 0;
  top: auto;
  left: auto;
  right: 0;
  bottom: 0;
  color: #fff;
  background: rgba(0,0,0,0.2);
  z-index: 2;
}

.img-thumb .img-copyright span {
  word-break: normal;
}

@media screen and (min-width:1080px) {
  .img-thumb {
    float: right;
    margin-left: 10px;
  }
}

.cdo-search__mega-menu,.autocompleter {
  display: none;
  position: absolute;
  z-index: 4;
  top: -5px;
  left: -6px;
  right: -6px;
  background: #eef1f5;
  padding: 80px 0 20px;
  border-radius: 3px;
  box-shadow: 0 0 3px 3px rgba(0,0,0,0.15);
}

.autocompleter .row {
  padding: 5px 20px;
}

.autocompleter .row.selected,.autocompleter .row:hover {
  background: rgba(255,255,255,0.8);
}

.autocompleter .row:before {
  content: "\f054";
  padding-right: 7px;
  vertical-align: middle;
  font-size: 12px;
  font-weight: 300;
  font-family: cdoicons;
  color: rgba(35,75,154,0.47);
}

@media screen and (max-width:1079px) {
  .cdo-search__mega-menu {
    top: 0;
    left: 0;
    right: 0;
    padding: 80px 0 0;
    font-size: .9375em;
    background: transparent;
  }
}

@media screen and (max-width:959px) {
  .cdo-search__mega-menu {
    padding: 50px 0 0;
  }
}

.entry-body.british-grammar .section {
  margin-top: 20px;
}

.entry-body.british-grammar .section ~ .section {
  margin-top: 40px;
}

.entry-body.british-grammar .section_anchor {
  height: 0;
}

.entry-body.british-grammar .panel {
  margin: 20px 0;
}

.entry-body.british-grammar h2,.entry-body.british-grammar h3,.entry-body.british-grammar h4 {
  color: #234b9a;
}

.entry-body .phrase-title,.entry-body .runon-title,.entry-body.british-grammar .panel-head {
  display: inline-block;
  margin: 0 0 10px;
  font-size: 1.1em;
  font-weight: bold;
  color: #234b9a;
}

.entry-body.british-grammar blockquote {
  font-size: inherit;
  font-style: inherit;
  color: #666;
}

.entry-body .phrase-head,.entry-body .runon-head,.entry-body .runon-body,.entry-body .phrase-body,.entry-body .phrase-body>.def-block,.entry-body.british-grammar .panel-head,.entry-body.british-grammar .panel-body {
  position: relative;
}

.entry-body .phrase-head:before,.entry-body .runon-head:before,.entry-body.british-grammar .panel-head:before {
  content: "\F054";
  position: absolute;
  top: 1px;
  left: -24px;
  font-weight: 300;
  font-family: cdoicons;
  color: #234b9a;
}

.entry-body .phrase-body:before,.entry-body .runon-body:before,.entry-body.british-grammar .panel-body.pad-indent:before {
  content: " ";
  position: absolute;
  top: 0;
  left: 15px;
  height: 100%;
  width: 3px;
  background: #eff1f6;
  z-index: -1;
}

.entry-body.british-grammar blockquote .utterance {
  clear: both;
  padding-left: 2em;
}

.entry-body.british-grammar blockquote .speaker {
  float: left;
  font-weight: bold;
  color: #234b9a;
  font-style: normal;
  margin-left: -2em;
  margin-top: 2px;
}

.entry-body.british-grammar .nav p,.entry-body.british-grammar td p {
  margin: 0;
}

.entry-body.british-grammar .nav>p {
  margin-top: 20px;
  line-height: 1.5em;
  font-weight: 700;
}

.entry-body.british-grammar .nav ul {
  margin-left: 30px;
  list-style-type: none;
}

.entry-body.british-grammar .nav a {
  font-weight: 700;
  color: #234b9a;
  text-decoration: none;
}

.entry-body.british-grammar .nav a:hover {
  text-decoration: underline;
}

.entry-body.british-grammar td {
  background: #eef1f5;
}

.entry-body.british-grammar blockquote::before {
  content: "";
}

.ruby {
  display: inline-block;
  align: text-bottom;
}

.rt {
  display: block;
  font-size: 80%;
  text-align: center;
  font-style: normal;
}

.rb {
  display: block;
}

.intonation-arrow {
  display: inline-block;
  height: 2.25em;
  vertical-align: bottom;
  width: 0;
  font-weight: normal;
}

.entry-body.british-grammar h1 {
  margin: 0 0 5px;
}

.entry-body.british-grammar .header {
  margin-bottom: 20px;
}

.entry-body .phrase-head,.entry-body .phrase-head:before,.entry-body .runon-head,.entry-body .runon-head:before,.entry-body .idiom-head,.entry-body .idiom-head:before {
  color: #5776b3;
}

.grammar-toc .h3 {
  margin-bottom: 2px;
}

.grammar-toc a {
  position: relative;
  display: block;
  padding: 12px 20px 12px 40px;
  text-decoration: none;
  color: #222;
}

.grammar-toc .section>a:before {
  position: absolute;
  content: "+";
  top: 50%;
  margin-top: -12px;
  left: 20px;
  font-size: 140%;
  color: #fa6043;
}

.grammar-toc .section.open>a:before {
  content: "\2013";
  margin-top: -14px;
}

.grammar-toc ul {
  margin: 0 0 20px;
  list-style: none;
}

.grammar-toc ul li {
  margin: 0;
  border-bottom: solid 1px #fff;
}

.grammar-toc>ul>li {
  background: #eee;
}

.grammar-toc>ul>li>ul>li {
  background: #eee;
  border-bottom: 0;
}

.grammar-toc>ul>li>ul>li:last-child {
  background: #eee;
  border-bottom: solid 1px #fff;
}

.grammar-toc>ul>li>ul>li>ul>li {
  background: #eee;
  border-bottom: 0;
}

.grammar-toc>ul>li>ul>li>ul>li:last-child {
  background: #eee;
  border-bottom: solid 1px #fff;
}

.grammar-toc>ul>li>ul>li>ul>li>ul>li {
  background: #eee;
  border-bottom: 0;
}

.grammar-toc>ul>li>ul>li>ul>li>ul>li:last-child {
  background: #eee;
  border-bottom: solid 1px #fff;
}

.grammar-toc>ul>li>ul>li>a {
  padding: 10px 20px 10px 40px;
}

.grammar-toc>ul>li>ul>li>ul>li>a {
  padding: 8px 20px 8px 40px;
}

.grammar-toc ul ul {
  margin: 0 0 -1px 15px;
  display: none;
}

.grammar-toc ul li.open>ul {
  display: block;
}

.sidebar-toc .current>a {
  font-weight: bold;
  color: #234b9a;
}

.inter-toc a {
  position: relative;
  display: block;
  padding: 10px 20px;
  text-decoration: none;
  color: #222;
}

.inter-toc ul {
  margin: 0;
  list-style: none;
}

.inter-toc ul li {
  background: #eee;
  margin-bottom: 2px;
}

.inter-toc ul li:last-child {
  margin-bottom: 0;
}

.inter-toc ul ul {
  margin: 0 0 0 20px;
}

.inter-toc ul ul li a:before {
  content: "\F054";
  font-family: cdoicons;
  color: #bfcce9;
  padding-right: 10px;
}

.med-obj__thumb--tight {
  position: relative;
}

.caro__el {
  position: relative;
  vertical-align: top;
}

.caro__el div {
  position: relative;
  margin-bottom: 10px;
}

.img-copyright {
  position: absolute;
  top: 0;
  left: 0;
  max-width: 100%;
  border: 0;
  background: rgba(0,0,0,0.4);
  color: #fff;
  border-radius: 0 0 4px 0;
  outline: 0;
}

.mobile .img-copyright {
  top: 37px;
  border-radius: 0 4px 4px 0;
}

.img-copyright i {
  display: inline-block;
  padding: 3px 5px;
  font-weight: bold;
  font-style: normal;
}

.img-copyright span {
  display: none;
  padding: 3px 5px;
  word-break: break-word;
  font-weight: normal;
  text-align: center;
}

.img-copyright.open {
  border-radius: 0;
  min-width: 100%;
}

.img-copyright.open i {
  display: none;
}

.img-copyright.open span {
  display: inline-block;
}

.cdo-hero--dataset .img-copyright {
  position: relative;
  border-radius: 0;
}

.cdo-hero--dataset .img-copyright.open {
  min-width: 10%;
}

.cdo-hero--error .cdo-hero__caption {
  position: relative;
  bottom: initial;
}

.cdo-hero--error .img-copyright {
  position: relative;
  border-radius: 0;
  background: rgba(255,255,255,0.4);
  color: #000;
}

.cdo-hero--error .img-copyright.open {
  min-width: 10%;
}

.notification {
  margin: 0;
}

.notification.banner {
  position: fixed;
  bottom: 0;
  width: 100%;
  font-size: .9em;
  z-index: 10000;
}

.notification.banner>li {
  display: none;
  margin: 0;
  padding: 10px 20px 0;
  background: rgba(17,50,111,.88);
  color: #fff;
}

.notification.banner>li:after {
  content: '';
  display: block;
  clear: both;
}

.notification.banner p,.notification.banner button {
  margin-bottom: 10px;
}

.notification.banner p {
  display: inline-block;
  margin-right: 10px;
}

.notification.banner button {
  background: #bfcce9;
  border-color: #bfcce9;
  color: #111;
}

.notification.banner button:hover {
  opacity: .9;
}

.notification.banner a {
  color: #fff;
  font-weight: 700;
  text-decoration: none;
}

.notification.banner a:hover {
  text-decoration: underline;
}

.notification.banner>li li {
  list-style: none;
}

.notification.banner .red {
  background: #e84427;
}

.notification.banner .red button {
  background-color: #b7371e;
  border-color: #b7371e;
  color: white;
}

.smartbanner-show {
  margin-top: 80px;
}

.smartbanner-show .smartbanner {
  display: block;
}

.smartbanner {
  position: absolute;
  left: 0;
  top: 0;
  display: none;
  width: 100%;
  height: 80px;
  line-height: 80px;
  font-family: 'Helvetica Neue',sans-serif;
  background: #f4f4f4;
  z-index: 9998;
  -webkit-font-smoothing: antialiased;
  overflow: hidden;
  -webkit-text-size-adjust: none;
}

.smartbanner-container {
  margin: 0 auto;
  white-space: nowrap;
}

.smartbanner-close {
  display: inline-block;
  vertical-align: middle;
  margin: 0 5px 0 5px;
  font-family: 'ArialRoundedMTBold',Arial;
  font-size: 20px;
  text-align: center;
  color: #888;
  text-decoration: none;
  border: 0;
  border-radius: 14px;
  -webkit-font-smoothing: subpixel-antialiased;
}

.smartbanner-close:active,.smartbanner-close:hover {
  color: #aaa;
}

.smartbanner-icon {
  display: inline-block;
  vertical-align: middle;
  width: 57px;
  height: 57px;
  margin-right: 12px;
  background-size: cover;
  border-radius: 10px;
}

.smartbanner-info {
  display: inline-block;
  vertical-align: middle;
  width: 44%;
  font-size: 11px;
  line-height: 1.2em;
  font-weight: bold;
}

.smartbanner-title {
  font-size: 13px;
  line-height: 18px;
}

.smartbanner-button {
  position: absolute;
  right: 20px;
  top: 0;
  bottom: 0;
  margin: auto 0;
  height: 24px;
  font-size: 14px;
  line-height: 24px;
  text-align: center;
  font-weight: bold;
  color: #6a6a6a;
  text-transform: uppercase;
  text-decoration: none;
  text-shadow: 0 1px 0 rgba(255,255,255,0.8);
}

.smartbanner-button:active,.smartbanner-button:hover {
  color: #aaa;
}

.smartbanner-ios {
  background: #f4f4f4;
  background: linear-gradient(to bottom,#f4f4f4,#cdcdcd);
  box-shadow: 0 1px 2px rgba(0,0,0,0.5);
  line-height: 80px;
}

.smartbanner-ios .smartbanner-close {
  border: 0;
  width: 18px;
  height: 18px;
  line-height: 18px;
  color: #888;
  text-shadow: 0 1px 0 white;
}

.smartbanner-ios .smartbanner-close:active,.smartbanner-ios .smartbanner-close:hover {
  color: #aaa;
}

.smartbanner-ios .smartbanner-icon {
  background: rgba(0,0,0,0.6);
  background-size: cover;
  box-shadow: 0 1px 3px rgba(0,0,0,0.3);
}

.smartbanner-ios .smartbanner-info {
  color: #6a6a6a;
  text-shadow: 0 1px 0 rgba(255,255,255,0.8);
}

.smartbanner-ios .smartbanner-title {
  color: #4d4d4d;
  font-weight: bold;
}

.smartbanner-ios .smartbanner-button {
  padding: 0 10px;
  min-width: 10%;
  color: #6a6a6a;
  background: #efefef;
  background: linear-gradient(to bottom,#efefef,#dcdcdc);
  border-radius: 3px;
  box-shadow: inset 0 0 0 1px #bfbfbf,0 1px 0 rgba(255,255,255,0.6),0 2px 0 rgba(255,255,255,0.7) inset;
}

.smartbanner-ios .smartbanner-button:active,.smartbanner-ios .smartbanner-button:hover {
  background: #dcdcdc;
  background: linear-gradient(to bottom,#dcdcdc,#efefef);
}

.smartbanner-android {
  background: #3d3d3d url(data:image/gif;base64,R0lGODlhCAAIAIABAFVVVf///yH5BAEHAAEALAAAAAAIAAgAAAINRG4XudroGJBRsYcxKAA7);
  box-shadow: inset 0 4px 0 #88b131;
  line-height: 82px;
}

.smartbanner-android .smartbanner-close {
  border: 0;
  width: 17px;
  height: 17px;
  line-height: 17px;
  margin-right: 7px;
  color: #b1b1b3;
  background: #1c1e21;
  text-shadow: 0 1px 1px #000;
  box-shadow: 0 1px 2px rgba(0,0,0,0.8) inset,0 1px 1px rgba(255,255,255,0.3);
}

.smartbanner-android .smartbanner-close:active,.smartbanner-android .smartbanner-close:hover {
  color: #eee;
}

.smartbanner-android .smartbanner-icon {
  background-color: transparent;
  box-shadow: none;
}

.smartbanner-android .smartbanner-info {
  color: #ccc;
  text-shadow: 0 1px 2px #000;
}

.smartbanner-android .smartbanner-title {
  color: #fff;
  font-weight: bold;
}

.smartbanner-android .smartbanner-button {
  min-width: 12%;
  color: #d1d1d1;
  padding: 0;
  background: 0;
  border-radius: 0;
  box-shadow: 0 0 0 1px #333,0 0 0 2px #dddcdc;
}

.smartbanner-android .smartbanner-button:active,.smartbanner-android .smartbanner-button:hover {
  background: 0;
}

.smartbanner-android .smartbanner-button-text {
  text-align: center;
  display: block;
  padding: 0 10px;
  background: #42b6c9;
  background: linear-gradient(to bottom,#42b6c9,#39a9bb);
  text-transform: none;
  text-shadow: none;
  box-shadow: none;
}

.smartbanner-android .smartbanner-button-text:active,.smartbanner-android .smartbanner-button-text:hover {
  background: #2ac7e1;
}

.smartbanner-windows {
  background: #f4f4f4;
  background: linear-gradient(to bottom,#f4f4f4,#cdcdcd);
  box-shadow: 0 1px 2px rgba(0,0,0,0.5);
  line-height: 80px;
}

.smartbanner-windows .smartbanner-close {
  border: 0;
  width: 18px;
  height: 18px;
  line-height: 18px;
  color: #888;
  text-shadow: 0 1px 0 white;
}

.smartbanner-windows .smartbanner-close:active,.smartbanner-windows .smartbanner-close:hover {
  color: #aaa;
}

.smartbanner-windows .smartbanner-icon {
  background: rgba(0,0,0,0.6);
  background-size: cover;
  box-shadow: 0 1px 3px rgba(0,0,0,0.3);
}

.smartbanner-windows .smartbanner-info {
  color: #6a6a6a;
  text-shadow: 0 1px 0 rgba(255,255,255,0.8);
}

.smartbanner-windows .smartbanner-title {
  color: #4d4d4d;
  font-weight: bold;
}

.smartbanner-windows .smartbanner-button {
  padding: 0 10px;
  min-width: 10%;
  color: #6a6a6a;
  background: #efefef;
  background: linear-gradient(to bottom,#efefef,#dcdcdc);
  border-radius: 3px;
  box-shadow: inset 0 0 0 1px #bfbfbf,0 1px 0 rgba(255,255,255,0.6),0 2px 0 rgba(255,255,255,0.7) inset;
}

.smartbanner-windows .smartbanner-button:active,.smartbanner-windows .smartbanner-button:hover {
  background: #dcdcdc;
  background: linear-gradient(to bottom,#dcdcdc,#efefef);
}

.smartbanner-android {
  position: initial;
}

.smartbanner-container {
  margin: 0 auto;
  white-space: normal;
}

.smartbanner-android * {
  box-shadow: none;
  text-shadow: none;
}

.smartbanner-android {
  background: #f7f7f7;
  box-shadow: inset 0 3px 0 #a7a7a7;
}

.smartbanner-android .smartbanner-close {
  color: #6f6f6f;
}

.smartbanner-android .smartbanner-button {
  position: absolute;
  top: 24px;
  right: 22px;
  color: #fff;
  border: 0;
  box-shadow: none;
  margin: 0;
  line-height: 30px;
}

.smartbanner-android .smartbanner-button-text {
  background: #589442;
  border-radius: 5px;
}

.smartbanner-android .smartbanner-button-text:active,.smartbanner-android .smartbanner-button-text:hover {
  background: #589442;
}

.smartbanner-android .smartbanner-info {
  width: 70%;
  padding-right: 65px;
}

.smartbanner-android .smartbanner-info * {
  color: #434343;
}

.smartbanner-android .smartbanner-close,.smartbanner-android .smartbanner-close:hover {
  color: #868686;
  background: 0;
  box-shadow: none;
  text-shadow: none;
  font-size: 30px;
}

.smartbanner-android .smartbanner-info span {
  visibility: hidden;
}

.report-popup *,.example-source-popup * {
  box-sizing: border-box;
}

.report-popup {
  position: absolute;
  bottom: 25px;
  right: -6.5px;
  width: 240px;
  margin: 10px 0;
  z-index: 6;
  background: #fff;
  border: 1px solid #c5c5c5;
  box-shadow: 0 0 15px rgba(0,0,0,.18);
  font-size: 14px;
  text-align: left;
}

.def-report-popup {
  position: absolute;
  bottom: 25px;
  width: 240px;
  margin: 10px 0;
  z-index: 6;
  background: #fff;
  border: 1px solid #c5c5c5;
  box-shadow: 0 0 15px rgba(0,0,0,.18);
  font-size: 14px;
  text-align: left;
}

.example-source-popup {
  position: absolute;
  bottom: 25px;
  right: .5px;
  width: 240px;
  margin: 10px 0;
  z-index: 6;
  background: #fff;
  border: 1px solid #c5c5c5;
  box-shadow: 0 0 15px rgba(0,0,0,.18);
  font-size: 14px;
  text-align: left;
  font-style: normal;
  cursor: text;
}

.sandbox-add-popup {
  position: absolute;
  bottom: 25px;
  right: .5px;
  width: 240px;
  margin: 10px 0;
  z-index: 6;
  background: #fff;
  border: 1px solid #c5c5c5;
  box-shadow: 0 0 15px rgba(0,0,0,.18);
  font-size: 14px;
  text-align: left;
  font-style: normal;
  cursor: text;
}

.report-popup:before,.example-source-popup:before,.sandbox-add-popup:before {
  content: '';
  display: inline-block;
  position: absolute;
  right: 11px;
  width: 0;
  height: 0;
  border-style: solid;
  bottom: -10px;
  border-width: 10px 10px 0 10px;
  border-color: #c5c5c5 transparent transparent transparent;
}

.def-report-popup:before {
  content: '';
  display: inline-block;
  position: absolute;
  left: 3px;
  width: 0;
  height: 0;
  border-style: solid;
  bottom: -10px;
  border-width: 10px 10px 0 10px;
  border-color: #c5c5c5 transparent transparent transparent;
}

.report-popup.under,.def-report-popup.under,.example-source-popup.under,.sandbox-add-popup.under {
  top: 25px;
  bottom: auto;
}

.report-popup.under:before,.def-report-popup.under:before,.example-source-popup.under:before,.sandbox-add-popup.under:before {
  bottom: auto;
  top: -10px;
  border-width: 0 10px 10px 10px;
  border-color: transparent transparent #c5c5c5 transparent;
}

.report-popup .title,.def-report-popup .title {
  font-weight: bold;
  padding: 8px;
  border-bottom: 1px solid #c5c5c5;
  margin: 0;
  display: block;
}

.report-popup .error,.def-report-popup .error {
  padding: 8px;
  background: #a22f1b;
  color: #fff;
  text-overflow: ellipsis;
  width: 240px;
  overflow: hidden;
  font-size: 14px;
}

.report-popup .info,.def-report-popup .info {
  padding: 8px;
  background: #bfcce9;
  color: #11326f;
  text-overflow: ellipsis;
  width: 240px;
  overflow: hidden;
  font-size: 14px;
}

.report-form,.def-report-form {
  position: relative;
  border-top: solid 1px #c5c5c5;
  padding: 2px 0;
}

.report-form input,.def-report-form input {
  border: 0;
}

.report-form input[type='text'],.def-report-form input[type='text'] {
  width: 100%;
  margin: 3px;
  outline: 0;
  padding: 8px;
  background: 0;
  box-shadow: none;
  margin: 0;
  border: solid 1px;
  font-weight: normal;
}

.report-form ul,.def-report-form ul {
  list-style-type: none;
  margin: 8px;
}

.report-form .reason-list,.def-report-form .report-list {
  position: relative;
  margin-left: 20px;
}

.report-form .reason-list label,.def-report-form .report-list label {
  margin-left: -2px;
}

.report-form #reason-option1,.report-form #reason-option2,.report-form #reason-option3,.def-report-form #report-option1,.def-report-form #report-option2,.def-report-form #report-option3 {
  position: absolute;
  top: 3px;
  height: 14px;
  left: -20px;
}

.report-form #reason-option-other,.def-report-form #report-option-other {
  display: inline-block;
  vertical-align: middle;
  margin-right: 5px;
  height: 14px;
}

.report-form label,.def-report-form label {
  float: none;
  margin: 0;
  padding: 0;
  display: inline-block;
  width: 90%;
  font-weight: normal;
}

.example-source-popup .example-source-close {
  background: #e84526;
  position: absolute;
  top: -12px;
  right: -12px;
  color: #fff;
  height: 24px;
  line-height: 22px;
  width: 24px;
  text-align: center;
  border-radius: 100%;
  cursor: pointer;
}

.sandbox-add-popup.under .sandbox-add-close {
  background: #e84526;
  position: absolute;
  bottom: -8px;
  right: -12px;
  color: #fff;
  height: 24px;
  line-height: 22px;
  width: 24px;
  text-align: center;
  border-radius: 100%;
  cursor: pointer;
}

.hansard-source .example-source-popup.under .example-source-close {
  top: 100px;
}

.wikipedia-source .example-source-popup.under .example-source-close {
  top: 75px;
}

.example-source-popup .example-source-close .fcdo-close {
  color: #fff;
}

.hansard-source .example-source-popup .example-source-popup-message {
  margin: 8px 8px 8px 20px;
}

.wikipedia-source .example-source-popup .example-source-popup-message {
  margin: 8px 8px 8px 30px;
}

.example-source-popup .example-source-popup-message img {
  height: 24px;
  width: 24px;
  position: absolute;
  margin-left: -26px;
}

.help-cdl .icon-table td:first-child {
  text-align: -webkit-center;
}

.help-cdl .icon-table td {
  border: 0;
}

.help-cdl span.example-beta-icon:before {
  margin-left: 0;
}

.vote-section {
  text-align: center;
  width: 27px;
  margin: 10px 20px;
}

.vote-section-icon {
  text-align: center;
  width: 25px;
}

.vote-section .fcdo,.vote-section-icon .fcdo {
  color: #686868;
}

.sandbox-vote-def {
  display: flex;
}

.sandbox-vote-def .headword {
  font-size: 2em;
}

.sandbox-vote-def .def-content {
  margin: 10px;
}

.sandbox-vote-def .smaller {
  margin-top: 10px;
}

.cpexamps {
  margin-bottom: 10px;
}

.cpexamps .white {
  color: white;
}

.cpexamps .italic {
  font-style: italic;
}

.cpexamps .bold {
  font-weight: bold;
}

.cpexamps .fcdo-comment-o {
  color: #000;
  vertical-align: text-bottom;
}

.example-btn {
  background: #234b9a;
  font-style: normal;
  line-height: 24px;
  min-width: 80px;
  height: 44px;
  float: right;
  margin: 8px;
}

.example-cancel-btn {
  background: #d0a44c;
}

.cpexamps .ex-opinion {
  color: #d0a44c;
  font-size: .9em;
  margin: 10px 0;
}

.cpexamps-head {
  padding: 12px 20px;
  background: #eff1f6;
  border-left: solid 1px #e6e6eb;
  border-right: solid 1px #e6e6eb;
}

.cpexamps-head p {
  font-size: 1em;
  margin: 0;
}

.cpexamps-head>div {
  display: flex;
  justify-content: space-between;
}

.cpexamps-head .flex {
  display: flex;
  justify-content: space-between;
}

.cpexamps-head .entry-link {
  white-space: nowrap;
  max-height: 48px;
  margin: 0 0 0 20px;
}

.cpexamps-head .entry-link i {
  font-size: 1.5em;
}

.cpexamps-head .helpus {
  font-size: 1.1em;
  margin-bottom: 6px;
  font-weight: bold;
}

.cpexamps-head .report-example-inappropriate-icon {
  padding: 2px;
}

.cpexamps-head .example-beta-btn {
  padding: 3px 8px;
  border-width: 2px;
  border-radius: 7px;
  border-color: #fff;
  border-style: solid;
  background: #e84427;
  color: #fff;
  font-weight: normal;
  height: 27px;
  white-space: nowrap;
  text-decoration: none;
}

span.example-beta-icon:before {
  content: 'BETA';
  margin-left: 5px;
  padding: 1px 3px;
  border-radius: 3px;
  border-color: #fff;
  background: #e84427;
  color: #fff;
  font-size: 14px;
}

.cpexamps-body {
  min-height: 240px;
  padding: 15px;
  margin: 0 0 20px;
  border: 1px solid #e6e6eb;
}

.cpexamps-body .title-container {
  margin-top: 5px;
}

.cpexamps-body .word-title {
  font-size: 1em;
  line-height: 2em;
  margin-top: 5px;
}

.cpegs {
  line-height: 1.5em;
}

.cpegs a {
  text-decoration: none;
}

.cpegs a:hover {
  text-decoration: underline;
}

.cpegs .margin-blue {
  background: #bfcce9;
  margin: 0;
  height: 35px;
}

.cpegs .margin-blue a {
  float: right;
  margin: 5px 20px 5px 0;
}

.cpegs .egs {
  background: #f4ead6;
}

.cpegs .egs .contentslot {
  background: #FFF;
  padding: 10px 0;
  text-align: center;
}

.cpegs .eg {
  border-bottom: 1px solid rgba(0,0,0,0.2);
  padding: 10px 15px;
}

.cpegs .eg .source {
  text-align: right;
  font-size: .9em;
}

.cpegs .eg .source .example-source {
  color: #234b9a;
  cursor: pointer;
  position: relative;
  display: inline;
}

.cpegs .eg em {
  font-style: normal;
}

.cpegs .eg .bi-content {
  margin-top: 5px;
}

.cpegs .report-example-inappropriate {
  padding: 2px 6px;
  border-width: 0;
  border-radius: 2px;
  margin-left: 4px;
  position: relative;
}

.entry-nav:after {
  content: " ";
  display: block;
  clear: both;
}

.cpegs .report-example-inappropriate:hover,.report-sandbox-def:hover {
  background: rgba(0,0,0,0.1);
}

@media screen and (min-width:450px) {
  .cpexamps-body {
    padding: 20px 20px 15px;
  }
}

@media screen and (min-width:762px) and (max-width:1280px) {
  .cpexamps-head .flex-res {
    display: block;
  }

  .cpexamps-head .entry-link {
    margin: 00px 0 10px 0;
  }
}

@media screen and (max-width:599px) {
  .cpexamps-head .flex-res {
    display: block;
  }

  .cpexamps-head .entry-link {
    margin: 0 0 10px 0;
  }
}

.sandbox-examps .cpexamps-head {
  background: #e84427;
}

.sandbox-examps .sandbox-examps-head .fcdo-comment-o {
  color: #fff;
}

.sandbox-examps .cpegs .egs {
  background: #fff;
}

.sandbox-examps .egs .eg:first-child {
  border-top: 1px solid rgba(0,0,0,0.2);
}

.sandbox-examps .margin-red {
  background: #b7371e;
  margin: 0 0 20px 0;
  padding: 12px 20px;
  border-left: solid 1px #e6e6eb;
  border-right: solid 1px #e6e6eb;
  display: flex;
  justify-content: space-between;
}

.sandbox-examps .margin-red div {
  align-self: center;
}

.sandbox-examps .block-title {
  font-weight: normal;
  color: #fff;
}

.sandbox-examps .sub-block-title {
  font-size: 1em;
  font-weight: normal;
  color: #f3bab3;
}

.kdict .runon {
  margin-top: 20px;
}

.kdict .trans {
  display: inline;
}

.kdict .examp {
  margin: 15px 0;
}

.kdict .examp .trans {
  font-weight: normal;
  font-style: italic;
  display: block;
  margin: 0;
}

#overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 99999999;
  overflow: hidden;
  align-items: center;
  background: rgba(64,64,64,0);
  transition: all .4s cubic-bezier(0.36,0.55,0.19,1);
  display: none;
}

#overlay.active {
  background: rgba(64,64,64,.2);
  display: flex;
}

.modal-container {
  background: #fff;
  margin: auto;
  width: 30%;
  border-radius: 3px;
  -moz-box-shadow: 0 3px 6px 0 rgba(0,0,0,.5);
  box-shadow: 0 3px 6px 0 rgba(0,0,0,.5);
}

.modal-container h2 {
  background-color: #234b9a;
  color: #fff;
  font-size: 18px;
  user-select: none;
  padding: 12px 16px;
  border-radius: 3px;
}

.modal-container .close {
  color: #fff;
  float: right;
  font-size: 24px;
  padding: 8px 16px;
}

.modal-container .close:hover,.modal-container .close:focus {
  text-decoration: none;
  cursor: pointer;
}

.modal-container .modal-body {
  padding: .01em 16px;
}

#navigation .modal {
  min-height: 0;
}

#navigation .modal-container {
  background-color: white;
  width: 100%;
  margin: 0;
}

#navigation .modal-container .modal-body {
  padding: 0;
}

#navigation .header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 15px;
  background-color: white;
  color: #292929;
  font-size: 1.6em;
}

#navigation .modal-container .close {
  color: #292929;
}

@media screen and (max-width:762px) {
  #navigation .modal-container {
    border-radius: 0;
    box-shadow: none;
    top: 0;
    bottom: 0;
    position: fixed;
    overflow: scroll;
  }

  #navigation .modal {
    width: 100%;
    height: 100%;
    margin: 0;
  }
}

.lightboxLink {
  cursor: pointer;
  position: relative;
  z-index: 1;
  max-width: 200px;
  max-height: 200px;
}

.lightboxOverlay {
  background: rgba(0,0,0,0.8);
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 10;
  padding: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.lightboxContainer {
  display: inline-block;
  position: relative;
  padding-bottom: 30px;
}

.lightboxImage {
  min-height: 200px;
  min-width: 200px;
  vertical-align: middle;
  border: solid 5px #fff;
  border-radius: 3px;
  background: #fff;
}

.lightboxClose {
  position: absolute;
  right: 10px;
  top: 10px;
  color: #000;
  font-size: 1.5em;
  text-decoration: none;
}

.lightboxCopyright {
  position: absolute;
  bottom: 0;
  color: #fff;
  left: 0;
}

.learn-more-box {
  width: 400px;
  margin-top: 10px;
}

.learn-more-box .btn {
  width: 400px;
  text-align: left;
  padding: 12px 20px;
  margin: 0;
  font-weight: bold;
}

.learn-more-box ul {
  padding: 12px 20px;
  margin: 0;
}

@media screen and (max-width:761px) {
  #search_bar {
    display: none;
  }

  #search_bar.open {
    display: block;
  }

  body {
    padding-top: 48px;
  }
}

@media screen and (min-width:762px) {
  #cdo_search_trigger {
    display: none;
  }
}
</style>"""
print(css, "\n")

for text in soup.find_all("span", "di-body"):
    print(css, text)
