<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/haryHuds0n/AsteriskConvertAudio">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Asterisk PCM Converter</h3>

  <p align="center">
    Bulk convert Asterisk PBX PCM to Mp3 file
    <br />
    <a href="#getting-started"><strong>Explore the docs »</strong></a>

  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<img src="images/wav-to-mp3.png" alt="drawing" width="700"/>


## Getting Started
### Prerequisites

* [Ffmpeg](https://windowsloop.com/install-ffmpeg-windows-10/)


### Installation

* Clone the repo and install requirements
   ```bash
    git clone https://github.com/haryHuds0n/AsteriskConvertAudio.git
    
    cd AsteriskConvertAudio
    
    pip install -r requirements.txt
   ```
<!-- USAGE EXAMPLES -->
## Usage

Open Command Prompt or Powershell where the script is locate and execute it. 
  ```bash
  Python MergeFilePython [-v] [-h] <Path>
  ```
  Argument
  
  * Path: Absolute path to folder contain raw (PCM) file.
  
  Options
  * -v: Increase output verbose.
  * -h: Display help message.

For more infomation, please refer to the some documention below

- [PythonWave Library](https://docs.python.org/3/library/wave.html)
- [Python PyDub Library](https://github.com/jiaaro/pydub)
- [PyDub Readthedocs](https://audiosegment.readthedocs.io/en/latest/audiosegment.html)
<br/><br/>
<!-- ROADMAP -->

See the [open issues](https://github.com/haryHuds0n/AsteriskConvertAudio/issues) for a full list of proposed features (and known issues).




<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- CONTACT -->
## Contact

Hary - Email: example@example.com

Project Link: [Asterisk PBX Convert Audio](https://github.com/haryHuds0n/AsteriskConvertAudio.git)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/haryHuds0n/AsteriskConvertAudio.svg
[contributors-url]: https://github.com/haryHuds0n/AsteriskConvertAudio/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/haryHuds0n/AsteriskConvertAudio.svg
[forks-url]: https://github.com/haryHuds0n/AsteriskConvertAudio/network/members
[stars-shield]: https://img.shields.io/github/stars/haryHuds0n/AsteriskConvertAudio.svg
[stars-url]: https://github.com/haryHuds0n/AsteriskConvertAudio/stargazers
[issues-shield]: https://img.shields.io/github/issues/haryHuds0n/AsteriskConvertAudio.svg
[issues-url]: https://github.com/haryHuds0n/AsteriskConvertAudio/issues
[license-shield]: https://img.shields.io/github/license/haryHuds0n/AsteriskConvertAudio.svg
[license-url]: https://github.com/haryHuds0n/AsteriskConvertAudio/blob/master/LICENSE.md
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[thumbnail-image]: images/wav-to-mp3.png
