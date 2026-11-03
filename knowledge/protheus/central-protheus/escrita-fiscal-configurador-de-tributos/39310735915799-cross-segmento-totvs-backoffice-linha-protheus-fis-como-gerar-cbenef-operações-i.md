---
article_id: 39310735915799
category: Escrita Fiscal - Configurador de Tributos
content_hash: 68af96e67e693860e4eb8df58a8e07d454697209d6382868273d31258722bb7c
fetched_at: '2026-06-28T22:39:17.102369+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) -  FIS - Como gerar cBenef
  operações Isentas no Fisa170?
type: support-article
updated_at: '2026-03-26T14:57:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39310735915799-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-gerar-cBenef-opera%C3%A7%C3%B5es-Isentas-no-Fisa170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39310735886999) Tempo aproximado para leitura: 08:00**min**  
  
**Dúvida**  
Como gerar cBenef operações Isentas no Fisa170?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões]  
  
**Solução**  
Segue exemplo de configuração para ICMS operação isenta , configurado no Fisa170, o exemplo se aplicar a qualquer estado.

Exemplo

MV\_ESTADO = SP

Cliente = SP

TES

CFOP = 5915

cBenef SP070090

Cadastro do codigo SP070090 na rotina fisa156

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como configurar os Códigos de Valores Declaratórios de São Paulo no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38006107103639-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-os-C%C3%B3digos-de-Valores-Declarat%C3%B3rios-de-S%C3%A3o-Paulo-no-Protheus)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39310797276695)

Configurador

ID tributos

ICMS

Regra de base de calculo

O:ZERO

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39310735888151)![](https://centraldeatendimento.totvs.com/hc/article_attachments/39310797278615)

Regra de aliquota

O:ZERO

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39310735890327)

Regra de escrituração

Incidencia = isento

CST = 40

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39310735890839)

Regra de calculo Documentos Fiscais - ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39310797279639)![](https://centraldeatendimento.totvs.com/hc/article_attachments/39310797280407)![](https://centraldeatendimento.totvs.com/hc/article_attachments/39310797280791)

Pedido de Vendas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39310797282839)

IBSEST / IBSMUN / CBSFED - operação isentas

cClasstrib = 410999

cBenef

Mensagem

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39310797284631)

Cadastro Regra de Ajuste de lançamento

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39310735896727)![](https://centraldeatendimento.totvs.com/hc/article_attachments/39310797288087)![](https://centraldeatendimento.totvs.com/hc/article_attachments/39310735901591)![](https://centraldeatendimento.totvs.com/hc/article_attachments/39310735901719)

XML

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributária – Nota Técnica 2025.002 v.1.10, v1.20 e V1.30. IBS - CBS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33208366723607-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tribut%C3%A1ria-Nota-T%C3%A9cnica-2025-002-v-1-10-v1-20-e-V1-30-IBS-CBS)

prod>

<cProd>**000027**</cProd>

<cEAN>**SEM GTIN**</cEAN>

<xProd>**NCM 39269090**</xProd>

<NCM>**39269090**</NCM>

<cBenef>**SP070090**</cBenef>

<CFOP>**5915**</CFOP>

<uCom>**UN**</uCom>

<qCom>**1.0000**</qCom>

<vUnCom>**1000.0000000000**</vUnCom>

<vProd>**1000.00**</vProd>

<cEANTrib>**SEM GTIN**</cEANTrib>

<uTrib>**UN**</uTrib>

<qTrib>**1.0000**</qTrib>

<vUnTrib>**1000.0000000000**</vUnTrib>

<indTot>**1**</indTot>

</prod>

<imposto>

<ICMS>

<ICMS40>

<orig>**0**</orig>

<CST>**41**</CST>

</ICMS40>

</ICMS>
