---
article_id: 360025548013
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 40249936a8bfff92367a8363c1b6e9d15eda9505fe760a213f99dea6f35e3a68
fetched_at: '2026-06-28T22:42:07.941312+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Preenchimento
  do Campo Ind Isenção - C30_INDISE = 1
type: support-article
updated_at: '2022-08-18T17:45:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025548013-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Preenchimento-do-Campo-Ind-Isen%C3%A7%C3%A3o-C30-INDISE-1
---

**Dúvida**  
Como preencher o campo Ind Isenção - C30\_INDISE de forma automática no TAF igual a 1?  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 12  
  
**Solução**  
Para que o campo Ind Isenção - C30\_INDISE seja preenchido de forma automática no documento do TAF, será necessário efetuar o cadastro do campo Ind Isen Prv = Sim (F4\_INDISEN) no cadastro do TES. 

Após o correto preenchimento e escrituração do documento nos Livros Fiscais o sistema irá preencher o campo FT\_INDISEN = 1 na tabela SFT. 

Após efetuar o processo acima, será necessário executar o extrator selecionando o layout T013 (Documento Fiscal), e o processamento no TAF.   
  
Abaixo artigos relacionados ao campo C30\_INDISE:  
  
<https://tdn.totvs.com/pages/releaseview.action?pageId=568930485>

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058072493-MP-TAF-Grava%C3%A7%C3%A3o-do-Campo-Id-Aquisi%C3%A7%C3%A3o-CMT-INDAQU-na-Rotina-TAFA272>  
  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058015593-MP-FIS-Fluxo-de-Grava%C3%A7%C3%A3o-do-Campo-Id-Aquisi%C3%A7%C3%A3o-CMT-INDAQU-TAFA272?source=search>
