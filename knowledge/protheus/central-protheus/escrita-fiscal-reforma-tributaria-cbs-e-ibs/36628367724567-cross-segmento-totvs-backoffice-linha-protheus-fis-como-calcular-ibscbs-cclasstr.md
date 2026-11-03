---
article_id: 36628367724567
category: Escrita Fiscal - Reforma Tributaria - CBS e IBS
content_hash: ea33c2cac913ba004d92d520f56f2c43c6dd12c09c70c5af876ee98ed6a31947
fetched_at: '2026-06-28T22:39:15.704235+00:00'
product: protheus
section_id: 33305945453079
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como calcular IBS/CBS
  cClasstrib 515001 Diferimento  100%  forma Hibrida?
type: support-article
updated_at: '2025-12-18T18:00:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36628367724567-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-IBS-CBS-cClasstrib-515001-Diferimento-100-forma-Hibrida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36628351656215) Tempo aproximado para leitura: 00:10**min**  
  
**Dúvida**  
 Como calcular IBS/CBS cClasstrib 515001 Diferimento  100%  forma Hibrida?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Nesse exemplo vamos trabalhar com a forma Hibrida de calculo, sendo ICMS, PIS e COFINS pelo TES e IBS/CBS pelo Configurador de tributos

<https://tdn.totvs.com/pages/releaseview.action?pageId=955482625>

**Exemplo de Calculo**

Mercadoria = 1000,00

Base de calculo do ICMS = 1000,00\* ( red 60% ) = 600,00\*18% = 72,00

TES

Calcula icms = sim

L fiscal icms = outros

CST =20

Red base = 40%

Pis/cofins = ambos

cred pis/cof = não calcula

CST pis = 06

CST cof =06

**cClasstrib 515001 - redução de aliquota 60% e diferimento 100%**

Base de calculo do IBS/CBS = 1000,00-72,00 = 928,00

CBS - 928,00\*0,36% = 3,34

IBS - 928,00\*0,04% = 0,37

Para calculo com redução de aliquota, precisa calcular o IBSMUN

IBSMUN

IBSEST

CBSFED

Regra de base de calculo IBSEST , IBSMUN e CBSFED

* **Cód. Regra (F27\_CODIGO)**: TB0001
* **Descrição (F27\_DESC)**: BASE DE CALCULO: CBS FED/IBS EST
* **Valor Origem (F27\_VALORI)**: 11 - Formula Manual
* Fórmula: ( O:VAL\_MERCADORIA + O:FRETE + O:SEGURO + O:DESPESAS + O:VAL\_II ) - ( O:DESCONTO + O:VAL\_PS2 + O:VAL\_CF2 + O:VAL\_ICMS + O:VAL\_DIFAL + O:VAL\_FECP + O:VAL\_FCPDIF + O:VAL\_ISS )

Regra de Alíquota - CBSFED

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36628367695767)

Regra de Aliquota - IBSEST

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36628367695895)

Regra de Aliquota - IBSMUN

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36628367696151)

Regra de escrituração - IBSEST, IBSMUN e CBSFED

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36628367696791)

Regra de Calculo Documentos Fiscais - CBSFED

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36628367697175)![](https://centraldeatendimento.totvs.com/hc/article_attachments/36628367698839)![](https://centraldeatendimento.totvs.com/hc/article_attachments/36628367699607)

Origem x destino = 000002 - todas as Ufs

Participante = Todos os clientes / Todos os fornecedores

Operação = 000069 - CFOP = 5102

Produto = 000052 - ncm 3808.9329

Regra de Calculo Documentos Fiscais - IBSEST

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36628351661463)![](https://centraldeatendimento.totvs.com/hc/article_attachments/36628351661847)

Perfis os mesmos

Regra de Calculo Documentos Fiscais - IBSMUN

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36628367700887)![](https://centraldeatendimento.totvs.com/hc/article_attachments/36628351662487)

Perfis os mesmos

Pedido de Vendas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36628351662743)

Documento emitido

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36628351663511)

Para a transmissão

Importa que os parâmetros abaixo estejam criados e configurados no Protheus.

[Documentação do parâmetro MV\_CSTGXML](https://tdn.totvs.com/pages/viewpage.action?pageId=1011566715)

[Documentação do parâmetro MV\_RTC55](https://tdn.totvs.com/pages/viewpage.action?pageId=1013641031)

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributária – Nota Técnica 2025.002 v.1.10, v1.20 e V1.30. IBS - CBS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33208366723607-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tribut%C3%A1ria-Nota-T%C3%A9cnica-2025-002-v-1-10-v1-20-e-V1-30-IBS-CBS)

XML

IBSCBS>

BSCBS>

<CST>**515**</CST>

<cClassTrib>**515001**</cClassTrib>

<gIBSCBS>

<vBC>**928.00**</vBC>

<gIBSUF>

<pIBSUF>**0.1000**</pIBSUF>

<gDif>

<pDif>**100.0000**</pDif>

<vDif>**0.37**</vDif>

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

<pDif>**0**</pDif>

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

<vDif>**3.34**</vDif>

</gDif>

<gDevTrib>

<vDevTrib>**0**</vDevTrib>

</gDevTrib>

<gRed>

<pRedAliq>**60.0000**</pRedAliq>

<pAliqEfet>**0.36**</pAliqEfet>

</gRed>
