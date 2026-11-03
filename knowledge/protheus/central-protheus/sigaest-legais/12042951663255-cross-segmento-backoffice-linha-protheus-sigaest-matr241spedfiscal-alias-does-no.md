---
article_id: 12042951663255
category: SIGAEST - LEGAIS
content_hash: b3d186d9c34d89b8ecbd1a60c392c947e7e849be363f56ed1ea10c7ba83c6d16
fetched_at: '2026-06-28T22:38:51.739624+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR241/SPEDFISCAL
  - Alias does not exist SCGN***** on REPORTPRINT(MATR241.PRW)
type: support-article
updated_at: '2023-03-07T14:43:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12042951663255-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR241-SPEDFISCAL-Alias-does-not-exist-SCGN-on-REPORTPRINT-MATR241-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:12 min** **Dúvida**O que fazer quando ocorre o error.log "*Alias does not exist SCGN\*\*\*\*\* on REPORTPRINT(MATR241.PRW)*" no MATR241 (Relação do Bloco K)?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Para correção do errorlog '***Alias does not exist: SCGN on BLOCOK/REPORTPRINT(SPEDXFUN.PRW/MATR241.PRW)***' é necessária a aplicação dos pacotes abaixo:

Testar em ambiente de Homologação antes de sua base oficial com as atualizações a seguir:  
  
-[Acumulado SIGAFIS conforme sua release](https://tdn.totvs.com/pages/releaseview.action?pageId=525823851)  
  
-[Acumulado SIGAEST conforme sua release](https://tdn.totvs.com/x/2hgdHw)  
  
-[LIB Atual](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/) - **[Logo Guará](https://suporte.totvs.com/portal/p/10098/download?e=989259) | [Harpia R.33 e R.2210](https://suporte.totvs.com/portal/p/10098/download?e=1050526)**

-[Appserver](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/) - **[Lobo Guará](https://suporte.totvs.com/portal/p/10098/download#detail/947528) | [Harpia R.33 e R.2210](https://suporte.totvs.com/portal/p/10098/download#detail/1031460)**  
-[Smartclient](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/smartclient) - **[Lobo Guará](https://suporte.totvs.com/portal/p/10098/download#detail/947510) | [Harpia R.33 e](https://suporte.totvs.com/portal/p/10098/download#detail/1031469) [R.2210](https://suporte.totvs.com/portal/p/10098/download#detail/1031460)**  
-[DBAccess](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/)  
  
***Obs:*** Aplicar após backups e validar primeiro em ambiente de homologação.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Legais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)
