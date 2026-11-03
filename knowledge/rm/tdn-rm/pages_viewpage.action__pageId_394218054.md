---
content_hash: 5d3284e86b6083bef31defa458df732fbae557911d6e79ad07e5a811608283e8
fetched_at: '2026-06-29T00:09:09.941781+00:00'
page_id: '394218054'
product: rm
source: tdn-rm
title: 3698357 FOPCALCULO01-4576 Importação de Dados Cadastrais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=394218054
version: 1
---

# Importação de Dados Cadastrais

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Importação de Dados do RM Labore |
| **Situação/Requisito:** | Ao executar o conceito para importação de funcionários foi simulado o erro apresentado pelo cliente.  Validando a rotina via código, foi identificado que o incidente ocorre no momento de inclusão do Funcionário, quando o DataServer FopFuncData executa sua função de DoSaveRecord (salvar registro). Ao executar essa função, o sistema identifica a quantidade de linhas do arquivo XML informado no conceito. Para cada registro retornado o sistema faz validações para identificar se a pessoa associada já existe. Caso não exista ele insere uma nova linha relacionada à pessoa, caso sim faz a junção de campos da linha existente com os novos campos retornados.  O incidente ocorre porque a cada linha de pessoa que o sistema insere, ele adiciona a linha do funcionário ao conjunto de informações. Então em uma próxima validação, o sistema valida se esse conjunto de informações do funcionário já possui registro. Caso sim ele parte para junção. Porém nesse caso a junção não é válida devido chaves divergentes, apresentado então o erro. |
| **Solução/Implementação:** | Ajustado a importação de funcionários via conceito |
| **Tickets relacionados:** | 3698357 |
