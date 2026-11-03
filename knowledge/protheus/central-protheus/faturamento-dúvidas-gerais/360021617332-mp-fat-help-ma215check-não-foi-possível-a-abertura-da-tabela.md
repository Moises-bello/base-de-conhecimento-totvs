---
article_id: 360021617332
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 09b21bd8133a77c1cbf38c36e81326412d28fc109e1b79334dd709389d746328
fetched_at: '2026-06-28T22:38:31.083453+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP - FAT - Help MA215CHECK: Não foi possível a abertura da tabela '
type: support-article
updated_at: '2021-04-28T15:55:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021617332-MP-FAT-Help-MA215CHECK-N%C3%A3o-foi-poss%C3%ADvel-a-abertura-da-tabela
---

**Ocorrência**Ao acessar o modulo Faturamento apresenta o Help: **MA215CHECK**: Não foi possível a abertura da tabela **SA1**, como proceder?  
   
 **Ambiente**Microsiga Protheus – Faturamento – A partir da versão 11.80  
   
 **Causa**O help ocorre pois as tabelas são exclusivas e esta rodando o Refaz Acumulado em alguma maquina.  
   
 **Solução**O sistema somente valida se as tabelas estão exclusivas se a rotina Refaz Acumulados **MATA215** estiver em execução.

Para solucionar, aguarde o termino do Refaz Acumulados e tente novamente o acesso.
