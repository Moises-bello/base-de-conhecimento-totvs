---
content_hash: 2eb5a86c8801d48e4beb16aedf18250cba495dc46a2c6dcf17c9aa3c799f056c
fetched_at: '2026-06-29T00:11:28.410393+00:00'
page_id: '73077793'
product: rm
source: tdn-rm
title: RMPAT00004_Roteiro de Conversão do Totvs Gestão Patrimonial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=73077793
version: 9
---

|  |  |  |
| --- | --- | --- |
| **Produto** | : | Totvs Gestão Patrimonial – **Versão:** 11.5x |
| **Processo** | : | Conversão do Totvs Gestão Patrimonial |
| **Subprocesso** | : | Conversão |
| **Data da publicação** | : | 08/08/2013 |

Este documento tem como objetivo orientá-lo nos procedimentos que devem ser feitos antes e após a conversão para o Bonum.Net.   
 O TOTVS Gestão Patrimonial foi todo migrado para a tecnologia .Net. Esta linguagem de programação possui várias funcionalidades que permitem que sejam disponibilizados maior usabilidade e flexibilidade no dia a dia dos usuários dos sistemas da linha RM.

O Bonum.Net possui recurso de utilização de vários cenários de cálculos, contabilização operações utilizando eventos contábeis, transferências de controle, alocações Patrimônios, Liberação de Competência etc.

