---
content_hash: 83f682c2845fb20eb57a56f5e42acfba9391273ea0810dc0053d80896231f49f
fetched_at: '2026-06-29T00:08:47.682558+00:00'
page_id: '320373358'
product: rm
source: tdn-rm
title: DT Somar Bolsas de Mesma Ordem e Tipo de Aplicação em Cascata
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=320373358
version: 3
---

# Somar Bolsas de Mesma Ordem e Tipo de Aplicação em Cascata

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Gestão Educacional* |
| **Módulo:** | **TOTVS Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Geração de Lançamentos* | *Geração de Lançamentos* | | *Regeração de Lançamentos* | *Regeração de Lançamentos* | | *Simulação da Parcela* | *Simulação da Parcela* | |
| **Cadastros Iniciais:** | *Classificação de Bolsas, Bolsas do Contrato, Contrato* |
| **Parâmetro(s):** | *Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin - Geral 2/4 | Somar bolsas de mesma ordem e tipo de aplicação em cascata* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | DEDUINTEGRACOES-1068 |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *N/A* |
| **Tabelas Utilizadas:** | *SPARAM* |
| **Sistema(s) Operacional(is):** | *N/A.* |

## Descrição

Com o objetivo de flexibilizar a aplicação das bolsas em cascata, foi criado o parâmetro "Somar bolsas de mesma ordem e tipo de aplicação em cascata" em Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin - Geral 2/4. Ao marcar esse parâmetro o sistema irá somar os descontos das bolsas em cascatas que forem configurados com mesma ordem de aplicação, ordem configurada tanto na classificação de bolsas como no contrato do aluno, para então aplicar sobre o valor base da parcela.

**Exemplo:**

Parcela: R$ 1000,00.

Bolsa 1            18%                    Ordem 1  
Bolsa 2            5%                      Ordem 2  
Bolsa 3            10%                    Ordem 1

Valor a ser pago:

R$ 1000,00 - (Bolsa 1 + Bolsa 3) = R$ 720,00  
                                                         R$ 720,00 - Bolsa 2 = **R$ 684,00**.

Importante salientar que a soma dos descontos só ocorrerá se a ordem de aplicação definida tanto na classificação de bolsas quanto no contrato do aluno for a mesma para as bolsas em cascata que serão aplicadas:

Classificação das bolsas em cascata

Ordem de aplicação da bolsa 1 definida no contrato do aluno

Ordem de aplicação da bolsa 2 definida no contrato do aluno

Caso o parâmetro não seja marcado ou a ordem de aplicação das bolsas sejam diferentes, na classificação ou no contrato, o comportamento do sistema não mudará e as bolsas em cascatas serão aplicadas uma por vez sobre um valor base da parcela que será decrescida de acordo com o desconto gerado.

**Exemplo:**

Parcela: R$ 1000,00.

Bolsa 1            18%                    Ordem 1  
Bolsa 2            5%                      Ordem 3  
Bolsa 3            10%                    Ordem 2

Valor a ser pago:

R$ 1000,00 - Bolsa 1 = R$ 820,00  
                                      R$ 820,00 - Bolsa 3 = R$ 738,00  
                                                                          R$ 738,00 - Bolsa 2 = **R$ 701,10.**
