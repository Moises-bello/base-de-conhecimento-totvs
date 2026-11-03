---
content_hash: 0d3d8671243a2d3ad9abd76ee7f4af099069b437e1f00d79e4e99bb56c0ed87b
fetched_at: '2026-06-29T00:08:57.248231+00:00'
page_id: '353286168'
product: rm
source: tdn-rm
title: 920069 RMSAU-2598 DT Data/Hora de previsão de execução do exame
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=353286168
version: 4
---

# Data/Hora de previsão de execução do exame

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Pedido de Exames |  |  | | --- | | **Rotina(s) envolvida(s)** | | Pedido de Exames pelo PEP RM | | Pedido de Exames pelo PEP 2 | | Pedido de Exames - Unidade de Diagnóstico | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server®, Oracle® |
| **Tabelas Utilizadas:** | SZPEDEXAMEITEM |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Inclusão de campo para se informar a data e hora prevista para a execução do exame. O novo campo está presente nas seguintes telas:

* Menu Prontuário / aba Exames Complementares / Botão Solicitar Exames
* Menu Unidades Diagnósticos / aba Exames Solicitados
* A data e era informados no PEP 2 refletirão este novo campo dentro do RM

## Procedimento para Utilização

UtilizacaoPEP\_RMExames Complementares

* Acessar o menu Prontuário
* Selecionar um paciente
* Acessar a aba Exames Complementares e clicar no botão Solicitar Exames

* Se a data for informada, a mesma será lançada no pedido de exames para que a área responsável se organize diante da necessidade médica
PedidoPedido de Exames

Na tela de Pedido de Exames, tanto para paciente interno e externo, a data de previsão de execução será disponibilizada. A mesma não é obrigatória, mas caso seja informada, ela terá as seguintes validações:

* A data deve ser válida
* A data não pode ser menor que a data do pedido
* A data não pode ser maior que a data de entrega
* A data não pode ser anterior à data de coleta

pep2Pep 2controle pedidoControle de Pedido de Exames

Na tela de visão do Controle de Pedido de Exames, o novo campo estará disponível para visualização, ordenação. Caso a coluna não esteja visível, ela pode ser incluída pelo botão "Configurar Colunas"
