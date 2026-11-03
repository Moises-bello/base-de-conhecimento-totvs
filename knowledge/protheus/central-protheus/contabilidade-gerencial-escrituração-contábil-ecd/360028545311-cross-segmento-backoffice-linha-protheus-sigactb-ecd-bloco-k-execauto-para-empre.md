---
article_id: 360028545311
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 70a607f625dacfbe8080b2913c681cf551cdcd123259b9169b0164a885e8c915
fetched_at: '2026-06-28T22:40:44.230055+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus  - SIGACTB - ECD BLOCO K - EXECAUTO
  PARA EMPRESAS QUE NÃO ESTÃO NÃO SIGAMAT '
type: support-article
updated_at: '2022-07-18T20:15:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028545311-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-BLOCO-K-EXECAUTO-PARA-EMPRESAS-QUE-N%C3%83O-EST%C3%83O-N%C3%83O-SIGAMAT
---

**Dúvida**

O Protheus possibilita gerar o bloco K da ECD para empresas que não estão no SIGAMAT  
  
**Ambiente**  
Microsiga Protheus – Contabilidade – A partir da versão P12  
  
**Solução**

Foi liberado um Execauto  FWMVCRotAuto  que pode ser configurado para que o bloco K seja gerado para empresas que não estão no sigamat

Para mais detalhe verifique : <http://tdn.totvs.com/pages/releaseview.action?pageId=362453480>

#### 

**Para seu conhecimento :**

#### A Issue DSERCTR1-21129  está em andamento como "Solicitação de Melhoria " onde  esta sendo avaliado pelo desenvolvimento a possibilidade de  :

* empresa não tenha necessidade de estar no Sigamat (Licença) do Protheus
* os lançamentos do bloco K sejam integrado de outro Sistema (segregado) ,diretamente para as ["Tabelas da ECD"](http://tdn.totvs.com/pages/releaseview.action?pageId=287077842) e rotina de escrituração
* ao gerar o arquivo a a rotina de escrituração busque diretamente de outro Sistema (segregado) sem a necessidade de buscar dados (cadastrais e saldos) no Protheus

Veja mais:

[-ECD Layout 7 SPED Bloco K saldos consolidados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026403252-MP-SIGACTB-ECD-Layout-7-SPED-Bloco-K-saldos-consolidados?source=search)

[-ECD SPED CONTABIL TABELA E ROTINA Bloco K](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013554251-MP-SIGACTB-ECD-SPED-CONTABIL-TABELA-E-ROTINA-Bloco-K?source=search)
