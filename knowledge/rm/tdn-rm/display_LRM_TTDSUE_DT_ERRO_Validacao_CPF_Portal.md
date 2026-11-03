---
content_hash: 22ebf009215c651cbcdeb50051a009e5883793d4505e1fdd50557f5e2e975896
fetched_at: '2026-06-29T00:06:11.444696+00:00'
page_id: '203769543'
product: rm
source: tdn-rm
title: TTDSUE_DT_ERRO_Validacao_CPF_Portal
type: documentation
url: https://tdn.totvs.com/display/LRM/TTDSUE_DT_ERRO_Validacao_CPF_Portal
version: 3
---

# INSCRIÇÃO DE CANDIDATO (PORTAL)

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS - Processo Seletivo* |
| **Função:** | *Inscrição de Candidato (portal)* |
| **Situação/Requisito:** | *Mesmo mantendo o parâmetro CPF como opcional, ao alterar a seleção do estado natal, o campo CPF está sendo decorado como obrigatório.* |
| **Solução/Implementação:** | *A rotina para validar a obrigatoriedade do CPF para estrangeiros estava realizando uma validação inválida. Foi realizado o ajuste deste método para permtir o correto funcionamento do controle.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.8* |
