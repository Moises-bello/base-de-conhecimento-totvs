---
article_id: 360028517372
category: NFe - Nota Fiscal Eletrônica
content_hash: 1abc63395f4056ef72c62c65d14028b4e1031bdaeb33fbb3d0b18ab78b2e909a
fetched_at: '2026-06-28T22:40:01.975351+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - variable does
  not exist CESPECIE on U_MT100TOK(MT100TOK.PRW)'
type: support-article
updated_at: '2024-05-16T19:26:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028517372--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-variable-does-not-exist-CESPECIE-on-U-MT100TOK-MT100TOK-PRW
---

**Dúvida**Como corrigir o error.log variable does not exist CESPECIE on U\_MT100TOK(MT100TOK.PRW)  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos

**Solução**

No módulo Faturamento, em NFe Sefaz, ao inutilizar uma nota saltada pelo botão **Inutilização,** ocorre o error log abaixo:

**variable does not exist CESPECIE on U\_MT100TOK**(MT100TOK.PRW) 09/05/2019 15:14:00 line :18

[TOTVS build: 7.00.131227A-20180920 NG]  
Called from U\_MT100TOK(MT100TOK.PRW) 09/05/2019 15:14:00 line : 18  
Called from EXECBLOCK(APLIB190.PRW) 01/03/2019 16:49:26 line : 163  
Called from A920TUDOK(MATA920.PRW) 31/08/2018 10:34:51 line : 1671

Ou

**variable does not exist CFORMUL on U\_MT100TOK**(MT100TOK\_AP5.PRW) 11/12/2017 13:42:49 line : 117

[TOTVS build: 7.00.131227A-20151103]  
Called from EXECBLOCK(APLIB190.PRW) 20/10/2016 15:18:44 line : 161  
Called from A920TUDOK(MATA920.PRW) 12/07/2017 09:14:10 line : 1741

Este incidente é causado por alguma validação que está sendo feita pelo ponto de entrada MT100TOK.  
O botão **Inutilização** não necessita de Ponto de Entrada, ele por si só, envia as informações necessárias sobre a inutilização para a Sefaz.

Caso tenha necessidade em continuar utilizando o PE acima na inutilização, sugerimos que o reavalie.

**Importante:** O botão deve ser usado apenas em situações em que houve um salto na numeração da nota fiscal eletrônica ou quando o número da nota fiscal eletrônica ainda não foi utilizado (não foi registrado nas tabelas SD2, SF2, SFT e SF3). Esse botão é responsável por registrar essas informações nas tabelas e transmitir a invalidação da nota.

Para notas que já foram geradas no sistema, mas não foram transmitidas ou foram rejeitadas pela Sefaz, é possível cancelar e retransmitir a nota como se fosse uma transmissão normal.
