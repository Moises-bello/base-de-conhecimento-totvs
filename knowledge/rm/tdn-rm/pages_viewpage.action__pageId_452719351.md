---
content_hash: 0eaba9a5fe1072a0cfe70744baa875570d79b4cd1364c7f72c7d2fb7b05f41ff
fetched_at: '2026-06-29T00:10:06.936682+00:00'
page_id: '452719351'
product: rm
source: tdn-rm
title: DIRF/Informe de Rendimentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719351
version: 20
---

A DIRF (Declaração do Imposto de Renda Retido na Fonte) é a Declaração feita fonte pagadora, com o objetivo de informar à Secretaria da Receita Federal do Brasil:

* O valor do Imposto de Renda e/ou Contribuições retidos na Fonte, dos rendimentos pagos ou creditados para seus beneficiários
* O pagamento, crédito ou remessa a residentes ou domiciliados no exterior, ainda que não tenha havido retenção do imposto, inclusive nos casos de isenção ou alíquota zero
* Os rendimentos isentos e não tributáveis de beneficiários, pessoas físicas e jurídicas domiciliadas no País
* Os pagamentos de plano de Assistência à Saúde – coletivo empresarial

Neste módulo será possível gerar a DIRF em arquivo conforme o layout disponibilizado pela Receita Federal do Brasil do ano base corrente e do Informe de Rendimentos.   
  
Recursos da DIRF:

* Gravar perfil de parâmetros de geração;
* Geração multi-coligada;
* Personalização dos relatórios Informe de Rendimentos e DIRF para Conferência;
* Melhor Performance;

**Utilizado o Módulo DIRF**  
 É importante observar que ao abrir o módulo DIRF, o usuário terá a opção de digitar um nome no campo "Perfil".

Este perfil gravará todos os parâmetros definidos nos campos respectivos para gerar as Saídas. Inclua o nome do Perfil e em seguida marque o campo "Salvar Perfil ao Concluir";  
Sugerimos que o primeiro perfil seja incluído para a "Parametrização da DIRF em arquivo", pois a partir deste facilitará a criação dos demais perfis.

**Parâmetros Gerais**  
 Na tela de parâmetros gerais, deverá ser definido os Parâmetros de Seleção que consistem em:

* **Quebra de Seção**: código de quebra centralizador. Geralmente é identificado como uma interrogação , sendo que esta representa a "Seção Coligada", geralmente representada pelo 0 (zero), cadastrada no Cadastro de Seções.
* **Competência:** defina a Competência Inicial = 01, Competência Final = 12 e Ano = "Ano base". O sistema irá verificar a existência de eventos na ficha financeira que possuem data de pagamento com os mesmos meses informados neste campo.
* **Seleção de Funcionários**: seleção para definir os funcionários que serão relacionados.
* **Gerar no Final do Processo**:
  + *DIRF em arquivo***:** Arquivo que será gerado no layout definido anualmente pela legislação regulamentadora, para envio a RFB dos valores de rendimentos tributáveis ou não.
  + *DIRF para conferência***:** Relatório de conferência dos valores da DIRF. Marcando esta opção, o processo solicita que o usuário informe o código do relatório da DIRF para conferência no campo específico
  + *Informe de Rendimentos***:** Relatório de Informação dos Rendimentos do ano base de cada funcionário. Os campos deste relatório são definidos pela legislação regulamentadora da DIRF. Marcando esta opção, o processo solicita que o usuário informe o código o relatório do Informe de rendimentos no campo especifico
* **Código Relatório – DIRF Conferência:** Informe o relatório que será gerado quando selecionado para gerar no final do processo a opção 'DIRF para conferência'. O sistema disponibiliza o relatório FOPREL0007 – DIRF para conferencia.
* **Código Relatório – Informe Rendimentos:** Informe o relatório que será gerado quando selecionado para gerar no final do processo a opção 'Informe de Rendimentos'. O sistema disponibiliza três tipos de relatórios de Informe de Rendimentos: FOPREL0008 – Informe de Rendimentos, FOPREL0011 – Informe de Rendimentos detalhado, FOPREL0012 – Informe de Rendimentos em TXT.
* **Utiliza Layout Modificado – DIRF em arquivo:** marcando esta opção, o processo habilita o campo 'Gerador de Saídas – DIRF em Arquivo', onde o usuário é obrigado a informa o código do relatório do layout do Modificado da DIRF em arquivo.

**Observações:**

O módulo da DIRF permite utilizar relatórios personalizados para geração do Informe de Rendimentos e DIRF para conferencia, que devem ser importados pelo RM Reports e referenciados nos campos respectivos "Código do Relatório – DIRF para conferência" e "Código do Relatório – Informe de Rendimentos".

***Opções de Seleção:***

