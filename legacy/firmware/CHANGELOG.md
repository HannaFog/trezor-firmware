# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added
- Set initialized in storage to false if no mnemonic is present.  [#965]
- Support multiple change-outputs.  [#1098]

### Changed
- `Features.pin_cached` renamed to `unlocked`, and it is now `true` even if PIN is not set.

### Deprecated

### Removed

### Fixed
- Re-introduce ability to spend pre-Overwinter UTXO on Zcash-like coins.  [#1030]

### Security

------------

### Older changelog:

Version 1.9.1 [Jun 2020]
* Stream previous tx also for Segwit inputs

Version 1.9.0 [Apr 2020]
* Disallow changing of settings via dry-run recovery
* Wipe code
* Make LoadDevice debug only and drop its XPRV feature
* Add feature to retrieve the next U2F counter
* Passphrase redesign
* Cache up to 10 sessions (passphrases)
* Show xpubs with multisig get_address
* Update nanopb api to version 0.4

Version 1.8.3 [Sep 2019]
* Small code improvements

Version 1.8.2 [Aug 2019]
* OLED display security improvements
* Fix display of non-divisible OMNI amounts

Version 1.8.1 [May 2019]
* Fix fault when using the device with no PIN
* Fix OMNI transactions parsing

Version 1.8.0 [Feb 2019]
* Security improvements
* Upgraded to new storage format
* Stellar and NEM fixes
* New coins: ATS, KMD, XPM, XSN, ZCL
* New ETH tokens
* Included bootloader 1.8.0

Version 1.7.3 [Dec 2018]
* Fix USB issue on some Windows 10 installations

Version 1.7.2 [Dec 2018]
* Add support for OMNI layer: OMNI/MAID/USDT
* U2F fixes
* Don't ask for PIN if it has been just set
* Included bootloader 1.6.1

Version 1.7.1 [Oct 2018]
* Add support for Lisk
* Add support for Zcash Sapling hardfork
* Implement seedless setup

Version 1.7.0 [Sep 2018]
* Switch from HID to WebUSB
* Add support for Stellar
* Included bootloader 1.6.0

Version 1.6.3 [Aug 2018]
* Implement RSKIP-60 Ethereum checksum encoding
* Add support for new Ethereum networks (ESN, AKA, ETHO, MUSI, PIRL, ATH, GO)
* Add support for new 80 Ethereum tokens
* Improve MPU configuration
* Included bootloader 1.5.1

Version 1.6.2 [Jun 2018]
* Add possibility to set custom auto-lock delay
* Bitcoin Cash cashaddr support
* Zcash Overwinter hardfork support
* Support for new coins:
  - Decred, Bitcoin Private, Fujicoin, Groestlcoin, Vertcoin, Viacoin, Zcoin
* Support for new Ethereum networks:
  - EOS Classic, Ethereum Social, Ellaism, Callisto, EtherGem, Wanchain
* Support for 500+ new Ethereum tokens
* Included bootloader 1.5.0

Version 1.6.1 [Mar 2018]
* Use fixed-width font for addresses
* Lots of under-the-hood improvements
* Fixed issue with write-protection settings
* Included bootloader 1.4.0

Version 1.6.0 [Nov 2017]
* Native SegWit (Bech32) address support
* Show recognized BIP44/BIP49 paths in GetAddress dialog
* NEM support
* Expanse and UBIQ chains support
* Bitcoin Gold, DigiByte, Monacoin support
* Ed25519 collective signatures (CoSi) support

Version 1.5.2 [Aug 2017]
* Clean memory on start
* Fix storage import from older versions

Version 1.5.1 [Jul 2017]
* Wipe storage after 16 wrong PIN attempts
* Enable Segwit for Bitcoin
* Bcash aka Bitcoin Cash support
* Message signing/verification for Ethereum and Segwit
* Make address dialog nicer (switch text/QR via button)
* Use checksum for Ethereum addresses
* Add more ERC-20 tokens, handle unrecognized ERC-20 tokens
* Allow "dry run" recovery procedure
* Allow separated backup procedure

Version 1.5.0 [May 2017]
* Enable Segwit for Testnet and Litecoin
* Enable ERC-20 tokens for Ethereum chains

Version 1.4.2 [Jan 2017]
* New Matrix-based recovery method
* Minor Ethereum fixes (including EIP-155 replay protection)
* Minor USB, U2F and GPG fixes

Version 1.4.1 [Oct 2016]
* Support for Zcash JoinSplit transactions
* Enable device lock after 10 minutes of inactivity
* Enable device lock by pressing left button for 2 seconds
* Confirm dialog for U2F counter change

Version 1.4.0 [Aug 2016]
* U2F support
* Ethereum support
* GPG decryption support
* Zcash support

Version 1.3.6 [Jun 2016]
* Enable advanced transactions such as ones with REPLACE-BY-FEE and CHECKLOCKTIMEVERIFY
* Fix message signing for altcoins
* Message verification now shows address
* Enable GPG signing support
* Enable Ed25519 curve (for SSH and GPG)
* Use separate deterministic hierarchy for NIST256P1 and Ed25519 curves
* Users using SSH already need to regenerate their keys using the new firmware!!!

Version 1.3.5 [Feb 2016]
* Double size font for recovery words during the device setup
* Optimizations for simultaneous access when more applications try communicate with the device

Version 1.3.4 [Aug 2015]
* Screensaver active on ClearSession message
* Support for NIST P-256 curve
* Updated SignIdentity to v2 format
* Show seconds counter during PIN lockdown
* Updated maxfee per kb for coins

Version 1.3.3 [Apr 2015]
* Ask for PIN on GetAddress and GetPublicKey
* Signing speed improved

Version 1.3.2 [Mar 2015]
* Fix check during transaction streaming
* Login feature via SignIdentity message
* GetAddress for multisig shows M of N description
* PIN checking in constant time

Version 1.3.1 [Feb 2015]
* Optimized signing speed
* Enabled OP_RETURN
* Added option to change home screen
* Moved fee calculation before any signing
* Made PIN delay increase immune against hardware hacking

Version 1.3.0 [Dec 2014]
* Added multisig support
* Added visual validation of receiving address
* Added ECIES encryption capabilities

Version 1.2.1 [Jul 2014]
* Added stack overflow protection
* Added compatibility with Trezor Bridge

Version 1.2.0 [Jul 2014]
* Fix false positives for fee warning
* Better UI for signing/verifying messages
* Smaller firmware size

Version 1.1.0 [Jun 2014]
* Minor UI fixes
* Better handling of unexpected messages
* Added AES support

Version 1.0.0 [Apr 2014]
* Added support for streaming of transactions into the device
* Removed all current limits on size of signed transaction

[#965]: https://github.com/trezor/trezor-firmware/issues/965
[#1030]: https://github.com/trezor/trezor-firmware/issues/1030
[#1098]: https://github.com/trezor/trezor-firmware/issues/1098
