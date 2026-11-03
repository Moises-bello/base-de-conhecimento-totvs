---
article_id: 360035476254
category: Manutenção de Ativos (SIGAMNT)
content_hash: 0f236e932bd756fc6350efa61da74a9571cf4a240fc152663fd3f506598e3f91
fetched_at: '2026-06-28T22:42:32.746036+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: 'Manufatura - Linha Protheus - MNT - Apontamento Insumos Terceiros '
type: support-article
updated_at: '2024-06-13T12:26:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035476254-Manufatura-Linha-Protheus-MNT-Apontamento-Insumos-Terceiros
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Como apontar **Insumos Terceiros** na **OS - Ordem de Serviço**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Versão 12  
  
**Solução**O parâmetro **MV\_NGMNTES - Integração Manutenção (MNT) com Estoque (ES)** com o conteúdo igual a **S - Sim** indica que o **Manutenção de Ativos -** **SIGAMNT** está integrado com o **Estoque**, neste caso para apontar o insumo do tipo **Terceiros** é necessário:

* incluir um **Documento de Entrada - MATA103**;
* informe no campo **Produto - D1\_COD** o código informado no parâmetro **MV\_PRODTER - Item de estoque que indica Terceiros no SIGAMNT**;
* informe no campo **Ordem Servic - D1\_ORDEM** uma **OS** incluída no módulo de **Manutenção de Ativos**;
* depois de terminar a inclusão do documento, consulte no **Retorno Mod. 2 - MNTA435**, e o insumo já será considerado como **Insumo Realizado**.

O Parâmetro **MV\_NGMNTES** com o conteúdo igual a **N - Não** indica que o **SIGAMNT** não está integrado com o **Estoque**, desta forma a inclusão é realizada na própria rotina **MNTA435**, na *grid* de **Insumos Realizados**.
