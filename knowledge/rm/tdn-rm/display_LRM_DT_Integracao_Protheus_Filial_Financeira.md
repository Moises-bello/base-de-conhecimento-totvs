---
content_hash: 0a828a5120a48597c736f09b4432a5572a50fa75bbdc2a0e800418e6f1f14031
fetched_at: '2026-06-29T00:06:14.577636+00:00'
page_id: '210047911'
product: rm
source: tdn-rm
title: DT_Integracao_Protheus_Filial_Financeira
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Integracao_Protheus_Filial_Financeira
version: 4
---

# INTEGRAÇÃO RM x PROTHEUS - LANÇAMENTO FINANCEIRO FGTS/INSS POR FILIAL FINANCEIRA (SISTÊMICA)

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Administração de Pessoal /*  *Cliente e Fornecedor* | *Mapeamento do Filial Financeira* | |
| **Versões/Release:** | **12.1.5** |

## Descrição

Integração dos lançamentos financeiros entre RM Labore e Protheus mapeado entre o Cliente Fornecedor/CEI do RM Labore e a Filial Financeira(Sistêmica) do Protheus.

Filial Financeira (Sistêmica) no Protheus são obras de construção civil cadastradas juntamente com as filiais fiscais(estabelecimento)  no módulo ‘Cadastro de Filiais’ do Protheus

## Procedimento para Utilização

**Mapeamento da Filial Financeira (Sistêmica)**

O mapeamento entre a Filial Financeira (Sistêmica) do Protheus é feito com o Cliente/Fornecedor, ou com um CEI de Cliente Fornecedor do RM.

Mapeamento com Cliente/Fornecedor **Administração de Pessoal / Cliente e Fornecedor**

Mapeamento com CEI de Cliente Fornecedor **Administração de Pessoal / Cliente e Fornecedor – Anexo: CEI do Cliente / Fornecedor** 

Lançamentos Financeiros **Encargos / Lançamentos (RM Labore)**

A tela de lançamentos financeiros foi atualizada para exibir os dados do tomador (CNPJ e CEI) e a filial financeira.

**Integração Financeira com outros BackOffices**

Ao executar o processo ‘Integração financeira com outros Backoffices’, a filial financeira é enviada. O campo utilizado para enviá-la é o campo FILIAL (BRANCHID), já existente no XML da mensagem.

Caso não haja valor para a Filial Financeira, é enviada a Filial (RM).
