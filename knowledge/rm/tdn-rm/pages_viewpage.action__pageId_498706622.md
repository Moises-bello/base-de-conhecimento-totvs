---
content_hash: 75bf48b7659337a3838995100bb70b3b937f5a29b8e60a1c967486f87bf7542e
fetched_at: '2026-06-29T00:10:22.721757+00:00'
page_id: '498706622'
product: rm
source: tdn-rm
title: MATFATCMPCRM01-8409 DT CT-e Aéreo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=498706622
version: 2
---

# CT-e Aéreo

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | RM Backoffice |
| **Módulo:** | Totvs Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Informe a rotina. | Informe o nome técnico da rotina. | |
| **Cadastros Iniciais:** | -. |
| **Parâmetro(s):** | Ambiente | Gestão de Estoque, Compras e Faturamento | Parâmetros Vendas | Faturamento | Tipo de Mov, | Aba Fis - Conhecimento de Transporte |
| **Ponto de Entrada:** | - |
| **Tickets relacionados** | MATFATCMPCRM01-8409 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATFATCMPCRM01-8409 |
| **País(es):** | Bra |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | TCTEAEREO, TCTEAEREOINFMANUSEIO, TCTEFLUXOCARGA, TCTEFLUXOCARGAPASS, TCTECARGAPERIGOSA |
| **Sistema(s) Operacional(is):** | - |
| **Pacote:** | - |

## Descrição

Para esta implementação, três pontos importantes sofreram alterações: Parâmetro, Movimento e Envio de Conhecimento de Transporte (CT-e).

Esse documento se refere às alterações especificas do modal Aéreo: para outras informações sobre o CT-e, acessar o documento [MATFATCMPCRM01-1358 DT CT-e versão 3.00](http://tdn.totvs.com/pages/viewpage.action?pageId=306839706).

### Parâmetro

Acessar a visão de Parâmetros do Módulo, através do caminho: Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento.

Após escolhido o Tipo de Movimento (1.2.XX ou 2.2.XX) e navegar até a Etapa Fis - Conhecimento de Transporte, a nova opção 'Aéreo' estará disponível na Caixa de Seleção referente ao Modal.

### Movimento

#### Aéreo, Fluxo de Carga e Carga Perigosa

Após parametrizado corretamente, o movimento deverá apresentar a opção 'CT-e' em seu menu.

Nessa tela pode ser encontrada a aba **Fluxo de Carga**. O Fluxo de Carga contém informações obrigatórias para o Modal Aéreo.

Mais informações podem encontradas a partir da página 157 do Manual de Orientações do Contribuinte do CT-e (versão 3.0).

Também pode ser encontrada a aba **Aéreo**, onde contemplará os novos campos que deverão ser utilizados de acordo com a Legislação.

Mais informações sobre os campos da legislação podem ser encontradas a partir da pagina 191 do Manual de Orientações do Contribuinte do CT-e (versão 3.0).

Caso a Carga Transportada seja classificada como Perigosa pela ONU, deve-se preencher os dados referentes a essa carga na **Carga Perigosa - ONU.**

Mais informações sobre esses campos estão contidas a partir da página 193 do Manual de Orientações do Contribuinte do CT-e (versão 3.0).

## Procedimento para Implantação

Será necessário executar os scripts contidos no **RM Atualizador** para se criar as tabelas utilizadas para o CT-e Aéreo.

Além disso, é necessário instalar um dos seguintes pacote de atualizações:

* 12.1.23.209 ou
* 12.1.26
