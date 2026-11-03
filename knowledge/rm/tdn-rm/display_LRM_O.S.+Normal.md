---
content_hash: c44f0fe391d085e4d6e236c30fef1393329d3bae31d16bc062883f49d0f9175e
fetched_at: '2026-06-29T00:09:26.740195+00:00'
page_id: '423938398'
product: rm
source: tdn-rm
title: O.S. Normal
type: documentation
url: https://tdn.totvs.com/display/LRM/O.S.+Normal
version: 4
---

Ordem de serviço (OS) é um documento através do qual são expedidos serviços a serem executados, sejam eles na manutenção de um objeto que necessite de reparos em uma oficina mecânica ou em uma prestação de serviço como a instalação de um telefone solicitado por um assinante a uma prestadora de serviço de telefônica por exemplo.   
Uma OS é composta de uma numeração própria que é usada para a sua identificação e identificação dos [produtos/serviços](http://tdn.totvs.com/pages/viewpage.action?pageId=423938817) que também fazem parte dela e de uma ou mais mãos de obra que são as pessoas encarregadas de efetuarem os serviços contidos na OS.  
O TOTVS Manutenção, permite que uma empresa controle todo o seu processo de manutenção incluindo o controle de Ordens de Serviço e de todos os itens relativos a ela.   
Ele é capaz de controlar desde o atendimento ao cliente, passando pela fase de análises/andamento, alocação da [mão de obra](http://tdn.totvs.com/pages/viewpage.action?pageId=423938584) e execução dos serviços até à hora em que a ordem de serviço for finalizada estiver pronta para ser faturada.   
O faturamento da Ordem de Serviço é feito dentro do sistema [TOTVS Gestão de Estoque, Compras e Faturamento](http://tdn.totvs.com/pages/viewpage.action?pageId=198948835). Para saber mais sobre como faturar um movimento clique aqui.  
A ordem de serviço é uma extensão do movimento do sistema TOTVS Gestão de Estoque, Compras e Faturamento, sendo assim, todas as possibilidades de parametrização existentes dentro do movimento passam a ser possíveis na ordem de serviço como por exemplo o uso de fórmulas de consistências, a possibilidade de usar descontos e despesas dentro da ordem de serviço, meio de pagamento, cópia de movimento, o uso de [produtos](http://tdn.totvs.com/pages/viewpage.action?pageId=423938817) substitutos / similares dentre outras.   
Toda a parametrização que fuja do contexto do sistema TOTVS Manutenção é realizada dentro do sistema TOTVS Gestão de Estoques, Compras e Faturamento acessando o tipo de movimento.

**E****stornar Item não Recebido**

Esse processo não é apresentado para ser executado diretamente na Ordem de Serviço, entretanto, é possível executar esse processo em um movimento gerado a partir da Ordem de Serviço (uma Requisição de Material, por exemplo) no TOTVS Gestão de Estoque, Compras e Faturamento.   
Ao executar o processo "Estornar Item não Recebido" para um item de um movimento gerado pela Ordem de Serviço, o vínculo do item com a Ordem de Serviço é removido e será possível excluir o item da Ordem de Serviço.

**Concluir Pedido**

Esse processo não é apresentado para ser executado diretamente na Ordem de Serviço, entretanto, é possível executar esse processo em um movimento gerado a partir da Ordem de Serviço (Requisição de Material, por exemplo) no TOTVS Gestão de Estoque, Compras e Faturamento.   
Ao executar o processo "Concluir Pedido" para um item de um movimento gerado pela Ordem de Serviço, o vínculo do item com a Ordem de Serviço NÃO é removido, e desta forma não é possível excluir o item da Ordem de Serviço.

---
