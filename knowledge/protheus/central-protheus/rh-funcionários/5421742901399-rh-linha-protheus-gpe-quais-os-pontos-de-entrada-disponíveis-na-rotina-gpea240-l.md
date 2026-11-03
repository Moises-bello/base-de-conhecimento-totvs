---
article_id: 5421742901399
category: RH - Funcionários
content_hash: fd0f7c7ed3b4a2aeaad44af62f5f0fe88ed02a64108c5d79d335516435ed1061
fetched_at: '2026-06-28T22:43:28.671547+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Quais os pontos de entrada disponíveis na rotina
  GPEA240-Lançamentos de Ausências
type: support-article
updated_at: '2025-08-18T19:38:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5421742901399-RH-Linha-Protheus-GPE-Quais-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEA240-Lan%C3%A7amentos-de-Aus%C3%AAncias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31668934146967) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Quais os pontos de entrada disponíveis na rotina GPEA240-Lançamento de Ausências?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17.

**Solução**Os pontos de Entrada do fonte GPEA240 foram **descontinuados** a partir da versão 12 com a migração da rotina do Lançamentos de Ausências para tecnologia MVC.   
Em substituição a eles, é possível a utilização de funções nativas do **MVC,** conforme o exemplo abaixo:

User Function GPEA240()

Local aParam := PARAMIXB

Local cIdPonto := ""

Local cIdModel := ""

Local lRet := .T.

Local aArea := GetArea()

If aParam <> NIL

cIdPonto := aParam[2]

cIdModel := aParam[3]

If cIdPonto == 'MODELCOMMITNTTS'

ApMsgInfo('Chamada apos a gravação total do modelo e fora da transação (MODELCOMMITNTTS).' + CRLF + 'ID ' + cIdModel)

//Inclusão do tratamento customizado

EndIf

EndIf

RestArea(aArea)

Return lRet

Para mais informações, acesse a documentação completa em: <https://tdn.totvs.com/pages/releaseview.action?pageId=6815175>

**Saiba mais:**

[RH - Linha Protheus - GPE - Pontos de Entrada disponíveis no cálculo de Benefícios - GPEXCBEN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403158529175-RH-Linha-Protheus-GPE-Pontos-de-Entrada-dispon%C3%ADveis-no-c%C3%A1lculo-de-Benef%C3%ADcios-GPEXCBEN)

[RH - Linha Protheus - GPE - Quais são os pontos de entrada disponíveis na rotina GPEM660](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036292353-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEM660)

[RH - Linha Protheus - GPE - Quais são os pontos de entrada disponíveis na rotina GPEM020](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045122494-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEM020)

[RH - Linha Protheus - GPE - Quais os Pontos de Entrada disponíveis na rotina GPEA180 - Transferências](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036096713-RH-Linha-Protheus-GPE-Quais-os-Pontos-de-Entrada-dispon%C3%ADveis-na-rotina-GPEA180-Transfer%C3%AAncias)

[RH - Linha Protheus - GPE - Quais são os pontos de entrada disponíveis na rotina GPEM080](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045165513-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEM080)
