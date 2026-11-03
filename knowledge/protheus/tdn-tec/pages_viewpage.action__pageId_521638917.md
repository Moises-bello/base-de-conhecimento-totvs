---
content_hash: 58d9aed9a609a1ae63940dd7f4c6a8dbfce73c133a4cbe462155ec83363b2a79
fetched_at: '2026-07-02T19:24:26.607036+00:00'
page_id: '521638917'
product: protheus
source: tdn-tec
title: Erro ao criar um TCBrowse com variáveis no bLine que não foram criadas antes
  do refresh de tela
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=521638917
version: 1
---

|  |  |
| --- | --- |
| Ocorrência | Criando um TCBrowse que no bLine possui variáveis que são criadas apenas depois do refresh de tela, ocorre erro no refresh por executar o bLine. |
| Correção | O refresh continua chamando a criação do TCBrowse com suas colunas, porém não executa o bLine. |
| Informações adicionais | * Referente ao chamado: DTAPPSRV-767 * Disponível em builds iguais ou superiores a [13.1.3.49](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.1.3.49) e [13.2.3.49](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.2.3.49). |
