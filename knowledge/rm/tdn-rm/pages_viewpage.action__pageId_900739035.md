---
content_hash: 776616005b3b1c01af574a8deb32da4d2a6c6c1bee1263fc202023d27e12313b
fetched_at: '2026-06-29T00:12:02.357589+00:00'
page_id: '900739035'
product: rm
source: tdn-rm
title: Integração SmartView
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=900739035
version: 17
---

A integração com SmartView tem como objetivo fornecer maior flexibilidade para a visualização das informações através de Visão de Dados, Tabelas Dinâmicas e relatórios.

Requisitos Técnicos

Para que a integração entre o TOTVS Inteligência Tributária e o SmartView funcione, é necessário que o mesmo esteja devidamente configurado. Para isso basta seguir os tutoriais disponíveis em:  e .  
Detalhes adicionais disponível em: [Instalação SmartView - Base de conhecimento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13311540250007-Cross-Segmentos-Backoffice-RM-BI-Instala%C3%A7%C3%A3o-Smart-View)

# Índice

1. [Recursos disponíveis](https://tdn.totvs.com/pages/viewpage.action?pageId=900739035#recursos-disponiveis)
2. [Seleção de Recursos](https://tdn.totvs.com/pages/viewpage.action?pageId=900739035#selecao-recursos)
3. [Visualização dos dados](https://tdn.totvs.com/pages/viewpage.action?pageId=900739035#visualizacao-dados)

# Recursos disponíveisrecursos-disponiveis

## Padrão

Por padrão nós disponibilizamos um conjunto de recursos (Visões de dados) já configurados para o RM/SmartView contendo as mesmas informações disponíveis no TOTVS Inteligência Tributária.

Para utilizar esses recursos padrão siga o tutorial do [TOTVS Compartilhamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8876331402775-Framework-Linha-RM-Frame-TOTVS-Compartilhamento) e o .

Lista de recursos disponíveis

* FISTRP0019 - TOTVS Inteligência Tributária - Detalhamento das Operações por Participante
* FISTRP0020 - TOTVS Inteligência Tributária - Detalhamento das Operações por NCMNBS
* FISTRP0022 - TOTVS Inteligência Tributária - Detalhamento dos Débitos de ICMS
* FISTRP0023 - TOTVS Inteligência Tributária - Detalhamento dos Créditos de ICMS
* FISTRP0024 - TOTVS Inteligência Tributária - Detalhamento dos Ajustes de Apuração do ICMS
* FISTRP0025 - TOTVS Inteligência Tributária - Detalhamento das Operações do ISS
* FISTRP0026 - TOTVS Inteligência Tributária - Detalhamento de débitos do PIS/COFINS
* FISTRP0027 - TOTVS Inteligência Tributária - Detalhamento de créditos do PIS/COFINS
* FISTRP0028 - TOTVS Inteligência Tributária - Detalhamento de débitos de IPI
* FISTRP0029 - TOTVS Inteligência Tributária - Detalhamento de créditos de IPI
* FISTRP0030 - TOTVS Inteligência Tributária - Detalhamento dos Ajustes de Apuração do IPI

## Customizado

É possível criar recursos do SmartView com os mesmos objetos de negócio utilizados nos recursos padrões, sendo eles:

Lista de objetos de negócio disponíveis

* TOTVS Inteligência Tributária - Operações por Participante
* TOTVS Inteligência Tributária - Operações por NCM/NBS
* TOTVS Inteligência Tributária - Crédito/Débito do ICMS
* TOTVS Inteligência Tributária - Ajustes da Apuração do ICMS
* TOTVS Inteligência Tributária - Detalhamento das Operações do ISS
* TOTVS Inteligência Tributária - Crédito/Débito de PIS/COFINS
* TOTVS Inteligência Tributária - Crédito/Débito do IPI
* TOTVS Inteligência Tributária - Ajustes da Apuração do IPI

Após a criação do recurso no SmartView é necessário vinculá-lo no RM, através do tutorial

Requisito Monitor Tributário

Para que o recurso fique disponível dentro do TOTVS Inteligência Tributária, durante a inclusão dentro do RM é necessário que sejam informados **TOTVS Gestão Fiscal**para o campo **Aplicação (Obrigatório)** e o **331 - D - Monitor Tributário** para o campo **Tipo (Obrigatório)**, conforme imagem abaixo:

---

# Seleção de Recursosselecao-recursos

Para exibir os dados no SmartView basta clicar na opção **ABRIR NO SMART VIEW**, como destacado na imagem abaixo:

*(Clique na imagem para ampliar.)*

Após selecionar a opção **ABRIR NO SMART VIEW** irá abrir uma tela com todos os recursos disponíveis para utilização (todos os recursos inclusos no RM com o tipo **331 - D - Monitor Tributário**), conforme imagem abaixo:

*(Clique na imagem para ampliar.)*

Basta selecionar o recurso que queira utilizar e clicar em **Abrir no Smart View**

---

# Visualização dos dadosvisualizacao-dados

## Parametrização do recurso

Os filtros ativo no TOTVS Inteligência Tributária serão utilizados no recurso selecionado.

No exemplo ao lado, o recurso selecionado irá conter a coligada 17 - EFD - CONTRIBUIÇÕES e suas filiais e o período de um ano (01/2024 - 01/2025).

*(Clique na imagem para ampliar.)*

Para utilizar o Smart View, após a seleção do recurso irá abrir uma tela com o nome do recurso e um botão **Enviar.**Os parâmetros estão pré-definidos como demonstrado acima.

Basta clicar no botão **Enviar** e será carregado as informações.

*(Clique nas imagens para ampliar.)*
