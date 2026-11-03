---
article_id: 360025500071
category: Gestão de Transportes (TMS)
content_hash: 97e65214625b08c31b06ccc04e0bcb941369a23f7705dec80e1c3c9af709ae4e
fetched_at: '2026-06-28T22:45:29.257286+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Gerar Contrato de Carreteiro com Adiantamento
type: support-article
updated_at: '2021-11-05T13:43:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025500071-Log%C3%ADstica-Linha-Protheus-TMS-Gerar-Contrato-de-Carreteiro-com-Adiantamento
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:02:25 min****Dúvida**Como gerar **contrato de carreteiro** com **adiantamento**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**No contrato de carreteiro, para que o adiantamento possa ser descontado do valor do frete que será pago, é necessário que a despesa utilizada esteja parametrizada para movimentar banco.  
  
Quando a despesa utilizada não movimenta banco, o Sistema gera um título do tipo **NDF - Non Deliverable Forward** que pode ser abatido por meio de **Compensação Financeira**. Quando a despesa movimenta banco, o valor apontado como adiantamento é apresentado no complemento da viagem.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024221951/mceclip0.png)

Para verificar se o tipo da **despesa**utilizada **movimenta banco**, ao incluir ou alterar uma viagem, vá em **Complemento de Viagem - TMSA240,** em seguida acesse **Outras Ações/Adiantamento/Desp.**Ao abrir a tela de **Adiantamentos e Despesas**, clique na coluna **Cod. Despesa**e acione **F3:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024107092/mceclip0.png)

Quando a viagem é gerada, o Sistema gera um título do tipo **PA - Pagamento antecipado**no financeiro. O número do **PA** gerado é igual ao número da viagem**.****Para gerar uma viagem com adiantamento:**

* Em **Gestão de Transportes - SIGATMS,** acesse **Atualizações/Viagens/Rodoviário Entrega/Viagem-mod.2 - TMSA144**;
* Incluir a viagem informando **Rota**, documentos e complemento de viagem;
* Dentro do complemento da viagem, selecione **Ações Relacionadas,** **Adiantam/ Desp**. e informe a despesa referente ao adiantamento e seu valor;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024107272/mceclip1.png)

O exemplo citado acima se refere a uma **viagem de entrega**, mas pode ser utilizado também em **viagens de coleta e transporte**.

* Confira os dados e **Confirme**.

**Para gerar contrato de carreteiro por viagem:**

* Em **SIGATMS,** acesse **Atualizações/Terceiros/Contrato Carreteiro - TMSA250**
* Em **Contrato de Carreteiro**, clique em **Por Viagem**.
* Em**Param** informe a faixa de viagens que vão gerar os contratos. Também é possível definir para qual tipo de frota será gerado o contrato, itens referente a contabilização e para qual veículo será gerado o contrato. Confira os dados e **Confirme**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024342712/mceclip0.png)

Na geração do contrato o valor da despesa que movimenta banco também é apresentado como adiantamento.

* Dentro do contrato é possível apresentar todos os títulos gerados pelo processo, a partir da geração do **PA** no início da viagem.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024359511/mceclip1.png)

* O número do título gerado pelo contrato é igual ao número do contrato.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024359551/mceclip2.png)**

* Para consultar título gerado, acessar o módulo **Financeiro****/****Atualizações/Contas a Pagar/Contas a Pagar - FINA050:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024343032/mceclip3.png)**

****![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024343072/mceclip4.png)****
