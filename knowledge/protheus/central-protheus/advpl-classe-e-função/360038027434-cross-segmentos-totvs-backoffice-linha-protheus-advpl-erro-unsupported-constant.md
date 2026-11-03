---
article_id: 360038027434
category: ADVPL - Classe e Função
content_hash: d634b9301febdd284406f2e444ba18b4dc55647db63b61c7848ad0f499c023f2
fetched_at: '2026-06-28T22:40:19.194739+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Erro unsupported
  constant assign on line ao compilar
type: support-article
updated_at: '2022-01-10T14:17:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038027434-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-unsupported-constant-assign-on-line-ao-compilar
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao utilizar a instrução  " variavel1+= ";" += \_variavel2 += "; "  
gera o erro na compilação **"***unsupported constant assign on line*"  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.25  
  
**Causa**O server passou a não permitir operações e operadores que atualizem conteúdos de expressões constantes.  
  
**Solução**Não é possível mais operadores que atualizem conteúdos de expressões constantes , sendo assim a compilação será finalizada com a mensagem "\*\**unsupported constant assign on line* \*\*"

\*\*Disponível em builds superiores a 7.00.131227A, ou seja build do Lobo-Guará.  
  
**Saiba mais**[Correção - Proteção de Operação com Constantes na Compilação AdvPL](https://tdn.totvs.com/pages/viewpage.action?pageId=235579499)
