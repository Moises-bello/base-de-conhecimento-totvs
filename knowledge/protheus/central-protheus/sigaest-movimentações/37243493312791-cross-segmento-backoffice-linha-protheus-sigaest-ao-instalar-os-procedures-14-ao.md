---
article_id: 37243493312791
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 929ffe54140e5e46f7d56dc0e6652d70d9668dd6bce484df6724e98fa06753b1
fetched_at: '2026-06-28T22:38:53.891485+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Ao instalar os Procedures
  14 ao 18 é gerado erro: "Invalid column name ''IS_ACTIVE" e "É necessário declarar
  a variável escalar "@vcTPDCENV2".'
type: support-article
updated_at: '2026-01-27T13:52:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37243493312791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Ao-instalar-os-Procedures-14-ao-18-%C3%A9-gerado-erro-Invalid-column-name-IS-ACTIVE-e-%C3%89-necess%C3%A1rio-declarar-a-vari%C3%A1vel-escalar-vcTPDCENV2
---

Ao instalar as procedures do estoque da versão 14 à 18 no TOTVS Protheus, ocorre erro "Invalid column name 'IS\_ACTIVE'" e falta da variável "@vcTPDCENV2". A solução é aplicar a atualização correspondente à versão (12.1.2210, 12.1.2310, 12.1.2410 ou 12.1.2510) e reinstalar as procedures. Links para as atualizações estão disponíveis no artigo.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37243502540439) Tempo aproximado para leitura: 00**:01:00 min**  
  
**Ocorrência**  
Ao instalar os Procedures do estoque da 14 ao 18 é gerado erro:

**"Invalid column name 'IS\_ACTIVE"**

"**É necessário declarar a variável escalar "@vcTPDCENV2".**

**"Must declare the scalar variable "@vcTPDCENV2""**

Caso o cliente utilize banco Oracle apresentará o seguinte cabeçalho no erro:

**Error : 24344 - ORA-24344: success with compilation error**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Para resolver o erro da instalação das procedures é necessário aplicar a seguinte atualização e depois reinstalar:

12.1.2210:<https://r.totvs.io/p/1230883> ;

12.1.2310:<https://r.totvs.io/p/1230881> ;

12.1.2410:<https://r.totvs.io/p/1230880> ;

12.1.2510:<https://r.totvs.io/p/1230882> ;

Issue: [DMANMAT01-47031](https://tdn.totvs.com/x/M7gbPQ)

### **Após atualização, reinstale as procedures conforme esse boletim:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Procedure Desatualizada ou Incompatível](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-ou-Incompat%C3%ADvel)

***Saiba mais:***

[*Clique aqui e acesse mais artigos sobre Movimentação no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
