---
article_id: 360057363253
category: Manutenção de Ativos (SIGAMNT)
content_hash: 314563d2f49035a3e5ed3fe469a5dca94b234b141e0e73a91fdaf57a20f95dea
fetched_at: '2026-06-28T22:42:34.194482+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Layout importação de bens
type: support-article
updated_at: '2025-05-26T17:49:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057363253-Manufatura-Linha-Protheus-MNT-Layout-importa%C3%A7%C3%A3o-de-bens
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18667085409559)***Tempo aproximado para leitura: **00:01:50 min**  
**Dúvida**Qual o *layout* para importação de **bens** no **MNTA105 - Gera bens a partir de texto**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Versão 12  
  
**Solução**O *layout* para importação de **bens** no **MNTA105** é:

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Posição | Coluna | Descrição | Tipo | Tamanho | Decimal | Obrigatório | *Default* | Valores obrigatório | Formatação |
| 1 | **T9\_CODBEM** | **Bem** | **C** | 16 | 0 | Sim |  |  | AAAAAAAAAAAAAAAA |
| 2 | **T9\_CODFAMI** | **Família** | **C** | 6 | 0 | Sim |  |  | AAAAAA |
| 3 | **T9\_NOME** | **Nome do Bem** | **C** | 40 | 0 | Sim |  |  | AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA |
| 4 | **T9\_CCUSTO** | **Centro Custo** | **C** | 9 | 0 | Sim |  |  | AAAAAAAAA |
| 5 | **T9\_CALENDA** | **Turno** | **C** | 3 | 0 | Sim |  |  | AAA |
| 6 | **T9\_TIPMOD** | **Tipo Modelo** | **C** | 10 | 0 | Sim |  |  | AAAAAAAAAA |
| 7 | **T9\_CATBEM** | **Categoria Bem** | **C** | 1 | 0 | Não | **1** | \* | A |
| 8 | **T9\_PADRAO** | **Padrão Família** | **C** | 1 | 0 | Não | **N** |  | A |
| 9 | **T9\_ESTRUTU** | **Estrutura** | **C** | 1 | 0 | Não | **N** |  | A |
| 10 | **T9\_PRIORID** | **Prioridade** | **C** | 3 | 0 | Não | **ZZZ** |  | AAA |
| 11 | **T9\_INDPOND** | **Muda Pondera** | **C** | 1 | 0 | Não | **N** |  | A |
| 12 | **T9\_SITMAN** | **Situação Manutenção** | **C** | 1 | 0 | Não | **A** |  | A |
| 13 | **T9\_SITBEM** | **Situação Bem** | **C** | 1 | 0 | Não | **A** |  | A |
| 14 | **T9\_FABRICA** | **Fabricante** | **C** | 6 | 0 | Não |  |  | AAAAAA |
| 15 | **T9\_STATUS** | **Status** | **C** | 2 | 0 | Não |  |  | AA |
| 16 | **T9\_CENTRAB** | **Centro de Trabalho** | **C** | 6 | 0 | Não |  |  | AAAAAA |
| 17 | **T9\_FORNECE** | **Fornecedor** | **C** | 6 | 0 | Não |  |  | AAAAAA |
| 18 | **T9\_LOJA** | **Loja Fornecedor** | **C** | 2 | 0 | Sim |  | \*\* | AA |
| 19 | **T9\_MODELO** | **Modelo** | **C** | 10 | 0 | Não |  |  | AAAAAAAAAA |
| 20 | **T9\_SERIE** | **Serie** | **C** | 20 | 0 | Não |  |  | AAAAAAAAAAAAAAAAAAAA |
| 21 | **T9\_DTCOMPR** | **Data de Compra** | **D** | 8 | 0 | Não |  |  | 99/99/9999 |
| 22 | **T9\_PRGARAN** | **Prazo Garantia** | **N** | 6 | 0 | Não |  |  | 999999 |
| 23 | **T9\_UNGARAN** | **Unidade do Prazo de garantia** | **C** | 1 | 0 | Sim |  | \*\* | A |
| 24 | **T9\_DTGARAN** | **Data da Garantia** | **D** | 8 | 0 | Não |  |  | 99/99/9999 |
| 25 | **T9\_CODESTO** | **Código de Estoque** | **C** | 15 | 0 | Não |  |  | AAAAAAAAAAAAAAA |
| 26 | **T9\_TEMCONT** | **Tem contador** | **C** | 1 | 0 | Não | **N** |  | A |
| 27 | **T9\_TPCONTA** | **Tipo de Contador** | **C** | 20 | 0 | Sim |  | \*\*\* | AAAAAAAAAAAAAAAAAAAA |
| 28 | **T9\_POSCONT** | **Posição do Contador** | **N** | 9 | 0 | Sim |  | \*\*\* | 999999999 |
| 29 | **T9\_DTULTAC** | **Data Último Acompanhamento** | **D** | 8 | 0 | Sim |  | \*\*\* | 99/99/9999 |
| 30 | **T9\_CONTACU** | **Contador Acumulado** | **N** | 12 | 0 | Sim |  | \*\*\* | 999999999999 |
| 31 | **T9\_VARDIA** | **Variação dia** | **N** | 6 | 0 | Sim |  | \*\*\* | 999999 |
| 32 | **T9\_LIMICON** | **Limite do Contador** | **N** | 9 | 0 | Sim |  | \*\*\* | 999999999 |
| 33 | **T9\_PERACOM** | **Período do Acompanhamento** | **N** | 3 | 0 | Não |  |  | 999 |
| 34 | **T9\_UNIACOM** | **Unidade de Acompanhamento** | **C** | 1 | 0 | Sim |  | \*\* | A |
| 35 | **T9\_VALODES** | **Valor de controle de vida útil** | **N** | 9 | 0 | Não |  |  | 999999999 |
| 36 | **T9\_UNIDDES** | **Unidade de medida de controle de vida útil do bem** | **C** | 1 | 0 | Sim |  | \*\* | A |
| 37 | **T9\_CLIENTE** | **Cliente** | **C** | 6 | 0 | Não |  |  | AAAAAA |
| 38 | **T9\_LOJACLI** | **Loja do Cliente** | **C** | 2 | 0 | Sim |  | \*\* | AA |
| 39 | **T9\_VALCPA** | **Valor de aquisição do Bem** | **N** | 12 | 2 | Não |  |  | 999999999.99 |
| 40 | **T9\_CUSTOHO** | **Valor do custo do bem** | **N** | 9 | 2 | Não |  |  | 999999.99 |
| 41 | **T9\_MOVIBEM** | **Movimentação do Bem** | **C** | 1 | 0 | Não | **N** |  | A |
| 42 | **T9\_DTINSTA** | **Data de Instalação** | **D** | 8 | 0 | Não |  |  | 99/99/9999 |
| 43 | **T9\_CONTGAR** | **Contador para controle de Garantia** | **N** | 9 | 0 | Não |  |  | 999999999 |
| 44 | **T9\_ITEMCTA** | **Item Conta Contábil** | **C** | 9 | 0 | Não |  |  | AAAAAAAAA |
| 45 | **T9\_VALVENA** | **Valor Venal do bem** | **N** | 12 | 2 | Não |  |  | 999999999.99 |
| 46 | **T9\_LUBRIFI** | **Bem passível ou não de lubrificação** | **C** | 1 | 0 | Não | **1** |  | A |
| 47 | **T9\_PARTEDI** | **Indica controle de Parte Diária** | **C** | 1 | 0 | Não | **2** |  | A |

Legenda da coluna valores obrigatórios:  
\* Para importar **Bem - MNT080**, informe o conteúdo **1 - Bem**. Para importar **Veículo - MNTA084**, informe o conteúdo **2 - Frota integrada ao TMS** ou **4 - Frota não integrada ao TMS**.  
\*\* - Obrigatório se o item anterior for preenchido, do contrário deve ser nulo;  
\*\*\* - Obrigatório se o **bem** for controlado por contador.  
 **Anexo**  
Exemplo de *layout* de bens:
