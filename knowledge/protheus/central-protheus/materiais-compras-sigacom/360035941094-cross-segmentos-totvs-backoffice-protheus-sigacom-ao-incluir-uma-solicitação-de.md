---
article_id: 360035941094
category: Materiais - Compras (SIGACOM)
content_hash: cf3f64c45d7026c2452dbabf7c2ca7dcce0cd94485a3a7be2ecc63ea09f34dad
fetched_at: '2026-06-28T22:41:12.898923+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM  - Ao incluir uma Solicitação
  de Compras, ocorre o Help: FWNOWIDTH para o campo C8_FORMAIL'
type: support-article
updated_at: '2022-05-16T21:12:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035941094-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ao-incluir-uma-Solicita%C3%A7%C3%A3o-de-Compras-ocorre-o-Help-FWNOWIDTH-para-o-campo-C8-FORMAIL
---

**Dúvida**

Ao incluir uma Solicitação de Compras, ocorre o Help: **FWNOWIDTH** para o campo **C8\_FORMAIL**

**Ambiente**Protheus – Compras – A partir da versão 12  
  
**Causa**  
Esse incidente pode ocorrer, se o tamanho dos campos do sistema ou base de dados estiverem diferentes.

Valor atribuído difere do tamanho (E-mail).  Este E-mail trata-se do campo **SC8-> C8\_FORMAIL** comparado com **o campo SA2->A2\_EMAIL**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047835873/mceclip0.png)

**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesso o Configurador do Protheus;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046965874/mceclip1.png)

2. No menu do configurador acesse **Base de dados -> Dicionário de dados -> Base de Dados**;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047836513/mceclip2.png)

3. Clique sobre a opção **Dicionário de Dados** e em seguida na lupa, busque pela tabela **SC8**. Ao localizar, clique sobre o botão editar

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046966774/mceclip3.png)

Selecione a tabela SC8, clique no botão ![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047861493/mceclip12.png)

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047861393/mceclip11.png)

Pesquise pelo campo C8\_FORMAIL e clique no edit ![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046989694/mceclip14.png)

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046989554/mceclip13.png)

Altere o campo **C8\_FORMAIL,** condizente com o tamanho do **campo A2\_EMAIL**

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047861133/mceclip10.png)

O tamanho do campo abaixo, é apenas um exemplo, lembre-se que deve ser igual ao tamanho do campo **A2\_EMAIL**.

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047860173/mceclip8.png)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
