---
article_id: 8809989489303
category: RH - Contabilização
content_hash: 0fe662ada34ca0abfd975fb65bbc0329ee7c57b7134ef127d2ea2e43d188273b
fetched_at: '2026-06-28T22:43:45.926016+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Contabilização da provisão de baixas de rescisão,
  baixa de férias e baixa de transferência
type: support-article
updated_at: '2026-04-23T18:23:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8809989489303-RH-Linha-Protheus-GPE-Contabiliza%C3%A7%C3%A3o-da-provis%C3%A3o-de-baixas-de-rescis%C3%A3o-baixa-de-f%C3%A9rias-e-baixa-de-transfer%C3%AAncia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33713470108823) Tempo aproximado para leitura: **00:03:00 min****Dúvida**  
Como contabilizar as baixas de rescisão, baixa de férias e baixa de transferência da provisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

1. Apresentamos aqui um relatório de provisão com as 3 baixas de provisão: baixa de rescisão, baixa de férias (quitação) e baixa de transferência.

**Configuração:**  
MV\_TRFAMES: AAAAMM  
MV\_RATPROV: N

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8810679641879)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8810715319831)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8810748839959)

2. Importante ressaltar que sempre a contabilização será espelho do que foi gerado na provisão e a primeira conferência será verificar se no relatório está apresentado corretamente os valores e linhas correspondentes.

Vamos analisar o relatório e a tela de contabilização da baixa de rescisão:

Verbas no acumulados de provisão:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8811157322519)

Relatório de provisão apresentando as baixas:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8810673952279)  
Lançamentos contábeis após processamento da rotina GPEM110:   
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8811202889751)  
  
3. Vamos analisar o relatório e a tela de contabilização da baixa de transferência:

Verbas no acumulados de provisão:  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8811261954199)

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8811265121559)

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8811502431895)

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8814200136343)

4. Vamos analisar o relatório e a tela de contabilização da baixa de férias quando ocorre quitação proporcional dos valores (pagamento de férias):

Verbas no acumulados de provisão:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8814647482903)

Relatório de provisão com as baixas de férias proporcionais:   
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8814606395543)

Lançamentos contábeis após processamento da contabilização:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8814966741783)

**Saiba Mais:**  
[Página Centralizadora da Contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109092-RH-Contabiliza%C3%A7%C3%A3o)
