---
article_id: 360018756531
category: Contabilidade Gerencial - Entidades
content_hash: 51d5c156163ed8f0920bbd0194a858791f43fd17d164316f842990793774f937
fetched_at: '2026-06-28T22:40:49.773628+00:00'
product: protheus
section_id: 1500001537661
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA250: Como o Protheus
  trata as amarrações contábeis? '
type: support-article
updated_at: '2023-06-06T19:30:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018756531-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA250-Como-o-Protheus-trata-as-amarra%C3%A7%C3%B5es-cont%C3%A1beis
---

**Dúvida**Como o protheus trata as amarrações contábeis?

**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
  
**Solução**

# Cadastro de Amarração

No cadastro de Amarração são incluídos os códigos que irão representar os grupos de amarração aos quais uma entidade contábil poderá pertencer.

Os códigos dos grupos de amarração são informados nos cadastros das entidades contábeis para criar um vínculo entre um Código de Regra e um Código de Contra-Regra.

# Regras e Contra-Regras

## Conceitos

* As regras e contra-regras são basicamente grupos utilizados para identificar contas, centros de custos, itens contábeis e classes de valor que devem ser utilizados sempre em conjunto.
* As regras e contra-regras tem a finalidade de restringir a combinação entre as entidades contábeis, ou seja, uma conta contábil somente poderá ser utilizada em conjunto com centros de custos, itens contábeis e classes de valor que atenderem os critérios definidos na amarração.
* Para que as regras de amarração atuem corretamente todas as entidades contábeis devem ter seus campos Regras e Contra-Regras informados, pois as entidades com estes campos em branco não são restringidas no lançamento.

## Critérios de Amarração

Os critérios de amarração das regras e contra-regras para a entidade **Conta Contábil** devem ser definidos de acordo com a estrutura abaixo:

**Regra Nível 01**: Regra para Centro de Custo:

Define o grupo de centros de custo que pode ser utilizado com a conta contábil

**Regra Nível 02**: Regra para Item Contábil:

Define o grupo de itens contábeis que pode ser utilizado com a conta contábil

**Regra Nível 03**: Regra para Classe de Valor:

Define o grupo de classes de valor que pode ser utilizado com a conta contábil

![](http://tdn.totvs.com/download/attachments/334339285/regra_conta.jpg?version=1&modificationDate=1517312268000&api=v2)

Os critérios de amarração das regras e contra-regras para a entidade **Centro de Custo**devem ser definidos de acordo com a estrutura abaixo:

**Contra-Regra Nível 01:** Contra-Regra para Conta Contábil:

Grupo ao qual o cento de custo pertence, para poder ser ou não utilizado com contas contábeis.

**Regra Nível 02:** Regra para Item Contábil:

Define o grupo de itens contábeis que pode ser utilizado com o centro de custo.

**Regra Nível 03:** Regra para Classe de Valor:

Define o grupo de classes de valor que pode ser utilizado com o centro de custo.

![](http://tdn.totvs.com/download/attachments/334339285/regra_cc.jpg?version=1&modificationDate=1517312268000&api=v2)

Os critérios de amarração das regras e contra-regras para a entidade **Item Contábil** devem ser definidos de acordo com a estrutura abaixo:

**Contra-Regra Nível 01**: Contra-Regra para Conta Contábil:

Grupo ao qual o item contábil pertence, para poder ser ou não utilizado com contas contábeis.

**Contra-Regra Nível 02**: Contra-Regra para Centro de Custo:

Grupo ao qual o item contábil pertence, para poder ser ou não utilizado com centros de custo.

**Regra Nível 03:** Regra para Classe de Valor:

Define o grupo de classes de valor que pode ser utilizado com o item contábil.

![](http://tdn.totvs.com/download/attachments/334339285/regra_item.jpg?version=2&modificationDate=1517312267000&api=v2)

Os critérios de amarração das regras e contra-regras para a entidade **Classe de Valor** devem ser definidos de acordo com a estrutura abaixo:

**Contra-Regra Nível 01**: Contra-Regra para Conta Contábil:

Grupo ao qual a classe de valor pertence, para poder ser ou não utilizada com contas contábeis.

**Contra-Regra Nível 02:** Contra-Regra para Centro de Custo:

Grupo ao qual a classe de valor pertence, para poder ser ou não utilizada com centros de custo.

**Contra-Regra Nível 03:** Contra-Regra para Item Contábil:

Grupo ao qual a classe de valor pertence, para poder ser ou não utilizada com itens contábeis.

![](http://tdn.totvs.com/download/attachments/334339285/regra_clvl.jpg?version=1&modificationDate=1517312268000&api=v2)

## Exemplo de Utilização

De acordo com os critérios das regras e contra-regras podemos utilizar qualquer combinação das entidades abaixo em um lançamento contábil, considerando as mesmas uma regra geral:

#### Conta Contábil: 111001

Regra para Centro de Custo: CC001

Regra para Item Contábil: IT001

Regra para Classe Valor: CV001

#### Centro de Custo: ADM001

Contra-Regra para Conta Contábil: CC001

Regra para Item Contábil:  IT001

Regra para Classe Valor: CV001

#### Item Contábil: EQP001

Contra-Regra para Conta Contábil: IT001

Contra-Regra para Centro de Custo: IT001

Regra para Classe Valor: CV001

#### Classe de Valor: CPU001

Contra-Regra para Conta Contábil: CV001

Contra-Regra para Centro de Custo: CV001

Contra-Regra para Item Contábil: CV001

Para definir uma exceção à regra geral pode-se utilizar a seguinte regra específica:

#### Conta Contábil: 111002

Regra para Centro de Custo: CC002

Regra para Item Contábil: IT001

Regra para Classe Valor: CV001

#### Centro de Custo: ADM002

Contra-Regra para Conta Contábil: CC002

Regra para Item Contábil:  IT001

Regra para Classe Valor: CV001

Saiba mais :

[Amarração Regras e Contra - Regras](https://tdn.totvs.com/pages/releaseview.action?pageId=334339285)

Amarração com MV\_CTABAMAR = 2

|  |  |
| --- | --- |
| **MV\_CTBAMAR** | Ativa controle de Amarração nos lançamentos contábeis. Definição 0=Não tem amarração,   1=Regra de níveis, 2=Regra de Amarração tabela CTA. |

[CTB0169\_Regras de amarração de entidades contábeis utilizando MV\_CTBAMAR igual á 2 no Cadastro de Amarração Contábil (CTBA250)](https://tdn.totvs.com/pages/releaseview.action?pageId=500278830)

[AMARRAÇÃO INFORMAÇÕES GERAIS](https://tdn.totvs.com/pages/releaseview.action?pageId=634502100)

[Amarrações CTBA250 BRA - MV\_CTBAMAR e MV\_PAR02](https://tdn.totvs.com/pages/viewpage.action?pageId=617354926)

[Cross Segmento - Backoffice Linha Protheus - SIGACTB CTBA250 AMARRAÇÃO ENTIDADE ADICIONAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412245088023-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA250-AMARRA%C3%87%C3%83O-ENTIDADE-ADICIONAL?source=search)

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA250: Validação de Amarrações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006746912-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA250-Valida%C3%A7%C3%A3o-de-Amarra%C3%A7%C3%B5es?source=search)
