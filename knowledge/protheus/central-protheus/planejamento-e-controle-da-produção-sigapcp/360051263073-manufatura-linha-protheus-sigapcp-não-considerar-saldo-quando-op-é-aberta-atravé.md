---
article_id: 360051263073
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: bb428ff24eefec74e72cb2a93aa24fc9df0b922d7700a48780e6f5a8262f3875
fetched_at: '2026-06-28T22:42:44.573606+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Não considerar saldo quando OP é aberta
  através do pedido de venda
type: support-article
updated_at: '2023-12-19T17:57:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051263073-Manufatura-Linha-Protheus-SIGAPCP-N%C3%A3o-considerar-saldo-quando-OP-%C3%A9-aberta-atrav%C3%A9s-do-pedido-de-venda
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:50 min**  
**Dúvida**Como fazer para não considerar o saldo em estoque quando a **OP - Ordem de Produção** é aberta por pedido de venda?  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Para que sempre abra a **OP** por vendas, independente do saldo é necessário configurar os parâmetros:

* **Considerar Armazém Padrão?** igual a **Não**
* **Cons. Saldos de Armazéns?** igual a **Não**

Desta forma o Sistema não irá consultar o saldo em nenhum armazém e serão abertas as **OPs**.  
  
Ou ainda pode desativar o parâmetro **MV\_CONSEST - Considera estoque na geração de Ordem de produção**. **Importante**Se desativar o parâmetro **MV\_CONSEST** terá impactos em outras situações, exemplo abertura de solicitação de compra automática ou a abertura da **OP** **intermediária**.
