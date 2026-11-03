---
article_id: 360021889552
category: BI - Business Intelligence - Smart analytics
content_hash: 89e6a291375fe2140f2263d9ffd4586cede01755e7dcd6a74806099298e57cee
fetched_at: '2026-06-28T22:37:04.125365+00:00'
product: protheus
section_id: 1500001539741
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Configurando o arquivo
  Purge para limpeza de dados antigos no GoodData
type: support-article
updated_at: '2022-07-27T18:03:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021889552-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Configurando-o-arquivo-Purge-para-limpeza-de-dados-antigos-no-GoodData
---

**Dúvida**Como configurar o arquivo Purge para posteriormente executar o Graph de limpeza Purge\_history no GoodData e apagar o histórico com os dados mais antigos.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Smart/Fast Analytics - A partir da versão 11.80  
  
**Solução**1. Inicialmente dentro do "data integration console" do GoodData, clique em "download" para baixar os arquivos do projeto e acessar o **fact\_parameters.txt**(TOTVS\_V12) ou **purge\_parameters.txt**(TOTVS\_V11) que está dentro da pasta "data\transform\fact\_parameters.  
2. Após acessar o arquivo, siga as seguintes instruções para configuração do purge: <http://tdn.totvs.com/display/public/PROT/IMP0003_Como_configurar_arquivo_Purge>  
3. Configurado o arquivo Purge, basta salvá-lo e executar o re-deploy do arquivo que foi previamente baixado.  
4. Passo feito, vamos agora executar Graph de limpeza Purge\_History: <http://tdn.totvs.com/pages/releaseview.action?pageId=237375761>  
  
Finalizado tal ação, os dados no projeto deverão levar em conta o período que foi parametrizado dentro **fact\_parameters.txt**(TOTVS\_V12) ou **purge\_parameters.txt**(TOTVS\_V11)
