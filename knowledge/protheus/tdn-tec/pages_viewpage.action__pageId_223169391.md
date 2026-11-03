---
content_hash: ed13527ac317e27e595faad1c7cf4c9abe080c2e9bfde74ab249549efa746ecc
fetched_at: '2026-07-02T19:24:18.999426+00:00'
page_id: '223169391'
product: protheus
source: tdn-tec
title: Melhoria - Verificação de Repositório na primeira execução
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223169391
version: 2
---

A partir da build 7.00.131227a, com data de geração igual ou superior a , foi inserida uma verificação executada na carga do repositório.

|  |  |
| --- | --- |
| Situação | Utilização de repositório onde houve falha de um ou mais fontes em uma compilação por lote. |
| Ocorrência | Caso uma compilação em lote, de múltiplos fontes AdvPL, apresentasse falha em algum código, os fontes compilados com sucesso eram gravados no repositório, porém o fonte que apresentou falha precisa ser recompilado. Caso o fonte em questão não fosse re-compilado, somente seria apresentado erro na carga do fonte quando alguma função desse fonte fosse chamada. |
| Melhoria | Na entrada do primeiro usuário em um ambiente, na carga do índice do repositório de objetos (RPO), é verificado se existe algum fonte com compilação incompleta no repositório. Caso um ou mais fontes estejam nesta condição, será gerada uma mensagem de aviso, gravada no log de console do true. |
| Informações adicionais | * Não há chamado relacionado. * Melhoria feita em conformidade com o processo de melhoria contínua da aplicação. * Disponível a partir da build 7.00.131227A, com data de geração igual ou superior a |
