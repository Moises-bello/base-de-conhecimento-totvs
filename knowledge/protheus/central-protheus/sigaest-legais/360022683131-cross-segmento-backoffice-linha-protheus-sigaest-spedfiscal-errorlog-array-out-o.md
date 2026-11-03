---
article_id: 360022683131
category: SIGAEST - LEGAIS
content_hash: e7ca78a524055a47679e19d07d67a2b7c005479ba9a19be6da9b1b3def2f096c
fetched_at: '2026-06-28T22:38:51.517669+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - SPEDFISCAL - Error.log
  "Array out of bounds ( 1 of 0 ) on BLOCOK(SPEDXFUN.PRW)"
type: support-article
updated_at: '2026-01-20T12:14:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022683131-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-SPEDFISCAL-Error-log-Array-out-of-bounds-1-of-0-on-BLOCOK-SPEDXFUN-PRW
---

**Ocorrência**  
Ao gerar o SPEDFISCAL com a opção **Bloco K = Sim** ocorre o erro "Array out of bounds ( 1 of 0 ) on BLOCOK(SPEDXFUN.PRW)".   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**

Este error.log ocorre por falta de registro na base. Abaixo segue exemplo desse erro:

Pesquisar no erro a opção: **COD\_PART(C)**

K\_K200\_SC671200; Rdd:SQLITE; Alias:K200\_SC671200; Filter :; Recno:4; Total Recs:6; Order:0

Index (0) :k200\_sc6712001 FILIAL+DTOS(DT\_EST)+COD\_ITEM+IND\_EST+COD\_PART  
Field 1: FILIAL(C) :0101  
Field 2: REG(C) :K200  
Field 3: DT\_EST(D) :2018/05/31  
Field 4: COD\_ITEM(C) :800500300304   
Field 5: QTD(N) :120  
Field 6: IND\_EST(C) :2  
**Field 7: COD\_PART(C): SA20131350007**Fornecedor - 013135 Loja: 0007

O mesmo pode ocorrer também na SA1:

**Field 7: COD\_PART(C): SA10131350007**Cliente - 013135 Loja: 0007

**Solução**

Para solucionar essa inconsistência, é necessário existir o Cliente ou Fornecedor em sua tabela SA1 ou SA2, respectivamente.

Após incluir o cliente/loja ou fornecedor/loja, não vai mais gerar esse error.log em sua base.

**Caso já exista o cliente e ou fornecedor**

- Validar se o **campo B6\_TPCF** esta devidamente preenchido com C ou F;

- Caso não esteja informado, esta é a causa do problema, pois essa campo deve estar preenchido (neste caso, validar se houve alguma manipulação na base de dados, bem como drop e append ou alguma alteração).

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Legais/Fiscais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)
