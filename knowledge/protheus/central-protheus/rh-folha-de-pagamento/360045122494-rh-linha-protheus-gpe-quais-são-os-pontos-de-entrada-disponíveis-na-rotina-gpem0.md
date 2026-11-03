---
article_id: 360045122494
category: RH - Folha de Pagamento
content_hash: d59865ee33b56e4412b3a936890388c299d93250faf82bc91d57f7645257a648
fetched_at: '2026-06-28T22:44:16.232693+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Quais são os pontos de entrada disponíveis na rotina
  GPEM020
type: support-article
updated_at: '2024-09-12T20:06:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045122494-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEM020
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26334669341847) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Quais são os pontos de entrada disponíveis na rotina GPEM020?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**Abaixo os pontos de entrada disponíveis na rotina GPEM020:

**1) Ponto de Entrada: GP690FIL**Ponto de Entrada GP690FIL - Alterar filtro do cálculo de dissídio

|  |  |
| --- | --- |
| **Descrição:** | Este ponto de entrada permite alterar dias de Aviso no cálculo da rescisão |
| **Localização:** | GPEM690 |
| **Eventos:** | GPEM690 |
| **Programa Fonte:** | GPEM690.PRX |
| **Função:** | GPEM690 |
| **Retorno:** | cFiltro - Filtro do cálculo |

Exemplo:

#Include '[Protheus.ch](http://protheus.ch/)'  
  
User Function GP690FIL()  
  
Local nTipo     := Paramixb[1]  
Local cFiltro    := Paramixb[2]  
  
//Filtro SRA (SQL)  
If nTipo == 1  
    cFiltro := cFiltro1  
//Filtro Cálculo (AdvPl)  
Else  
    cFiltro := cFiltro2  
EndIf  
  
Return cFiltro

/\*

No exemplo, é feito verificação da chamada do ponto de entrada: 1 - Filtro em SQL para a tabela SRA e 2 - Filtro em AdvPl para o cálculo.

\*/

**2) Ponto-de-Entrada: VERLOGFL - Log de Cálculo Personalizado**

|  |  |
| --- | --- |
| Versões: | A partir da versão Microsiga Protheus 12.1.17 |
| Compatível Países: | Todos |
| Sistemas Operacionais: | Todos |
| Compatível às Bases de Dados: | Todos |
| Idiomas: |  |

**Descrição:**

Este ponto de entrada está localizado no final do processamento dos funcionários e serve para mostrar um log de cálculo personalizado.  
  
Para executar a gravação do log, deverá criar uma fórmula que executará a função personalizada que grava o log de cálculo a cada funcionário.  
  
Esta fórmula deverá ser posicionada após o último roteiro de cálculo de folha de pagamento.

Programa Fonte

```
GPEM020.PRX
```

Sintaxe

VERLOGFL - Log de Cálculo Personalizado ( ) --> Nil

Retorno

**Nil**

(nulo)* Nil

**3)** **Ponto de Entrada: GPM020ROT - Flexibilizar cálculo de roteiros para intermitentes**

Ajuste no cálculo de roteiros para permitir a definição de quais roteiros NÃO deverão ser calculados para funcionários de contrato intermitente, através do ponto de entrada GPM020ROT.

No exemplo abaixo, é definido que os roteiros PLA, VRF, VAL, BEN,131, 132, ADI, PLR **NÃO** serão calculados para funcionário de contrato intermitente. Conforme exemplo, tal definição é efetuado na variável de tipo caracter *cRotInter* e seu conteúdo é retornado no próprio ponto de entrada.

```
#INCLUDE "PROTHEUS.CH"

User Function GPM020ROT()

Local cRotInter  := PARAMIXB[1]

// Roteiros que NÃO serão calculados para funcionários com contrato intermitente
// PLA, VRF, VAL, BEN,131, 132, ADI, PLR
cRotInter := ( fGetCalcRot('C') + "*" + fGetCalcRot('D') + "*" + fGetCalcRot('E')  + "*" + fGetCalcRot('I') + "*" + fGetCalcRot('5') + "*" + fGetCalcRot('6') + "*" + fGetCalcRot('2') + "*" + fGetCalcRot('F') )

Return cRotInter
```

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
