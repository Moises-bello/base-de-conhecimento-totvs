---
content_hash: 62425827bb3bf49680b08db141ffe0b4a74c6c38442d49f496db5955aea8acdb
fetched_at: '2026-06-29T00:08:45.693484+00:00'
page_id: '312155559'
product: rm
source: tdn-rm
title: 1594862 FINANCEIRO01-3703 DT Geração de acordo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=312155559
version: 92
---

# GERAÇÃO DE ACORDO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Gerar acordo |
| **Situação/Requisito:** | Não foi possível gerar acordo para os lançamentos oriundos do Módulo Educacional Referência de objeto não definida para uma instância de um objeto. RM.Fin.Lan.Service em RM.Fin.Lan.Acordo.Base.FinLanEducacionalAcordoSbc`1.DoSaveSubscriber() em RM.Lib.Subscriber.RMSSubscriberController`2.DoSaveSubscriber(List`1 list) em RM.Fin.Lan.Acordo.FinLanAcordoMod.AcordoDotNet(List`1 listAcordo) em RM.Fin.Lan.Acordo.FinAcordoGeracaoProcData.DoExecute(RMSParamsProc Params) |
| **Solução/Implementação:** | Ajuste no processo de inclusão de boleto para exibir a mensagem de convenio não informado para a conta caixa do lançamento. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000040 |

divs
