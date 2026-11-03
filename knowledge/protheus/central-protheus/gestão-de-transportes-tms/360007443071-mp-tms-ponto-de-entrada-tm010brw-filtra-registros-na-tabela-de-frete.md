---
article_id: 360007443071
category: Gestão de Transportes (TMS)
content_hash: 5ff0c1018c09a1d4fa6646789210f00d93cf3953b51d5f6007b55aff2436ffa6
fetched_at: '2026-06-28T22:45:33.503766+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: MP - TMS - Ponto de entrada TM010BRW Filtra Registros na Tabela de Frete
type: support-article
updated_at: '2019-12-27T13:14:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007443071-MP-TMS-Ponto-de-entrada-TM010BRW-Filtra-Registros-na-Tabela-de-Frete
---

**Dúvida**Como implementar o ponto de entrada **TM010BRW** Filtra Registros na Tabela de Frete?

**Ambiente**  
Microsiga Protheus – Gestão de Transportes – A partir da versão 11.80  
  
  
**Solução**O ponto de entrada **TM010BRW** está localizado no fonte **TMSA010 Tabela** **de** **Frete** e permite ao usuário filtrar os registros que serão exibidos no *browser*, nas rotinas **Tabela de Frete** e **Tabela de Frete a Pagar**.

**Programa Fonte**: TMSA010.PRW  
  
**Sintaxe**: TM010BRW - Filtra Registros na Tabela de Frete ( ) --> cFiltro

**Retorno:**  
cFiltro  
         (caracter)  
         Condição de filtro que será utilizado no browse.

**Exemplos:**  
  
User Function TM010BRW()  
  
Local cFiltro := ''//Exemplo de Tabela de Frete a Receber  
  
If Left(FunName(1),7) == 'TMSA010'   
          If !TMSTbAtiva('GEN1','01',.F.,, '1',) //Função que valida se a tabela está ativa   
                   cFiltro := 'DT0\_TABFRE <> 'GEN1''   
          End if   
Endif //Exemplo de Tabela de Frete a Pagar  
  
If Left(FunName(1),7) == 'TMSA790'   
          If !TMSTbAtiva('PAG1','01',.F.,, '2',) //Função que valida se a tabela esta ativa   
                   cFiltro := 'DT0\_TABFRE <> 'PAG1''   
          End if   
End if   
  
Return cFiltro
