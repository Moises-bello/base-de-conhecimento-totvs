---
content_hash: 889228111c9570e14cb98a892940579769790e1f1594f7b6200cd1c0d1bfc4e8
fetched_at: '2026-06-29T00:06:30.280786+00:00'
page_id: '235318434'
product: rm
source: tdn-rm
title: TUMJSJ_DT_Cadastro_Plano_Contas_Integracao_Mensageria_Unica
type: documentation
url: https://tdn.totvs.com/display/LRM/TUMJSJ_DT_Cadastro_Plano_Contas_Integracao_Mensageria_Unica
version: 120
---

# INTEGRACAO EDUCACIONAL X PROTHEUS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | *Integração Educacional x Protheus* |
| **Situação/Requisito:** | *Cadastro de plano de conta, através da mensagem AccountAntAccount - 2.000, não era realizado devido um erro de validação de coligada na tabela De-Para.* |
| **Solução/Implementação:** | *A alteração da informação utilizada na tag CODCOLIGADA do XSLT gerou um impacto na transformação e a validação não era realizada forma correta. Foi criada mais uma tag no XSLT da transformação para receber o CompanyInternalID que será utilizado para validar se a coligada está cadastrada na tabela De-Para, utilizando a GFILIAL.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
