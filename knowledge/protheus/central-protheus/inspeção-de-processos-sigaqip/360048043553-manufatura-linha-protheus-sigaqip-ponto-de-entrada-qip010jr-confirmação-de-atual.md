---
article_id: 360048043553
category: Inspeção de Processos (SIGAQIP)
content_hash: ebd35f123488960a92795a3d623ef0779104360dd9f224cf6aefd899cdbe366d
fetched_at: '2026-06-28T22:42:25.908595+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Ponto de entrada QIP010JR confirmação
  de atualização
type: support-article
updated_at: '2021-08-10T15:00:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048043553-Manufatura-Linha-Protheus-SIGAQIP-Ponto-de-entrada-QIP010JR-confirma%C3%A7%C3%A3o-de-atualiza%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:45 min**  
**Dúvida**Qual o conceito do **PE - Ponto de Entrada QIP010JR - Confirmação de atualização**?  
  
**Ambiente**Totvs Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Solução**O **PE QIP010JR** é executado na confirmação da atualização da rotina **QIPA010 - Especificação de Produtos** do módulo **SIGAQIP - Inspeção de Processos**.  
  
**Eventos**  
Executado na validação da **QIPA010**, antes do início da gravação dos dados.  
  
**Programa Fonte: QIPA010  
  
Sintaxe**

```
QIP010JR - Confirmação de atualização ( ) --> lRet  
Retorno  
lRet(logico)
```

Indica se os dados do cadastro estão aptos para gravação.  
  
**Importante**Este **PE** também é executado na rotina **QIPA012 - Cadastros de Especificações de Produtos**.
