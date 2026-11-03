---
content_hash: 3fc2b03e9633695255f6387ae16f472b8ba6a9de4cf4e936a0d433bcce9cfff1
fetched_at: '2026-06-29T00:08:16.534469+00:00'
page_id: '247924801'
product: rm
source: tdn-rm
title: TVAODJ_DT_Criacao_NovoCC_Salario_Paternidade
type: documentation
url: https://tdn.totvs.com/display/LRM/TVAODJ_DT_Criacao_NovoCC_Salario_Paternidade
version: 1
---

# CRIAÇÃO DE NOVO CÓDIGO DE CÁLCULO PARA SALÁRIO PATERNIDADE

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Afastamento* | *Histórico de Afastamento* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Afastamento** | *Histórico de Afastamento* | | **Férias**  *Folha Mensal* | **Lançamento das Férias**  *Cálculo da Folha Mensal* | |
| **Cadastros Iniciais:** | *Cadastro de Evento* |
| **Parâmetro(s):** | *Tipo do Afastamento* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *TVAODJ* |
| **Requisito (ISSUE):** | *Folha* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server, Oracle* |
| **Tabelas Utilizadas:** | *PCODSITUACAO, PCODAFAST, PEVENTO* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Durante o período de afastamento do tipo Y - Licença Paternidade, o funcionário estava recebendo o salário através dos Códigos de Cálculo 1 ou 2.

Conforme a Lei, "as Empresas que aderirem ao programa, que é facultativo, poderão deduzir de impostos federais (IR) o total da remuneração paga integralmente à sua(eu) funcionária(o). A regra só vale para as empresas que possuam tributação sobre lucro real. Empresas que declaram pelo lucro presumido ou estão integradas no Simples Nacional podem aderir, mas estas não terão direito à dedução no IR".

Com o cálculo sendo feito nos eventos de CC's 1 ou 2 ficava complicado de separar o valor para fazer a dedução.

Foi implementado o novo CC 353 - SALÁRIO PATERNIDADE, para lançar somente o valor referente ao período de afastamento tipo Y.

Este evento terá as mesmas características do eventos de remuneração, CC's 1 e 2.
