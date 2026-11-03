---
article_id: 360026204011
category: Gestão de Transportes (TMS)
content_hash: cb1e9312fee638072b8438faac4b2fe50440487cc12aa70964744a3702d6b111
fetched_at: '2026-06-28T22:45:29.311209+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Impressão do Logo na DACTE e DAMDFE
type: support-article
updated_at: '2024-12-05T17:30:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026204011-Log%C3%ADstica-Linha-Protheus-TMS-Impress%C3%A3o-do-Logo-na-DACTE-e-DAMDFE
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22825895154583)***Tempo aproximado para leitura:**00:00:45 min****Dúvida**Como exibir o logo da empresa na impressão da **DACTE** e **DAMDFE**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões.  
  
**Solução**Crie um arquivo **.BMP** dentro da pasta **protheus\_data/system** com as seguintes informações:  
Para **CT-e**: Nome do arquivo **logoCte + Código da Empresa**;Para **MDF-e**: Nome do arquivo **logoDAMDFE + Código da Empresa**.  
  
Exemplo do nome do arquivo:  
Sendo **01** o código da empresa

![empresa01.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360025779112)

Para **CT-e:** O nome do arquivo será **logoCte01**

![logocte01.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360025834971)

Para **MDF-e**: o Nome do arquivo será **logoDAMDFE01**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046102374)**

Atente-se a configuração de extensões de nomes de arquivo.   
Se a opção estiver desabilitada, o nome do arquivo fica sem a extensão **.BMP**, não sendo necessário escrevê-lo no nome.

![extensoes_de_nomes_de_arquivos.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360025779572)

**DACTE**impresso:

![dacte.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046962573)

**DAMDFE**impresso:

![damdfe.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046961633)

**Importante**O arquivo deve ter o tamanho de 50 x 50 *pixels* e arquivo em média de 25KB. **Glossário  
CT-e:** Conhecimento de Transporte Eletrônico **DACTE:** Documento Auxiliar do CT-e **DAMDFE:** Documento Auxiliar do MDF-e **MDF-e:** Manifesto de Documentos Fiscais Eletrônico
