---
content_hash: 427e24dabd22d2db562e62fce40f8acb51cc46498d4a62ba18f1e8870417a362
fetched_at: '2026-06-29T00:08:21.343877+00:00'
page_id: '268813048'
product: rm
source: tdn-rm
title: TVYAL9_DT_Processo_Seletivo_Terceirizado_Cadastro_Mae_Obrigatorio
type: documentation
url: https://tdn.totvs.com/display/LRM/TVYAL9_DT_Processo_Seletivo_Terceirizado_Cadastro_Mae_Obrigatorio
version: 114
---

# PROCESSO SELETIVO TERCEIRIZADO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | *Processo seletivo terceirizado* |
| **Situação/Requisito:** | *Ao utilizar o processo seletivo terceirizado para fazer a matrícula, ocorre um erro para alguns candidatos informando que o campo "mãe" é obrigatório, quando o campo mãe é definido como obrigatório no cadastro do aluno.* |
| **Solução/Implementação:** | *Foi identificado que a mensagem é exibida pois o em alguns casos a pessoa "mãe" já existe porém na validação o sistema não encontra corretamente e neste caso tenta inserir novamente, como não consegue inserir retorna a mensagem informando que a mãe é obrigatória. Foi feito o ajuste na validação se mãe/pai existe e o tratamento da mensagem de log informando corretamente o por que do erro no momento do cadastro de mãe/pai caso ocorra alguma inconsistência na operação.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
