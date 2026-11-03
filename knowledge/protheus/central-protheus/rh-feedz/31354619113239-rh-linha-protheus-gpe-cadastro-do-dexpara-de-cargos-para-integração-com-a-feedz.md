---
article_id: 31354619113239
category: RH - Feedz
content_hash: 86a95d11a10354c3f34a80b08b01d8858046ad88b044d26746fd52900819f527
fetched_at: '2026-06-28T22:43:08.584859+00:00'
product: protheus
section_id: 30156142614039
source: central-protheus
title: RH - Linha Protheus - GPE - Cadastro do DexPara de Cargos para integração com
  a Feedz
type: support-article
updated_at: '2025-04-11T21:13:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31354619113239-RH-Linha-Protheus-GPE-Cadastro-do-DexPara-de-Cargos-para-integra%C3%A7%C3%A3o-com-a-Feedz
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31354642125463) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como fazer o cadastro do DexPara de Cargos para integração com a Feedz?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**A criação do **DexPara de Cargos** só é necessária quando a tabela **SQ3** (Cargos), **tem algum nível de exclusividade**. Essa medida é obrigatória pois a **Feedz não aceita registros que tenham descrições iguais** (nomes), mesmo quando os códigos são diferentes.  
  
Veja exemplo do fluxo de validações e cadastros:  
  
**1 -** A tabela **SQ3** é totalmente exclusiva:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31354642131991)  
  
  
  
**2 -** A rotina do **DexPara de Cargos (GPEA944B)** deve ser **incluída no menu** pelo **Configurador:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31354642132375)  
  
  
  
**3 -** No ambiente existem dois Cargos com descrição Teste e código 01, portanto, é necessário relacionar estes dois registros para que na Feedz, exista **um único cadastro de Cargo com essa nomenclatura:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31354619089047)  
  
  
  
**4 -** Ao acessar a rotina do **DexPara de Cargos** pela primeira vez, a tela será exibida vazia. Para incluir um registro, clique na opção **Incluir:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31354619091223)  
  
  
  
**5 -** Os campos **Código e Descrição são livres**, e não é obrigatório que eles tenham o mesmo código e descrição dos Cargos que serão utilizados.   
Após preenchimento destes campos, clique em **Outras Ações > Vincular Cargos:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31354619091991)  
  
  
  
**6 -** Na janela de seleção, devem ser **selecionados** os **Cargos** que serão **vinculados:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31354642135831)  
  
  
  
**7 -** Com isso, a rotina mostra ao usuário os **Cargos selecionados que serão vinculados**. Estando tudo correto, basta Confirmar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31354619094039)  
  
  
  
**8 -** Após salvar o cadastro, a tela do **DexPara de Cargo**s ficará desta forma:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31354642138647)  
  
  
  
**9 -** Por fim, faça a **integração** dos Cargos pela rotina de **Carga Inicial (GPEM939):**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31354642139159)  
  
  
  
**10 -** Se **não existirem inconsistências** nos dados, a integração será concluída com sucesso:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31354619103511)  
  
  
Cabe ressaltar que se a tabela SQ3 for **totalmente compartilhada**, **não é necessário o cadastro do DexPara de Cargos**.  
  
**Saiba Mais:**[RH - Linha Protheus - GPE - Integração de Cargos para Feedz](https://centraldeatendimento.totvs.com/hc/pt-br/articles/31355180660887-RH-Linha-Protheus-GPE-Integra%C3%A7%C3%A3o-de-Cargos-para-Feedz)  
[Documentação Técnica - Integração com a Feedz - Pt. 1](https://tdn.totvs.com/pages/releaseview.action?pageId=756450483#jsons-funcionarios)  
[Documentação Técnica - Integração com a Feedz - Pt. 2](https://tdn.totvs.com/pages/viewpage.action?pageId=756451624)
