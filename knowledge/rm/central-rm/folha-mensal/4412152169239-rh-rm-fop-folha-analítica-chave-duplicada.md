---
article_id: 4412152169239
category: Folha Mensal
content_hash: 6284c441d237fb59a6c8d51df1234c8518c826a14e590d4295f6d1b59cb8ac1a
fetched_at: '2026-06-28T22:46:59.362887+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Folha Analítica: Chave Duplicada'
type: support-article
updated_at: '2024-10-04T19:07:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412152169239-RH-RM-FOP-Folha-Anal%C3%ADtica-Chave-Duplicada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26845464237463)**Tempo aproximado para leitura: **00:01:25 min****Ocorrência**Ao gerar folha analítica, o sistema apresenta a seguinte mensagem de erro: **Chave Duplicada.**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412157612311)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**A mensagem de erro ocorre pois, existe mais de um mesmo layout importado no sistema ou o layout importado está parametrizado incorretamente.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Verifique se em **Gestão | RM Reports** haja a existência de 2(dois) arquivos com o mesmo código.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26845477151127)  
  
2. Caso positivo, realize a exclusão de ambos os relatórios da folha analítica importados. Segue abaixo documentação para lhe auxiliar no processo.  
  
[RH - RM - FOP - RM Reports: Exclusão de Relatórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411688075799-RH-RM-FOP-RM-Reports-Exclus%C3%A3o-de-Relat%C3%B3rios?source=search)  
  
3. Logo, importe o **relatório FOPREL0009** novamente. Segue abaixo documentação para lhe auxiliar no processo.  
  
[RH - RM - FOP - RM Reports: Importação de Relatórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007544951-RH-RM-FOP-RM-Reports-Importa%C3%A7%C3%A3o-de-Relat%C3%B3rios?source=search)  
  
4. Feito os passos 1, 2 e 3, verifique no cadastro do relatório o **Tipo** informado. O correto seria o **193 - Folha Analítica**.  
  
**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412157522839)****5.** Em seguida, gere a folha analítica novamente.
