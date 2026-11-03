---
content_hash: d373ad46ce0c30725cdac5569013725aaf464e6de32ad61fb61044addfb836e8
fetched_at: '2026-06-29T00:08:34.916153+00:00'
page_id: '274852505'
product: rm
source: tdn-rm
title: Gerando Certificado SSL
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerando+Certificado+SSL
version: 13
---

# Índice

---

.\*ndice:

# Objetivo

---

        O objetivo deste documento é mostrar a geração de um certificado SSL e como configurá-lo para ser utilizado no Portal Web (Totvs - Gestão de Conteúdo).

# Introdução

---

        O **certificado SSL** uma vez configurado possibilitará que o tráfego de informações na rede sejam criptografados.

       Este recurso é nativo do próprio Windows, em caso de informações mais técnicas as mesmas poderão ser adquiridas através do site da Microsoft.

Importante

A configuração de certificado de segurança **SSL** ou **TLS** obedecem os mesmos passos de configuração demonstrados neste documento. Ambos são protocolos que conferem segurança de comunicação na Internet.

Configuração:

**Não** prestamos suporte à este tipo de configuração por se tratar de ajuste de ambiente, o documento serve apenas como guia. Para tanto, é necessário o auxílio de um Web Master.

# Passos para gerar o certificado

---

        A seguir estão os passos para gerar o certificado. Clique sobre as imagens para ampliá-las.

falsePasso a PassoPasso 1Passo 1Passo 1

1. Selecione a página inicial do IIS;
2. Selecione o ícone Certificados de Servidor;
3. Clique em Abrir Recurso;
4. Na página apresentada, selecione a opção: "Criar Certificado Autoassinado...".

Passo 2Passo 2Passo 2

Informe o nome para o certificado que será criado e clique em "OK".

Passo 3Passo 3Passo 3

Observe que o certificado foi gerado corretamente.

Observação:

Caso já possua um certificado emitido por um órgão certificador, basta importá-lo dentro do ISS e seguir os passos de configuração.

Ver imagem

# Passos para configurar o certificado para utilizá-lo no portal

---

        A seguir estão os passos para configurar o certificado. Clique sobre as imagens para ampliá-las.

falsePasso a PassoPasso 1Passo 1Passo 1

1. Selecione o ***DEFAULT DO WEB SITE*** e siga as orientações para adicionar as ligações do site:
2. Selecione a opção "Ligações";
3. Clique em "Adicionar";
4. Selecione "HTTPS";
5. Selecione o certificado criado;.
6. Clique em "OK" para finalizar.

Passo 2Passo 2Passo 2

Realizando a Configuração do SSL para o site criado:

1. Selecione o site que será parametrizado;
2. Selecione "Configurações de SSL";
3. Clique em "Abrir Recurso".

Passo 3Passo 3Passo 3

1. Selecione a opção "Exigir SSL";
2. Clique em "aCEITAR";
3. Selecione "Aplicar";
4. Visualize a mensagem de sucesso.

Passo 4Passo 4Passo 4

Outro procedimento a ser realizado será alterar o endereço do portal utilizando https:// (conforme a imagem abaixo):

***O endereço abaixo refere-se a um ambiente de teste para simulação deste processo (aqui na TOTVS),*** ***este endereço possivelmente será diferente do ambiente da empresa.***Passo 5Passo 5Passo 5

Após a realização desta parametrização solicito que seja reiniciado o IIS e acessar o portal para realização dos testes.

Abaixo segue exemplo para reiniciar IIS:

Após reiniciar o serviço do IIS - o processo será concluído já podendo acessar o Portal Web normalmente.

falsefalse

**Produto:** Framework

false

**Versão:** 11.XX; 12.XX

false

**Processo:** Gerar um Certificado SSL e parametrizar o mesmo para ser utilizado no *Portal WEB (TOTVS - Gestão de conteúdos)*

falsefalse

**Status:** Finalizado

false

**Data:** 19/09/2016

false

**Autores:**
