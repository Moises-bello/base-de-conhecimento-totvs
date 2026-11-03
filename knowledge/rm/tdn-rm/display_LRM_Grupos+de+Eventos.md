---
content_hash: b620b543317e61396ca07f518030c6de40c39e69e88a6548fade77d68723494f
fetched_at: '2026-06-29T00:10:07.308585+00:00'
page_id: '452719397'
product: rm
source: tdn-rm
title: Grupos de Eventos
type: documentation
url: https://tdn.totvs.com/display/LRM/Grupos+de+Eventos
version: 10
---

Através de módulo o usuário poderá fazer o lançamento de todo o movimento mensal do funcionário, tais como Vale Transporte, Empréstimo, Códigos Fixo, Eventos Programados, Salário Maternidade e outros.

Parâmetro **'Lançar salário maternidade'**  
Faz o lançamento o evento de código de cálculo 17 – Salário maternidade e sua respectiva média parametrizado no sindicato no movimento do funcionário. Caso seja necessário lançar o salário maternidade no mês posterior ao início da licença maternidade, devido a entrega do atestado ter ocorrido após o fechamento da folha, marque também o parâmetro **‘Recalcular média após o primeiro mês da licença’.**

**Atenção:**

1 – Quando o recálculo da média é selecionado todo o cálculo da média será refeito, mas sempre considerando como referência o mês de início da licença maternidade. E o campo na pasta Parâmetros do cadastro de funcionários será sempre atualizado toda vez que houver recálculo. Então caso haja alguma alteração no sindicato, por exemplo, acarretará alteração no valor da média de licença maternidade e alteração no campo que armazena este cálculo.

2 – Este recálculo de médias não será feito caso a situação do funcionário for D – demitido.

Parâmetro **'Lançar verbas com Insuficiência de Saldo do mês ou período anterior'**  
Armazena os descontos dos eventos lançados nas verbas do mês/período anterior que causaram insuficiência de saldo.  
Este processo é executado somente para o funcionário que tem o parâmetro Utiliza Controle de Saldo de Verbas em Cadastros | Funcionários | Parâmetros marcado.  
   
**Exemplo I:**  
O funcionário está com débito de R$ 700,00 de farmácia conveniada à empresa, e possui total de proventos R$ 500,00, o sistema armazena o saldo relativo a diferença entre proventos e descontos(R$ 200,00) na tabela PFVERBAS.   
No caso do funcionário não possuir saldo para desconto da verba no mês atual, o desconto é efetuado no meses posteriores.   
   
**Atenção I:**  
A ordem de lançamento dos eventos de descontos que geraram saldo negativo é por ordem de prioridade do evento. Quando os eventos tem a mesma prioridade, a segunda ordem é o código do evento. Porém o INSS, IRRF e Pensão Alimentícia tem prioridade de desconto superior a qualquer ordem.  
   
**Atenção II:**  
Os descontos do período ou competência anterior somente serão lançados quando o parâmetro Lança eventos da integração com insuf. saldo do mês/período anterior estiver marcado. Porém para o envelope atual a cada recálculo, o sistema verifica se existe saldo para lançamento dos eventos de insuficiente de saldo do envelope atual.  
   
**Atenção III:**  
A cada recálculo o sistema verifica a necessidade de guarda os descontos na aba Verbas c/ Insuficiência de Saldo tabela PFVERBAS.  
   
**Atenção IV:**  
O código de cálculo 20-ARREDONDAMENTO PROVENTO somente é lançado quando o funcionário utiliza arredondamento no cadastro de funcionário.  
   
**Atenção V:**  
Quando o parâmetro Desconto Perdoado existente em Cadastros | Eventos | Aba Inc. Descontos estiver marcado este evento é gravado na tabela PFVERBAS com o campo DESCONTADO igual a 1, para não ser lançado no movimento.  
   
**Atenção VI:**  
No lançamento do Vale Transporte (código de cálculo 6) e Contribuição Sindical (código de cálculo 12)o sistema calcula o valor e abate o valor já descontado.  
   
