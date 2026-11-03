---
article_id: 360042299993
category: TAF - eSocial - Atualização
content_hash: dde624324780895377c8e85cb9a59807fe9dc25756e42900aaafec3b85f1b530
fetched_at: '2026-06-28T22:45:13.401538+00:00'
product: protheus
section_id: 1500001547902
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Atualizações - O caminho especificado,
  o nome do arquivo ou ambos são muito longos.
type: support-article
updated_at: '2024-09-24T18:01:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042299993-RH-Linha-Protheus-TAF-eSocial-Atualiza%C3%A7%C3%B5es-O-caminho-especificado-o-nome-do-arquivo-ou-ambos-s%C3%A3o-muito-longos
---

**Ocorrência**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055871354)

Ao atualizar o TAF e TSS, é apresentado um erro: "**O caminho especificado, o nome do arquivo ou ambos são muito longos"**, onde o processo de atualização é abortado.

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Rotinas Comuns - Todas as versões.

**Causa**

O erro acontece pois existe dentro da sua raiz do TAF uma pasta com um caminho grande, e quando o sistema faz o backup ele cria mais um diretório de backup o caminho ultrapassa 248 caracteres que é o limite do Windows.

Vide imagem abaixo do Sistema Operacional Windows:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055871654)

**Solução**

1 - Verificar se dentro da sua estrutura TAF se existem subpastas que foram criadas manualmente, se existir, remova estas diretórios excluindo ou movendo para um diretório diferente da estrutura do TAF.
