---
article_id: 20593040180759
category: Originação de Grãos (OG)
content_hash: 1d5bac33642e4af8c0e85af3e127f4bd708f52d669b691099afea4d5e0376aa9
fetched_at: '2026-06-28T22:45:37.006314+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Apontamento para precificação, adição contrato
  da nova comercialização
type: support-article
updated_at: '2025-01-07T14:08:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20593040180759-Agro-Linha-Protheus-AGR-Apontamento-para-precifica%C3%A7%C3%A3o-adi%C3%A7%C3%A3o-contrato-da-nova-comercializa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20593023960599) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**  
No módulo **Comercialização (Linha Protheus) - Originação de Grãos (OG)**, ao realizar o processo para precificar uma adição na nova comercialização é apresentada a ocorrência **Apontamento para precificação, adição contrato da nova comercialização**.  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**  
Esse incidente ocorre, pois será necessário realizar o processo para precificar uma adição na nova comercializaçãono Sistema.  
  
**Solução**  
Para solucionar essa ocorrência, ao incluir uma adição ao contrato usando a nova comercialização, ao confirmar a adição é necessário definir qual entrega tabela **Cadências do Contrato - NNY** será inserido a quantidade da adição.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20593023962263)

Na confirmação da adição é atualizado a quantidade da entrega **NNY**, do **Contrato - NJR** e adicionado um novo registro linha nas **Regras Fiscais - N9A** para a adição.  
O contrato passará para **status previsto**, sendo necessário informar alguns campo obrigatórios nas regras fiscais, como Movimento de **Entrada e Saída - TES**, finalidade e natureza. Após informado os dados poderá confirmar novamente o contrato.

![ADIT1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20593040146967)

A quantidade adicionada ao contrato precisa receber um preço, para tal, acessar a rotina **Painel de Fixação - OGC004** e realizar a fixação de preço para este item do contrato.

![ADIT2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20593023964823)

No painel de fixação, para o contrato terá um registro com o status de fixação parcial, **clicar em fixar contrato e gerar a fixação**, será gerado um novo negocio para o contrato para a quantidade que foi fixada, em seguida **aprovar este novo negocio para confirmar a fixação de preço**, esta aprovação pode ser feita no **painel de fixação** no botão **outras ações**.

![ADIT3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20593040149399)

Após realizado a fixação e aprovado a negociação desta fixação, será possível gerar a expedição **romaneio** para a adição realizada no contrato.
