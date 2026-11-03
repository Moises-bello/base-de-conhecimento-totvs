---
article_id: 28234633325207
category: Materiais - Compras (SIGACOM)
content_hash: e037692e96b91c4c98db332c898c00741039ec5529c75131afa8154f01b1dca2
fetched_at: '2026-06-28T22:41:22.127130+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ponto de Pedido  não
  Agrupa Fornecedor
type: support-article
updated_at: '2024-12-03T12:13:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28234633325207-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ponto-de-Pedido-n%C3%A3o-Agrupa-Fornecedor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28234633309591) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Ao utilizar a rotina Ponto de Pedido, quando selecionamos a opção Gera Documento, o sitema não esta agrupando os produtos por fornecedor.  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12  
  
**Solução**

Para agrupar os pedidos por fornecedor, é importante seguir os seguintes passos:

1. Se for utilizada a opção para gerar Pedido de Compras na rotina MATA170, é necessário realizar a amarração entre Produto e Fornecedor na rotina MATA061, além de vincular uma condição de pagamento no cadastro do fornecedor.
2. Caso haja mais de um fornecedor no Cadastro do Produto x Fornecedor, o sistema selecionará automaticamente o fornecedor com a maior Nota para a geração do pedido.
3. Se o produto estiver associado a um Contrato de Parceria, os pedidos não serão agrupados

**Saiba mais em :**

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como é realizado o cálculo de necessidade na rotina Ponto de Pedido?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27256450694935-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-%C3%A9-realizado-o-c%C3%A1lculo-de-necessidade-na-rotina-Ponto-de-Pedido)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Não está considerando Solicitação de Compras bloqueadas para o cálculo da necessidade na Rotina de solicitação de Compras por Ponto de Pedido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27310881678615-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-N%C3%A3o-est%C3%A1-considerando-Solicita%C3%A7%C3%A3o-de-Compras-bloqueadas-para-o-c%C3%A1lculo-da-necessidade-na-Rotina-de-solicita%C3%A7%C3%A3o-de-Compras-por-Ponto-de-Pedido)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
