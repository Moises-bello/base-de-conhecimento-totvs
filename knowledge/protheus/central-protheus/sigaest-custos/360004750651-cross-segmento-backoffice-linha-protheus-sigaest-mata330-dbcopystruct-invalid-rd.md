---
article_id: 360004750651
category: SIGAEST - CUSTOS
content_hash: 8c01e11403a4abcea1dc2acbac2d5872da4ec7b496002471e527bdb4419174e5
fetched_at: '2026-06-28T22:39:00.403370+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - DBCopyStruct
  Invalid RDD CTREE on MA330PROCESS
type: support-article
updated_at: '2025-03-12T12:22:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004750651-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-DBCopyStruct-Invalid-RDD-CTREE-on-MA330PROCESS
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30503448199959)**Tempo aproximado para leitura: **00:01:00min**

**Ocorrência**No modulo Estoque/Custos,ao realizar o processamento da rotina Recálculo do Custo Médio, é apresentado o error.log "**DBCopyStruct - Invalid RDD CTREE on MA330PROCESS(MATA330)"** impedindo o termino do processamento.  
  
**Ambiente**Protheus – Estoque/Custos – A partir da versão 12.1.17  
  
**Causa**   
Esse incidente ocorre devido ao conteúdo do parâmetro **MV\_A330DRV**que está inválido.  
  
**Solução**  
Para solucionar este problema, realize os seguintes passos:  
1. Avalie o conteúdo do parâmetro **MV\_A330DRV**através do modulo Configurador (SIGACFG);  
2. Ajuste para o valor "**DBFCDX**" sem as aspas;  
3 . Execute novamente o Recálculo do Custo Médio.

**Saiba mais:**

[Tec - Função Dbcreate](http://tdn.totvs.com/display/tec/DBCreate)

[MP - SIGAEST - Lentidão na rotina de Recálculo do Custo Médio (MATA330)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047206834)

[MP- SIGAEST - Erro na Chamada do Processo na MATA330 (Recálculo do Custo Médio)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027658632)

[MP - SIGAEST - MATA330 - Error.log (THREAD ERROR type mismatch on $ on A330NIVCQ)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059194234)

[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
