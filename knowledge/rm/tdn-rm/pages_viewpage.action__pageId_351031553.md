---
content_hash: 716429da86ac87a575b8762243e7da203344d9ef46c5cbeddc731ffcbeb4ba59
fetched_at: '2026-06-29T00:08:55.926494+00:00'
page_id: '351031553'
product: rm
source: tdn-rm
title: DT Nova opção do controle de Histórico de Alterações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=351031553
version: 4
---

# NOVA OPÇÃO DO CONTROLE DE HISTÓRICO DE ALTERAÇÕES

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | **Habilitação* Histórico de Alterações* | **Habilitação* Histórico de Alterações* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Histórico de Alterações** | **Histórico de Alterações** | |
| **Cadastros Iniciais:** | *Convênio, Borderô, Lançamento* |
| **Parâmetro(s):** | *Em Utilitários,Outros | Habilitação Histórico de Alterações* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-5260> |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *Sql e Oracle* |
| **Tabelas Utilizadas:** | *FLANHST,* *FTRBLANHST,* *FLANINTEGRACAOHST,* *FLANRATCCUHST,* *FLANRATDEPHST,* *FRELLANHST,* *FRETENCAOACUMULADAHST,* *FRETENCAOACUMULADARATEIOHST,* *FRETENCAOIRRFHST,* *FLOGVALORESHST,* *FHISTVALORESINTEGRACAOHST* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

No controle de histórico de alterações, a opção "Habilitar somente para Totvs Incorporação" irá habilitar o controle de histório de alteração somente para os registros deste produto.  
O objetivo é a flexibilização do processo para outros módulos cujo controle não é necessário.

## Procedimento para Implantação

Para disponibilizar o recurso, deve ser habilitado a opção no cadastro de perfil do usuário.

## 

## Procedimento para Utilização

Acessar o menu Utilitários, aba Outros | Habilitação Histórico de Alterações

Selecionar a opção "Habilitar somente para Totvs Incorporação"

Importante: Essa opção estará disponível para todos os clientes que já tenham o histórico geral habilitado e que estejam no novo modelo revitalizado do TOTVS Incorporação. Ao realizar a troca de controle do histórico, é aconselhável que se faça o logout / Login no sistema para a leitura dos parâmetros.

Ao marcar a opção "Habilitar  somente para Totvs Incorporação" todos os registros de histórico que já existiam na base, e que não sejam do TOTVS Incorporação, serão removidos de forma irreversível.
