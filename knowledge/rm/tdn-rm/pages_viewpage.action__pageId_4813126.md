---
content_hash: 2147d0d2a764b4ee92346a2a39d7a1fe67236ea13a6a22b4f9c6d8908a0df88a
fetched_at: '2026-06-29T00:10:19.221609+00:00'
page_id: '4813126'
product: rm
source: tdn-rm
title: Controle Orçamentário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813126
version: 7
---

BLOCK

Controle Orçamentário

FAQ: **Controle Orçamentário**

Avaliação

* **Introdução**

Apresentar a correta parametrização do controle orçamentário bem como sua aplicação nos tipos de movimentos dentro de um processo de gestão de compras.

Solução

* **Desenvolvimento/Procedimento**

***1.* *Parametrização***

* Nos parâmetros Controle Orçamentário deverá ser parametrizado para utilizar nova versão do orçamento, bem como a descrição dos tipos de orçamentos.

> Orçado: Descrição que será apresentada do valor orçado, ou seja, o valor que esta sendo previsto para ser utilizado.
>
> Real: Descrição que será apresentada do valor realizado, ou seja, o valor que esta efetivamente sendo utilizado, gasto.
>
> Opcional1: Descrição que será apresentada de um valor opcional, ou seja, um valor comprometido, reservado, mas inda não efetivado
>
> Opcional2: Idem explicação do campo valor opcional1.

* Nos parâmetros do tipo de movimento deverá ser informado as seguintes parametrizações:
  + Edição da Natureza Orçamentária/Financeira do item: Definir como será a utilização desta no item de movimento.
  + Controla Orçamento: Define se o tipo de movimento fará parte do controle orçamentário dentro da empresa. Após habilitados os seguintes campos devem ser parametrizados conforme conveniência:

> Efeito no orçamento: Definido neste campo qual será o efeito, aumenta ou diminui, sobre os valores dos tipos de orçamento que são Orçado, Real, Opcional1, Opcional2. Lembrando que a apresentação destes nomes pode variar conforme descrição definida pelo usuário nos parâmetros do Orçamento, “Descrição do Tipo de Orçamento”.
>
> Ação ao Exceder Orçamento: Define qual a ação será feita quando o saldo for excedido. Se avisa, barra, ou bloqueia.
>
> Data Default do Orçamento: Define entre as datas do movimento, qual será utilizada para controle do orçamento.
>
> Utiliza rateio no orçamento: Define se o rateio será utilizado no controle orçamentário ou não, caso seja as opções são: item ou do movimento. Lembrando que neste caso o sistema irá fazer a proporção do percentual/valor do rateio em relação ao valor do orçamento.
>
> Fórmula do valor unitário do orçamento: Neste campo será informado a fórmula do orçamento. Neste caso deverá ser informado o valor de uma unidade, pois para efeito do orçamento o sistema automaticamente multiplica a quantidade do item de movimento pela fórmula do valor orçado. Exemplo de Fórmula do valor do orçamento considerando o valor do IPI do item – desconto do item + despesa do item + frete rateado para o item:

> **KPU + (LVL ('IPI') - KDE + KDS + TABITM ('RATEIOFRETE' , 'V') ) / KQT**

***2.* *Cadastro das Tabelas de Orçamento***

Para acessar as tabelas a serem utilizadas neste processo acesse m*enu / Cadastro / Tabelas De Orçamento*, exceto para o caso da Natureza Orçamentária Financeira que fica localizado no m*enu / Cadastro / Tabelas Auxiliares*.

