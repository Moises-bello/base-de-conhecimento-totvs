---
content_hash: c09b74ab311580bf72fd1d14bc3cbe9f99ef774137ede9942cf1574e1a15683f
fetched_at: '2026-06-29T00:06:03.993352+00:00'
page_id: '200903976'
product: rm
source: tdn-rm
title: TT9635_DT_Cadastro_de_responsavel_financeiro_com_tipo_cliente_fornecedor_global_12_1_7
type: documentation
url: https://tdn.totvs.com/display/LRM/TT9635_DT_Cadastro_de_responsavel_financeiro_com_tipo_cliente_fornecedor_global_12_1_7
version: 3
---

# RESPONSÁVEL FINANCEIRO

|  |  |
| --- | --- |
| **Linha de Produto:** | **RM*.* |
| **Segmento:** | *Educacional.* |
| **Módulo:** | *TOTVS Gestão Educacional.* |
| **Função:** | *Cadastro de responsável financeiro com tipo cliente fornecedor global.* |
| **Situação/Requisito:** | *Ao cadastrar o responsável financeiro, é exibida uma m*ensagem incoerente*com a parametrização de tipo de cliente fornecedor. Isto ocorre porque*  *a**recuperação dos tipos de cliente fornecedor na tela de parâmetros de tesouraria não leva em consideração o parâmetro "Default Cli/For Global" do*  *financeiro.* |
| **Solução/Implementação:** | *Inclusão de verificação do parâmetro "Defaul Cli/For Global" do financeiro para recuperar os tipos de cliente fornecedor. Desta forma, quando o*  *parâmetro estiver marcado, são recuperados os tipos de cliente fornecedor da coligada global, e quando estiver desmarcado, os tipos de cliente*  *fornecedor são da**coligada**do contexto.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | **N/A.** |
| **Versões/Release:** | *12.1.7.* |
