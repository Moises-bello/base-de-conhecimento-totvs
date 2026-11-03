---
content_hash: 64a63f325da28322105a27744cedde5430e37127bd2ef7cc01c619b6da05ef25
fetched_at: '2026-06-29T00:08:58.081384+00:00'
page_id: '359469653'
product: rm
source: tdn-rm
title: 2659641 FISCAL01-4388 DT Geração do registro T003 do TAF Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=359469653
version: 1
---

# Geração do Registro T003 do TAF Fiscal erro de Referência de objeto não definida para uma instância de um objeto

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Totvs Gestão Fiscal |
| **Função:** | TAF Fiscal |
| **Situação/Requisito:** | Na geração da Integração RM x TAF ocorre a seguinte mensagem no log:  [09:13:24] ====================================================== [09:13:24] Ocorreu um erro inesperado na geração. [09:13:24]  [09:13:24] System.NullReferenceException [09:13:24] Erro: Referência de objeto não definida para uma instância de um objeto. [09:13:24] ====================================================== [09:13:24] em RM.Gen.Runtime.GenRuntimeModule.InsereT003\_GetRegistrosF100EFDPisCofins(FisContribuicoesDocsNEscrituradosCxt GetRegistrosF100EFDPisCofinsItem) em RM.Gen.Runtime.GenRuntimeModule.OnExecute(List`1 files) em TNF.Gen.Runtime.RuntimeModule.Execute() |
| **Solução/Implementação:** | Alteração na geração do registro T003, alteração na validação do preenchimento do campo IE pois o mesmo não é obrigatório e como estava nulo no cadastro do participante gerava erro de Referência de objeto não definida para uma instância de um objeto. |
