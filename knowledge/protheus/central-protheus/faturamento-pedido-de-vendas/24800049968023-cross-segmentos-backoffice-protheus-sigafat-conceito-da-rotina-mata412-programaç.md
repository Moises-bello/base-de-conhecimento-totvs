---
article_id: 24800049968023
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: e4f40e39d6152cdd1263f88a5246e7b83781ba1e3fd3fbdf8a00d21ddb050b14
fetched_at: '2026-06-28T22:38:39.747170+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Conceito da rotina "MATA412
  - Programação de entregas"
type: support-article
updated_at: '2024-07-11T11:32:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24800049968023-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Conceito-da-rotina-MATA412-Programa%C3%A7%C3%A3o-de-entregas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24800034155671) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Qual o conceito da rotina "MATA412 - Programação de entregas"?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Permite que fornecedores possam atender aos parceiros, a quantidade ao pedido que deve ser entregue, conforme a programação solicitada pelo cliente. Dessa forma, são viabilizadas as seguintes situações:

* Os parceiros podem enviar pedidos com produtos previstos e indicar uma previsão de compra junto ao fornecedor.
* O pedido do cliente possa ser entregue em datas e horários específicos, conforme sua necessidade.
* Receber os pedidos de clientes por meios eletrônicos, utilizando troca de mensagens XML, para gerar automaticamente a entrega programada.
* Facilita o controle de vendas futuras, previstas ou firmes, permitindo otimizar o planejamento de compra de produtos acabados ou insumos para produção através da integração entre a programação de entrega e o pedido de venda.

Uma Programação de Entrega pode ter itens previstos para o fornecedor poder se preparar para atender futuramente ou itens firmes, que devem ser entregues em data e hora específica, conforme instruções do cliente.

Quando o cliente confirmar parcialmente um item previsto, é gerado um novo item na quantidade confirmada com status Firme e o item existente com status Previsto terá sua quantidade subtraída da quantidade confirmada.

**Exemplo:**

O cliente envia uma mensagem com um produto previsto na quantidade de 1000 unidades, criando uma programação de 1000 itens desse produto com status Previsto e, posteriormente, envia uma mensagem de confirmação de 500 unidades. O produto é desmembrado em dois itens com quantidade de 500 unidades: um com status Previsto e outro com status Firme.

A Programação de Entrega gera um Pedido de Venda, sem a necessidade de redigitação de dados e, após ela ser gravada, é necessário utilizar a opção Gerar Pedido de Venda. A geração é manual, pois, os dados recebidos eletronicamente não possuem a condição de pagamento e a TES obrigatórios para o Pedido de Venda e, portanto, devem ser inseridos manualmente. A opção Inserir TES permite definir uma TES para todos os itens de uma única vez.

O Pedido de Venda é gerado com um item para cada produto em cada data e hora de entrega, portanto, se a Programação de Entrega tiver o mesmo produto em datas diferentes, são gerados um item para cada data de entrega do mesmo produto. A mesma regra vale para o status, onde é gerado um item para previstos e um para firmes.

Os itens da Programação de Entrega podem gerar vários itens no pedido, conforme seu status e data de entrega, porém, o faturamento deles não pode ser parcial.

Pedidos de Venda gerados pela Programação de Entrega com itens previstos não podem ser desbloqueados por estoque para evitar que haja empenho no controle de estoque, assim, o item constará apenas como previsão no controle de saldos do produto.

Na geração do Documento de Saída, o filtro para os itens pode ser por data de entrega do item, pois, isso, facilita a busca dos itens com entrega programada em datas específicas, sendo que, apenas os pedidos firmes podem ser faturados.

As tabelas SD0 e SDX armazenam o cabeçalho (identificação do pedido recebido do cliente) e os itens (dados dos produtos solicitados) da Entrega Programada, respectivamente.

O TOTVS Colaboração insere dados automáticos na rotina MATA412, mas nada impede de ser manualmente inserido registros nessas rotinas sem a integração.

**Saiba mais:**

* [Programação de Entrega (MATA412 - SIGAFAT)](https://tdn.totvs.com/x/VZ3aFQ)
* [Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT- Configuração e Orientações sobre TOTVS Colaboração 2.0 - EDI de Venda](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026742453-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Configura%C3%A7%C3%A3o-e-Orienta%C3%A7%C3%B5es-sobre-TOTVS-Colabora%C3%A7%C3%A3o-2-0-EDI-de-Vendas?source=search)s