Se sua empresa ainda não conhece as novidades do **"TOTVS Gestão Patrimonial"** acesse o portal do cliente ([www.totvs.com/suporte](http://www.totvs.com/suporte)) e faça o download do documento **"TOTVS Gestão Patrimonial\_NET.rar"**

A apresentação das novidades também está disponível no link abaixo: <http://www.slideshare.net/totvsconnect/totvs-gesto-patrimonial-bonumnet> .   
   
 **Siga as instruções abaixo:**

**1º Passo:** **Antes de executar a conversão para a versão 11.50 acesse o sistema RM Bonum**.**exe.**

Verifique quais são os meses que já se encontram encerrados ,ou seja , verifique se todas as contabilizações de aquisições, ocorrências e depreciações já foram enviadas para a contabilidade.

O Bonum.Net (versão 11.50) possui uma sistemática de cálculos diferente do Bonum em Delphi (versão 11.40). Desta forma, pequenas diferenças de arredondamento podem ocorrer entre os dois sistemas.

Por este motivo, sugerimos que para os meses que já se encontram encerrados (integrados com a contabilidade) seja feita a liberação mensal até o mês em questão. Assim não ocorrerão diferenças entre os valores apresentados no sistema de Gestão Patrimonial e o sistema de Gestão Contábil.   
 As contabilizações e todas as operações patrimoniais (baixas, acréscimos, etc) dos próximos meses **(meses que ainda não foram encerrados)** deverão ser feitas no Bonum.Net (versão 11.50).

Sugerimos que antes do processo de Liberação de Período verifique se as cotações estão corretamente informadas, ou seja, verifique se não há variação de um ano para outro,  através do menu Cadastros > Moedas e Índices > Selecione o índice > Anexos > Cotação. O mesmo processo de ser realizado para a moeda R$, caso tenha uma alteração de cotação acerte conforme processo  abaixo, emita os relatórios e verifique os valores novamente.

Acesse Menu Cadastros > Moedas e Índices > Selecionar a moeda R$ > Processos > Preencher intervalo de cotações:  
Período aplicar: (Somente para o período em aberto)  
Fator: 1,000  
Marcar: Subescrever datas do intervalo  
Marcar: Fator Fixo  
Desmarcar: Considerar Somente dias úteis

Acesse Menu Cadastros > Moedas e Índices > Selecionar o índice UFIR > Processos > Preencher intervalo de cotações:  
Período aplicar: 01/01/1990 a 31/12/2030  
Fator: 0,8287  
Marcar: Subescrever datas do intervalo  
Marcar: Fator Fixo  
Desmarcar: Considerar Somente dias úteis

**Ex:** Vamos supor que meu ano cálculo no RM Bonum é **01/2012** ( o ano cálculo na versão 11.40 pode ser visualizado no rodapé da tela do sistema). Todas as contabilizações de aquisições, ocorrências e depreciações até o mês de **setembro** já foram integradas com a contabilidade.  
 Então preciso emitir o relatório **"Razão Auxiliar"** no Bonum para conferir se os saldos Patrimoniais estão de acordo com a contabilidade.

 Para emitir o relatório deve-se acessar o menu **Relatórios/Razão** **Auxiliar**

.

Após será apresentada a tela para que sejam informadas as opções desejadas.

De acordo com nosso exemplo, o mês inicial e final informado será **Setembro**. Poderíamos também emitir o relatório com mês inicial em **janeiro** e final em **setembro,** pois precisamos conferir os saldos patrimoniais no final de **setembro**.

Para exemplificar vamos emitir o relatório para as contas **1.01.1.1.650** a **1.01.1.1.656** conforme print abaixo.

Reparem que a conta **1.01.1.1.650** apresentou um saldo final de **R$ 67.000,00** para o valor Patrimonial.

Já o saldo final de **Depreciação Acumulada – conta 1.01.1.1.651** foi de **R$ 5.024,97**

Ou seja, no módulo **TOTVS Gestão Contábil** estas contas contábeis devem possuir o mesmo saldo final, pois até o mês de setembro todas as contabilizações já foram **integradas ao lote zero da contabilidade.**

**2º PASSO:** Para conferência do saldo contábil dentro do **TOTVS Gestão Contábil** sugerimos que seja emitido um B**alancete** ou **Razão Analítico** para conferência.  
 Em nosso exemplo, vamos emitir um **Balancete**.

Após acessar o **TOTVS Gestão Contábil**, deve-se acessar o menu **Relatórios/Balancete**.

Seguindo o nosso exemplo, vamos emitir o relatório para a conta **1.01.1.1.650 e conta 1.01.1.1.651** no período de **01/09/2011 a 30/09/2011**.

 

Reparem que o saldo final da conta **1.01.11.650** e da conta **1.01.1.1.651** **coincidem** com os saldos do **Razão Auxiliar** do RM Bonum.   
 **Este mesmo procedimento deve ser feito para todas as contas do Ativo Imobilizado.**

**ATENÇÃO:** Após a conferência e conciliação dos saldos das contas, deve-se emitir todos os relatórios necessários e executar uma **cópia de segurança (backup)** da base de dados, pois o próximo passo será a execução da **Liberação de Período** no RM Bonum.

É muito importante que todos os relatórios necessários já tenham sido emitidos e um backup de segurança já tenha sido feito, **pois a liberação irá apagar os cálculos existentes e após não será possível emitir dados do período liberado.**

No caso de qualquer problema na **liberação do período**, este backup deve ser voltado imediatamente, portanto este processo deve **ser feito fora do expediente de trabalho**, pois caso ocorra algum problema e seja **necessário voltar o backup**, os demais departamentos da empresa não serão afetados com a restauração.

No exemplo que apresentamos, a contabilidade já está encerrada até o mês **09/2011** e os saldos do **Razão Auxiliar** estão de acordo com os **saldos na contabilidade**, portanto o próximo passo será realizar a **liberação mensal** até o mês **09**.

**3º PASSO:** Para liberação mensal deve ser acessado o menu **Utilitários/Liberações.**

Após será apresentada a tela para que sejam informados os dados da liberação.

 

No campo **"Tipo"** deve ser informado **"Mensal"** e no campo **"Mês final de liberação"** deve ser informado o mês desejado.  
 Em nosso exemplo vamos informar o mês de **Setembro.**

**4º PASSO:** Após a realização da Liberação de Período até o mês de **Setembro,** sugerimos que seja emitido o relatório **"Razão Auxiliar"** no RM Bonum para o mês de **Outubro**. O objetivo da emissão deste relatório é conferir se os saldos anteriores estão de acordo com o saldo final que foi apresentado antes da liberação.

**Ex:** Vamos emitir o relatório **Razão Auxiliar** para as contas **1.01.1.1.650** e **1.01.1.1.651** no mês de **outubro** **após a liberação mensal** que foi feita.

 

**Reparem** que o saldo anterior em **30/09** para a conta **1.01.1.1.650** se encontra em **67.000,00.** O saldo anterior para a conta de depreciação **1.01.1.1.651** em **30/09** é de **5.024,97.** Ou seja, os saldos anteriores estão corretos e de acordo com os saldos finais **antes da liberação**.

**ATENÇÃO:** Sugerimos que esta conferência seja feita para todas as contas contábeis do ativo imobilizado.  
 Após a realização da conferência dos valores, **a conversão da base de dados para a versão 11.50 poderá ser feita.**

Orientamos que primeiramente seja convertida uma base de **"Testes"**, para que todos os processos internos sejam testados e conferidos antes da conversão da **base oficial de produção**. É muito importante que os usuários conheçam os novos recursos e realizem os testes de acordo com os processos internos existentes.

**5º PASSO:** Acessar o Conversor de base de dados – **versão 11.50**. Após executar o conversor o mesmo irá verificar se existem patrimônios cadastrados na base, existindo patrimônios será apresentada a mensagem abaixo:

Ao final da conversão da base para a **versão 11.50** caso ocorram erros no log, o mesmo deverá ser enviado para análise da equipe técnica da TOTVS. **Não ocorrendo erros a base poderá ser acessada**.

**Feita a conversão para a versão 11.50**, ao acessar o **RM Bonum.exe pela primeira vez** será apresentada a mensagem abaixo:

**Ao confirmar este processo,** **os registros existentes na base serão convertidos para as novas tabelas do Bonum.NET.**   
 **Atenção:** Ao final deste processo será apresentado um log de conversão, caso o log apresente **algum erro**, favor entrar em contato com a equipe técnica de suporte do **RM Bonum** para análise do mesmo.

Após a conversão para o **Bonum.Net**, o processo de execução dos cálculos de depreciações deverá ser feito.   
 **O Bonum.Net trabalha com o conceito mensal.** Considerando nosso exemplo, após a conversão para o **Bonum.Net** o mês de cálculo será **outubro,** pois antes de converter a base realizamos a liberação mensal do período de setembro. Então a seguir, iremos executar os cálculos para este mês.

**6º PASSO:** Para execução dos cálculos devemos acessar o menu **Cadastros/Cálculos.**

 Após devemos selecionar o **Cálculo** e clicar em **Processos/Cálculo do Patrimônio.**

Após clicar em "**Cálculo do Patrimônio"** será apresentada a tela para confirmação do Processo. Confirmando a execução, será iniciada o processo de cálculos do mês em questão.

**ATENÇÃO: Sem a execução deste processo a depreciação dos Patrimônios não é realizada, portanto este processo é imprescindível.**

Existem outras formas de acesso para execução dos cálculos. O processo pode ser executado também pelos seguintes menus:

**Na visão de Cadastros/Cenários** **acessar a opção Processos/Calcular Cenário**

**Na visão de Patrimônios** **acessar a opção Processos/Cálculo de Depreciação**

**ATENÇÃO:** **Caso o processo seja executado na visão de Patrimônios, deverá ser feito um filtro de todos os patrimônios,selecioná-los e executar o processo. Os patrimônios do tipo título não devem ser filtrados para execução de cálculos.**

**7º PASSO:** Para emissão do relatório de conferência dos **saldos patrimoniais** deve-ser realizar os seguintes procedimentos:   
 Primeiramente deve-se importar o relatório **"Ficha de Imobilizado".** O relatório **"Razão Auxiliar"** que existe no sistema Delphi foi substituído pelo **"Ficha de Imobilizado"**. Esta substituição foi necessário devido à nova estrutura de tabelas. No **Bonum.Net** não existe o conceito de **grupo de contas**, a contabilização das operações é feita utilizando **eventos contábeis**.

O relatório **"Ficha de Imobilizado"** irá apresentar **os valores patrimoniais/depreciações** **acumuladas/** **depreciações mensais** de cada grupo, com suas **respectivas operações patrimôniais (baixas, acréscimos, transferências monetárias, transferências de controle) caso existam.**

Deve-se acessar o menu **Relatórios/Gerador.NET (Preview)**.

 Após devemos acessar **Processos/Importar Estrutura de Relatório**.

Após será apresentada a tela para seleção do relatório.   
   
 **OBS: O relatório "Ficha de Imobilizado" também pode ser emtido** **por filial, para isso é necessário importar também o relatório "2 - Ficha de Imobilizado por Filial".**

Após a seleção do relatório, devemos clicar em **"Abrir",** então será apresentada a tela abaixo.

Devemos clicar em **"Executar".** Feito isto o relatório será importado para futura utilização no sistema.

Uma vez importado o relatório, devemos realizar a emissão da **"Ficha de Imobilizado**.

Deve-se acessar o menu **Relatórios/Ficha de Imobilizado**.

Será apresentada a tela para informação dos dados desejados. Em nosso exemplo, como realizamos a liberação até o **mês 09 antes de converter a base**, vamos emitir o relatório para o **mês 10**.

Em nosso exemplo a base já se encontra no ano de **2012,** por este motivo estamos utilizado este ano como exemplo.

Deve ser informado o **cenário desejado** para emissão do relatório. Em nosso exemplo vamos informar o **cenário de cálculo padrão,** este é o cenário que foi convertido automaticamente pelo sistema.Vamos informar o período de apuração de 10/2012 a 10/2012, marcar a opção de Patrimônios Ativos e não selecionar filiais.

 

Ao clicar em **"Avançar"** devemos informar os grupos desejados. **Em nosso exemplo**, vamos informar o **grupo de código 850**, este é o grupo que de **Máquinas Pesadas** que foi convertido para o **Bonum.Net** .

Após informar os grupos desejados devemos clicar em **"Avançar"**.

Será apresentada a tela para marcação das **opções desejadas e seleção do relatório de ficha de imobilizado**.

Após será apresentado o relatório conforme tela abaixo, com os **valores Patrimoniais (valores bases) e valores de depreciação acumulada com suas depreciações e possíveis operações patrimoniais (baixas, acréscimos, etc)**.

**Em nosso exemplo, emitimos o relatório apenas para o grupo 850**, reparem que os saldos anteriores referentes ao dia 30/09/2012 são os mesmos saldos que foram apresentados no **sistema Delphi** antes de realizarmos a conversão para a **versão 11.50**.  
 **Atenção:** **O relatório deve ser emitido para todos os grupos do ativo imobilizado para conferências dos valores.**

**Após conferência de todos os saldos anteriores de todos os grupos de Patrimônios, o usuário já poderá utilizar todos os processos e recursos disponíveis no Bonum.Net.**

**Este roteiro teve o objetivo de demonstrar os passos que devem ser feitos antes e após a conversão para conferência dos saldos patrimoniais.**

**Reforçando que no caso dos meses que já se encontram encerrados (integrados com a contabilidade) sugerimos que seja feita a liberação mensal até o mês em questão.**

**Caso a empresa não realize a liberação de período mensal ou anual antes da conversão para a versão 11.50, será necessário verificar se os saldos patrimoniais apresentados após a conversão estão coincidindo com a contabilidade. Esta conferência deverá ser feita mensalmente e por este motivo é um processo bem trabalhoso. Abaixo iremos citar os procedimentos para conferência dos saldos.**   
   
   
   
    
 **ROTEIRO DE CONFERÊNCIA DOS SALDOS APÓS A CONVERSÃO, PARA AS EMPRESAS QUE NÃO IRÃO REALIZAR A LIBERAÇÃO DE PERÍODO**

**1****º Passo:** Vamos supor que o ano cálculo da coligada seja **2012** . Antes de realizar a conversão para a **versão 11.50**, deve-se verificar se os saldos patrimoniais estão de acordo com a contabilidade.

No exemplo que iremos apresentar, as operações patrimoniais **(baixas, acréscimos, transferências)** e contabilizações até o mês de fevereiro já estão integradas, então vamos emitir o relatório no RM Bonum para o mês de fevereiro.

Deve-se acessar o menu **Relatórios/Razão Auxiliar** no **RM Bonum**. Em nosso exemplo vamos emitir o relatório para a conta de **Máquinas e Equipamentos** no mês de fevereiro.

 A conta de Máquinas e Equipamentos apresentou um saldo final de **R$ 70.000,00.**

Agora vamos emitir o relatório para a conta de **Depreciação Acumulada de Máquinas** **e Equipamentos.**

A conta de **Depreciação Acumulada de Máquinas e Equipamentos** apresentou o saldo de **R$ 1.000,01.**

**2º Passo:** Vamos verificar se os saldos contábeis estão de acordo com os valores apresentados no Razão Auxiliar.

Dentro do RM Saldus deve-se acessar o menu **Relatórios/Balancete** e emitir o relatório para a conta desejada. No nosso exemplo vamos emitir o relatório para a conta **1.03.1.2.042** e **1.03.1.1.017** (mesmas contas que emitimos no **Razão Auxiliar** do **RM Bonum**).   
   
 Os valores apresentados no balancete **foram os mesmos do relatório Razão Auxiliar**:  
 **R$ 70.000,00** para a conta de **Máquinas** e **R$ 1.000,01** para a conta de **Depreciação Acumulada**.

 

**3º Passo:** Após conferir os **saldos patrimoniais** do **RM Bonum** com os **saldos contábeis**, deve ser feito um backup da base de dados para realização da conversão da base. Sugerimos **que a conversão da base seja feita sempre para uma base de testes antes de converter a base oficial**.   
 **OBS: Todos os relatórios necessários também devem ser emitidos antes da conversão** **da base.**

Após realização destes procedimentos deve-se acessar o conversor para a **versão 11.50** e iniciar a conversão. Ao identificar que existem patrimônios cadastrados na base, o converso apresentará a mensagem abaixo:   
   
 Ao final da conversão da base para a **versão 11.50** caso ocorram erros no log, o mesmo deverá ser enviado para análise da equipe técnica da TOTVS, **não ocorrendo erros o sistema poderá ser acessado**.

**4º Passo: Feita a conversão para a versão 11.50**, ao acessar o **RM Bonum.exe pela primeira vez** será apresentada a mensagem abaixo:   
    
    
 **Ao confirmar este processo,** **os registros da base serão convertidos para as tabelas do Bonum.NET.**   
 **Atenção:** Ao final deste processo será apresentado um log de conversão, caso o log apresente algum erro, favor entrar em contato com a equipe técnica de suporte do **RM Bonum** para análise do mesmo.

Após a conversão para o **Bonum.Net**, o processo de execução dos cálculos de depreciações deverá ser feito.

**O Bonum.Net trabalha com o conceito mensal,** após a conversão para o **Bonum.Net** o mês de cálculo será **janeiro/2012**. Então vamos executar os cálculos para este mês.

**Atenção: Caso existam ocorrências na coligada as mesmas serão convertidas para o Bonum.Net, porém a contabilização já deve ter sido feita , pois as ocorrências são convertidas com o status de "Não Contábil".**   
   
   
 **5º Passo:** Para execução dos cálculos devemos acessar o menu **Cadastros/Cálculos.**

Após devemos selecionar o **Cálculo** e clicar em **Processos/Cálculo do Patrimônio.]**

 

Após clicar em "**Cálculo do Patrimônio"** será apresentada a tela para confirmação do Processo. Confirmando a execução será iniciada o processo de cálculos do mês em questão.

**ATENÇÃO: Sem a execução deste processo a depreciação dos Patrimônios não é realizada, portanto este processo é imprescindível.**   
 Existem outras formas de acesso para execução dos cálculos. O processo pode ser executado também pelos seguintes menus:   
   
 **Na visão de Cadastros/Cenários, opção Processos/Calcular Cenário**

**Na visão de Patrimônios , opção Processos/Cálculo de Depreciação**

**ATENÇÃO:** **Caso o processo seja executado na visão de Patrimônios, deverá ser feito um filtro de todos os patrimônios, selecioná-los e executar o processo. Os patrimônios do tipo título não devem ser filtrados** **para execução de cálculos.**

**6º Passo:** Após realizar o cálculo para o mês de **janeiro/2012**, precisamos verificar se os **saldos patrimoniais** de **janeiro** estão de acordo com os **saldos contábeis.**   
 Para emissão do relatório de conferência dos saldos patrimoniais deve-ser realizar os seguintes procedimentos:

Primeiramente deve-se importar o relatório **"Ficha de Imobilizado".** O relatório **"Razão Auxiliar"** que existe no sistema Delphi foi substituído pelo **"Ficha de Imobilizado"**. Esta substituição foi necessário devido à nova estrutura de tabela. Pois no **Bonum.Net** não existe o conceito de **grupo de contas**, a contabilização é feitas utilizando **eventos contábeis**.

O relatório **"Ficha de Imobilizado"** irá apresentar **os valores patrimoniais/depreciações** **acumuladas/** **depreciações mensais** de cada grupo, com suas **respectivas operações patrimoniais (baixas, acréscimos, transferências monetárias) caso existam.**

Deve-se acessar o menu **Relatórios/Gerador.NET (Preview)**.

 Após devemos acessar **Processos/Importar Estrutura de Relatório**.

Após será apresentada a tela para seleção do relatório.

**OBS: O relatório "Ficha de Imobilizado" também pode ser impresso por filial, para isso é necessário importar também o relatório "2 - Ficha de Imobilizado por Filial".**

Após seleção do relatório devemos clicar em **"Abrir"**, então será apresentada a tela abaixo.

Devemos clicar em **"Executar".** Feito isto o relatório será importado para futura utilização no sistema.   
 Uma vez importado o relatório, devemos realizar a emissão da **"Ficha de Imobilizado**" utilizando o relatório que acabamos de importar.

Acessar o menu **Relatórios/Ficha de Imobilizado**.

Será apresentada a tela para informação dos dados desejados. Em nosso exemplo, vamos emitir o relatório para o **mês 01**.   
 Em nosso exemplo a coligada já se encontra no ano de **2012**, por este motivo estamos utilizado este ano.

Deve ser informado o **cenário desejado** para emissão do relatório. Em nosso exemplo vamos informar o **cenário de cálculo padrão**. Este é o cenário que foi convertido automaticamente pelo sistema.

 

 Em nosso exemplo **não vamos** marcar a opção de **"Selecionar Filiais".** Se o usuário marcar esta opção deverá utilizar o relatório de **"Ficha de Imobilizado por filial". O período de apuração será de 01/2012 a 01/2012.**

Ao clicar em **"Avançar"** devemos informar os grupos desejados. **Em nosso exemplo**, vamos informar o **grupo de código 650 – Máquinas e Equipamentos.** Após informar o grupo devemos informar o código do relatório.

Após devemos clicar em **"Avançar"**. Então será apresentada a tela para marcação das opções desejadas e selecionar o relatório **"Ficha de Imobilizado".**

Ao clicar **em avançar e executar** o relatório será será apresentado .

O relatório apresentou um saldo de **R$ 50.000,00** para o **Valor Base** e **R$ 416,67** de **Depreciação Acumulada** do grupo **Máquinas e Equipamentos.**

**7º Passo: Acessar o RM Saldus e emitir o relatório balancete para o mês de janeiro para as contas acima.**

**Deve se acessar o Saldus e selecionar menu Relatórios/Balancete. Após deve-se informar o período do e as contas desejadas para emissão do relatório. Em nosso exemplo vamos informar o período de janeiro de 2012.**

 

No balancete as contas apresentaram os saldos em janeiro de acordo os saldos patrimoniais apresentados na Ficha de Imobilizado. O mês de janeiro está **ok** para o grupo de **Máquinas**, na prática a empresa **precisará conferir todos os grupos de imobilizado existentes**. Em nosso exemplo como **janeiro está ok**, vamos proceder para realizar a conferência de fevereiro, pois a contabilidade já está integrada até este mês.

**8º Passo:** Para realizar a conferência de fevereiro, precisamos **liberar a competência do mês de janeiro**. Deve-se acessar o menu **Utilitários/Liberações/Liberação de Competência.**  
   
 Após deve-se clicar em **Avançar** será apresentada as mensagens de alerta:   
   
   
 Ao clicar em **"Avançar"** é apresentada uma lista para conferência. Marque todas as opções e clique em **Avançar**.   
   
 Será apresentada a tela informando o período de cálculo atual e o próximo período de cálculo. Marque a opção **"Executar recálculo"** para que o recálculo seja executado.

 Após deve-se clicar em **"Avançar"** e **"Executar"** o processo.Ao final será apresentado um log informando o novo mês de cálculo.

 

**9º Passo:** Emitir a Ficha de Imobilizado **(conforme demonstrado no 6º Passo)** para o mês de fevereiro.

Os saldos apresentados para o mês de fevereiro foram:  
 **R$ 70.000,00 para a conta de Máquinas e Equipamentos e R$ 1.000,01 para a conta de Depreciação Acumulada**

    
 Os saldos apresentados coincidem com os saldos contábeis apresentados no **2º Passo,** ou seja neste exemplo que apresentamos, **depois da conversão** os valores patrimoniais estão de acordo com a contabilidade.

Em nosso exemplo a contabilidade já estava encerrada até **fevereiro 2012**, por este motivo iremos conferir até este mês. A partir do mês 03/2012 todas as operações patrimoniais serão feitas e contabilizadas no **Bonum.Net**. Para que seja possível realizar as operações patrimoniais e cálculos do mês 03/2012 é necessário executar o processo de **"Liberação de Competência"** **(processo citado no 8º Pass**o).

Conforme já informado anteriormente, devido a sistemática de arredondamento do **Bonum.Net**, poderão ocorrer casos em que o valor de **depreciação mensal** do **Bonum.Net** não irá coincidir com o valor existente na contabilidade.  
 Caso isto ocorra, será necessário realizar um **estorno contábil** do **valor de depreciação** **mensal** para ajustar os valores, pois os saldos patrimoniais do **Bonum.Net** devem estar de acordo com os saldos contábeis.

**Exemplo:**  
 Vamos supor que o valor de depreciação mensal acima tivesse sido apresentado como **R$ 583,33.** Neste caso o saldo da conta de **Depreciação Acumulada de Máquinas** seria **R$ 1.000,00,** então seria necessário realizar um **estorno contábil no valor de 0,01** para ajustar o saldo contábil com o saldo patrimonial. Outra maneira de ajuste, seria editar o lançamento mensal de depreciação existente no **RM Saldus** e realizar a **alteração do valor do lançamento**.

**Os lançamentos originados do RM Bonum que foram gerados no modelo Delphi permitem a alteração de valor.**   
 **OBS:** **No exemplo que apresentamos não existiam ocorrências na base antes da conversão. Caso existam, as ocorrências são migradas como "Não Contábil" e os valores das mesmas também serão apresentadas no relatório "Ficha de Imobilizado".**   
 **Os valores das ocorrências também poderão apresentar divergências com os valores existentes na contabilidade,existindo diferenças deve-se seguir a mesma orientação que citamos acima para ajustar o valor de depreciação (realizar estorno contábil ou alterar o valor do lançamento existente no RM Saldus).**

**Atenção: As** **aquisições e ocorrências que existiam antes da conversão da base não podem ser contabilizadas no Bonum.Net, por este motivo a conferência dos valores apresentados no relatório de Ficha de imobilizado com os saldos contábeis é de extrema importância.**   
 Diante do exemplo apresentado, podemos constatar que a conversão de base de dados sem realizar a liberação de período é bem mais trabalhosa, e havendo divergência de valores será necessário **ajustes contábeis**. Por este motivo sugerimos que antes da conversão para o **Bonum.Net** seja feita a **liberação de período mensal ou anual conforme citado na primeira parte deste roteiro.**

Qualquer dúvida favor entrar em contato com nossa equipe de suporte técnico.
