---
article_id: 17676758386071
category: TAF - REINF
content_hash: 020a7ce0f5bf45f91fa1be7ab25edaaf13140ab5d9efe21c56ff54c04e44ba02
fetched_at: '2026-06-28T22:41:34.899057+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - TAF - REINF- Erro Schema IsenImun'':
  [Facet ''pattern''] The value ''1'' is not accepted by the pattern ''2|3''.'
type: support-article
updated_at: '2023-10-12T16:28:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17676758386071-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Erro-Schema-IsenImun-Facet-pattern-The-value-1-is-not-accepted-by-the-pattern-2-3
---

#### **Produto**

#### TAF - SIGATAF - A partir da 12.1.33 e superior

**Dúvida**

Ao realizar a transmissão de um evento ocorre a seguinte rejeição:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17676570066327)

**Causa**

O erro de schema ocorre por que esta sendo gerada a TAG isenImun=1 no XML do TAF, conforme o layout do REINF essa TAG não pode ser gerada com esse conteúdo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17676637115159)

**Solução** 

Alterar o cadastro do participante deixando o campo **Isento/Imune (C1H\_ISEIMUN)** em branco .

**Informações sobre isenção e imunidade.**

**Valores válidos:**

2 - Instituição de educação e de assistência social sem fins lucrativos, a que se refere o art. 12 da Lei nº 9.532, de 10 de dezembro de 1997;

3 - Instituição de caráter filantrópico, recreativo, cultural, científico e às associações civis, a que se refere o

art. 15 da Lei nº 9.532, de 1997.

Atualizações > Cadastros > Fiscais > participante > localize o participante > aba informações Gerais.  
   
![](https://totvssuporte.zendesk.com/attachments/token/jsUuieFnWcwEXbkN94NswF8Pj/?name=image.png)

Faça um acesso nos títulos nas rotinas PAGAMENTO e FATURA/RECIBO, faça uma alteração qualquer , salva e retorna como estava e salva novamente para validar se o não esta fazendo alteração no XML quando retransmite.

Exclua a apuração e gera novamente após esse procedimento e retransmite .

[Cross Segmentos - Backoffice Protheus - TAF - REINF - Como excluir apuração inconsistente.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8549885209879-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-excluir-apura%C3%A7%C3%A3o-inconsistente-?source=search)
