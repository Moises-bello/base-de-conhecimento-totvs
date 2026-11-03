---
article_id: 360021654772
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: f0c5722a4843a7497af1841f580d84cf74743419b5e2898e3ccda47e56561dcd
fetched_at: '2026-06-28T22:42:07.782342+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Extrator Fiscal
  não gera o layout T020
type: support-article
updated_at: '2022-08-18T17:29:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021654772-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Extrator-Fiscal-n%C3%A3o-gera-o-layout-T020
---

**Ocorrência**O Extrator Fiscal não esta alimentando a tabela TAFST1 com o Layout **T020 - Apuração do ICMS**  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Causa**Este incidente ocorre quando o campo **CDH\_PERIOD** esta diferente de 1º  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Realize a Apuração do ICMS novamente e informe o período igual a 1º - Período;  
2. Acesse o Extrator Fiscal novamente, informe o período e responda a pergunta **Deseja Integrar?**igual a 3-Ambos ;  
3. Selecione somente o Layout T020 e Confirme.
