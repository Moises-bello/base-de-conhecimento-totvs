---
content_hash: e60db23c8ee3f3b6e11f636de8ec23d9f8a445c80d2f25ab1fa16000aaeda808
fetched_at: '2026-06-29T00:09:39.869154+00:00'
page_id: '431674854'
product: rm
source: tdn-rm
title: 4144910 FISCAL01-7007 DT - Codificação - Erro na geração do R2050 - Valor suspenso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=431674854
version: 2
---

# Cadastro de Lançamento Fiscal

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Layout TAF |
| **Situação/Requisito:** | Na integração RM x TAF o registro T015AK os valores para os tributos decorrentes de processo judicial não estão sendo gerados corretamente. |
| **Solução/Implementação:** | Foi Realizado Acerto no Layout para que os valores sejam gerados corretamente.  13=Previdencia (Funrural) - Será gerado com a informação do Campo ***Retenção Suspensa /Dep Jud*** da pasta Memória de Cálculo.  24 = GILRAT - Será gerado com a informação do campo ***Valor não retido GILRAT*** da aba GILRAT/SENAR  25 = SENAR -  Será geado com a informação do campo V***alor não retido SENAR** da aba GILRAT/SENAR*  Exemplo do registro Gerado gerado:  |T015AK|1|10298340420188260001|3812|1**|1,50|13|** |T015AK|1|10298340420188260001|3812|1|**1,20|24|** |T015AK|1|10298340420188260001|3812|1|**0,30|25|** |
| **Requisito:** | FIS000062 |
