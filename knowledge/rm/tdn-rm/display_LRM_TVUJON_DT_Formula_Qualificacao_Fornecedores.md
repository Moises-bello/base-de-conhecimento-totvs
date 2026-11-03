---
content_hash: d07996a4f0e7e75b5b1eebf575d057d142c1780e455b6c34025cca8fb5700b9f
fetched_at: '2026-06-29T00:08:19.283340+00:00'
page_id: '266982943'
product: rm
source: tdn-rm
title: TVUJON_DT_Formula_Qualificacao_Fornecedores
type: documentation
url: https://tdn.totvs.com/display/LRM/TVUJON_DT_Formula_Qualificacao_Fornecedores
version: 114
---

# Fórmula de Qualificação de Fornecedores

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Estoque, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | COM.025 | QUALIFICACAO DE FORNECEDORES | |
| **Cadastros Iniciais:** | *-* |
| **Parâmetro(s):** | *-* |
| **Ponto de Entrada:** | *-* |
| **Chamados Relacionados** | TVUJON |
| **Requisito (ISSUE):** | - |
| **País(es):** | *Br* |
| **Banco(s) de Dados:** | *-* |
| **Tabelas Utilizadas:** | TREQUISITOQUALIFIC |
| **Sistema(s) Operacional(is):** | *-* |

## Descrição

Melhoria realizada para o auxiliar a criação da fórmula responsável pela qualificação do fornecedor, foi criada uma nova função de fórmula responsável por retornar os dados do Fornecedor e do Produto no contexto da cotação.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *12.1.13.101* deste chamado.

A fórmula deve ser parametrizada na etapa Gestão de Compras -> 04.06.09 - Qualificação de fornecedores, podendo ser utilizada na "Qualificação por Fornecedores" e na "Qualificação por Produto/Fornecedor".

## Procedimento para Utilização

A função de fórmula **TABQUALIFICACAO** é responsável por retornar as seguintes informações:

Código da Coligada do Fornecedor  
Exemplo de Utilização: **TABQUALIFICACAO('CODCOLCFO', 'N')**

Código do Fornecedor  
Exemplo de Utilização: **TABQUALIFICACAO('CODCFO', 'S')**

Coligada do contexto  
Exemplo de Utilização: **TABQUALIFICACAO('CODCOLIGADA', 'N')**

Identificador do requisito  
Exemplo de Utilização: **TABQUALIFICACAO('IDREQUISITO', 'N')**

Identificador do produto (No caso de Qualificação por Produto/Fornecedor)  
Exemplo de Utilização: **TABQUALIFICACAO('IDPRD', 'N')**

Exemplo de utilização:

Esta função pode ser utilizada em uma fórmula que qualifica o fornecedor com base na última entrega.

Neste contexto, a função **TABQUALIFICACAO** seria utilizada para retornar a **Coligada** e o **Código do Fornecedor**, para ser utilizado como parâmetro em uma sentença SQL que identifique a última compra e compare a data de entrega da mesma com data de emissão da Nota Fiscal.

Se houve antecipação, o fornecedor será bem qualificado, ou seja, a sua pontuação poderá ser maior ou igual a pontuação minima especificada no parâmetro conforme o print acima.

Caso contrário terá uma qualificação menos positiva e sua pontuação será menor do que a pontuação minima definida na parametrização.

De acordo com essas informações será definido a Qualificação do Fornecedor.

Formula para retornar a **Coligada** do Fornecedor

Formula para retornar o **Código** do Fornecedor

Sentença SQL que retornara os dados de **Data Entrega** e **Data de Emissão** do ultimo movimento utilizando como parâmetro as formulas que retornam os dados de **Coligada** e **Código** do Fornecedor .

Formula parametrizada para "**Qualificação por Fornecedores**" de acordo com o primeiro print.

divs
