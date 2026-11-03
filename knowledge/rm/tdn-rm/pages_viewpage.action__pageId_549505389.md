---
content_hash: 8e4118105f41bd6ee556dfd24d2155770ed8d30aedfcc2c3e9663f24fcde9484
fetched_at: '2026-06-29T00:10:43.059658+00:00'
page_id: '549505389'
product: rm
source: tdn-rm
title: FISCAL01-12880 DT Cópia de Parâmetros Gerais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=549505389
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Parametrização |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12880 |

## **02. SITUAÇÃO/REQUISITO**

Criar o processo de cópia entre Coligadas para a Parametrização Geral do TOTVS Gestão Fiscal.

## **03. SOLUÇÃO**

Foi adicionado um novo processo de Parametrização Geral do TOTVS Gestão Fiscal para realizar a cópia entre Coligadas.

As FKs existentes no Parametrizador terão o seguinte comportamento:

* **TIPODOCDEFAULT** (Espécie Default): A chave deste lookup é o próprio código e não um ID. Então, não foi necessário efetuar conversão. Verificamos se o registro parametrizado na Coligada de Origem existe na Coligada de Destino para copiá-lo ou enviar Nulo;

* **INDICECOMPFED** (Índice para Compensações de Tributos Federais): Lookup com a tabela GMOEDA. Esta tabela não é por Coligada. Sendo assim, não precisamos nos preocupar. Basta apenas copiar o valor como os demais campos;

* **CODCCUSTOFX** (Centro de Custo Default): A chave deste lookup é o próprio código e não um ID. Então, não foi necessário efetuar conversão. Verificamos se o registro parametrizado na Coligada de Origem existe na Coligada de Destino para copiá-lo ou enviar Nulo;

* **CODTDODARFDEFAULT** (Tipo de Documento Default): A chave deste lookup é o próprio código e não um ID. Então, não foi necessário efetuar conversão. Verificamos se o registro parametrizado na Coligada de Origem existe na Coligada de Destino para copiá-lo ou enviar Nulo;

* **CODCFOFX\CODCOLCFOFX** (Cliente/Fornecedor Default para Guias DARF): A chave deste lookup é o próprio código e não um ID. Então, não foi necessário efetuar conversão. Verificamos se o registro parametrizado na Coligada de Origem existe na Coligada de Destino para copiá-lo ou enviar Nulo;

* **CODFILIALMATRIZ** (Filial Matriz): A chave deste lookup é o próprio código e não um ID. Então, não foi necessário efetuar conversão. Verificamos se o registro parametrizado na Coligada de Origem existe na Coligada de Destino para copiá-lo ou enviar Nulo;

* **CODTDOFX** (Tipo de Documento Default): A chave deste lookup é o próprio código e não um ID. Então, não foi necessário efetuar conversão. Verificamos se o registro parametrizado na Coligada de Origem existe na Coligada de Destino para copiá-lo ou enviar Nulo;

* **NUMEROLOTESALDUS** (Número Lote RMSaldus): A chave deste lookup é o próprio código e não um ID. Então, não foi necessário efetuar conversão. Verificamos se o registro parametrizado na Coligada de Origem existe na Coligada de Destino para copiá-lo ou enviar Nulo;

* **IDCLASSIFMUNICIBGE** (Classificação IBGE Município): Lookup com a tabela DCLASSIFMUNICIPIO. Esta tabela não é por Coligada. Sendo assim, não precisamos nos preocupar. Basta apenas copiar o valor como os demais campos;

* **IDCLASSIFMUNICFEDERAL** (Classificação Federal Município): Lookup com a tabela DCLASSIFMUNICIPIO. Esta tabela não é por Coligada. Sendo assim, não precisamos nos preocupar. Basta apenas copiar o valor como os demais campos;

IMPORTANTE!!!

* O processo não irá tratar os dados específicos para filiais.
