---
content_hash: 36dfeaf000465614de8be065f15cf1500ab52ec81c9c85637eb029affcdb749a
fetched_at: '2026-06-29T00:06:07.038559+00:00'
page_id: '201734448'
product: rm
source: tdn-rm
title: ER_PCREQ-6544_SAÚDE_CIH_FLUIG_12.1.9_PARÂMETROS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201734448
version: 3
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | CIH | **Módulo** | Parâmetros |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | SAÚDE\_CIH\_FLUIG | **IRM1** | PCREQ-6530 |
| **Requisito1** | PCREQ-6544 | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** |  | **Réplica** |  |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

A parametrização possibilitará ao usuário definir qual a periodicidade que a importação das informações dos pacientes deverá acontecer.

### (Obrigatório)

## Definição da Regra de Negócio

 

O usuário informará a Data de Início e Data Fim, ou seja, o intervalo que o CIH ficará importando as informações do sistema de Gestão Hospitalar da Unidade.

 

Deverá informar também o horário que a importação ocorrerá.

 

 Após esta parametrização, o CIH importará todas as informações dos Pacientes (Internação e Alta, Antibiótico, CID, Cirurgias, Cultura Final, Eventos Adversos).

### Opcional

## Protótipo de Tela

**Protótipo 01**

### Opcional

## Fluxo do Processo

1. O usuário define o período que as importações deverão acontecer;
2. O sistema realiza a importação no momento pré-determinado.
3. O log de usuário é gerado.

### (Opcional)

### (Opcional)

### (Opcional)

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
