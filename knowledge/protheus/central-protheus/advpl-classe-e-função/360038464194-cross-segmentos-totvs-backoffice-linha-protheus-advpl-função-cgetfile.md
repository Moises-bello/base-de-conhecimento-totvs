---
article_id: 360038464194
category: ADVPL - Classe e Função
content_hash: 4febfd4788d311fdd96cb34ea7f08eded66ee6c0283c8b6148422d3d984cc2a5
fetched_at: '2026-06-28T22:40:19.325745+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Função cGetFile
type: support-article
updated_at: '2022-01-10T19:04:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038464194-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-cGetFile
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min****Dúvida**O componente cGetFile, o mesmo possui um comportamento ao selecionarmos a coluna, ele ignora o nome do arquivo e considera somente conteúdo da coluna selecionada. Esse é o comportamento adequado da função?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) - ADVPL - A partir da versão 12.1.23  
  
**Solução**É comportamento da função, e não interfere no funcionamento. O comportamento não foi alterado, foi implementado no Lobo-Guara colunas com mais informações do arquivo como tamanho e data/hora.  
No NG(12.1.17) somente existia a coluna do nome do arquivo, sendo assim era somente retornado o mesmo.   
**Comportamento atual:**Forçar o usuário a selecionar a coluna correta, sendo que ao clicar na coluna a linha inteira fica selecionada, **retornando apenas o valor da coluna.**
