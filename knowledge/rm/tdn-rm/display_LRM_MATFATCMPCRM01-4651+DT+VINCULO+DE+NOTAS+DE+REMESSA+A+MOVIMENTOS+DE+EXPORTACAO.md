---
content_hash: ad71b43bb4a0fc9cad34c40ae38126c93783ab78b4428669c8e6b2642b0824d3
fetched_at: '2026-06-29T00:09:09.854972+00:00'
page_id: '394211614'
product: rm
source: tdn-rm
title: MATFATCMPCRM01-4651 DT VINCULO DE NOTAS DE REMESSA A MOVIMENTOS DE EXPORTACAO
type: documentation
url: https://tdn.totvs.com/display/LRM/MATFATCMPCRM01-4651+DT+VINCULO+DE+NOTAS+DE+REMESSA+A+MOVIMENTOS+DE+EXPORTACAO
version: 1
---

# VÍNCULO DE NOTAS DE REMESSA NO MOVIMENTO DE EXPORTAÇÃO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Totvs Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | MOV.001 | INCLUSÃO DE MOVIMENTO | |
| **Cadastros Iniciais:** | - |
| **Parâmetro(s):** | - |
| **Ponto de Entrada:** | - |
| **Tickets relacionados** | 3343953 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATFATCMPCRM01-4651 |
| **País(es):** | Bra |
| **Banco(s) de Dados:** | SQL Server |
| **Tabelas Utilizadas:** | TITMVINCEXPORTACAO |
| **Sistema(s) Operacional(is):** | - |
| **Pacote:** | - |

## Descrição

Implementação para permitir o Vínculo de Notas de Remessa, ao Movimento de Exportação

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação de um dos seguintes pacotes de atualizações:

* 12.1.18.331 ou superiores
* 12.1.19.334 ou superiores
* 12.1.20.331 ou superiores
* 12.1.21 ou superiores

## Procedimento para Utilização

* Em Movimentos de Exportação, será possível vincular, além de Movimentos de Entrada, Movimentos de Saída (Remessa). Essa operação ocorre no Item de Movimento, na opção **Informações Adicionais → Relac. Mov. Exportação**. A coluna **Tipo de Operação** diferencia se a operação é de Entrada ou de Saída.
* Importante notar que as Quantidades **serão validadas por Tipo de Operação.**Assim, cada Tipo de Operação (Entrada e Saída), poderá conter no máximo a mesma quantidade existente no campo Quantidade da Aba Cabeçalho.   
  Exemplo: O Item possui Quantidade 10: dessa forma, pode-se vincular até 10 de quantidade do Tipo de Operação Entrada e mais 10 do Tipo de Operação Saída.
* Caso se tente ultrapassar essa quantidade para qualquer uma das duas operações, o sistema emitirá uma mensagem de consistência ao vincular.
