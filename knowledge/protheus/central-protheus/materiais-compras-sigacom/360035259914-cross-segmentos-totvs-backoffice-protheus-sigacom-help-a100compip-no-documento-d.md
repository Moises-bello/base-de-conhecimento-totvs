---
article_id: 360035259914
category: Materiais - Compras (SIGACOM)
content_hash: 9a21e8b764680c1ee2a47fd7ab63d6815489b724561fa276a166240ee30bd562
fetched_at: '2026-06-28T22:41:18.804469+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - HELP A100COMPIP no
  Documento de Entrada
type: support-article
updated_at: '2022-05-18T20:55:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035259914-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-HELP-A100COMPIP-no-Documento-de-Entrada
---

**Dúvida**

HELP A100COMPIP

**Ambiente**

Protheus – Compras – A partir da versão 12  
  
**Solução**

Ao classificar a pré-nota, é exibida a mensagem HELP A100COMPIP

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046693973/mceclip0.png)

A mensagem é exibida devido o conteúdo do campo Tipo da Nota  estar preenchido como **Complemento.**

*Atualizações -> Movimentos -> Documento de Entrada ( **Mata103** )*

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045834114/mceclip1.png)

Nesta situação, como trata-se de um complemento é necessário atrelar a uma Nota fiscal de origem, que pode ser feita de três maneiras:

**1a. Opção**

Na linha dos itens, informe manualmente os campos:

- Docto. Orig: Nota fiscal original ( **D1\_NFORI** )

- Série Orig: Série da Nota fiscal ( **D1\_SERIORI** )

- It. Doc. Orig: Ítem da Nota fiscal ( **D1\_ITEMORI** )

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046696733/mceclip2.png)

**2a. Opção**

Posicionar na linha dos ítens e pressionar a tecla F7, será apresentada uma tela, Notas fiscais  de origem complemento, possibilitando selecionar a respectiva Nota fiscal.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046697233/mceclip3.png)

**3a. Opção**

Ao clicar em Outras ações, selecionar Origem, será apresentada a ela Notas fiscais  de origem Complemento ( igual da 2a. opção).

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045838074/mceclip8.png)

Após vincular o documento de origem, o sistema permitirá a classificação sem emitir o aviso de alerta.
