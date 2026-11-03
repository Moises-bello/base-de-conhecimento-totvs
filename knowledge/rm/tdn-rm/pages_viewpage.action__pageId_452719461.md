---
content_hash: e6ab5c5a737b81b7dfd1a34166eff5827a0021778c441b9dffe7f5a74b6b0afc
fetched_at: '2026-06-29T00:10:07.881379+00:00'
page_id: '452719461'
product: rm
source: tdn-rm
title: Pasta Identificação - Requisição de Transferência em Lote
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719461
version: 3
---

**Pasta Identificação - Requisição de Transferência em Lote**

Na pasta Identificação os seguintes dados devem ser informados:

**Número -** Gerado automaticamente e com valor único.

**Status -** Será apresentado logo após a abertura da requisição como "Pendente". Este campo será alterado à medida que a requisição for avançando no fluxo de aprovações assumindo os valores parametrizados e definidos para cada etapa.

Para verificar a parametrização acesse: Configurações | Tipos de Requisições. Os status que poderão ser definidos pelo fluxo de aprovação são "Em Andamento", "Aprovado" e "Reprovado".

Os status "Suspenso" e "Cancelado" serão definidos conforme a utilização do processo "Suspender requisição " e "Cancelar Requisição" respectivamente. O status "Concluído" será determinado quando o processo "Concluir requisição" for realizado através do menu "Efetivar Transferência em Lote".

**Os status das requisições são representados pelas cores:**   
Aprovada – cor verde

Cancelada – cor preta

Concluída – cor roxa

Em Andamento – cor amarela

Pendente – cor laranja

Reprovada – cor vermelha

Suspensa – cor azul

**Nome do Aprovador Atual -** Este campo não é editável e apresentará o nome do aprovador atual da requisição, ou seja, o responsável atual pela requisição, conforme definição do fluxo de aprovações.

**Conclusão -** Irá apresentar a data que a requisição foi concluída, ou seja, a data que foi realizada a efetivação da transferência em lote.

**Requisitante -** Somente podem ser selecionados chefes da coligada na qual o usuário do Totvs Gestão de Pessoas esteja logado. Esta informação poderá ser modificada enquanto a requisição estiver pendente ou se nenhum parecer tiver sido cadastrado.

Caso a requisição seja aberta pelo "Totvs RM Portal" este campo exibirá o nome do usuário logado não podendo ser modificado.

**Observação**:

Se o usuário trocar o requisitante, todos os funcionários vinculados serão removidos da requisição.

**Previsão -** Deverá ser informada a data prevista para a transferência em lote, não podendo receber um valor inferior à data atual (data do dia). Este campo poderá ser alterado enquanto a requisição estiver pendente ou em andamento, e caso a requisição esteja pendente, apenas se nenhum parecer tiver sido cadastrado. Por definição o sistema sugere a data atual.

**Justificativa -** Ao solicitar uma transferência em lote deverá ser informada uma justificativa para tal solicitação. Este campo poderá ser alterado enquanto a requisição estiver pendente ou se nenhum parecer tiver sido cadastrado.

Dados de alteração

**Filial -** Permite que seja selecionada a filial proposta para a transferência em lote dos funcionários relacionados.

Neste campo, serão exibidas apenas as filiais onde o requisitante seja chefe de alguma seção e a filial pertencer à coligada em que o usuário está logado. Este campo poderá ser alterado enquanto a requisição estiver pendente e desde que nenhum parecer esteja cadastrado.

No Totvs RM Portal enquanto a requisição estiver em andamento e o aprovador atual não estiver lotado na seção destino.

**Seção -** Após o preenchimento do campo "Filial", este campo ficará habilitado permitindo que seja selecionada a seção proposta para a transferência do funcionário selecionado. Somente poderá ser selecionada uma seção pertencente à filial que tiver sido selecionada.

Este campo poderá ser alterado enquanto a requisição estiver pendente e desde que nenhum parecer esteja cadastrado. No Totvs RM Portal enquanto a requisição estiver em andamento e o aprovador atual não estiver lotado na seção destino.

**Motivo da mudança de seção -** Este campo poderá ser alterado enquanto a requisição estiver pendente e desde que nenhum parecer esteja cadastrado. No Totvs RM Portal, durante a abertura da requisição ou enquanto a requisição estiver em andamento.

**Gerar substituição -** Esta opção deverá ser marcada se for necessário manter o número de vagas disponíveis ao concluir esta requisição, em função das configurações definidas no controle de lotação. Este campo poderá ser alterado enquanto a requisição estiver pendente e desde que nenhum parecer esteja cadastrado.

No Totvs RM Portal, enquanto a requisição estiver em andamento desde que o aprovador atual seja o chefe da seção de origem do funcionário.

**Transferir Vaga -** Esta opção deverá ser marcada se for necessário reduzir o número de vagas disponíveis na seção de origem do funcionário transferido e, aumentar em uma unidade o total de vagas disponíveis na seção de destino, em função das configurações definidas no controle de lotação. Este campo poderá ser alterado enquanto a requisição estiver pendente e desde que nenhum parecer esteja cadastrado.

No Totvs RM Portal, enquanto a requisição estiver em andamento desde que o aprovador atual seja o chefe da seção de origem do funcionário.
