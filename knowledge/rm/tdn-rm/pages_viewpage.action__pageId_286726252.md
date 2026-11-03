---
content_hash: 6fef2bbacba2b851f4dd45e5e1f87c27c7f74c8524e8415fdef3ea5d95cb95f3
fetched_at: '2026-06-29T00:08:41.413365+00:00'
page_id: '286726252'
product: rm
source: tdn-rm
title: DT Parâmetro no convênio para cancelar boleto ao alterar valor(es) do lançamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286726252
version: 98
---

# Parâmetro para cancelar o boleto caso o(s) valor(es) do lançamento seja alterado.

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Alteração de Boleto* | *Alteração de Boleto* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Cancelamento de Boleto* | *Cancelamento de Boleto* | |
| **Cadastros Iniciais:** | *Parametrizar o Convênio com os dados bancários para poder gerar um novo boleto.* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5FINANCEIRO01-2190 |
| **País(es):** | *BRA* |
| **Banco(s) de Dados:** | *SQL e ORACLE* |
| **Tabelas Utilizadas:** | *FCONVENIO, FBOLETO, FPARAMCONV* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Criado um parâmetro na tela de convênio para que seja definido se ao alterar o(s) valor(es) do boleto, o mesmo seja cancelado ou tenha seu valor(es) modificado(s). Este parâmetro é envolvido nos processos de alteração e cancelamento de lançamento.

## Importante

Esta necessidade surgiu por conta de que alguns bancos que não possuem um comando específico para realizar a atualização do(s) valor(es) do boleto registrado, desta forma caso seja necessário alterar o(s) valor(es) do lançamento, o boleto deixará de ser válido.

## Procedimento para Configuração

* Acesse o menu Movimentações Bancárias | Convênio | aba Cobrança Bancária;

Marcar a opção 'Cancelar boleto(s) pendente(s) de remessa ao alterar valor(es) do(s) lançamentos(s) '

## Procedimento para Utilização

Alteração de lançamento:

       1.            Inclua um lançamento;

       2.            Inclua um boleto para o lançamento criado;

       3.            Faça a remessa do boleto e cancele sua remessa, desta forma teremos um lançamento com um boleto pendente remessa;

       4.            Edite o lançamento e altere qualquer campo de valor, ao salvar o lançamento o sistema irá cancelar automaticamente o boleto como marcado o parâmetro no convênio.

Cancelamento de lançamento:

       1.            Inclua dois lançamento;

       2.            Inclua um boleto para os dois lançamentos criados;

       3.            Faça a remessa do boleto e cancele sua remessa, desta forma teremos um lançamento com um boleto pendente remessa;

       4.            Selecione um lançamento e cancele-o, o outro lançamento que sobrar, o sistema irá cancelar automaticamente o boleto como marcado o parâmetro no convênio. Isto ocorre pois ao desvincular o(s) lançamento(s) cancelado(s) do boleto o sistema atualiza o valor do boleto para o(s) lançamento(s) restante(s).

divs
