---
article_id: 4402654192663
category: Financeiro - Consultas / Relatórios
content_hash: ab9c2638ce5148655f7e70599ec990b6518242ffa8fc3feef805649008f0e4ff
fetched_at: '2026-06-28T22:37:58.469498+00:00'
product: protheus
section_id: 1500001539561
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINC022 - Porque quando
  MV_BXCNAB=S, o sistema não considera na consulta o totalizador o movimento E5_TIPODOC=VL
type: support-article
updated_at: '2023-01-25T23:41:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402654192663-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINC022-Porque-quando-MV-BXCNAB-S-o-sistema-n%C3%A3o-considera-na-consulta-o-totalizador-o-movimento-E5-TIPODOC-VL
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Porque quando **MV\_BXCNAB = S**, o sistema não considera na consulta do Fluxo por natureza os movimentos **tipo BA**, ao invés de considerar o movimento **totalizador BL ou VL** que são os movimentos que atualizam o saldo bancário e constam no extrato bancário?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -Financeiro - Todas as versões  
  
**Solução**A rotina FINC022 é uma rotina que chama Fluxo por Natureza, tem que ser título a título para mostrar Natureza por Natureza (por isso considera o tipo **BA** e não **VL**), pois **pode haver várias naturezas no totalizador.**  
  
E outro detalhe o **FINC021** esta sim é a rotina de fluxo de caixa.  
Na documentação oficial é bem clara  
[FINC022 Fluxo Por Natureza](https://tdn.totvs.com/display/public/PROT/FINC022+Fluxo+Por+Natureza)  
![](https://totvssuporte.zendesk.com/attachments/token/TQ59mThMqOKuZ7K5rOksOJB8n/?name=inline1084387963.png)
