---
article_id: 8031087513239
category: Funcionários
content_hash: 2f0756879c37487c99493f2a4fce56d793e84d6bb020365f392051784b346848
fetched_at: '2026-06-28T22:47:03.283612+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: RH - RM - FOP - Erro ao acessar cadastro de Dependentes :Ambiguous column name
  CODCOLIGADA Ambiguous column name CHAPA
type: support-article
updated_at: '2025-03-11T10:32:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8031087513239-RH-RM-FOP-Erro-ao-acessar-cadastro-de-Dependentes-Ambiguous-column-name-CODCOLIGADA-Ambiguous-column-name-CHAPA
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30557284894231)** Tempo aproximado para leitura:**00:01:31 min****Ocorrência**Ao acessar o cadastro de dependentes no cadastro de funcionários, ocorre o seguinte erro:

Ocorreu um erro ao efetuar a leitura da visão:  
Ambiguous column name 'CODCOLIGADA'.  
Ambiguous column name 'CHAPA'.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8030773385367)  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Este erro ocorre pois é necessário ajustar a FopDependAction, portanto para correção do erro siga a orientação apresentada no campo solução.    
  
**Solução**Para solucionar a ocorrência acima acesse:  **Serviços Globais | Serviços | Preferências de Anexo**s.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10110128653463)

Procurar e editar a Action Anexo (1) **FopDependAction.**

![](https://totvssuporte.zendesk.com/attachments/token/o6DAxz4gMLCmGJWXtqd5UnDLH/?name=inline-1505052444.png)

Alterar o campo DETALHE para **PFDEPEND.CODCOLIGADA;PFDEPEND.CHAPA**

![](https://totvssuporte.zendesk.com/attachments/token/78rFOo5PTf7FfF2a9SY29W5gu/?name=inline1087314824.png)

**Importante:** reiniciar o Host e aguardar 5 minutos para validar o configuração .
