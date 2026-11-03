---
content_hash: 8bc3b1bb023f29d74db1cae18d091c85176b98e6a0a6e335a3eb1e971e77f745
fetched_at: '2026-07-02T19:24:23.444474+00:00'
page_id: '450141818'
product: protheus
source: tdn-tec
title: Seção [BTMonitorAppD] - Chave LogMaxNumFiles
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450141818
version: 3
---

Define o número máximo de arquivos de log por nó gerados pelo Agente da AppDynamics.

## Valores válidos

| Valor | Descrição |
| --- | --- |
| 10 (Padrão) | Define como 10 o número máximo de arquivos de log por nó gerados pelo Agente da AppDynamics. |
| > 0 | Define o número máximo de arquivos de log por nó gerados pelo Agente da AppDynamics. |

## Observações

* Após atingido o número máximo estabelecido, os arquivos de log existentes serão rotacionados, fazendo com que o mais antigo seja excluído para que um mais novo seja criado;
* Um novo arquivo de log será criado quando o Agent for inicializado ou quando o tamanho máximo for atingido, conforme .

## Exemplo

Define como **5** o número máximo de arquivos de log por nó gerados pelo Agente da AppDynamics:

## Abrangência

Builds [17.3.0.8](http://tdn.totvs.com/display/tec/Application+Server+-+17.3.0.8).

## Veja também
