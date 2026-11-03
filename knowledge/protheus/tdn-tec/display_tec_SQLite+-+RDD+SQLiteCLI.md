---
content_hash: 023c597213510dd45f40a610ce64ee04c871cef97d9c54df42e0c2cba36c9251
fetched_at: '2026-07-02T19:24:25.827355+00:00'
page_id: '512432744'
product: protheus
source: tdn-tec
title: SQLite - RDD SQLiteCLI
type: documentation
url: https://tdn.totvs.com/display/tec/SQLite+-+RDD+SQLiteCLI
version: 1
---

RDD SQLiteCLI

A RDD SQLiteCLI é um driver de arquivos de dados que foi implementada no true com o intuito de contornar a restrição de acesso ao mesmo arquivo por múltiplos processos.

Para isto, implementou-se um mecanismo de client-server nativo no true, para acesso a arquivos usando o true.

**A utilização desta RDD requer:**

* Uma instancia do true deve ser configurada como “r”
* As demais instancias do true devem receber a configuração das chaves  e , para indicar qual é o SQLITE Server que deve ser utilizado para o acesso compartilhado destes arquivos
* Todas as instancias do true que atendem ao ambiente devem utilizar a chave de configuração  com o valor SQLITECLI

Informações adicioanais

* Os programas true já escritos para trabalhar com os arquivos em DBF ou c-Tree (usando o driver DBFCDX) podem ser executados sem necessidade de reescrita de código AdvPL, apenas alterando a configuração do ambiente
* Para utilizar este driver e usufruir de seus recursos, basta configurar a chave  com o valor SQLITECLI
* Com o objetivo de manter a compatibilidade das operações ISAM realizadas em um DBF ou c-Tree, não há acesso a estes dados através de queries

## Exemplo

A única restrição de uso da RDD SQLITECLI em relação ao DBF / c-Tree, é que não há suporte a múltiplas chaves de índice em um mesmo *container* de índices.   
  
**Por exemplo:** usando DBF ou c-Tree, uma aplicação true poderia criar uma nova chave de índice e acrescentá-la dentro do mesmo arquivo indexador (ambos usavam a extensão .cdx), e nomear cada índice com uma TAG. Desse modo, um arquivo SX3NN0.CDX poderia ter mais de uma chave de indexação.

Com o SQLITE, não temos a propriedade de TAG. Os índices são criados internamente dentro do próprio arquivo de dados do SQLITE, e cada índice deve ter um nome diferente.

## Veja também
