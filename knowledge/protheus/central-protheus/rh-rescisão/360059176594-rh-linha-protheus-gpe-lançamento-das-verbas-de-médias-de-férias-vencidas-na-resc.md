---
article_id: 360059176594
category: RH - Rescisão
content_hash: 6adff79cf5682ccd02e781e9bf28143e83e9e8e70dcd1f77db08b973d3c6ce90
fetched_at: '2026-06-28T22:43:49.755301+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Lançamento das verbas de médias de férias vencidas
  na rescisão e férias indenizadas Sistema não permite e emite alerta
type: support-article
updated_at: '2025-06-26T11:49:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059176594-RH-Linha-Protheus-GPE-Lan%C3%A7amento-das-verbas-de-m%C3%A9dias-de-f%C3%A9rias-vencidas-na-rescis%C3%A3o-e-f%C3%A9rias-indenizadas-Sistema-n%C3%A3o-permite-e-emite-alerta
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33067314197911)**Tempo aproximado para leitura:**00:02:30 min**

**Ocorrência**Realizado lançamento das verbas de férias indenizadas na rescisão e médias de férias vencidas, Sistema emite alerta: **Atenção! Necessário preencher campo Num. Identif (RGB) com as datas inicial e final do período aquisitivo correspondente à verba lançada, no formato AAAAMMDD-AAAAMMDD para que o lançamento seja impresso corretamente no TRCT. este lançamento deve ser feito pela tela de rescisão**, e impede salvar para prosseguir com cálculo.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101884633)  
 **Ambiente**Protheus - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**Implementada **trava** no Sistema quando **informadas** as verbas com identificador de cálculo **0086 (férias Indenizadas)** e **0248 (Média de Férias Vencidas Rescisão) para que seja informado a qual período aquisitivo referem-se.**

Esta informação é **necessária** para que o **TRCT** (Termo de Rescisão de Contrato de Trabalho) **não** seja impresso com **campo em branco.**  
  
**Solução**Informe no campo **Num. Identif** as datas inicial e final do **período aquisitivo** correspondente à verba lançada, no formato **AAAAMMDD-AAAAMMDD.**

![](https://p23.zdusercontent.com/attachment/888110/Z833SPFEKMUdeouSnUtbF70v4?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..12iRwb6lorSSO7vi81aotA.sPdSX4clrVLbbpd9QkTBPtTV1L_DskR8-XhU6fE16MNysLkfjzA3WBAeSWQav12bjT7BY4LcjaYRN_AjEqTpwWk4y3A-2nPNb9EiIYRRn-J0YDqKrEoliscCZLMdkMfuesTjOuSm3OoVLTWhg-NVpaUYlrN-J5pt86Famv5ZMg_U7HnGRTFZbOwxtzWckuGQmz-moFPCpzrs2bkZeKl0NWoFjKYjWKEArRo5Ww8kCR7lwAJdkbZDvS8HjKVBte5w1eTz_pcM05GjJEnfN8Byv1IrDIV1i476BHVXq0XEAro.iI7q-Ythk08RfdK1MepE3Q)
