---
content_hash: 9ca7b4a47d3acf3226cfcf23d798cf7335feee780d462517d7cfa023151fe92e
fetched_at: '2026-06-29T00:06:03.953468+00:00'
page_id: '200903309'
product: rm
source: tdn-rm
title: TSPERX_DT_Cadastro_de_responsavel_financeiro_com_tipo_cliente_fornecedor_global_11_82_40
type: documentation
url: https://tdn.totvs.com/display/LRM/TSPERX_DT_Cadastro_de_responsavel_financeiro_com_tipo_cliente_fornecedor_global_11_82_40
version: 2
---

# RESPONSÁVEL FINANCEIRO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional.* |
| **Módulo:** | *TOTVS Gestão Educacional.* |
| **Função:** | *Cadastro de responsável financeiro com tipo cliente fornecedor global.* |
| **Situação/Requisito:** | *Ao cadastrar o responsável financeiro, é exibida uma m*ensagem incoerente* com a parametrização de tipo de cliente fornecedor. Isto ocorre porque*  *a* *recuperação dos tipos de cliente fornecedor na tela de parâmetros de tesouraria não leva em consideração o parâmetro "Default Cli/For Global" do*  *financeiro.* |
| **Solução/Implementação:** | *Inclusão de verificação do parâmetro "Defaul Cli/For Global" do financeiro para recuperar os tipos de cliente fornecedor. Desta forma, quando o*  *parâmetro estiver marcado, são recuperados os tipos de cliente fornecedor da coligada global, e quando estiver desmarcado, os tipos de cliente*  *fornecedor são da* *coligada* *do contexto.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *11.82.40.* |
