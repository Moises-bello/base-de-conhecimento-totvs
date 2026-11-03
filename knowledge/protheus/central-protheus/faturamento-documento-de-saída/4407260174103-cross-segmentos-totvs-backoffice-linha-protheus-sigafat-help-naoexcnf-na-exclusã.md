---
article_id: 4407260174103
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 6265950a7688d3289508ac21bddbdf615cfa494340edd828464e3a6ec33ec872
fetched_at: '2026-06-28T22:38:45.074114+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Help NAOEXCNF
  na exclusão da Nota
type: support-article
updated_at: '2025-05-26T12:51:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407260174103-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-NAOEXCNF-na-exclus%C3%A3o-da-Nota
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao tentar excluir um Documento de Saída (MATA521A) o sistema apresenta o Help NAOEXCNF.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - todas as versões.  
  
**Causa**Ao tentar excluir um documento de saída (MATA521A), o sistema pode apresentar o Help **NAOEXCNF** indicando que há um título de imposto, gerado por este documento de saída, que sofreu uma baixa, total ou parcial. O sistema também demonstrará o número do título.

Ao excluir o documento, o sistema exclui todos os registros vinculados a ele para manter a integridade dos dados, caso o título vinculado tenha sofrido baixa é necessário volta-lo para o Status "Em carteira" para que o mesmo possa ser excluído.  
  
**Solução**Para que o documento possa ser excluído:

1. Estorne a baixa do título de imposto informado no Help NAOEXCNF;

2. O título voltará ao Status "em carteira";

3. Realize a Exclusão do Documento de Saída (MATA521A).
