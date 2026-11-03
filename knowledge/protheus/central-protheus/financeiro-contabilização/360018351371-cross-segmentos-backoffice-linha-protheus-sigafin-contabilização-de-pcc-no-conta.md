---
article_id: 360018351371
category: Financeiro - Contabilização
content_hash: 52ccf33603898f2b12cbc77c5a2f93fc752eec2eee3f798422cb68c48fca1c90
fetched_at: '2026-06-28T22:38:05.311794+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Contabilização de PCC
  no contas a receber com a LP 520
type: support-article
updated_at: '2022-07-29T03:04:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018351371-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Contabiliza%C3%A7%C3%A3o-de-PCC-no-contas-a-receber-com-a-LP-520
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como contabilizar **PCC** com o parâmetro **MV\_BR10925**na baixa ou na emissão utilizando a **LP 520**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

1ª opção: Se o parâmetro **MV\_BR10925** = 2 (**Na Emissão**), utilize os campos **E1\_PIS**, **E1\_COFINS** e **E1\_CSLL** para contabilização.

2ª opção: Se o parâmetro **MV\_BR10925** = 1 (**Na Baixa**), utilize os campos **E5\_VRETPIS**, **E5\_VRETCOF** e **E5\_VRETCSL** para contabilização e neste caso, será contabilizado tanto valor integral, quanto proporcional.  
  
**Importante:**  
Para que a contabilização ocorra de forma proporcional, será necessário que um analista inloco crie a regra de contabilização, por tratar-se de uma necessidade do negócio, alinhada em conjunto com um consultor Contábil, não faz parte do escopo do Suporte Técnico.
