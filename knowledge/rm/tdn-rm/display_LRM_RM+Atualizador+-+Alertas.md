---
content_hash: b7a6b92666e59e9a65e05da5f09025bda6989ea4e0ce938c6f990ad5cba0bb1b
fetched_at: '2026-06-29T00:12:07.358915+00:00'
page_id: '923582285'
product: rm
source: tdn-rm
title: RM Atualizador - Alertas
type: documentation
url: https://tdn.totvs.com/display/LRM/RM+Atualizador+-+Alertas
version: 16
---

| Duplicidade de Nomes na Criação de Tabelas e Índices |
| --- |
| Durante o processo de conversão da base de dados, a rotina de criação de novas estruturas realiza validações prévias de nomenclatura. Caso seja identificada uma tentativa de criar uma tabela ou índice utilizando o nome de um objeto já existente no banco, o sistema avaliará a equivalência das estruturas para determinar o tratamento adequado no log.   **Log de Aviso**   * Ocorre quando a estrutura do objeto colidente é estritamente idêntica à que seria criada:    + **No caso de índices:** o índice precisa utilizar as mesmas colunas, exatamente na mesma ordem.   + **No caso de tabelas:** todas as características das colunas precisam ser idênticas para que a falha seja convertida em um alerta.     Caso contrário, a falha identificada pelo SGBD será reportada como erro e bloqueará a base de dados, conforme ocorre nas demais situações. |

| Alerta de alteração em colunas que possuem índices e/ou estatísticas associadas ( Sql Server ) |
| --- |
| Em alguns casos, durante a atualização da base de dados, um script pode ser impedido de modificar uma coluna devido à presença de objetos associados, como índices ou estatísticas.  Quando isso ocorre, é necessário avaliar e remover temporariamente esses objetos para que a conversão da base seja concluída com sucesso. |
