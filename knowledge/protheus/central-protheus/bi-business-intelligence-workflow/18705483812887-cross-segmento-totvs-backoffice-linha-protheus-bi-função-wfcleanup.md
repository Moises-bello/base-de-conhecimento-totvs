---
article_id: 18705483812887
category: BI - Business- Intelligence - Workflow
content_hash: 012706b4db7f46e8f9a0bded1b11504d619b41837f183f19341f354b21e87bbc
fetched_at: '2026-06-28T22:37:03.118486+00:00'
product: protheus
section_id: 1500001550762
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Função WFCLEANUP
type: support-article
updated_at: '2023-10-31T20:12:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18705483812887-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Fun%C3%A7%C3%A3o-WFCLEANUP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18705522571287) Tempo aproximado para leitura: **03:00 min** **Dúvida**Como utilizar a Função "***WFCLEANUP***"?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – BI – *Workflow* - Todas as releases.  
  
**Solução**A manutenção de diretórios do *Workflow* pode ser realizada de forma manual ou automática.  
É possível efetuar a manutenção/limpeza dos *WF* já finalizados nas pastas "***inbox***", "***outbox***" e "***sent***" que ficam dentro da "Protheus Data" do Ambiente Protheus.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18705516426135)  
  
Para manutenção automática, basta agendar dentro do Schedule a execução da Função "***WFCleanUp***":  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18705701653911)  
  
**WFCleanUp (<empresa>, <filial>, <período>)**Exemplo:  
**WFCleanUp ("99","01","30")  
  
Observações:** No campo <**período**> informar o tempo que deseja manter salvo os arquivos antigos.  
  
  
**Saiba mais:**  
[**Manutenção de Diretórios do WF (WFCLEANUP)**](https://tdn.totvs.com.br/pages/releaseview.action?pageId=225951042)  
**[FAQs Workflow](https://tdn.totvs.com/display/PROT/FAQs+-+Workflow)**
