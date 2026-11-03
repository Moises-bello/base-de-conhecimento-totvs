---
content_hash: 79268e3e690df98fabaa8290d9bbc6dfb57cd13afff7a09a9e916c13e48fa247
fetched_at: '2026-06-29T00:06:22.515566+00:00'
page_id: '223920064'
product: rm
source: tdn-rm
title: TTYTVK_DT_Duplicidade_de_Lançamentos_Financeiros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223920064
version: 2
---

# DUPLICIDADE DE LANÇAMENTOS FINANCEIROS - PREENCHIMENTO DO CAMPO CODPARCELALAN DA TABELA SLAN

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **TOTVS Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Geração de lançamentos* | **Geração de lançamentos financeiros** |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Geração de lançamentos* | **Geração de lançamentos financeiros** | | *Cancelamento de lançamentos* | *Cancelamento de lançamentos* | | *Acordo* | *Acordo de lançamentos do Educacional* | | *Conversor oficial* | *Conversor da versão 12.1.10* | |
| **Cadastros Iniciais:** | *1. Cadastro de parcelas do contrato  *2. Cadastro de responsáveis das parcelas *3. Cadastro de bolsas no contrato (opcional)*** |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A.* |
| **Chamados relacionados** | N/A |
| **Requisito (ISSUE):** | *N/A.* |
| **País(es):** | *Todos.* |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas utilizadas:** | *N/A* |
| **Sistema(s) operacional(is):** | *Todos.* |
| **Versões/Release:** | *12.1.10* |

## Descrição

Alteração no preenchimento do campo CODPARCELALAN da tabela SLAN a fim de evitar a duplicidade de registros de lançamentos para uma mesma parcela financeira.

Os processos alterados foram:

1. Geração de lançamentos financeiros do Educacional
2. Geração de acordo de lançamentos do Educacional
3. Cancelamento de lançamentos do Educacional
4. Conversor oficial da versão 12.1.10

Nos três primeiros processos citados acima, temos a alteração de preenchimento do campo SLAN.CODPARCELALAN.

No item 4, temos um backup da tabela SLAN na tabela SLAN\_OLD\_CODPARCELALAN bem como a alteração de todos os registros de SLAN com o campo IDLAN precedido por um '#'.

**Exemplo**:  #10024

Em seguida, o conversor processará todos os registros de SLAN vinculados à alguma parcela, ou seja, SLAN.IDPARCELA não poderá ser nulo. A ordem de processamento será de registros NÃO CANCELADOS (FLAN.STATUSLAN <> 2) e, sem seguida, os lançamentos CANCELADOS (STATUSLAN = 2) para não priorizarmos um lançamento cancelado com o valor correto no caso de duplicidade de registros.

O preenchimento do campo citado acima, segue as regras abaixo:

1) PARA LANÇAMENTOS QUE NÃO SÃO BOLSAS DE CRÉDITO

CodParcelaLan =   
 # +   
 SLAN.CODCOLIGADA +   (Coligada)  
 SLAN.IDPARCELA +          (Id. da Parcela)  
 FLAN.CODCOLCFO +        (Coligada do Cliente Fornecedor)   
 FLAN.CODCFO +               (Código do Cliente Fornecedor)   
 SPARCELA.CODSERVICO (Código do serviço da parcela)

**Exemplo**:

CODPARCELALAN = #1132601C015841 =>

#            (Caractere coringa para identificar o novo formato de CODPARCELALAN) +   
 1            (Coligada)  
 13260   (Id. da Parcela)  
 1            (Coligada do Cliente Fornecedor)   
 C01584 (Código do Cliente Fornecedor)   
 1            (Código do serviço da parcela)

2) PARA LANÇAMENTOS DE BOLSAS DE CRÉDITO

CodParcelaLan =   
 # +   
 SLAN.CODCOLIGADA +   (Coligada)  
 SLAN.IDPARCELA +          (Id. da Parcela)  
 FLAN.CODCOLCFO +        (Coligada do Cliente Fornecedor)   
 FLAN.CODCFO +               (Código do Cliente Fornecedor)   
 SPARCELA.CODSERVICO (Código do serviço da parcela)  
 SBOLSALAN.CODBOLSA  (Código da Bolsa de Crédito) +   
 SBOLSALAN.IDLAN           (Ref. do lançamento do responsável do aluno - origem)

**Exemplo**:

CODPARCELALAN = #1132601C005201518114 =>

#            (Caractere coringa para identificar o novo formato de CODPARCELALAN) +   
 1            (Coligada)  
 13260   (Id. da Parcela)  
 1            (Coligada do Cliente Fornecedor)   
 C00520 (Código do Cliente Fornecedor)   
 1            (Código do serviço da parcela)                                                
 5            (Código da Bolsa de Crédito)   
 18114   (Ref. do lançamento do responsável do aluno - origem)

3) PARA LANÇAMENTOS CANCELADOS (STATUSLAN = 2)

O preenchimento do CODPARCELALAN obedecerá as regras acima caso o lançamento seja de bolsa de crédito ou não e concatenará o valor do CODPARCELALAN encontrado com uma string no formato: '##' + (Data no formato: yyyymmdd) + (Hora no formato: hhMMss)

**Exemplo**:

CODPARCELALAN = #1132901C015841##20151222104623 (Lançamento cancelado em 22/12/2015 10:46:23)

**OBSERVAÇÃO** :

A geração de lançamentos e a geração de acordo preencherão o campo em questão conforme itens 1 e 2 acima

O cancelamento de lançamentos do Educacional preencerá o campo em questão conforme item 3 acima.

Caso sejam encontrados registros duplicados na base a ser convertida, o conversor verificará se o valor para SLAN.CODPARCELALAN encontrado já foi preenchido em algum outro registro. Em caso afirmativo, o preenchimento do campo será o valor gerado anteriormente para CODPARCELALAN + '$' + <QUANTIDADE DE REGISTROS COM O MESMO VALOR DE CODPARCELALAN ENCONTRADA>.

## Procedimento para Implantação

Necessária execução do conversor de base 12.1.10

## Procedimento para Configuração

N/A

## Procedimento para Utilização

1. Converter a base para a versão 12.1.10
2. Gerar um lançamento financeiro para uma parcela qualquer de um contrato
3. Cancelar um lançamento do Educacional gerado anteriormente
4. Gerar um acordo para um lançamento do Educacional
