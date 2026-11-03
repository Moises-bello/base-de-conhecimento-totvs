---
article_id: 24228316042007
category: eSocial
content_hash: 90d16001ae33e2cc3545608201d58e52eff389a490e8c1c2628d5cd9bd95842f
fetched_at: '2026-06-28T22:47:15.327761+00:00'
product: rm
section_id: 11645725240471
source: central-rm
title: 'RH - RM - RHU - S-2501: Guia DCTFWEB gerada com valores zerados'
type: support-article
updated_at: '2024-06-19T17:48:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24228316042007-RH-RM-RHU-S-2501-Guia-DCTFWEB-gerada-com-valores-zerados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24228355969303) Tempo aproximado para leitura: **00:00:58 min** **Dúvida**Ao gerar a guia DCTFWEB os valores são trazidos zerados. O que fazer?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - 12.1.34.263, 12.1.2205.211, 12.1.2209.155 e superiores.  
  
**Solução**Geralmente, quando a guia DCTFWEB é gerada com valores zerados e estes já foram informados no cadastro dos períodos do evento S-2501 - Informações dos Tributos Decorrentes de Processo Trabalhista, decorre do campo 'Código de Receita' não ter sido preenchido.  
  
O campo 'Código de Receita' não se trata de um campo obrigatório, mas é indispensável quando há pagamentos a serem realizados, pois é através deste que você irá informar qual receita é proveniente o débito a ser calculado.  
  
O campo poderá ser identificado no **cadastro do evento S-2501** | **Guia Identificação do período e da base de cálculo dos tributos** | **Incluir contribuição social** | **Código de receita** e deverá ser preenchido com o código de receita de acordo com a **[Tabela 29 - Códigos de Receita - Reclamatória Trabalhista](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-nt-02-2024/tabelas.html#29)**[:](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-nt-02-2024/tabelas.html#29) **![](https://centraldeatendimento.totvs.com/hc/article_attachments/24229913984919)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24229942156055)  
  
Saiba Mais**Para maiores informações referentes ao preenchimento dos campos do evento S-2501, acesse:  
[RH - RM - RHU - eSocial: S-2501 - Mapeamento dos campos para geração do evento S-2501](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18863423016855)
