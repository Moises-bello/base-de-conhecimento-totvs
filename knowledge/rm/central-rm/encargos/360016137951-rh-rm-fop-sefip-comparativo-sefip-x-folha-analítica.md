---
article_id: 360016137951
category: Encargos
content_hash: 0e9e7e4a1bc0286e68252016f48b836b7734a97e37bbff0b3764c59d546ffb31
fetched_at: '2026-06-28T22:46:53.380320+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: 'RH - RM - FOP - SEFIP: Comparativo SEFIP x Folha Analítica'
type: support-article
updated_at: '2025-03-13T10:09:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016137951-RH-RM-FOP-SEFIP-Comparativo-SEFIP-x-Folha-Anal%C3%ADtica
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura**: 00:01:20 min****Dúvida**Como gerar o arquivo Comparativo SEFIP x Folha Analítica?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para gerar o arquivo **Comparativo SEFIP x Folha Analítica** deverá seguir os passos a seguir.  
  
1. Acesse Folha Mensal | Folha Analítica e gere o relatório da Folha Analítica no formato **NET.txt ,** conforme print abaixo:

O código do relatório a ser usado é o **FOPREL0009**. Para correta geração, deve marcar a flag **PDF**, e marcar a flag **Gerar arquivo para comparativo SEFIP x Folha Analítica**

![](https://totvssuporte.zendesk.com/attachments/token/wYZxJRVYximYCBchuMBBRApf1/?name=inline-81865843.png)

Após concluir, o arquivo será gerado com a estrutura conforme print abaixo:

![](https://totvssuporte.zendesk.com/attachments/token/91XRYsaqkgYZOWkKEKgx5YjvK/?name=inline1287324498.png)  
2. Acesse **Encargos | SEFIP | Geração SEFIP** para gerar a **SEFIP**. Ao gerar a **SEFIP**, importe o arquivo RE para para o validador e depois será gerado outro arquivo com a extensão SFP, o arquivo **SEFIP-SFP.**  
  
3. Acesse **Encargos | SEFIP | Comparativo SEFIP x Folha Analítica** e informe o arquivo NET.txt da Folha Analítica gerado e o arquivo **SEFIP-SFP** gerado do validador. A geração será feita com o relatório **FOPREL00006**. Informe um diretório para salvar e execute a rotina.

![comparativo.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360011673872/comparativo.jpg)

4. Para fazer comparação dos valores, perceba que os valores divergentes serão apresentados na cor vermelha.

![fsfsfssf.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360011667531/fsfsfssf.jpg)

**Saiba mais**  
[Comparativo SEFIP x Folha Analítica](https://tdn.totvs.com/pages/releaseview.action?pageId=452719469)
