---
article_id: 36438951656727
category: SIGAACD - Automação e Coleta de Dados
content_hash: e9cb51e4269cc0ba20a739812cf7b285a044d70d37b1d11e79803c9ca1a23d6d
fetched_at: '2026-06-28T22:39:12.838275+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - MSCBSPOOL - Geração
  dos arquivos.REL ao reimprimir etiqueta.
type: support-article
updated_at: '2025-11-19T12:54:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36438951656727-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-MSCBSPOOL-Gera%C3%A7%C3%A3o-dos-arquivos-REL-ao-reimprimir-etiqueta
---

Foi implementada uma correção para excluir automaticamente arquivos .REL gerados na impressão pela classe FWMsPrinter na pasta "IMPRESSO"; arquivos .rel antigos devem ser removidos manualmente.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36438936084759) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como corrigir é gerado arquivos com extensão .REL na pasta "IMPRESSO" que não são removidos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
Efetuado o tratamento para excluir o arquivo .REL que foi gerado na impressão e criados pela classe FWMsPrinter, arquivos .rel pre-existentes devem ser removidos manualmente.

Segue o pacote para correção, aplicar em base de homologação e realizar o Backup das informações.

**12.1.2210:**<https://r.totvs.io/p/1182732> ; **12.1.2310:**<https://r.totvs.io/p/1182734> ; **12.1.2410:**<https://r.totvs.io/p/1182733> ; **12.1.33:**<https://r.totvs.io/p/1182735> ;

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
