---
content_hash: 9fdc220b22a2d553b926fb816bc83a6abc7f8da293fd3625875f17bb860866d4
fetched_at: '2026-06-29T00:10:57.119712+00:00'
page_id: '59441262'
product: rm
source: tdn-rm
title: Gerar Lançamentos Financeiros a partir da Data de Entrega dos Itens
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=59441262
version: 3
---

**Produto:** TOTVS Gestão de Estoque, Compras e Faturamento **Versão 11.20**

**Processo do Sistema**: Integração Financeira

**SubProcesso**: Gerar Lançamentos Financeiros a partir da Data de Entrega dos Itens

***Como Fazer***

Como parametrizar o sistema gerar os lançamentos financeiros a partir da data de entrega dos itens de movimento?

***Definição do Processo***

A partir da versão 11.20.0 foi disponibilizada uma nova opção para a geração de lançamentos financeiros, quando incluídos à partir de um movimento. Este recurso é denominado Parcelamento.

O Parcelamento permite ao usuário gerar lançamentos financeiros personalizados a partir de dois parâmetros: a Data de Vencimento e o Valor da Parcela, que poderão ser informados manualmente ou gerados automaticamente, através de uma Condição de Pagamento informada pelo usuário.

Outra novidade é a geração das parcelas usando a data de entrega dos itens de movimento como base para o vencimento dos lançamentos financeiros a serem gerados no TOTVS Gestão Financeira. O usuário também poderá editar a composição das parcelas geradas pelo sistema, caso o mesmo tenha permissão.

O foco deste Como Fazer se limitará apenas à geração de lançamentos com base na data de entrega dos itens, para mais informações sobre o recurso de parcelamento acesse: <http://www.wikihelp.totvs.com.br>

***Parametrizações Necessárias***

Acessar **| Cadastro | Fórmula |** e cadastrar uma fórmula a ser utilizada para composição do valor a ratear para o movimento

Exemplo:

KQT \* KPU

Observação:

- A fórmula do valor a ratear nos movimentos habilitados com Parcelamento pela data de entrega do item, deve conter variáveis que tratam o valor a ratear por item de movimento. Esta manutenção será de responsabilidade do usuário que estiver configurando a utilização do recurso.

Acessar | **Opções | Parâmetros | RMNucleus |** e selecionar processo onde o tipo de movimento a ser utilizado para este fim foi configurado e editá-lo da seguinte forma.

ü **Etapa Item– Identificação 1/2**

Informar **| Data Entrega : Edita |**

Observação:

- O parâmetro ‘Data Entrega’ poderá ser configurado como ‘Edita’, ‘Consiste’, ou ‘Mostra’. Desde que a data de entrega do item de movimento seja informada para cada item, fica a cargo do usuário especificar qual a parametrização lhe é mais conveniente.

ü **Etapa Fin– Condições de Pagamento**

Informar **| Parcelamento: Usa com data entrega item |**

ü **Etapa Fin– Faturamento 1/6**

Marcar **| Fatura o Movimento: Sim |**

ü **Etapa Fin– Faturamento 3/6**

Informar **| Formula do Valor a Ratear: Informar a fórmula criada anteriormente para buscar o valor a ratear para o item |**

Observação:

- Não será abordada toda a parametrização da integração financeira, visto que cada empresa trabalha de forma diferente e a forma como cada parâmetro é configurado é de responsabilidade do usuário. Neste artigo Como Fazer apresenta apenas o básico para que o recurso funcione da forma como é esperado.

***Descrição do Processo***

* Incluir a movimentação como de costume;
* Na aba **| Identificação | Cabeçalho |** do item de movimentação, o usuário preencherá a data de entrega do item;
* Na aba **| Integrações | Financeira |** do movimento, o usuário deverá informar uma condição de pagamento e clicar no botão para que as parcelas sejam geradas.
* Ao salvar o movimento os lançamentos financeiros serão gerados conforme as parcelas geradas na etapa anterior.

Observação:

Caso a condição de pagamento utilizada, gere parcelas com datas de vencimentos iguais para itens distintos, os valores serão agrupados em uma única parcela para essa data de vencimento.

Exemplo:

Suponha um movimento com os seguintes itens e suas respectivas datas de entrega e valores:

|  |  |  |
| --- | --- | --- |
| **Item** | **Data de Entrega** | **Valor Total** |
| 01.01 | 05/02/2011 | 50 |
| 01.02 | 10/02/2011 | 90 |
| 01.03 | 05/02/2011 | 100 |

Na Aba **| Integrações | Financeira |**é informada a condição de pagamento 30/60/90 dias. O resultado que se obtém ao clicar em **Gerar** é o seguinte:

|  |  |
| --- | --- |
| **Data de Vencimento** | **Valor da Parcela** |
| 05/03/2011 | 50 |
| 10/03/2011 | 30 |
| 05/04/2011 | 50 |
| 10/04/2011 | 30 |
| 05/05/2011 | 50 |
| 10/05/2011 | 30 |

A data de vencimento é gerada a partir da data de emissão de cada item e a condição de pagamento utilizada. No caso, como a condição é 30, 60 e 90 dias, cada item gerou 3 parcelas cada, com vencimento a partir da Data de entrega de cada item..

Como a data de entrega dos itens 01.01 e 01.03 são a mesma, na geração do Parcelamento o valor dos itens 01.01 e 01.03 são agrupados e rateados conforme a condição de pagamento informada para geração automática das parcelas.

***Informações Adicionais***

- A fórmula do valor a ratear nos movimentos habilitados com Parcelamento pela data de entrega do item, deve conter variáveis que tratam o valor a ratear por item de movimento. Esta manutenção será de responsabilidade do usuário que estiver configurando a utilização do recurso.

- O tratamento das opções: ‘Efeito na 1ª. Parcela’, ‘Distribuição do Valor Opcional’ e ‘Valor na 1ª. Parcela’ não sofrem alterações quando se usa o Parcelamento.

- Este recurso só está disponível para as bases migradas para o novo modelo Backoffice.
