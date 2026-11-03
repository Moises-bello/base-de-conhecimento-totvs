---
content_hash: b0a1ed55e074a0a42a45f60fc68787d89237665857ceff1e108449bd8f889146
fetched_at: '2026-06-29T00:08:17.056624+00:00'
page_id: '251494471'
product: rm
source: tdn-rm
title: TVMRA3_DT_Responsavel_Vinculo_Validacao_Campos_Obrigatorios
type: documentation
url: https://tdn.totvs.com/display/LRM/TVMRA3_DT_Responsavel_Vinculo_Validacao_Campos_Obrigatorios
version: 111
---

# CADASTRO DE RESPONSÁVEIS - PORTAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Processo Seletivo* |
| **Função:** | *Cadastro de responsáveis - Portal* |
| **Situação/Requisito:** | *Ao cadastrar um responsável que já existe como pessoa e possui algum vínculo com a instituição (funcionário, professor ou aluno) o sistema tenta validar campos obrigatórios no processo seletivo que o responsável não possui preenchido no cadastro de pessoa, porém por ter vínculo com a instituição, estes não podem ser alterados, assim, a validação impede a conclusão do cadastro.* |
| **Solução/Implementação:** | **Foi feito um ajuste para que assim que for identificado que o responsável já existe, seja verificado se possui vínculo com a instituição, possuindo, a obrigatoriedade não é valida pelo lado do processo seletivo não será validada, validando somente o que for obrigatório pelo cadastro de pessoa, pois assim a alteração dos dados só poderá ser feito pela área responsável, evitando que o responsável altere seus dados sem permissão.** |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
