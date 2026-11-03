---
article_id: 29123914080279
category: Financeiro - Conciliador Backoffice
content_hash: a6eeeb43eabb5758a2877af46f9a71a5c45a6e4f52411144143512d6c91e46de
fetched_at: '2026-06-28T22:37:47.104232+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - CTBA940 - Não aparece RA, PA
  e NCC na nova Conciliação Backoffice
type: support-article
updated_at: '2026-01-08T12:20:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29123914080279-Cross-Segmentos-Backoffice-Linha-Protheus-CTBA940-N%C3%A3o-aparece-RA-PA-e-NCC-na-nova-Concilia%C3%A7%C3%A3o-Backoffice
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29123914062615) Tempo aproximado para leitura: **00:05 min**  
  
**Ocorrência**  
Registros do tipo RA, PA e NCC não aparecem no novo Conciliador Backoffice, o que fazer?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - 12.1.2210  
  
  
**Solução**  
Para que os títulos de adiantamento gerem a movimentação bancária necessária (tabela FK5) e sejam listados no Conciliador Backoffice (CTBA940), é fundamental observar a configuração do parâmetro de baixa.

Para que seja exibido nessa nova rotina, é necessário que ele **movimente banco**, ou seja, que possua o preenchimento do **cheque de adiantamento** com movimentação bancária ativa.  
   
Essas informações podem ser visualizadas diretamente pelo **F12** na rotina, durante inclusões ou baixas:

![image (5).png](https://centraldeatendimento.totvs.com/hc/article_attachments/37527045895831)

Nesse cenário, o título gera o registro imediato na tabela FK5, e, após a conclusão do processo, será possível visualização via CTBA940 (conciliador backoffice).

**Saiba mais**

[Cross Segmento Protheus - Backoffice Linha Protheus - SIGAFIN - Quais os modos de inclusão de PA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004726827-Cross-Segmento-Protheus-Backoffice-Linha-Protheus-SIGAFIN-Quais-os-modos-de-inclus%C3%A3o-de-PA)
