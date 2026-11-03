---
content_hash: 63ea01d1bb2566ac87b6a28e0167f6d32689388716da3e5665126f82e2b3421b
fetched_at: '2026-06-29T00:06:09.775473+00:00'
page_id: '203757153'
product: rm
source: tdn-rm
title: ER_PCREQ -6545_SAÚDE_CIH_FLUIG_12.1.9_VALIDAÇÕES AUTOMÁTICAS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=203757153
version: 1
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS CIH | **Módulo** | MENU LATERAL |
| **Segmento Executor** |  | | |
| **Projeto1** | SAÚDE\_CIH\_FLUIG\_12.1.9 | **IRM1** | * [PCREQ-6530](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-6530 "PCREQ-6530") |
| **Requisito1** | * [PCREQ-6545](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-6545 "PCREQ-6545") | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** |  | **Réplica** |  |
| **País** | (X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### Objetivo

As validações automáticas têm como principal objetivo, unificar e automatizar as seguintes rotinas:

* Compilador de Hemocultura: Agrupar os resultados de hemoculturas do mesmo paciente.
* Atualizar IRIC: Índice de Risco de Infecção Cirúrgica
* Atualização de multiresistência de germe: o CIH deverá verificar toda a alteração que ocorrer no cadastro de antibióticos e e atualizar a informação de multirresistência no cadastro de Germes.
* Validação das Informações do Prontuário: Cada importação realizada pela CIH, os dados do paciente e os demais cadastros são atualizados. Ao executar a validação das informações automáticas, o CIH deverá alterar o status da importação para Ok.

### Definição da Regra de Negócio

* Compilador de hemocultura: A cada importação realizada - de acordo com a parametrização - o CIH deve agrupar todos os resultados de Hemoculturas realizados pelo paciente e apresentar um único número consolidando as amostras.
* Atualizar o IRIC: A cada importação realizada ou alteração no Prontuário do Paciente, o CIH deve atualizar o cálculo do IRIC. Este cálculo utiliza os seguintes fatores: Risco Cirúrgico, Tempo de Ferida Aberta e Tipo de Ferida.

 

Sendo assim:

 

IRIC 0 = se os três fatores de risco estiverem ausentes;

 

IRIC 1 = se apenas um dos fatores de risco for presente e os outros ausentes

 

IRIC 2 = se dois fatores forem presentes e o outro for ausente;

 

IRIC 3 = se os três fatores de risco forem presentes.

 

* Multiresistência de Germe: Sempre que o campo Multiresistência for atualizado e um antibiótico for incluído no cadastro de Germes (Cadastros > Germes)  o CIH deverá verificar todos os pacientes que possuírem no resultado de Cultura Final o mesmo Germe e incluir no campo Multiresistência a opção **Sim.**
* Validação informações Prontuário Paciente: Em algumas importações realizadas, as informações do Prontuário do Paciente ficam em branco, neste momento o campo **Status da Importação** deste registro fica com a cor vermelha, informando que não está completo. A validação das informações do Prontuário do Paciente servirá para que o CIH deixe todos os Status de Importação **Verdes,** mas não alterará as informações cadastrais. Ou seja, os campos que não foram importados continuarão sem preenchimento.

 

## Protótipo de Tela

### Fluxo do Processo

### 

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
