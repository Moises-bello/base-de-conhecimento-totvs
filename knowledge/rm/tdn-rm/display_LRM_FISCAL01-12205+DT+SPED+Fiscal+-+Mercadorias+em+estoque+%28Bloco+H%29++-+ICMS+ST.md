---
content_hash: 4893ed9e6301dcf9e9991f9db0c3a35565f276f5361d2177beece7d423dda4a7
fetched_at: '2026-06-29T00:10:38.053338+00:00'
page_id: '543086159'
product: rm
source: tdn-rm
title: FISCAL01-12205 DT SPED Fiscal - Mercadorias em estoque (Bloco H)  - ICMS ST
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-12205+DT+SPED+Fiscal+-+Mercadorias+em+estoque+%28Bloco+H%29++-+ICMS+ST
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Geração de Arquivo EFD ICMS IPI |
| Ticket: | FISCAL01-12205 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12205 |

## **02. SITUAÇÃO/REQUISITO**

#### **Tela de geração da rotina e Bloco H**

Criar o flag “Gerar Estoque - Ressarcimento ICMS ST” na pasta de Dados do Inventário. Este flag só deve ser apresentado (ou habilitado) se um dos Motivos do Inventário for “Por Determinação dos Fiscos”.

Habilitando esse flag, o sistema irá gerar o Bloco H de acordo com as regras estabelecidas pelo RS para os contribuintes varejistas:

|  |  |
| --- | --- |
| Registro H005 | Com motivo "05 – Por determinação dos fiscos" |
|  | Registro H010 | Para cada uma das mercadorias em estoque que seja tributada pelo ICMS ST |
|  | Registro H020 | **BC\_ICMS**: BC do ICMS ST  **VL\_ICMS**: (BC do ICMS ST \* ALÌQ INTERNA) | (valor unitário) |

Devem ser selecionados os produtos que atendam às seguintes regras:

* Sejam tributados pelo ICMS ST,
* Data de início da tributação pelo ICMS ST seja igual ou anterior à Data do Inventário, e
* Que possuam saldo em estoque nesta data.

## **03. SOLUÇÃO**

Na tela de parâmetro do Sped Fiscal

Na aba Dados do Inventário foi implementado o parâmetro Gerar Estoque - Ressarcimento ICMS ST.

Este parâmetro será exibido quando for selecionado o Motivo do Inventário 1 ou Motivo do Inventário 2: Por determinação do Fisco.

Observação: Será possível gerar o Inventário 2 com H020 referente às informações do ICMS-ST e o inventário 1 ser gerado normalmente com as informações do ICMS.

Sempre que o parâmetro "Gerar Estoque - Ressarcimento ICMS ST" estiver habilitado o registro H020 será gerado com informação do ICMS-ST se for encontrado lançamento de entrada do produto em questão.

Seleção dos Lançamentos Fiscais para recuperar os valores da Base de Cálculo do ICMS ST e Valor do ICMS + Valor do ICMS ST:

Tipo de Lançamento: Entrada  
Status do Lançamento: Normal  
Data do Lançamento: Menor ou igual a Data do Inventário  
Não seja Lançamento de Devolução  
Tenha valor do ICMS ST no item  
O produto deve ser tributado pelo ICMS-ST com data igual ou anterior a data parametrizada do inventário. campo observado TPRDCODFISCAL.DTINICIOICMSST  
Será selecionado o lançamento fiscal mais recente.
