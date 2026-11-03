---
article_id: 9661051324823
category: Originação de Grãos (OG)
content_hash: 4d4945d97e9088ed88588f2ea10face50a06e997e242f910c1d81d6f8b1a5d40
fetched_at: '2026-06-28T22:45:39.579854+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Gestor de Entidade - Tela Principal - Saldos
  e Contratos
type: support-article
updated_at: '2025-04-09T19:39:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9661051324823-Agro-Linha-Protheus-AGR-Gestor-de-Entidade-Tela-Principal-Saldos-e-Contratos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20354280993431)** Tempo aproximado para leitura: **00:01:20 min  
  
Dúvida**Como é divisão do **Gestor de Entidade** e quais são eles? **Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12 **Solução**

O Gestor de Entidade é dividido em dois painéis: **Saldos** e **Contratos**.

No painel **Saldos** são apresentados todos os tipos de contrato que a Entidade consultada possui registrado, podendo ele ser Contrato de Venda, de Compras, de Terceiros e Em Terceiros. Conforme a linha que é posiciona no painel **Saldos**, no painel inferior **Contratos** são apresentados os contratos referente ao registro. Por exemplo: No painel Saldos caso esteja selecionado Contrato de Venda, no painel inferior são apresentados todos os contratos de venda da entidade consultada.

O painel **Saldos** exibe um totalizador agrupado por tipo de contrato dos volumes físico/fiscal recebidas ou entregues, saldos, diferença de volume fiscal, volume reservado e quantidade disponível para transferência.

A quantidade disponível para transferência considera o volume de **entrada**, **subtraindo** os **volumes fixados** **e** **vinculados a romaneio**, **devoluções** e **reservas**.

Os dados da coluna **Diferença Fiscal** referem-se a diferença de peso Físico e Fiscal do recebimento ou entrega.

As mesmas colunas do painel **Saldos** são apresentadas no painel **Contratos**. A diferença consiste que o primeiro é um agrupador por tipo de contrato e o segundo são dados individuais de cada contrato.

Painel de Saldos: Outras Ações - Ações relacionadas

**Trf. Mult. Origens**

**Contrato de Compra**

**Contrato de Venda**

**Contrato Depósito de 3º**

**Contrato Depósito em 3º**  
**Serviço Armazenagem**  

Permite realizar transferência de saldos de contratos de múltiplas origens. Essa operação é possível somente para contratos de compra e de armazenagem de terceiros.

Ao acessar essa opção é aberta nova tela onde por meio do menu **Outras Ações** é possível definir os filtros de pesquisa para selecionar os contratos que serão transferidos. Após selecionar os contratos, deve-se clicar na opção de menu Transferir que abrirá tela para informar os dados do contrato de destino.

As transferências geralmente são utilizadas para mudar a titularidade da mercadoria. Abaixo são descritas as movimentações possíveis:

**Transferências entre contratos de compra**

 São gerados romaneios sem pesagem automaticamente para efetivar a movimentação. Para o contrato de origem é gerado um romaneio com operação de saída do tipo **Devolução de Compra**. Para o contrato de destino é gerado um romaneio com operação de entrada do tipo **Entrada por Compra**.

**Transferências entre contratos de armazenagem de terceiros**

A movimentação fiscal é gerada automaticamente. Para o contrato de origem é gerado automaticamente um romaneio sem pesagem com operação de saída do tipo **Devolução de Depósito** e para o contrato de destino um romaneio sem pesagem com operação de entrada do tipo **Entrada para Depósito**.

**Transferências de contrato de armazenagem de terceiros** **para contrato de compra**

É gerado automaticamente um romaneio sem pesagem com operação de saída do tipo **Devolução de Depósito** para o contrato origem e um romaneio com operação de entrada do tipo **Entrada por Compra** para o contrato de destino.

**Transferências de contrato de compra** **para** **contrato de armazenagem**

É gerado automaticamente um romaneio sem pesagem com operação de saída do tipo **Devolução de Compra** para o contrato origem e um romaneio com operação de entrada do tipo **Entrada para Depósito** para o contrato de destino.

Os principais campos do contrato de destino para serem preenchidos:

| Campo | Descrição |
| --- | --- |
| Campo | Descrição |
| --- | --- |
| TES | Indica a TES para movimentação do contrato de destino. |
| Entidade / Loja | Indica o código da entidade e loja de destino. |
| Local | Indica o Local do Estoque de destino. |
| Tipo Contrato | Indica o tipo de contrato de destino. As opções disponíveis são Compra e Armazém 3º. |
| Form. Próprio | Indica se é formulário próprio ou não. Quando a opção é não, deve se informar os dados do documento fiscal como número e série. Marcando a opção como SIM o documento fiscal será gerado pela módulo. |

Na parte inferior da tela de transferência são apresentados os contratos de origem selecionados. Os principais campos para preenchimento são:

| Campo | Descrição |
| --- | --- |
| TES | Indica a TES para movimentação do contrato de origem. |
| Local | Indica o Local do estoque de origem. |
| Quantidade | Indica a quantidade a ser transferida. |

Painel de Contratos: Outras Ações - Ações relacionadas  
**Romaneios****Visualizar****Financeiro****Transferência****Pendências**Permite consultar os romaneios gerados para o contrato que encontra-se posicionado.
