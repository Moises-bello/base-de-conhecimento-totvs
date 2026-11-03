---
content_hash: e77c3194b22b14c305c7f51d1cdcc748a12fc02efb4306ee3af31427f0d90822
fetched_at: '2026-06-29T00:12:13.451806+00:00'
page_id: '956646458'
product: rm
source: tdn-rm
title: DT - Tornar fracionáveis os processos de importação e consulta de arquivos
  do TPF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=956646458
version: 6
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | TOTVS Processos Fiscais (TPF) |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-26025 e FISCAL01-26022 |

## **02. SITUAÇÃO/REQUISITO**

Permitir o fracionamento dos processos de Envio, Importação e Consulta de arquivos XML do TPF.

## **03. SOLUÇÃO**

Os processos de Envio, Importação e Consulta podem ser fracionados no momento da execução.

Caso o usuário não tenha feito o cadastro de segurança de jobs fracionáveis para as classes dos processos a execução ocorre normalmente até o limite de registros de cada processo. Se a quantidade de registros ultrapassar o limite apenas os registros abaixo do limite serão processados e uma mensagem será exibida no log do processo informando a quantidade de registros processados e a necessidade do cadastro do fracionamento para o processamento de um número maior de registros por cada execução dos processos.

Limites por Processo:

* Envio: 1000
* Importação: 900
* Consulta: 900

Exemplo de log com erro

Os processos determinam a quantidade de frações necessárias dinamicamente conforme a quantidade de registros sendo processados.

Mais informações na .

Disponível a partir da biblioteca 12.1.2410
