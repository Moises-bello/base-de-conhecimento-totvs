---
article_id: 360026782773
category: Materiais - Compras (SIGACOM)
content_hash: 367c8a0b6ae1b85337edef8624ce930fcd35ad8deadb4f26458c8b67cce88cf8
fetched_at: '2026-06-28T22:41:17.698255+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Exemplo de Alçada com
  Centro de Custo (Entidades Contábeis)
type: support-article
updated_at: '2022-05-18T20:50:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026782773-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Exemplo-de-Al%C3%A7ada-com-Centro-de-Custo-Entidades-Cont%C3%A1beis
---

**Dúvida**

Exemplo de Alçada com Centro de Custo (Entidades Contábeis)

**Ambiente**Protheus – Compras – A partir da versão 12

**Solução**

É necessário configurar os parâmetros **MV\_APRPCEC=T (Pedido de Compras), MV\_APRSCEC=T (Solicitação de Compras)** e **MV\_ALTPDOC=T**

Cadastro de Aprovadores rotina MATA095 informação do valor disponível para aprovação e se diário, semanal ou mensal e moeda.

Cadastro do Perfil de Aprovação rotina COMA210 informar range de aprovação para o bloqueio do pedido, valor mínimo e máximo e a moeda.

Cadastro do Grupo de Aprovação  rotina MATA114  na pasta cadastrais informar o(s) aprovador(es) que participarão do grupo, nível, tipo de aprovador se é apenas um vistador ou aprovador, limite automático se sim ira validar o range informado no perfil de aprovação para o bloqueio como não bloqueara qualquer valor, Tipo de liberação Usuário, Nível ou Documento e o perfil de aprovação.

Na pasta Tipos de Documentos flag a opção Item pedido.

Na pasta Entidades contábeis informar o centro de custo, conta contábil, classe de valor e ou item contábil que fara parte de seu grupo para aprovação.

*Observação:* Ao incluir o pedido o sistema validara o bloqueio de acordo com os valores definidos no range do perfil de aprovação e deverá conter as informações cadastradas em seu grupo como centro de custo e entidade contábil e classe de valor e item contábil.

Exemplo de Configuração e funcionamento do processo:

No cenário a seguir há 3 itens no Pedido de Compras:

|  |  |  |
| --- | --- | --- |
| **ITEM** | **VALOR** | **ENTIDADE CONTÁBIL** |
| 0001 | 29.000,00 | 113 |
| 0002 | 29.000,00 | 113 |
| 0003 | 31.000,00 | 112 |

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042490113/mceclip0.png)

Dentro do Pedido de Compras (***MATA120/MATA121***) é possível consultar para quais aprovadores constam pendentes os registros através do botão **Outras Ações > Aprovac.**:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042492053/mceclip2.png)

Neste cenário a liberação fica pendente para dois aprovadores de acordo com o cadastro do Perfil de Aprovação (***COMA210***).

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042491873/mceclip1.png)

No Grupo de Aprovação (***MATA114***) é definido o aprovador, a hierarquia, e o centro de custo para aprovação:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041651014/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042494233/mceclip1.png)

Com a configuração acima o sistema levará a pendência de Aprovação de Documentos (***MATA094***) dos itens do Pedido de Compras para usuários diferentes devido os valores e os centros de custos. É possível notar que para o item 0003 consta na alçada dos dois aprovadores devido o Perfil do Aprovador:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041653394/mceclip4.png)

A legenda é apresentada diferente para cada usuário obedecendo o hierarquia informada no Grupo de Aprovação.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042494733/mceclip3.png)

**Parâmetros envolvidos no processo:**

* MV\_APRPCEC
* MV\_APRSCEC
* MV\_ALTPDOC

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)

[Grupo de Aprovação (MATA114)](https://tdn.totvs.com/pages/releaseview.action?pageId=274637723)
