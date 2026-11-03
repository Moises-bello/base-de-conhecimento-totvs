---
article_id: 360020801392
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 5e938437fcf74e78f03a204db055c7b10c3ce8d07097f5bca04608bb3534af06
fetched_at: '2026-06-28T22:39:07.954181+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Quais os Códigos dos
  Lançamentos Padronizados do Estoque?
type: support-article
updated_at: '2026-06-17T15:51:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020801392-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Quais-os-C%C3%B3digos-dos-Lan%C3%A7amentos-Padronizados-do-Estoque
---

O artigo apresenta os lançamentos padronizados (LPs) utilizados na contabilização dos movimentos de estoque no TOTVS Backoffice (Protheus), detalhando códigos, descrições e particularidades de cada LP, além de orientações sobre configurações e links para aprofundamento em outros módulos e processos relacionados ao estoque.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32150767203095) Tempo aproximado para leitura: **00:03:45 min**

**Dúvida**

Quais os lançamentos padronizados (LP's) utilizados para contabilização dos movimentos de estoque

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Segue abaixo uma lista com os lançamentos padronizados do Estoque para contabilização dos movimentos:

|  |  |
| --- | --- |
| **ESTOQUE/CUSTOS** | |
|  |  |
| ***Internos / Internos Mod 2*** | |
| **Código** | **Lançamento** |
| **666** | Saída de Saldo em estoque (Requisição) |
| **668** | Entrada de Saldo em estoque (Devolução) |
|  |  |
| ***Baixas de Solicitações ao Armazém*** | |
| **67A** | Movimento de Estoques - Rateio da Solicitação ao Armazém |
| **67B** | Movimento de Estoques - Rateio da Solicitação ao Armazém - Estorno |
|  |  |
| ***Produção*** | |
| **Código** | **Lançamento** |
| **666** | Saída de saldo em estoque (requisição) para materiais com apropriação direta |
| **668** | Entrada de saldo em estoque (devolução / produção) para materiais com apropriação direta) |
| **679** | Entrada de saldo em estoque (devolução) para materiais com apropriação indireta) |
| **680** | Saída de saldo em estoque (requisição) para materiais com apropriação indireta) |
|  |  |
| ***Transferências Mod 2/ Desmontagem / Integracao com PCO*** | |
| **Código** | **Lançamento** |
| **670** | [Saída de saldo em estoque (requisição) - movimento origem](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410253103127) |
| **672** | Entrada de saldo em estoque (devolução) - movimento destino |
|  |  |
| ***Recálculo do Custo Médio*** | |
| **Código** | **Lançamento** |
| **682** | Retorno poder de terceiros (item Documento Entrada) |
| **681** | [Nota de Compra, Entrada por Transferencia entre filiais E também Remessa de terceiros (item Documento Entrada)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/40279431218839-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEST-Como-realizar-a-contabiliza%C3%A7%C3%A3o-de-um-documento-de-entrada-no-m%C3%B3dulo-do-estoque) |
| **Particularidades para Contabilizar as LPS 681 E 682**  - A TES, tanto de REMESSA quanto RETORNO deve estar configurada com ATUALIZA ESTOQUE (F4\_ESTOQUE) = SIM - A TES de REMESSA, deve estar com o campo (F4\_PODER3) = R - A TES de REMESSA, deve possuir amarração claro da TES de devolução (F4\_TESDV) = TES DE DEVOLUÇAO - A TES de devolução, deve possuir controle de poder de terceiros (F4\_PODER3) = D | |
| **641** | [Devolução de Vendas (item Documento Entrada)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410249729687-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Como-Contabilizar-Devolu%C3%A7%C3%A3o-de-Pedido-de-Venda-) |
| **669** | (LANÇAMENTO OBSOLETO) Segue TDN sobre  [Clique aqui](https://tdn.totvs.com/display/PROT/Compatibilidade+-+Fechamento+estoque+X+Acompanha+custos#:~:text=Lan%C3%A7amentos%20Padr%C3%B5es%20667/669) |
| **667** | (LANÇAMENTO OBSOLETO) Segue TDN sobre  [Clique aqui](https://tdn.totvs.com/display/PROT/Compatibilidade+-+Fechamento+estoque+X+Acompanha+custos#:~:text=Lan%C3%A7amentos%20Padr%C3%B5es%20667/669) |
| **668** | Entrada de saldo em estoque (devolução / produção) para materiais com apropriação direta). |
| **666** | Saída de saldo em estoque (requisição) para materiais com apropriação direta. |
| **679** | Entrada de saldo em estoque (devolução/produção) para materiais com apropriação indireta. |
| **680** | Saída de saldo em estoque (requisição) para materiais com apropriação indireta. |
| **678** | - Venda de mercadoria (item do Documento de Saída)  - Saida por Transferencia entre filiais.  - Devolução de compra **Somente via ponto de entrada:** [A330CDEV - Contabilização dos movimentos de devolução de compras](https://tdn.totvs.com/x/eJgXDg) |
| **676** | Entrada de saldo em estoque (Devolução/Produção) no inventário On-Line.  Clique [***nesse link***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32136769508375-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Lan%C3%A7amento-Padr%C3%A3o-674-e-676-particularidades-importantes) e veja particularidades importantes sobre essa LP |
| **674** | Saída de saldo em estoque (requisição) no inventário On-Line.  Clique [***nesse link***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32136769508375-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Lan%C3%A7amento-Padr%C3%A3o-674-e-676-particularidades-importantes) e veja particularidades importantes sobre essa LP |

|  |
| --- |
| **Importante:** **O lançamento padrão é desenvolvido e conjunto com o departamento contábil de sua empresa, juntamente com o analista programador, o suporte não auxiliar em quaisquer regras customizadas utilizadas em seu lançamento, como por exemplo no campo CT5\_VRL01, a regra padrão utilizada é somente (SD\*->SD\*\_nome\_do\_campo) onde "\*" é referente a tabela da movimentação para sua contabilização).** |

Referente aos Lançamentos padronizados das **Baixas de Solicitações ao Armazém**:

**A contabilização ocorrerá das seguintes formas:**  
**Online** - Ao efetuar a baixa da pré-requisição (LP 67A) e ao efetuar o estorno da baixa da pré-requisição (LP 67B).  
**Offline** - Ao executar o recálculo do custo médio via rotina MATA330 ou a contabilização do recálculo do custo médio via rotina MATA331.

**As seguintes tabelas estarão posicionadas ao disparar os LPs:**  
SD3 - Movimentações Internas  
SGS - Rateio da Solicitação ao Armazém  
SCP - Solicitação ao Armazém (somente na contabilização online)

## **Demais lançamentos de outros modulos**

**Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Contabilização Compras**

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027616491-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Contabiliza%C3%A7%C3%A3o-Compras>

**Cross Segmentos - Backoffice Protheus - SIGAFAT - Lançamento Padrão para contabilizar no Faturamento**

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017692191-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Lan%C3%A7amento-Padr%C3%A3o-para-contabilizar-no-Faturamento>

**Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Lançamentos Padrões do Financeiro**  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050526913-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Lan%C3%A7amentos-Padr%C3%B5es-do-Financeiro>

**Saiba mais:**

[SIGAEST - Como Contabilizar as Movimentações Internas do Estoque?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405082704791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-Contabilizar-as-Movimenta%C3%A7%C3%B5es-Internas-do-Estoque)

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
