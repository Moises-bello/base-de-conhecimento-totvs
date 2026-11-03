---
article_id: 4459170494999
category: TAF - eSocial - Eventos Periódicos
content_hash: c4fb726746169836fb1f934741e35d3921e8eac83beae3ba7f1af33099385967
fetched_at: '2026-06-28T22:45:19.124523+00:00'
product: protheus
section_id: 1500001536901
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial-Periódicos - S-1260 - Erro de schema::
  Element ´{http://www.esocial.gov.br/schema/evtComProd/v02_05_00}ideEstabel´: Missing
  Child element(s). expected is ( http://www.esocial.gov.br/schema/evtComProd/v02_05_00}tpComer
  )'
type: support-article
updated_at: '2024-05-24T19:00:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4459170494999-RH-Linha-Protheus-TAF-eSocial-Peri%C3%B3dicos-S-1260-Erro-de-schema-Element-http-www-esocial-gov-br-schema-evtComProd-v02-05-00-ideEstabel-Missing-Child-element-s-expected-is-http-www-esocial-gov-br-schema-evtComProd-v02-05-00-tpComer
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23692587878935) Tempo aproximado para leitura: **05:00:00 min****Ocorrência**

Ao tentar transmitir (enviar) o evento de medicina **S-1260 -** **Comercialização da Produção Rural Pessoa** **Física** (TAFA414)é retornado Erro de Schema:

*Erro de schema:: Element ´{http://www.esocial.gov.br/schema/evtComProd/v02\_05\_00}ideEstabel´: Missing Child element(s). expected is ( http://www.esocial.gov.br/schema/evtComProd/v02\_05\_00}tpComer ).*

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Periódicos - S-1260 -Comercialização da Produção Rural Pessoa Física – (TAFA414)- Todas as versões  
  
**Causa**O governo está esperando que informe a tag <*tpComer*> para validar a  tag <*ideEstabel*>.  
  
**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse a rotina do evento S-1260, no TAF:

[TAF - EVENTOS PERIÓDICOS - S-1260 - Como incluir as notas de Comercialização da Produção Rural Pessoa Física no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404851618839)

2. Realizar o preenchimento dos campo **"Indic. Comer"** e **"vrTotCom"** localizados dentro do grupo **Total da Comercialização por Tipo de Comercialização.**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4459157873047)

3. Salve a alteração.

**Observação:**

Estamos orientando o preenchimento manual dentro do TAF, caso deseje que o campo venha do ERP de origem correto, realizar a abertura de um chamado no Setor (módulo) onde o XML foi gerado, para que receba a orientação quanto a geração desta tag.
