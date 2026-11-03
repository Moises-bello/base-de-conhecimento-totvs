---
article_id: 4416784463511
category: Originação de Grãos (OG)
content_hash: 832e8e50873239f5673583df4c082e0dbd71e2cbcfe261ac7afccd1de09b165e
fetched_at: '2026-06-28T22:45:43.227549+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Precificação, aditação contrato nova comercialização
type: support-article
updated_at: '2025-06-24T20:21:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416784463511-Agro-Linha-Protheus-AGR-Precifica%C3%A7%C3%A3o-adita%C3%A7%C3%A3o-contrato-nova-comercializa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20584346695063) Tempo aproximado para leitura: **00:01:20 min** **Dúvida**Como precificar uma aditação na nova comercialização no **SIGAAGR**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Ao incluir uma adição ao contrato usando a nova comercialização, ao confirmar a aditação é necessário definir qual entrega tabela **Cadências do Contrato - NNY** será inserido a quantidade da aditação.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416789469335)

Na confirmação da aditaçãoé atualizado a quantidade da entrega **NNY**, do **Contrato - NJR** e adicionado um novo registro linha nas **Regras Fiscais - N9A** para a aditação.  
O contrato passará para **status previsto**, sendo necessário informar alguns campo obrigatórios nas regras fiscais, como Movimento de **Entrada e Saída - TES**, finalidade e natureza. Após informado os dados poderá confirmar novamente o contrato.

![ADIT1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7888102744343)

A quantidade adicionada ao contrato precisa receber um preço, para tal, acessar a rotina **Painel de Fixação - OGC004** e realizar a fixação de preço para este item do contrato.

![ADIT2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7888104946839)

No painel de fixação, para o contrato terá um registro com o status de fixação parcial, **clicar em fixar contrato e gerar a fixação**, será gerado um novo negocio para o contrato para a quantidade que foi fixada, em seguida **aprovar este novo negocio para confirmar a fixação de preço**, esta aprovação pode ser feita no painel de fixação no botão outras ações.

![ADIT3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7888107868951)

Após realizado a fixação e aprovado a negociação desta fixação, será possível gerar a expedição **romaneio** para a aditação realizada no contrato.
