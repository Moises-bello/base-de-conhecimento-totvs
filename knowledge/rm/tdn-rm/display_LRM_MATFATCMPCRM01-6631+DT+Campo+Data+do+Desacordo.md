---
content_hash: 7abba85de9ac661f385ec504605573d1e20d760a2bf173d64a938351e2f9625e
fetched_at: '2026-06-29T00:09:58.229234+00:00'
page_id: '451278080'
product: rm
source: tdn-rm
title: MATFATCMPCRM01-6631 DT Campo Data do Desacordo
type: documentation
url: https://tdn.totvs.com/display/LRM/MATFATCMPCRM01-6631+DT+Campo+Data+do+Desacordo
version: 3
---

# Data do Desacordo em movimentos de anulação

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | BackOffice |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Movimento | MovMovimentoBaseAction | |
| **Cadastros Iniciais:** | Movimento |
| **Parâmetro(s):** | Parâmetros → Gestão de Estoque, Compras e Faturamento → Tipo de Movimento → Conhecimento de Transporte Eletrônico |
| **Ponto de Entrada:** | N/A |
| **Tickets relacionados** | N/A |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATFATCMPCRM01-6631 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SqlServer e Oracle |
| **Tabelas Utilizadas:** | TMOVTRANSP |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | 12.1.24 |

## Descrição

Para prover uma maior flexibilidade em movimentos de CT-e, foi criado o campo Data do Desacordo (TMOVTRANSP.DATADESACORDO), o qual será utilizado para o preenchimento da Tag <dEmi> no grupo <infCteAnu>. 

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações de uma das seguintes versões:

* 12.1.21.212 ou
* 12.1.24 e superiores

## Procedimento para Utilização

O campo Data do Desacordo será habilitado em "Tela de edição do movimento → Transporte → Identificação" quando o Tipo de CT-e for igual a anulação.
