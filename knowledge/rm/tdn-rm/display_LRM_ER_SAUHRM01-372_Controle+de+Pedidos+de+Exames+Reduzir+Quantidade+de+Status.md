---
content_hash: 2df78b5229794ed07d387cfe77d7c1fcd196d4befe0bf7d05779a52a0bf0b011
fetched_at: '2026-06-29T00:08:13.395781+00:00'
page_id: '244418548'
product: rm
source: tdn-rm
title: ER_SAUHRM01-372_Controle de Pedidos de Exames Reduzir Quantidade de Status
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_SAUHRM01-372_Controle+de+Pedidos+de+Exames+Reduzir+Quantidade+de+Status
version: 2
---

|  |  |  |  |
| --- | --- | --- | --- |
| Especificação |  |  |  |
| Produto | TOTVS HOSPITALAR | Módulo | RM SAUDE |
| Segmento Executor | Saúde |  |  |
| Projeto | SAUHRM01 | IRM | SAUHRM01-36 |
| Requisito | SAUHRM01-372 | SubTarefa | SAUHRM01-421 |
| País | ( X ) Brasil  (  ) Argentina  (  ) México  (  ) Chile  (  ) Paraguai  (  ) Equador   (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. |  |  |

\_Toc355276661\_Toc355276662

# Objetivo

Visando um maior ganho operacional, o cliente solicita a redução de "Cliques" na rotina de Controle de pedidos de exames/ Tela de preenchimento de Resultados.  
 A solicitação tem como objetivo a supressão das confirmações utilizando os Cliques em "OK" ou "F4".  
 Ver tela de exemplo abaixo:   
 No "Executar Ação" e "Concluir Digitação" o sistema deverá salvar o registro sem a necessidade de clicar no "F4". Após esta operação o mesmo deverá se posicionará no próximo status e assim por diante.   
 Caso o atendente clique no botão "ok" este utilizará a função já existente no sistema, que é o salvamento e retorno para tela inicial que é a "Controle e pedido de exames".  
 Tela 1  
 \_GoBack

# \_Toc355276664Definição da Regra de Negócio

**RN001** – Criação de parâmetro na tela de "Parâmetros Gerais", onde o cliente poderá escolher pelo salvamento automático dos status dos exames quando este selecionar uma das opções do campo "Executa Ação" no módulo de controle e Pedidos de Exames.   
 **RN002** – Com o parâmetro habilitado toda escolha do campo "Executa Ação" terá seu salvamento automático;   
 **RN003** – Para retornar a tela inicia – Controle de Pedidos de Exames será necessário clicar no botão OK.

|  |  |  |  |
| --- | --- | --- | --- |
| Rotinas Envolvidas |  |  |  |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** |
| Preenchimento de Resultado | Alteração | Controle de pedidos de Exames/Preenchimento de resultados |

# Escopo Negativo

O sistema ficará suscetível a erros, ou seja, se o atendente executar uma ação incorreta o sistema ira gravar a ação em questão, pois não existira a ação humana de clicar em "F4" ou "OK".

# \_Toc355276665Protótipo de Tela

Tela 2 – Parâmetros de parâmetros Gerais. Opções/Parâmetros Gerais - Aba Unidade Diagnostico

|  |  |
| --- | --- |
| \_Toc355276666**Regras da Interface** |  |
| **RI-001** | Na tela 1 - No "Executar Ação" e "Concluir Digitação" o sistema deverá salvar o registro sem a necessidade de clicar no "F4". Após esta operação o mesmo deverá se posicionará no próximo status e assim por diante. |
| **RI-002** | Na Tela – 2 Habilitar o parâmetro "Suprime confirmação "F4" e "OK" na tela de Digitação de Resultado" o sistema executará estas funções automaticamente no "Executar Ação" na tela de Digitação de Resultado. |
|  |  |
|  |  |

# \_Toc355276667Fluxo do Processo

# Dicionário de Dados

Não necessário para o desenvolvimento deste requisito.

# Grupo de Perguntas

Não necessário para o desenvolvimento deste requisito.

# **Consulta Padrão**

Não necessário para o desenvolvimento deste requisito.

# Estrutura de Menu

Não necessário para o desenvolvimento deste requisito.
