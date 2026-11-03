---
article_id: 36941159586455
category: Contabilidade Gerencial - Conciliador BackOffice
content_hash: 4fb1e37ff2fcf8a7a420762cc96037214c74490e589ce5c3088ee890a2152b21
fetched_at: '2026-06-28T22:40:31.016778+00:00'
product: protheus
section_id: 31314114896791
source: central-protheus
title: Cross Segmentos - Linha Backoffice Protheus - CTBA940 - Tela em branco do conciliador
type: support-article
updated_at: '2025-12-11T13:27:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36941159586455-Cross-Segmentos-Linha-Backoffice-Protheus-CTBA940-Tela-em-branco-do-conciliador
---

**Dúvida**  
Ao acessar a rotina de conciliação no Protheus, o sistema esta apresentando "três pontinhos" mantendo a tela em branco, a tela não abre e não apresenta informações.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial- A partir da release 12.1.2210  
  
**Solução:**  
Este erro de tela em branco em rotinas POUI normalmente ocorre devido à **incompatibilidade dos arquivos temporários utilizados na composição do front da rotina.**

Este incidente ocorre normalmente devido à:

1- A**tualizações do ambiente, assim verifique se o sistema está totalmente atualizado conforme portal do cliente:**

[Webapp](https://suporte.totvs.com/portal/p/10098/download?e=1168455#all/all/all/search/webapp)

[LIB](https://suporte.totvs.com/portal/p/10098/download?e=1168455#000006/368/TFLIB/)

[Appserver](https://suporte.totvs.com/portal/p/10098/download?e=1168455#000006/368/TFAPP/)

[Central de Atualizações](https://tdn.totvs.com/pages/releaseview.action?pageId=532651679)

2- I**ncompatibilidade dos arquivos temporários utilizados na composição do front da rotina** efetuado pela leitura dos dados na pasta **http-root** localizada na **Protheus\_data.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/36941159573527)**

Entre na sua pasta protheus\_data e**renomeie ou exclua** a pasta http-root, podendo deixar como http-hoot-bkp,

 Reinicie todos os serviços do **Protheus**. Após a reinicialização, acesse novamente o **Conciliador Backoffice  (CTBA940).**

**Saiba mais:**

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - Erro HTTP ao acessar novas rotinas PO-UI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11535166755095-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Erro-HTTP-ao-acessar-novas-rotinas-PO-UI)
