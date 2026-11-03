---
content_hash: b3fbf49d2637d91f324252a560f110811b72dd0001d441afa4867b1a5153046b
fetched_at: '2026-06-29T00:08:17.606842+00:00'
page_id: '256316813'
product: rm
source: tdn-rm
title: TVQI01_DT_Integracao_Educacional_Fluig_LMS
type: documentation
url: https://tdn.totvs.com/display/LRM/TVQI01_DT_Integracao_Educacional_Fluig_LMS
version: 116
---

# INTEGRAÇÃO EDUCACIONAL X FLUIG LMS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Integração Educacional x Fluig LMS* | *Integração Educacional x Fluig LMS* | |
| **Cadastros Iniciais:** | *N/A* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *Sql Server e Oracle* |
| **Tabelas Utilizadas:** | *N/A* |
| **Sistema(s) Operacional(is):** | *Windows 7* |

## Descrição

Ajuste para liberação da integração entre o módulo Educacional e o Fluig LMS, através de mensageria única.

## Procedimento para Implantação

Caso não tenha a integração instalada, é necessário a execução do Configurador no módulo de integração para a instalação do pacote "Educacional x Fluig LMS".

Caso tenha a integração "Educacional x LMS" instalada, será necessário removê-la para a instalação da nova integração, pois elas não são compatíveis.

## Procedimento para Utilização

Para a instalação da integração com o Fluig LMS:

1. Acessar o Configurador no módulo de integração:  
   Caminho: ***Integração | Ferramentas | Configurar***
2. Autenticar com o usuário e senha de conexão ao banco de dados;
3. Selecionar o pacote de integração: "***TOTVS Educacional x Fluig LMS***"
4. Acessar a visão de integrações para a configuração da integração:  
   Caminho: ***Integração | Integração | Mensagem Única | Integrações***

Caso tenha a integração "***TOTVS Educacional x LMS***" instalada:

1. Acessar a visão de integrações para a remover a integração:  
   Caminho: ***Integração | Integração | Mensagem Única | Integrações***  
   ***\* Recomendável anotar as configurações antes de removê-la para a configuração no novo pacote de integração***
2. Acessar o Configurador no módulo de integração:  
   Caminho: ***Integração | Ferramentas | Configurar***
3. Autenticar com o usuário e senha de conexão ao banco de dados;
4. Selecionar o pacote de integração: "***TOTVS Educacional x Fluig LMS***"
5. Acessar a visão de integrações para a configuração da integração:  
   Caminho: ***Integração | Integração | Mensagem Única | Integrações***

***Documento técnico da integração:***

divs
