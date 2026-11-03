---
content_hash: 78394f5ab8d561133cd47c5cfe7abe2bb7ecabfb886271e1a3444f84c28d2e4a
fetched_at: '2026-06-29T00:06:00.346772+00:00'
page_id: '196053421'
product: rm
source: tdn-rm
title: ER_PCREQ-6033_HTML_Framework_Diario_de_Projeto
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-6033_HTML_Framework_Diario_de_Projeto
version: 19
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### 

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Projetos |
| **Segmento Executor** | Construção & Projetos | | |
| **Projeto1** | R\_C&P\_TOP007 | **IRM1** | PCREQ-6032 |
| **Requisito1** | PCREQ-6033 | **Subtarefa1** | PDR\_CP\_TOP008-131 |
| **Chamado2** | Não se aplica. | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** | Não. |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | Pré-Requisitos para melhor entendimento da especificação:  TOTVS HTML Framework -  Fluig - <http://tdn.totvs.com/display/public/fluig/Sobre+o+Fluig>  Projetos - <http://wikihelp.totvs.com.br:1210/WikiHelp/PRJ/PRJ.Projetos.aspx>  Diário de Projeto - <http://wikihelp.totvs.com.br:1210/WikiHelp/PRJ/PRJ.DiarioProjeto.aspx> | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 Migração da funcionalidade de Diário de Projeto para o ambiente Fluig utilizando o TOTVS HTML Framework.

## Definição da Regra de Negócio

### **TOTVS HTML *Framework***

O TOTVS | HTML *Framework* foi concebido para tratar apenas a camada de interface das aplicações, confiando que os produtos por trás da interface irão conceder a infraestrutura e a implementação mínima dos serviços para utilização do *framework*. 

Ela tem como objetivo:

* + Fornecer uma Infraestrutura de componentes visuais e de serviços (de interface) HTML5;

* + Prover uma IDE de desenvolvimento HTML5, baseada no TDS ([TOTVS Developer Studio](http://ds.totvs.com/));

* + Disponibilizar um Template de CRUD responsivo com respectivo acelerador no TDS, baseado em Serviços providos pelos produtos;

* + Estruturar um ambiente de desenvolvimento compatível com o Fluig e que possa ser utilizados por todos os produtos TOTVS.

A arquitetura pode ser resumida de acordo com a imagem a baixo:

Mais informações sobre o TOTVS HTML Framework: 

### Fluig

No mundo dos negócios, onde as empresas precisam ter controle sobre suas operações e, ao mesmo tempo, agilidade para atender aos diversos processos que acontecem simultaneamente, a forma de interação mudou. A comunicação e os procedimentos são determinados, mas não rígidos, e a única constância é justamente a mudança e tudo precisa estar em nossas mãos.

Entendendo a mudança no comportamento dos indivíduos no ambiente corporativo e as demandas tecnológicas, a TOTVS criou a plataforma fluig com o objetivo de centralizar em uma única tela todos os processos, documentos e sistemas com um único login em uma interface de comunicação colaborativa.

Em resumo Fluig é uma plataforma de produtividade e colaboração que unifica a gestão de processos, documentos e identidades.

Mais informações sobre o Fluig nos links:

* <http://tdn.totvs.com/display/public/fluig/Sobre+o+Fluig>
* <http://www.fluig.com/>

### Diário do Projeto

O diário de projeto, também conhecido como diário de obra, é um documento usado para registrar informações importantes sobre cada dia de atividade do projeto.

É uma espécie de memorial da obra. Nele, é anotado tudo o que aconteceu de importante no projeto em um determinado dia:

* + Os serviços feitos
  + Os equipamentos utilizados - e por quantas horas
  + As condições do clima, etc.

E, se necessário, também podem ser descritos no diário os problemas na execução de serviços, falhas nos equipamentos, etc.

O diário de projeto é importante, pois ele conta, dia a dia, a história do projeto ao longo de todo seu período de execução.

No TOTVS Obras e Projetos a funcionalidade de Diário de Projeto está localizado no seguinte caminho: Construção e Projetos -> Controle -> Diário de Projeto.

#### Migração

Para a funcionalidade de Diário de Projeto do TOTVS Obras e Projetos serão desenvolvidas telas Web utilizando o TOTVS HTML Framework.

Uma vez que as telas Web forem desenvolvidas, estas serão inserida na plataforma Fluig para que o usuário possa ter um acesso mais ágil e prático da funcionalidade.

Serão desenvolvidas três telas para o Diário de Projeto e mais três telas para o cadastro de Classificação do Diário de Projeto da seguinte forma:

* + Tela com a listagem dos itens salvos na base de dados com opções para Adicionar, editar, visualizar e excluir um registro;
  + Tela com os detalhes de um registro;
  + Tela com um formulário para Adicionar ou Editar um registro.

Na tela de listagem do Diário de Projeto serão mostradas as seguintes informações: Código e Descrição do Projeto, Data, Assunto (novo campo),Código e Descrição da Classificação, Código, Nome e Descrição da Tarefa e a Ocorrência (vide Protótipo 1).

Ainda na listagem do Diário de Projeto ao clicar no link "Exibir detalhes...", serão mostrados todos os documentos associados ao Diário do Projeto com as opções de Download do mesmo.

Haverá um campo para pesquisar pelo campo assunto ou ocorrência do Diário. Terá também uma busca avançada onde poderá pesquisar por um intervalo de data e ocorrências.

A tela de Adicionar ou Editar um registro para o Diário de Projeto irá conter os seguintes campos: Data (obrigatório), Assunto, Classificação, Tarefa e a Ocorrência (obrigatório) (vide Protótipo 2).

Quando o usuário estiver editando um Diário de Projeto haverá um Anexo de Documentos listando todos os documentos associados ao Diário. Terá a opção de Inserção, Edição e Download dos documentos.

A tela de Detalhes de um registro do Diário de Projeto irá conter as mesmas informações da listagem porém especifica para um registro (vide Protótipo 3).

Na tela de listagem de Classificação de Diário de Projeto serão mostradas as seguintes informações: Código e Descrição da Classificação (vide Protótipo 4).

Haverá um campo para pesquisar os registros pelo código ou descrição da Classificação.

A tela de Detalhes da Classificação irá conter as mesmas informações supracitadas específica para um registro (vide Protótipo 5).

A tela de Adicionar ou Editar a Classificação irá conter os seguintes campos: Código e Descrição da Classificação e ambos obrigatórios (vide Protótipo 6).

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Diário de Projeto | Envolvida | Construção e Projetos -> Controle -> Diário de Projeto -> Cadastro | - |
| Classificação de Diário de Projeto | Envolvida | Construção e Projetos -> Controle -> Diário de Projeto -> Classificação | - |

***Tabelas Utilizadas***

* *MPRJDIARIO – Diário de Projeto*
* *MCLASSDIARIO - Classificação de Diário de Projeto*
* *MTRF - Planilha de Atividades*

## Protótipo de Tela

### **Protótipo 1**

### **Protótipo 2**

### **Protótipo 3**

### **Protótipo 4**

### **Protótipo 5**

### **Protótipo 6**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
