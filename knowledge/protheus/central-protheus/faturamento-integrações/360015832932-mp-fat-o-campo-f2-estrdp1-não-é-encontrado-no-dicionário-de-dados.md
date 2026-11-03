---
article_id: 360015832932
category: Faturamento - Integrações
content_hash: 87a1d7cf9e36c46d44b218d4d9d2b2ccccc200f06b77096854a3ccaa7665f635
fetched_at: '2026-06-28T22:38:26.583104+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: MP - FAT - O campo F2_ESTRDP1 não é encontrado no dicionário de dados
type: support-article
updated_at: '2021-04-28T15:15:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015832932-MP-FAT-O-campo-F2-ESTRDP1-n%C3%A3o-%C3%A9-encontrado-no-dicion%C3%A1rio-de-dados
---

**Dúvida**

O campo **F2\_ESTRDP1**não é encontrado no dicionário de dados.

**Ambiente**

Microsiga Protheus - a partir da versão 12.

**Solução**

O campo F2\_ESTRDP1 tem por finalidade permitir o uso de múltiplos redespachos na integração do módulo de Faturamento Protheus x GFE (Gestão de Frete Embarcador).

Como já existe o tratamento para o campo no fonte **OMSM011**, neste caso, será necessário criar os  campos relacionados a múltiplos redespachos, seguindo as seguintes características:

**- F2\_REDESP2,F2\_REDESP3,F2\_REDESP4,F2\_REDESP5** com estrutura igual da  **F2\_REDESP**, sendo que o cliente deve atribuir os redespachante necessários;

**- F2\_TFRDP1,F2\_TFRDP2,F2\_TFRDP3,F2\_TFRDP4,F2\_TFRDP5** com estrutura igual a **F2\_TPFRETE**, segue mesmas regras de atribuição do **F2\_TPFRETE** ;

**- F2\_ESTRDP1,F2\_ESTRDP2,F2\_ESTRDP3,F2\_ESTRDP4,F2\_ESTRDP5** com estrutura igual a **A1\_EST**, onde o cliente deve informar o estado de destino do redespacho;

**- F2\_CMURDP1,F2\_CMURDP2,F2\_CMURDP3,F2\_CMURDP4,F2\_CMURDP5** com estrutura igual a **A1\_COD\_MUN**, onde o cliente deve informar o código da cidade de destino do redespacho.

E no ponto **M461LSF2** deverá atribuir o conteúdo dos campos.

**SAIBA MAIS:** **<http://tdn.totvs.com/pages/viewpage.action?pageId=271185194>**

**[FAT0244 - Principais ocorrências da Integração Protheus Faturamento X GFE](http://tdn.totvs.com/pages/viewpage.action?pageId=337359685)**
