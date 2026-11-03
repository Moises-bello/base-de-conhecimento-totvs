---
content_hash: b64a89c108f24ef8b1b1db175a1cb2596059098d403fbbf4dfec5eeab66a4ec6
fetched_at: '2026-06-29T00:08:51.577033+00:00'
page_id: '337349574'
product: rm
source: tdn-rm
title: DT Notas Explicativas Fatos Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=337349574
version: 1
---

# Notas Explicativas Fatos Contábeis

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *Informe a linha de produto.* |
| **Segmento:** | *Informe o segmento.* |
| **Módulo:** | **Informe o módulo*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Notas explicativas* | *CtbNotaExplicativaDemoForm* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Cadastro de fatos contábeis* | *CtbEstruturaDemonstracaoAction* | |  |  | |
| **Cadastros Iniciais:** | *Estrutura de Demonstração e Fatos contábeis* |
| **Parâmetro(s):** | *Não se aplica.* |
| **Ponto de Entrada:** | **Não se aplica.** |
| **Tickets relacionados** | **Não se aplica.** |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [CONTROLADORIA01-923](http://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-923) |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *Oracle e Sql Server* |
| **Tabelas Utilizadas:** | *CNOTAEXPLICATIVA* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Para atender o Layout 6.0 da ECD foi disponibilizado, na tela de cadastro de fatos contábeis, a aba de notas explicativas. A nota irá afetar três registros já existentes, o J100 - Balanço Patrimonial, o J150 - Demonstração de Resultados e o J210 Demonstração de Lucros ou Prejuízos Acumulados / Demonstração de Mutações do Patrimônio Líquido. Vale ressaltar que o preenchimento desse campo é facultativo.

O cadastro de notas, existente na aba Notas Explicativas, é composto pelos seguintes campos.

* Período - Indica o intervalo de tempo a que essa nota explicativa pertence. Ele é composto pelas opções 1º Trimestre, 2º Trimestre, 3º Trimestre, 4º Trimestre e Anual.
* Ano - Ano do período informado.
* Nota Explicativa - Nota a ser enviada para o SPED. Ela poderá ter, no máximo, 255 caracteres e poderá ser composta por letras e números.

É importante frisar que todos os campos existentes no cadastro são obrigatórios.
