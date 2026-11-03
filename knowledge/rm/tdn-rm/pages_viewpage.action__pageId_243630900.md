---
content_hash: 7ae30591c1d3da365f1406a3cc696335786c169ea9b7a0f9ce15746bac505400
fetched_at: '2026-06-29T00:08:11.920567+00:00'
page_id: '243630900'
product: rm
source: tdn-rm
title: RPT00017.1.1 - QRCode (Passo a Passo)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243630900
version: 18
---

# Índice:

---

.\*ndice:

# Como utilizar:

---

      Na janela suspensa **"Caixa de Ferramentas"**, escolha **"Código de Barras".**

2. Na janela suspensa **"Grade de Propriedades",** referente ao controle já adicionado **"CódigodeBarras1"** na propriedade **"Simbologia",** escolher **"QRCode".**

# Propriedades Customizáveis referentes a Simbologia QRCode:

---

**Modo de compactação:**

| Nome do modo de compactação | Descrição do modo de compactação |
| --- | --- |
| Alfa Numérico | Uma combinação de caracteres alfabéticos e numéricos são codificados. Máximo de **4.296** caracteres. |
| Byte | Dados binários são codificados. Máximo de **2.953** bytes **(~3 kb)**. |
| Numérico | Dados numéricos são codificados. Máximo de **7.089** caracteres. |

**Tópico Externo: [QRCodeCompactionModeEnum](https://documentation.devexpress.com/#CoreLibraries/DevExpressXtraPrintingBarCodeQRCodeCompactionModeEnumtopic)**

**image2016-7-6 16-19-372image2016-7-6 15:40:2.png, image2016-7-6 15:27:24.png, image2016-7-6 16:18:43.png, image2016-7-6 16:17:19.png, image2016-7-6 16:19:37.png, image2016-7-6 16:55:3.png, image2016-7-6 16:55:49.pngdateGaleria Modo de Compactação Alfa Numérico**

OBS

O modo de compactação **"Alfa Numérico"** compreende apenas valores de **A-Z (maiúsculo)** e alguns caracteres especiais como **"."**, **":"**,**"("**, **")".**

**image2016-7-6 16-19-372image2016-7-6 15:40:2.png, image2016-7-6 15:27:24.png, image2016-7-6 16:18:43.png, image2016-7-6 16:17:19.png, image2016-7-6 16:19:37.png, image2016-7-6 16:37:28.png, image2016-7-6 16:39:51.pngdateGaleria Modo de Compactação Byte**

OBS

O modo de compactação **"Byte"** suporta apenas **2,953 kb**, ou seja, um campo imagem, da tabela **GIMAGEM**, **não pode ser usado,** já que o número de bytes que o representa **é maior** do que o **máximo suportado** pelo componente**.**

**image2016-7-6 16-19-372image2016-7-6 15:40:2.png, image2016-7-6 15:27:24.png, image2016-7-6 16:18:43.png, image2016-7-6 16:37:28.png, image2016-7-6 16:39:51.png, image2016-7-6 16:55:3.png, image2016-7-6 16:55:49.pngdateGaleria Modo de Compactação Numérico**

# Nível de Correção de Erro:

---

| Nome do Nível de Correção de Erro | Descrição do Nível de Correção de Erro |
| --- | --- |
| H | Permite recuperar por volta de **30%** de perda de dados. |
| L | Permite recuperar por volta de **7%** de perda de dados. |
| M | Permite recuperar por volta de **15%** de perda de dados. |
| Q | Permite recuperar por volta de **25%** de perda de dados. |

**Tópico Externo:** **[QRCodeErrorLevelEnum](https://documentation.devexpress.com/#DocumentServer/DevExpressBarCodesQRCodeErrorLevelEnumtopic)**

# Versão:

---

| Nome da Versão | Descrição da Versão |
| --- | --- |
| AutoVersion | A versão é autocalculada. |
| Version1 | **21**x**21** |
| Version10 | **57**x**57** |
| Version11 | **61**x**61** |
| Version12 | **65**x**65** |
| Version13 | **69**x**69** |
| Version14 | **73**x**73** |
| Version15 | **77**x**77** |
| Version16 | **81**x**81** |
| Version17 | **85**x**85** |
| Version18 | **89**x**89** |
| Version19 | **93**x**93** |
| Version2 | **25**x**25** |
| Version20 | **97**x**97** |
| Version21 | **101**x**101** |
| Version22 | **105**x**105** |
| Version23 | **109**x**109** |
| Version24 | **113**x**113** |
| Version25 | **117**x**117** |
| Version26 | **121**x**121** |
| Version27 | **125**x**125** |
| Version28 | **129**x**129** |
| Version29 | **133**x**133** |
| Version3 | **29**x**29** |
| Version30 | **137**x**137** |
| Version31 | **141**x**141** |
| Version32 | **145**x**145** |
| Version33 | **149**x**149** |
| Version34 | **153**x**153** |
| Version35 | **157**x**157** |
| Version36 | **161**x**161** |
| Version37 | **165**x**165** |
| Version38 | **169**x**169** |
| Version39 | **177**x**177** |
| Version4 | **33**x**33** |
| Version40 | **177**x**177** |
| Version5 | **37**x**37** |
| Version6 | **41**x**41** |
| Version7 | **45**x**45** |
| Version8 | **49**x**49** |
| Version9 | **53**x**53** |

**Tópico Externo: [QRCodeVersionEnum](https://documentation.devexpress.com/#CoreLibraries/DevExpressXtraPrintingBarCodeQRCodeVersionEnumtopic)**

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** QRCode

falsefalse

**Status:** Finalizado

false

**Data:** 10/10/2017

false

**Autores:**
