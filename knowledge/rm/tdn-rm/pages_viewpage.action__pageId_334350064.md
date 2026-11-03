---
content_hash: cd8f8714a1dacffc0125edb59afd2e929c6292cb294dfc98807da6de5c51c272
fetched_at: '2026-06-29T00:08:50.949430+00:00'
page_id: '334350064'
product: rm
source: tdn-rm
title: Como_Fazer_Venda_Deságio_No_Cálculo_De_Valor_Líquido_No_Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=334350064
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | : | TOTVS Incorporação 12.1.18 e superiores |
| **Processo** | : | Plano de Financiamento |
| **Subprocesso** | : | Geração do Plano de Financiamento |
| **Data da publicação** | : |  |

**OBJETIVO:**

Trazer as parcelas do Plano de Financiamento da Venda com Modelo de Cálculo PRICE a Valor Presente, sem a necessidade de se ter que efetivar um Aditivo de Alteração do Valor da Parcela.

**PREMISSAS:**

Habilitar o Reajuste Online (<http://wikihelp.totvs.com.br/WikiHelp/FIN/FIN.ContasAReceber.aspx> - Item: Reajuste - Subitem: Baixa Manual);

Ter vendas com parcelas em aberto a vencer com base no Modelo de Cálculo PRICE;

Alterar o parâmetro “*Tipo de Deságio no Cálculo de Valor Líquido no Financeiro (Reajuste em Memória)*” do módulo imobiliário, “*Ambiente | Parâmetros | TOTVS Incorporação | Contrato | Plano de Financiamento | Etapa 5 – Plano de Financiamento*” de “*nenhum”* para “***Valor Presente Meses: será calculado o valor presente da parcela de acordo com cada mês que for antecipado***”.

Figura A - <http://wikihelp.totvs.com.br/WikiHelp/IMB/IMB.ParamContratoPlFinanciamento.aspx>*\**

*\*Os cálculos para o modelo SACRE ainda não foram implementados.*

**UTILIZAÇÃO:**

* No exemplo abaixo, temos uma venda cujas parcelas do Grupo 2 são calculadas com base no Modelo de Cálculo PRICE:

* Configuramos o parâmetro *“Tipo de Deságio no Cálculo de Valor Líquido no Financeiro (Reajuste em Memória)”* para *“**Valor Presente Meses**”*, nesta coligada*:*

* Na visão de Vendas, acessamos o anexo dos Lançamentos Financeiros, filtramos os lançamentos do Grupo 2, definimos a Data de Cálculos do Valor Líquido (Data Líquido) à esquerda do rodapé desta visão e solicitamos o cálculo do Valor Presente destas parcelas para a Data de 31/08/2018:

* Ao realizarmos esta ação, o sistema apresenta os valores das parcelas para a Data de Baixa, na Data de Cálculo do Valor Líquido predefinida;

* Ao editamos a Parcela ID 15195, deste grupo, que tem o vencimento em 25/05/2018, também é possível de se visualizar os detalhes da realização deste cálculo, acessando a aba *“Valores | Gerais”* e após preencher os dados do agrupador *“Valor Líquido”*, acionar o botão *“Exibir Cálculo do Valor Líquido”*:

* Na janela “Cálculo do Valor Líquido” que se abre, é possível de se visualizar o componente Desconto Juros, o qual o sistema utiliza para fazer o deságio dos Juros calculados pelo Modelo PRICE:

* Também é possível de se gerar um relatório de Ficha Financeira com essas informações para o Cliente:

* A Data Base definirá a Data de Cálculo do Valor Líquido das parcelas, quando a opção “*Considerar Deságio*” estiver marcado:

* Na Ficha Financeira constará na composição dos valores das parcelas o campo Desconto, que é referente ao deságio do modelo PRICE e também uma mensagem informando ao Comprador que estes valores de deságio são referentes à Data Base da Ficha Financeira e que os mesmos estão sujeitos a confirmação/atualização:

Qualquer dúvida entre em contato com a equipe do Suporte do TIN.