> Natureza Orçamentária/Financeira: É uma classificação generalizada para o cadastro do produto e/ou itens do movimento. Por meio dessa classificação o produto poder ser agrupado como se fosse uma conta de despesa para a realização do orçamento. Esta tabela também é utilizada em um relatório padrão de Fluxo de Caixa do TOTVS Gestão Financeira (RM Fluxus) com ou sem a opção de rateio. Exemplo: Despesas com Hospedagem, Material de Escritório, etc.
>
> Classificação do Período: É utilizado para definir classificações de períodos de orçamento. Assim, será possível ter periodicidades coincidentes, isto porque podem existir situações em que uma determinada área da empresa tem um período orçamentário diferente de outra área.
>
> Período do Orçamento: É utilizado para definir os períodos nos quais serão executados o orçamento. Nesta tabela não há uma periodicidade fixa, permitindo assim, que possam ser planejados orçamentos futuros que não interfira no vigente.
>
> Vinculo do Usuário ao Centro de Custo: Neste cadastro é definido para quais centros de custo o usuário esta autorizado a realizar movimentações orçamentárias.
>
> Vínculo da Natureza do Orçamento ao Centro de Custo: Por meio deste cadastro é possível definir para quais naturezas financeiras um centro de custo pode ser utilizados durante as movimentações.
>
> Vínculo do Centro de Custo a Classificação do Período: Por meio deste cadastro é possível realizar a vinculação do centro de custo à classificação do período. Isto é necessário para não permitir que um centro de custo faça parte de mais de um orçamento ativo.

> OBS: Um Centro de custo não pode ser vinculado a mais de uma classificação do período.

* Vínculo do Centro de Custo Agrupador: Neste cadastro é possível definir um centro de custo como agrupador de outros centros de custo. O Agrupador irá concentrar a utilização do orçamento para outros centros de custo vinculados a ele. Ao incluir um movimento para o centro de custo agrupado (filho) o orçamento afetado é o definido para o centro de custo agrupador (pai). Para permitir maior flexibilidade no agrupamento dos centros de custo, as suas vinculações serão definidas por período orçamentário.

* Cadastro dos Valores Orçados: Esta tabela será utilizada para o registro e acompanhamento dos orçamentos.

> Neste cadastro será possível:

> Acompanhar o histórico de alterações realizadas diretamente no valor orçado;
>
> Consistir a alteração do valor orçado para que não ultrapasse o valor real já empenhado;
>
> Apenas os orçamentos dentro do período de movimentação global poderão ser alterados;
>
> A permissão de acesso seguirá o padrão dos demais cadastros visto que a manutenção dos orçamentos é feita de forma centralizada.

***3.* *Valores do Orçamento***

A consulta dos valores orçados pode ser feita pelo menu / Utilitários / Consulta dos Valores Orçados. Qualquer movimentação que for realizada no orçamento sempre ira afetar a tabela de saldo do orçamento e também ira incluir um registro na tabela (TMOVORCAMENTO) que foi criada para guardar as movimentações do orçamento, seja alterada via movimentação ou via cadastro de valores orçados.

A tabela de Saldo do orçamento terá os seguintes campos de valores:

> Valor Orçado: Este valor é alterado somente pela tela de manutenção do cadastro de orçamento.
>
> Valor Opcional 1 e 2: Os valores Opcional 1 e Opcional 2 são valores intermediários que podem ser configurados no efeito do orçamento por tipo de movimentos.
>
> Valor Excedente: Este valor é atualizado automaticamente, quando algum item do movimento excede o saldo do orçamento disponível no período, e o movimento fica com o status de bloqueado.
>
> Valor Realizado: Este valor é a ultima etapa que deve ser configurada para o efeito dos valores do orçamento.
>
> Valor Recebido e Valor Cedido: Estes valores são utilizados automaticamente na utilização do assistente que faz a transferência de valores do orçamento, para desbloquear um movimento.
>
> **- Saldo Disponível do Orçamento: A fórmula para chegar ao saldo disponível do orçamento por período é a seguinte:**

> **- Saldo do Período = Valor Orçado – (Valor Opcional 1 + Valor Opcional 2 + Valor Realizado) - Valor Cedido + Valor Recebido + Valor Excedente**

***4.* *Aplicação do Controle Orçamentário***

Para um melhor entendimento sobre a aplicação do “Controle Orçamentária” iremos exemplificar dentro de um caso pratico em uma Gestão de Compra (*Solicitação > Ordem de Compra > Nota Fiscal de Entrada*).

