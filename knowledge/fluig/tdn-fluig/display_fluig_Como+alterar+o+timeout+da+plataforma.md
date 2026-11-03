---
content_hash: 41115648d7d21c34486cf396d628753f0007e43aadb30cbda8c088a7858220e4
fetched_at: '2026-06-28T21:35:19.189731+00:00'
page_id: '198939868'
product: fluig
source: tdn-fluig
title: Como alterar o timeout da plataforma
type: documentation
url: https://tdn.totvs.com/display/fluig/Como+alterar+o+timeout+da+plataforma
version: 17
---

Fique atento!

Esta página foi revisada para considerar as configurações do TOTVS Fluig **a partir** da atualização **1.6**.

4.\*ndice

# Objetivo

---

Este guia visa mostrar o procedimento para aumentar o *timeout* na execução de processos que contenham formulários com *datasets*, atividades de serviço, entre outros.

# Como alterar o *timeout*

---

Para aumentar o *timeout* da plataforma, siga os passos descritos abaixo.

Atenção!

A realização deste procedimento pode causar problemas de performance na plataforma. Recomendamos que seja realizado em ambiente de homologação antes de configurar em produção.

falseExemplos2A partir da 2.0

**01.** Pare os serviços do Fluig.

**02.** Edite o arquivo **standalone.xml**, que está disponível em [diretório\_instalação]/appserver/standalone/configuration, alterando o parâmetro **<coordinator-environment default-timeout="300"/>** dentro do subsystem **jboss:domain:transactions:5.0** para o valor que desejar. Se não houver o parâmetro, basta adicionar.

standalone.xml



    
 
 
 
 
]]>

**03.** Salve as alterações.

**04.** Inicie os serviços do Fluig na ordem correta.

11.7 até 1.8.2

**01.** Pare os serviços do Fluig.

**02.** Edite o arquivo **domain.xml**, que está disponível em [diretório\_instalação]/appserver/domain/configuration, alterando o parâmetro **<coordinator-environment default-timeout="300"/>** dentro do subsystem **jboss:domain:transactions:5.0** para o valor que desejar. Se não houver o parâmetro, basta adicionar.

xmlEclipsedomain.xml



    
 
 
 
 
]]>

**03.** Salve as alterações.

**04.** Inicie os serviços do Fluig na ordem correta.

3Até a 1.6.5

**01.** Pare os serviços do Fluig.

**02.** Edite o arquivo **domain.xml**, que está disponível em [diretório\_instalação]/appserver/domain/configuration, alterando o parâmetro **<coordinator-environment default-timeout="300"/>** dentro do subsystem **jboss:domain:transactions:3.0** para o valor que desejar. Se não houver o parâmetro, basta adicionar.

xmlEclipsedomain.xml





 

]]>

**03.** Salve as alterações.

**04.** Inicie os serviços do Fluig na ordem correta.

Após realizar esse procedimento, o *timeout* da plataforma será alterado conforme o parâmetro definido.
