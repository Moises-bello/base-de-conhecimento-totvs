---
content_hash: 6a59eb0082ff3b24f1ae196767c6ff8cd72e2044d872aab8feed3936f2ef803d
fetched_at: '2026-06-29T00:06:12.569263+00:00'
page_id: '205917821'
product: rm
source: tdn-rm
title: DT_Fluig_Workflow_de_Aprovação_de_Movimentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=205917821
version: 11
---

# Fluig - Workflow de Aprovação de Movimentos

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Aprovação por Workflow | *Informe o nome técnico da rotina.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Aprovação de Movimentos | *Informe o nome técnico da(s) rotina(s) envolvidas.* | |  |  | |
| **Cadastros Iniciais:** | Tipo de Movimento |
| **Parâmetro(s):** | Integração Fluig |
| **Requisito (ISSUE):** | PCREQ-4514 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas Utilizadas:** | TTMV – Tipos de Movimento TMOV – Movimento TITMMOV – Itens de Movimento TITMMOVWFLUIG – Relacionamento entre Item de Movimento e Workflow Fluig |
| **Sistema(s) Operacional(is):** | Windows 7 SP1 ou superior. |
| **Versões/Release:** | 12.1.8 |

## Fluxo de Aprovação por Item de Movimento

## Descrição

A integração do Fluig com o TOTVS Gestão de Estoque, Compras e Faturamento  consiste na geração automática de *Workflows,* no Fluig, dada a inclusão de um Movimento que esteja parametrizado para o mesmo e que seja necessário a aprovação de um usuário para faturamento, alteração ou inclusão em Cotação.

## Procedimento

**Processos envolvidos no fluxo de aprovação por Movimento/Item de Movimento:**

**Inclusão de Movimento:**

Ao incluir o Movimento ou os Itens de Movimento o *Workflow* é incluído de acordo com a parametrização, na Etapa Inicial, para que o usuário determinadopossa realizar a aprovação ou desaprovação. Caso, não tenha sido aprovado o Movimento não poderá ser Faturado.

**Alteração de Movimento:**

Ao alterar um movimento, caso o tipo de movimento esteja parametrizado para utilizar o Workflow de Aprovação no Fluig para Faturamento, se o campo Item Utilizado da tabela TITMMOVWFLUIG tenha o seu valor como verdadeiro é criado um novo workflow com a nova quantidade, caso contrário, se o campo Item Utilizado tenha o seu valor como falso será realizado o estorno do Workflow de Aprovação no Fluig e em seguida uma inclusão de um novo Workflow.

Caso esteja parametrizado para Agrupamento por Movimento será gerado um novo Workflow com todos os itens que possuam quantidade maior que zero.

Caso esteja parametrizado para Agrupamento por Item de Movimento será gerado um novo Workflow para este item. Neste caso os Workflows dos demais itens não serão afetados.

Somente serão gerados novos workflows para os itens de movimento que não estão participando de cotação.

**Estorno de Item Não Recebido**

Ao executar o processo de estornar item não recebido o campo Item Utilizado da tabela TITMMOVWFLUIG dos itens de movimentos de origem relacionados terão o seu valor alterado para falso.  Não haverá alteração nos workflows existentes para o movimento de origem.

**Faturamento de Movimento**

No Faturamento do Movimento é realizada a consulta no estado do *workflow,* e de acordo com a parametrização se a aprovação for por Item, portanto, somente serão faturados os Itens aprovados e o movimento ficará com o Status de Parcialmente Faturado caso apenas um Item de Movimento estiver aprovado dentre outros no Movimento, caso a aprovação seja por Movimento todos os itens serão faturados se o *workflow* estiver aprovado e o Status do será alterado para Faturado. O campo Item Utilizado da tabela TITMMOVWFLUIG terá o seu valor alterado para verdadeiro.

**Cancelamento de Movimento**

