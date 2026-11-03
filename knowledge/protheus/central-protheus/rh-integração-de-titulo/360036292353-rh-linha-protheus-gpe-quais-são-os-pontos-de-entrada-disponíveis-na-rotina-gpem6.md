---
article_id: 360036292353
category: RH - Integração de Titulo
content_hash: cd90cfc2c4bf54e468223980f5d5aeb018a08bbb0636d81b165f35f03d1c182e
fetched_at: '2026-06-28T22:43:36.433160+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Quais são os pontos de entrada disponíveis na rotina
  GPEM660
type: support-article
updated_at: '2025-07-14T21:08:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036292353-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEM660
---

**Dúvida**Quais são os pontos de entrada disponíveis na rotina GPEM660  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal  - Versão 12.1.17  
  
**Solução:**Abaixo, estão listados os pontos de entrada disponíveis na rotina GPEM660:  
  
**1) Ponto de entrada GP660LEG e GP660COR (**[Ponto de Entrada para alterar a legenda da rotina GPEM660](https://tdn.totvs.com/display/PROT/1971919+DRHPAG-11319+DT+Ponto+de+Entrada+para+alterar+a+legenda+da+rotina+GPEM660))

GP660LEG e GP660COR

**/\* ALTERA A DEFINICAO DA LEGENDA \*/**

USER *FUNCTION* GP660LEG()  
  
LOCAL aParam := PARAMIXB  
Local aRet := {}  
Aadd(aRet,{"RC1->RC1\_INTEGR<>'9'" , "BR\_VERMELHO", OemToAnsi("Teste de Legenda") })  
RETURN aRet

**/\* ALTERA A EXPLICACAO DAS CORES DA LEGENDA \*/**

USER *FUNCTION* GP660COR()

LOCAL aParam := PARAMIXB  
Local aRet := {}  
Aadd(aRet,{ "BR\_VERMELHO", OemToAnsi("Teste de Legenda") })

 RETURN aRet

**2) Ponto de Entrada GPM60VLD - (Validação de Inclusão/Alteração em Movimentação de Títulos):**

Criado ponto de entrada GPM60VLD para validar a inclusão ou alteração do título.  
Será executada a validação padrão e se o retorno for positivo então será chamada a validação customizada.

Nome : GPM60VLD

Parâmetros de Entrada :

aParam[1] - Tipo de chamada (1 = Inclusão;2=Alteração)

Retorno : Verdadeiro ou Falso

Fonte de Exemplo :

User function GPM60VLD()  
  
Local nTipo := ParamIXB[1]  
Local lRet := .T.  
/\*  
nTipo == 1 -> Inclusão  
nTipo == 2 -> Alteração  
\*/

Return lRet

**3) Ponto de Entrada GPM060EX  (Exclusão de Títulos)**[RH - Linha Protheus - GPE - Funcionalidade do ponto de Entrada: GPM060EX (Exclusão de Títulos)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22767086347287-RH-Linha-Protheus-GPE-Funcionalidade-do-ponto-de-Entrada-GPM060EX-Exclus%C3%A3o-de-T%C3%ADtulos)

**4) Ponto-de-Entrada: GP660ROT (Menu Cadastro de Movimentação de Títulos)**  
[RH - Linha Protheus - GPE - Funcionalidade do ponto de Entrada: GP660ROT (Menu Cadastro de Movimentação de Títulos)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13982837224471-RH-Linha-Protheus-GPE-Funcionalidade-do-ponto-de-Entrada-GP660ROT-Menu-Cadastro-de-Movimenta%C3%A7%C3%A3o-de-T%C3%ADtulos)  
  
**Saiba Mais**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
