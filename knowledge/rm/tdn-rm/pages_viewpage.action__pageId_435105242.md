---
content_hash: de417e6156c29467f68393743cc6be962ef0580f0b27b6d66a07b37e3db2acf3
fetched_at: '2026-06-29T00:09:49.140929+00:00'
page_id: '435105242'
product: rm
source: tdn-rm
title: Contratos de Venda - Dados Gerais - Identificação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105242
version: 17
---

Nesta pasta, serão informados os dados que identificarão a Venda/Aluguel cadastrada.  
Campos a serem preenchidos:

**Tipo Contrato:** Nesta opção o usuário irá selecionar se contrato será uma Venda.  
**Venda/Aluguel:** Informe o Número da venda cadastrada.

O número da venda será sequencial ou não, dependendo da parametrização do sistema. Caso o parâmetro "Venda Sequencial" Menu Ambiente | Parâmetros | TOTVS Incorporação| Contrato | Venda/Aluguel, esteja marcado, ao criar a venda, o sistema incluirá um número de venda. Caso o parâmetro esteja desmarcado, o usuário deverá informar um número de venda.

**Número do Contrato:** Após a efetivação da venda e a geração do contrato neste campo aparece o número referente ao contrato.

Este campo não pode ser editado. Ele somente irá mostrar o número do contrato depois que ele for gerado.

**Empreendimento:** Selecione o empreendimento da venda/aluguel.   
**Referência de entrega para o componente:** Determina qual tipo de data será usada como referência de entrega, para os componentes geradores de parcela e de Juros e Correção Monetária.

Tendo as seguintes opções:

* Data de entrega do empreendimento;
* Data do habite-se;
* Data da entrega das chaves;
* Data de assinatura.

**Tabela de Preço**: Selecione a tabela de preço que será utilizado na venda. Através da Tabela de Preço é possível determinar qual será o preço do Item de Contrato da Venda. Para maiores informações sobre a Tabela de Preço .   
**Modalidade:** Selecione a Modalidade que será utilizada na venda. A Modalidade tem como função definir um modelo de Grupos  e Componentes que irão compor as Condições da Venda. As condições podem ser alteradas mesmo possuindo uma Modalidade Associada a Venda.    
Na lista de opções serão apresentadas todas as modalidades cadastradas através do Menu Cadastro | Modalidade Venda;  
Ao incluir ou editar um contrato de locação o usuário possa optar por preencher ou não o campo "Modelo de Contrato".

Através do parâmetro "Restringe modalidade de venda", que se encontra no seguinte caminho Ambiente|Parâmetros|Totvs Incorporação|Contrato|Modalide, é possível definir quais modalidades poderão ser exibidas para a venda, são elas:

* + **Por Empreendimento**: Será exibida somente as Modalidades que estão associada ao Empreendimento;
  + **Não restringe**: Será exibida todas as Modalidades cadastradas;
  + **Por tabela de preço:** Será exibido somente a Modalidade associada a Tabela de Preço da venda;

**Conta Caixa:** Informe qual Conta Caixa será utilizada na venda, onde fará integração com o TOTVS Gestão Financeira. Ao gerar os Lançamentos Financeiros no Gestão Financeira, os mesmo já serão vinculados a Conta Caixa informada.   
**Campo Livre:** Esse campo é possível escrever qualquer observação necessária na venda. Ele pode ser editado em qualquer Situação da Venda.    
**Data Venda/Aluguel:** Informe qual é a data em que a venda foi criada

 Se o parâmetro "Usar data do sistema para a data da venda", através do Menu Ambiente|Parâmetros| TOTVS Incorporação|Contrato|Venda|Parâmetros do Contrato por Coligada   , estiver marcado, ao criar uma venda, este campo será preenchido automaticamente com a data do sistema.

**Data do Cancelamento:** Caso a venda esteja com a situação cancelada, o sistema irá mostrar neste campo a data do cancelamento;  
**Data Base:** É a data base que o sistema irá tomar como padrão para efetuar as correções do plano de financiamento, quando os componentes de reajuste estiverem parametrizados para utilizar a Data Base da Venda;  
**Data Cadastro:** Campo preenchido automaticamente pelo sistema com a data atual do sistema no dia em que foi realizada a inclusão da venda;  
**Data de Entrega das Chaves:** Informe a data que o cliente receberá as chaves do seu imóvel;  
**Data da Assinatura:** Informe a data de Assinatura desta venda;  
**Data Previsão Entrega:** Informe a data de previsão de entrega da subunidade desta venda;  
**Data de quitação:** Caso a venda esteja com a situação Quitada, o sistema irá mostrar neste campo a data da quitação. Esse campo é preenchido automaticamente com a mesma Data de Baixa da última parcela em aberto deste Contrato de Venda;  
**Dia de Vencimento:** Caso o usuário informe um dia ele será sobreposto ao dia de vencimento da primeira parcela informado na regra geradora de parcela, caso não seja informado o sistema permanece com comportamento padrão. Caso o usuário configure utilizar dia útil este irá sobrepor o dia de vencimento informado no contrato de venda  
**Número do atendimento:** Aqui será informado qual o número da solicitação de atendimento que está responsável pela entrega das chaves. Esse campo é preenchido com a execução do processo de entrega de chaves.

