---
article_id: 360028350192
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 4fcd5726fb1c492fc0f07fc2de299379128289db15cd8a5a30d8493573843a92
fetched_at: '2026-06-28T22:42:09.225497+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Alteração de
  Valores da Guia de Recolhimento
type: support-article
updated_at: '2022-08-17T19:43:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028350192-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Altera%C3%A7%C3%A3o-de-Valores-da-Guia-de-Recolhimento
---

**Dúvida**

Ponto-de-Entrada: DADOSTIT - Alteração de valores da Guia de Recolhimento

**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 10.  
  
**Solução**  
Descrição:  
Ponto de Entrada localizado após a gravação das informações padrão do tributo para título a ser gerado no financeiro, isso vale para todos os impostos processados na função GravaTit(). Deve ser utilizado para complementar ou alterar os valores referentes ao número da Guia de Recolhimento e data de vencimento do título da guia de recolhimento.

Programa Fonte

Sintaxe

DADOSTIT - Alteração de valores da Guia de Recolhimento ( [ @ARRAY ] ) --> ARRAY

Parâmetros:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029015032/mceclip0.png)

Retorno  
**ARRAY**  
       (vetor)  
       [1] = Retornar o número do título. [2] = Retornar o vencimento do título.  
  
**Observações:**  
  
A USER FUNCTION pode retornar "Nil" e manter o tratamento padrão, ou pode retornar um array contendo no primeiro indice o número do título que foi alterado e no segundo indice o vencimento do título que foi alterado.

**Exemplos:**  
User Function DADOSTIT() Local aTeste := {}Local cOrigem := PARAMIXB[1]If AllTrim(cOrigem)=="MATA954" //Apuracao de ISS aTeste := {"9999999999", DataValida(dDataBase+30,.T.)}EndIf Return (aTeste)  
Variáveis

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029014171/mceclip1.png)

Abaixo link contendo as informações acima:

<http://tdn.totvs.com/pages/releaseview.action?pageId=6077146>
