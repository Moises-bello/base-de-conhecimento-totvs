---
article_id: 360007451691
category: Gestão de Transportes (TMS)
content_hash: 0118f522c1833fc436d4629efa5bb59506f6ab35087eff71c105b12e85443ee0
fetched_at: '2026-06-28T22:45:29.657167+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM040COP Alteração de campos
  na cotação de frete
type: support-article
updated_at: '2022-01-18T17:58:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007451691-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM040COP-Altera%C3%A7%C3%A3o-de-campos-na-cota%C3%A7%C3%A3o-de-frete
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)*** Tempo aproximado para leitura: **00:00:48 min  
  
Dúvida**Como implementar o ponto de entrada **TM040COP** **Alteração de campos na cotação de frete**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM040COP** está localizado no **TMSA040** **Cotação de Frete** e permite ao usuário limpar os campos que desejar no momento em que é feita uma copia a partir de uma outra cotação de frete.  
  
**Programa Fonte**: TMSA040.PRW  
  
**Sintaxe**: TM040COP - Alteração de Campos na Cotação de Frete ( [ ] )  
  
**Parâmetros**:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Nome | Tipo | Descrição | Default | Obrigatório | Referência |
|  | Array of Record |  |  |  |  |

**Retorno**:  
              ()

**Exemplos**:  
#Include 'Protheus.ch'  
User Function TM040COP()//-- Campos a serem apagados na hora da cópia, antes da tela aparecer.  
M->DT4\_PRZVAL := CriaVar("DT4\_PRZVAL",.T.)  
M->DT4\_OBS := ""  
Return  
  
**Variáveis**:  

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Tipo | Escopo | Pode Alterar | Descrição |
|  | Array of Record | Global | Não |  |
