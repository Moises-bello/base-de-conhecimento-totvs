---
article_id: 360019128831
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 7ea15cb5632c0d6234bb4e5e718d784ea5e2ddbe63cd30d2338819b5f59eabe5
fetched_at: '2026-06-28T22:37:20.099380+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Parâmetro MV_CNPEDVE
  - Como vincular um Contrato do Gestão de Contratos a um Pedido de Venda no Faturamento
  ?
type: support-article
updated_at: '2024-06-07T20:05:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019128831-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Par%C3%A2metro-MV-CNPEDVE-Como-vincular-um-Contrato-do-Gest%C3%A3o-de-Contratos-a-um-Pedido-de-Venda-no-Faturamento
---

**Dúvida**

Parâmetro MV\_CNPEDVE - Como vincular um Contrato do Gestão de Contratos a um Pedido de Venda no Faturamento ?

**Ambiente**

Protheus - SIGAGCT - A partir da release 12.1.017

**Solução**

Com o objetivo de tornar mais simples, flexível e ágil o processo de inclusão de pedido de venda á partir  
de um contrato gerado no “Gestão de Contratos (SIGAGCT)”, existe o parâmetro “**MV\_CNPEDVE**” para a rotina “Pedido de Venda (MATA410)”.

Com isso, quando o parâmetro estiver ativado (conteúdo igual a .T.) é possível incluir um pedido vinculando a um contrato e realizando todo o processo de medição de forma automática (via MsExecAuto) á partir dos dados contidos no pedido de venda.

**MV\_CNPEDVE** → Indica se permite a geração de pedidos de venda vinculados a contratos, gerando assim a medição automaticamente, a partir do pedido de venda.

**Procedimentos para utilização:**

O sistema deve ter já cadastrado, um Contrato de Venda, sem Controle de Alçadas e que esteja vigente pelo módulo **Gestão de Contratos (SIGAGCT)**.

1. Acesse Faturamento (SIGAFAT) e selecione as opções **Atualizações/ Pedidos/ Pedidos de Venda;**

2. Clique na opção **Incluir;**

3. Posicione o cursor no campo **Cliente** e tecle F9;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20462287596183)

4. Inclua **Vínculo a Contrato** – SIGAGCT;

5. Selecione o contrato, competência, a planilha e confirme;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20462293186967)

6. Ao confirmar a inclusão do Pedido de Vendas gera-se a Medição para o Contrato vinculado com status encerrado.

***Obs:***

Pelo padrão do funcioanamento desta opção F9 do parâmetro **MV\_CNPEDVE**, ela não permite a realização de medição ou escolha de Contratos de Vendas do tipo de Serviço, Semi-Fixo ou Recorrentes.

Caso seja escolhido um contrato de um destes tipos será retornada a mensagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24036632140055)

E para estes tipos de contratos a possibilidade de realização da medição é apenas através da rotina de Medição CNTA121 no módulo Gestão de Contratos.

***Saiba Mais:***

[GCT0007\_Parâmetro\_MV\_CNPEDVE](https://tdn.totvs.com/x/QgG8DQ)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
