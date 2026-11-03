---
article_id: 4405299236631
category: Call Center - Televendas
content_hash: 6740c550d56e672cb5ea02ba79b0070a49869252cbc58fbb1ab5484c8bf8f439
fetched_at: '2026-06-28T22:41:30.218888+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK- Integração SIGATMK
  x SIGACRD
type: support-article
updated_at: '2021-07-30T14:28:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405299236631-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Integra%C3%A7%C3%A3o-SIGATMK-x-SIGACRD
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **HH:MM:SS min** **Dúvida**

Quais as configurações necessárias para gerar a integração entre o SIGATMK e SIGACRD (Sistema de Fidelização e Análise de Crédito)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK - Todas as versões  
  
**Solução**

Para que ocorra a integração, é necessário:

* **Parâmetros**:

  - **MV\_AUTOCOM** = 1

  - **MV\_EMPTEF**= 00000000 

  - **MV\_OPFAT**=S

  -**MV\_CRDAVAL** = 13|22|43

  -**MV\_FORMCRD**="CH/FI"

  -**MV\_CRDTPLC**=FI

  -**MV\_LJIDCLI**=3, o padrão é 1.

* Utilizar um servidor SITEF - informações para habilitação, contate a Software Express - **<https://www.softwareexpress.com.br/>**, ou entre em contato com o suporte no telefone (11) 3170-5353 . Para testes existe o aplicativo demo: **<https://portaldocliente.softwareexpress.com.br/distri/aplicativos/simulado/sitdemo.zip>**

* Utilizar as dlls de automação no smartclient para comunicação com o SITEF, maiores informações para download:  **[MP - SIGALOJA - Incompatibilidade de DLL com as releases 17, 23, 25 e 27](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038118953-MP-SIGALOJA-Incompatibilidade-de-DLL-com-as-releases-17-23-25-e-27)  / [MP - SIGALOJA - Homologação do SmartClient de 64 bits](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051214674)**

* **Configuração de webservice -** seguir as mesmas instruções do portal do vendedor para criação do webservice: **[MP - FAT - Configuração completa do portal do vendedor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021311972-MP-FAT-Configura%C3%A7%C3%A3o-completa-do-portal-do-vendedor).**

* **Configuração do SIGACRD (módulo 55) -** Criar o **Cartão(****CRDA130**) para venda própria e **Cadastro do cliente com dados relacionados ao perfil** (**CRDA010**)- preenchendo as informações obrigatórias das sub-abas compl.Ficha, Ref.Trabalho, Ref.Cartões, Ref.Bancárias, Ref.Pessoal da Aba Cadastral e a aba Cartões e Doc.entregue .

* **Configuração do SIGATMK (módulo 13)** :
  + **Administradora Financeira (LOJA070)** para Financiamento próprio, preenchendo os campos **AE\_FINPRO=SIM** e **AE\_PLABEL=SIM;**
  + **Cadastro de Estação (TMKA121)**, aba integrações, preencher o endereço do webservice e preencher a pergunta "**Integrar com SIGACRD**?" igual a Sim;
  + Associe o cadastro de estação ao **Grupo de Atendimento** (**TMKA040**);
  + Associe o Grupo de Atendimento ao**Cadastro de Operador**(**TMKA090**);

* Inicie o Servidor SITEF e estarte o Console do Server.ini com o job do Web Service habilitado;

* Efetue um **Atendimento Televendas** (**TMKA271**) com o tipo de operação faturamento com o cliente cadastrado para que ocorra a análise de crédito pelo SIGACRD:

![consulta_CRD_x_atendimento_TMK.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4405304074647/consulta_CRD_x_atendimento_TMK.gif)

**Observação:**

* A validação da consulta também poderá ser efetuada pelo CPF cadastrado na rotina **Cadastro do cliente com dados relacionados ao perfil** (**CRDA010**) através do botão CPF. Ou cancelar a consulta através do botão abandona.![](https://tdn.totvs.com/download/attachments/631316353/image2021-7-29_18-15-25.png?version=1&modificationDate=1627593325437&api=v2)

* Se o parâmetro **MV\_BLOQUEI** estiver ativo, o sistema não fará a análise de crédito via SIGACRD, deixe o parâmetro MV\_BLOQUEI = F para que a regra de análise de crédito seja via SIGACRD e não SIGAFAT.

Para maiores informações do processo, acesse: **[TMK0082 Integração TMK x SIGACRD](https://tdn.totvs.com/x/gR_hJQ)**
