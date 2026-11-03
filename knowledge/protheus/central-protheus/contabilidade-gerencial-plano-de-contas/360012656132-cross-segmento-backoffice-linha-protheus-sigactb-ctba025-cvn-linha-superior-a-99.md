---
article_id: 360012656132
category: Contabilidade Gerencial - Plano de Contas
content_hash: d12e68ff9d9beb111a4082685b91a312fc1d8fd8951364853631ba9dbe5f0a4a
fetched_at: '2026-06-28T22:40:33.385527+00:00'
product: protheus
section_id: 1500001549022
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB CTBA025 : CVN_LINHA superior
  a 999 linhas'
type: support-article
updated_at: '2022-06-20T20:05:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012656132-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA025-CVN-LINHA-superior-a-999-linhas
---

**Dúvida**

Ao plano de contas referencial o sistema  limitou a 999 linhas, qual o  procedimento para que a tabela CVN suporte linhas superiores a 999  
   
 **Ambiente**Protheus – Contabilidade – A partir da versão 11.80  
  
   
**Solução**

Por padrão o campo CVN\_LINHA possui tamanho 3, em caso de alteração do tamanho deve-se seguir os seguintes passos  
1 - Exportar os planos de contas referenciais existentes  
2 - Através do configurador altere o tamanho do campo  
3 - Salve  a alteração   
4 - Recrie a tabela CVN  
5 - Importe os planos referenciais existentes

Este procedimento é necessário pois o campo CVN\_LINHA é alimentado com 0(zero) a esquerda de acordo com o tamanho do campo.

Documentações relacionadas

Documentação :[552100 DSERCTR1-162 DT Chave duplicada CVN\_LINHA](http://tdn.totvs.com/display/PROT/552100+DSERCTR1-162+DT+Chave+duplicada+CVN_LINHA)

Patch :<https://suporte.totvs.com/portal/p/10098/download?e=571197>
