---
content_hash: 93b461de072a26d441df564668d4ea310e10b8179f90eb796133d6c94a162828
fetched_at: '2026-06-29T00:10:42.898400+00:00'
page_id: '547876371'
product: rm
source: tdn-rm
title: FISCAL01-12875 DT Copia de Natureza de Operação (CFOP)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=547876371
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Exercício Fiscal |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12875 |

## **02. SITUAÇÃO/REQUISITO**

Criar o processo de cópia entre Coligadas para o cadastro de Natureza de Operação

## **03. SOLUÇÃO**

Foi adicionado um novo processo no cadastro de Naturezas de Operação para realizar a cópia dos registros entre Coligadas

Regras:

* Ao realizar a cópia de uma Natureza não global (Por Filial), a cópia só será realizada se existir uma Filial de mesmo código na Coligada de Destino;
* Serão atribuídas à Natureza na Coligada de Destino Regras de ICMS e IPI que possuírem o mesmo código das Regras existentes na Natureza na Coligada de Origem;
* Será atribuído à Natureza na Coligada de Destino o Exercício que possua período coincidente com o período da Coligada de Origem, de acordo com a seguinte regra:
  + Será selecionado um exercício na Coligada de Destino que possua **Data Inicial menor** ou igual a Data Inicial do Exercício de Origem e **Data Final maior** ou igual a Data Final do Exercício de Origem;
* Se a Máscara do Exercício de Destino for diferente da Máscara do Exercício de Origem a Natureza não será copiada;
* O processo realiza copia somente entre Coligadas

Tratamento das Chaves Estrangeiras:

* Caso a Natureza esteja parametrizada com Regra de Dependência para Estado, este Estado será setado na Natureza da coligada de destino;
* Caso a Natureza esteja parametrizada com Regra de Dependência para Região, será buscado o ID da Região na coligada de destino com o mesmo Código da Região utilizada na Natureza na coligada de origem;
* Caso a Natureza esteja parametrizada com Regra de Dependência para Grupo de Municípios, será buscado o ID do Grupo de Municípios na coligada de destino com o mesmo Código do Grupo de Municípios utilizado na Natureza na coligada de origem.
