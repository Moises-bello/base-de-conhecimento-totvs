---
article_id: 360056876054
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 1eb8b7f57829e4f647f223458bd7ee09123bb4e27fcb3f25d5fa21a1aea6167e
fetched_at: '2026-06-28T22:42:43.592070+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem A380BQTOR
type: support-article
updated_at: '2024-02-27T14:45:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056876054-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-A380BQTOR
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:55 min  
  
Ocorrência**No módulo **Planejamento e Controle da Produção**, ao tentar alterar a quantidade do campo **D4\_QTDEORI - Qtd. Empenho** no **MATA380 - Ajuste de Empenho Simples**ou no **MATA381 - Ajuste de Empenho Múltiplo**é apresentada a mensagem **A380BQTOR**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098879513/mceclip0.png)

**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Causa**  
Essa mensagem ocorre quando a quantidade resultante da subtração dos campos **D4\_QTDEORI - Qtd. Empenho** e **D4\_QUANT - Sal. Empenho** é diferente do mesmo cálculo aplicado na tabela **SD4 - Requisições empenhadas**.  
  
**Solução**  
Para alterar a quantidade do campo **Qtd. Empenho**, obrigatoriamente deve-se manter a diferença entre os valores.  
Exemplo:  
**Qtd. Empenho: 10  
Sal. Empenho: 5**  
Caso ocorra a alteração do campo **Qtd. Empenho** para **20**, o campo **Sal. Empenho** deve ser alterado para **15**.
