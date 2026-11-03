---
article_id: 360034424993
category: Gestão de Transportes (TMS)
content_hash: adc3659b32bd66ca8bc6fe5c86aa350fb2655ba5e76159157230d39ca3aed049
fetched_at: '2026-06-28T22:45:27.578228+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Conhecimento de transporte eletrônico MOC
  versão 3.00A
type: support-article
updated_at: '2021-09-28T20:27:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034424993-Log%C3%ADstica-Linha-Protheus-TMS-Conhecimento-de-transporte-eletr%C3%B4nico-MOC-vers%C3%A3o-3-00A
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como se adequar as novas regras do **MOC** referente ao **CTe** **3.00A**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Foi implementada a funcionalidade para atender o **Manual de Orientações do Contribuinte** versão **3.00A**, assim como o **Anexo II – Manual de Especificações Técnicas do DACTE**. As principais alterações contempladas estão descritas abaixo:

1. Criação da *tag* **ICMSST** no evento **EPEC**;
2. Exclusão da *tag* **pICMSInterPart** do leiaute do **CT-e**;
3. *Tag* **infCTeSupl** - **Informações Suplementares** do **CT-e**;
4. Dispensa de validação da **IE** do tomador quando autorização de um **CT-e EPEC**;
5. Unificação das regras de validação de chave de acesso;
6. Validação chave de acesso do **CT-e** de anulação informado;
7. Definição da **Consulta Pública resumida e consulta completa** para atores do **CT-e** identificados pelo certificado digital;
8. Definição do **QR Code** do **CT-e**.

A **release**oficial referente a essa legislação foi expedida e publicada em nossa **Central de Downloads**.  
Para a utilização desta funcionalidade, é necessário atualizar o **SIGATMS** e o **TSS**. Solicite a atualização para o Suporte da TOTVS.  
  
Para que as *tags* **infCTeSupl** e **qrCodCte** sejam criadas, é necessária a criação do parâmetro **MV\_URLQCOD**.   
  
Nos parâmetros do **Monitor do CT-e - TMSAE70**, a **versão CT-e** permanece como **3.00**.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043696574/mceclip1.png)

**Saiba mais** Para acessar a documentação da solicitação acesse o *link*: [CT-e 3.00A.](http://tdn.totvs.com/pages/viewpage.action?pageId=502460473)   
Para a criação do parâmetro **MV\_URLQCOD**, segue documentação: [Logística - Linha Protheus - TMS - Tag infCteSupl no CT-e versão 3.00A](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035596554-MP-TMS-Tag-infCteSupl-no-CT-e-vers%C3%A3o-3-00A) **Glossário  
CT-e** - Conhecimento de transporte eletrônico  
**DACTE** - Documento Auxiliar do Conhecimento de Transporte Eletrônico  
**EPEC** - Evento Prévio de. Emissão em Contingência**IE** - Inscrição Estadual**MOC** - Manual de Orientação ao Contribuinte**QR Code** - Quick Response **SEFAZ**- Secretaria de Estado da Fazenda  
**SIGATMS -**Gestão de Transportes  
**TSS** - *Totvs Sped Service*  
**ICMSST -** Imposto sobre Circulação de Mercadorias e Serviços em Substituição Tributária
