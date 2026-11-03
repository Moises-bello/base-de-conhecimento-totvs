---
article_id: 360025385391
category: Gestão de Transportes (TMS)
content_hash: 1d0161b9d4ff3a7a98bc291b20033db5e62ead700cb1e72c2f21aadf0af72e24
fetched_at: '2026-06-28T22:45:32.389445+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TME73BUT Inclusão de botões
  no painel da rotina MDF-e
type: support-article
updated_at: '2023-03-01T19:42:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025385391-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TME73BUT-Inclus%C3%A3o-de-bot%C3%B5es-no-painel-da-rotina-MDF-e
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura:**00:00:36 min****Dúvida**Como implementar o ponto de entrada **TME73BUT** - **Inclusão de botões** no painel da rotina **MDF-e**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Este ponto de entrada está localizado no monitor da rotina **MDF-e - Manifesto Eletrônico de Documentos Fiscais**, permitindo adicionar botões no painel da rotina.  
 **Programa Fonte**: TMSAE73.PRW  
  
**Parâmetros**: Nenhum  
  
**Retorno**:  
aBtnUser(vetor) - Array com os novos botões a serem adicionados.   
  
**Exemplos**:  
User Function TME73But()   
aBtnUser := { 'Teste', {
