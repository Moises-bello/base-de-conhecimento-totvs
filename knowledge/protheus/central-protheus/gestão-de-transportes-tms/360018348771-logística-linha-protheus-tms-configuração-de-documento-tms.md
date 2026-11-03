---
article_id: 360018348771
category: Gestão de Transportes (TMS)
content_hash: b4962e51bd0b2305ded64c71a6cd4785eade2813eed86adeb858eb9cbef395e7
fetched_at: '2026-06-28T22:45:27.549174+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Configuração de documento TMS
type: support-article
updated_at: '2022-02-02T11:23:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018348771-Log%C3%ADstica-Linha-Protheus-TMS-Configura%C3%A7%C3%A3o-de-documento-TMS
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura:**00:02:06 min  
  
Dúvida**Como realizar o cadastro de **Configuração de Documento - TMSA150**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões  
  
**Solução**A importância deste cadastro deve-se a necessidade da geração de documentos que representarão fiscal, financeira e operacionalmente os serviços prestados pelo transportador.  
  
Comparando com um cenário mais comum de uma revenda de mercadorias de uso e consumo que emite a **NF-e** para formalizar suas vendas, o transportador por sua vez para acobertar sua prestação de serviço de transporte emite o **CT-e** ou a **NFS-e**.  
  
Por padrão, o **TOTVS Logística TMS** disponibiliza alguns tipos de documentos que são essenciais na operação do modulo, sendo eles**:**

* **Ordem de coleta**;
* **CTRC**;
* **AWB***;*
* **Nota Fiscal** entre outros documentos fiscais.

Este cadastro tem como objetivo possibilitar o vinculo do tipo de documento **DUI\_DOCTMS - Doc. Transp.** com o produto de cálculo **DUI\_CODPRO - Cod. Produto** e série **DUI\_SERIE - Série**.  
  
Com o advento do **CT-e**, os documentos que antes eram emitidos em formulário contínuo **CTRC**, passaram a ser validados pela **SEFAZ**, para contemplarmos algumas necessidades sistêmicas de identificação desses documentos eletrônicos, utilizamos o parâmetro **MV\_ESPECIE** para informar o **tipo do documento CT-e** e a **série que será utilizada** para esse tipo de documento.  
  
Portanto, apesar da nomenclatura **CTRC** disponível neste cadastro, o módulo, se configurado de maneira correta fará a geração de documentos eletrônicos **CT-e** e **NFS-e**.  
  
Existem ainda outros tipos de documentos que são disponibilizados na consulta padrão do campo **DUI\_DOCTMS**  - **Doc. Transp.** com a ativação do parâmetro **MV\_TMSCFEC**.  
  
**Importante**  
Este cadastro posteriormente será vinculado ao cadastro de **Regra de Tributação - TMSA410** e **Regra por Cliente - TMSA600**.  
  
**Glossário****AWB** - Air Waybill**CT-e** - Conhecimento de Transporte Eletrônico  
**CTRC** - Conhecimento de Transporte Rodoviário de Cargas  
**NF-e** - Nota Fiscal Eletrônica  
**NFS-e** - Nota Fiscal de Serviço Eletrônico  
**SEFAZ** - Secretaria de Estado da Fazenda
