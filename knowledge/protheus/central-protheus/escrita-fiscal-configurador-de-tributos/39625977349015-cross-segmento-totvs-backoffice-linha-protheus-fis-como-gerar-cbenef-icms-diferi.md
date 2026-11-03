---
article_id: 39625977349015
category: Escrita Fiscal - Configurador de Tributos
content_hash: 3b09a7674e5b56d90520c59f1754fe74de38faaa0cafdbc9e99c47c78c1656db
fetched_at: '2026-06-28T22:39:17.086993+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus)  - FIS - Como gerar cbenef
  icms diferido forma Hibrida ?
type: support-article
updated_at: '2026-04-09T13:17:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39625977349015-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-gerar-cbenef-icms-diferido-forma-Hibrida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39625977317271) Tempo aproximado para leitura: 05:00 **min**  
  
**Dúvida**  
Como gerar cbenef icms diferido forma Hibrida ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**  
Essa documentação vai auxiliar o cliente a configurar o icms diferido pelo legado para gerar o cBenef , vamos usar o exemplo do estado de SP

MV\_ESTADO = SP

Cliente = SP

TES

**F4\_ICM:**SIM

**F4\_LFICM:** Outros

**F4\_ICMSDIF: 1**

**F4\_PICMDIF: 100%**

**CST = 51**

Código cBenef = SP053500

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39625992761751)

Cadastrar na rotina Fisa156 de forma manual, conforme orientação

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como configurar os Códigos de Valores Declaratórios de São Paulo no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38006107103639-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-os-C%C3%B3digos-de-Valores-Declarat%C3%B3rios-de-S%C3%A3o-Paulo-no-Protheus)

exemplo do calculo:

Valor da mercadoria = 1000,00

Base de calculo ICMS = 1000,00 \*18% = 180,00

ICMS diferido = 180,00

<ICMS51>

<orig>**0**</orig>

<CST>**51**</CST>

<modBC>**3**</modBC>

<pRedBC>**0**</pRedBC>

<vBC>**1000.00**</vBC>

<pICMS>**18.0000**</pICMS>

<vICMSOp>**180.00**</vICMSOp>

<pDif>**100.0000**</pDif>

<vICMSDif>**180.00**</vICMSDif>

<vICMS>**0**</vICMS>

</ICMS51>

IBS/CBS - Configurador de tributos

<https://tdn.totvs.com/pages/releaseview.action?pageId=1025239075>

**Manutenção manual da formula Base de Cálculo:**

* **Cód. Regra (F27\_CODIGO)**: TB0001
* **Descrição (F27\_DESC)**: BASE DE CALCULO: CBS FED/IBS EST
* **Valor Origem (F27\_VALORI)**: 11 - Formula Manual
* Fórmula: ( O:VAL\_MERCADORIA + O:FRETE + O:SEGURO + O:DESPESAS + O:VAL\_II ) - ( O:DESCONTO + O:VAL\_PS2 + O:VAL\_CF2 + O:VAL\_ICM\_TRIBUTADO + O:VAL\_DIFAL + O:VAL\_FECP + O:VAL\_FCPDIF + O:VAL\_ISS\_TRIBUTADO + O:VAL\_IPI\_TRIBUTADO )

Regra de escrituração

**cClasstrib 515001**

Configuração de acordo com a documentação

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como calcular IBS/CBS cClasstrib 515001 Diferimento 100% forma Hibrida?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36628367724567-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-IBS-CBS-cClasstrib-515001-Diferimento-100-forma-Hibrida)

Pedido de Vendas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39625992763543)

Configuração para o cBenef

**MV\_MTCLF3K =0**

**Fisa140**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39625992765847)

Reflexo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39625977323287)

Para o icms diferido ser gerado no cbenef o mesmo precisa ser calculado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39625977326359)

<NCM>**39269090**</NCM>

<cBenef>**SP053500**</cBenef>

**Obs: Para não destacar o ICMS diferido no XML usar o parametro MV\_art186**

[**Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como destacar em nota de diferimento BC.ICMS e V.ICMS no XML e Danfe**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020715772-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-destacar-em-nota-de-diferimento-BC-ICMS-e-V-ICMS-no-XML-e-Danfe)

Para a transmissão estar configurado de acordo com a informação abaixo:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como destacar em nota de diferimento BC.ICMS e V.ICMS no XML e Danfe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020715772-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-destacar-em-nota-de-diferimento-BC-ICMS-e-V-ICMS-no-XML-e-Danfe)

**Transmissão**

IBSCBS>

<CST>**515**</CST>

<cClassTrib>**515001**</cClassTrib>

<gIBSCBS>

<vBC>**1000.00**</vBC>

<gIBSUF>

<pIBSUF>**0.1000**</pIBSUF>

<gDif>

<pDif>**100.0000**</pDif>

<vDif>**0.40**</vDif>

</gDif>

<gDevTrib>

<vDevTrib>**0**</vDevTrib>

</gDevTrib>

<gRed>

<pRedAliq>**60.0000**</pRedAliq>

<pAliqEfet>**0.04**</pAliqEfet>

</gRed>

<vIBSUF>**0**</vIBSUF>

</gIBSUF>

<gIBSMun>

<pIBSMun>**0**</pIBSMun>

<gDif>

<pDif>**100.0000**</pDif>

<vDif>**0**</vDif>

</gDif>

<gDevTrib>

<vDevTrib>**0**</vDevTrib>

</gDevTrib>

<gRed>

<pRedAliq>**60.0000**</pRedAliq>

<pAliqEfet>**0**</pAliqEfet>

</gRed>

<vIBSMun>**0**</vIBSMun>

</gIBSMun>

<vIBS>**0**</vIBS>

<gCBS>

<pCBS>**0.9000**</pCBS>

<gDif>

<pDif>**100.0000**</pDif>

<vDif>**3.60**</vDif>

</gDif>
