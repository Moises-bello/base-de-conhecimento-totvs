---
content_hash: 50fd54dd5f0e9ac0f5ec52aaaf210f1650a709ecada7f1c7187a5827087ae3f8
fetched_at: '2026-06-29T00:10:08.513898+00:00'
page_id: '452719528'
product: rm
source: tdn-rm
title: Tabelas de Cálculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719528
version: 10
---

Este cadastro guarda as tabelas de cálculo, que são utilizadas na montagem de fórmulas, para cálculo de eventos como INSS, comissão, etc. Isso permite, por exemplo, controlar as várias faixas de cobrança de determinado tributo.

**Janela de Visão**

Nesta janela de cadastro, são visualizados, no lado esquerdo, dados de identificação e vigência de cada tabela e, no lado direito, os itens (valores) da tabela selecionada (aquela em que estiver posicionado o cursor).

**Identificação**

Nesta pasta, informam-se os dados de identificação de cada tabela de cálculo. Pode-se cadastrar mais de uma tabela de cálculo com o mesmo código, desde que tenham períodos de vigência distintos.

**Atenção 1:**

As tabelas de INSS e IRRF devem ser cadastradas obrigatoriamente. Somente devemos criar uma nova tabela se houver alteração nos valores ou alíquotas. Caso contrário o usuário deverá ser prorrogada a data de termino da vigência.

**Atenção 2:**

Somente devemos criar uma nova tabela se houver alteração nos valores ou alíquotas. Caso contrário o usuário deverá ser prorrogar a data de termino da vigência. Nesta pasta, encontraremos os seguintes campos:

**Código**

Informe um código alfanumérico (limite: seis posições) para a tabela.

**Finalidade**

Selecione uma finalidade para a tabela de cálculo, conforme as opções: 0 - sem finalidade específica Tabelas de cálculo criadas com essa finalidade são utilizadas em cálculos de eventos gerais, de acordo com a necessidade do usuário.

1 – INSS São as tabelas que o sistema utiliza para o cálculo do INSS.

2 – IRRF São as tabelas que o sistema utiliza para o cálculo do IRRF.

3 – RRA

4 – IRRFPL    (São as tabelas que o sistema utiliza para o cálculo do IRRF sobre Participação nos Lucros.)

5 – INSS\_REFORMA   ([Como fazer Transição para o cálculo finalidade 5 - INSS\_REFORMA](https://tdn.totvs.com.br/pages/editpage.action?pageId=532663681))

**Início Vigência**

Informe o início da vigência da tabela. Use o botão à direita do campo para acessar o calendário e selecionar a data.

**Final Vigência** I

Informe o início da final da tabela. Use o botão à direita do campo para acessar o calendário e selecionar a data. **V**

**Visualizar gráfico de datas cadastradas** Ao acessar esta pasta de identificação, será visualizada um gráfico (régua) com todos os períodos vigência cadastrados para a tabela em questão. Se a opção for desabilitada, o gráfico deixará de ser visualizado. Porém, se a pasta for fechada e novamente acessada, o gráfico será novamente visualizado. Para deixar de visualizar o gráfico deve-se fechar o gráfico ou então utilizar o botão ESC.

**Descrição**

Nome/descrição da tabela (limite: 30 caracteres).

**Arredondar valor:** Habilitando esta opção, o sistema irá arredondar valores calculados conforme a aplicação das tabelas de Cálculo.

*Exemplo*:

Base de IRRF: 2.247,67 \* 7,5% = 168,57525 - 117,49 (valor dedutível) = 51,08525.

* Com o parâmetro marcado, irá lançar no envelope de pagamento o valor de 51,09.
* Com o parâmetro desmarcado, irá lançar no envelope de pagamento o valor de 51,08.

Observação:

O parâmetro “Arredondar valor” não se aplica à tabelas com finalidade ligadas ao INSS porque de acordo com a legislação, o valor será truncado. Veja exceção no parâmetro “[Arredonda INSS teto quando funcionário possui outro vínculo de terceiros](https://tdn.totvs.com.br/display/public/LRM/Encargos+Sociais)” 

**Atualiza final de vigência na liberação da competência**

Este parâmetro se destina a permitir que o usuário escolha para cada registro na devida tabela se seu final de vigência deve ser atualizado ou não na liberação de competência.

**Desprezar centavos** Selecione esta opção se pretender que sejam desprezados os centavos dos valores informados na tabela. Este botão permite copiar registros de tabelas de uma coligada para outra.

Dica

Quando as tabelas de cálculo das finalidades de INSS e IRRF são alteradas, e a competência atual da folha de pagamento está dentro da vigência dessas tabelas, os envelopes de pagamento calculados anteriormente passam a ficar pendentes de recálculo. 

Veja seção IMPORTANTE sobre o Recálculo Automático do envelope no TDN do [Envelope de pagamento](https://tdn.totvs.com.br/display/public/LRM/Envelope+de+Pagamento)

Valores da Tabela  
IRRFPL  
Folha de Pagamento  
Copiar Tabelas de Cálculo Entre Coligadas
