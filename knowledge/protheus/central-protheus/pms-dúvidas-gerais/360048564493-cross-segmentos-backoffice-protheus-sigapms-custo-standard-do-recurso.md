---
article_id: 360048564493
category: PMS - Dúvidas Gerais
content_hash: 7ef13043683f009d97266171f195a90f6fb94497fe162601db4bd37688b6df13
fetched_at: '2026-06-28T22:37:17.645854+00:00'
product: protheus
section_id: 1500001539681
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Custo Standard do Recurso
type: support-article
updated_at: '2024-02-26T18:04:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048564493-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Custo-Standard-do-Recurso
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21627360670743)**Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como é preenchido o custo Standard do recurso, localizado na tarefa?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAPMS - A partir da versão 11.80.  
  
**Solução**

O campo Custo Standard (**AFA\_CUSTD** )  menciona o custo unitário do recurso.

Este campo é preenchido de acordo com a informação  do campo **AE8\_VALOR** Valor Unitário do Recurso. O campo está localizado na rotina Cadastro de Recurso (**PMSA050**).

Existem duas maneiras de preencher o valor unitário do produto **AE8\_VALOR**:

1° Manual, ou seja pode inserir no campo o valor unitário do recurso;

2° Preenchimento automático de acordo com o valor cadastrado no produto **B1\_CUSTD**.

Ao inserir o produto no campo **AE8\_PRODUT** Cod. do Produto se este cadastro estiver com o conteúdo do campo Custo Standard preenchido **B1\_CUSTD**, o sistema carrega está informação automática para o **AE8\_VALOR**, que consequentemente alimenta o campo  da tarefa **AFA\_CUSTD**.