Ao cancelar um movimento, caso o tipo de movimento esteja parametrizado para utilizar o Workflow de Aprovação no Fluig para Faturamento, será realizado o estorno do Workflow de Aprovação no Fluig de acordo com a regra de alteração de movimento.

Ao cancelar um movimento, o campo Item Utilizado da tabela TITMMOVWFLUIG dos itens de movimentos de origem relacionados terão o seu valor alterado para falso. Não haverá alteração nos workflows existentes para o movimento de origem.

**Processos envolvidos no fluxo de aprovação de Cotação de Compra**

**Inclusão de Movimento**

Ao incluir um novo movimento, caso o tipo de movimento esteja parametrizado para utilizar o Workflow de Aprovação no Fluig para a Cotação, será incluído um novo Workflow de acordo com os parâmetros definidos.

**A****lteração de Movimento**

Ao alterar um movimento, caso o tipo de movimento esteja parametrizado para utilizar o Workflow de Aprovação no Fluig para Faturamento, se o campo Item Utilizado da tabela TITMMOVWFLUIG tenha o seu valor como verdadeiro é criado um novo workflow com a nova quantidade, caso contrário, se o campo Item Utilizado tenha o seu valor como falso será realizado o estorno do Workflow de Aprovação no Fluig e em seguida uma inclusão de um novo Workflow.

Caso esteja parametrizado para Agrupamento por Movimento será gerado um novo Workflow com todos os itens que possuam quantidade maior que zero.

Caso esteja parametrizado para Agrupamento por Item de Movimento será gerado um novo Workflow para este item. Neste caso os Workflows dos demais itens não serão afetados.

Somente serão gerados novos workflows para os itens de movimento que não estão participando de cotação.

**Cancelamento de Movimento**

Ao cancelar um movimento, caso o tipo de movimento esteja parametrizado para utilizar o Workflow de Aprovação no Fluig para a Cotação, será realizado o estorno do Workflow de Aprovação no Fluig de acordo com a regra de alteração de movimento.

Ao cancelar um movimento, o campo Item Utilizado da tabela TITMMOVWFLUIG dos itens de movimentos de origem relacionados terão o seu valor alterado para falso. Não haverá alteração nos workflows existentes para o movimento de origem.

**Estorno de Item Não Recebido**

Ao executar o processo de estornar item não recebido o campo Item Utilizado da tabela TITMMOVWFLUIG dos itens de movimentos de origem relacionados terão o seu valor alterado para falso.  Não haverá alteração nos workflows existentes para o movimento de origem.

**Inclusão de Cotação**

Durante o processo de inclusão de uma nova Cotação, somente serão apresentados Itens de Movimentos que tenham sido aprovados no processo de Workflow de Aprovação no Fluig, nos casos em que o Tipo de Movimento selecionado para a Cotação estejam parametrizados para utilizarem Workflow de Aprovação no Fluig para a Cotação.

Após retornar os itens de movimento disponíveis para serem utilizados na Cotação, será verificado o Estado Final de Aprovação de cada um dos itens de movimento e somente aqueles que possuírem no Fluig algum dos estados finais parametrizados serão exibidos para o usuário selecioná-los para utilização na Cotação que está sendo criada.

O campo Item Utilizado da tabela TITMMOVWFLUIG terá o seu valor alterado para verdadeiro.

**Cancelamento de Cotação**

Ao cancelar uma cotação, o campo Item Utilizado da tabela TITMMOVWFLUIG dos itens de movimentos da cotação que está sendo cancelada terão o seu valor alterado para falso. Não haverá alteração nos workflows existentes para o movimento de origem.

**Exclusão de Item da Cotação**

Ao excluir um item da cotação, o campo Item Utilizado da tabela TITMMOVWFLUIG do item de movimento que está sendo excluído terá o seu valor alterado para falso. Não haverá alteração nos workflows existentes para o movimento de origem.

**Workflows de Exemplo**

