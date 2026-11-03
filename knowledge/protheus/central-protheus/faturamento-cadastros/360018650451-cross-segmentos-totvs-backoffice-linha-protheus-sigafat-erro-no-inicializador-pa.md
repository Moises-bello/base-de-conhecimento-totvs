---
article_id: 360018650451
category: Faturamento - Cadastros
content_hash: 083fe3478b102247120c4976223cce905e83d06a0d9022054b5cfd40086f3a31
fetched_at: '2026-06-28T22:38:35.519502+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Erro No Inicializador
  Padrão do Campo A1_VM_MARC
type: support-article
updated_at: '2021-11-17T19:02:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018650451-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Erro-No-Inicializador-Padr%C3%A3o-do-Campo-A1-VM-MARC
---

**Dúvida**

Ao excluir um cliente (**MATA030**) o sistema apresenta três mensagens de erro informando que:

1. INITTER - Erro no conteúdo do Inicializador Padrão: Campo. (Marcação)
2. INITTER - Erro no conteúdo do Inicializador Padrão: Campo: **A1\_VM\_MARC**
3. MA030TEMPV - Cliente não poderá ser excluído. Filial "x".

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da versão 11.

**Causa**

A mensagem que apresenta inconsistência no inicializador padrão do campo A1\_VM\_MARC ocorre por que o campo **A1\_COD\_MARC** possui a chamada do A1\_VM\_MARC e por que o campo A1\_COD\_MARC está posicionado posteriormente a A1\_WM\_MARC.  
  
**Solução**

É necessário que o campo A1\_COD\_MARC esteja na posição anterior ao A1\_VM\_MARC

Para configurar a ordem correta do campo, acesse:

1. No módulo configurador (SIGACFG);
2. Acesse base de dados, dicionário de dados;
3. Acesse a tabela SA1;
4. Valide a ordem dos campos: A1\_COD\_MARC e A1\_VM\_MARC deixando A1\_COD\_MARC a frente de A1\_VM\_MARC, exemplo, A1\_COD\_MARC = ordem 20 / A1\_VM\_MARC = ordem 21.
