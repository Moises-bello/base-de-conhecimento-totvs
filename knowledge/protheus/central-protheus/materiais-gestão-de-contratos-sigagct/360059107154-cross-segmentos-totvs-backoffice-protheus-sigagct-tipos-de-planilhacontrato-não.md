---
article_id: 360059107154
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: e84b70eeeb3707a5df018f1f8eeb4a79403606a6c2957d3a11c3907f22e0edca
fetched_at: '2026-06-28T22:37:24.169032+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Tipos de Planilha/Contrato
  não aparecem na Inclusão de um Contrato no Dashboard de Contratos ( CNTA330 )
type: support-article
updated_at: '2025-02-11T13:23:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059107154-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Tipos-de-Planilha-Contrato-n%C3%A3o-aparecem-na-Inclus%C3%A3o-de-um-Contrato-no-Dashboard-de-Contratos-CNTA330
---

**Dúvida:**

O que fazer quando não aparecer os Tipos de Planilha ou Tipos de Contrato na Inclusão de um Contrato no Dashboard ( CNTA330 ) de Contratos ?

**Ambiente:**Protheus – Gestão de Contratos  – A partir da versão 12

**Causa:**No Protheus está cadastrado os Tipos de Planilha e Tipos de Contratos, mas na Inclusão do Contrato através do Dashboard/Portal de Contratos (CNTA330) não está aparecendo Tipos de Planilhas/Contratos para Seleção.

Alguns Tipos de de Planilhas/Contrato não irão aparecer para seleção, pois, não são todos os Tipos de Planilha/Contratos que são suportadas na Inclusão de Contrato atravás do Dashboard de Contratos.

**Solução:**

Dessa forma orienta-se o cadastramento de um Tipo de Planilha/Contrato conforme as configurações abaixo para que possa ser utilizado na Inclusão do Contrato no Dashboard:

* CNL\_MEDEVE/CN1\_MEDEVE = 2 (Medição Eventual = Não);
* CNL\_MEDEVE/CN1\_MEDEVE = 1 (Medição Eventual = Sim) e CNL\_CTRFIX/CN1\_CTRFIX = 1 ou 2 (Planilha/Contrato Fixo = Sim ou Não);
* CNL\_CROCTB/CN1\_CROCTB = 2 (Cronograma contábil = Não);
* CNL\_CROFIS/CN1\_CROFIS = 2 (Cronograma físico = Não);
* CNL\_PLSERV = 2 (Planilha de serviço = Não);

***Saiba Mais:***

[5 - Elaboração e Edição de Contrato](https://tdn.totvs.com/pages/releaseview.action?pageId=507008434)

[22134710 DTEXPRO-4857 DT Exibição de Tipos de Contrato suportados pelo Dashboard](https://tdn.totvs.com/x/EiEkNg) 

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
