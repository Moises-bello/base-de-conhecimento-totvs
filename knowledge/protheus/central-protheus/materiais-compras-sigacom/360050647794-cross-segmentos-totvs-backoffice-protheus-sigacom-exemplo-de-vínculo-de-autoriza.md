---
article_id: 360050647794
category: Materiais - Compras (SIGACOM)
content_hash: 67fe6b4cf3363962eae637f671598a7a494be0b93fd5107d98f036838e474549
fetched_at: '2026-06-28T22:41:18.592023+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Exemplo de vínculo
  de Autorização de Entrega no Documento de Entrada
type: support-article
updated_at: '2022-05-18T20:52:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050647794-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Exemplo-de-v%C3%ADnculo-de-Autoriza%C3%A7%C3%A3o-de-Entrega-no-Documento-de-Entrada
---

**Dúvida**

Exemplo de vínculo de Autorização de Entrega no Documento de Entrada.

**Ambiente**

Protheus – Compras – A partir da versão 12  
  
**Solução**

Exemplo do processo de inclusão do Contrato até o vinculo com Documento de Entrada

- Incluir um Produto, acesse Atualização > Cadastros > **Produtos (MATA010) -** Tabela **SB1**

O produto deve ter contrato parceria habilitado, ou seja, **SIM** ou **AMBOS:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079057493/mceclip0.png)**

 - Incluir um Contrato Parceria, acesse Atualização > Contratos >**Contrato Parceria (MATA125) -** Tabela **SC3**com os dados acordados com o fornecedor:

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079057933/mceclip1.png)**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077917414/mceclip2.png)**

- Incluir um Autorização de Entrega, acesse Atualização > Contratos > Autorização de Entrega (MATA122) - Tabela SC7

Nesse momento é vinculado o Contrato de Parceria com a Autorização de Entrega. O vínculo pode ser realizado por Contrato ou Item do Contrato.

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079058233/mceclip3.png)**

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079058653/mceclip4.png)**

Após vincular o sistema gatilha as informações com base no Contrato Parceria e o campo de Solicitação é preenchido com o código do Contrato:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077918014/mceclip5.png)

Nesse momento o sistema permite alterar a quantidade caso seja necessário.

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077918334/mceclip7.png)

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079061013/mceclip9.png)

Se utilizada uma quantidade menor na consulta do Contrato Parceria deve constar com a legenda de parcialmente atendido conforme imagem:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079060873/mceclip8.png)

- Incluir Documento de Entrada acesse Atualização > Movimentos > Documento de Entrada (MATA103) - Tabela SD1 e SF1

**![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077921014/mceclip10.png)**

**![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079061333/mceclip11.png)**

O código no campo Pedido de Compras refere-se a Autorização de Entrega

**![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077921154/mceclip12.png)**

No Documento de Entrada também é permitido ajustar a quantidade. Se utilizada uma quantidade menor na consulta do Contrato Parceria e Autorização de Entrega deve constar com a legenda de parcialmente atendido conforme imagem:

**![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077921314/mceclip13.png)**

**![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077921454/mceclip14.png)**

**![mceclip15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079061713/mceclip15.png)**

Dessa forma a Autorização de Entrega continua apresentando no Documento de Entrada até que seja utilizado o saldo total.

**![mceclip16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079062293/mceclip16.png)**

Quanto utilizado o saldo total do Contrato é alterada a legenda para Contrato Atendido

![mceclip17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077922354/mceclip17.png)
