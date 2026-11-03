---
article_id: 360057781774
category: RH - Dissídio
content_hash: 0bc7feb5930acf25d6bbaf6d18cba6975ea8dfd716482cf6ebda3372c7e08e72
fetched_at: '2026-06-28T22:43:44.324349+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Verba de redução salarial - id 1397 no cálculo
  de dissídio retroativo
type: support-article
updated_at: '2025-08-20T14:33:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057781774-RH-Linha-Protheus-GPE-Verba-de-redu%C3%A7%C3%A3o-salarial-id-1397-no-c%C3%A1lculo-de-diss%C3%ADdio-retroativo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34317300907415) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Sistema não gera a verba de redução salarial ou não calcula a diferença da mesma dentro do cálculo de dissídio retroativo.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da Versão 12.1.17.  
  
**Solução**Necessário verificar se a redução de salarial foi feita corretamente, pois quando a verba não é demonstrada no cálculo quer dizer que o sistema não reconhece que o funcionário teve esse período de redução.

1. Verifique a configuração da tabela S061 - Manutenção de tabela:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097964174)

2. Verifique o histórico de contrato do funcionário, onde a data de início e fim da vigência, assim como o código do PPE deverá corresponder ao conteúdo da tabela S061:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097964254)  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097964294)  
  
3. Cálculo de dissídio retroativo:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097964654)

O cálculo da diferença da verba de redução vai depender de sua configuração - aba dissídio retroativo:  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100232293)

4.Verifique se o mnemônico **P\_LPPEATIV** esta ativo.

Se o mnemônico estiver desabilitado o calculo do dissidio não será feito. 

Saiba Mais:  
[Página Centralizadora do Dissídio (GPEM690)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
