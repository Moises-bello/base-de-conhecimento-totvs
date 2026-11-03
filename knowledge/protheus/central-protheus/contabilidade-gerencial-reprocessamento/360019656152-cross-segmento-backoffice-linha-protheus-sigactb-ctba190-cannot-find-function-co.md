---
article_id: 360019656152
category: Contabilidade Gerencial - Reprocessamento
content_hash: 8dbe03d0889696d5c6eb94bdf5711e4faabc51c042019ee2ee5701138c02f411
fetched_at: '2026-06-28T22:40:41.917681+00:00'
product: protheus
section_id: 1500001548742
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA190 cannot find
  function CONA080 '
type: support-article
updated_at: '2023-11-13T16:00:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019656152-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA190-cannot-find-function-CONA080
---

**Ocorrência**

Ao rodar reprocessamento apresenta erro: **cannot find function CONA080**

**Ambiente**Protheus – Contabilidade Gerencial – 12.1.17

**Solução**

A rotina **CONA080**, pertence a o modulo **SIGACON** que foi **descontinuado**. No módulo **SIGACTB,** a rotina responsável pelo reprocessamento contábil é o **CTBA190 - Reprocessamento**

Verifique se rotina esta disponível em seu menu do módulo **SIGACTB**, caso não esteja, realize a troca do menu.  
  
Para maiores informações sobre as alterações no menu, acesse: <http://tdn.totvs.com/pages/viewpage.action?pageId=271164329>
