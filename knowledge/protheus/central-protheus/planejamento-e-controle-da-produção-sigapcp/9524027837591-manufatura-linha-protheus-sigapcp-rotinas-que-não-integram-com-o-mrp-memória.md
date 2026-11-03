---
article_id: 9524027837591
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: b443d21d7b4ec0591d10536c955e7526965f737ef2ee637e401b924b4407a1e8
fetched_at: '2026-06-28T22:42:45.912071+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Rotinas que não integram com o MRP
  Memória
type: support-article
updated_at: '2022-10-13T14:05:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9524027837591-Manufatura-Linha-Protheus-SIGAPCP-Rotinas-que-n%C3%A3o-integram-com-o-MRP-Mem%C3%B3ria
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:00:40 min  
  
Dúvida**Quais rotinas não integram automaticamente com o **PCPA712 - MRP Memória**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**As rotinas **MATA200 - Estrutura** e **MATA018 - Indicador de Produto** não integram automaticamente os dados com o **MRP Memória**. Para que a **integração** aconteça de maneira automática, é necessário utilizar os programas substitutos **PCPA200 - Estrutura (nova Versão)** e **MATA019- Indicador Produto (Mod 2).**  
  
Caso as rotinas **MATA200** e **MATA018** continuem sendo utilizadas, é necessário, obrigatoriamente, executar a rotina **PCPA140 - Sincronização** antes de rodar o **MRP Memória**.
