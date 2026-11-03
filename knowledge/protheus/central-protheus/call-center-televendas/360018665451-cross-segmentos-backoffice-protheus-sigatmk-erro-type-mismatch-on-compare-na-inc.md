---
article_id: 360018665451
category: Call Center - Televendas
content_hash: 22bb06d0594e7c64a80faba72f9015cac971a2a9722d699905c2e8e5647bb3c6
fetched_at: '2026-06-28T22:41:30.247804+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Erro "type mismatch on compare"
  na inclusão de produto no Televendas (TMKA273)
type: support-article
updated_at: '2026-06-16T14:09:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018665451-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Erro-type-mismatch-on-compare-na-inclus%C3%A3o-de-produto-no-Televendas-TMKA273
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41263235653143)** **Tempo aproximado para leitura:****00:02:00 min**

**Dúvida:**

Como corrigir o error.log "type mismatch on compare" ao incluir um produto na rotina Televendas?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGATMK - Todas as versões

**Causa**

Esse comportamento ocorre devido a um conflito no comparativo de tipos de dados do sistema: quando o parâmetro é preenchido com aspas internas (ex: `'502'`), o sistema interpreta o conteúdo como **Caractere** (texto); se estiver sem as aspas (ex: `502`), o sistema o interpreta como **Numérico**, gerando a inconsistência "type mismatch on compare  on TKP000A(TMKA273.PRW)".

Para resolver o problema, realize o ajuste no parâmetro seguindo os passos abaixo:

1. Acesse o módulo **Configurador** (SIGACFG);
2. Vá em **Ambiente** > **Cadastros** > **Parâmetros**;
3. Pesquise pelo parâmetro **MV\_BONUSTS**;
4. Altere o conteúdo informando o código da TES **obrigatoriamente entre aspas simples** (Exemplo: `'502'`);
5. Clique em **Salvar** para confirmar a alteração.

Após ajustar o parâmetro, refaça a inclusão do produto e o processo será concluído sem erros.
