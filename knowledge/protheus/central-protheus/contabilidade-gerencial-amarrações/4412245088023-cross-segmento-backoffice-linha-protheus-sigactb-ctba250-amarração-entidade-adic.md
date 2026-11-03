---
article_id: 4412245088023
category: Contabilidade Gerencial - Amarrações
content_hash: 841f955c143b9fb1e8f7767b2231bf3bce908a782694835efce29f2cd7087e7a
fetched_at: '2026-06-28T22:41:05.764765+00:00'
product: protheus
section_id: 1500001548302
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA250 - AMARRAÇÃO
  ENTIDADE ADICIONAL
type: support-article
updated_at: '2025-01-22T14:43:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412245088023-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA250-AMARRA%C3%87%C3%83O-ENTIDADE-ADICIONAL
---

**Dúvida**Como realizar amarração da entidade adicional a outras entidades

Sistema não esta possibilitando a amarração das entidades adicionais as demais entidades   
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - Contabilidade Gerencial - Todas as versões

**Solução**

A amarração da CTA, é realizada através  da rotina de [amarração CTBA250 - Em Atualizações / Cadastros  / Amarrações (CTBA250),](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000607608-MP-SIGACTB-Amarra%C3%A7%C3%A3o-Cont%C3%A1bil-n%C3%A3o-Valida-Entidades?source=search)  
  
O cadastro das entidades adicionais (05 ...) não existe tratamento para campos de regra e contra regra.

* Isso quando parâmetro [MV\_CTBAMAR = 1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006746912-MP-SIGACTB-CTBA250-Valida%C3%A7%C3%A3o-de-Amarra%C3%A7%C3%B5es?source=search)
* Já quando  o parâmetro [MV\_CTBAMAR = 2](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006746912-MP-SIGACTB-CTBA250-Valida%C3%A7%C3%A3o-de-Amarra%C3%A7%C3%B5es?source=search) o sistema permite amarrar entidade adicionais as demais entidades (Plano de contas, centro de custo, item contábil e classe de valor)

1º Após executar o**[U\_CTBWIZENT](https://tdn.totvs.com/pages/releaseview.action?pageId=59900337)**o sistema irá criar os campos das  [Entidades adicionais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013316351-MP-SIGACTB-Entidades-adicionais?source=search)

2º Realize a  [Inclusão entidade adicional](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018873072-MP-SIGACTB-Como-Incluir-entidade-adicional?source=search)   através da rotina CTBA005 

Ex.: Para entidade 05 Ent THOM foi criada "T001 THOMMY" 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412258135959/mceclip0.png)

3º Através da rotina de amarração  [(CTBA250),](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000607608-MP-SIGACTB-Amarra%C3%A7%C3%A3o-Cont%C3%A1bil-n%C3%A3o-Valida-Entidades?source=search)​​​ , sistema apresenta a entidade cadastrada

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412258474263/mceclip1.png)

* Selecione a entidade

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412244945943/mceclip2.png)

4º Posicione sobre a entidade  que deseja amarração exemplo abaixo Plano de contas

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412273773847/mceclip3.png)

* Selecione a conta ,  o sistema relaciona a conta a entidade 05 Ent THOM , veja que a parte inferior em nenhum momento fica editável

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412244977047/mceclip4.png)

5º Posicione  sobre a entidade  Centro de custo  que deseja amarrar 

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412273809303/mceclip5.png)

* Selecione o centro de custo , veja que o sistema relacionou  o centro de custo a entidade 05 Ent THOM .

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412258608151/mceclip6.png)

6º Ao salvar o sistema  amarrar as amarrado as entidades  relacionadas

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412258633367/mceclip7.png)
