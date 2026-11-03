---
content_hash: 3c177a3432e468d1c1ae76e89a3657ca2f003e032e5693e1d42882ab8a80e66e
fetched_at: '2026-06-29T00:10:46.823053+00:00'
page_id: '556378814'
product: rm
source: tdn-rm
title: API/PO-UI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=556378814
version: 2
---

# Introdução

A partir da versão 12.1.29 é possível criar um Metadados para utilizá-lo via Web API e, inclusive, ter o layout integrado com componentes do [PO-UI](https://po-ui.io/documentation/po-dynamic-form). O objetivo desta documentação é dar um passo a passo de como criar um projeto de Metadados para API.

Documentação API

Para mais informações sobre o acesso e utilização das APIs de Metadados, acesse .

# Passo a passo

Segue o passo a passo de como criar um projeto metadados para API.

## 1. Modelo de Negócio

Ao abrir para cadastrar um novo modelo de negócio, será exibido a caixa com a opção "Web API / PO-UI". Caso esta caixa seja marcada, o modelo e todas as apresentações e projetos associados ao mesmo serão considerados do tipo API.

## 2. Apresentação de formulários

Ao criar uma apresentação com um Modelo de Negócio do tipo API, não será possível adicionar Actions Anexas e Processos, apresentando um erro conforme imagem abaixo:

Lookup

Os recursos Lookup (caixa de pesquisa) e os eventos OnValidate também estão disponíveis para acesso via API.

## 3. Geração do projeto

Ao criar um projeto relacionado a uma apresentação para API, serão exibidos apenas os menus "customização" e os menus de aplicações API/PO-UI.

Para acessar o projeto gerado por dentro do RM basta utilizar o Executar, na barra lateral direita.

# Conclusão

Como foi visto, poucas alterações são necessárias para criar um projeto Metadados API, que se torna disponível na . Com exceção do que foi apresentado aqui, a utilização dos Metadados segue da mesma forma.
