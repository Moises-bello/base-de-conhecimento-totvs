---
article_id: 1500004464142
category: Rescisão
content_hash: 61396ef312e5c64734022b036437923446d6887731811bb0df55fa743beaa417
fetched_at: '2026-06-28T22:46:55.240688+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - TRCT: Considerar um dia útil antes do Aviso Prévio Trabalhado
  (Campo 25)'
type: support-article
updated_at: '2022-10-20T21:26:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004464142-RH-RM-FOP-TRCT-Considerar-um-dia-%C3%BAtil-antes-do-Aviso-Pr%C3%A9vio-Trabalhado-Campo-25
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: 00:01:20 min**

**Dúvida**

Para aviso Prévio Trabalhado, como considerar um dia útil antes no início do aviso (Campo  25)?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**

Este parâmetro está presente na rotina do TRCT, em Folha de Pagamento | Rescisão | Relatórios | TRCT | Portaria 1621/2010, para que ao gerar TRCT para funcionário com Aviso Prévio Trabalhado, seja levada no campo '25 - Data do Aviso Prévio', a data com um dia útil anterior ao cadastrado:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005727801/mceclip0.png)  
  
Exemplo:

Para um funcionário com Aviso Prévio Trabalhado, data 12/11/2021:  
  
![](https://tdn.totvs.com/download/attachments/520681839/image2019-11-18_11-28-42.png?version=1&modificationDate=1574090923427&api=v2)  
  
No arquivo será levada a data 11/11/2021:  
  
![](https://tdn.totvs.com/download/attachments/520681839/image2019-11-18_12-39-41.png?version=1&modificationDate=1574095181973&api=v2)  
  
**Observações:**

1. Para funcionários com data iniciada em sábado, domingo ou feriados, será considerada a data do último dia útil anterior a data cadastrada;

2. Para funcionários com Aviso Prévio Misto, com o parâmetro marcado, também retornará um dia útil anterior a data inicial do Aviso Trabalhado;

3. Ao marcar os parâmetros 'Para aviso Prévio Trabalhado considerar um dia útil antes no início do aviso (Campo 25)' e 'Data Aviso Prévio Indenizado igual à data de demissão', também retornará um dia útil anterior a data inicial do Aviso Trabalhado.  
  
**Saiba mais**:

[TRCT - Emissão do arquivo no TOTVS Folha de Pagamento](https://tdn.totvs.com/pages/releaseview.action?pageId=42042615)
