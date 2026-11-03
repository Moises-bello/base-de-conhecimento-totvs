---
content_hash: 2b8f1a2be7ff22fb84c020e7017a3aef4591646843b11e42ca1598ec9e5fdc28
fetched_at: '2026-06-29T00:06:28.141751+00:00'
page_id: '233749704'
product: rm
source: tdn-rm
title: DT_Exclusao_Lançamento_Financeiro_Integracao_Protheus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=233749704
version: 2
---

# Exclusão de Lançamento Financeiro Integração Protheus

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Encargos | Lançamentos Financeiros | |
| **Versões/Release:** | 12.1.10 |

## Descrição

Atualmente existe uma integração de lançamentos financeiros do RM com o Protheus, de forma que os lançamentos do RM podem ser enviados e incluídos no módulo financeiro do Protheus.

Visando contemplar a necessidade de estorno e cancelamento destes lançamentos (no Protheus chamados de títulos), foi desenvolvido novo fluxo de integração para realizar o cancelamento destes lançamentos no RM, e automaticamente envio do comando de exclusão para o Protheus.

## Procedimento para Utilização

Considerando os cenários de lançamentos financeiros: não integrados, integrados no Protheus, e integrados e baixados.

Siga os seguintes passos para efetuar a exclusão, observando os resultados em cada um dos cenários citados acima:

**1.** Primeiramente, conceda permissão ao usuário para usar a funcionalidade

**2.** No módulo Folha de Pagamento, acesse aba “Encargos”, botão “Lançamentos”, menu “Lançamentos (RM Labore)”

**3.** Selecione os lançamentos que deseja excluir, clique no menu “processos”, e selecione a opção “Excluir Lançamento Financeiro Labore/BackOffice”, e aguarde o processo executar

**4.** Aguarde a conclusão da execução do processo, pois é assíncrono. O RM depende do retorno do Protheus para decidir como seguir o fluxo (possibilidades serão exemplificadas à seguir).

**5.** Caso o lançamento só exista no lado RM (ainda não foi incluído no Protheus), este é excluído imediatamente no RM, informando no log do processo que o lançamento existe somente no RM (não integrado no Protheus). Neste caso não é necessário ocorrer nenhuma integração.

**6.** Caso o lançamento já tenha sido incluído no Protheus, o RM chama a rotina de integração e envia o comando para exclusão, esperando a resposta do Protheus para efetivar a exclusão no lado RM.

 Quando Protheus responde com sucesso, o RM efetiva a exclusão do registro na base de dados, concluindo a integração.

**7.** Caso o lançamento já tenha sido incluído no Protheus e já esteja “baixado”, a exclusão será abortada.

 

O Protheus responde com erro informando o motivo, e o RM não efetiva a exclusão do registro na base de dados, concluindo a integração sem sucesso.
