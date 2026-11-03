---
content_hash: 23491cdedb345bfa55b88315039b646572f31e793a0a233b5cd436f5d7535077
fetched_at: '2026-06-29T00:10:37.689965+00:00'
page_id: '540874711'
product: rm
source: tdn-rm
title: TOTVS Gestão Hospitalar > Atendimento > Recepção > Dados de um paciente > Anonimização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=540874711
version: 15
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Processo para anonimizar pacientes**

sumarioVisão Geral

## **01. VISÃO GERAL**

Para atender a [Lei Nº 13.709/18](http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709.htm) foi criado o processo "Anonimização" dentro do cadastro do Paciente, este processo irá alterar os campos permitidos e definidos para um valor fictício (ex: 000). 

Campos passíveis de anonimizar:

| Coluna | Descrição |
| --- | --- |
| CODRELIGIOES | Convicções religiosas |
| CONTA | Número de identificação (CPF, RG. etc.) |
| FOTO (IDIMAGEM) | Identificadores de Via Eletrônica (e-mail, etc.) |
| NOMECARTORIOCERT | Nome do paciente |
| NOMECONJUGE | Nome do cônjuge do paciente |
| NOMECONTATO | Nome de contato com o paciente |
| NOMEINDICACAO | Nome do paciente |
| NOMEPAI | Nome do pai do paciente |
| NUMTITULOELEIT | Número do título de eleitor |
| PISPASEP | Número do PIS |
| TITULARPLANO | Nome do titular do plano de saúde |

Processo para anonimizar pacientes

## **02. PROCESSO PARA ANONIMIZAR PACIENTES**

Para ter acesso ao processo é necessário que seja concedida permissão ao item de menu no perfil desejado:

O processo pode ser executado através do RM e RM Saúde, acessível através do menu citado abaixo:

Devemos selecionar um dos pacientes na lista. Após selecionar o paciente devemos selecionar a opção anonimização, que fica na guia de processos, vide imagem abaixo:

O processo será executado em segundo plano e seu resultado poderá ser consultado no rodapé do TOTVS Saúde:

Podemos exibir o Log do processo:

Dados do usuário anonimizado:
