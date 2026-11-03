---
content_hash: 3f133490ec7ed2d209f0c742ca66be8f79188d3fdef1f5b10273c6d472fc7782
fetched_at: '2026-06-29T00:09:23.934795+00:00'
page_id: '422546165'
product: rm
source: tdn-rm
title: Tabela Dinâmica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546165
version: 15
---

#f5f5f5#363636noneTabela Dinâmica

## **Conteúdo**



## **01. Visão GeralVisaoGeral**

Através do menu - Obrigações Acessórias | Federais | ECF | Tabela Dinâmica, o usuário deve executar o processo de importação das tabelas dinâmicas que serão vinculadas ao Evento Tributário  e posteriormente serão geradas informações para ECF.   
A tabela a ser listada será apresentada conforme a forma de tributação selecionada e pasta (Grupo) que o usuário está parametrizando.

## **02. Arquivos Disponíveis****ArquivosDisponiveis**

Na Central de Compartilhamento TOTVS foi disponibilizado um arquivo TXT (CSV) com todas as informações das tabelas dinâmicas publicadas pela ECF para que seja importada.

Arquivos:

FISPLA0001 - Imunes Isentas.csv  
FISPLA0002 - Lucro Arbitrado.csv  
FISPLA0003 - Lucro Presumido.csv  
FISPLA0004 - Lucro Real.csv

## **03. Formato dos ArquivosFormatoDosArquivos**

Todos os arquivos disponibilizados, descritos no item anterior, possuem a seguinte estrutura em suas colunas:

|  |  |
| --- | --- |
| Código | 0 |
| Descrição | 1 |
| DT\_IN | 2 |
| DT\_FIM | 3 |
| Grupo | 4 |
| Registro | 5 |
| Forma de Tributação | 6 |
| Tributo | 7 |

## **04. Tabela Dinâmica de Lucro RealLucroReal**

Antes de importar essa tabela, é necessário parametrizar um período de vigência para ECF no cadastro da Filial através dos Anexos → opção Parâmetros ECF - Escrituração Contábil Fiscal.

Dos registros M300 e M350 (coluna 5, vide item anterior), serão importados no sistema apenas os que se enquadrem na Qualificação da Pessoa Jurídica da filial, que pode ser parametrizada também no cadastro da Filial em Anexos > Parâmetros ECF - Escrituração Contábil Fiscal > Tributação > Qualificação da Pessoa Jurídica.

Segue abaixo quais registros serão importados de acordo com a Qualificação da Pessoa Jurídica selecionada na Filial:

QualificacaoFilialleftPjEmGeralPJ em Geral

Serão importados os registros **M300A** e **M350A** do arquivo.

PjSistemaFinanceiroPJ Componente do Sistema Financeiro

Serão importados os registros **M300B** e **M350B** do arquivo.

SociedadesSeguradorasSociedades Seguradoras

Serão importados os registros **M300C** e **M350C** do arquivo para a qualificação "Sociedades Seguradoras, de Capit. ou Ent. Aberta de Prev. Compl".

Observação

Como é possível cadastrar vários parâmetros da ECF na filial, a qualificação considerada na importação dos registros será a que possuir a Data Final da escrituração mais recente, na aba Identificação dos Parâmetros ECF da Filial.
