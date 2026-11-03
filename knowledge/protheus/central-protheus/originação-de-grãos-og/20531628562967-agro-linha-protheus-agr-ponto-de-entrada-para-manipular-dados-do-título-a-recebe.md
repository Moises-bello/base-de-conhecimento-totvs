---
article_id: 20531628562967
category: Originação de Grãos (OG)
content_hash: 430e69b97f0930c3cacfc67d2ae60c9afef9ce7792a3407bea2f3496767d0efa
fetched_at: '2026-06-28T22:45:43.010941+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de entrada para manipular dados do título
  a receber DCO PEPRO
type: support-article
updated_at: '2025-07-14T19:46:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20531628562967-Agro-Linha-Protheus-AGR-Ponto-de-entrada-para-manipular-dados-do-t%C3%ADtulo-a-receber-DCO-PEPRO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20531628507159) Tempo aproximado para leitura: **00:00:40 min****Ocorrência**  
No módulo **Comercialização (Linha Protheus) - Originação de Grãos (OG)**, ao realizar o processo para fazer o **ponto de entrada** para manipular os dados do título à receber é apresentada a ocorrência **Ponto de entrada para manipular dados do título a receber DCO PEPRO**.  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**  
Esse incidente ocorre, pois é necessário realizar o processo para fazer o **ponto de entrada** para manipular os dados no Sistema.  
  
**Solução**  
Para solucionar essa ocorrência, o **Ponto de Entrada** é o **OGX81SE1 - Permite manipular dados do Título a Receber**, ele é chamado ao gerar títulos a receber do **DCO PEPRO** - **Prêmio Equalizador Pago ao Produtor Rural** rotina **OGA810 - DCO PEPRO.****Exemplo:**

**Função de usuário OGX81SE1()**  
**Local aFina040 := aClone(PARAMIXB[1])**  
**Local cCodPro := PARAMIXB[2]**  
  
**aAdd( aFina040, {"E1\_SEUCAMPO" , '' , Nil } )**  
  
**Retorna aFina040**
