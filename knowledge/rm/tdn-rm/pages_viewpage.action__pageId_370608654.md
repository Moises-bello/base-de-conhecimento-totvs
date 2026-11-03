---
content_hash: 466fb3bdb1aa0cfcb5248c12a535b119f35364691aa3e6eea7899c0a719a4f36
fetched_at: '2026-06-29T00:09:00.929857+00:00'
page_id: '370608654'
product: rm
source: tdn-rm
title: 2969487 FISCAL01-4887 DT Integração RMxTAF - REINF - Referência de objeto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=370608654
version: 2
---

# Integração RM x TAF - REINF - Referência de objeto

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Totvs Gestão Fiscal |
| **Função:** | Geração do Registros TAF Fiscal |
| **Situação/Requisito:** | Ao gerar os registros de integração do RM para com o TAF, é apresentado uma mensagem de inconsistência: Consulta uma cadeia de caracteres localizada semelhante a Não há nenhum registro para ser salvo.  [12:40:09] System.NullReferenceException [12:40:09] Erro: Referência de objeto não definida para uma instância de um objeto. [12:40:09] ====================================================== [12:40:09] em RM.Fis.Sped.FisLancamentoFiscalCxt.<>c\_DisplayClass262\_0.<getParticipanteLanc> b\_1(Fis0150CxtTAF part) em System.Collections.Generic.List`1.FindIndex(Int32 startIndex, Int32 count, Predicate`1 match) em RM.Fis.Sped.FisLancamentoFiscalCxt.getParticipanteLanc(List`1 listaParticipantes,  FisLancamentoFiscalCxt lanc) |
| **Solução/Implementação:** | Ajuste no Método que carregava os Participantes para que o erro não seja mais apresentado  e o Processo seja executado com sucesso. |