4.1. Parametrização das movimentações e cadastro dos valores do orçamento.

* Parametrização dos Tipos de Movimentos:

> *Solicitação de Compras*: Aumenta o valor opcional 1, neste caso chamado de *“Reserva”.*
>
> *Ordem de Compras*: Aumenta o valor o valor opcional 2, neste caso chamado de “*Comprometido*”*.*
>
> *Nota Fiscal*: Aumenta o valor realizado.

* Cadastro dos Valores do período:

> Período = 01/01/20XX à 31/12/20XX
>
> Natureza do Orçamento = Material de Escritório
>
> Centro de Custo = Marketing
>
> Valor do Orçamento = 5.000,00

4.2. Inclusão das movimentações

* Inclusão do movimento de **“Solicitação de Compras”** com os seguintes dados:

+ Data de emissão/data do orçamento = 15/01/20XX.
+ Centro de custo do orçamento = Marketing
+ Natureza do Orçamento = Material de Escritório
+ Valor do orçamento = R$ 1.500,00

Foi incluído o movimento de solicitação de compras com os dados descritos acima no valor de **R$ 1.500,00**, acreditando que será gasto este valor para atender esta solicitação.

Salvo o movimento, foi consultado o saldo do orçamento que retornou os seguintes valores:

Orçado =                               5.000,00

(-) Real =                                       0,00

(-) Reserva =                         1.500,00

(-) Comprometido =                      0,00

(+) Valor Recebido =                    0,00

(-) Valor Cedido =                        0,00

(+) Valor Excedente =                 0,00

**= Saldo (Disponivel) =        3.500,00**

OBS: Como a solicitação aumente o saldo Reserva o sistema deixa como saldo disponivel apenas **R$ 3.500,00**

* Inclusão do movimento de **“Ordem de Compra”.**

Após negociação entre do setor de compra da empresa e seu fornecedor, ficou fechado os valores para atender a solicitação de compras, conforme dados abaixo.

> Centro de custo do orçamento = Marketing
>
> Natureza do Orçamento = Material de Escritório
>
> Valor do orçamento = R$ 1.600,00.

Assim o movimento de Solicitação de Compras foi faturado/recebido gerando a Ordem e Compras. Após salvar o movimento, foi consultado o saldo do orçamento que passou a apresentar os seguintes valores:

Orçado =                                         5.000,00

(-) Real =                                                 0,00

(-) Reserva =                                          0,00

(-) Comprometido =                        1.600,00

(+) Valor Recebido =                              0,00

(-) Valor Cedido =                                  0,00

(+) Valor Excedente =                          0,00

**= Saldo (Disponivel) =                 3.400,00**

**Observação 01: Todo movimento faturamento/recebimento que afete os valores do orçamento, terá seu saldo definido no tipo de movimento estornado, isto porque em um faturamento parcial o sistema estorna o saldo do orçamento e afeta novamente apenas para os itens não faturados.**

Observação 02**: Para o caso de faturamento/recebimento de movimento é SEMPRE recomendado trabalhar com o parâmetro “Baixar Pedido de Compra/Venda após Geração do Movimento” como “Baixar Sempre”.**

* Inclusão do movimento de **“Nota Fiscal”.**

Após fechamento das condições junto ao fornecedor feito na Ordem de Compra, ficou acertado que parte da mercadoria seria entregue de imediato e parte seria entregue em uma posterior oportunidade. A primeira Nota Fiscal afetou o realizado em **R$ 1.000,00**,deixando pendente o valor de **R$ 600,00** do valor comprometido da Ordem de Compra que ainda não foi recebido.

Após a inclusão do movimento de *Nota Fiscal* proveniente do faturamento da *Ordem de Compra*, foi consultado o saldo do orçamento que passou a apresentar os seguintes valores:

Orçado = 5.000,00

(-) Real = 1.000,00

