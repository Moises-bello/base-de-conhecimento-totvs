---
article_id: 360007377671
category: Gestão de Transportes (TMS)
content_hash: 6636c6badd0743f81db19120da109115becc62ca8431731a4ada042cf70d6f65
fetched_at: '2026-06-28T22:45:29.560398+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada MA410SML  Confirmação da
  simulação de frete
type: support-article
updated_at: '2024-09-18T12:47:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007377671-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-MA410SML-Confirma%C3%A7%C3%A3o-da-simula%C3%A7%C3%A3o-de-frete
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21684644277911)  Tempo aproximado para leitura: 00:00:30 min  
  
Dúvida**Como implementar o ponto de entrada **MA410SML** - Confirmação da simulação de frete?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **MA410SML** está localizado no **MATA410** Pedido de Venda, e será executado na confirmação da tela de simulação.

A primeira posição do **paramIXB** contém um array com as informações de retorno da simulação.  
  
O *array* contém as informações abaixo:

Identificação da opção selecionada pelo usuário - Conteúdo igual a 1.  
Código da Transportadora  
Nome da Transportadora  
Valor do Frete  
Prazo de Entrega  
Número do Cálculo  
Classificação do Frete  
Tipo de Operação  
Trecho  
Tabela  
Número da Negociação  
Rota  
Data da Validade  
Faixa  
Tipo do Veículo

**Programa Fonte**: **MATA410.prw**  
  
**Parâmetros**: paramIXB   
  
**Exemplos**:  
User Function MA410SML()

Local nI:=0

For nI:=1 To Len(ParamIXB[1])   
If ParamIXB[1][nI][1] == "1"  
M->C5\_FRETE :=ParamIXB[1][nI][4]  
EndIf  
Next nI

Return
