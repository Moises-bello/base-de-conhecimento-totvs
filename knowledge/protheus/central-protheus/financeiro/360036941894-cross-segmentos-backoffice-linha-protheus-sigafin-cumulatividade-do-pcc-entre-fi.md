---
article_id: 360036941894
category: Financeiro
content_hash: 3fd1658d566e7a98e70d100dbc933386edb1128eed07e4133b817d8c6d744a2a
fetched_at: '2026-06-28T22:38:00.969856+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Cumulatividade do PCC
  entre filiais
type: support-article
updated_at: '2022-06-15T02:11:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036941894-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Cumulatividade-do-PCC-entre-filiais
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Como acumular o PCC de títulos que estão em diferentes filiais ?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

Deve-se respeitar as seguintes parametrizações:

* **Contas a Receber:**

**PCC Emissão**  
MV\_BR10925 = 2  
MV\_PCCAGCL = ( 1 - Não aglutina; 2 - Aglutina pelo mesmo CNPJ/CPF; 3 - Aglutina pela mesma raiz CNPJ. ) \* Cliente  
MV\_PCCAGFL = ( 1 - Não aglutina; 2 - Aglutina pelo mesmo CNPJ/CPF; 3 - Aglutina pela mesma raiz CNPJ. ) \* Filial

**PCC Baixa**  
MV\_BR10925 = 1  
MV\_PCCAGCL = ( 1 - Não aglutina; 2 - Aglutina pelo mesmo CNPJ/CPF; 3 - Aglutina pela mesma raiz CNPJ. ) \* Cliente  
MV\_PCCAGFL = ( 1 - Não aglutina; 2 - Aglutina pelo mesmo CNPJ/CPF; 3 - Aglutina pela mesma raiz CNPJ. ) \* Filial  
MV\_CONSFIL = .T.

* **Contas a Pagar:**

**PCC Emissão**

MV\_BX10925 = 2  
MV\_PCCAGFR = ( 1 - Não aglutina; 2 - Aglutina pelo mesmo CNPJ/CPF; 3 - Aglutina pela mesma raiz CNPJ. ) \* Fornecedor  
MV\_PCCAGFL = ( 1 - Não aglutina; 2 - Aglutina pelo mesmo CNPJ/CPF; 3 - Aglutina pela mesma raiz CNPJ. ) \* Filial

**PCC Baixa**

MV\_BX10925 = 1  
MV\_PCCAGFR = ( 1 - Não aglutina; 2 - Aglutina pelo mesmo CNPJ/CPF; 3 - Aglutina pela mesma raiz CNPJ. ) \* Fornecedor  
MV\_PCCAGFL = ( 1 - Não aglutina; 2 - Aglutina pelo mesmo CNPJ/CPF; 3 - Aglutina pela mesma raiz CNPJ. ) \* Filial  
MV\_CONSFIL = .T.
