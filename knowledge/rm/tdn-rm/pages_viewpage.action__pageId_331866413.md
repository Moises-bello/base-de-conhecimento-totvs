---
content_hash: c620ae3dbf69d198cc59bf00381af82d7f562dfd8bf11c15901dc352e95ac21e
fetched_at: '2026-06-29T00:08:50.124322+00:00'
page_id: '331866413'
product: rm
source: tdn-rm
title: DT Notas Explicativas Contas Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=331866413
version: 7
---

# Notas Explicativas Contas Contábeis

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *Informe a linha de produto.* |
| **Segmento:** | *Informe o segmento.* |
| **Módulo:** | **Informe o módulo*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Notas explicativas* | *CtbNotaExplicativaContaForm* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Cadastro de contas contábeis* | *CtbContaAction* | |  |  | |
| **Cadastros Iniciais:** | *Contas contábeis* |
| **Parâmetro(s):** | *Não se aplica.* |
| **Ponto de Entrada:** | **Não se aplica.** |
| **Tickets relacionados** | **Não se aplica.** |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [CONTROLADORIA01-922](http://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-922) |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *Oracle e Sql Server* |
| **Tabelas Utilizadas:** | *CNOTAEXPLICATIVA* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Para atender o Layout 6.0 da ECD foi disponibilizado, na tela de cadastro de contas contábeis, um anexo de notas explicativas. A nota irá afetar três registros já existentes, o J100 - Balanço Patrimonial, o J150 - Demonstração de Resultados e o J210 Demonstração de Lucros ou Prejuízos Acumulados / Demonstração de Mutações do Patrimônio Líquido. Vale ressaltar que o preenchimento desse campo é facultativo.

O anexo é composto pelos seguintes campos.

* Período - Indica o intervalo de tempo a que essa nota explicativa pertence. Ele é composto pelas opções 1º Trimestre, 2º Trimestre, 3º Trimestre, 4º Trimestre e Anual.
* Ano - Ano do período informado.
* Nota Explicativa - Nota a ser enviada para o SPED. Ela poderá ter, no máximo, 255 caracteres e poderá ser composta por letras e números.

É importante frisar que todos os campos existentes no anexo são obrigatórios.

Observação: Para o registro J210, não será possível buscar a nota explicativa através do anexo de plano de contas. Para este registro será implementado outra configuração para atendê-lo.
