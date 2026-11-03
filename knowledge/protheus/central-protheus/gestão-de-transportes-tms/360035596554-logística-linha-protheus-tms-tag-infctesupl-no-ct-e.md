---
article_id: 360035596554
category: Gestão de Transportes (TMS)
content_hash: 342ef49c7264cbde133b2443526af35a2c741efaa6cc49eeaf2b4b116d6d88d8
fetched_at: '2026-06-28T22:45:33.397308+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Tag infCteSupl no CT-e
type: support-article
updated_at: '2023-07-20T14:40:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035596554-Log%C3%ADstica-Linha-Protheus-TMS-Tag-infCteSupl-no-CT-e
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16163305114903)***Tempo aproximado para leitura: **00:01:35 min**  
**Dúvida**Como gerar a *tag* **infCteSupl** no **XML** do **CT-e**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**A *tag***infCteSupl** é responsável por receber as informações que geram o **QR Code** no **CT-e.** A primeira parte dessa *tag* é o endereço do site do **Portal** da **SEFAZ** autorizadora do **CT-e,**este variando para cada estado e para ambiente.  
  
Para definir por filial qual o endereço que deve ser utilizado na geração do **CT-e**, foi criado o parâmetro **MV\_URLQCOD.**  
  
Para configurá-lo, é necessário acessar o endereço [Relação de Serviços Web](https://dfe-portal.svrs.rs.gov.br/CTE/Servicos)e identificar qual o endereço de **QR Code** correto considerando a **UF** e o ambiente. Por exemplo, foi encontrado o endereço do ambiente de homologação para o estado de São Paulo.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047254113)

Identificado o endereço correto, é necessário criar o parâmetro **por filial** e preencher com o *link.*

*![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047254273)*

**Importante**  
Se o parâmetro não for criado ou for preenchido de maneira incorreta, a **SEFAZ** irá rejeitar o **CT-e**, como:

* **Rejeição 850** - O grupo de informações do **QR Code infCTeSupl** deve ser informado.
* **Rejeição 851** - Endereço do site do **Portal Nacional** para a consulta via **QR Code** difere do  
  previsto.

**Glossário  
CT-e**- Conhecimento de Transporte eletrônico  
**DACTE** - Documento Auxiliar de CT-e  
**MV\_URLQCOD -**Informar a URL para pesquisa via QR Code, impresso na DACTE **QR Code**- Quick Response **SEFAZ**- Secretaria de Estado da Fazenda**UF** - União Federativa  
**URL** - Uniform Resource Locator  
**XML** - Extensible Markup Language
