# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.1.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
<!-- insertion marker -->
## Unreleased

<small>[Compare with latest](https://github.com/Josef-Friedrich/tmep/compare/v3.0.0...HEAD)</small>

## [v3.0.0](https://github.com/Josef-Friedrich/tmep/releases/tag/v3.0.0) - 2024-02-10

### Added

- Add some type hints

### Changed

- Rewrite documentation generation submodule
- Extend command line helper tmep-doc
- Rename class `Functions` into `DefaultTemplateFunctions`
- Rename method `DefaultTemplateFunctions.functions()` to `DefaultTemplateFunctions.get()`
- Switch to pytest

### Removed

- `tmep.doc` re-export in `__init__.py`

## [v2.4.0](https://github.com/Josef-Friedrich/tmep/releases/tag/v2.4.0) - 2024-01-04

<small>[Compare with v2.3.4](https://github.com/Josef-Friedrich/tmep/compare/v2.3.4...v2.4.0)</small>

## [v2.3.4](https://github.com/Josef-Friedrich/tmep/releases/tag/v2.3.4) - 2024-01-02

<small>[Compare with v2.3.2](https://github.com/Josef-Friedrich/tmep/compare/v2.3.2...v2.3.4)</small>

### Added

- Add missing types and update tooling ([49df004](https://github.com/Josef-Friedrich/tmep/commit/49df004b0e4222c63f188a70373d8453b146afde) by Josef Friedrich).
- Add tooling for auto format ([db8971b](https://github.com/Josef-Friedrich/tmep/commit/db8971b713da43e07117cb58e699a3208b800248) by Josef Friedrich).
- Add README_template.rst ([e91752d](https://github.com/Josef-Friedrich/tmep/commit/e91752d27bc12c30a6a4574234a25072b4cdf46e) by Josef Friedrich).
- Add license classifiers in pyproject.toml ([ac45035](https://github.com/Josef-Friedrich/tmep/commit/ac450350fbf73ba58c7cc224f002c55c10ed2712) by Josef Friedrich).

### Fixed

- Fix and update publish-to-pypi workflow ([fe1184b](https://github.com/Josef-Friedrich/tmep/commit/fe1184b036adcdf1a4b44983e16b4b8ded0274dc) by Josef Friedrich).
- Fix readthedocs build ([77cced0](https://github.com/Josef-Friedrich/tmep/commit/77cced0731e6b2dc6d7257e210b2f2a98d8a700e) by Josef Friedrich).
- Fix docs ([471616e](https://github.com/Josef-Friedrich/tmep/commit/471616e55047ce8c5cb99f74e51ef4d7fdb620ad) by Josef Friedrich).
- Fix tox tests ([ed9ad5a](https://github.com/Josef-Friedrich/tmep/commit/ed9ad5a6caa6492d7abf80bbd1e06dfbc48180ad) by Josef Friedrich).
- Fix github actions ([9bcabc9](https://github.com/Josef-Friedrich/tmep/commit/9bcabc9d3fd609a52d8a66268027931e67b0485e) by Josef Friedrich).

## [v2.3.2](https://github.com/Josef-Friedrich/tmep/releases/tag/v2.3.2) - 2022-07-12

<small>[Compare with v2.3.1](https://github.com/Josef-Friedrich/tmep/compare/v2.3.1...v2.3.2)</small>

## [v2.3.1](https://github.com/Josef-Friedrich/tmep/releases/tag/v2.3.1) - 2022-07-12

<small>[Compare with v2.3.0](https://github.com/Josef-Friedrich/tmep/compare/v2.3.0...v2.3.1)</small>

### Fixed

- Fix tests ([79b625b](https://github.com/Josef-Friedrich/tmep/commit/79b625b246ef45874444f7d3c828b81aed1f61fd) by Josef Friedrich).

### Removed

- Remove further files that belonged to the versioneer ([8ee9452](https://github.com/Josef-Friedrich/tmep/commit/8ee945290e089c8e596b116bd033305db03be32a) by Josef Friedrich).
- Remove versioneer ([e7bdf63](https://github.com/Josef-Friedrich/tmep/commit/e7bdf63c49237f81363b63eebfbff91c7bbe0510) by Josef Friedrich).

## [v2.3.0](https://github.com/Josef-Friedrich/tmep/releases/tag/v2.3.0) - 2022-06-23

<small>[Compare with v2.2.0](https://github.com/Josef-Friedrich/tmep/compare/v2.2.0...v2.3.0)</small>

### Added

- Add py.typed to the package data ([36943a8](https://github.com/Josef-Friedrich/tmep/commit/36943a8a422e4161aa86728fb1b6822988ac225f) by Josef Friedrich).

## [v2.2.0](https://github.com/Josef-Friedrich/tmep/releases/tag/v2.2.0) - 2022-06-23

<small>[Compare with v2.1.0](https://github.com/Josef-Friedrich/tmep/compare/v2.1.0...v2.2.0)</small>

### Added

- Add py.typed ([286a0ef](https://github.com/Josef-Friedrich/tmep/commit/286a0ef038ec22083a59ca16e7b8e8d38a9aac62) by Josef Friedrich).

## [v2.1.0](https://github.com/Josef-Friedrich/tmep/releases/tag/v2.1.0) - 2022-06-23

<small>[Compare with v2.0.2](https://github.com/Josef-Friedrich/tmep/compare/v2.0.2...v2.1.0)</small>

### Added

- Add more types ([02ce963](https://github.com/Josef-Friedrich/tmep/commit/02ce9634bb2391e6c35c0374b09ba6b76dfc320a) by Josef Friedrich).
- Add some types ([f4f22ed](https://github.com/Josef-Friedrich/tmep/commit/f4f22ed69b2ed86323af29319f45cbba3993e090) by Josef Friedrich).
- Add some type hints ([cbfd483](https://github.com/Josef-Friedrich/tmep/commit/cbfd483aa69d35ce6658695d1cfb618447fee0e2) by Josef Friedrich).

### Fixed

- Fix readthedocs build ([38809f8](https://github.com/Josef-Friedrich/tmep/commit/38809f8ba6ac94aa88a295e14018d80bbbe53c47) by Josef Friedrich).

## [v2.0.2](https://github.com/Josef-Friedrich/tmep/releases/tag/v2.0.2) - 2021-01-24

<small>[Compare with v2.0.1](https://github.com/Josef-Friedrich/tmep/compare/v2.0.1...v2.0.2)</small>

### Fixed

- Fix travis test 2 ([aa8c679](https://github.com/Josef-Friedrich/tmep/commit/aa8c679712654bcf99202d333646d684f54736a1) by Josef Friedrich).
- Fix travis test ([c77a3ab](https://github.com/Josef-Friedrich/tmep/commit/c77a3ab753fcec01346585b39239a5fc6eb15c22) by Josef Friedrich).

## [v2.0.1](https://github.com/Josef-Friedrich/tmep/releases/tag/v2.0.1) - 2019-12-29

<small>[Compare with v2.0.0](https://github.com/Josef-Friedrich/tmep/compare/v2.0.0...v2.0.1)</small>

## [v2.0.0](https://github.com/Josef-Friedrich/tmep/releases/tag/v2.0.0) - 2019-03-25

<small>[Compare with v1.1.3](https://github.com/Josef-Friedrich/tmep/compare/v1.1.3...v2.0.0)</small>

### Added

- Add the readthedocs badge ([1876f15](https://github.com/Josef-Friedrich/tmep/commit/1876f158c5aaca1f039eca00d1e4655c01c7ef7d) by Josef Friedrich).

## [v1.1.3](https://github.com/Josef-Friedrich/tmep/releases/tag/v1.1.3) - 2019-02-14

<small>[Compare with v1.1.2](https://github.com/Josef-Friedrich/tmep/compare/v1.1.2...v1.1.3)</small>

### Fixed

- Fix Windows installation bug cased by encoding issues ([c2942f8](https://github.com/Josef-Friedrich/tmep/commit/c2942f84fbf71a8bc7806216ce9c8b94c4fb55da) by Josef Friedrich).

## [v1.1.2](https://github.com/Josef-Friedrich/tmep/releases/tag/v1.1.2) - 2018-03-11

<small>[Compare with v1.1.1](https://github.com/Josef-Friedrich/tmep/compare/v1.1.1...v1.1.2)</small>

## [v1.1.1](https://github.com/Josef-Friedrich/tmep/releases/tag/v1.1.1) - 2018-03-11

<small>[Compare with v1.1.0](https://github.com/Josef-Friedrich/tmep/compare/v1.1.0...v1.1.1)</small>

## [v1.1.0](https://github.com/Josef-Friedrich/tmep/releases/tag/v1.1.0) - 2018-03-10

<small>[Compare with v1.0.9](https://github.com/Josef-Friedrich/tmep/compare/v1.0.9...v1.1.0)</small>

## [v1.0.9](https://github.com/Josef-Friedrich/tmep/releases/tag/v1.0.9) - 2018-02-28

<small>[Compare with v1.0.8](https://github.com/Josef-Friedrich/tmep/compare/v1.0.8...v1.0.9)</small>

### Added

- Add new function: 'initial' ([1d524e1](https://github.com/Josef-Friedrich/tmep/commit/1d524e1eb7af7e29e1b871caefb52356d48003c6) by Josef Friedrich).

## [v1.0.8](https://github.com/Josef-Friedrich/tmep/releases/tag/v1.0.8) - 2018-02-07

<small>[Compare with v1.0.7](https://github.com/Josef-Friedrich/tmep/compare/v1.0.7...v1.0.8)</small>

### Removed

- Remove tox env from .travis.yml ([71a9b7c](https://github.com/Josef-Friedrich/tmep/commit/71a9b7c4d0fa02428b875eb4daf9c4bb28def6c9) by Josef Friedrich).

## [v1.0.7](https://github.com/Josef-Friedrich/tmep/releases/tag/v1.0.7) - 2018-01-29

<small>[Compare with v1.0.6](https://github.com/Josef-Friedrich/tmep/compare/v1.0.6...v1.0.7)</small>

### Added

- Add some documentation ([e723275](https://github.com/Josef-Friedrich/tmep/commit/e723275a2dd31c6591f267b15642169c62558e98) by Josef Friedrich).
- Add new function ([d90cfd4](https://github.com/Josef-Friedrich/tmep/commit/d90cfd4a54f357d6e604e4e4eefc4ca49a6f92f6) by Josef Friedrich).

## [v1.0.6](https://github.com/Josef-Friedrich/tmep/releases/tag/v1.0.6) - 2018-01-28

<small>[Compare with v1.0.5](https://github.com/Josef-Friedrich/tmep/compare/v1.0.5...v1.0.6)</small>

### Fixed

- Fix ½ifdefempty{} ([f69cfc2](https://github.com/Josef-Friedrich/tmep/commit/f69cfc21be3fc7eea0e72166c70b5a4ea7d001de) by Josef Friedrich).

## [v1.0.5](https://github.com/Josef-Friedrich/tmep/releases/tag/v1.0.5) - 2018-01-28

<small>[Compare with v1.0.4](https://github.com/Josef-Friedrich/tmep/compare/v1.0.4...v1.0.5)</small>

### Added

- Add bin script ([9ba9016](https://github.com/Josef-Friedrich/tmep/commit/9ba901623527d97f1dc9a95abffecc6ec7cb80f9) by Josef Friedrich).
- Add new function ([8cc6939](https://github.com/Josef-Friedrich/tmep/commit/8cc6939b5d73ae1c899a5bfb092b4b3db6017267) by Josef Friedrich).

### Fixed

- Fix doc strings ([540f3e8](https://github.com/Josef-Friedrich/tmep/commit/540f3e87a60f99a1524c7f95ba16a1d8a4865383) by Josef Friedrich).

## [v1.0.4](https://github.com/Josef-Friedrich/tmep/releases/tag/v1.0.4) - 2018-01-27

<small>[Compare with v1.0.3](https://github.com/Josef-Friedrich/tmep/compare/v1.0.3...v1.0.4)</small>

### Changed

- Change section weight ([5bbc1be](https://github.com/Josef-Friedrich/tmep/commit/5bbc1be4e8a0f500a795e6b8ce7b5b43d513f55f) by Josef Friedrich).

## [v1.0.3](https://github.com/Josef-Friedrich/tmep/releases/tag/v1.0.3) - 2017-12-15

<small>[Compare with v1.0.2](https://github.com/Josef-Friedrich/tmep/compare/v1.0.2...v1.0.3)</small>

### Fixed

- Fix readme code blocks ([d5c994f](https://github.com/Josef-Friedrich/tmep/commit/d5c994f51d1d65f9ffce2f8221bf12935384b2ca) by Josef Friedrich).
- Fix travis matrix ([ed217e4](https://github.com/Josef-Friedrich/tmep/commit/ed217e4238c51cfc955c0860e6d37933cfc2ff5f) by Josef Friedrich).

## [v1.0.2](https://github.com/Josef-Friedrich/tmep/releases/tag/v1.0.2) - 2017-03-01

<small>[Compare with v1.0.1](https://github.com/Josef-Friedrich/tmep/compare/v1.0.1...v1.0.2)</small>

### Fixed

- Fix flake8 issue ([975ea88](https://github.com/Josef-Friedrich/tmep/commit/975ea888f88f3feea202a451c1f8e37063d3c4c5) by Josef Friedrich).

## [v1.0.1](https://github.com/Josef-Friedrich/tmep/releases/tag/v1.0.1) - 2016-10-26

<small>[Compare with v0.1.0](https://github.com/Josef-Friedrich/tmep/compare/v0.1.0...v1.0.1)</small>

## [v0.1.0](https://github.com/Josef-Friedrich/tmep/releases/tag/v0.1.0) - 2016-10-24

<small>[Compare with v0.0.8](https://github.com/Josef-Friedrich/tmep/compare/v0.0.8...v0.1.0)</small>

## [v0.0.8](https://github.com/Josef-Friedrich/tmep/releases/tag/v0.0.8) - 2016-10-16

<small>[Compare with v0.0.7](https://github.com/Josef-Friedrich/tmep/compare/v0.0.7...v0.0.8)</small>

### Added

- Add default value for shorten ([49096b8](https://github.com/Josef-Friedrich/tmep/commit/49096b8ca27e6ef5e5e62ce0eb9da1462c579992) by Josef Friedrich).

## [v0.0.7](https://github.com/Josef-Friedrich/tmep/releases/tag/v0.0.7) - 2016-10-16

<small>[Compare with v0.0.6](https://github.com/Josef-Friedrich/tmep/compare/v0.0.6...v0.0.7)</small>

### Added

- Add more tests ([1b05fec](https://github.com/Josef-Friedrich/tmep/commit/1b05fec4c34a90e304313aebd80f14142e995979) by Josef Friedrich).
- Add more test for functions ([efa462c](https://github.com/Josef-Friedrich/tmep/commit/efa462c65b7d0921286841e7d90ae372bb94bfb9) by Josef Friedrich).

### Fixed

- Fix asciify with unicode symbols ([4679efc](https://github.com/Josef-Friedrich/tmep/commit/4679efca7ffb8d00bf5872c0e4d39a94c947f9d7) by Josef Friedrich).
- Fix some flake8 issues ([0bfad60](https://github.com/Josef-Friedrich/tmep/commit/0bfad6008bdcd331053438060a5f9781b970beeb) by Josef Friedrich).

## [v0.0.6](https://github.com/Josef-Friedrich/tmep/releases/tag/v0.0.6) - 2016-10-14

<small>[Compare with v0.0.5](https://github.com/Josef-Friedrich/tmep/compare/v0.0.5...v0.0.6)</small>

### Added

- Add more tests ([ce400dd](https://github.com/Josef-Friedrich/tmep/commit/ce400dd74217ee9f6eaca16437de47e91d425c39) by Josef Friedrich).

## [v0.0.5](https://github.com/Josef-Friedrich/tmep/releases/tag/v0.0.5) - 2016-10-10

<small>[Compare with v0.0.4](https://github.com/Josef-Friedrich/tmep/compare/v0.0.4...v0.0.5)</small>

### Added

- Add textwrap to docs ([89a592e](https://github.com/Josef-Friedrich/tmep/commit/89a592e65ce9e735b05771df655fbfc062480fe5) by Josef Friedrich).

### Fixed

- Fix some flake8 issues ([b700590](https://github.com/Josef-Friedrich/tmep/commit/b70059096ff5fc042ccd28790ae1693e214fec40) by Josef Friedrich).

## [v0.0.4](https://github.com/Josef-Friedrich/tmep/releases/tag/v0.0.4) - 2016-10-02

<small>[Compare with v0.0.3](https://github.com/Josef-Friedrich/tmep/compare/v0.0.3...v0.0.4)</small>

### Added

- Add versioneer ([4b2b038](https://github.com/Josef-Friedrich/tmep/commit/4b2b038dc09429ea5945105b9b2e3e0a7b2357d4) by Josef Friedrich).
- Add tox dependencies ([992ac60](https://github.com/Josef-Friedrich/tmep/commit/992ac60907127654edf29ebc7384ad1bb4293afe) by Josef Friedrich).
- Add apidoc ([29f57b8](https://github.com/Josef-Friedrich/tmep/commit/29f57b84d49e2f99f7fe3aaef8c97906b14043a3) by Josef Friedrich).
- Add sphinx files ([80f30ac](https://github.com/Josef-Friedrich/tmep/commit/80f30ac7bf024520dc2bf2030794f12212605b43) by Josef Friedrich).

### Fixed

- Fix tox in travis ([94c4cc2](https://github.com/Josef-Friedrich/tmep/commit/94c4cc2c73ced80ede5d76db3ade929dec560875) by Josef Friedrich).
- Fix tox tests ([f7aacfe](https://github.com/Josef-Friedrich/tmep/commit/f7aacfe6f8d28eeecba51acd61e891ff3827ec11) by Josef Friedrich).
- Fix doc folder structure ([069f76b](https://github.com/Josef-Friedrich/tmep/commit/069f76b46730a7a237c19e53132a15c47021e11f) by Josef Friedrich).
- Fix links ([c20833a](https://github.com/Josef-Friedrich/tmep/commit/c20833a46ba712de760796bee9a7ad33f9de41a3) by Josef Friedrich).
- Fix pyflakes and pep8 issues ([613554c](https://github.com/Josef-Friedrich/tmep/commit/613554c2782c106a561f0df8113acdb6232bfd88) by Josef Friedrich).

### Changed

- Change sphinx theme ([0f56b87](https://github.com/Josef-Friedrich/tmep/commit/0f56b87447a990d49b4e5b9b2124da0049b85742) by Josef Friedrich).

## [v0.0.3](https://github.com/Josef-Friedrich/tmep/releases/tag/v0.0.3) - 2016-09-03

<small>[Compare with first commit](https://github.com/Josef-Friedrich/tmep/compare/de9fa7376e86e4bdaac76168832258e61bf3dbc6...v0.0.3)</small>

### Added

- Add MANIFEST.in ([9142a84](https://github.com/Josef-Friedrich/tmep/commit/9142a84dbb96ca7dc8d937383c703a7d84891825) by Josef Friedrich).
- Add long description ([1226928](https://github.com/Josef-Friedrich/tmep/commit/12269284ec0c3efed3258a3a0e5e491b26675b15) by Josef Friedrich).
- Add tests to tests folder ([cbc6505](https://github.com/Josef-Friedrich/tmep/commit/cbc65058c86cdcbfab73ac3d7689a86e4f0f72c4) by Josef Friedrich).
- Add more documentation ([0682427](https://github.com/Josef-Friedrich/tmep/commit/06824272c5b2d9329687c3668168404163b2fad9) by Josef Friedrich).
- Add test to test parameter functions in tmep.parse() ([b6e4a4d](https://github.com/Josef-Friedrich/tmep/commit/b6e4a4d5b1196f7ba0a4e45eea3b6a1f47f80e5f) by Josef Friedrich).
- Add basic example code ([7c0edad](https://github.com/Josef-Friedrich/tmep/commit/7c0edad7e522c84724eca4b3ab90088c17400c86) by Josef Friedrich).
- Add test file from beets ([737c9ae](https://github.com/Josef-Friedrich/tmep/commit/737c9ae767545b5e93b03ebe2bb2b9df6640b1bd) by Josef Friedrich).
- Add badges ([e14d72d](https://github.com/Josef-Friedrich/tmep/commit/e14d72de8029ce2f73c5efd1559665e96bdfecd6) by Josef Friedrich).
- Add some tests ([a127de8](https://github.com/Josef-Friedrich/tmep/commit/a127de8fe8ed56dc5aa7496da581d94145be6f67) by Josef Friedrich).
- Add Travis CI support ([3409faf](https://github.com/Josef-Friedrich/tmep/commit/3409faf9adf3614aecf3dc3a883fbc649345bf29) by Josef Friedrich).
- Add link to beets project ([6a49f9d](https://github.com/Josef-Friedrich/tmep/commit/6a49f9db43dd014ce81824741e21c2b98391a0b4) by Josef Friedrich).
- Add unit test ([7a3c8bb](https://github.com/Josef-Friedrich/tmep/commit/7a3c8bbf20da572bed8ede8bcd4c76d131af9dae) by Josef Friedrich).
- Add wrapper for Classes ([20c589a](https://github.com/Josef-Friedrich/tmep/commit/20c589aa1aab60f1a790c378de86030e96c1e20b) by Josef Friedrich).
- Add init file ([858e216](https://github.com/Josef-Friedrich/tmep/commit/858e21657c00fb5d77882d11b014e6669439e4bf) by Josef Friedrich).
- Add test to README ([cb27e57](https://github.com/Josef-Friedrich/tmep/commit/cb27e57f06f3a186a8a1be41413cd28592389129) by Josef Friedrich).
- Add setup.py ([e629c99](https://github.com/Josef-Friedrich/tmep/commit/e629c998c03d69fb436dd0e5bd626a317d449aa5) by Josef Friedrich).
- Add code ([f89964c](https://github.com/Josef-Friedrich/tmep/commit/f89964c348d26ef87476a68cb9471a5bcd11ed78) by Josef Friedrich).

### Fixed

- Fix indentation ([2f8f00f](https://github.com/Josef-Friedrich/tmep/commit/2f8f00fef7925f2cbb7124c588394a5b6d2648e0) by Josef Friedrich).
- Fix Python 2/3 issues ([55755f9](https://github.com/Josef-Friedrich/tmep/commit/55755f902bf155583e9ad4433d548eba3c9e57a4) by Josef Friedrich).
- Fix tests ([d554a13](https://github.com/Josef-Friedrich/tmep/commit/d554a13d8c4cf44ce2f8d59a4a21ff69f7ae623e) by Josef Friedrich).
