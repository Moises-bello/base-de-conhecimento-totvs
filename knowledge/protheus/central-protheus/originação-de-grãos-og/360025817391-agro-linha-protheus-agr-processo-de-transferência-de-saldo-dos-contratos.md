---
article_id: 360025817391
category: Originação de Grãos (OG)
content_hash: c6650c9609b9d1b89db899bf8584b75295f77c35b82a30c9494d513e07e46eec
fetched_at: '2026-06-28T22:45:44.706354+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Processo de Transferência de saldo dos contratos
type: support-article
updated_at: '2025-06-25T11:17:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025817391-Agro-Linha-Protheus-AGR-Processo-de-Transfer%C3%AAncia-de-saldo-dos-contratos
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20803689814423)***Tempo aproximado para leitura: **00:01:30 min****Dúvida**Na rotina**OGA290 - Contrato de Venda** há um contrato em que a metade do saldo foi faturada, porém será necessário alterar o destinatário do contrato para que seja efetuado o faturamento do saldo restante. Como devemos proceder para cadastrar um novo contrato com o novo destinatário, efetuando a transferência do saldo restante do contrato?  
  
 **Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**O ideal a ser feito nessa situação é a **supressão** do saldo restante e a **finalização** do que já foi movimentado para colocar o saldo no novo contrato. Mas sem efetuar o **cancelamento do contrato**, pois ele possui **Nota Fiscal** vinculada por causa das movimentações já efetuadas e isso poderia causar complicações.  
Para efetuar esse processo siga os seguintes passos:

* Acesse o contrato e visualize o que resta de saldo, no campo **Qtd.Sld.Fco**;

![SAL.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/7951808437143)

* Na tela inicial do contrato acesse a opção **Outras Ações > Mais Ações > Adic./Supres.**;

![Screenshot_5.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360024658691)![SAL2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/7951811671447)

* Clique em **Incluir** para efetuar a Supressão. Na opção **Tipo** informe **Supressão**. No campo **Qtd. Alt.** insira o saldo restante do contrato. No campo **Código** informe o **Motivo da Alteração**, que já deve ser previamente cadastrado por meio da rotina **OGA140 -****Alteração de Contrato**. Confirme. Confirme novamente por meio de Outras Ações **>** Confirmar;

![Screenshot_3.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360024660431)

![Screenshot_7.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360024660651)

* Feche a tela de Alteração de Contrato e com o contrato selecionado verifique se a **Qtd.Sld.Fco** está zerada. Em seguida acesse **Outras Ações > Status**. Finalize o **Sts.Ass.**, **Sts.Fis.**, **Sts.Fin.** e o **Sts.Est.** Para finalizar o **Status de Assinatura** basta clicar no botão Assinatura e aceitar a finalização. Para os demais a Finalização é feita por meio das Outras Ações;

![Screenshot_8.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360024663572)

* Após efetuado esse processo Finalize o contrato por meio de **Outras Ações > Finalizar**;

![Screenshot_9.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360024676391)

* Em seguida inclua um novo contrato, adicione nele o saldo suprimido anteriormente e siga o processo.
