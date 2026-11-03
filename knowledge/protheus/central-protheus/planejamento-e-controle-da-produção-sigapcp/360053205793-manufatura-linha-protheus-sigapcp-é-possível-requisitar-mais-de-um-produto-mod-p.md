---
article_id: 360053205793
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 9a73dd33d85d881c7b3fc5b9b6541c9fd66dfd55e25bb8223dea5e9b72b9f0c7
fetched_at: '2026-06-28T22:42:42.227799+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - É possível requisitar mais de um produto
  MOD pelo centro de custo
type: support-article
updated_at: '2021-06-01T14:58:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053205793-Manufatura-Linha-Protheus-SIGAPCP-%C3%89-poss%C3%ADvel-requisitar-mais-de-um-produto-MOD-pelo-centro-de-custo
---

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:00:40 min  
  
Dúvida**  
É possível requisitar mais de um produto **MOD - Mão de obra** pelo **centro de custo**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
Não existe parametrização nas rotinas **MATA680 -****Produção** **PCP MOD 1** e**MATA681 - Produção PCP MOD 2** para requisitar mais de um produto **MOD** pelo **centro de custo**. Porém, existe o ponto de entrada **MT680GD3 - Validação do retorno** que permite a implementação desta validação.  
  
**Saiba mais**  
Para consultar a documentação deste ponto de entrada consulte o *link*[MT680GD3 - Validação do Retorno](https://tdn.totvs.com/pages/releaseview.action?pageId=330837203)
