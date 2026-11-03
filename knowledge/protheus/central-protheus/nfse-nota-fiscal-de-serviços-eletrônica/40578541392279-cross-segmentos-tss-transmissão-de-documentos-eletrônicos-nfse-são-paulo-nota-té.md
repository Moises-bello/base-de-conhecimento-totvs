---
article_id: 40578541392279
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 3b0746b23231342bee3d18801b7d895f0dd0c9b06fc58b967f61e7bdcc1e4f86
fetched_at: '2026-06-28T22:39:58.692355+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - TSS Transmissão de Documentos Eletrônicos - NFSE - São Paulo
  - Nota Técnica SE/CGNFS-e nº 007
type: support-article
updated_at: '2026-06-23T17:17:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40578541392279-Cross-Segmentos-TSS-Transmiss%C3%A3o-de-Documentos-Eletr%C3%B4nicos-NFSE-S%C3%A3o-Paulo-Nota-T%C3%A9cnica-SE-CGNFS-e-n%C2%BA-007
---

**Dúvida**  
A Secretaria Municipal da Fazenda da Prefeitura de São Paulo anunciou mudanças importantes na sistemática de emissão da Nota Fiscal de Serviços eletrônica (NFS-e) nos [leiautes 1 e 2](https://www.totvs.com/blog/fiscal-clientes/nfs-e-sao-paulo-detalha-regras-do-ibs-e-cbs-obrigatorios-a-partir-de-agosto-de-2026/). As alterações **passaram a valer em 14 de maio de 2026**e impactam diretamente o preenchimento das informações relacionadas aos tributos federais, especialmente **PIS, COFINS e CSLL.**

A atualização foi realizada para adequar o sistema da NFS-e à[Nota Técnica SE/CGNFS-e nº 007/2026](https://www.totvs.com/blog/fiscal-clientes/nfs-e-nacional-nota-tecnica-no-007-2026-esclarece-pis-cofins-retencoes-e-atualiza-codigos-de-operacao/), publicada em fevereiro de 2026 pela Secretaria-Executiva do Comitê Gestor da NFS-e.  
  
Comunicado completo: <https://www.totvs.com/blog/fiscal-clientes/sao-paulo-atualiza-emissao-de-nfs-e-com-mudancas-em-tributos-federais>.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**  
Para adequarmos as alterações realizadas pela prefeitura, foi realizada a abertura da issue **DSERTSS1-36826** com a equipe de **Produto do TSS,** **liberada em 26/05/2026:**  
  
**Aplicar o ptm no RPO do TSS:**  
Atualizações [12.1.2410](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1255363)  
Atualizações [12.1.2510](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1255361)

**Atualizar schema de São Paulo-SP:**  
[**Usar apenas aquivo nfse\_v2.00\_3550308.xsd desse pacote**](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1253725)  
  
Para o correto funcionamento é importante **aplicar no Protheus** o pacote da issue **DSERTSS1-36777** que contem o rdmake NFSEXMLENV:  
Atualizações [12.1.2410](https://r.totvs.io/p/1252104%C2%A0)  
Atualizações [12.1.2510](https://r.totvs.io/p/1252102)

A atualização do RDMake implica também na **atualização do XSD único**, que deve ser colocado na pasta **Schemas do TSS:**  
Atualizações [12.1.2410](https://r.totvs.io/p/1244003%20)   
Atualizações [12.1.2510](https://r.totvs.io/p/1243999)  
  
**Crie na SX6 o parametro MV\_NT007 e coloque conteúdo .T., reinicie o Protheus em seguida:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40820526772631)

O **parâmetro** deverá ser configurado como **True** caso a prefeitura tenha aderido à NT 007, caso contrário, devera estar como False.

**IMPORTANTE:** **O TSS compartilhado já contempla todas as atualizações disponibilizadas para o município de São Paulo/SP referentes à NT 007.**
