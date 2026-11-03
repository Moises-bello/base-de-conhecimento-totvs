---
article_id: 360025956751
category: Gestão de Transportes (TMS)
content_hash: af35caf5095968137da9b917d808eafae619b28065ae12defe3ffe2424511ce1
fetched_at: '2026-06-28T22:45:32.506706+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Quantidade de documentos que serão relacionados
  nos arquivos XML enviados a operadora de frota Repom
type: support-article
updated_at: '2022-11-09T10:53:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025956751-Log%C3%ADstica-Linha-Protheus-TMS-Quantidade-de-documentos-que-ser%C3%A3o-relacionados-nos-arquivos-XML-enviados-a-operadora-de-frota-Repom
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:40 min**  
**Dúvida**Como definir a quantidade de documentos que serão relacionados nos **XML** - *Extensible Markup Language* enviados a operadora de frota **Repom**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Para que no envio do **XML**a operadora de frota **REPOM** seja relacionado mais de um **CT-e** - **Conhecimento de Transporte Eletrônico**, é necessário configurar o parâmetro **MV\_DOCSOPE**, onde no mesmo deve informar a quantidade máxima de documentos que serão relacionados nos arquivos **XML**.  
  
Assim, no arquivo **xxxx\_emitecontrato.xml** irá gerar a *tag* raiz **<conhecimentos>**, onde dentro dela irá gerar as *tags* **<conhecimento>**, sendo informado dentro de cada grupo os conhecimentos de transporte informados na viagem em questão, conforme demonstra imagem abaixo:

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360024940131/Capturar.PNG)