* **Funcionários ou Autônomos**
  + *Apenas com IRRF*: Imprime apenas funcionários que sofreram desconto de IRRF
  + *Com IRRF ou autônomos com rendimentos acima de R$6.000,00 ou assalariado com rendimentos acima de 28.123,91*: Imprime os funcionários autônomos e assalariados que, no ano calendário, entraram em alguma das condições descritas conforme a RFB 1.216 de 15/12/2011
  + *Todos*: Imprime todos os funcionários com exceção daqueles que não tiveram pelo menos um dos seguintes rendimentos abaixo:
    - Qualquer valor de rendimento incidente em IRRF
    - Qualquer valor de desconto de IRRF
    - Bolsa de Estudo Recebida por Médico-Residente
    - Indenizações rescisão, PDV, acidente de Trabalho
    - Desconto de assistência (médico - odonto - hospitalares)
    - Valor de pensão ou aposentadoria por Moléstia grave ou acidente em serviço

**Observações:** Para o uso dos parâmetros acima: A RFB através da Instrução normativa determina que a DIRF deverá ser declarada por empresa (coligada), e deverão ser relacionados:

* + Todos os autônomos que no ano base tiveram rendimentos acima de R$6.000,00, ou que tiveram retenção de IRRF (mesmo que apenas em 1 mês do ano base), e
  + Todos os assalariados que no ano base tiveram rendimentos igual ou acima de R$ de 28.123,91, ou que tiveram retenção de IRRF (mesmo que apenas em 1 mês do ano base);

A sugestão é que seja utilizado o código de seção que representa da Coligada; que a seleção de funcionários seja toda marcada; e que seja marcada a opção "Com IRRF ou autônomos com rendimentos acima de R$6.000,00 ou assalariado com rendimentos acima de 28.123,91".  
É importante certificar-se de que antes de gerar a DIRF / Informe de Rendimentos, todos os lançamentos referentes ao caixa 12 (último caixa do ano) estejam processados, tais como lançamentos de folha, férias e rescisões.

**Opções**

*Considera movimentação de competência anterior para transferidos***:** Ao marcar este parâmetro, o sistema passará a considerar a movimentação da competência anterior à data de transferência. Este tratamento será feito para funcionários com admissão por transferência, cuja a data de transferência seja no primeiro dia de qualquer competência. Não marcando este parâmetro os eventos pagos em competência anterior ao mês da transferência não serão considerados.

**Exemplo:**

Funcionário é demitido por transferência no último dia do mês na coligada A (30/06/2007)  
E com última movimentação na competência 6 caixa 7  
Funcionário é admitido no primeiro dia do mês na coligada B (01/07/2007)  
Nesta situação com o parâmetro marcado o sistema passará a considerar a movimentação da competência 6 na coligada B ou no CNPJ destino.

*Selecionar somente funcionários com CPF preenchido:* Ao marcar este parâmetro, o sistema selecionará apenas os funcionários que tenham CPF preenchidos na pasta "Documentos" do seu cadastrado.

*Agrupar funcionários sem CPF como um único funcionário*: Marcando esta opção, o sistema agrupará todos os funcionários que porventura não possuem CPF cadastrado.

Desconsidera número de dependentes no mês da rescisão por transferência: Ao marcar esta opção funcionários com dependentes de IRRF transferidos no mês não terão o número de dependente deduzido em duplicidade no mês da transferência. Caso contrário a dedução ocorrerá duas vezes.

*Gerar Informe de Rendimentos em TXT*: Ao marcar esta opção o processo irá gerar o Informe de Rendimentos no formato .txt. Para que o processo gere o arquivo em .txt é necessário que o relatório importado no RM Reports e referenciado no campo "Código do Relatório – Informe de Rendimentos" seja o de código FOPREL0012 - Informe de Rendimentos em Arquivo TXT.

*Usar Responsável(DIRF em Arquivo) na geração do Informe de Rendimentos:*

*Ao marcar esta opção o campo 8 do informe de rendimentos sairá com as informações cadastradas no responsável da DIRF em arquivo, caso contrário sairá com as informações da coligada.*

**Localização do(s) arquivo(s)**: Informar o caminho onde serão salvos os arquivos gerados. Os arquivos são salvos em caminho informado no diretório com nome da coligada gerada  
  
  
**Seleção de Coligadas**  
  
O usuário poderá selecionar uma ou mais coligadas que deseja gerar a DIRF/Informe de Rendimentos. Serão listadas todas as coligadas que estão na mesma competência/ano.  
  
Selecionando os "checkbox" de cada coligada, o sistema processará a geração da DIRF multi-coligada.  
É importante observar, que deverão ser incluídas as parametrizações para cada coligada, clicando no botão "Adicionar parâmetros as Coligadas".  
  
O usuário possuí o recurso de copiar parâmetros e eventos entre coligadas. Os parâmetros copiados só ficam visíveis para o usuário, perfil e coligada do contexto da coligada que fez a cópia, não sendo acessível na coligada de destino.   
  
**Parâmetros da Coligada**  
  
A adição dos parâmetros as coligadas, consiste no preenchimento de dados do Responsável / empresa, e definição dos eventos respectivos a cada informação a ser prestada a DIRF/Informe de Rendimentos.  
  
Primeiramente, o usuário deverá verificar a necessidade de personalizar as Opções de Seleção da coligada. Se for necessário, basta clicar em "Usar parâmetros específicos" para que sejam habilitados os campos "Seleção de Funcionários" e a aba "Parâmetros específicos" que irá determinar as opções de seleção e de geração da DIRF, desconsiderando, portanto, para a coligada que tiver o parâmetro marcado, os parâmetros Globais definidos anteriormente.

