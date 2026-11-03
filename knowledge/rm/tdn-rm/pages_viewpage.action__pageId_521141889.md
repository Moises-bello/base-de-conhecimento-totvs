---
content_hash: 1d4cae6900ea0dd066282ea18e5f33aff61ae578fbac99fa2f4ba5c7c8191f88
fetched_at: '2026-06-29T00:10:31.288296+00:00'
page_id: '521141889'
product: rm
source: tdn-rm
title: FISCAL01-11432 DT Cadastro dos Imóveis Rurais - Cadastro Filiais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=521141889
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | Filiais |
| Ticket: | FISCAL01-11432 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11432 |

## **02. SITUAÇÃO/REQUISITO**

Eu, como Analista Financeiro, necessito informar os campos de pertinentes aos imóveis rurais na aplicação:

1. Flag para indicação se é uma propriedade rural  
2. CAFIR (Com DV),  
3.Cadastro de Atividade Econômica da Pessoa Física.

Os mesmos serão usados na rotina Livro Caixa digital do produtor rural.  
**CRITÉRIOS DE ACEITE:**

●Imóvel rural foi mapeado como um registro de Filial  
●CAFIR - Cadastro de Imóveis Rurais (Com DV): alfanumérico com 8 caracteres  
●Cadastro de Atividade Econômica da Pessoa Física com tamanho de 18 caracteres (14 caracteres +  
formatação): NNN.NNN.NNN/NNN-NN  
●Versão atual (12.1.27)

## **03. SOLUÇÃO**

No BackOffice -> Gestão Fiscal -> Cadastros (Globais) -> Filiais -> [Novo] -> Dados Adicionais, foi criado os seguintes campos:

●Flag “​Propriedade Rural”  
●Campo CAFIR com 8 caracteres  
●Campo ​ Cadastro de Atividade Econômica da Pessoa Física com 18 caracteres e seguinte formatação de  
máscara: NNN.NNN.NNN/NNN-NN

## **04. DEMAIS INFORMAÇÕES**

Disponível apenas a partir da versão 12.1.27. Necessário executar a marcação de script LI.2019.11\_01
