---
content_hash: 9b89ec70e70c2c47adf7466bf77e7f390892766998bfb48cb1efaf1229e959f8
fetched_at: '2026-06-29T00:06:22.599635+00:00'
page_id: '223923487'
product: rm
source: tdn-rm
title: TTTJCD_DT_Erro_Ao_Cadastrar_Bolsa
type: documentation
url: https://tdn.totvs.com/display/LRM/TTTJCD_DT_Erro_Ao_Cadastrar_Bolsa
version: 121
---

# INCLUSÃO DE BOLSA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Inclusão de bolsa* |
| **Situação/Requisito:** | *Ao inserir uma bolsa para um contrato que possua várias parcelas com a mesma data de vencimento, o sistema ao validar o total de bolsa atribuído, pode impedir que a bolsa seja inserida no contrato, mesmo que o seu valor seja inferior ao valor das parcelas. O situação ocorre devido o sistema considerar várias parcelas com a mesma data de vencimento como se fosse uma única parcela, somando-se assim o valor das bolsas.* |
| **Solução/Implementação:** | *Foi realizada otimização da validação do valor total de bolsas afim de evitar que uma bolsa com valor superior ao valor da parcela seja inserida no contrato do aluno.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *TTZWT9* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *11.82.43* |
| **Versão Corrigida:** | *11.82.43* |
| **Versão Expedida:** | *11.82.43* |

divs
