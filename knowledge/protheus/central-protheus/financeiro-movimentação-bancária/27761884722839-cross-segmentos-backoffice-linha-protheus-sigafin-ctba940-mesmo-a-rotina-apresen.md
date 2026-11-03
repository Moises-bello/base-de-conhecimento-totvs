---
article_id: 27761884722839
category: Financeiro - Movimentação Bancária
content_hash: f187f2ef01819baa0eba823c5ae02c9e8e9f321e9c2bcf337e47e0f56e73f0e9
fetched_at: '2026-06-28T22:38:19.461149+00:00'
product: protheus
section_id: 1500001550402
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Mesmo a rotina
  apresentando erro ao importar arquivo, está sendo alimentado a tabela SIG
type: support-article
updated_at: '2024-11-19T12:48:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27761884722839-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Mesmo-a-rotina-apresentando-erro-ao-importar-arquivo-est%C3%A1-sendo-alimentado-a-tabela-SIG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27761884715543) Tempo aproximado para leitura: **00****:08:00 min** **Dúvida**

Mesmo a rotina apresentando erro ao importar arquivo, está sendo alimentado a tabela SIG  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Caso a rotina automática não registrar o erro nas tabelas **SIF/SIG**, o usuário não teria como saber que houve um erro. Gravar o erro nessas tabelas permite que essa informação fique visível para ele na rotina **FINA474** depois que o **JOB** é executado.  
  
Já no conciliador (**CTBA940**), o usuário consegue marcar esses registros e mandar ignorar.  
  
Esse ponto se encontra documentado no link abaixo:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=747320567>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27761867615895)

Caso deseje um comportamento diferente do atual, é necessário solicitar uma melhoria por meio de nossa central colaborativa.
