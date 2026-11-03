---
article_id: 35712744309911
category: Gestão de Armazenagem (WMS)
content_hash: dbd3e837d6ee1955f2a291dd309dd243aa8390fa8de030f538572c1f8b8b37c6
fetched_at: '2026-06-28T22:45:48.058304+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Logística - Linha Protheus - WMS - Mecanismo de geração da numeração sequencial
  a partir da release 12.1.2410
type: support-article
updated_at: '2025-10-27T12:43:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35712744309911-Log%C3%ADstica-Linha-Protheus-WMS-Mecanismo-de-gera%C3%A7%C3%A3o-da-numera%C3%A7%C3%A3o-sequencial-a-partir-da-release-12-1-2410
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35712760055319) Tempo aproximado para leitura: **00:02:33 min**  
  
**Dúvida**  
Como funciona o mecanismo de geração da numeração sequencial a partir da ***release*** **12.1.2410**?  
  
**Ambiente**  
TOTVS Logística - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (WMS) - Versão 12  
  
**Solução**  
A partir da *release* **12.1.2410**, o mecanismo de geração da numeração sequencial das movimentações de **Nota Fiscal de Entrada**, **Nota Fiscal de Saída** e **Movimentações Internas** deixou de ser controlada através do parâmetro **MV\_DOCSEQ - Ultimo numero sequencial utilizado para movimentos do SIGA ADVANCED.** Este valor não deve ser alterado pelos usuários e passou a ser controlada através do ***License Server**.*  
  
Buscando uma melhora do produto e desempenho foi alterado o comportamento da gravação do **NUMSEQ**, onde o Sistema deixou de utilizar o parâmetro **MV\_DOCSEQ** para utilizar a função **NEWPROXNUM,** que faz uso do ***License Server*** para gerar a próxima numeração.  
  
Com isso, torna-se ainda mais importante a correta configuração da chave **SpecialKey** em cada ambiente utilizado pela empresa, pois essa chave define uma ***string*** que é concatenada à ***string*** básica no controle de numeração.  
  
Caso ela não seja configurada corretamente, ambientes diferentes compartilharão a mesma numeração, que será obtida com base no primeiro ambiente acessado, o que pode causar duplicidade indevida no controle de sequenciais.  
  
**Saiba mais**  
Para mais detalhes, consultar a documentação: [2024 - 31/10 Parâmetro MV\_DOCSEQ](https://tdn.totvs.com/pages/releaseview.action?pageId=840763998#samples1--1022532727)
