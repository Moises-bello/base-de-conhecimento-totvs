---
article_id: 360018299971
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: 875f56dcb6a93ea89c16552188986fb341278f0a565a953771bfe6b8e0618fad
fetched_at: '2026-06-28T22:41:48.238116+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA012/ATFA240 - Ao
  digitar o grupo de bens, as informações referentes a contabilidade são apagadas
type: support-article
updated_at: '2023-11-30T11:59:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018299971-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-ATFA240-Ao-digitar-o-grupo-de-bens-as-informa%C3%A7%C3%B5es-referentes-a-contabilidade-s%C3%A3o-apagadas
---

**Ocorrência**

Ao utilizar a **classificação de ativo(ATFA240) ou a inclusão(ATFA012)**, ao selecionar um grupo é apresentada a mensagem:

Essa alteração implicará na perda dos dados digitados,deseja continuar ?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013518872)

Caso a resposta seja **SIM** algumas informações da **Contabilidade e Valor da Moeda 1 são zeradas**.

**Ambiente**Protheus – Ativo Fixo – 12.1.17

**Causa**Pode ser causado por dois motivos:

**1-** Rotina ATFA012 anterior a data 27/09/2018  
**2-** Os campos da tabela FNG estarem vazios para esse grupo.  
**3 -**  Tabelas FNG e SNG estão com o compartilhamento diferente

**Solução**

Para solucionar essa questão siga os passos abaixo:

**1-** Caso a rotina **ATFA012** se encontre **anterior a data 27/09/2018**, aplique o seguinte pacote:  [DSERCTR1-14600](https://tdn.totvs.com/pages/releaseview.action?pageId=382557083)

**2-** Verifique se a **linha referente a tabela FNG do grupo utilizado** está preenchida conforme imagem:

![](https://totvssuporte.zendesk.com/attachments/token/1yFNejgddjjg6KUIyxCvmWHNf/?name=inline1541151856.png)

**Caso contrário, o mesmo deve ser cadastrado para o funcionamento correto do gatilho de grupos**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000430341)Conceito e configurações [N1\_GRUPO na Classificação dos bens oriundos de documento de entrada e do cadastro do ativo (ATFA012).](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017504832-MP-SIGAATF-ATFA240-Classifica%C3%A7%C3%A3o-de-Bens)
