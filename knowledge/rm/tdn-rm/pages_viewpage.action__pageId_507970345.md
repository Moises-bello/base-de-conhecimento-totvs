---
content_hash: 8cf61d706fc133d563008b5e377c408d495a3b3a48843f7c6c08b73a89e6be7e
fetched_at: '2026-06-29T00:10:25.979474+00:00'
page_id: '507970345'
product: rm
source: tdn-rm
title: DT - RHU01-8689 Automatização dos dias de Licença Maternidade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=507970345
version: 1
---

# Automatização dos dias de Licença Maternidade

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | RH |
| **Módulo:** | Gestão de Pessoas |
| **Função:** | Pré-Atestado |
| **Situação/Requisito:** | Assim como é feito hoje no RM, caso o motivo de afastamento seja Licença maternidade preencher o número de dias com 120 dias na tela de solicitação de atestado do Portal. |
| **Solução/Implementação:** | Agora são preenchidos automaticamente o campo **Dias**com o valor 120 e o campo da **data fim** com uma data 120 dias a frente da data início. Além disso foram feitas validações para que os campos referentes a data se comportem da mesma forma que no sistema:   * Trocar a data início mantem o valor do campo Dias e altera o valor do campo da data fim da forma: **data fim = data início + dias** * Trocar campo Dias mantem a data de início e altera o valor do campo da data fim  da forma: **data fim = data início + dias** * Trocar data fim mantem a data início e altera o valor do campo Dias da forma: **dias = data fim - data início** |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | RHU01-8689 |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
