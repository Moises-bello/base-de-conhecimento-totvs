---
content_hash: 474de6b745eb4bf292109c510ad08acfba785af1b8ceed7630ed81d1347328cf
fetched_at: '2026-06-29T00:08:51.984761+00:00'
page_id: '338375504'
product: rm
source: tdn-rm
title: DT Log de operações do eduCONNECT
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=338375504
version: 5
---

# Log de operações do eduCONNECT

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Gestão Educacional* |
| **Módulo:** | **TOTVS eduCONNECT** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Log do eduCONNECT* | **Log do eduCONNECT* para análise de problemas ao disparar mensagens e ao efetuar login pelo EducaMobile.* | |
| **Cadastros Iniciais:** | *Processo "Agendamento/envio de mensagens",*  *Fórmula visual,*  *Login do EducaMobile pelo eduCONNECT* |
| **Parâmetro(s):** | *TOTVS Gestão Educacional | Configurações | Parâmetros | Ativar integração com o eduCONNECT;*  **TOTVS Gestão Educacional | Configurações | Parâmetros | Código da Instituição;**  **TOTVS Gestão Educacional | Configurações | Parâmetros | Url de conexão com o eduCONNECT;**  **TOTVS Gestão Educacional | Configurações | Parâmetros | Usuário de autenticação;**  *e o sistema estar autenticado com o eduCONNECT.* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | PORTALMOBILE01-1784 |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | **N/A** |
| **Tabelas Utilizadas:** | **N/A** |
| **Sistema(s) Operacional(is):** | **N/A** |

## Descrição

A funcionalidade de log do eduCONNECT tem como proposta o registro de log das operações que ocorrem no eduCONNECT em caso de falha de alguma operação. Entre as operações estão o envio de mensagens em geral ao eduCONNECT, login no EducaMobile pelo eduCONNECT, envio de mensagens através via fórmula visual, e procedimentos de inclusão, atualização ou exclusão de entidades, tais como categorias.

## Procedimento para Configuração

## **CONFIGURAÇÃO DE PARÂMETROS**

1. Nos parâmetros do sistema, em TOTVS Educacional | Configurações | Parâmetros | 15.10 - eduCONNECT | eduCONNECT 1, deve-se realizar a autenticação no eduCONNECT, pois a atividade de fórmula visual "Notificação eduCONNECT" irá utilizar estas configurações para o envio de notificação.

## Procedimento para Utilização

Para utilizar a funcionalidade é preciso que algum procedimento de envio de mensagens, login ou manipulação de entidades do eduCONNECT tenha gerado algum erro.

Por tratarmos de processos assíncronos, ou ainda, procedimentos que não retornam mensagens de erro passíveis de serem analisadas em tempo de execução, por exemplo, na tela de um dispositivo móvel, estas são direcionadas ao cadastro de logs do eduCONNECT, com o intuito de facilitar a interpretação dos problemas.

O formulário do log dará uma visão mais abrangente de qual o real motivo a operação não ocorreu corretamente no sistema. Maiores detalhes do erro em questão, ficarão disponíveis na aba mensagem de log:
