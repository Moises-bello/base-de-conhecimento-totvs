---
content_hash: b809bca32d00173f5588f2a504629103a967014b72ec2a76da610120504f80b2
fetched_at: '2026-06-29T00:11:06.298903+00:00'
page_id: '633320979'
product: rm
source: tdn-rm
title: Portal de Imóveis - Wizard de Instalação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=633320979
version: 6
---

### Introdução

---

A partir da versão 12.1.33, o wizard de instalação do Portal de Imóveis foi modificado, simplificando a instalação do portal e a configuração dos bancos de dados e webservices RM.

### **Etapas do Wizard**

---

##### Passo 1: Sobre o instalador

---

Esta etapa é apenas uma introdução que resume os procedimentos que deverão ser executados

##### Passo 2: Informar conexão com WebService e API TOTVS

---

Neste momento deveremos definir o caminho público da URL dos webservices TOTVS que serão consumidos pelo Portal de Imóveis.

* **Informe a URL do WebService TOTVS**: Endereço do webservice. Exemplo: *[http://url:porta/wsDataServerPVI/MEX?wsdl](http://localhost:8051/wsDataServerPVI/MEX?wsdl)*
* **Informe a URL da API REST TOTVS:** Endereço da API Rest. Exemplo: *[http://url:porta/](http://localhost:8051/wsDataServerPVI/MEX?wsdl)*
* **Usuário**: Usuário de acesso ao webservice;
* **Senha**: Senha do usuário

##### Passo 3: Informar os dados do banco de dados

---

Nesta etapa iremos configurar os dados do banco onde o Portal de Vendas de Imóveis será instalado

* **DBMS:** MySql ou SQLServer;
* **Servidor:** Selecionar o IP ou IP/Instância;
* **Porta:** Usar a padrão do DBMS ou a definida no DBMS;
* **Nome do Banco de Dados:** Por padrão o nome do banco de dados default é o Portal de Imóveis podendo ser alterado;
* **Usuário do Banco do Portal de Imóveis:** Usuário de acesso do banco de dados;
* **Senha do Banco do Portal de Imóveis:** Senha de acesso do usuário.

##### Passo 4: Restaurar o banco de dados

---

Este passo irá avançar automaticamente assim que o banco for restaurado no endereço definido no passo 3.

##### Passo 5: Instalação concluída

---

Apenas um informativo com as configurações de login para o primeiro acesso no Portal de Imóveis.
