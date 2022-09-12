# shibafes2022-toilet-monitoring-system
## 概要
- ./toilet_pico/main*f.py　をmain.pyにrenameして各フロアのRaspberry Pi Pico(Micro Python)に書き込んで使用。
- ./main.pyは0201にあるRaspberryPiで実行。systemdでserviceにすること推奨。
- Pythonのコードが汚くて整備性が低いのは許してください。
---
- [shibafes2022-toilet-monitoring-system](#shibafes2022-toilet-monitoring-system)
  - [概要](#概要)
  - [- Pythonのコードが汚くて整備性が低いのは許してください。](#--pythonのコードが汚くて整備性が低いのは許してください)
  - [接続方法](#接続方法)
    - [women 2F](#women-2f)
    - [women 3F](#women-3f)
    - [women 4F](#women-4f)
    - [women 5F](#women-5f)
    - [women 6F](#women-6f)
    - [men 2F](#men-2f)
    - [men 3-5F](#men-3-5f)
    - [men 6F](#men-6f)
---
## 接続方法

### women 2F 
| Pico| ケーブル |
| --- | ------- |
| GP0 | UART0 TX to 0201 |
| GP1 | UART0 RX from 3F women|
| GP5 | none |
| GP6 | toilet1 Signal |
| GP7 | toilet2 Signal |
| GP8 | toilet3 Signal |
| GP9 | toilet4 Signal |
| 3V3 | toilet GND | 
| GND | 各フロア共通GND |

### women 3F 
| Pico| ケーブル |
| --- | ------- |
| GP0 | UART0 TX to 2F women |
| GP1 | UART0 RX from 4F women |
| GP5 | UART1 RX from 0201 |
| GP6 | toilet1 Signal |
| GP7 | toilet2 Signal |
| GP8 | toilet3 Signal |
| GP9 | toilet4 Signal |
| GP10 | toilet5 Signal |
| GP11 | toilet6 Signal |
| GP12 | toilet7 Signal |
| GP18 | toilet**11** Signal |
| GP19 | toilet**10** Signal |
| GP20 | toilet**9** Signal |
| GP21 | toilet**8** Signal |
| 3V3 | toilet GND | 
| GND | 各フロア共通GND |

### women 4F 
| Pico| ケーブル |
| --- | ------- |
| GP0 | UART0 TX to 3F women |
| GP1 | UART0 RX from 5F women|
| GP5 | UART1 RX from 0201 |
| GP6 | toilet1 Signal |
| GP7 | toilet2 Signal |
| GP8 | toilet3 Signal |
| GP9 | toilet4 Signal |
| 3V3 | toilet GND | 
| GND | 各フロア共通GND |

### women 5F 
| Pico| ケーブル |
| --- | ------- |
| GP0 | UART0 TX to 4F women |
| GP1 | UART0 RX from 6F women |
| GP5 | UART1 RX from 0201 |
| GP6 | toilet1 Signal |
| GP7 | toilet2 Signal |
| GP8 | toilet3 Signal |
| GP9 | toilet4 Signal |
| GP10 | toilet5 Signal |
| GP11 | toilet6 Signal |
| GP12 | toilet7 Signal |
| GP18 | toilet**11** Signal |
| GP19 | toilet**10** Signal |
| GP20 | toilet**9** Signal |
| GP21 | toilet**8** Signal |
| 3V3 | toilet GND | 
| GND | 各フロア共通GND |

### women 6F 
| Pico| ケーブル |
| --- | ------- |
| GP0 | UART0 TX to 5F women |
| GP1 | none |
| GP5 | UART1 RX from 0201 |
| GP6 | toilet1 Signal |
| GP7 | toilet2 Signal |
| GP8 | toilet3 Signal |
| GP9 | toilet4 Signal |
| 3V3 | toilet GND | 
| GND | 各フロア共通GND |

### men 2F 
| Pico| ケーブル |
| --- | ------- |
| GP0 | UART0 TX to 0201 |
| GP1 | UART0 RX from 3F men |
| GP5 | none |
| GP6 | toilet1 Signal |
| GP7 | toilet2 Signal |
| GP8 | toilet3 Signal |
| GP9 | toilet4 Signal |
| GP10 | toilet5 Signal |
| GP11 | toilet6 Signal |
| 3V3 | toilet GND | 
| GND | 各フロア共通GND |

### men 3-5F 
| Pico| ケーブル |
| --- | ------- |
| GP0 | UART0 TX to (now floor-1)F men |
| GP1 | UART0 RX from (now floor+1)F men |
| GP5 | UART1 RX from 0201 |
| GP6 | toilet1 Signal |
| GP7 | toilet2 Signal |
| GP8 | toilet3 Signal |
| GP9 | toilet4 Signal |
| GP10 | toilet5 Signal |
| GP11 | toilet6 Signal |
| 3V3 | toilet GND | 
| GND | 各フロア共通GND |

### men 6F 
| Pico| ケーブル |
| --- | ------- |
| GP0 | UART0 TX to 5F men |
| GP1 | none |
| GP5 | UART1 RX from 0201 |
| GP6 | toilet1 Signal |
| GP7 | toilet2 Signal |
| GP8 | toilet3 Signal |
| GP9 | toilet4 Signal |
| GP10 | toilet5 Signal |
| GP11 | toilet6 Signal |
| 3V3 | toilet GND | 
| GND | 各フロア共通GND |



--- 
このREADMEは書いてる途中です。
