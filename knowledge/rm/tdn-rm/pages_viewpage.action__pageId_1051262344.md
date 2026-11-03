---
content_hash: 5427e7a7ba82aba6940e87ce44d9a609d1e0b0f91d15520b3fe8f7567384dddf
fetched_at: '2026-06-29T00:05:51.569931+00:00'
page_id: '1051262344'
product: rm
source: tdn-rm
title: Utilização da Matriz SOD
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1051262344
version: 9
---

## **01. VISÃO GERAL**

A Matriz de Segregação de Funções SOD é uma ferramenta que ajuda a identificar e controlar conflitos de interesse e riscos de segurança em uma organização.

### Pré-requisitos

Para utilizar os recursos da Matriz SOD, é necessário:

1. Ter permissão no  ao menu **Serviços Globais > Segurança > Matriz SOD.**
2. Possuir o [TOTVS SmartView](https://tdn.totvs.com/display/public/TREP/SMART+VIEW) configurado no RM:  |
3. Ter acesso aos objetos de negócio abaixo conforme descrito na documentação :

* + Usuários com conflitos na Matriz SOD
  + Perfis com conflitos na Matriz SOD

## **02. CADASTROS**

Para configurar a Matriz SoD é necessário cadastrar:

**1 -** (ex: baixo, médio, alto risco)

**2 -** **Riscos** (tipo de problema identificado)

**3 -** (quais permissões não podem coexistir)

Depois disso, o sistema consegue gerar recursos como:

* **Consulta de Conflitos por usuário** → mostra usuários com acessos incompatíveis
* **Consulta de Conflitos por perfil** → mostra perfis com permissões conflitantes

## **03. IMPORTAÇÃO DOS RECURSOS**

Após cadastrar os Níveis de alerta, os Riscos e os Conflitos pelo menu **Serviços Globais > Segurança > Matriz SOD > Cadastros,** é possível visualizar os conflitos por usuário e por perfil por meio dos recursos obtidos no TOTVS Compartilhamento.

### Utilizando TOTVS Compartilhamento

No , importe os arquivos **Consulta de Conflitos por Usuários**e **Consulta de Conflitos por Perfil:**

falsePasso a PassoPasso 1Passo 1Passo 1

No , pesquise Por Recursos SmartView do produto Gestão Estratégica com o filtro "%Consulta%":

Passo 2Passo 2Passo 2

Clique em Download e importe os arquivos **Consulta de Conflitos por Usuários**e **Consulta de Conflitos por Perfil:**

Passo 3Passo 3Passo 3

Após a importação, os relatórios serão exibidos como **Visão de Dados** no **SmartView** cadastrado no ambiente.

## **04. VISUALIZAÇÃO DOS RECURSOS**

Para visualizar os resultados do cadastro, acesse o SmartView e selecione um dos recursos para visualizar a consulta correspondente:

É possível visualizar os arquivos diretamente no [TOTVS SmartView](https://tdn.totvs.com/display/public/TREP/SMART+VIEW) ou pela

### Consulta de Conflitos por Usuário

* Apresenta todos os usuários que possuem alguma permissão de menu conflitante, entre um mesmo perfil ou perfis diferentes.

### Consulta de Conflitos por Perfil

* Apresenta todos os perfis com permissão de menu conflitante.
