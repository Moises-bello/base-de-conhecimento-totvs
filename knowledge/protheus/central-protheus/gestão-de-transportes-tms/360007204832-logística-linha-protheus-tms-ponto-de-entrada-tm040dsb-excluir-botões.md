---
article_id: 360007204832
category: Gestão de Transportes (TMS)
content_hash: 007df90d6819abfba3b498782c905ce8ef03d98709f4730e461a16f299dc4a99
fetched_at: '2026-06-28T22:45:29.663730+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM040DSB Excluir botões
type: support-article
updated_at: '2022-01-18T18:06:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007204832-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM040DSB-Excluir-bot%C3%B5es
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)*** Tempo aproximado para leitura: **00:01:12 min  
Dúvida**Como implementar o ponto de entrada **TM040DSB** **Excluir botões**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM040DSB** está localizado no **TMSA040** **Cotação de Frete** e permite ao usuário excluir botões na ***EnchoiceBar***, na rotina de **Cotação de Frete**.  
  
**Programa Fonte**: TMSA040.PRW  
  
**Sintaxe**: TM040DSB - Excluir Botões ( < aBotao> , < nOpcao> ) --> aBotao  
  
**Parâmetros**:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Nome | Tipo | Descrição | Default | Obrigatório | Referência |
| aBotao | Array of Record |  |  | X |  |
| nOpcao | Array of Record | nOpcao - opção do aRotina |  | X |  |

**Retorno**:   
aBotao  
           (vetor)  
           aBotao - Array com os botões que serão exibidos na *Enchoice* da Rotina.  
  
**Exemplos**:  
No exemplo a seguir vamos excluir o **botão 2 Atualiza a Composição do Frete**, quando for inclusão de cotação de frete.  
  
**Exemplo do Ponto de Entrada**  
User Function TM040DSB()  
Local aBotao := PARAMIXB[1] //Array com os botões  
Local nOpcao := PARAMIXB[2] //opção da rotina  
If nOpcao == 3 //Inclusao  
        aDel(aBotao, 2) //--Opção a ser excluída da rotina aSize(aBotao,Len(aBotao)-1) //Redimensiona o array  
End If  
Return aBotao  
  
**Variáveis**:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Tipo | Escopo | Pode Alterar | Descrição |
|  | Array of Record | Global | Não |  |
