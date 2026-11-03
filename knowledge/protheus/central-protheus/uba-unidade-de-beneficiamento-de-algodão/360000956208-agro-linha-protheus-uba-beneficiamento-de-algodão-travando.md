---
article_id: 360000956208
category: UBA - Unidade de Beneficiamento de Algodão
content_hash: e22e0e606f3ee1382a56219cca0163d5895da8f6aae918489f8eba31b47e141f
fetched_at: '2026-06-28T22:45:35.582950+00:00'
product: protheus
section_id: 360005717853
source: central-protheus
title: Agro - Linha Protheus - UBA - Beneficiamento de algodão travando
type: support-article
updated_at: '2025-06-18T14:02:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000956208-Agro-Linha-Protheus-UBA-Beneficiamento-de-algod%C3%A3o-travando
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21969241541015)** Tempo aproximado para leitura: **00:00:35 min  
  
Ocorrência**No módulo **Comercialização (Linha Protheus) - UBA - Unidade de Beneficiamento de Algodão**, ao realizar a rotina **AGRA615 -****Beneficiamento** e inserir a pesagem do fardo beneficiado, o Sistema trava e nenhum outro processo pode ser realizado.  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - UBA - Unidade de Beneficiamento de Algodão - A partir da versão 12.1.17  
  
**Causa**Esse incidente ocorre porque a opção para imprimir etiqueta está ativa, e quando existe algum problema com a impressora configurada, ocorre o travamento do processo.   
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

**1.** Acesse a rotina **AGRA615**;

**2.** Clique em **F12**;

**3.** Altere o parâmetro **Imprime Etiqueta?** para **Não**, até que a impressora configurada seja ajustada.
