---
content_hash: edf85abe79bfe59e978de03d7c69854304b03a32c31100bc997af9bd92a5ffa0
fetched_at: '2026-06-28T21:35:24.413364+00:00'
page_id: '269422853'
product: fluig
source: tdn-fluig
title: Certificado HTTPS (SSL/TLS) Gratuito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269422853
version: 7
---

# Índice

4true.\*ndicenone

# Objetivo

---

O objetivo deste artigo é apresentar uma forma de obter o certificado HTTPS gratuito. A **Let’s Encrypt** (<https://letsencrypt.org>) é uma autoridade certificadora aberta, gratuita e automática. São membros da Linux Foundation e foram criados com o intuito de trazer mais segurança e privacidade à internet. Entre os principais apoiadores hoje destacam-se Cisco, Akamai, Google, Facebook, Mozilla, HP e outros destes porte.

O certificado é **válido por 60 dias**, porém a renovação pode e deve ser **automatizada**.

## Como Funciona

---

A Let's Encrypt utiliza um protocolo denominado ACME (*Automatic Certificate Management Environment*). Em resumo, se baseia num conjunto de pedidos ou desafios para o servidor *web* que contém o certificado. A validação do domínio é realizada com base nas respostas e garantida pelo uso de um par de chaves. Para tanto é necessário um cliente ACME no servidor que será consultado pela autoridade certificadora (AC). Para mais informações [clique aqui](https://github.com/ietf-wg-acme/acme/).

Após isto, para as solicitações de renovação e revogação dos certificados, basta o servidor enviar mensagens de gerenciamento de certificado e assiná-las com o par de chaves válido. Para obter um certificado, o *client* gera um PKCS e envia à Let’s Encrypt solicitando a emissão de um certificado para o(s) domínio(s), utilizando a chave pública informada.

## Como utilizar

---

A Let's Encrypt possui uma lista de dezenas de clientes e APIs para automatizar a geração, configuração e renovação dos certificados.

Abaixo iremos demonstrar um deles em ambiente Linux CentOS e utilizando o cliente Certbot, que é recomendado pela Let’s Encrypt. Para outros sistemas operacionais ou aplicações, consulte o site da [Certbot](https://certbot.eff.org/) ou o guia da [Let's Encrypt](https://letsencrypt.org/getting-started/).

Não é necessário nenhum cadastro prévio.

### Em ambiente Linux (CentOS ou derivados) + Apache

**Instalação Certbot:**

bash

**Usando em modo *webroot*:**

bash

**Renovando o certificado:**

Adicionar o comando ao crontab para ser executado semanalmente.

bash

**Saiba Mais**  
Em caso de dúvidas, mais informações podem ser encontradas em:

* **[Let’s Encrypt: https://letsencrypt.org/](https://letsencrypt.org/getting-started/)**
* **CertBot** (Cliente recomendado): **<https://certbot.eff.org/>**
* [Configuração HTTPS da plataforma](http://tdn.totvs.com/x/vdMgFQ)