**Item Contrato**  
Nesta área deverá ser cadastrado a Subunidade que será utilizado na Venda/Aluguel.  
Campos a serem preenchidos:

**Empreendimento:** Campo traz automaticamente o nome do Empreendimento que foi cadastrado na Venda.

Este campo não poderá ser editado, pois o empreendimento já foi cadastrado na venda.

**Unidade:** Informe a Unidade do Empreendimento cadastrado na Venda e que contenha a Subunidade desejada;  
**Sub-Unidade:** Informe a Sub-unidade da Unidade cadastrada anteriormente;  
**Tabela de Preço:** Campo que é preenchido com a tabela de preço da Sub-Unidade cadastrada anteriormente. Esse campo é preenchido;  
**Valor do Item:** Informe o valor da Sub-Unidade.

O campo será preenchido automaticamente caso a subunidade possui tabela de preço vinculada.  
Esse campo pode ser bloqueado para edição, caso o parâmetro "Valor do item da venda", que se encontra no seguinte caminho Ambiente|Parâmetros TOTVS Incorporação|Contrato|Tabela de Preço, estiver com a opção "Mostra";

**Valor de Acréscimo:** Informe o valor de acréscimo da Sub-unidade, se houver.  
**Valor de Desconto:** Informe o valor de desconto da Sub-unidade, se houver.  
**Valor Comissão Pago Pelo Cliente (Na Mesa):** Informe o valor da comissão pago pelo cliente diretamente ao corretor, esse valor não entra no plano de financiamento e deve ser descontado da tabela de preço ou do valor do item. **\*A partir da versão 12.1.2205**  
**Valor de líquido : Valor do Item + Valor de Acréscimo - Valor de Desconto - Valor Comissão Pago Pelo Cliente** . **\*A partir da versão 12.1.2205**

**Situação:** Este campo é controlado pelo sistema e informa a situação que a venda está naquele momento.

As situações podem ser:

* **Em Preparação:** 1ª situação da venda;
* **Efetivada:** como o próprio nome diz, quando a venda já foi efetivada;
* **Quitada:** situação alterada automaticamente quando a última parcela do plano de financiamento é quitada;
* **Distratada:** quando a venda foi cancelada por um distrato;
* **Cancelada:** quando a venda foi cancelada pelo processo "Cancelar Contrato";
* **Bloqueada**: esta é a única situação que o sistema não controla, ou seja, o usuário coloca uma venda como bloqueada e automaticamente a sub-unidade também fica bloqueada;

**Ref. de Entrega:** Exibe o valor selecionado no campo "Referência de entrega para o componente".  
**Data Venda:** Exibe o valor informado no campo Data Venda/Aluguel  
**Valor da Venda:** Valor do contrato definido no campo Valor do Item no cadastro do item da Venda/Aluguel.  
**Valor Total Acréscimo:** Valor de acréscimo da venda.   
**Valor de Desconto Contrato:** Exibe o valor de desconto do Contrato.   
**Valor Total Financiamento:** Exibe o valor total financiado no Contrato.   
**Baixado(%):** Representação gráfica que mostra a soma de todos os valores baixados no contrato.  
**Valor Venda Atualizado:** Valor da venda atualizado por meio de reajustes e aditivos.  
**Valor Desconto Baixado:** Soma de todos os **valores baixados** dos componentes de desconto, ou seja, soma os valores de integração correspondentes ao tipo de componente de desconto **código 900.** Caso deseje que o somatório contemple também o valor de baixa do desconto financeiro, deverá ser apenas cadastrado no cadastro de componente, um componente do tipo desconto financeiro de **código 910** para que o TOTVS construção Gestão de Imóveis consiga somar o desconto financeiro baixado a este campo de valor desconto baixado da venda.

**Total Baixado:** Soma de todos os valores baixados no contrato. Representa a soma do valor original baixado das parcelas do contrato. Também são considerados os valores financeiros (Juros, desconto, multa e etc....) no cálculo.  
**Saldo Devedor:** Soma de todos os valores em aberto restantes do contrato.  
**Valor Crédito:** Exibe o valor de Crédito no Contrato.

false

Veja Também

---
