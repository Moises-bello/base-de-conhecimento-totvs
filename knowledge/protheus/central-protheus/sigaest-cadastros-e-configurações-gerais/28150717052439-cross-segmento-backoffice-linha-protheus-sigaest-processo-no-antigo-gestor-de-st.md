---
article_id: 28150717052439
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 37818d9870447aa6cc04c1e3996266e510fd19d9b9cbc8145701cb3c997b7c44
fetched_at: '2026-06-28T22:39:09.710147+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Processo no antigo
  Gestor de Stored Procedure
type: support-article
updated_at: '2024-12-05T19:06:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28150717052439-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Processo-no-antigo-Gestor-de-Stored-Procedure
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28150717032599) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**

Como desinstalar e instalar procedures no antigo gestor de Stored Procedure?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todos os Módulos - Todas as versões

**Solução**Abaixo indicamos como eram realizados os processos de Instalação de Stored Procedures no antigo Gestor de Stored Procedure, lembrando que nos Releases mais atuais do Protheus é utilizado o [Novo Gestor de Stored Procedures (CFGX051M).](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009382821-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Novo-Gestor-de-Stored-Procedures-CFGX051M)

Acesse também: [Stored Procedures utilizadas no produto Estoque e Custos](https://tdn.totvs.com/x/wi3AFQ)

**Processo no antigo gestor de Stored Procedure:**

**1° Passo** - Baixá-los do Portal do Cliente:

Realize os filtros para localizar o pacote de Procedures. Checar também na coluna Data para buscar o pacote mais atual:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28150717034135)

**2° Passo** - Reinicie os serviços do Protheus (appserver e dbacess), seja via Serviços do Windows ou via Monitor;

**3° Passo** - Acesse a opção de menu **Base de Dados >****Dicionario > Stored Procedure > (CFGX051)**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28150717035799)**

**4° Passo** - Caso estejam instaladas, devemos desinstalar primeiro, selecionando a opção "Desinstalar" e a Procedure que deseja desinstalar

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28150721825687)

**5° Passo** - Após desinstalar as Procedures, faça uma cópia de segurança (*backup*) dos arquivos das Procedures existentes na pasta *System* (os arquivos vem com nomenclatura **p12\_01.sps, p12\_02.sps, p12\_03.sps,** até a **p12\_24.sps**).

**6° Passo** - Copie o novo pacote de Stored Procedures baixadas na pasta *System;*

**7° Passo** - Volte ao Configurador, no menu **Base de Dados >****Dicionario > Stored Procedure > (CFGX051)**da mesma forma que o passo 3;

**8° Passo** - Escolha a opção "Instalação" e dê um **Ok**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28150721829655)**

**9° Passo** - Selecione a(s) Procedure(s) que irá instalar

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28150721831575)**

**10° Passo** - Selecione a Empresa ou Grupo e confirme

**![](http://tdn.totvs.com/download/attachments/364916162/image2018-5-22_14-9-16.png?version=1&modificationDate=1527465883000&api=v2)**

**11° Passo** - As Procedures serão compiladas em seu Banco de Dados

![](http://tdn.totvs.com/download/attachments/364916162/image2018-5-22_14-10-25.png?version=1&modificationDate=1527465883000&api=v2)

**12° Passo** - Por fim, a mensagem de sucesso.

![](http://tdn.totvs.com/download/attachments/364916162/image2018-5-22_14-11-6.png?version=1&modificationDate=1527465883000&api=v2)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*

[Instalando pacotes de Stored Procedures](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28150721529623-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Instalando-pacotes-de-Stored-Procedures)

[Desinstalando pacotes de Stored Procedures](Desinstalando%20pacotes%20de%20Stored%20Procedures)
