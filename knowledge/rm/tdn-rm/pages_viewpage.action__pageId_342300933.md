---
content_hash: 81f42e3c1b080ff398971201fd61fc4b7f637d2d197c54a5b2138a43c35ebd12
fetched_at: '2026-06-29T00:08:52.700112+00:00'
page_id: '342300933'
product: rm
source: tdn-rm
title: DT Exibir apenas Naturezas/Centro de Custo sintéticas no Fluxo de Caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=342300933
version: 3
---

# Opção para exibir apenas Naturezas e Centro de Custos sintéticos no Fluxo de Caixa

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Fluxo de Caixa | Fluxo de Caixa |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Lançamentos | Lançamentos | | Extratos | Extratos | | Natureza Orçamentária Financeira | Natureza Orçamentária Financeira | | Centro de Custo | Centro de Custo | |
| **Cadastros Iniciais:** | Cadastrar Naturezas Orçamentárias Financeiras, Centro de Custo, Lançamento, Extrato de Caixa, Conta/Caixa. |
| **Parâmetro(s):** | N/A |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | FINANCEIRO01-5321 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL, ORACLE |
| **Tabelas Utilizadas:** | FLAN, FXCX, FCXA |
| **Sistema(s) Operacional(is):** | Windows. |

## Descrição

Uma opção no Fluxo de caixa para exibir os dados somente nas linhas de natureza financeira ou centro de custo sintéticos. Hoje o sistema exibe os sintéticos e logo abaixo os analíticos "pertencentes" ao mesmo. Por default essa opção deve vir desmarcada.

## Procedimento para Configuração

* Para parametrizar um Fluxo de Caixa siga a documentação: <http://tdn.totvs.com/display/public/rm/Fluxo+de+Caixa>

## Procedimento para Utilização

* Ao Abrir o Fluxo de Caixa, na aba Parâmetros teremos apresentado a opção de "Considera apenas códigos sintéticos para Centros de Custos e Naturezas".

* Ao executar o Fluxo de Caixa sem utilizar o parâmetro, temos essa visualização.

* Com o parâmetro marcado teremos essa visualização.

* Com esta melhoria o sistema agora faz a carga da aba dados com todos os lançamentos que compõem o saldo daquela célula. Com ou sem o parâmetro marcado.

  

* IMPORTANTE: Ao clicar em 'Simular Inclusão' será apresentada a mensagem de que não é possível realizar inclusão de lançamentos  e extratos na simulação de sintéticos.
