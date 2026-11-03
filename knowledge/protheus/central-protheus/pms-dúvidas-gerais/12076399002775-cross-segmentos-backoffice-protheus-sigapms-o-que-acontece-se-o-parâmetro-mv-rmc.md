---
article_id: 12076399002775
category: PMS - Dúvidas Gerais
content_hash: 334ec851378f0be5eca5ce7122b75fd9c44ebd340d0252c57e54aa6e0e7420de
fetched_at: '2026-06-28T22:37:17.691778+00:00'
product: protheus
section_id: 1500001539681
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - O que acontece se o parâmetro
  MV_RMCOLIG estiver ativo?
type: support-article
updated_at: '2024-02-23T15:06:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12076399002775-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-O-que-acontece-se-o-par%C3%A2metro-MV-RMCOLIG-estiver-ativo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21567438938519) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**O que ocorre se o parâmetro **MV\_RMCOLIG** estiver ativo? Eu fico sem acessos ao PMS?  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as versões  
  
**Causa**O parâmetro **MV\_RMCOLIG** ativa a integração com o TOP do RM.   
  
**Solução**O **MV\_RMCOLIG** faz parte de uma integração com o produto RM, que envolve a configuração de Procedures e a ativação dos parâmetros, por padrão o preenchimento dos parâmetros é: 

* MV\_INTPMS: N
* MV\_RMCOLIG: 0

**Por padrão com o parâmetro habilitado, você não tem acesso a algumas rotinas do PMS, devido a integração com RM e o sistema apresenta o help:**

![pms.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12076391469463)

**Saiba Mais**  
[TOTVS Obras e Projetos x BackOffice Protheus - Cadastro Empresas/Filiais](https://tdn.totvs.com/pages/releaseview.action?pageId=425459668)

[Integração Protheus X TOP – Totvs Obras e Projetos](https://tdn.totvs.com/pages/releaseview.action?pageId=6795080)
