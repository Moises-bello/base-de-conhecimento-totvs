---
article_id: 38498924298519
category: SIGAACD - Automação e Coleta de Dados
content_hash: 1c45f83e6f9719d357de29c12cbd05b61f3bdd5b179ef014962d34a9a1f3bcdb
fetched_at: '2026-06-28T22:39:12.510542+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Código de tipo de
  Impressão Inválido, como corrigir?
type: support-article
updated_at: '2026-02-19T14:18:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38498924298519-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-C%C3%B3digo-de-tipo-de-Impress%C3%A3o-Inv%C3%A1lido-como-corrigir
---

Para solucionar o erro ao imprimir etiquetas na Pré-Nota de entrada no TOTVS Protheus, é necessário cadastrar o local de impressão usando código numérico (exemplo: 001) na rotina ACDA060, e configurar esse código nos parâmetros MV\_IACD01 até MV\_IACD04, em vez de utilizar nomes como "Zebra".

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38498924285079) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Ao gerar uma impressão de etiqueta, pela rotina da Pré-Nota de entrada apresenta uma mensagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38498920348695)   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
Na rotina Local de Impressão(ACDA060) é necessário criar os códigos de impressão com numeração exemplo 001, e não com o nome exemplo Zebra.

Depois de ajustado o nome do local de impressão, é necessário informar o código 001 por exemplo nos parâmetros [MV\_IACD01](https://centraldeatendimento.totvs.com/hc/pt-br/articles/235302467-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Par%C3%A2metros-SX6-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados) até [MV\_IACD04](https://centraldeatendimento.totvs.com/hc/pt-br/articles/235302467-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Par%C3%A2metros-SX6-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados).

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
