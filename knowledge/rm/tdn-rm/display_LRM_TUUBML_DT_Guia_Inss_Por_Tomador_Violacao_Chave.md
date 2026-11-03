---
content_hash: ca520eb66d0a84638bb7d393e9405b95cc0817607ff88e43b35372b867401527
fetched_at: '2026-06-29T00:08:13.545147+00:00'
page_id: '244426042'
product: rm
source: tdn-rm
title: TUUBML_DT_Guia_Inss_Por_Tomador_Violacao_Chave
type: documentation
url: https://tdn.totvs.com/display/LRM/TUUBML_DT_Guia_Inss_Por_Tomador_Violacao_Chave
version: 117
---

# GUIA DE INSS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Guia de INSS por Tomador* |
| **Situação/Requisito:** | Ao gerar Guia de INSS marcando o parâmetro Guia por tomador, sistema retorna mensagem de erro:  Processo finalizado com Erros e/ou Avisos.  System.Data.ConstraintException: A coluna 'CODIGO, SECAO, CODCOLIGADA' está restrita a conter valores exclusivos. O valor '11.111.111/0001-11, 01, 1' já existe. |
| **Solução/Implementação:** | *Ajustado a geração da guia de inss por tomador quando o tomador empresa tem mais de um cei vinculado aos funcionários.* |
| **Chamados relacionados:** | *TUUBML* |

divs
