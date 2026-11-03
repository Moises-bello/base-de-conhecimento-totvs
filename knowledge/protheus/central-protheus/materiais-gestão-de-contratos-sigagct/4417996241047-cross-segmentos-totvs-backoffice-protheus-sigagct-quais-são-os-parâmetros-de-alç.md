---
article_id: 4417996241047
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: c8c2a8b6bba9e49828fe518e9f13420cf33443a382cddca343b2e88d08cc59ef
fetched_at: '2026-06-28T22:37:20.298622+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT -  Quais são os Parâmetros
  de alçada de entidades contábeis no Módulo Gestão de Contratos?
type: support-article
updated_at: '2022-01-04T13:57:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417996241047-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Quais-s%C3%A3o-os-Par%C3%A2metros-de-al%C3%A7ada-de-entidades-cont%C3%A1beis-no-M%C3%B3dulo-Gest%C3%A3o-de-Contratos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Quais são os principais Parâmetros de alçada de entidades contábeis no Módulo Gestão de Contratos?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

***MV\_APRMDEC***: controle de alçada por entidades contábeis para itens da medição

***MV\_APRMINV***: habilita aprovação inversa de medição: F - desativado: aprovação por itens e depois por contrato(padrão) / T - ativado: aprovação por contrato e depois por itens- inversa

***MV\_APRCINV***: habilita o fluxo inverso de aprovação de contrato/itens para itens/contratos. f desativado: aprovação por itens e depois por contrato(padrão)/t: ativado. aprovação por contrato e depois por itens, inversa

***MV\_APRCTEC***: habilita o controle de de alçadas por entidades contábeis para os itens de contrato, podendo assumir os seguintes valores: 0- desativado, 1- somente contrato de compras, 2- somente contrato de vendas, 3- todos os contratos

***MV\_APRRVEC***: habilita o controle de alçadas por entidades contábeis para os itens de contrato para as revisões informadas. deve ser informado o número do tipo de revisão, conforme ordem apresentada na tela, separados por ;

**Obs:**

Além de ativar os parâmetros acima de acordo com a necessidade da empresa será necessário realizar outras configurações conforme exemplo nos artigos abaixo em "Saiba Mais".

***Saiba Mais***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Alçada por entidade Contábil na Rotina Nova Medição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012904982-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Al%C3%A7ada-por-entidade-Cont%C3%A1bil-na-Rotina-Nova-Medi%C3%A7%C3%A3o?source=search)

[Cross Segmentos - TOTVS Backoffice Protheus - SIGAGCT - Alçada Por Entidade Contábil na Mudança de Situação do Contrato e / ou Revisão do Contrato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404552326039-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGAGCT-Al%C3%A7ada-Por-Entidade-Cont%C3%A1bil-na-Mudan%C3%A7a-de-Situa%C3%A7%C3%A3o-do-Contrato-e-ou-Revis%C3%A3o-do-Contrato?source=search)

[Tipos de Contratos - CNTA021 - Gestão de Contratos - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=274323782)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
