---
article_id: 38769642972311
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 31e1d89057dbabe12173d1af27e1313371e12dc7cbbf145d76f1de4d53bd205f
fetched_at: '2026-06-28T22:38:58.536549+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento – Backoffice (Linha Protheus) – SIGAEST – Obrigatoriedade de
  Lote em Movimentações e Pedidos de Venda
type: support-article
updated_at: '2026-03-03T16:53:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38769642972311-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Obrigatoriedade-de-Lote-em-Movimenta%C3%A7%C3%B5es-e-Pedidos-de-Venda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38769610302487) Tempo aproximado para leitura: 00**:01:00 min**  
  
**Dúvida**  
Por que o sistema exige a informação de lote nos produtos de saída/origem nas rotinas de Movimentações e Pedidos de Venda?  
Existe parâmetro para desativar essa obrigatoriedade?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Estoque Custos - Todas as versões  
  
**Solução**  
Nas rotinas de **Movimentações** e **Pedidos de Venda**, quando o produto está configurado para **controle de lote**, o sistema torna obrigatória a informação do lote nos movimentos de **saída/origem**.

Essa exigência ocorre porque, em operações de saída, é necessário identificar exatamente qual lote está sendo baixado do estoque, garantindo a rastreabilidade e a consistência das informações.

Caso o lote não seja informado no produto de origem, o sistema apresenta a seguinte mensagem:

> **Help: LOTECTOBR**  
> **Problema:** Quando o produto utiliza controle de Rastro, deve ter preenchido no movimento o campo Lote do produto.  
> **Solução:** Preencher o campo de Lote no Movimento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38769610303767)

Já nos movimentos de **destino**, a informação do lote não é obrigatória. Quando não informada, o sistema realiza a geração automática de um lote.

**Importante:**  
Não existe parâmetro no sistema que permita desativar a obrigatoriedade de informar o lote nos produtos de saída/origem quando o controle de lote estiver ativo.

Quando o lote não é informado no produto de origem, o sistema apresenta mensagem de bloqueio, conforme exemplo disponível no help do sistema.

**Saiba mais:**  
[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
