---
content_hash: 1b88f79f5de95e51ffa9a0c70a25d4eab11afee1ad275a41305d983b08213785
fetched_at: '2026-06-29T00:08:34.791262+00:00'
page_id: '274841561'
product: rm
source: tdn-rm
title: 649285 MSAU-6779 DT Migração da Tela de Lançamentos de BPA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274841561
version: 106
---

# Migração da tela de lançamentos de BPA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | Rotina | Nome Técnico | | Faturamento | lançamentos de procedimentos BPA | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server® e ORACLE® |

## Descrição

Migração da tela de procedimentos de BPA para a nova MDI.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da versão 12.1.16.117 da biblioteca do RM.

## Procedimento para Utilização

* No TOTVS gestão hospitalar, acesse o menu Faturamento > Faturamento SUS > Lançamento de procedimento de BPA.
* Cadastre um novo BPA;
* Ao selecionar um atendimento o sistema vai carregar todas os BPAs da parcial do atendimento dentro da aba "Procedimentos do paciente";
* Ao terminar de preencher todos os campos obrigatórios do lançamento clique no botão salvar;
* Em seguida, clique no botão Processos > Liberar BPA;
* O sistema vai validar todos os dados dos BPAs lançados para parcial, e caso não encontre nenhum problema de cadastro, o sistema irá liberar todos os procedimentos de BPA e a parcial de atendimento para faturamento.

divs
