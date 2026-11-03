---
article_id: 11919290791063
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: fa87f8a42fd88dbb51ce77e3b23468a401e0ba4be9524d34f715e55918df1270
fetched_at: '2026-06-28T22:42:04.865376+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - EFD Contribuições
  - Registros A100/170 duplicado no arquivo '
type: support-article
updated_at: '2023-10-17T20:40:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11919290791063-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Registros-A100-170-duplicado-no-arquivo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao gerar o **EFD Contribuições** os registros **A100/170** são gerados em duplicidade.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Causa**A duplicidade ocorre devido à  escrituração incorreta na nota, no que diz respeito ao cadastro de **TES** utilizado. Dessa forma, são geradas duas linhas na tabela **SF3 - Livros Fiscais** o que ocasiona a duplicidade.  
  
**Solução**Para que o problema não ocorra é preciso que o cadastro de **TES** utilizado na escrituração das notas, tenham as seguintes configurações quanto aos campos destacados abaixo:

![](https://totvssuporte.zendesk.com/attachments/token/o5aOz9MZELAjUEMBZAZYedzWc/?name=inline1019203245.png)  
  
Se o campo **L.Fiscal.ISS** diferente de Não, os campos **L.Fisc.ICMS** e **L.Fiscal.IPI** precisa estar = N-Não e vice versa.   
Isso para não gerar a duplicidade na tabela **SF3**. 

Para as notas já escrituradas dessa forma, realize o seguinte procedimento:

1. Faça alteração no cadastro de **TES**;  
2. Reprocesse as notas em questão para que o **Protheus** delete as duas linhas geradas na tabela **SF3**;  
3. Apure novamente o período;  
4. Gere novamente o Arquivo **EFD****Contribuições**.
