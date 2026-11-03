---
article_id: 360006647952
category: Contabilidade Gerencial - Relatórios Razões
content_hash: f43e27224b0f7b35537773ae4c453bd878b235ed47096dbadf75deb2bd2b2848
fetched_at: '2026-06-28T22:40:41.109951+00:00'
product: protheus
section_id: 1500001548782
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Cannot find function
  CONR060  
type: support-article
updated_at: '2022-05-23T20:41:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006647952-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Cannot-find-function-CONR060
---

**Ocorrência**Ao gerar Razão Contábil apresenta erro: **cannot find function CONR060**

**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
  
 **Solução**A rotina CONR060, pertence a o modulo SIGACON que foi descontinuado. No módulo SIGACTB, a rotina responsável pelo relatório razão contábil é o CTBR400 - RAZÃO CONTÁBIL

Verifique se rotina esta disponível em seu menu do módulo SIGACTB, caso não esteja, realize a troca do menu.  
   
 Para maiores informações sobre as alterações no menu, acesse: <http://tdn.totvs.com/pages/viewpage.action?pageId=271164329>
