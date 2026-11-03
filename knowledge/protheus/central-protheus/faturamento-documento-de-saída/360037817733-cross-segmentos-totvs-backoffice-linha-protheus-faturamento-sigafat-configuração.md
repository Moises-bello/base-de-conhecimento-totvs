---
article_id: 360037817733
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 3997b6b8ff55aaaa132c7186e0a38ff3485419a6ae6115d4396fae37fa0cd8c5
fetched_at: '2026-06-28T22:38:44.180538+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - Configuração do FATJOBNFE para mais de uma empresa
type: support-article
updated_at: '2023-03-20T19:18:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037817733-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Configura%C3%A7%C3%A3o-do-FATJOBNFE-para-mais-de-uma-empresa
---

**Dúvida**

Configuração do FATJOBNFE para mais de uma empresa.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

Para os casos da empresas que possuem mais de uma filial é  necessário configurar uma seção do job para cada filial, exemplo:

      [ONSTART]  
      JOBS=FatJobNFe\_<empresa><filial>  
      [FatJobNFe\_<empresa><filial>] 

      ...

      nParms=2  
​      **parm1=<Empresa>  
      PARM2=AAAA**

      [ONSTART]  
      JOBS=FatJobNFe\_<empresa><filial>  
      [FatJobNFe\_<empresa><filial>] 

      ...

      nParms=2  
     ​ parm1=**<Empresa>  
      PARM2=BBBB**

Caso possua mais de um empresa para configuração, é necessário que efetue a configuração em cada empresa de forma separada, não há uma centralizadora por empresa.

Caso possua ambiente com Gestão de empresa, é necessário registrar no INI uma sessão para cada Filial, onde os parâmetros devem receber por exemplo:

parm1=T1 (Grupo de empresa)  
parm2=D MG 01 (D=Empresa, MG=Unidade, 01=Filial)

**Saiba Mais**: **[FAT0191\_FATJOBNFE\_para\_Exclusão\_documento\_de\_Saída\_MATA521](https://tdn.totvs.com/pages/viewpage.action?pageId=272154294)**
