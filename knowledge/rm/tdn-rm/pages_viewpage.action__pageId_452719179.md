---
content_hash: 57af4348c2fa98f1f784e7a0f6b65681a4640657aeb316906e6a28d5dca062e2
fetched_at: '2026-06-29T00:10:03.957218+00:00'
page_id: '452719179'
product: rm
source: tdn-rm
title: Tomador de Serviços
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719179
version: 3
---

Esta etapa é configurada para empresas tomadoras de serviços.  
    
 **Parâmetros e Campos**  
 Utiliza Tomadores de serviço  
 Este parâmetro deverá ser marcado quando a empresa utilizar tomador de serviços.

**Exemplo**  
 A empresa "Conservadora" tem 30 funcionários que são faxineiros. Esta empresa cedeu 10 faxineiros à TOTVS e 20 faxineiros à Coca-Cola. A empresa Conservadora deverá marcar o campo "Utiliza Tomador de Serviços" e na movimentação do funcionário deverá ser informada proporcionalmente aos dias trabalhados em cada tomador de serviço.  
    
 **Observações**  
 Marcando este parâmetro é habilitados os demais campos abaixo desta etapa de configuração do parametrizador. Também é exibido os Cadastros e Processos abaixo:

* Clientes e Fornecedores em Administração de Pessoal | Cadastros
* Rateio Tomadores em Administração de Pessoal | Cadastro | Funcionários | Informações para Cálculo
* Distribuição Sefip em Encargos | SEFIP | SEFIP
* Editar distribuição Sefip em Encargos | SEFIP | SEFIP

As informações dos tomadores de serviço serão prestadas nos arquivos do SEFIP com código de recolhimento 150 e 155.   
    
 **Atenção**

* Para emitir a GRFC e a empresa utilizar tomador de serviço, deverá gerar a distribuição de SEFIP, antes de gerar a GRFC.
* Para empresas que utilizam "Tomadores de Serviço", o usuário deverá fazer a distribuição do tomador primeiramente, observando os dias a serem distribuídos no cadastro do funcionário no menu Rateio de Tomadores.

Cód. Fórmula do fator de proporcionalização  
 Neste campo será informado uma fórmula que irá retornar o total a ser distribuído para cada funcionário. O usuário poderá utilizar uma fórmula para retornar o total de dias trabalhados / horas normais do funcionário no mês em vigência. O resultado desta fórmula servirá para consistir a informação de dias trabalhados/horas normais no momento em que o usuário vai digitar a distribuição de dias por tomador de serviço no cadastro do funcionário, limitando ao total de dias trabalhados/ horas normais retornado pela fórmula. No cálculo da distribuição da movimentação do SEFIP a fórmula também será considerada. O cálculo é feito da seguinte forma: valor total do evento na movimentação dividido pelo total de dias/horas retornado pela fórmula e multiplicado pelo número de dias/horas informado em cada tomador de serviço. Para os eventos que não seguem rateio o valor será informado integralmente para empresa.

**Exemplo**  
 Fórmulas que poderão ser utilizadas :   
 ND - Dias trabalhados considerando admissão e demissão.  
 NDTRAB - Dias trabalhados considerando admissão, demissão, afastamentos, férias, calendário mensal e horário.  
 (N('0001') - N('0008') ) - Total de Horas normais - Faltas  
 (N('0002') - N('0008') ) - Total de Dias trabalhados - Faltas  
    
 **Atenção**  
 Para funcionários mensalistas esta fórmula poderá retornar o número de dias trabalhados e no caso de horistas será retornado o número de horas trabalhadas.  
    
 **Observação**  
 A fórmula de proporcionalizacão não é obrigatória, caso o usuário não a informe, o sistema sempre calculará 30 dias, independente se o código do recebimento é Mensalista ou Horista.  
 Cód. da empresa/coligada no cadastro de tomadores  
 Neste campo será informado o tomador que representa a empresa, pois será neste tomador que será lançado a movimentação referente à empresa. Este parâmetro é utilizado para identificar qual o tomador (default) quando o usuário não tiver informação sobre o tomador para o funcionário.   
 **Observações**

* Para cadastrar os tomadores de serviços, o campo "Utiliza Tomadores de Serviço" deverá estar previamente marcado e cadastrados em Cadastros | Clientes/Fornecedores.
* Neste campo só retornar os Clientes/Fornecedores que tiverem com os parâmetros 'Tomador de serviços folha' e 'Ativo' marcados em Administração de Pessoal | Cadastros | Cliente e Fornecedor
* Quando houver dois códigos de Clientes/Fornecedores iguais (coligada corrente e coligada global), ao informar o código o sistema acatará o código do Cliente/Fornecedor da coligada corrente. Se o usuário desejar informar o código do Cliente/Fornecedor da coligada global, o mesmo deverá ser selecionado pelo nome.
* Em caso da coligada possuir Integração com Módulo TOTVS Gestão Financeira e nos parâmetros deste módulo, na etapa "Parâmetros Lançamentos", estiver desmarcado o parâmetro "Permite Globais", não será possível associar em campos de cadastros do TOTVS Folha de Pagamento, Cliente/Fornecedor que foram cadastrados como "Global".

