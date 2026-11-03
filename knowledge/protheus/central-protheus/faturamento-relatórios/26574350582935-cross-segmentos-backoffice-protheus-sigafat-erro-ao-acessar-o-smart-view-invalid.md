---
article_id: 26574350582935
category: FATURAMENTO - RELATÓRIOS
content_hash: ed902a8c4fc4ff8285c2662649eb38e3bfae9351b9262f154a7da2fbc65ffe6e
fetched_at: '2026-06-28T22:38:23.038071+00:00'
product: protheus
section_id: 1500001539381
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Erro ao acessar o Smart View
  Invalid object name 'SX10'.
type: support-article
updated_at: '2024-09-24T10:56:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26574350582935-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Erro-ao-acessar-o-Smart-View-Invalid-object-name-SX10
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26574318217751) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao acessar o Smart View, na tela do Protheus é apresentada a mensagem "Erro na importação do recurso, verificar os logs do Smart view e do Protheus", ao validar os logs, é registrado o seguinte erro:

```
Erro no objeto de negócio 'totvs.protheus.backoffice.com.smartview.integratedprovider.purchasegroupsreportsbusinessobject'  
Invalid object name 'SX10'.
```

**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Causa**O Objeto de Negócio referenciado no erro é responsável por verificar tabelas como a de Peruntas (SX1) no ambiente vinculado ao REST.

Na configuração do REST existe a chave "PrepareIn" que é responsável por estabelecer qual Empresa/Filial esta vinculada ao REST.

Caso a chave "PrepareIn" não esteja configurada devidamente, é possível que o Smart View tente localizar a tabela "**SX10**", por exemplo, ao invés de pesquisar por "**SX1010**" (Nome da tabela com o código da empresa).  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Realize o ajuste da chave "PrepareIn", conforme documentação **[REST com ERP Microsiga Protheus](https://tdn.totvs.com/x/4UoSCw)**

2. Verifique as demais configurações através da documentação: [**Configuração do SmartView**](https://tdn.totvs.com/x/8WTCMQ)

3. Caso o problema persista, entre em contato com o time de Suporte Framework da TOTVS.
