---
article_id: 360012397592
category: RH - Arquitetura Protheus
content_hash: 714ac2686704d34b87f3492a424002d4b459759b19a0692ba4641f21a55eacc1
fetched_at: '2026-06-28T22:43:03.224530+00:00'
product: protheus
section_id: 206960847
source: central-protheus
title: MP - BD - Como efetuar a inclusão de Menu sem utilizar o SIGACFG
type: support-article
updated_at: '2019-11-22T12:14:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012397592-MP-BD-Como-efetuar-a-inclus%C3%A3o-de-Menu-sem-utilizar-o-SIGACFG
---

**Dúvida**Como efetuar a inclusão de Menu sem utilizar o **SIGACFG**?  
   
 **Ambiente**Protheus – Configurador – A partir da versão 11.80  
   
**Solução**1. Acesse a pasta **Protheus\_data/system**, e faça uma cópia da **sigagpe**:

![](http://tdn.totvs.com/download/attachments/244419369/image2016-7-21%2011%3A48%3A44.png?version=1&modificationDate=1469113104000&api=v2)

1. Defina a ordem em que será apresentado o próximo Menu, neste exemplo, o **GPEM045** e **GPEM046** foram incluídos depois do **GPEM024**- **CNIS** que fica em **Miscelanea/**  
**Cálculos.**2. Foi aplicado o comando Ctrl + F no arquivo txt e localizado o **GPEM024**;  
  
3. Os dados foram copiados conforme abaixo e alteradas algumas informações.

![](http://tdn.totvs.com/download/attachments/244419369/image2016-7-21%2011%3A53%3A10.png?version=1&modificationDate=1469113105000&api=v2)

4. Os dados copiados foram:

<MenuItem Status="Enable">  
<Title lang="pt">Cnis</Title>  
<Title lang="es">Cnis</Title>  
<Title lang="en">Cnis</Title>  
<Function>GPEM024</Function>  
<Type>01</Type>  
<Tables>SJ4</Tables>  
<Access>xxxxxxxxxx</Access>  
<Module>61</Module>  
<Owner>0</Owner>  
<KeyWord>  
<KeyWord lang="pt"> </KeyWord>  
<KeyWord lang="es"> </KeyWord>  
<KeyWord lang="en"> </KeyWord>  
</KeyWord>  
</MenuItem>  
  
5. Abaixo desta informação foram incluídos o **GPEM045** e **GPEM046**.  
A *Function* deverá ser substituída pelo código que identifica o programa;  
O *Title* deverá ser substituído pelo nome do Programa que no caso abaixo é o **Qualif. Cadastral**.  
Os itens copiados deverão ser copiados de **<MenuItem Status=Enable> até </MenuItem>**.

![](http://tdn.totvs.com/download/attachments/244419369/image2016-7-21%2011%3A54%3A57.png?version=1&modificationDate=1469113106000&api=v2)

![](http://tdn.totvs.com/download/attachments/244419369/image2016-7-21%2011%3A57%3A9.png?version=1&modificationDate=1469113109000&api=v2)

6. Acesse o **SIGAGPE**:

![](http://tdn.totvs.com/download/attachments/244419369/image2016-7-21%2011%3A57%3A49.png?version=1&modificationDate=1469113108000&api=v2)

7. A rotina será executada normalmente.