* **Eventos:**

o    *Restituição de IRRF*: Informe o evento de restituição de IRRF que o sistema deverá considerar no campo 'Imposto de Renda Retido' do informe de rendimentos e da DIRF. Este evento não deve ter o código de cálculo 122 -  Restituição IRRF, pois o evento com o CC 122 vai reduzindo automaticamente o valor do IR retido para a DIRF, não sendo necessário informa-lo neste campo e caso seja informado o valor do abatimento será duplicado. Neste campo deve ser informado apenas quando utiliza-se outro evento para restituição de IRRF que não tenha o código de cálculo 122.  
  
o    *13º pago pela Previdência sobre Licença Maternidade*: Preencher este campo com o evento de 13º salário pago pela previdência sobre Licença Maternidade, lançado na ficha financeira durante o período informado no campo 'Período Referência' para a empregada gestante com afastamento iniciado entre 12/1999 a 31/08/2003, ou para segurada empregada doméstica, contribuinte individual, trabalhadora avulsa e segurada especial. Nos demais casos este campo deverá ficar em branco.

**Aba Parâmetros Específicos**  
Comtempla todas as opções de seleção dos parâmetros globais, exceto a opção 'Gerar Informe de Rendimentos em TXT'.

* **Usa filtro de seleção ao gerar DIRF em arquivo**

Marcado esta opção, o usuário poderá gerar a DIRF em arquivo utilizando o filtro de seleção, ou seja, poderá determinar quais funcionários serão ou não enviados para o arquivo.   
Quando um dos parâmetros "apenas com IRRF" ou "com IRRF ou rendimentos acima de 6.000,00 ou assalariado com rendimentos acima de R$30.639,90" estiverem marcados o parâmetro "Usa filtro de seleção ao gerar DIRF em arquivo" não será salvo e gravado no perfil.

* **Seção Centralizador da Coligada**

Este recurso atende os clientes que não tem seção centralizadora (seção empresa) no cadastro de seção e desejam escolher qual será a seção que o sistema utilizará na geração da DIRF e Informe de Rendimentos.  
Para isso deverá marcar o parâmetro "Forçar seção centralizadora (apenas para empresas que não possuem uma seção centralizadora de toda a coligada)" e preencher o campo "Código da Seção Centralizadora".  
Com o parâmetro desmarcado, o sistema buscará os dados da primeira seção do cadastro de seção.  
  
**Exemplo:**

Estrutura de seção sem quebra da empresa, somente com quebra de coligada:  
01 - Centralizadora do CNPJ 2  
02 - Centralizadora do CNPJ 1  
03 - Centralizadora do CNPJ 3  
   
Ao processar a DIRF ou Informe de Rendimentos com o parâmetro desmarcado, o sistema buscará os dados da seção 01.  
Com o parâmetro marcado o cliente poderá determinar de qual seção o sistema buscará os dados.  
   
**Observação**

É possível optar em utilizar a descrição da seção selecionada ou da coligada, para isso utilize o parâmetro "Utilizar descrição da seção selecionada na DIRF em Arquivo". 

**Aba DIRF em Arquivo**  
Esta aba só será exibia, quando a opção 'Gerar Processo no Final' foi DIRF em arquivo ou DIRF para conferência.     
   
Não fazem parte de parâmetros específicos, e devem ser definidos obrigatoriamente, os dados solicitados na aba "DIRF em arquivo" e suas respectivas Abas: "Responsável", "Declarante", "Pessoa Jurídica", "Campos Complementares":  
Como estes dados são preenchidos dentro da coligada, existe recurso para eles serem copiados para outras coligadas em caso de os dados serem iguais para as demais, ou alguma delas.  
   
Ainda dentro dos parâmetros da Coligada, deverão ser relacionas em cada aba os eventos referentes aos Campos da DIRF / Informe de Rendimentos, e também os registros das Operadoras de Saúde, juntamente com o CNPJ e o código ANS. Dentro de cada registro de Operadora, deverá ser referenciado o(s) evento(s) utilizado(s) para descontos na folha dos funcionários, relativos a assistência saúde.  
Caso haja desconto de assistência saúde, é importante observar se o parâmetro "Indicador de Assistência à Saúde", localizado em "DIRF em Arquivo" sub-aba "Declarante", está preenchido com "2 – Existe pagamento de valor pelo titular/dependente". Caso contrário, não serão relacionados os valores de assistência saúde no arquivo da DIRF.  
   
**Próxima tela**  
Finalizado, o perfil de parâmetros definidos no início do processo será gerado:  
   
Se foi selecionado DIRF em Arquivo: será gerado no caminho definido pelo usuário o arquivo DIRF.001.  
   
Se foi selecionado "Informe de Rendimentos": Os informes serão gerados na tela e poderão se impressos, ou também enviados por e-mail (bastando selecionar esta opção nos parâmetros da coligada), ou enviados para o RM Portal (utilizando o parâmetro "Enviar Gerador de Relatórios").

**Maiores detalhes veja em:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=223159003>
