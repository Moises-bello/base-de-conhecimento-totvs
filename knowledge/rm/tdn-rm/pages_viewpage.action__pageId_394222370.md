---
content_hash: f3d344dbc0da9eb7c3a789ef048590f798175f8b4e704fc00397ba89b79815a9
fetched_at: '2026-06-29T00:09:09.996802+00:00'
page_id: '394222370'
product: rm
source: tdn-rm
title: DSAUGCIH-280  Validação Status Importação Cultura Parcial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=394222370
version: 1
---

# Alteração do status da importação da Cultura Parcial ao Importar Cultura Final

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Controle de Infecção Hospitalar |
| **Função:** | Utilitários / Importação / Cultura Final |
| **Requisito:** | ao importar uma cultura parcial que já possua culturas parciais importadas(a ligação é feita pelo campo **NUMPEDIDOCULTURA** no layout), o sistema altera o status da importação da cultura parcial de 0(não validado) para 1(validado):. |
| **Solução/Implementação:** | Ao importar uma cultura parcial que já possua culturas parciais importadas(a ligação é feita pelo campo **NUMPEDIDOCULTURA** no layout), o sistema altera o status da importação da cultura parcial de 0(não validado) para 1(validado).  Ao importar a Cultura Final, o status da importação da cultura parcial foi alterado, observando que o sistema não deve alterar o status da importação da cultura Final, e sim somente da cultura Parcial |
