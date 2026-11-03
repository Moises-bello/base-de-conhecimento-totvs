---
article_id: 16027352703639
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 44be0a3f72fdbf621dc6d1742d2e40ecce6d8ec405b2cc9f86069afcf8218342
fetched_at: '2026-06-28T22:40:48.912325+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001-ECF - Como corrigir
  meu arquivo txt que gerou períodos, ou valores divergentes (K030, N030)
type: support-article
updated_at: '2025-05-28T14:15:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16027352703639-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Como-corrigir-meu-arquivo-txt-que-gerou-per%C3%ADodos-ou-valores-divergentes-K030-N030
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16027377517847) Tempo aproximado para leitura: **00:05:00 min****Dúvida**  
Como corrigir meu arquivo txt que gerou períodos, ou valores divergentes (K030, N030)?

DT\_FIN - K030 - foi gerado do 01/01 a 31/01 para o Bloco T01 (Trimestral)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17264913872407)  
Neste caso, o correto era o sistema ter gerado  K030 de 01/01 31/03 para o Bloco T01 (Trimestral).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17264908441239)

**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
**Solução**  
Para solucionar esse erro, realize os seguintes passos:

1.  Excluir todos os registros, através da rotina TAFTICKET ou [através da rotina Exclusão Por Período Fiscal - TAFAEXCPER](https://tdn.totvs.com/pages/releaseview.action?pageId=273986947)  
   
![https://lh6.googleusercontent.com/895e03OXvoASBoDqQ_LMPpnyFekGZE-Kb7MncW0U43dKuWtf_BZdWcuC9HeIVm4ARzJp_nI6sc60pLCDeow5P-OIxkGVHTNyLhkf4yreU14C9sjIE6OyyOYLkX4ty8Xoa0ueQelLLnQJockVuUkdQw](https://totvssuporte.zendesk.com/attachments/token/5AfgD7EcFSZUazGzjZidDfYxn/?name=inlineImage.png)  
   
2. Excluir os registros com períodos divergentes nas rotinas [TAFA311(K030) , TAFA361(L030) , TAFA319(N030)](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512#Obriga%C3%A7%C3%A3oECF-Escritura%C3%A7%C3%A3oCont%C3%A1bilFiscal-BlocoK-SaldosdasContasCont%C3%A1beiseReferenciais),[TAFA321 (L030)](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512#Obriga%C3%A7%C3%A3oECF-Escritura%C3%A7%C3%A3oCont%C3%A1bilFiscal-BlocoK-SaldosdasContasCont%C3%A1beiseReferenciais) Obs: Exclua somente o registro que esta com erro.

3. Excluir as revisões (CTBS001) com o parâmetro **MV\_CTBDLRV  = .T.**  
   
[Cross Segmento - Backoffice Linha Protheus - SIGACTB CTBS001 ECD/ECF Limpeza das tabelas de Revisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026508851-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-ECF-Limpeza-das-tabelas-de-Revis%C3%A3o?source=search)

4. Gere nova revisão, e gere novamente o txt na central de obrigações selecione todos os blocos:

![](https://totvssuporte.zendesk.com/attachments/token/QjjOxX4e6BJbFaoQYqeA7Z8x8/?name=image.png)
