---
content_hash: 87949af28dd312af16fefd7942f992a0391d89ed05feffad1d5b6aabdf397d18
fetched_at: '2026-06-29T00:08:52.318583+00:00'
page_id: '338378219'
product: rm
source: tdn-rm
title: Financeiro01-3971- Relatório das operações Liquidadas com Moeda em Espécie
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=338378219
version: 4
---

# Book de Relatórios - Gestão Financeira

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão Financeira*. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Relatórios. | Gerador de Relatórios - RM Reports |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | N/A. | N/A | |  |  | |
| **Cadastros Iniciais:** | N/A |
| **Parâmetro(s):** | N/A |
| **Ponto de Entrada:** | N/A. |
| **Tickets relacionados** | <https://totvssuporte.zendesk.com/agent/tickets/1715571> |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-3971> |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | *MS-SqlServer e Oracle* |
| **Tabelas Utilizadas:** | N/A |
| **Sistema(s) Operacional(is):** | *MS-Windows* |

## Descrição

A partir da de janeiro/2018 a Receita Federal passou a exigir uma nova obrigação acessória que se chama DME - Declaração de Operações Liquidadas com Moeda em Espécie

A Declaração de Operações Liquidadas com Moeda em Espécie (DME) é uma obrigação que trata de informações relativas a uma operação liquidada, total ou parcialmente, em espécie (dinheiro), decorrente de alienação ou cessão onerosa ou gratuita de bens e direitos, de prestação de serviços, de aluguel ou de outras operações que envolvam transferência de moeda em espécie, prestada à Secretaria da Receita Federal do Brasil (RFB) por meio de formulário eletrônico.

Atualmente a Receita disponibiliza em seu portal e-CAC o fórmulário para entrega da DME.  O acesso a DME está disponível no Centro Virtual de Atendimento ao Contribuinte (e-CAC, no serviço “apresentação da DME”) da RFB na internet no endereço: <http://www.receita.fazenda.gov.br>.

Como atualmente a Receita Federal não disponibiliza nenhum tipo de serviço para que a rotina possa ser gerada automaticamente foi desenvolvido no RM Reports um relatório para apresentar as operações liquidadas com moeda em espécie. Portanto o relatório disponibilizado é uma maneira de auxiliar nossos clientes na identificação das operações de forma segregada para que possa facilitar o preenchimento das informações dentro do formulário disponibilizado pela Receita Federal.

## Procedimento para Utilização

1. O primeiro passo é importar o relatório dentro do RM Reports. Deve-se acessar o menu Gestão/RM Reports.
2. Após realizar o filtro da forma desejada, deve-se importar o relatório que se encontra dentro da pasta de objetos Gerenciais no subdiretório Relatórios. O código do relatório é o "FINREL0039 - Relatório das operações Liquidadas com Moeda em Espécie". Para importação acesse o menu: Processos/Importar estrutura do Relatório e selecione o relatório no caminho citado acima.
3. Após a importação do relatório, deve-se executar o mesmo acessando o menu Processos/Gerar Relatório e clicar no botão 'Avançar'.
4. Após clicar em avançar será apresentada a tela para preenchimento dos parâmetros do relatório. Este relatório possui o parâmetro de Data inicial e Data final de baixa, pois o envio da DME é solicitado mensalmente. Após informar os parâmetros deve-se avançar e executar o processo. Após as baixas que foram liquidadas com moeda em espécie dentro do período informado serão apresentadas. O relatório apresenta as baixas com quebra por coligada em cada página.
5. Após a geração do relatório, o usuário deve conferir as movimentações apresentadas e estando tudo ok utilizar o relatório para preenchimento do DME dentro do porta e-CAC da RECEITA FEDERAL.  
   OBS: Como esta obrigação trata das operações liquidadas em espécie, o relatório possui uma condição em sua sentença para apresentar somente as baixas que foram feitas com a forma de pagamento = Dinheiro.
