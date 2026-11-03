---
article_id: 360006746912
category: Contabilidade Gerencial - Amarrações
content_hash: c1b7e5ed1e62b68899804f281253aaf56fbecf73f195c942ed0e2b86d092ab3c
fetched_at: '2026-06-28T22:41:05.780601+00:00'
product: protheus
section_id: 1500001548302
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA250: Validação
  de Amarrações'
type: support-article
updated_at: '2025-01-22T14:34:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006746912-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA250-Valida%C3%A7%C3%A3o-de-Amarra%C3%A7%C3%B5es
---

**Dúvida:**As amarrações realizadas entre contas contábeis e demais entidades, não é validada no sistema.  
  
**Ambiente:**Microsiga Protheus - Versões 11 e 12

**Requisito**

1- Veja se a entidade está habilitada para Uso através da rotina [CTBA130](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006661492-MP-SIGACTB-CTBA130-Altera%C3%A7%C3%A3o-de-Entidades-Cont%C3%A1beis?source=search)

2 - Através da rotina  de cadastro Plano de contas (CTBA020),  Centro de custo (CTBA030) , Item contábil (CTBA040) e Classe de valor (CTBA060) realize o cadastro das entidades que pretende utilizar.

**Solução:**Quando o parâmetro MV\_CTBAMAR está igual a 1:  
1- Crie um código de amarração através da rotina Amarração (CTBA250[)](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba250_cadastro_amarracao.htm);  
2- No cadastro das entidades contábeis Plano de contas (CTBA020),  Centro de custo (CTBA030), Item contábil (CTBA040) e Classe de valor (CTBA060), informe o código de amarração nos campos "Regra de Nível" das respectivas entidades que deseja efetuar a amarração.  
  
Com o MV\_CTBAMAR igual a 2:  
1- Na rotina Amarração (CTBA250), crie o código de amarração.  
2- Posteriormente, selecione todas as entidades contábeis Plano de contas (CTBA020),  Centro de custo (CTBA030), Item contábil (CTBA040) e Classe de valor (CTBA060) que deseja incluir amarração.

Com o MV\_CTBAMAR igual a 3 (Entid. Adicionais):

* Para utilizar a amarração utilizando também Entidades Adicionais, deve-se utilizar a rotina com o parâmetro**MV\_CTBAMAR 2** ou **3.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18047723875351)  
  
**Observação:**

Quando o parâmetro estiver configurado com 1, é importante que todas as entidades contábeis possuam amarrações, pois caso houver alguma entidade sem vínculo, o lançamento contábil pode ser gravado sem que ocorra validações.  
  
Caso o MV\_CTBAMAR estiver igual a 2, a amarração será validada no lançamento, independente de todas as entidades envolvidas no lançamento possuírem amarrações.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18047728247447)

* [Amarrações - CTBA250](https://tdn.totvs.com/pages/viewpage.action?pageId=617364987)

  + [Alteração X3\_RELAÇÂO do campo CTA\_FILIAL - TQT369](https://tdn.totvs.com/pages/viewpage.action?pageId=185735610)
  + [Amarrações CTBA250 BRA - MV\_CTBAMAR e MV\_PAR02](https://tdn.totvs.com/pages/viewpage.action?pageId=617354926)
  + [Amarrações - Informações Gerais](https://tdn.totvs.com/pages/viewpage.action?pageId=634502100)
  + [Opção Aplicar seleção Cadastro de amarração - THPLK0](https://tdn.totvs.com/pages/viewpage.action?pageId=76251164)
  + [CTB0169\_Regras de amarração de entidades contábeis utilizando MV\_CTBAMAR igual á 2 no Cadastro de Amarração Contábil (CTBA250) .](https://tdn.totvs.com/pages/releaseview.action?pageId=500278830)