(-) Reserva = 00,00

(-) Comprometido = 600,00

(+) Valor Recebido = 0,00

(-) Valor Cedido = 0,00

(+) Valor Excedente = 0,00

**= Saldo (Disponivel) = 3.400,00**

OBS1: O saldo comprometido permaneceu em **R$ 600,00** porque a ordem de compra não foi recebida em sua totalidade.

***5.* *Realocação Orçamentária***

Este recurso é utilizado para a liberação de movimento que trabalha com o orçamento, mas que esteja com o status do movimento como “**Bloqueado**”, ou seja, quando o valor do orçamento do item de movimento for maior que o orçamento disponível. O movimento só terá o status de “**Bloqueado**” quando o tipo de movimento estiver parametrizado para este procedimento.

Para visualizar os movimentos que estão bloqueados por falta de verba do orçamento, o usuário deverá acessar o menu *Opções / Realocação Orçamentária* e será apresentada uma grid com todos os movimentos bloqueados.

Para desbloquear um movimento, o usuário deve selecionar o movimento na lista, e clicar no botão “**Assistente de Realocação**”. O assistente é aberto com todos os itens que excederam o orçamento do movimento selecionado. Após selecionar os itens que deseja desbloquear, e clicar no botão avançar, é apresentada uma tela com as opções de realocação respeitando as regras definidas no perfil do usuário, que são:

+ Realoca entre Naturezas do Centro de Custo.
+ Realoca entre Naturezas e Centros de Custo que está Associado.
+ Realoca entre Naturezas e Centros de Custo que está Associado, com Valores dos Períodos Anteriores.

Para liberar o orçamento excedente, o usuário pode retirar valores de valores orçamentos até atingir o valor necessário.

***5.1.* *Procedimento para Realocação Orçamentária***

1. Acesse o menu Opções / Realocação Orçamentária;

2. Selecione ou cria um filtro, e em seguida execute o filtro;

3. Serão apresentados todos os movimentos bloqueados;

4. Clique no botão “Assistente de Realocação” para desbloquear o movimento;

5. O assistente será aberto com todos os itens que excederam o orçamento do movimento selecionado;

6. Selecione o item de movimento a ser desbloqueado;

7. Clique no botão “Avançar”;

8. Será apresentado uma tela do assistente chamado “Transferência”;

9. Selecione o Orçamento de Origem e o Valor de Transferência;

10. Clique na “Seta azul com indicação para baixo” para confirmar o valor a transferência;

11. Clique no botão “Avançar”;

12. Será apresentada uma tela de confirmação com os seguintes dizeres “Realocação Efetuada com sucesso!”

13. Basta acessar o movimento bloqueado para verificar que o status do movimento não esta mais como bloqueado.

***5.2.* *Procedimento para Consultar Valores do Orçamento***

1. Acesse o menu Utilitários / Consultar Valores do Orçamento;

2. Será apresentada uma janela chamada “Consulta de Orçamento”;

3. Na Pasta Dados da Consulta são apresentados três novas subpastas para serem filtrados;

4. Filtre o orçamento conforme conveniência;

5. Selecione os registros da tela “Resultado da Consulta”;

6. Clique na Pasta Consulta;

7. Serão apresentados os orçamentos disponíveis do sistema;

8. Na Pasta de Consulta, existem as opções de “Agrupamento de Centro de Custo ou Natureza” e “Agrupamento de Período”, para melhor visualizar os orçamentos de forma agrupada.

Obs.: É possível utilizar o controle orçamentário a partir do TOTVS Gestão Financeira. Veja a documentação [clicando aqui.](http://tdn.totvs.com.br/download/attachments/185734326/Boletim%20t%C3%A9cnico%20-%20Or%C3%A7amento%20financeiro.pdf?version=1&modificationDate=1424898844000&api=v2)

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Rpt/Rpt.Reports.aspx)

**COMUNIDADE **[R@Materiais e Finanças](https://totvs.byyou.com/?space=rmateriais)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015
