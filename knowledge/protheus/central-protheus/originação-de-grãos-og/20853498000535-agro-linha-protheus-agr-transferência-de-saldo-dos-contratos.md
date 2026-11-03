---
article_id: 20853498000535
category: Originação de Grãos (OG)
content_hash: 8bc6034197fef5f5f493f601911abc17a79fcfd2ca6c7fe88be9d96274013603
fetched_at: '2026-06-28T22:45:45.184467+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Transferência de saldo dos contratos
type: support-article
updated_at: '2025-06-18T11:07:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20853498000535-Agro-Linha-Protheus-AGR-Transfer%C3%AAncia-de-saldo-dos-contratos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20853497899159) Tempo aproximado para leitura: **00:02:15 min**

**Ocorrência**  
No módulo **Comercialização (Linha Protheus) - Originação de Grãos (OG)**, ao realizar o processo para cadastrar um novo contrato com o novo destinatário é apresentada a ocorrência **Apontamento Transferência de saldo dos contratos**.  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**  
Esse incidente ocorre, pois é preciso realizar o processo para cadastrar um novo contrato com o novo destinatáriono Sistema.  
  
**Solução**  
Para solucionar essa ocorrência, o ideal a ser feito nessa situação é a **supressão** do saldo restante e a **finalização** do que já foi movimentado para colocar o saldo no novo contrato. Mas sem efetuar o **cancelamento do contrato**, pois ele possui **Nota Fiscal** vinculada por causa das movimentações já efetuadas e isso poderia causar complicações.  
Para efetuar esse processo realize os seguintes passos:

**1.** Acesse o contrato e visualize o que resta de saldo, no campo **Qtd.Sld.Fco**;

![SAL.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/20853455884311)

**2.** Verifique na tela inicial do contrato acesse a opção **Outras Ações > Mais Ações > Adic./Supres.**;

![Screenshot_5.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/20853497910423)![SAL2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/20853455892887)

**3.** Clique em **Incluir** para efetuar a Supressão. Na opção **Tipo** informe **Supressão**. No campo **Qtd. Alt.** insira o saldo restante do contrato. No campo **Código** informe o **Motivo da Alteração**, que já deve ser previamente cadastrado por meio da rotina **OGA140 -****Alteração de Contrato**. Confirme novamente por meio de **Outras Ações > Confirmar**;

![Screenshot_3.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/20853455898135)

![Screenshot_7.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/20853455902871)

**4.** Feche a tela de Alteração de Contrato e com o contrato selecionado verifique se a **Qtd.Sld.Fco** está zerada. Em seguida acesse **Outras Ações > Status**. Finalize o **Sts.Ass.**, **Sts.Fis.**, **Sts.Fin.** e o **Sts.Est.** Para finalizar o **Status de Assinatura** basta clicar no botão **Assinatura** e aceitar a finalização. Para os demais a Finalização é feita por meio das **Outras Ações**;

![Screenshot_8.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/20853455906455)

**5.** Após efetuado esse processo Finalize o contrato por meio de **Outras Ações > Finalizar**;

![Screenshot_9.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/20853455910935)

**6.** Verifique em seguida inclua um novo contrato, adicione nele o saldo suprimido anteriormente e siga o processo.
