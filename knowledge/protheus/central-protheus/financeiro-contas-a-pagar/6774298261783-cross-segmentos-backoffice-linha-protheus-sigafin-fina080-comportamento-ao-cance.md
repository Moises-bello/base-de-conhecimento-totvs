---
article_id: 6774298261783
category: Financeiro - Contas a Pagar
content_hash: 2bb81c9dd04138537941bca5567a022823ec8e5745cf7f2a4c72b609a89a7ee6
fetched_at: '2026-06-28T22:38:08.434941+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus  - SIGAFIN - FINA080 - Comportamento
  ao cancelar baixa de títulos com PCC
type: support-article
updated_at: '2022-06-14T20:24:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6774298261783-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA080-Comportamento-ao-cancelar-baixa-de-t%C3%ADtulos-com-PCC
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:04:00min**

**Dúvida**Sendo o fato gerador do PCC a baixa do título principal, qual é o comportamento do sistema ao cancelar a baixa?  
  
**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) - Financeiro - FINA080- Todas as versões  
  
**Solução**Considerando o processo e comportamento padrão da rotina **FINA080**, caso os títulos **TX** estejam em aberto, a rotina fará a exclusão dos **títulos de impostos** ao cancelar a baixa do **título principal.**

**Importante**Caso exista alguma baixa nos títulos **TX**, não será possível cancelar a baixa do título principal, sendo informado o **HELP : NODELETA.**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6774134069655/mceclip0.png)**
