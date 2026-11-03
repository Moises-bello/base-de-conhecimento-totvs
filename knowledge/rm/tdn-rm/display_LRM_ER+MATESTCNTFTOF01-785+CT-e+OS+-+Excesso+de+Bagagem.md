---
content_hash: 080f48767997fdc94f2f3d522299621dcd8fab6a5e8d3581e2c9e1fdb6ae8854
fetched_at: '2026-06-29T00:08:44.351898+00:00'
page_id: '307845415'
product: rm
source: tdn-rm
title: ER MATESTCNTFTOF01-785 CT-e OS - Excesso de Bagagem
type: documentation
url: https://tdn.totvs.com/display/LRM/ER+MATESTCNTFTOF01-785+CT-e+OS+-+Excesso+de+Bagagem
version: 108
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## 

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Movimento |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | MATESTCNTFTOF01 | **IRM/EPIC1** | MATESTCNTFTOF01-785 |
| **Requisito/Story/Issue1** | MATESTCNTFTOF01-813 | **Subtarefa1** | NA |
| **Chamado/Ticket2** | NA | | |
| **País** | ( x ) Brasil | | |
| **Outros** | NA | | |

## 

## Objetivo

Especificar o que deve ser feito no sistema, possibilitando o envio de CT-e OS referente a excesso de bagagem.

## 

## Definição da Regra de Negócio

Parâmetros - Tipo de Movimento

* Na etapa **Fis - Conhecimento de Transporte**, no ComboBox **Tipo do CT-e OS** (TTMVEXT.TIPOSERVICOCTEOS) deve ser acrescentado o valor "Excesso de Bagagem".

Tela de Edição do Movimento

* Quando **Tipo do CT-e OS**igual a "Excesso de Bagagem", em CTRC | CTRC Saída, na tela **Notas Fiscais Conhec. Transporte**, exibir os campos **Data Emissão** (TCTRC.DATAEMISSAO), **Número Nota** (TCTRC.NUMERODOC), **Série** (TCTRC.SERIEDOC), **Sub Série** (TCTRC.SUBSERIEDOC) e **Valor Total** (TCTRC.VALORTOTAL).
* Quando **Tipo do CT-e OS**igual a "Excesso de Bagagem", em CTRC | CTRC Saída, na tela **Notas Fiscais Conhec. Transporte**, caso o campo **Tipo de Documento** seja informado com um tipo de documento referente a CT-e (FTDO.CODMODDOC igual a 57), não exibir as abas **Informações Contingência** e **Documento Auxiliar Eletrônico**.
* Quando **Tipo do CT-e OS**igual a "Excesso de Bagagem", em CTRC | CT-e, não exibir a opção **Informações de Percurso**.

Envio do XML

* Quando **Tipo do CT-e OS**igual a "Excesso de Bagagem",  o grupo de informações "infPercurso" não deve ser preenchido.
* Quando **Tipo do CT-e OS**igual a "Excesso de Bagagem", o grupo de informações "toma" é opcional. Se o campo **Cliente/Fornecedor Tomador** (TMOVTRANSP.TOMADORCODCFO) for informado no movimento, preencher o grupo, caso contrário não preencher.
* Quando **Tipo do CT-e OS**igual a "Excesso de Bagagem", o grupo de informações "infQ"  é opcional. Se o campo **Quantidade** (TMOV.QUANTIDADE) do GroupBox **Volume** estiver informado, preencher o grupo, caso contrário não preencher.

* Quando **Tipo do CT-e OS**igual a "Excesso de Bagagem", o grupo de informações "infDocRef" é obrigatório. Preencher com as informações do(s) CT-e(s) e/ou documento(s) referenciados em CTRC Saída. Para cada CT-e/documento referenciado:

| tag | Tipo | Obrigatoriedade | Tamanho | Campo RM |
| --- | --- | --- | --- | --- |
| nDoc | Caracter | Obrigatória | 1 - 20 | TCTRC.NUMERODOC |
| serie | Caracter | Opcional | 1 - 3 | TCTRC.SERIEDOC, se informado |
| subserie | Caracter | Opcional | 1 - 3 | TCTRC.SUBSERIEDOC, se informado |
| dEmi | Data | Obrigatória | 10 | TCTRC.DATAEMISSAO |
| vDoc | Numérico | Opcional | 13,2 | TCTRC.VALORTOTAL, se informado |

* Quando **Tipo do CT-e OS**igual a "Excesso de Bagagem", o grupo de informações "infModal" é obrigatório.
* Os demais grupos de informações não citados nessa especificação não sofrem alteração em relação a forma como já são gerados para os outros tipos de CT-e OS que estão no mercado.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [ACAA040 – Parâmetros] | [Alteração] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA050 – Negociação Financeira] | [Envolvida] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA060 – Cadastro de Pedidos] | [Criação] | [Atualizações -> Acadêmico-> Cadastros] | - |

**Tabelas Utilizadas**

* + TTMVEXT - Tipos de Movimento
  + TMOV - Movimentos
  + TCTRC - Notas Fiscais Conhec.Transporte
  + TMOVTRANSP - Dados de Transporte

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
