---
article_id: 360048123714
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: aef6536262efb9dbd8eb9acd685520cf93fc4e4d332b270d4f42a3283ec5dbb3
fetched_at: '2026-06-28T22:40:44.690652+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECD : J150 Nivel_AGL
  Não deve existir mais de uma linha de nível igual a 1 na DRE'
type: support-article
updated_at: '2022-06-08T12:52:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048123714-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-J150-Nivel-AGL-N%C3%A3o-deve-existir-mais-de-uma-linha-de-n%C3%ADvel-igual-a-1-na-DRE
---

**Ocorrência**

Nivel\_AGL Não deve existir mais de uma linha de nível igual a 1 na DRE

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070959194/mceclip0.png)  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
**Causa**

* Erro é apresentado devido a configuração o J150 possui mais de uma linha

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072107813/mceclip2.png)

* Veja como através do cadastro da visão (CTBA161) como a visão está configurada

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072107873/mceclip3.png)  
**Solução**

* Para que a situação não seja apresentada necessário revisar a estrutura da visão gerencial , veja que existe nível "total geral"
* Para mais detalhe  [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006972612-MP-SIGACTB-ECD-J150-?source=search)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072107953/mceclip4.png)

* Deve seguir o critérios para cadastro da Visão , para mais detalhe [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028247351-MP-SIGACTB-ECD-COMO-GERAR-O-REGISTRO-J150-?source=search)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072108213/mceclip5.png)

* Veja como o sistema gerou somente um nível 1

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070959934/mceclip6.png)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070961574/mceclip0.png) :

* Verifique se o nível de aglutinação criada na Visão segue "(mesmo conceito do plano de contas – Registro I050)"
* [MP-SIGACTB-ECD I050 : 5 - NIVEL O plano de contas com todas as suas contas sintéticas e analíticas deve conter no mínimo 4 níveis (Resolução CFC 1299/2010).](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028148692-MP-SIGACTB-ECD-I050-5-NIVEL-O-plano-de-contas-com-todas-as-suas-contas-sint%C3%A9ticas-e-anal%C3%ADticas-deve-conter-no-m%C3%ADnimo-4-n%C3%ADveis-Resolu%C3%A7%C3%A3o-CFC-1299-2010-?source=search)
* Veja o que o manual da receita descreve sobre o NIVEL\_AGL do J150(DRE)

![](https://totvssuporte.zendesk.com/attachments/token/1J5VKiIo6b2E8d21ZKT5Sp1WP/?name=inline-735632808.png)

Sabia mais:

[MP - SIGACTB - ECD registro J150 - 7-VL\_CTA e 2-COD\_AGL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028548031-MP-SIGACTB-ECD-registro-J150-7-VL-CTA-e-2-COD-AGL?source=search)

[MP - SIGACTB - ECD registro J005 - VL\_CTA\_INI / IND\_COD\_AGL e IND\_GRP\_BAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028866271-MP-SIGACTB-ECD-registro-J005-VL-CTA-INI-IND-COD-AGL-e-IND-GRP-BAL?source=search)
