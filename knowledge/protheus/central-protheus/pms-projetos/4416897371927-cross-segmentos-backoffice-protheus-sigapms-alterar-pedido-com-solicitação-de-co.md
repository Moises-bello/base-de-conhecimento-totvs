---
article_id: 4416897371927
category: PMS - Projetos
content_hash: cdcad9109f4f544a256bf0770ac7d2a987367859d8e232ace29f04160a8b1161
fetched_at: '2026-06-28T22:37:14.861830+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Alterar Pedido com Solicitação
  de Compras
type: support-article
updated_at: '2024-02-23T12:43:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416897371927-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Alterar-Pedido-com-Solicita%C3%A7%C3%A3o-de-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21563981773463) Tempo aproximado para leitura: **00:004 min** **Dúvida**

Ao visualizar projetos no Pedido de Compras gera a mensagem :

![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416896392983)

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as Versões  
  
**Solução**

A mensagem é gerada porque não é permitido a alteração do projeto, este item do pedido esta relacionado a uma solicitação de projeto por execução.

A execução do projeto tem como objetivo providenciar os insumos para a execução do projeto, ou seja, a compra de material, verificar quem deverá ser alocado e planejar as necessidades para que não falte nada na hora de executar as tarefas.

O controle de execução tem esse objetivo, o planejamento das necessidades. Neste momento é que vamos decidir se o material necessário será comprado, produzido ou solicitado ao almoxarifado, ou ainda se deverá ser reservado material já disponível no estoque para executar as tarefas.

Este planejamento também será registrado com o tipo PREVISTO, ou FIRME. Em ambos os casos, serão disparadas as gerações de solicitações, empenhos, etc.

Desse modo, é possível visualizar a solicitação de compras, e qualquer manutenção altere o pedido e posteriormente a solicitação. 

![20211223_151141.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4416883501079)

**Saiba mais em:** [Gerenciamento de Execução](https://tdn.totvs.com/x/P4oOFQ)
