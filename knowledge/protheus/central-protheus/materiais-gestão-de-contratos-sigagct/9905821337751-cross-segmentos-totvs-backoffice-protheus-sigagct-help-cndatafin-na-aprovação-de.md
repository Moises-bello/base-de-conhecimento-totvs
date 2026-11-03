---
article_id: 9905821337751
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: c956ebe03b58567af22bfff084e04cfca91674ca14351192671bac144410c27e
fetched_at: '2026-06-28T22:37:22.979446+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - HELP: CNDATAFIN na
  Aprovação de Revisões em Contratos ou ao Tornar o Contrato Vigente'
type: support-article
updated_at: '2025-04-17T18:53:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9905821337751-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-HELP-CNDATAFIN-na-Aprova%C3%A7%C3%A3o-de-Revis%C3%B5es-em-Contratos-ou-ao-Tornar-o-Contrato-Vigente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31492355237143) Tempo aproximado para leitura**00:05:00 min****Ocorrência**

HELP: CNDATAFIN na aprovação de Revisões em Contratos ou ao Tornar o Contrato Vigente

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9905359787031)  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - A partir da Versão 12.  
  
**Causa**

* O sistema só realiza a validação do parâmetro **MV\_DATAFIN** em cenários que serão gerados títulos provisórios no financeiro, ou seja, quando o contrato tem cronograma financeiro (**CNF**) e o parâmetro **MV\_CNPROVI** está ativo.
* O Help ocorre quando a Data do parâmetro **MV\_DATAFIN** é maior que a data de vencimento (**CNF\_DTVENC**) das parcelas em aberto que ainda não tenham sofrido medição, ou seja, parcela com o campo **CNF\_VLREAL** igual zero.

**Solução**  
Para solucionar essa ocorrência, pode utilizar umas das alternativas abaixo:  
1. Ajustar a Data do parâmetro **MV\_DATAFIN** para uma Data Menor o igual que a Data de Vencimento das parcelas do Cronograma (**CNF\_DTVENC)** que não sofreram medição.

2. Ajustar a data de vencimento das respectivas parcelas do cronograma (**CNF\_DTVENC)**, para uma data posterior a data informada no **MV\_DATAFIN** através dos tipos de revisão:  **Realinhamento, Renovação, Aditivo e/ou Aberta,** ou na alteração do contrato que ainda não se tornou **Vigente**

***Saiba Mais:***

[14535580 DMANMAT02-38809 DT Sistema permite aprovar alçada de revisão indevidamente](https://tdn.totvs.com/pages/releaseview.action?pageId=696692487)

[14667603 DMANMAT02-39634 DT Conflito com parâmetro MV\_DATAFIN em contratos antigos](https://tdn.totvs.com/x/N9JAKg)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Quais são os tipos de Revisão disponíveis, para revisar contratos no Gestão de Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034587334-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Quais-s%C3%A3o-os-tipos-de-Revis%C3%A3o-dispon%C3%ADveis-para-revisar-contratos-no-Gest%C3%A3o-de-Contratos-?source=search)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como desativar a geração de títulos provisórios na mudança de situação do contrato ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018381871-MP-GCT-Como-desativar-a-gera%C3%A7%C3%A3o-de-t%C3%ADtulos-provis%C3%B3rios-na-mudan%C3%A7a-de-situa%C3%A7%C3%A3o-do-contrato)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
