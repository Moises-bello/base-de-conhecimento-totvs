---
article_id: 360060839673
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 49f3aae84830ab4c2685278de67f8d95c6c8008ea1761693370ffdbb9824b76c
fetched_at: '2026-06-28T22:42:05.283619+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Ponto de Entrada EFDCON04 Ajuste de Crédito Pis/Cofins Apuração EFD Contribuições
type: support-article
updated_at: '2023-01-04T17:39:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060839673-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Ponto-de-Entrada-EFDCON04-Ajuste-de-Cr%C3%A9dito-Pis-Cofins-Apura%C3%A7%C3%A3o-EFD-Contribui%C3%A7%C3%B5es
---

**Dúvida**  
EFDCON04 Ajuste de Crédito Pis/Cofins Apuração EFD Contribuições  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 12  
  
**Solução**

Inclusão do ponto de entrada **EFDCON04**, no fonte **FISX001.prw**, para possibilitar a manipulação da **descrição do ajuste**, da **informação complementar**, do **numero do processo** e da **conta contábil** que tratam do detalhamento de ajuste do valor ou ajuste da base de calculo do **Crédito** de **PIS/COFINS** apurado.

Este ponto age antes da gravação das tabelas **CLA**, **CL4** e **F2Z**.

**Especificação**  
Parâmetros do ponto de entrada:  
PARAMIXB[1] Carácter   
Chave EFD

PARAMIXB[2] Carácter Tipo de Ajuste  
PARAMIXB[3] Carácter Descrição do ajuste  
PARAMIXB[4] Carácter Código Conta Contábil  
PARAMIXB[5] Carácter CST  
PARAMIXB[6] Número Alíquota  
PARAMIXB[7] Número Valor do Ajuste  
PARAMIXB[8] Carácter Período Atual  
PARAMIXB[9] Data Data Referência  
PARAMIXB[10] Lógico Ajuste de Base de calculo ou de valor do tributo. Se .T. ajuste de base. Se .F. Ajuste de valor.  
PARAMIXB[11] Carácter Tributo que está sendo ajustado. PIS = "1"; COFINS = "2"  
PARAMIXB[12] Carácter Número do documento ou Processo  
PARAMIXB[13] Carácter Informação complementar

**Retorno:**  
O ponto de entrada retorna um array de 4 posições:

**Nome**      **Tipo**          **Descrição**  
aRet[1]     Carácter     Descrição do ajuste  
aRet[2]     Carácter     Informação complementar do ajuste  
aRet[3]     Carácter     Número do documento ou processo  
aRet[4]     Carácter     Código da conta contábil

**Importante**

O sistema sempre espera um array de quatro posições com a ordem demonstrada acima.

Quando não tiver a necessidade da alteração do registro, retornar a posição em branco.

Lembrando que o código de conta contábil retornado através do ponto de entrada deve estar cadastrado devidamente no sistema.  
  
**Exemplo de Utilização:**

`#INCLUDE``"PROTHEUS.CH"`

`User Function EFDCON04()`

`Local cChvEfd     := PARAMIXB[``1``]``// Chave EFD`

`Local cTpAjuste   := PARAMIXB[``2``]``// Tipo de Ajuste`

`Local cDescrAju   := PARAMIXB[``3``]``// Descrição do ajuste`

`Local cConta      := PARAMIXB[``4``]``// Conta contábil`

`Local cCst        := PARAMIXB[``5``]``// CST`

`Local nAlq        := PARAMIXB[``6``]``// Alíquota`

`Local nVlAjuGrv   := PARAMIXB[``7``]``// Valor do ajuste`

`Local cPerAtu     := PARAMIXB[``8``]``// Período Atual`

`Local dDtRefer    := PARAMIXB[``9``]``// Data de referencia`

`Local lAjuBase    := PARAMIXB[``10``]``// Se ajuste de base (.T.) ou de valor (.F.)`

`Local cTributo    := PARAMIXB[``11``]``// Qual tributo está sendo ajustado Pis("1") ou Cofins ("2")`

`Local cNumDoc     := PARAMIXB[``12``]``// Numero do Documento ou processo`

`Local cInfCompl   := PARAMIXB[``13``]``// Informação complementar`

`Local aRet        := {}`

`If SUBSTR(cChvEfd,``18``,``4``) ==``'1.65'` `.and. cTributo ==``'1'`

`cDescrAju :=``"Ajuste teste"`

`cInfCompl :=``"Ajuste teste complementar"`

`cConta   :=``"ENTV000001"`

`ElseIf SUBSTR(cChvEfd,``18``,``4``) ==``'7.60'` `.and. cTributo ==``'2'`

`cDescrAju :=``"Ajuste teste"`

`cInfCompl :=``"Ajuste teste complementar"`

`cConta   :=``"ENTV000001"`

`EndIf`

`aAdd(aRet,cDescrAju)``// Descrição do ajuste`

`aAdd(aRet,cInfCompl)``// Informação complementar`

`aAdd(aRet,``""``)``// Num Doc`

`aAdd(aRet,cConta)``// Código conta contábil`

`Return aRet`

**Assuntos Relacionados:**

* Guia Prático EFD Contribuições: <http://sped.rfb.gov.br/estatico/20/6E34811D4F98083196E2A09880F048189788FC/Guia_Pratico_EFD_Contribuicoes_Versao_1_31%20-%2029_04_2019.pdf>
* Apuração e Arquivo EFD Contribuições:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/9995225390743-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Boletim-t%C3%A9cnico-Apura%C3%A7%C3%A3o-e-gera%C3%A7%C3%A3o-arquivo-txt-EFD-Contribui%C3%A7%C3%B5es?source=search>
