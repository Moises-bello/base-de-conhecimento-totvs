---
article_id: 38641672669463
category: SIGAACD - Automação e Coleta de Dados
content_hash: a63a35a2176d5079a467268ea719db2f0e4073f68a0ac6003cbbcbc41fb20875
fetched_at: '2026-06-28T22:39:12.726528+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Existem outros operadores
  em andamento nesta operação, a quantidade informada finaliza o saldo da operação
type: support-article
updated_at: '2026-02-25T21:24:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38641672669463-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Existem-outros-operadores-em-andamento-nesta-opera%C3%A7%C3%A3o-a-quantidade-informada-finaliza-o-saldo-da-opera%C3%A7%C3%A3o
---

O artigo explica que a mensagem "Existem outros operadores em andamento nesta operação, a quantidade informada finaliza o saldo da operação" ocorre quando diferentes operadores registram a mesma quantidade na mesma OP. A solução é desconectar o operador duplicado pela rotina Monitor RF no Protheus.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38641688660503) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como corrigir a mensagem "Existem outros operadores em andamento nesta operação, a quantidade informada finaliza o saldo da operação" que apresenta no apontamento de produção modelo II (ACDV025)?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.

**Causa**  
Em qual momento ocorre essa mensagem:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38641672661783)

Essa mensagem ocorre, quando você usa operadores diferentes, logado na mesma OP informando a mesma quantidade para apontamento da produção que deseja apontar.

**Exemplo**:

**Operador**: 001

**Operação**: 01

**Transação**: 02 (Produção)

Com esses mesmos dados, acesso o emulador com outro operador (exemplo 002).

**Recurso**: 001

**Quantidade** : 4,00

A mensagem será apresentada.

**Solução**

Como solução para esse cenário, é possível acessar a rotina Monitor RF(**CBMONRF**) no Protheus e monitorar os usuários logados na rotina de apontamento de produção modelo II (ACDV025), verificar qual operador está logado usando a mesma OP e a mesma quantidade.

Através do Monitor RF(**CBMONRF**) é possível desconectar um dos operadores, para dar andamento na finalização dessa OP, ou mesmo identificar a causa da mensagem.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
