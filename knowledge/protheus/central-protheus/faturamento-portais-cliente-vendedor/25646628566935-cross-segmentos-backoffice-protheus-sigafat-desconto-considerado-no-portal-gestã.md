---
article_id: 25646628566935
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: 00612607f51629e99f0e932f22708ebf06ec6c0defa2d1ccb1037d6c066c8797
fetched_at: '2026-06-28T22:38:23.928739+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Desconto considerado no Portal
  Gestão de Vendas
type: support-article
updated_at: '2024-08-14T17:14:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25646628566935-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Desconto-considerado-no-Portal-Gest%C3%A3o-de-Vendas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25646628529431) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Desconto considerado no Portal Gestão de Vendas?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.1.33  
  
**Solução**

O **Portal Gestão de Vendas** considera apenas os descontos informados diretamente nos itens (**SC6**), pois não tem no Layout os campos para digitação de descontos (**na solução padrão**) no cabeçalho (**SC5**).

Descontos adicionados no cabeçalho dos **Pedidos de Vendas** diretamente pelo **Protheus não serão calculados** no **Resumo dos Pedidos de Vendas** e não aparecerão no **PDF**. O total dos descontos, tanto dos itens quanto do cabeçalho, só aparecem por completo na função **Planilha Financeira**.

Ao inserir um desconto na linha do item do Pedido de Venda, dependendo do valor o sistema recalcula o valor/percentual de desconto.

Isso ocorre, pois o percentual aplicado sempre será calculado proporcionalmente ao valor do item e à sua quantidade.   
Este proporcional deve ser um valor comportado pelo tamanho de decimais de sua base, pois caso contrário, ocorrerá diferença no cálculo.

Abaixo demonstramos o cálculo realizado pelo sistema para determinar o Valor e o Percentual de desconto nos itens:

**Exemplo**de desconto pretendido incompatível com as decimais em relação à QUANTIDADE:

Quantidade: **218**

Valor Unitário: **10,00**

Desconto Pretendido: **3,96**

Saiba mais: 

[DR - Meus Pedidos](https://tdn.totvs.com/display/public/PROT/DR+-+Meus+Pedidos#DRMeusPedidos-NOVO_PEDIDO)

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Regra de Desconto no PGV](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9859028649239-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Regra-de-Desconto-no-PGV)
