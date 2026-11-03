---
article_id: 4406998772759
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 2ab1493a6d5d8b2f9158ada4f5d92151afefb824943834311d33b9456097a287
fetched_at: '2026-06-28T22:42:43.490554+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAPCP - InterFunctionCall: cannot find function
  MNTINTSASC in AppMap on A380TUDOOK(MATA380.PRX)'
type: support-article
updated_at: '2021-08-24T13:42:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406998772759-Manufatura-Linha-Protheus-SIGAPCP-InterFunctionCall-cannot-find-function-MNTINTSASC-in-AppMap-on-A380TUDOOK-MATA380-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:40 min****Ocorrência**No módulo **SIGAPCP - Planejamento e Controle da Produção**, ao tentar alterar um empenho na rotina **MATA380 - Empenho simples**, é apresentada a ocorrência **InterFunctionCall: cannot find function MNTINTSASC in AppMap on A380TUDOOK(MATA380.PRX)**  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**Esse incidente ocorre, pois o parâmetro **MV\_NGMNTCM - Integração Manutenção (MNT) com Compras (COM) Informar S=Sim ou N=Não** está igual a **S - Sim**, mas o módulo **SIGAMNT - Manutenção de Ativos** não está instalado no ambiente.   
  
**Solução**Para solucionar essa ocorrência, altere o parâmetro **MV\_NGMNTCM** para **N - Não**.
