---
article_id: 360036372794
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 20fc4b80cc08f8ee3d47d6ee426cf2846248c2721d7bc58a49e7ccef3ec7220e
fetched_at: '2026-06-28T22:42:02.624030+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos- Sped Fiscal
  - Notas Fiscais de Serviço Estão Sendo Apresentadas no Sped Fiscal.
type: support-article
updated_at: '2024-06-14T14:46:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036372794-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-Notas-Fiscais-de-Servi%C3%A7o-Est%C3%A3o-Sendo-Apresentadas-no-Sped-Fiscal
---

**Dúvida**Notas fiscais de serviço estão sendo apresentadas no **Sped Fiscal** indevidamente. A espécie utilizada no lançamento da nota fiscal de serviço está incorreta.  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80.  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Verifique se a espécie utilizada no lançamento da nota fiscal de serviço é uma das espécies listadas abaixo:

Espécie="**NFS**" modelo " " // NF Serviço  
Espécie = "**NFPS**" modelo " " // NF Prestação de Serviço  
Espécie="**RPS**" modelo " " // Recibo Provisório de Serviços - Nota Fiscal Eletrônica  
Espécie = **SPED** modelo "55" // Exclusiva para **DF - DISTRITO FEDERAL** - Nota fiscal eletrônica

2. Se a espécie utilizada é diferente das espécies citadas no item anterior, será necessário corrigir a espécie e selecionando uma das espécies listadas, pois assim, o sistema entenderá que trata-se de uma nota fiscal de serviço e não levará a nota para o arquivo magnético.

3. Caso não seja possível utilizar uma das espécies mencionadas, então, na TES, os campos **F4\_LFICM**, **F4\_LFISS** e **F4\_LFIPI** devem ser preenchidos = **NÃO**, pois neste caso, entendemos que não trata-se de um documento fiscal.
