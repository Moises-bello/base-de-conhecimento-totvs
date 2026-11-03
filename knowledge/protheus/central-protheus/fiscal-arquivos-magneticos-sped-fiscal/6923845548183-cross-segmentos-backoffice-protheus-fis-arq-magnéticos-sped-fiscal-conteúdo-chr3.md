---
article_id: 6923845548183
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: c1f0ac8a1184358e391d6b1f06f63da117c3564ed2b5e12d1bb60cc4de9e13f1
fetched_at: '2026-06-28T22:42:02.312021+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED Fiscal
  - Conteúdo CHR(39)|| ou +CHAR(39) apresentado no arquivo do Sped Fiscal
type: support-article
updated_at: '2022-06-22T10:56:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6923845548183-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-Fiscal-Conte%C3%BAdo-CHR-39-ou-CHAR-39-apresentado-no-arquivo-do-Sped-Fiscal
---

**Ocorrência**Ao gerar o arquivo txt do SPED Fiscal está sendo apresentado o conteúdo CHR(39)|| ou +CHAR(39).  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - A partir da versão 12.1.25  
  
**Causa**  
Este incidente foi mapeado e corrigido. O problema ocorria  nos casos em que os cadastros de clientes, produtos ou descrições possuíssem um **apóstrofo (')**. O sistema estava gravando no arquivo o conteúdo **CHR(39) ||** em banco de dados Oracle e **+CHAR(39)** em banco de dados SQL.

**Solução**Para que o problema não fosse mais apresentado, foi realizado um tratamento no fonte SPEDXFUN.PRW, para que, nos casos em que o sistema estiver realizando o controle do buffer do insert em tabelas temporárias (FwBulk) não realize um tratamento prévio da string que contém a query através da função SPDQRYCH.  
  
A correção é contemplada no pacote de atualização abaixo:

12.1.27:<https://suporte.totvs.com/portal/p/10098/download?e=1071303>;

12.1.33:<https://suporte.totvs.com/portal/p/10098/download?e=1071304> ;

Para acessar a documentação da solicitação acesse o link: <https://tdn.totvs.com/pages/viewpage.action?pageId=694110242>
