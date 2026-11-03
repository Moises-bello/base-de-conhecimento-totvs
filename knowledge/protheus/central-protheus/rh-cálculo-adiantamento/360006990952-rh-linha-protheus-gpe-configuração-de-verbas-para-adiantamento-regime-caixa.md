---
article_id: 360006990952
category: RH - Cálculo Adiantamento
content_hash: c397094cbbf655f0726462d2ccb2a3bdc7f8f810f1952f21694409c5ad08c7e6
fetched_at: '2026-06-28T22:43:14.285008+00:00'
product: protheus
section_id: 360011983213
source: central-protheus
title: RH - Linha Protheus - GPE - Configuração de verbas para Adiantamento (regime
  caixa)
type: support-article
updated_at: '2025-10-17T11:40:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006990952-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-de-verbas-para-Adiantamento-regime-caixa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24581200717079) Tempo aproximado para leitura: **00:02:30 min  
  
Dúvida**Como efetuar a configuração de verbas de IR para o tipo de regime caixa no cálculo do adiantamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12  
  
**Solução**Nesta base de conhecimento será apresentada a configuração correta do ambiente acerca do cálculo do **imposto de renda** do **adiantamento** salarial quando o cliente possuir **Regime de Caixa.**  
  
As verbas que são utilizadas no calculo do adiantamento devem seguir a seguinte configuração no **cadastro de verbas** (GPEA040):

|  |  |
| --- | --- |
| ID 0006 (verba de provento) | Ref.Adto "SIM"  IRRF = “SIM” |
| ID 0007 (verba de desconto) | Ref.Adto "NÃO"  IRRF = “SIM” |
| ID 0008 (verba de desconto do arredondamento) | Ref.Adto "NÃO"  IRRF = “NÃO” |
| ID 0009 (verba de desconto do IR de Adto) | Ref.Adto "SIM"   IRRF = “NÃO” |
| ID 0010 (verba de Base Ir Adto) | Ref.Adto “SIM"   IRRF = “NÃO” |
| ID 0011 (verba de desconto de Dif IR) | Ref.Adto "SIM"   IRRF = “NÃO” |
| ID 0012 (verba de Base IR Adto) | Ref.Adto "NÃO"  IRRF = “NÃO” |
| ID 0106 (verba de Base IR Mês Anterior) | Ref.Adto "NÃO"  IRRF = “NÃO” |
| ID 0107 (verba de BASE Desconto IR Mês Anterior) | Ref.Adto "NÃO"  IRRF = “NÃO” |

Para que o sistema gere essas verbas será necessário configurar também o campo **V Mes Segui** (RV\_CODMSEG) da seguinte maneira:

 - Verba de identificador **0015** com o campo **RV\_CODMSEG** com a verba do identificador **0106**

 - Verba de identificador **0066** com o campo **RV\_CODMSEG** com a verba do identificador **0107**

**IMPORTANTE:** Além da parametrização das verbas, no cadastro de **Períodos**, pelo caminho **>Atualizações >Definições de Cálculo >Períodos,** para os roteiros **FOL e ADI** a coluna **Data Pgto** deve seguir a regra do regime caixa, portanto o roteiro **FOL** deve ter a data de pagamento **dentro do mês seguinte até o 5º dia útil** conforme regra da **Receita Federal:**  
**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404328909591)**

**Exemplo**

Verba de Id**0015**

![](https://tdn.totvs.com/download/attachments/232817416/image2016-3-7%2013%3A21%3A53.png?version=1&modificationDate=1457360575000&api=v2)

Verba de ID **0106**

![](https://tdn.totvs.com/download/attachments/232817416/image2016-3-7%2013%3A23%3A28.png?version=1&modificationDate=1457360670000&api=v2)

Verba de ID **0066**

**![](https://tdn.totvs.com/download/attachments/232817416/image2016-3-7%2013%3A24%3A26.png?version=1&modificationDate=1457360728000&api=v2)**

Verba de ID **0107**

**![](https://tdn.totvs.com/download/attachments/232817416/image2016-3-7%2013%3A25%3A10.png?version=1&modificationDate=1457360773000&api=v2)**

**Exemplo de Teste Base de IR e Desconto de IR mês anterior**

Período **12/2014** Folha com Pagamento em **05/01/15:**

![](https://tdn.totvs.com/download/attachments/232817416/image2016-3-7%2013%3A27%3A21.png?version=1&modificationDate=1457360904000&api=v2)

Funcionário 100000

![](https://tdn.totvs.com/download/attachments/232817416/image2016-3-7%2013%3A28%3A3.png?version=1&modificationDate=1457360945000&api=v2)

Funcionário 100016

![](https://tdn.totvs.com/download/attachments/232817416/image2016-3-7%2013%3A28%3A48.png?version=1&modificationDate=1457360990000&api=v2)

Fechamento da folha 12/2014

**![](https://tdn.totvs.com/download/attachments/232817416/image2016-3-7%2013%3A30%3A0.png?version=1&modificationDate=1457361062000&api=v2)**

**Observação**Ao efetuar o **fechamento** da **folha,** é importante se certificar que o roteiro de **ADI** (adiantamento) do próximo mês esteja aberto, para que as verbas fiquem salvas no roteiro correto.

***![](https://tdn.totvs.com/download/attachments/232817416/image2017-8-25%2017%3A43%3A35.png?version=1&modificationDate=1503693816000&api=v2)***

Após o fechamento já é possível ver que o sistema levou as verbas de **IR** e **Base IR** mês anterior em **Lançamentos Por Funcionário** quando selecionamos o roteiro **ADI**

Funcionário 100000

![](https://tdn.totvs.com/download/attachments/232817416/image2016-3-7%2013%3A30%3A54.png?version=1&modificationDate=1457361116000&api=v2)

Funcionário 100016

![](https://tdn.totvs.com/download/attachments/232817416/image2016-3-7%2013%3A31%3A56.png?version=1&modificationDate=1457361178000&api=v2)

**Importante**Em casos de **implantação sem migração** dos valores do mês anterior vindos de outro sistema, as verbas de **Base IR mês Anterior** (Id 0106) e **IR mês anterior** (Verba do IR descontado na folha de pagamento no dia 05 do mês), devem ser **informadas** no cálculo do Adiantamento, apenas no **primeiro** cálculo de adiantamento feito no Protheus.

**Saiba mais**

[RH - Linha Protheus - GPE - Configuração de verbas para Adiantamento (regime competência)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036123334)

[RH - Linha Protheus - GPE - Adiantamento Salarial - Configurações e Conceitos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052166714-RH-Linha-Protheus-GPE-Adiantamento-Salarial-Configura%C3%A7%C3%B5es-e-Conceitos?source=search)

[RH - Cálculo Adiantamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983213-RH-C%C3%A1lculo-Adiantamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
