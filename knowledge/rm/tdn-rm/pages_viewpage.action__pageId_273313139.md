---
content_hash: 924d5a3d47ba2207d5982867ffbb95f311aa202c472edc2499d39da49fc6a4a5
fetched_at: '2026-06-29T00:08:31.842185+00:00'
page_id: '273313139'
product: rm
source: tdn-rm
title: 544350 MSAU-6113 DT Parâmetro para não Chamar Senha no Painel de Atendimento
  Eletivos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273313139
version: 110
---

# Parâmetro para não chamar senha no painel de atendimento eletivos

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Cadastros | Unidade de atendimento |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Atendimento | Painel de atendimentos eletivos | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle® e SQL Server® |

## Descrição

Criado parâmetro para não realizar chamada no painel de atendimentos eletivos, quando a senha estiver em registro de atendimento.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da versão 12.1.17.100 da biblioteca do RM.

## Procedimento para Utilização

       1.            No TOTVS Gestão Hospitalar, acesse Cadastro / Uso Geral / Unidade de atedimento.

       2.            Selecione uma unidade de atendimento e clique no botão editar.

       3.            Na aba Identificação, desmarque o parâmetro "Realiza chamada de senha no registro de atendimento" .

       4.           Em seguida acesse o Painel de atendimentos eletivos na unidade de atendimento configurada nos passo anterior.

       5.           Na aba de registro de atendimento, selecione uma senha e clique no botão chamar. A senha selecionada não vai aparecer no painel de chamadas.

divs
