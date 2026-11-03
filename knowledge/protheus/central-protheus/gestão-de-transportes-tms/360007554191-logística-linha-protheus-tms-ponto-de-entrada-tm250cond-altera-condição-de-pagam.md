---
article_id: 360007554191
category: Gestão de Transportes (TMS)
content_hash: e36c8b7dc42c9527225ff8af2be9ab8d2d19b891ce3a30607056015948158d58
fetched_at: '2026-06-28T22:45:32.208939+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM250COND Altera Condição
  de Pagamento
type: support-article
updated_at: '2022-11-29T20:05:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007554191-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM250COND-Altera-Condi%C3%A7%C3%A3o-de-Pagamento
---

**Dúvida**Como implementar o ponto de entrada **TM250COND** - Altera Condição de Pagamento?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM250COND** está localizado no fonte **TMSA250** (**Contrato** **de** **Carreteiro**) e tem como objetivo alterar a condição de pagamento informada no cadastro do proprietário do veiculo.  
  
**Programa** **Fonte**: TMSA250.PRW  
  
**Sintaxe**: TM250COND - Altera Condição de Pagamento ( ) --> cCond  
  
**Retorno**:  
  
**cCond**

(caracter)* Condição de Pagamento a ser considerada na geração do titulo a pagar.

**Exemplos**:  
  
User function TM250COND()

Local cCond := ' '

Return( cCond )
