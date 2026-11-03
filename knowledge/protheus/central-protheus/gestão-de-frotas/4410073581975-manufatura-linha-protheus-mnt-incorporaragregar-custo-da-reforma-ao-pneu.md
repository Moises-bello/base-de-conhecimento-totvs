---
article_id: 4410073581975
category: Gestão de Frotas
content_hash: 4271412930ac1ac99dfbe72b3dbe26715618142074f568d2c268be500327763c
fetched_at: '2026-06-28T22:42:39.445361+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Incorporar/Agregar Custo da Reforma ao
  Pneu
type: support-article
updated_at: '2021-10-06T20:23:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410073581975-Manufatura-Linha-Protheus-MNT-Incorporar-Agregar-Custo-da-Reforma-ao-Pneu
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:02:10 min****Dúvida**Como faço para incorporar ou agregar o custo da reforma ao pneu?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas - Todas as versões  
  
**Solução**O processo de incorporação de custo de reforma chama-se **Beneficiamento** e pode acontecer durante a reforma de um pneu da seguinte forma:

1. Ao realizar a geração da **O.S. - Ordem de Serviço** em lote, automaticamente é gerada para cada pneu uma **O.S.** e consequentemente uma **S.C. - Solicitação de Compra** para aquisição do serviço de reforma. Após isso a **S.C.** passa para o processo de compras, gerar **Cotação** e **Pedido de Compra**
2. Ao realizar o recebimento da **NFE - Nota Fiscal de Entrada**, indiferente da **TES -** **Tipo de Entrada/Saída.** Recomenda-se não movimentar estoque pois se trata de um **Serviço**, o custo deste **Serviço** é atribuído a **O.S.** do pneu, para o **Centro de Custo** do mesmo. A conta contábil é informada na **NFE**, pois o pneu, não possui relacionamento direto com **Conta Contábil**, apenas com o **Centro de Custo**.
3. Ao realizar o recebimento da **O.S.** **em lote**, o Sistema verifica se existe lançamento para a **O.S**., caso sim, a *flag* do campo **Realizado** para a ter a opção **Sim**, indicando que o serviço de reforma foi realizado. Ao confirmar o recebimento o pneu passa para o *status* **Aguardando Reforma**.
4. Na rotina de **Analise Técnica - MNTA600**, dependendo do destino realizado, poderá ocorrer a movimentação de estoque, referente ao produto para controle de pneus. Neste momento estamos nos referindo ao custo do produto pneu reformados e não ao custo do **Serviço**.  
     
   Para que o custo do pneu reformado esteja com o custo do serviço, deve-se realizar o processo do estoque de movimentação. Utilizando uma **TM - Tipo de Movimentação** com o campo **Valorizado** igual a **Sim** e **Quantidade Zero** igual a **Sim**, realizar a movimentação do produto **Pneu Reformado** com o custo do serviço.
5. Após o procedimento acima, ao realizar a **Analise técnica** com o destino **4 - Estoque Reformado**, será apresentado a tela para informar o produto **Pneu Reformado** e ao confirmar a inclusão da **Analise Técnica**, será realizado a movimentação do estoque, agregando saldo ao produto.
