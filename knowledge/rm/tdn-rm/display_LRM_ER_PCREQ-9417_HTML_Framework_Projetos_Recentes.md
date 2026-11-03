---
content_hash: a69d2e454fa2f549cef565eb46ed8d18b6e36fe218d3667ad6433a4564b81371
fetched_at: '2026-06-29T00:06:24.321707+00:00'
page_id: '224116648'
product: rm
source: tdn-rm
title: ER_PCREQ-9417_HTML_Framework_Projetos_Recentes
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-9417_HTML_Framework_Projetos_Recentes
version: 135
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Projetos |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP010 | **IRM1** | PCREQ-5330 |
| **Requisito1** | PCREQ-9417 | **Subtarefa1** | PDR\_CP\_TOP010-55 |
| **Chamado2** | Não se aplica. | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | Pré-Requisitos para melhor entendimento da especificação:   | Módulo | Link | | --- | --- | | Projetos | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Projetos.aspx> | | TOTVS HTML Framework |  | | Experiência de Uso #8 | <http://tdn.totvs.com.br/pages/releaseview.action?pageId=185761509> | | Fluig | <http://dev.fluig.com/> | | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Apresentar os Projetos mais recentes, ou seja, os últimos projetos utilizados pelo usuário na visão de mudança de contexto e na barra de projeto das páginas HTML do TOTVS Obras e Projetos.

## Definição da Regra de Negócio

### 1. Projetos Recentes no Desktop

Design Thinking é o conjunto de métodos e processos para abordar problemas, relacionados à aquisição de informações, análise de conhecimento e propostas de soluções. Criatividade para geração de soluções e razão para analisar e adaptar as soluções para o contexto. WikipédiA, A enciclopédia livre. Disponível em: <<http://pt.wikipedia.org/wiki/Design_thinking>> Acesso em 4 de fevereiro de 2016.

No TOTVS Obras e Projetos, ambiente Desktop, foi criado um anexo associado a visão de projetos que exibe os últimos projetos acessados pelo usuários permitindo a escolha.

Após o acesso a um projeto, é disponibilizado no menu do sistema a opção de acesso aos últimos projetos para facilitar ao usuário a troca de projetos.

No anexo de últimos projetos e no menu de acesso rápido, são exibidos os últimos 7 projetos.

### 2. Projetos Recentes na Web

Será aplicado também o conceito de Design Thinking feito na versão em Desktop do produto para o ambiente Web na páginas HTML do TOTVS Obras e Projetos.

Nas páginas existe um botão para escolher o contexto de informações para serem aplicados e utilizados nas páginas: escolher ou alterar uma coligada ou um projeto, por exemplo.

Será exibido um campo para escolher os projetos que o usuário tem acesso. O campo possui a funcionalidade de filtrar os projetos pelo código ou descrição facilitando assim encontrar o projeto.

Logo abaixo desse campo será exibido uma lista com os 7 últimos projetos recentes, ou seja, os projetos que foram abertos por último pelo usuário.

Essa lista irá conter as seguintes informações do Projeto ordenados pela data de acesso mais recente para a mais antiga:

* + Código;
  + Descrição;
  + Nome da Fase;
  + Código Auxiliar;
  + Número da Revisão;
  + Data e hora do último acesso

Ao clicar no Código ou Descrição do Projeto, o sistema automaticamente realiza o acesso ao mesmo obedecendo todas as regras para acesso aplicadas no processo atual.

Vide Protótipo 01.

### 3. Acesso Rápido aos Projetos Recentes

Além da página de acesso a troca de projeto no contexto, na barra de projeto, que é exibido em quase todas a páginas HTML do TOTVS Obras e Projetos, será criado um campo onde o usuário poderá trocar de projeto escolhendo os projetos que ele tem acesso.

Será mostrado primeiro neste campo, que é uma lista de projeto, os projetos mais recentes ordenado pela data de último acesso e posteriormente os outros projetos ordenados pelo código.

O projeto corrente será exibido em destaque na barra.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Página de Seleção de Contexto | Alteração | RM Web -> Projetos | Clicar no botão de seleção de contexto para exibir a página. |
| Diretiva da Barra de Projeto | Alteração | RM Web -> Projetos | Seleção de Projetos através da barra de Projeto |

***Tabelas Utilizadas***

* *MPRJUSRACESSO – Acesso de Usuários a Projetos*

## Protótipo de Tela

### **Protótipo 01 - Tela de seleção de contexto do Projeto**

### **Protótipo 02 - Escolha do Projeto pela barra de Projeto**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
