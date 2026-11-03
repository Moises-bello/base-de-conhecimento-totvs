---
content_hash: fc0a0246b88737db9dbb9581e90997947d105345615e4b8be5ddd417e3d7bf99
fetched_at: '2026-06-29T00:08:38.281634+00:00'
page_id: '285646379'
product: rm
source: tdn-rm
title: DT INCLUSÃO DE BOLETO NÚMERO DOCUMENTO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285646379
version: 107
---

# Inclusão de Boleto com Número de Documento copiado do Número de Documento do Lançamento

## Inclusão de Boleto

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projeto* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Inclusão de Boleto.* | *Inclusão de Boleto* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Integração Bancária* | *Integração Bancária* | | *Parâmetros* | *Parâmetros* | |
| **Cadastros Iniciais:** | *Lançamentos, Convênio, Conta/Caixa.* |
| **Parâmetro(s):** | *Inclusão a Receber, Número Documento Boleto* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5FINANCEIRO01-1131 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL, Oracle* |
| **Tabelas Utilizadas:** | *FLAN, FBOLETO* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição:

Criação de um parâmetro para que o usuário possa optar por copiar o número do documento do primeiro lançamento para o número de documento do boleto.

Este número não será utilizado para a geração do nosso número, pois esse é gerado pela referência do boleto.

Este parâmetro será por coligada.

## Procedimento para Implantação

A implementação estará disponível após atualização para versão do RM 12.1.18.1

1. 1. ###### No módulo TOTVS Gestão Financeira acesse*Ambiente > Parâmetros > TOTVS Gestão Financeira > Contas a Receber.*e verifique que o parâmetro*Número Documento do Boleto* é criado:

|  |  |
| --- | --- |
| **Nome da Variável:** | *Número Documento do Boleto* |
| **Tipo:** | *Parâmetro* |
| **Descrição:** | Define se o Número do Documento do Boleto será a Referência do Boleto ou o Número de Documento do Lançamento |
| **Valor Padrão:** | *Ref. Boleto.* |

## Procedimento para Utilização

Definir os parâmetros de inclusão de lançamento conforme imagem abaixo.

Após a conclusão da parametrização ao realizar a inclusão de um novo Boleto o sistema irá gerar um novo boleto com o número de Documento igual ao número de documento do lançamento.

Antes o sistema sempre preenchia o número do Documento do Boleto com sua Referência de Boleto.

## Vídeo

600400

divs
