---
article_id: 360025448734
category: Materiais - Compras (SIGACOM)
content_hash: 14a11d875cff7a0187f2e6e16de6750d60e7cf82af3a49a295be0bfafb0bc651
fetched_at: '2026-06-28T22:41:20.221227+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Multlock da tabela
  SA2 na classificação do Documento de Entrada
type: support-article
updated_at: '2022-05-18T21:04:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025448734-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Multlock-da-tabela-SA2-na-classifica%C3%A7%C3%A3o-do-Documento-de-Entrada
---

**Dúvida**

Multlock da tabela SA2 na classificação do Documento de Entrada

**Ambiente**

Protheus – Compras – A partir da versão 12  
  
**Solução**

Ao classificar Documento diferente com usuários distintos, mas que possuem o mesmo fornecedor e loja, o sistema apresenta alerta de *Multlock* relacionado a tabela **SA2** (fornecedor).

Exemplo de cenário para apresentar o alerta:

**Documento:** 07061807 **série:** 019

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040254833/mceclip0.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039417654/mceclip2.png)

**Documento:** 07061808 **série:** 019

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040254953/mceclip1.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039417794/mceclip3.png)

**Alerta:** MultLock

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039418694/mceclip4.png)

Em ambientes com alto volume de movimentações, poderá ocorrer situações em que uma rotina reserva o registro do fornecedor na tabela **SA2** para realizar a atualização, e quando uma segunda rotina tenta reservar o mesmo registro dispara o alerta de *“MultLock”*. Este tipo de situação pode ocorrer no sistema e se trata de uma característica, levando em consideração que a atualização dos dados na tabela **SA2** ocorre de maneira *on-line*.

Para atenuar as situações de concorrência entre processos que atualizam a tabela **SA2** existe o parâmetro **MV\_ATUFORN.**

Conteúdos:

**.T.** = O cadastro do fornecedor será atualizado ao realizar movimentações financeiras (*default*)  
**.F.** = O cadastro do fornecedor deixará de ser atualizado ao realizar uma movimentação financeira

**Observação:**

* Caso o parâmetro não existir, será realizada a atualização do cadastro do fornecedor normalmente.
* A chamada do ponto de entrada **MT103TRV** neste processo para a tabela **SA2** foi descontinuada na função **A050DupPag (FINXFIN.PRX)** e substituída pelo tratamento através desse parâmetro, já que teriam o mesmo propósito. Para as outras tabelas o Ponto de Entrada continua funcional.
* IMPORTANTE: O Ponto de Entrada MT103TRV continua funcional para a tabela SB2.
