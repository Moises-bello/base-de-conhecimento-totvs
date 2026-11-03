---
content_hash: 5100f13932362c5d862b27577ec551a8c618eb1ae4d7abb0ef8a10c64e58bd97
fetched_at: '2026-06-29T00:08:53.234928+00:00'
page_id: '344464124'
product: rm
source: tdn-rm
title: DT Bloco K - Implementações para o Plano de Contas Paralelo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=344464124
version: 17
---

# Implementações para o Plano de Contas Paralelo

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | Totvs Gestão Contábil. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Cadastro do Plano de Contas Paralelo / Gerenciar o Cadastro do Plano de Contas Paralelo. | CtbParaleloAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Geração do SPED Contábil (ECD). | CtbSpedContabilAction. | |  |  | |
| **Cadastros Iniciais:** | ***Não se aplica.*** |
| **Parâmetro(s):** | ***Não se aplica*.** |
| **Ponto de Entrada:** | ***Não se aplica*.** |
| **Tickets relacionados** | ***Não se aplica*.** |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [CONTROLADORIA01-1155](http://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-1155); [CONTROLADORIA01-1156](http://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-1156); [CONTROLADORIA01-1157](http://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-1157); [CONTROLADORIA01-1198](http://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-1198); [CONTROLADORIA01-1200](http://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-1200 "Bloco K - Criar Processo para alimentar o saldo das contas do Plano Consolidado") |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | ***SQL Server e Oracle*.** |
| **Tabelas Utilizadas:** | CPARALELO. |
| **Sistema(s) Operacional(is):** | Windows. |

## Descrição

Para possibilitar a inclusão de um plano de contas consolidado foi necessário adicionar a opção "Bloco K - Plano de Contas Consolidado".

* Na instituição responsável, que teve sua descrição alterada para "Instituição Responsável / Finalidade", foi adicionada a opção "Bloco K - Plano de Contas Consolidado".

* Quando a opção "Bloco K - Plano de Contas Consolidado" estiver selecionada no campo "Instituição Responsável/Finalidade" e a tela para associação de contas paralelas for exibida, a guia "Associação com Centro de Custos" ou "Associação com Contas Gerenciais" conforme a parametrização do plano selecionado não deverá aparecer.

* Quando uma coligada do tipo Controlada acessar o plano de contas paralelo irá visualizar o plano de contas consolidado (Bloco K - Plano de Contas Consolidado) cadastrado por sua coligada Controladora. Desta forma será possível associar suas contas contábeis ao plano paralelo cadastrado.

*Coligada 1 (Controladora)*

*Coligada 6 (Controlada)*

**Aba eliminação de valores**

Com o objetivo de gerar os blocos K310 e K315, foi implementado o cadastro de eliminação de valor. Se a Instituição Responsável / Finalidade for "Bloco K - Plano de Contas Consolidado", então a aba "Eliminação de Valores" será exibida. Através dela será possível informar a empresa detentora das parcelas do valor eliminado total e as contrapartes das parcelas do valor eliminado total, com os respectivos valores eliminados. A tela de eliminação de valores irá possuir os seguintes campos.

* Coligada detentora: Código da coligada detentora do valor aglutinado que foi eliminado.
* Coligada da contrapartida: Código da coligada da contrapartida.
* Conta da contrapartida: Código da conta consolidada da contrapartida. Serão exibidas as contas do plano de contas consolidado.
* Valor: Parcela da contrapartida do valor eliminado total.
* Data: Data que será verificada durante a execução do processo de atualização de saldo consolidado.
* Natureza: Indicador da situação do valor eliminado (devedor, credor).

Não será permitida a inclusão de valores eliminados se a coligada detentora e a coligada de contrapartida forem iguais. Também é importante ressaltar que tanto a coligada controladora quanto as controladas poderão visualizar, incluir, editar ou excluir os valores a serem eliminados.

Outro ponto que merece destaque é a possibilidade de incluir uma parcela da contrapartida do valor eliminado total, mesmo havendo um ou mais registros idênticos na base de dados.

Ex: Digamos que na base de dados exista um registro cuja coligada detentora seja 1, coligada contrapartida 6, conta contrapartida 1.11.001, data 26/03/2018, valor 8.500,00 e natureza credora. Nada impede que o usuário inclua outro registro com os mesmos valores, ou outro registro modificando apenas o valor da parcela, pois o valor eliminado total será a soma das parcelas da contrapartida.

**Anexo para conferência do saldo das contas do plano de contas consolidado**

As informações geradas pelo processo "Atualização do Saldo das Contas do Plano de Contas Consolidado" deverão ser exibidas pelo anexo "Saldo das Contas do Plano de Contas Consolidado". Ele estará visível apenas para os planos de contas cuja "Instituição Responsável/Finalidade" for "Bloco K - Plano de Contas Consolidado".
