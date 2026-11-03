---
article_id: 36424624332439
category: Inspeção de Processos (SIGAQIP)
content_hash: 2160dc94e72f4076bf555540ae04181b001dd5230113cbca37beae3e5faff48c
fetched_at: '2026-06-28T22:42:25.887746+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Ordem suspensa
type: support-article
updated_at: '2025-11-18T20:03:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36424624332439-Manufatura-Linha-Protheus-SIGAQIP-Ordem-suspensa
---

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36424630790167) Tempo aproximado para leitura: 00:00:55 min  
  
**Dúvida**  
No QIPA215 - Resultados é exibida uma mensagem **A ordem de produção selecionada não pode ser encerrada, porque não possui apontamentos de produção. Deseja que a ordem de produção seja suspensa?**. Como proceder?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Solução**  
Esta mensagem está relacionada ao parâmetro **MV\_QPINDIS - Informa o laudo que estará indisponibilizando a Ordem de Produção**. Este parâmetro aceita as opções:   
• E - Encerramento: Isto é, caso ainda estiver em aberto, a **OP - Ordem de Produção** será encerrada automaticamente, desde que exista apontamentos parciais.   
• S - Suspensa: A produção será suspensa temporariamente, até que seja reativada manualmente na rotina **MATA650 - Ordem de Produção**.   
  
Porém, independente de encerrar ou suspender a OP, não irá afetar na inspeção realizada.   
A ação é realizada apenas para a ordem de produção e não para a inspeção.   
  
**Importante**  
Para reativar a OP é necessário consultar a OP no **MATA650**, clicar em **Alterar** e alterar o campo **Situação** de **U-Suspensa**, para **N-Normal**.
