---
article_id: 360037188314
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 6b1b95bb5e5517ea0c8426fb3f402e68a3e3ea22dece72e849205939fddc395a
fetched_at: '2026-06-28T22:37:19.796772+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como configurar o Gestão
  de Contratos para gerar Títulos Financeiros ou Pedidos no encerramento da medição
  ?
type: support-article
updated_at: '2026-05-14T14:28:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037188314-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-configurar-o-Gest%C3%A3o-de-Contratos-para-gerar-T%C3%ADtulos-Financeiros-ou-Pedidos-no-encerramento-da-medi%C3%A7%C3%A3o
---

**Dúvida**

Como configurar o Gestão de Contratos e as medições para gerar Títulos Financeiros ou Pedidos no encerramento da medição ?

**Ambiente**

Protheus – SIGAGCT – A partir da versão 12.1.17

**Solução**

Consulte os nossos vídeos How-To:

[How To | MP-SIGAGCT - Medição - Gerando um Pedido](https://youtu.be/sPesGrjQTnc)

[How To | MP-SIGAGCT - Medição - Gerando um Título Financeiro](https://youtu.be/1kQBtPUvKiU)

Para a definição se no Encerramento da Medição de um Contrato será gerado um "Pedido" ou um "Titulo Financeiro", existe o campo **CNB\_PEDTIT** *(NOTA FISCAL/TÍTULO)* na tabela dos itens planilhas, onde poderá ser informado **Nota fiscal** , para que seja gerado ***Pedido de Compras/Vendas*** ao encerrar a medição ou ***Títulos*** direto no módulo financeiro.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049817493)

A informação contida no campo **CNB\_PEDTIT** será levada para o campo análogo da medição (**CNE\_PEDTIT)** quando incluída a medição para o contrato, podendo ser alterado no momento da medição se necessário.

No caso do contrato ser do Tipo Flexível, que não possui itens na planilha, a informação poderá ser inserida na inclusão da medição, no campo **CNE\_PEDTIT** *(NOTA FISCAL/TÍTULO)*, com a mesma funcionalidade descrita acima:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048919554)

***Obs1:***

A possibilidade de se realizar as medições gerando apenas contas a pagar ou contas a receber ao se encerrar a medição, sem que elas passem pelo processo de compras, é conforme reportado acima com a configuração do campo do item da medição (**CNE\_PEDTIT)** como "Título".

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Trilha de Videos Gestão de Contratos Básico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10008598705431-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Trilha-de-Videos-Gest%C3%A3o-de-Contratos-B%C3%A1sico?source=search)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
