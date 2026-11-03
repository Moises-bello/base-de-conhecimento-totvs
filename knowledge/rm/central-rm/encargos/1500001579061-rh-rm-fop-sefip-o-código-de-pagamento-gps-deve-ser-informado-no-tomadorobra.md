---
article_id: 1500001579061
category: Encargos
content_hash: d0c34547b7378f21fafc5c13f552ca16ad02805ff0e654dbc3cf0671efb53c0a
fetched_at: '2026-06-28T22:46:52.133241+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: 'RH - RM - FOP - SEFIP: O código de pagamento GPS deve ser informado no Tomador/Obra'
type: support-article
updated_at: '2025-03-12T10:06:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001579061-RH-RM-FOP-SEFIP-O-c%C3%B3digo-de-pagamento-GPS-deve-ser-informado-no-Tomador-Obra
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**Após gerar o arquivo **SEFIP** e importar para o aplicativo, é apresentada a mensagem de erro: **O código de pagamento GPS deve ser informado no Tomador/Obra:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100439554/mceclip0.png)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Esse erro ocorre quando, no cadastro do cliente/fornecedor que representa o tomador de serviço, não está informado o código de GPS.

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. No cadastro do **cliente/fornecedor I Integrações I Tributos**, informe o número em **Código de Pagamento GPS:**  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8739242087575/mceclip1.png)  
  
2**.** Acesse **Encargos | Liberação de Flags FGTS** e execute a rotina;  
  
3**.**Realize a geração da **SEFIP** novamente e importe para o aplicativo.
