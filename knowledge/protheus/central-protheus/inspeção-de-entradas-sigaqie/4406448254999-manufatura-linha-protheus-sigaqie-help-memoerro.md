---
article_id: 4406448254999
category: Inspeção de Entradas (SIGAQIE)
content_hash: 202ed8ea2e2721cc7a215a804d12f748ca6d6df64ead0055fef4b9acdc091deb
fetched_at: '2026-06-28T22:42:27.009095+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Help MEMOERRO
type: support-article
updated_at: '2021-08-18T10:56:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406448254999-Manufatura-Linha-Protheus-SIGAQIE-Help-MEMOERRO
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:40 min****Ocorrência**No módulo **SIGAQIE - Inspeção de Entradas**, ao tentar utilizar a rotina **QIEA215 - Resultados** ocorre o *Help* **MEMOERRO - Criação ou Leitura de arquivo inválido**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Causa**O *Help* **MEMOERRO** ocorre quando não existe o parâmetro **MV\_DIRCQ - Diretório destino onde serão armazenados os certificados de qualidade dos produtos que passaram no CQ, pelo processo Skip-lote** ou quando este parâmetro não possui conteúdo, ou ainda, se o diretório informado no seu conteúdo não existe dentro da pasta **Protheus\_data/System**. A mensagem também pode ocorrer se o usuário não tiver permissão de gravação no diretório informado.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique a existência do parâmetro **MV\_DIRCQ no SIGACFG - Configurador**;   
2. Confirme se o conteúdo do parâmetro não está vazio e, caso esteja preenchido, valide se o diretório informado existe dentro do diretório **Protheus\_data/System;**  
3. Valide se o usuário tem acesso ao diretório informado no conteúdo do parâmetro.