Tipo de tomador default  
 Marcar o tipo de tomador de serviço que a empresa cedente está relacionada, ou seja, se a empresa cedente é uma prestadora de serviços ou uma construção civil. Este parâmetro serve para o relatório do SEFIP ser gerado de acordo com o recolhimento, sendo que todas as empresas devem marcar o parâmetro. Para as empresas que cedem somente mão-de-obra específica como prestação de serviço ou apenas para construção civil devem marcar este parâmetro somente. Para as empresas de construção civil que cedem mão-de-obra de construção civil e de prestação de serviços e desejarem recolher para os tomadores de serviços no código de recolhimento específico de cada um, devem marcar este parâmetro como construção civil e nos tomadores de serviço especificar de acordo com o tipo.

**Exemplo**  
 Se um funcionário trabalhou na Empresa "Construtora X" em alguma obra civil "Tomador 1" por 10 dias e este mesmo funcionário trabalhou na limpeza "Tomador 2" por 15 dias, então o usuário deve marcar em tipo de tomador default "Construção civil" para gerar os administrativos.   
 Em Clientes/Fornecedores "Tomador 1" deve marcar "Construção civil" ou não marcar nada que será considerado o parâmetro marcado em tipo de tomador default e "Tomador 2" deve marcar "Cessão de mão-de-obra".  
 Em seguida deve fazer a distribuição de SEFIP e gerar o SEFIP:

* Informando o código de recolhimento 150 e parâmetro "gera funcionários administrativos" não marcado, será gerado os 15 dias trabalhados para o "Tomador 2".
* Informando o código de recolhimento 155 e parâmetro "gera funcionários administrativos" marcado, será gerado com os 10 dias do "Tomador 1" e os 05 dias da parte do administrativo da "Empresa cedente".

**Observações**  
 Ao gerar o SEFIP, o usuário deverá marcar o parâmetro 'Gerar funcionário administrativos' de acordo com o parâmetro marcado.  
    
 Se a empresa cedente é Cessão de mão-de-obra a parte dos administrativos deverá ser gerada nos códigos de recolhimentos 150. Se a empresa cedente é Construção Civil, a parte dos administrativos deverá ser gerada nos códigos de recolhimentos 155. O sistema funcionará da seguinte forma:

* Marcando somente o parâmetro em Tipo de tomador default no parametrizador, será gerado normalmente considerando todos os tomadores de serviço de acordo com a opção marcada.
* Marcando o tipo de tomador em Tipo de tomador default no parametrizador e em Cadastros | Clientes/Fornecedores, será considerado para empresa cedente o opção marcada em Tipo de tomador default e para os tomadores de serviços o tipo marcado em Cadastros | Clientes/Fornecedores.
* Marcando o tipo de tomador em Tipo de tomador default no parametrizador, em Cadastros | Clientes e Fornecedores e em Administração de Pessoal | Cadastro | Funcionários | Informações para Cálculo | Rateio Tomadores, será considerado para empresa cedente o parâmetro em Tipo de tomador default e para os tomadores de serviços o parâmetro marcado em Rateio Tomadores, no cadastro de funcionários

**Atenção**  
 Esta parametrização somente é válida para as empresas que estão caracterizadas como FPAS 507, pois o validador da CEF não valida o código de recolhimento 155 com FPAS 515.

Meses de distribuição guardados, para geração de SEFIP em atraso  
 Neste campo é informado a quantidade e meses que o sistema guardará a distribuição do SEFIP em meses anteriores.

**Observações**

* Quando o parâmetro 'utiliza tomadores de serviços' for marcado, o sistema irá preencher o campo para 2, devendo o usuário modifica-lo, caso queira.
* Este campo será limitado a 48 meses. Portanto, se o usuário digitar um número maior que 48, o campo voltará para o valor de 48 meses.
* Se neste campo for digitado valor maior que 12, o sistema emitirá mensagem de alerta informando que a performance da geração do SEFIP ficará lenta.

Distribuição de eventos por tomador via entrada de dados  
 Marcando esta opção será habilitada o processo 'Entrada de Movimento por Tomador' em Folha Mensal | Processos | Entrada de Movimento, onde será possível fixar um evento e um valor a um determinado Tomador de serviço.

**Exemplo**  
 O usuário poderá, pelo processo 'Entrada de Movimento por Tomador', informar um evento e vinculá-lo ao Tomador 1. Quando processada a distribuição em Encargos | SEFIP | SEFIP, o valor desse evento se manterá fixo no Tomador 1. Portanto, o sistema desconsiderar para esse evento, os tomadores informados no parametrizador ou no cadastro de funcionários.   
 Buscar descrição do tomador de serviço no cadastro de CEI  
 Marcando este parâmetro, o arquivo SEFIP será gerado considerando a descrição do tomador de serviço do cadastro de CEI informado em Administração de Pessoal | Cadastros | Cliente e Fornecedor, para os códigos de recolhimento 150 e 155.

**Observação**  
 O cadastro de cliente e fornecedor pode ter mais de um CEI vinculado ao mesmo. Então é necessário que o CEI seja informado no Rateio de Tomadores no cadastro de funcionários ou na Entrada de Movimento por Tomadores, para que seja feira a distribuição para o CEI correto.

Controla Saldo de compensações não deduzidas no SEFIP  
    
  

|  |  |
| --- | --- |
|  | Informações Complementares |

---

<<Voltar para tela anterior **Folha Normal**
