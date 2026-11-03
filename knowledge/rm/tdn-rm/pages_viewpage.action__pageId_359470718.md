---
content_hash: 71fb5fe608ec213d244d9afabb3b1ae3c22c09fb1aebb1b337566c6aae0102b0
fetched_at: '2026-06-29T00:08:58.088179+00:00'
page_id: '359470718'
product: rm
source: tdn-rm
title: 2690004 FISCAL01-4423 DT Geração de Registro TAF - REINF - GenRuntimeModule.InsereT078
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=359470718
version: 1
---

# Geração de Registro TAF - REINF - GenRuntimeModule.InsereT078

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Geração de Registro TAF |
| **Situação/Requisito:** | Ao executar o processo de "Geração de Registros - TAF Fiscal" foi apresentada a seguinte mensagem:  [16:21:05] ====================================================== [16:22:16] ====================================================== [16:22:16] Ocorreu um erro inesperado na geração. [16:22:16]  [16:22:16] System.NullReferenceException [16:22:16] Erro: Referência de objeto não definida para uma instância de um objeto. [16:22:16] ====================================================== [16:22:16] em RM.Gen.Runtime.GenRuntimeModule.InsereT078AC\_ListaItem(T078ABRecord T078AB, FisItemLancamentoCxt ListaItemItem, FisTotalizadores ListaTotalizadoresItem, FisLancamentoFiscalCxt GetTodosLancamentosItem) em RM.Gen.Runtime.GenRuntimeModule.InsereT078AB\_ListaTotalizadores(T078AARecord T078AA, FisTotalizadores ListaTotalizadoresItem, FisLancamentoFiscalCxt GetTodosLancamentosItem) em RM.Gen.Runtime.GenRuntimeModule.InsereT078AA\_GetTodosLancamentos(T078Record T078, FisLancamentoFiscalCxt GetTodosLancamentosItem) em RM.Gen.Runtime.GenRuntimeModule.InsereT078\_GetTodosLancamentos(FisLancamentoFiscalCxt GetTodosLancamentosItem) em RM.Gen.Runtime.GenRuntimeModule.OnExecute(List`1 files) em TNF.Gen.Runtime.RuntimeModule.Execute() [16:22:16] ====================================================== [16:22:16] Geração concluída com erros. Duração: 0:1:10,832 |
| **Solução/Implementação:** | Ajuste no processo de Geração dos Registros para o TAF para que o Registro T078AC não apresente o erro informado e passe a ser gerado corretamente |
| **Conversores e Parâmetros:** | Não se Aplica |
| **Documento de Referência:** | Não se Aplica |
