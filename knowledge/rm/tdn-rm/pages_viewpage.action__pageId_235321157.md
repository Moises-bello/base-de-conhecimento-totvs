---
content_hash: cfa5c7733efc09ec230b8c7e3054df186dad92356a9768b958c1655c3a4a7ff4
fetched_at: '2026-06-29T00:08:03.428340+00:00'
page_id: '235321157'
product: rm
source: tdn-rm
title: ER_PCREQ-10748_Lançamento_em_conta_da_taxa_de_sala
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235321157
version: 118
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | RM SAÚDE |
| **Projeto** | * [R\_SAU\_RM\_V12\_1516](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_SAU_RM_V12_1516 "R_SAU_RM_V12_1516") | **IRM** | * [PCREQ-10747](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-10747 "PCREQ-10747") |
| **Requisito** | * [PCREQ-10748](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10748 "PCREQ-10748") | **Subtarefa** | * [SAU\_DEV-4553](http://jira.totvs.com.br/browse/SAU_DEV-4553) |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

   Este documento tem como objetivo a especificação da funcionalidade de "Lançamento automático de Taxa de Sala Cirúrgica", no registro de informações cirúrgicas.

 

## Definição da Regra de Negócio

**RN001**

* No cadastro das "Condições Contratuais com Convênios", será criado um checkbox de nome "Utiliza Cobrança de Taxa de Sala Cirúrgica", cujo valor default deverá ser = false;
* Será adicionado um campo texto, onde deverá ser informado o tempo de tolerância para cobrança da próxima 1/2 hora, onde o valor máximo aceito deverá ser 30;
* Também serão adicionados ao formulário 2 lookups, que serão responsáveis por armazenar a taxa que será cobrada pela primeira hora da cirurgia e de cada 1/2 hora subsequente.

**RN002**

* No formulário de Registro de Informações de Cirurgias, será alterada a rotina de finalização, para que, no momento em que for finalizado, o seguinte fluxo seja executado:1 - Sistema verificará na condição contratual vigente se está sendo utilizada a cobrança de taxa de sala;  
  2 - Caso esteja sendo utilizada irá lançar na conta do paciente o valor da primeira hora;  
  3 - Após o lançamento da primeira hora, o sistema verificará quantos períodos de 1/2 hora ocorreram após a primeira hora, sendo que o ultimo período também deverá contar, mesmo que não complete 1/2 hora;  
  4 - O sistema então verificará se o último período está dentro do tempo de tolerância configurado. Caso positivo, deverá cobrar todos os períodos, conforme o preço configurado, caso negativo, não deverá cobrar pelo último.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [Condições Contratuais com convênios] | [Alteração] | [Cadastros > Faturamento > Condições Contratuais com Convênios] | **RN001** |
| [Registro de informações de Cirurgias] | [Alteração] | [Cuidados com o Paciente > Centro Cirúrgico > Registro de Informações Cirúrgicas] | **RN002** |

**Exemplo de Aplicação*:***

* Acesse o menu "Cadastros > Faturamento > Condições Contratuais com Convênios" e selecione a condição contratual desejada;
* Acesse a aba "Parâmetros 3" e, na parte inferior do formulário, preencha as informações referentes a Taxa de Sala Cirúrgica;
* Acesse o menu "Cuidados com o Paciente > Centro Cirúrgico > Registro de Informações Cirúrgicas" e inclua um novo registro;
* Informe o tempo de Sala correspondente, preencha as informações obrigatórias e salve o registro;
* Ainda no mesmo registro, clique em "Processos > Enviar Dados Para Faturamento";
* Na tela que abre, clique em "Executar";
* Acesse a elaboração de contas (Ctrl+l) e verifique se o lançamento da taxa de primeira hora, e a quantidade de taxas de 1/2 hora subsequentes estão de acordo com o parametrizado.

## Protótipo de Tela

**Protótipo 01**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
