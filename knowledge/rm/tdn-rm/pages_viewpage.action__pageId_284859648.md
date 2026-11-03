---
content_hash: b9bcfe6c362fe2c8d41c09c8ffd06a748c03cf00ea7e112563f26cfd5bb2cadc
fetched_at: '2026-06-29T00:08:36.960267+00:00'
page_id: '284859648'
product: rm
source: tdn-rm
title: RMFIN00009_E_Funcional_Remessa eletrônica para cancelamento de boletos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284859648
version: 5
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Financeira |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | N/A |
| **Ambiente:** | RM |
| **Passo a passo:** | N/A |
| **Observações:** |  |

## Objetivo

Permitir que sejam geradas remessas eletrônicas para para cancelamento dos  boletos junto aos bancos, ou seja,  realizar a comunicação eletrônica com o banco informando que determinados boletos pode ser "baixados" do sistema do banco.

## Definição da Regra de Negócio

No módulo financeiro atualmente ocorrem algumas situações de baixas manuais de lançamentos que possuem boletos. Ex: Um aluno vai até a Instituição de Ensino e quita o boleto que possui em aberto. Neste momento o usuário do módulo financeiro irá realizar a baixa manual do título, após a baixa manual no sistema, o status do boleto ficará baixado. Ocorre que na instituição bancária o boleto referente a este lançamento foi enviado via remessa de cobrança eletrônica e consta como "Em aberto". Então o responsável do financeiro, pode enviar uma remessa de cancelamento deste boleto para o banco, desta maneira a instituição financeira poderá dar "baixa" para este boleto em seu sistema. Esta situação apresentada é a mais comum de ocorrer, mas a podem ocorrer outras situações de cancelamento do boleto, a implementação permitirá que boletos que foram cancelados ou estejam inativos por algum motivo possa sem enviados via remessa para cancelamento junto aos bancos.

Como a empresa avisa para o banco que o Boleto deve ser cancelado?

Ao editar um boleto na pasta "Dados CNAB" existe o campo "Comando", neste campo deverá ser informado o código correspondente para o cancelamento junto ao banco. O usuário pode alterar este campo dos boletos via alteração global de boletos pelo processo "Alteração global de Boletos".

# Remessa para cancelamento de Boletos

Na visão de Boletos permitir que boletos com o status de cancelado ou baixado sejam enviados para a o banco para cancelamento. O usuário irá realizar o filtro dos boletos desejados , preencher o campo de comando utilizando a alteração global e após irá gerar o processo de cancelamento de boletos junto ao banco pelo menu de processos/Remessa de Cobrança.

# Processos envolvidos a serem evoluídos

Atualmente quando é feita a baixa manual de um lançamento que possui boleto, após a baixa deste boleto o status do mesmo fica como "Baixado", o usuário precisará filtrar este boletos para enviar ao banco. Será necessário implementar algum recurso que identifique que baixa do lançamento foi feita manualmente e preencher um novo campo na tabela de Boletos. Desta forma, os boletos baixados manualmente poderão ser filtrados pelo cliente para realização do envio do cancelamento junto ao banco.
