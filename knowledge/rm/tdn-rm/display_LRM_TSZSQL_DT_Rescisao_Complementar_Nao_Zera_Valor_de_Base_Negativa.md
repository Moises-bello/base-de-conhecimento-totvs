---
content_hash: c0939a89157da8ad0217a8786d6e18d341e6fe1e8ed485253999bdb25cc6bd48
fetched_at: '2026-06-29T00:06:12.953218+00:00'
page_id: '207355976'
product: rm
source: tdn-rm
title: TSZSQL_DT_Rescisao_Complementar_Nao_Zera_Valor_de_Base_Negativa
type: documentation
url: https://tdn.totvs.com/display/LRM/TSZSQL_DT_Rescisao_Complementar_Nao_Zera_Valor_de_Base_Negativa
version: 1
---

# RESCISÃO COMPLEMENTAR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão Complementar* |
| **Situação/Requisito:** | *A gerar uma rescisão complementar por dissídio, o valor do evento de CC 69 não estava sendo composto da forma correta, pois os valores das verbas que o compoe estavam negativos, somando à base de FGTS. O comportamento correto é que, caso a verba de composição da base de FGTS seja um valor negativo, que não seja acumulado nenhum valor, ao invés de continuar negativo.* |
| **Solução/Implementação:** | *Zerar o valor do evento que se encontra negativo no momento de compor a base de FGTS da rescisão complementar para que esta não fique com valor negativo, causando o problema de não levar os valores corretos na SEFIP 650.* |
| **Chamados relacionados:** | TSZSQL |
| **Versões/Release:** | *11.82.41* |
| **Versão Corrigida:** | *11.82.41* |
| **Versão Expedida:** | *11.82.41* |
