---
article_id: 360027941652
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 856d402aff0ceaf28b14b8681f9d473cb01bbb856bcf86da6602412bea605590
fetched_at: '2026-06-28T22:42:42.142816+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Controlar o produto utilizando potência
type: support-article
updated_at: '2021-10-19T11:02:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027941652-Manufatura-Linha-Protheus-SIGAPCP-Controlar-o-produto-utilizando-pot%C3%AAncia
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:01:50 min****Dúvida**Como realizar o controle de potência no produto? **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Os produtos que utilizam controle de rastreabilidade podem controlar também sua potência por **Lote/Lote + Sublote**. Esse controle permite identificar as características de potência do composto ativo de cada lote de um mesmo produto.Esse tipo de controle é muito utilizado por indústrias do ramo farmacêutico.  
Procedimentos para controlar potência de lote:

* Informe **Sim** no campo **B1\_CPOTENC** **-** **Contr. Potenc**.
* Para toda entrada de saldo desses produtos, que crie um novo **lote** ou **lote + sublote** e informe a respectiva potência.

Nos movimentos em que é informado um **lote/lote + sublote** já existente, a informação da potência é automaticamente informada pelo Sistema. As consultas de lote também apresentam essa informação.  
  
**Exemplo:**  
Uma indústria farmacêutica adquire de um fornecedor A, um quilo de um lote de um determinado composto químico. Neste quilo fornecido, na verdade, somente cinquenta por cento, ou seja, quinhentos gramas do lote são do composto requisitado, e o restante, os outros quinhentos gramas são impurezas. Assim, a potência deste lote é de 50%.  
Já o fornecedor B utiliza outro processo de fabricação e consegue que a potência de seu lote desse mesmo composto químico, seja de 100%, o que significa que, requisitar ao fornecedor B um quilo desse lote corresponde, irá receber exatamente um quilo do composto químico, sem impurezas.  
Com essa informação o Sistema pode calcular quanto ele deve requisitar, dependendo do fornecedor, para obter a quantidade que necessita.  
Se a produção solicitar um quilo deste composto, é preciso requisitar, na verdade, dois quilos do fornecedor A ou um quilo do fornecedor B.