As funcionalidades dos Workflows de Exemplo de Aprovação de Movimentos são: Customização do Formulário de acordo com o Tipo de Movimento, Ações no Movimento e Item de Movimento após a aprovação ou reprovação do Workflow. Segue abaixo mais detalhes em relação aos itens apresentados.

**1**.As regras para reprovação e aprovação de Workflow do Movimento são:

**1.1.** **Reprova e Cancela o Movimento**

O usuário ao reprovar um workflow poderá decidir a ação de Cancelamento do movimento. Sendo, o Movimento uma Ordem de Compra gerado através de uma Cotação, a mesma será reaberta.

Ao realizar o cancelamento do Movimento através do Workflow, o mesmo será finalizado para a respectiva ação. Quando se realizar o cancelamento do Movimento no Totvs Gestão de Estoque, Compras e Faturamento, o workflow terá o seu status alterado para Cancelado.

**1.2.** **Reprova e conclui o Movimento**

O usuário ao reprovar um workflow poderá decidir a ação de Concluir o movimento.

**1.3.** **Aprova e Fatura Movimento**

O usuário ao aprovar um workflow poderá decidir a ação de Faturar o movimento. Caso usuário deseja que determinada atividade o movimento seja faturado, então será necessário definir a opção de faturamento como Automático e o tipo de movimento (Default) que será gerado.  Como:

**2**.As regras para reprovação e aprovação de Workflow do Movimento/Item de Movimento são:

**2.1.** **Reprova Somente**

O usuário ao reprovar um workflow não realizará nenhuma ação no Movimento/Item de Movimento.

**2.2.** **Aprova Somente**

O usuário ao aprovar um workflow não realizará nenhuma ação no Movimento/Item de Movimento

**3.**As regras para reprovação e aprovação de Workflow de Item de Movimento são:

**3.1.** **Reprova e estorno de item não recebido (reabre a cotação)**

O usuário ao reprovar um workflow de Movimento / Item de Movimento poderá decidir a ação de Estorno de Item não recebido.

**4. Processos do Workflow**

**4.1.** **Movimento**

Para os Workflows com o tipo de Agrupamento por Movimento são disponibilizados os eventos finais: Cancelamento, Conclusão e Faturamento de Movimento. Sendo que para realizar o Faturamento será necessário definir a opção de faturamento como Automático e o tipo de movimento (Default) que será gerado.

**4.2.** **Item de Movimento**

Para os Workflows com o tipo de Agrupamento por Item de Movimento é disponibilizado novo evento final: Estorno de Item de Movimento.

Ao iniciar o processo e avançar para a Etapa de Definir Responsável o Workflow verificará se o Valor Liquido do Movimento está abaixo de R$10.000, caso esteja será automaticamente aprovado, senão irá para a etapa de Aprovação onde os responsáveis deverão ter o papel *PapelAprovacaoWfMat* e assumir a tarefa para realizar a aprovação.

O Papel *PapelAprovacaoWfMat* deverá ser previamente cadastrado e atribuído os usuários que deverão realizar a aprovação acima.

O Papel *RequisitanteWfMat* deverá ser previamente cadastrado e atribuído os usuários que deverão realizar a solicitação da aprovação.

Será disponibilizada uma consulta, como objeto gerencial, para o cadastro Consultas SQL com o código *FluigWF* para que seja possível utilizar o workflow retornando o valor líquido do Movimento.

O Workflow de exemplo disponibilizado pela TOTVS tem a funcionalidade de avançar da etapa inicial para a próxima atividade e em diante segue o fluxo normal, de realizar a aprovação automática ou para etapa de Aprovação. Para esta funcionalidade é necessário cadastrar um usuário e senha de integração (Usuário: [nucleus@totvs.com.br](mailto:nucleus@totvs.com.br) e Senha: Totvs@123).

## Importante

Caso seja parametrizado para utilizar a aprovação através do Fluig não será possível parametrizar o tipo de movimento para aprovar através do Agilis ou de aprovação por Fórmula. Apenas uma única aprovação pode ser configurada para cada Tipo de Movimento.

divs
