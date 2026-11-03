---
article_id: 38295962824215
category: Reforma Tributária
content_hash: a1fcecd5454379ea1c8286928fa0e0a4d5464a5216fc0b946717d47e2a257744
fetched_at: '2026-06-28T22:39:53.700480+00:00'
product: protheus
section_id: 34900856700439
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - NT 2018.005
  Criação das tags idCSRT e hashCSRT
type: support-article
updated_at: '2026-05-27T20:32:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38295962824215-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-NT-2018-005-Cria%C3%A7%C3%A3o-das-tags-idCSRT-e-hashCSRT
---

**Dúvida**  
Como destacar as tags idCSRT e hashCSRT no xml?  
  
**Ambiente**   
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**

Foi adequado o ERP Protheus para geração das tags **<idCSRT> e <hashCSRT>** referentes ao Responsável Técnico do XML (**<gRespTec>**) conforme **Nota Técnica 2018.005 v1.52.**

Pré-requisito para funcionamento:

Aplicar o patch e nfesefaz no Protheus:

12.1.2310:<https://r.totvs.io/p/1236955> ; [Somente para cliente com garantia estendida]

12.1.2410:<https://r.totvs.io/p/1236956> ;

12.1.2510:<https://r.totvs.io/p/1236953> ;

**Atualização do TSS**

**1.** **Arquivos de Schema:** [Download dos schemas](https://suporte.totvs.com/portal/p/10098/download?e=761857)  
Apoio caso necessário: [Procedimento: Substituir na pasta schemas do TSS.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552-Cross-Segmentos-TSS-Transmiss%C3%A3o-de-Documentos-Eletr%C3%B4nicos-Atualiza%C3%A7%C3%A3o-dos-SCHEMAS)  
  
**2.** **Atualizar RPO do TSS:** [Clique aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-Cross-Segmentos-TSS-Transmiss%C3%A3o-de-Documentos-Eletr%C3%B4nicos-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS) Atualizado em 31/12/2025  
Documentação: [maiores detalhes.](https://tdn.totvs.com/pages/releaseview.action?pageId=956646956)

O parâmetro **MV\_NT18005** tem como objetivo de definir data de vigência da **Nota Técnica 0018005**, na qual passa a ser obrigatório o  envio do **idCSRT** e do **hashCSRT** no grupo de campos de identificação do responsável técnico para o estado do Paraná.

Para o estado do Paraná, o **CSRT** será opcional em ambiente de **homologação** até **19/01/2026** e em **produção** até **23/02/2026**. Após essas datas, o envio do **idCSRT**e do **hashCSRT** passará a ser obrigatório. Portanto, até o início da obrigatoriedade, esses campos serão facultativos para as empresas.

O preenchimento do parâmetro **MV\_NT18005** funciona da seguinte forma:  
quando o parâmetro **não estiver criado**, será considerada automaticamente a **data de produção: 23/02/2026**.

**Exemplo de configuração do parâmetro MV\_NT18005:**

* **Homologação**: PR = 19/01/2026
* **Produção**: PR = 23/02/2026

No momento, a funcionalidade encontra-se vigente exclusivamente no estado do Paraná, sendo a data mencionada referente à sua entrada em produção.

Para possibilitar a habilitação futura da funcionalidade para outras **UFs**, o parâmetro aceita múltiplas configurações no formato **UF=DD/MM/AAAA**, conforme o exemplo **hipotético**abaixo:

**PR=23/02/2026;SP=DD/MM/AAAA;RJ=DD/MM/AAAA**

**Importante:**

* As UFs **SP** e **RJ** são apresentadas apenas como **exemplo de formatação**.
* Até que haja publicação oficial, somente o estado do **Paraná (PR)** deve ser considerado.
* Cada UF deve ser separada por ponto e vírgula (;).

.

Exemplo:

**MV\_NT18005** = PR=23/02/2026;

![](https://tdn.totvs.com/download/attachments/1039016241/image-2026-1-28_18-21-29.png?version=1&modificationDate=1769635289860&api=v2)![](https://tdn.totvs.com/download/attachments/1039016241/image-2026-1-28_18-23-23.png?version=1&modificationDate=1769635403500&api=v2)

Aviso

* Até que haja publicação oficial, somente o estado do **Paraná (PR)** deve ser considerado.

## **03. CRIAÇÃO DO PARÂMETRO**

**1.** Criando o parâmetro.

**a)**Acessar o módulo**SIGACFG;**

**b)** Acessar a rotina **Base de Dados** \ **Dicionário** \ **Base de Dados** ou **Ambiente** \ **Cadastros** \ **Parâmetros;**

Vamos utilizar a rotina **Ambiente** \ **Cadastros** \ **Parâmetros**.

![](https://tdn.totvs.com/download/attachments/1039016241/image2020-10-8_11-51-19.png?version=1&modificationDate=1769633459230&api=v2)

**c)** Selecionar **Parâmetros**, e em seguida, clicar na opção **Incluir**.

![](https://tdn.totvs.com/download/attachments/1039016241/image2020-10-8_11-50-29.png?version=1&modificationDate=1769633459160&api=v2)

**d)** Informar os dados da criação do parâmetro.

Na aba **Informações**, para os campos:

**Filial:** pode ser específico por filial ou em branco (genérico para todas as filiais).

**Nome da Var.:** nome do parâmetro: **MV\_NT18005**

**Tipo:**deve ser **1-Caractere**.

**Cont. Por**: Preencher conforme orientações do tópico **02. Exemplo de Utilização**

**Cont. Ing**:

**Cont. Esp**:

**e)** Na aba **Descrição**, para os campos:

**Descrição**: Define a vigencia e obrigatoriedade do CSRT.

**Cont. Descriç**:

Caso necessário, informar a descrição em outros idiomas, possuem os mesmos campos para inglês e espanhol.

![](https://tdn.totvs.com/download/attachments/1039016241/image-2026-1-28_18-21-29.png?version=1&modificationDate=1769635289860&api=v2)

Aviso

* Até que haja publicação oficial, somente o estado do **Paraná (PR)** deve ser considerado.
* Para utilizar esses recursos será necessário estar com a **LIB** a partir da versão **20250811**e com o **License Server**a partir da versão **versão 3.7.0**também atualizado.

Obs: A lib do Protheus precisa estar atualizada. Aplicar de acordo com sua versão. Faça backup antes de aplicar a lib.  
   
<https://suporte.totvs.com/portal/p/10098/download#detail/1168735>  
   
<https://suporte.totvs.com/portal/p/10098/download#detail/1050526>

[Framework - Linha Protheus - Atualização do License Server Virtual versões anteriores 3.5.0](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000518708-Framework-Linha-Protheus-Atualiza%C3%A7%C3%A3o-do-License-Server-Virtual-vers%C3%B5es-anteriores-3-5-0)
