---
content_hash: cf8580097bedc937aaddd0d8f6fe0e218f5563b4ea453bde42f7cda974217af0
fetched_at: '2026-06-29T00:08:46.352990+00:00'
page_id: '317002773'
product: rm
source: tdn-rm
title: DT Atividade de fórmula visual para enviar mensagens ao eduCONNECT
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=317002773
version: 6
---

# Atividade de fórmula visual para enviar mensagens ao eduCONNECT

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Gestão Educacional* |
| **Módulo:** | **TOTVS eduCONNECT** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Notificação eduCONNECT* | *Atividade de fórmula visual para envio de notificação ao eduCONNECT* | |
| **Cadastros Iniciais:** | *Categoria do eduCONNECT,*  *Cadastro de usuário,*  *Fórmula visual* |
| **Parâmetro(s):** | *TOTVS Gestão Educacional | Configurações | Parâmetros | Ativar integração com o eduCONNECT;*  **TOTVS Gestão Educacional | Configurações | Parâmetros | Código da Instituição;**  **TOTVS Gestão Educacional | Configurações | Parâmetros | Url de conexão com o eduCONNECT;**  **TOTVS Gestão Educacional | Configurações | Parâmetros | Usuário de autenticação;**  *e o sistema estar autenticado com o eduCONNECT.* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | PORTALMOBILE01-1782 |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | **N/A** |
| **Tabelas Utilizadas:** | **N/A** |
| **Sistema(s) Operacional(is):** | **N/A** |

## Descrição

Foi disponibilizado uma nova atividade de fórmula visual, para possibilitar aos clientes do TOTVS Educacional enviar notificação para seus usuários via aplicativo TOTVS eduCONNECT. Com essa nova atividade, os usuários podem customizar um cadastro ou processo para enviar notificação.

## Procedimento para Configuração

## 

**CONFIGURAÇÃO DE PARÂMETROS**

1. Nos parâmetros do sistema, em TOTVS Educacional | Configurações | Parâmetros | 15.10 - eduCONNECT | eduCONNECT 1, deve-se realizar a autenticação no eduCONNECT, pois a atividade de fórmula visual "Notificação eduCONNECT" irá utilizar estas configurações para o envio de notificação.

**CONFIGURAÇÃO DE MENUS**

1. Realizar o cadastro das categorias no TOTVS Educacional, para que seja possível informar qual a categoria será realizado a notificação no TOTVS eduCONNECT, conforme mostra exemplo abaixo:

## Procedimento para Utilização

Para utilizar a nova atividade de fórmula visual, deve-se acessar o cadastro de fórmula visual em "TOTVS Educacional | Gestão | Fórmula Visual:

1. Ao editar o cadastro de fórmula visual, acessar a aba Atividades e depois o agrupador  "Educacional", conforme mostra a figura abaixo:
2. Depois basta selecionar e arrastar a nova atividade "Notificação eduCONNECT" para a área de "fluxo de trabalho sequencial", conforme mostra a figura abaixo:
3. A atividade possui as propriedades dividias nos grupos "01 - Contexto dos parâmetros eduCONNECT",  "02 - Configuração da mensagem" e "Dados da mensagem", que devem ser preenchidas conforme a necessidade e parâmetros do cliente.

Para mais informações de como criar fórmula visual, pode-se obter através do TDN no link:
