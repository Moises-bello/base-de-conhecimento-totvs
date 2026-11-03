---
content_hash: cda538481c3f94797c908b4c0fb2aee3ae0999f1514d932180c51820269de123
fetched_at: '2026-07-02T19:24:26.820161+00:00'
page_id: '654947802'
product: protheus
source: tdn-tec
title: 7 - Resultados Testes
type: documentation
url: https://tdn.totvs.com/display/tec/7+-+Resultados+Testes
version: 7
---

Uma das características mais marcantes do **PROBAT** é sua capacidade de armazenar dados históricos de todas as suas execuções.

Para que isso seja possível, o PROBAT grava as informações em um Banco de Dados relacional, podendo ser:

* SQLite
* DBAccess **(\*\*)**

A utilização do SQLite é seu modo natural, portanto nem há necessidade de configuração pois nativamente o PROBAT já criará um BD na pasta *db\_sys* em seu diretório de funcionamento, seja *root path* ou *start path*.

Para saber como configurar o Banco de Dados, acesse: [Configurando BD](https://tdn.totvs.com/display/tec/a+-+Configurando+Banco+de+Dados)

Devido a esse recurso, ao exportar um resultado podemos unificar uma ou mais execuções, tornando o resultado único entre todas as execuções.  
Saiba mais em: [tlpp.probat.export()](https://tdn.totvs.com/pages/viewpage.action?pageId=656073816)

ÍndiceDisponibilidade

**(\*\*)** Somente a partir do AppServer 20.3.1.14 e tlppCore 01.04.05 os dados podem ser gravados em Banco de Dados relacional através do DBAccess e não somente em SQLite.
