---
article_id: 18702937314711
category: Comércio Exterior - Easy Export Control - Embarque
content_hash: 3ba5b15465791084b299745df597c390f242bbfec6ae1a304f334170ac92a030
fetched_at: '2026-06-28T22:36:56.578184+00:00'
product: protheus
section_id: 1500001549322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Integração campo
  E1_Hist do embarque para o financeiro
type: support-article
updated_at: '2023-11-08T19:39:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18702937314711-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Integra%C3%A7%C3%A3o-campo-E1-Hist-do-embarque-para-o-financeiro
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18702976351767)*Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**De onde é buscado os dados da capa do embarque no **SIGAEEC** para gravar o  histórico no campo **E1\_HIST (Financeiro)**?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Export Control* – A partir da versão 12.1.2210.

**Solução**

Referente à passagem de informação da capa de embarque do **SIGAEEC** para o campo **"E1\_HIST"** no contas a pagar(módulo Financeiro), o campo histórico será sempre preenchido pela informação vinda de **"EEC\_PREEMB"**(no embarque) e **"EEQ\_PREEMB"**(valor das parcelas do embarque).

Assim como, é possível também customizar a informação do campo via fontes "**.AHU**".

**Saiba mais**

[Substituir os arquivos XML do easylink por recursos no repositório](https://tdn.totvs.com/pages/releaseview.action?pageId=715827102)

[Migração dos arquivos XML do EasyLink por recursos no repositório - Linha Microsiga Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=715825853)