**Atenção VII:**  
A insuficiência de saldo não verifica data de pagamento.   
**Exemplo:**   
O desconto de faltas foi lançada no movimento com data de pagamento 31/12/2010 (Período 1) e o funcionário foi demitido em 30/12/2010 (Período 2), mesmo as faltas tendo sido descontada com data posterior a rescisão, o sistema desconta as faltas na rescisão.  
O mesmo ocorre com o lançamento do movimento para o próximo mês. Se lançarmos faltas com insuficiência de saldo para o próximo mês e se no mês atual recalcularmos o envelope com saldo, o sistema desconta as faltas na competência atual.  
   
**Observação I:**  
Para visualizar o saldo de verbas é preciso selecionar em Cadastros | Funcionários | Ficha Financeira a aba 'Verbas com Insuficiência de Saldo'.  
   
**Observação II:**  
Para lançar o débito do mês anterior, é necessário marcar o campo 'Lançar Verbas com Insuficiência de Saldo do mês ou período anterior' no módulo Movimento | Folha de Pagamento | Lançamentos Automáticos | Grupo de Eventos.

Parâmetro **'Lançar Provisionamento do Empréstimo do Crédito do Trabalhador eSocial'**

Parâmetro indicado para lançamento de verba de adiantamento na folha de pagamento. Marcando esse parâmetro o sistema lançará no movimento uma verba para provisionamento do empréstimo cadastrado com a modalidade "Crédito do Trabalhador eSocial".

A provisão será calculada proporcionalizando o valor do empréstimo da modalidade "Crédito do Trabalhador eSocial" de acordo com o percentual cadastrado em Parâmetros do cadastro de funcionários.

Com o parâmetro 'Lançar Provisionamento do Empréstimo do Crédito do Trabalhador eSocial' desmarcado não será lançado a provisão no movimento do funcionário.

Atenção:

* Quando o parâmetro de provisionamento estiver marcado desabilitará o parâmetro ‘Lançar Empréstimo'’
* Quando o parâmetro de 'Lançar Empréstimos' estiver marcado desabilitará o parâmetro 'Lançar Provisionamento do Empréstimo do Crédito do Trabalhador eSocial'

Veja exemplo em

Parâmetro **'Lançar Empréstimos'**

Esse parâmetro marcado lançará todos os empréstimos ou o empréstimo indicado no tipo de empréstimo. Esse tipo de empréstimo é indicado no cadastro de Empréstimo no anexo do cadastro de Funcionários.

IMPORTANTE:

O lançamento do empréstimo via grupo de eventos não é feito para funcionário demitido, caso queira lançar via grupo de eventos deve ser lançado antes da demissão.

Veja informação de como lançar empréstimos diretamente na demissão em [Cadastro de Rescisão](https://tdn.totvs.com/pages/releaseview.action?pageId=452719347)

Parâmetro **'Lançar Eventos Programados**'   
Quando este parâmetro estiver marcado o sistema irá lançar o evento no movimento por centro de custo (PFMOVCC) e o campo EDITADO será igual 1, isso para que a cada recálculo da folha estes eventos permaneçam com o centro de custo do evento programado.  
   
Caso o evento programado não tenha centro de custo informado, o sistema irá buscar o centro de custo do rateio fixo do cadastro do funcionário, e o campo EDITADO será 0 (zero).  
   
Sempre que existir o mesmo evento, na mesma vigência, e com o mesmo centro de custo, o sistema irá somar o valor.  
   
Quando existir um evento com centro de custo e outro sem centro de custo, o sistema não irá lançar o evento programado sem centro de custo, isso porque o campo EDITADO irá ficar igual a 1 e é regra do sistema sempre que os valores não podem ser alterados.  
Ordem do rateio por centro de custo:  
1. Entrada de Dados por Centro de Custo  
2. Centro de Custo Informado (Evento/Eventos Programados)  
3. Código do Rateio que o (Evento/Encargo Contábil/Lançamento Financeiro) Segue  
4. Segue Rateio Movimento de Ensino Importado (este rateio é somente para que utiliza Cálculo .Net e Movimento de ensino importado não precisa homologar)  
5. Rateio Fixo do Cadastro do Funcionário
