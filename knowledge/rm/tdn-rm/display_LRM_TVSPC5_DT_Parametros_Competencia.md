---
content_hash: a56af7ddf9682538ccce89743fd228c955659ea7ff1c00ffe60a6d2afb6198ab
fetched_at: '2026-06-29T00:08:18.722640+00:00'
page_id: '266966796'
product: rm
source: tdn-rm
title: TVSPC5_DT_Parametros_Competencia
type: documentation
url: https://tdn.totvs.com/display/LRM/TVSPC5_DT_Parametros_Competencia
version: 111
---

# PARÂMETROS DE COMPETÊNCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Parâmetros da* *competência* |
| **Situação/Requisito:** | Ao realizar o processo de Liberação da competência com os seguintes parâmetros:  Competência : 09/2016  Caixa : 10/2016  Dia do pagamento 31 (devido ao mês caixa ser 10)  Depois da competência liberada com os parâmetros acima e acessar o parametrizador , e informar o mês caixa como 9, mês que não tem 31 dias, o sistema não estava realizando a validação desta data, fazendo com que fosse gerasse erro ao acessar o envelope de pagamento devido ao mês não possuir esta data de pagamento que foi informada. |
| **Solução/Implementação:** | Foi ajustado o sistema para que no momento em que for alterado o campo de mês caixa o sistema valide se o mês caixa esta coerente com a data de pagamento. |
| **Chamados relacionados:** | TVSPC5 |

divs
