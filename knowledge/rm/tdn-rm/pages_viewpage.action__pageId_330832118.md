---
content_hash: d6c2fe8c51453fb89ed1895d02e1604c8b1826ecfbf862ffa4a8ed7899be1513
fetched_at: '2026-06-29T00:08:49.455525+00:00'
page_id: '330832118'
product: rm
source: tdn-rm
title: 1506490 FISCAL01-3124 DT  EFD Contribuições F100 Aplicações Financeiras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=330832118
version: 1
---

# EFD Contribuições

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Rotina Federal EFD Contribuições |
| **Situação/Requisito:** | Ao gerar a rotina EFD Contribuições é apresenta a seguinte mensagem:  [11:10:32] ====================================================== [11:10:32] Ocorreu um erro inesperado na geração. [11:10:32]  [11:10:32] System.NullReferenceException [11:10:32] Erro: Referência de objeto não definida para uma instância de um objeto. [11:10:32] ====================================================== [11:10:32] em RM.Gen.Runtime.GenRuntimeModule.InsereRegistro0500\_GetRegistrosF100EFDPisCofins(FisContribuicoesDocsNEscrituradosCxt GetRegistrosF100EFDPisCofinsItem) em RM.Gen.Runtime.GenRuntimeModule.OnExecute(List`1 files) em TNF.Gen.Runtime.RuntimeModule.Execute() [11:10:32] ====================================================== [11:10:32] Geração concluída com erros. Duração: 0:0:16,367  TESTES REALIZADOS:  Tentativa de geração da rotina EFD Contribuições no período 11/2017, ao executar a rotina é apresentado a mensagem:  Erro: Referência de objeto não definida para uma instância de um objeto. [11:10:32] ====================================================== [11:10:32] em RM.Gen.Runtime.GenRuntimeModule.InsereRegistro0500\_GetRegistrosF100EFDPisCofins(FisContribuicoesDocsNEscrituradosCxt GetRegistrosF100EFDPisCofinsItem) em RM.Gen.Runtime.GenRuntimeModule.OnExecute(List`1 files) em TNF.Gen.Runtime.RuntimeModule.Execute() |
| **Solução/Implementação:** | No layout EFD Contribuições o registro 0500 foi tratado para que não exiba inconsistência quando o registro F100 apresentar conta nula. |
| **Conversores e Parâmetros:** | Informe os conversores/parâmetros. |
| **Tickets relacionados:** | Não se Aplica |
| **Requisito:** | FIS000385 |
| **Documento de Referência:** | Não se Aplica |
