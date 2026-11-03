---
article_id: 22767086347287
category: RH - Integração de Titulo
content_hash: 3594860991596c892fd6a2963013958c6154dd6925fefe0623b3d14a3069b181
fetched_at: '2026-06-28T22:43:36.351140+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: 'RH - Linha Protheus - GPE - Funcionalidade do ponto de Entrada: GPM060EX 
  (Exclusão de Títulos)'
type: support-article
updated_at: '2025-07-14T21:08:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22767086347287-RH-Linha-Protheus-GPE-Funcionalidade-do-ponto-de-Entrada-GPM060EX-Exclus%C3%A3o-de-T%C3%ADtulos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22767112294551) Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**  
RH - Linha Protheus - GPE - Funcionalidade do ponto de Entrada: GPM060EX  (Exclusão de Títulos)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Versão 12.1.17

**Solução:**

Exemplo:

#Include '[Protheus.ch](http://protheus.ch/)'  
  
/\*  
O ponto de entrada GPM060EX substitui a validação padrão de exclusão de títulos  
No padrão, caso o título não esteja liberado ou esteja inconsistente, o título é excluído normalmente.  
Se o título já foi integrado e já foi baixado ou esteja em borderô, a exclusão não será permitida.  
\*/  
**User Function GPM060EX()**  
  
Local cFolMes     := SuperGetMV("MV\_FOLMES", .F., "")  
Local lRet     := .F.  
  
If RC1->RC1\_COMPET >= SubStr( cFolMes, 5, 2 ) + SubStr( cFolMes, 1, 4 )  
    lRet := .T.  
EndIf  
  
/\*  
No exemplo acima, é verificado se o titulo é referente a competência igual ou  
superior ao da folha em aberto.  
Caso seja, a exclusão do título é permitida, caso contrário, a exclusão não será efetuada.  
\*/  
  
Return lRet  
 **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22767112296983)**

Abaixo apresentação do ponto de entrada sendo executado:   
![gpm060EX.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/22767764148887)

Saiba Mais:  
[RH - Linha Protheus - GPE - Quais são os pontos de entrada disponíveis na rotina GPEM660](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036292353-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEM660)
