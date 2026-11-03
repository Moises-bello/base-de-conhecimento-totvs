---
article_id: 360044950994
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 24447b864e0a54dc76b04be95217ee85b543e64f9a62c284931da7a1f0088d0e
fetched_at: '2026-06-28T22:42:40.789137+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Alterar o número da ordem de produção
  sugerida pelo Sistema
type: support-article
updated_at: '2025-10-15T21:11:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044950994-Manufatura-Linha-Protheus-SIGAPCP-Alterar-o-n%C3%BAmero-da-ordem-de-produ%C3%A7%C3%A3o-sugerida-pelo-Sistema
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35662818434711)***Tempo aproximado para leitura:**00:01:05 min**  
**Dúvida**Como corrigir o número da ordem de produção sugerida pelo Sistema na tabela **SC2 - Ordem de Produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Eventualmente perde-se a sequência da numeração das **OPs - Ordens de Produções** cadastradas.  
Isso pode ocorrer quando uma **OP** é emitida por meio do pedido de venda, assumindo o número do pedido como número da **OP**, ou quando ocorre o cadastro manual de uma **OP** com um número superior à sequencia desejada.  
Nestes casos, para corrigir o número da**OP**, siga as instruções à seguir:

1. Acesse o **SIGACFG - Configurador** em **Cadastros/Ambientes/Controle de Numeração**;
2. Pesquise pelo *alias* **SC2** de acordo com o seu ambiente;
3. Altere a coluna **Número** acrescendo mais 1 ao último número de **OP** registrado.

**Importante**  
Se o controle de numeração é realizado via *license server*, toda vez que a máquina na qual o *license server* está instalado for reiniciada o controle da numeração será refeita, assumindo novamente o maior número armazenado em cada tabela, incluindo a **SC2**.
