---
article_id: 360035198573
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 815f57d12ad6f1d1eda0c3d27bca542fd56180e7585bfa141846a83d8a01201b
fetched_at: '2026-06-28T22:42:45.843168+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Regra utilizada pelo Sistema para definir
  a ordem dos lotes nos empenhos
type: support-article
updated_at: '2026-06-02T18:31:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035198573-Manufatura-Linha-Protheus-SIGAPCP-Regra-utilizada-pelo-Sistema-para-definir-a-ordem-dos-lotes-nos-empenhos
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40918688697111)***Tempo aproximado para leitura: **00:00:58 min**  
  
**Dúvida**  
Qual é a regra utilizada pelo Sistema para definir a ordem dos lotes nos empenhos na rotina **MATA650 - Ordem de Produção** e também os lotes que serão consumidos no momento do apontamento?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
O Sistema utiliza a regra **FEFO** - ***First Expired, First Out,*** ordenando os lotes por ***Validade + código do lote + código do sublote**,* para sugerir os lotes no empenho e também na requisição dos materiais, quando os empenhos não possuem lote definido no empenho*.*  
  
**Saiba mais**  
Para alterar a ordenação de empenho de lotes pode ser utilizado o **Ponto de Entrada** [MTSLDORD - Alteração da sequência de requisição de lote](https://tdn.totvs.com/pages/releaseview.action?pageId=6087842)
