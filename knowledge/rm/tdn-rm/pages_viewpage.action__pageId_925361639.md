---
content_hash: 6d53874dc753be541cd3e5a49d6963cd04804754eeaa2083a52e0bc47fb5fe02
fetched_at: '2026-06-29T00:12:07.462613+00:00'
page_id: '925361639'
product: rm
source: tdn-rm
title: Crédito do Trabalhador - Linha RM - Medida Provisória Nº 1.292, de 12 de Março
  de 2025
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=925361639
version: 131
---

false

**A partir das Versões:**

* [DT - Crédito do Trabalhador - eSocial](https://tdn.totvs.com/pages/viewpage.action?pageId=925346824)
* [DT - Crédito do Trabalhador - Cálculos](https://tdn.totvs.com/pages/viewpage.action?pageId=939246677)
* [DT - Crédito do Trabalhador - CC 487 e 488 lançados em período diferente da folha - Provisionamento Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=1039033071)
* [DT - Provisionamento Crédito Trabalhador - Lançar simultâneo para Férias e Adiantamento](https://tdn.totvs.com/pages/viewpage.action?pageId=1042927970)

## **CONTEÚDO**

* **Visão Geral**
* **Passos para utilização**
* **Exemplos de utilização**
* **Tabelas utilizadas**

CRÉDITO01. VISÃO GERAL

## **01. VISÃO GERAL**

Diferente dos empréstimos consignados anteriores onde vínculo é diretamente ligado a uma instituição financeira privada, o **Crédito do Trabalhador** irá permitir que o trabalhador escolha entre diversas instituições financeiras, com base nas melhores taxas de juros e condições oferecidas, onde irá tornar o crédito consignado mais acessível e eficiente para os trabalhadores.  
  
A inovação mais significativa está na digitalização e automação do processo, dispensando a exigência de convênios diretos entre empresas e instituições bancárias, o que torna a contratação desse tipo de crédito mais fácil e com menos burocracia. Os trabalhadores poderão acessar o **Credito do Trabalhador** por meio da **Carteira de Trabalho Digital**. Nela, será possível visualizar:

> - Instituições financeiras diversas e as opções de crédito disponíveis  
> - Taxas de juros e parcelas  
> - Prazos para pagamento e quitação do empréstimo  
> - Além de poder fazer simulações  
>   
> Ao escolher uma opção, o colaborador será direcionado ao banco. A instituição fará todos os trâmites de negociação e fechamento do contrato. Em seguida, as informações do empréstimo consignado contratado ficarão disponíveis na **CTPS Digital**. Dessa forma, o colaborador terá total controle sobre o seu crédito consignado.
>
> Este processo ainda poderá sofrer alterações em função de algumas normatizações que ainda estão em andamento, bem como, a possibilidade de disponibilização de uma forma coletiva de consulta ou importação das parcelas à serem consignadas na plataforma no governo.

**ATENÇÃO:** A TOTVS Folha de Pagamento RM está em processo de adequação para atender à **Medida Provisória Nº 1.292**.

Alterações e documentação foram liberadas de forma faseada, conforme abaixo:

* **1ª Fase: 26/03/2025:**  eSocial - [DT - Crédito do Trabalhador eSocial](https://tdn.totvs.com/pages/releaseview.action?pageId=925346824)
* **2ª Fase: 30/04/2025:** Cadastro do Empréstimo, Importação de Empréstimos Crédito do Trabalhador, Cálculos de Folha e Rescisão e Importação/Exportação
* **3ª Fase: 09/05/2025:** Cancelamento de Movimento e rescisão
* **4ª Fase: 16/05/2025:** Provisionamento de Férias - **P****ara a 4ª fase precisa executar o atualizador novamente.**
* **5ª Fase: 06/06/2025:** Recálculo automático
* **6ª Fase: 18/06/2025:** Provisionamento de férias proporcionalizando por dias de férias e Não zerar valor do empréstimo no cadastro para provisionamento preventivo nas férias
* **7ª Fase: 27/06/2025:** Margem Consignável considerando eventos com o somatório de todas as rubricas de vencimento e descontos com incidência previdenciária subtraindo o desconto de INSS e IRRF
* **8ª Fase: 04/07/2025:** Margem Consignável considerando os demais períodos do envelope de pagamento
* **9º Fase: 09/07/2025:** PORTARIA MTE Nº 933, DE 5 DE JUNHO DE 2025 - Possibilitar realizar mais de um crédito para o mesmo funcionário - [DT - Crédito do Trabalhador eSocial - Cálculos](https://tdn.totvs.com/pages/viewpage.action?pageId=939246677) Veja  também  sobre  alteração  na  importação  no  item  7 em [Importação Empréstimos FEBRABAN/ Crédito Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719677).

A liberação será nos release de mercado, ou seja, a partir do **release 12.1.2410 ou superiores**.

IMPORTANTE:

A partir de Agosto de 2025 foram liberadas melhorias de acordo com as alterações legislativas. Solicitamos que acompanhem os documentos técnicos nas [Novidades da Release](https://tdn.totvs.com.br/display/public/LRM/Novidades+da+Release) e mantenha a versão sempre atualizada.

02. PASSOS PARA UTILIZAÇÃO

## **02. PASSOS PARA UTILIZAÇÃO**

Script

Após a liberação da versão será necessário executar os scripts de criação de tabelas e seus respectivos campos do sistema através do sistema **RM.Atualizador.exe.**

Serão criadas as tabelas abaixo e seu respectivos campos:

* + PFEMPRT
  + PFDESCEMPRT
  + PGRPLANC
  + PREMCREDTRAB - Eventos da remuneração para margem consignável do crédito trabalhador
  + PFREMCREDTRAB - Eventos da remuneração para margem consignável do crédito trabalhador (Anexo do Funcionário)
Novos Códigos de Cálculos

No menu Administração de Pessoal | Eventos, será necessário criar os eventos utilizando os novos códigos de cálculo listados abaixo, conforme especificado na documentação.

* [480 - Desconto Empréstimo Crédito do Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=937704422)
* [481 - Provisão Empréstimo Crédito do Trabalhador Folha](https://tdn.totvs.com.br/pages/viewpage.action?pageId=938311697)
* [482 - Remuneração Base Empréstimo Crédito do Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=938311709)
* [483 - Insuficiência Saldo Empréstimo Crédito Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=938311723)
* [484 - Provento Provisão Empréstimo Créd.Trab.Folha](https://tdn.totvs.com.br/pages/viewpage.action?pageId=938311735)
* [485 - Provisão Crédito Do Trabalhador Férias 1º Mês](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707652)
* [486 - Provisão Crédito Do Trabalhador Férias 2º Mês](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707666)
* [487 - Provisão Crédito Trab. Férias 1º Mês Envelope](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707675)
* [488 - Provisão Crédito Trab. Férias 2º Mês Envelope](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707680)
* [489 - Adiantamento Provisão Emprést.Crédito](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707701)

IMPORTANTE:

A criação do código de cálculo na base é feita com a execução de um recálculo para os patches das versões 12.1.2406, 12.1.2410 e 12.1.2502, então é necessário executar algum recálculo na base e depois inserir os eventos no cadastro de eventos com os respectivos códigos de cálculo.

Parametrizador

No menu Configurações | Parametrizador | Folha Normal | Crédito Trabalhador, deverá ser realizada a devida parametrização para o correto funcionamento do processo, conforme orientações descritas na documentação: [Crédito Trabalhador - Parametrizador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=937259572)

No menu Configurações | Parametrizador | Folha Normal | Eventos Crédito do Trabalhador, deverá informar os eventos que irão compor a remuneração base para o cálculo da margem de desconto do empréstimo do crédito do trabalhador: [Eventos do Crédito Trabalhador](https://tdn.totvs.com.br/pages/releaseview.action?pageId=938311837)

falseObservação

Os eventos de desconto de INSS e IRRF (Folha, 13º Salário e Rescisão), já são considerados na remuneração conforme orientação da Portaria 435, não sendo necessário informa-los. Portanto, para este cadastro os eventos com estes código de cálculo não serão listados para inserção.

Importação do Empréstimo Crédito do Trabalhador

No menu Folha Mensal | Importações | Importação de Empréstimo Consignado FEBRABAN deverá ser importado o arquivo fornecido pelo **Portal Emprega Brasil**, conforme orientações descritas na documentação: [Importação Empréstimos FEBRABAN / Crédito do Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719677&draft=true)

Funcionário - Empréstimo

No menu Administração de Pessoal | Funcionário | Anexos | Folha de Pagamento | Empréstimos, os dados serão automaticamente preenchidos após a importação, conforme descrito na documentação: [Empréstimos Funcionários](https://tdn.totvs.com/pages/viewpage.action?pageId=452719572)

Funcionário - Desconto do Empréstimo

No menu Administração de Pessoal | Funcionário | Anexos | Folha de Pagamento | Empréstimos | Aba Desconto do Empréstimo, os dados serão automaticamente preenchidos após a importação, conforme descrito na documentação: [Desconto do Empréstimos](https://tdn.totvs.com/pages/viewpage.action?pageId=937695241)

Lançamento de provisão no adiantamento

O lançamento do valor referente a **provisão do empréstimo Crédito Trabalhador** no movimento de adiantamento do funcionário deverá ser realizado por meio do **lançamento via Grupo de Eventos**, acessado pelo menu Folha Mensal | Lançamentos | Grupo de Eventos. Detalhes em [Grupos de Eventos](https://tdn.totvs.com.br/display/public/LRM/Grupos+de+Eventos)

Caso o usuário queira lançar o provisionamento do valor do empréstimo no adiantamento, será necessário marcar o parâmetro: **“Lançar Provisionamento do Empréstimo do Crédito do Trabalhador eSocial”**, no momento do lançamento do adiantamento via Grupos de Eventos.

Caso o usuário NÂO queira lançar o provisionamento do valor do empréstimo no adiantamento, NÃO deve marcar o parâmetro: **“Lançar Provisionamento do Empréstimo do Crédito do Trabalhador eSocial”**, no momento do lançamento do adiantamento via Grupos de Eventos.

IMPORTANTE:

A provisão será calculada proporcionalizando o valor do empréstimo da modalidade "Crédito do Trabalhador eSocial" de acordo com o percentual cadastrado em Parâmetros do cadastro de funcionários.

Lançamento de provisão nas férias

Para lançar a **provisão do empréstimo Crédito Trabalhador** nas férias deve marcar o parâmetro "**Lança provisionamento do empréstimo Crédito Trabalhador nas férias**" no menu No menu Configurações | Parametrizador | Férias | [Empréstimos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719223). 

O lançamento do valor referente a **provisão do empréstimo Crédito Trabalhador** nas férias do funcionário deverá ser realizado automaticamente por meio do **cálculo das férias**, acessado pelo menu Administração de Pessoal | Funcionários | Movimento ! Férias.

IMPORTANTE:

Devem ser criados todos os eventos com os códigos de cálculos citados acima em Novos Códigos de Cálculos.

No menu Administração de Pessoal | Funcionário | Anexos | Movimento | Férias existe a possibilidade de lançar empréstimo nas férias de acordo com a parametrização, conforme descrito na documentação: [Cadastro de Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719354). O empréstimo na modalidade "Crédito do trabalhador e-Social" não será descontado nas férias, ou seja, somente será feita a provisão do valor nas férias.  Após o lançamento das férias no envelope de pagamento o usuário deve lançar o grupo de eventos para o desconto do empréstimo dessa modalidade.

Lançamento do Empréstimo na Folha de Pagamento e Rescisão

O lançamento do valor referente ao **empréstimo Crédito Trabalhador** no movimento do funcionário deverá ser realizado por meio do **lançamento via Grupo de Eventos**, acessado pelo menu Folha Mensal | Lançamentos | [Grupos de Eventos](https://tdn.totvs.com.br/display/public/LRM/Grupos+de+Eventos).

Para lançar o provisionamento do valor do empréstimo no adiantamento veja no link acima nesse documento atual com o nome "Lançamento de provisão no adiantamento".

No momento do lançamento da folha de pagamento via Grupos de Eventos, o usuário deverá selecionar os seguintes parâmetros para lançar o empréstimo importado anteriormente:

* **Lançar Empréstimos:** *Todos*
* **Tipo de Empréstimo:** Selecionar o tipo cadastrado correspondente ao *Crédito do Trabalhador*.

Após o lançamento do valor no movimento do funcionário, a alteração poderá ser consultada em dois locais:

* Funcionário | Anexos | Folha de Pagamento | Empréstimos | Aba Empréstimos - Detalhes em [Empréstimos Funcionários](https://tdn.totvs.com/pages/viewpage.action?pageId=452719572)
* Funcionário | Anexos | Folha de Pagamento | Empréstimos | Aba Descontos de Empréstimos - Detalhes em [Empréstimos Funcionários - Descontos de empréstimos](https://tdn.totvs.com/pages/viewpage.action?pageId=937695241)

IMPORTANTE:

O cálculo da margem consignável do funcionário será sobre o somatório de todas as rubricas de vencimento e descontos com incidência previdenciária subtraindo o desconto de INSS e IRRF, mas o usuário terá flexibilidade de informar quais eventos quer considerar para a margem consignável do desconto do empréstimo da modalidade "Crédito do Trabalhador eSocial" usando o parâmetro Configurações | Parametrizador | Folha Normal | Crédito Trabalhador | [Eventos do Crédito Trabalhador devem ser adicionados na base da Contribuição Previdenciária](https://tdn.totvs.com.br/pages/viewpage.action?pageId=937259572) seguindo a paramentrização dos eventos informados em Administração de Pessoal | Funcionário | Anexos | Folha de Pagamento | [Eventos Remuneração Crédito do Trabalhador](https://tdn.totvs.com/pages/viewpage.action?pageId=938311818)  e/ou em Configurações | Parametrizador | Folha Normal | [Eventos do Crédito do Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=938311837).

IMPORTANTE:

Utilizando o parâmetro Configurações | Parametrizador | Folha Normal | Crédito Trabalhador | [Eventos do Crédito Trabalhador devem ser adicionados na base da Contribuição Previdenciária](https://tdn.totvs.com.br/pages/viewpage.action?pageId=937259572) seguindo os eventos informados em Administração de Pessoal | Funcionário | Anexos | Folha de Pagamento | [Eventos Remuneração Crédito do Trabalhador](https://tdn.totvs.com/pages/viewpage.action?pageId=938311818)  e/ou em Configurações | Parametrizador | Folha Normal | [Eventos do Crédito do Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=938311837) o sistema seguirá da seguinte forma:

* PARÃMETRO DESMARCADO SEM EVENTOS INFORMADOS - Serão considerados APENAS eventos que compõem a base da Contribuição Previdenciária
* PARÃMETRO DESMARCADO COM EVENTOS INFORMADOS - Serão considerados APENAS eventos informados no Anexo ou Parametrizador para Remuneração Créd.Trabalhador
* PARÃMETRO MARCADO SEM EVENTOS INFORMADOS - Serão considerados eventos que compõem a base da Contribuição Previdenciária
* PARÃMETRO MARCADO COM EVENTOS INFORMADOS - Serão consideradas Base de INSS **adicionada** dos eventos informados no Anexo ou Parametrizador

**Atenção: Todas as formas acima considerarão os descontos de INSS e IRRF.**

**OUTRAS INFORMAÇÕES ÚTEIS PARA OS PASSOS:**

Eventos Remuneração Crédito do Trabalhador no Cadastro de Funcionários e Eventos do Crédito Trabalhador em Folha Normal no Parametrizador

O cálculo da margem consignável do funcionário será sobre o somatório de todas as rubricas de vencimento e descontos com incidência previdenciária subtraindo o desconto de INSS e IRRF, mas o usuário terá flexibilidade de informar quais eventos quer considerar para a margem consignável do desconto do empréstimo da modalidade "Crédito do Trabalhador eSocial" usando o parâmetro Configurações | Parametrizador | Folha Normal | Crédito Trabalhador | [Eventos do Crédito Trabalhador devem ser adicionados na base da Contribuição Previdenciária](https://tdn.totvs.com.br/pages/viewpage.action?pageId=937259572) seguindo a paramentrização dos eventos informados em Administração de Pessoal | Funcionário | Anexos | Folha de Pagamento | [Eventos Remuneração Crédito do Trabalhador](https://tdn.totvs.com/pages/viewpage.action?pageId=938311818)  e/ou em Configurações | Parametrizador | Folha Normal | [Eventos do Crédito do Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=938311837).

IMPORTANTE:

Utilizando o parâmetro Configurações | Parametrizador | Folha Normal | Crédito Trabalhador | [Eventos do Crédito Trabalhador devem ser adicionados na base da Contribuição Previdenciária](https://tdn.totvs.com.br/pages/viewpage.action?pageId=937259572) seguindo os eventos informados em Administração de Pessoal | Funcionário | Anexos | Folha de Pagamento | [Eventos Remuneração Crédito do Trabalhador](https://tdn.totvs.com/pages/viewpage.action?pageId=938311818)  e/ou em Configurações | Parametrizador | Folha Normal | [Eventos do Crédito do Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=938311837) o sistema seguirá da seguinte forma:

* PARÃMETRO DESMARCADO SEM EVENTOS INFORMADOS - Serão considerados APENAS eventos que compõem a base da Contribuição Previdenciária
* PARÃMETRO DESMARCADO COM EVENTOS INFORMADOS - Serão considerados APENAS eventos informados no Anexo ou Parametrizador para Remuneração Créd.Trabalhador
* PARÃMETRO MARCADO SEM EVENTOS INFORMADOS - Serão considerados eventos que compõem a base da Contribuição Previdenciária
* PARÃMETRO MARCADO COM EVENTOS INFORMADOS - Serão consideradas Base de INSS **adicionada** dos eventos informados no Anexo ou Parametrizador

**Atenção: Todas as formas acima considerarão os descontos de INSS e IRRF.**

Férias

No menu Administração de Pessoal | Funcionário | Anexos | Movimento | Férias existe a possibilidade de lançar empréstimo nas férias de acordo com a parametrização, conforme descrito na documentação: [Cadastro de Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719354). O empréstimo na modalidade "Crédito do trabalhador e-Social" não será descontado nas férias, ou seja, somente será feita a provisão do valor nas férias.  Após o lançamento das férias no envelope de pagamento o usuário deve lançar o grupo de eventos para o desconto do empréstimo dessa modalidade.

Importação | Exportação da Tabela de Empréstimo

No menu Configurações | Importações | Importação de dados da folha de pagamento, realizamos a adequação dos leiautes para contemplar os novos campos, conforme descrito na documentação: 

* [Layout Para Importação de Empréstimo](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719350)
* [Layout Para Importação de Histórico de Empréstimo](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719189)

IMPORTANTE:

Esses layouts apenas foram alterados para adequação da importação de dados sendo que a importação do arquivo de empréstimo crédito do trabalhador originado do Emprega Brasil deve ser importado no menu Folha Mensal | Importações | [Importação Empréstimos FEBRABAN / Crédito do Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719677&draft=true).

Informações para quando existir mais de um empréstimo para o mesmo funcionário:

Quando existir mais de um empréstimo para o mesmo funcionário:

* O provisionamento nas férias e no adiantamento será realizado para todos os empréstimos. O provisionamento será realizado em um único evento, com o somatório dos valores a serem provisionados nos empréstimos. Sendo que nas férias será separado apenas para o 1º mês e 2º mês quando houver férias partidas.

+ Quando não houver saldo no adiantamento da folha será descontado o valor total do empréstimo

* O desconto do empréstimo na folha de pagamento e na rescisão será em ordem cronológica, ou seja, levando em consideração o mais antigo para o mais recente de acordo com a data do empréstimo em: Administração de Pessoal / Funcionários / Empréstimos.

+ Quando houver mais de um empréstimo na mesma data, será considerado o código de cadastro do empréstimo para fins de identificação, pois será a ordenação vinda do arquivo importado.

* No evento de base de insuficiência de saldo registrado no envelope de pagamento será somado o valor por contrato.
* Para o cálculo da Margem Consignável, inicialmente será considerada a margem total disponível, desconsiderando os empréstimos. Em seguida, o valor de cada empréstimo será subtraído sequencialmente: o primeiro empréstimo será descontado da margem, e o valor restante servirá de base para o desconto do próximo empréstimo, e assim por diante.
* O desconto do crédito do trabalhador deverá ocorrer em **eventos distintos** para controle do eSocial, devido cada empréstimo ter um contrato separado.
03. EXEMPLOS DE UTILIZAÇÃO

## **03. EXEMPLOS DE UTILIZAÇÃO**

04. TABELAS UTILIZADAS e VALIDAÇÕES PARA LANÇAMENTOS

## **04. TABELAS UTILIZADAS**

* PFEMPRT
* PFDESCEMPRT
* PGRPLANC
* PREMCREDTRAB
* PFREMCREDTRAB

EXEMPLO DE VALIDAÇÃO PARA LANÇAMENTO DO EMPRÉSTIMO NA FOLHA

* COMPETÊNCIA ATUAL DA BASE - **MESCOMP/ANOCOMP - PPARAM**
* COMPETÊNCIA PARAMETRIZADOR - **ULTCOMPIMPORTADACREDTRAB - PPARAMADICIONAIS**
* INICIO DESCONTO **- INICIODESCONTO - PFEMPRT**
* COMP FINAL DESC - **MESFINAL/ANOFINAL - PFEMPRT**
* COMPETÊNCIA CADASTRO DE EMPRÉSTIMO - **MESCOMPATUAL/ANOCOMPATUAL - PFEMPRT**

LANÇA EMPRÉSTIMO QUANDO

* COMPETÊNCIA ATUAL DA BASE - **03/2026**
* COMPETÊNCIA PARAMETRIZADOR - **03/2026**
* INICIO DESCONTO **- MENOR OU IGUAL 01/03/2026**
* COMP FINAL DESC - **MAIOR OU IGUAL 01/03/2026**
* COMPETÊNCIA CADASTRO DE EMPRÉSTIMO - **03/2026**

NÃO LANÇA EMPRÉSTIMO QUANDO

CENÁRIO 1

* COMPETÊNCIA ATUAL DA BASE - **03/2026**
* COMPETÊNCIA PARAMETRIZADOR - **03/2026**
* INICIO DESCONTO **- MENOR OU IGUAL 01/03/2026**
* COMP FINAL DESC - **MAIOR OU IGUAL 01/03/2026**
* COMPETÊNCIA CADASTRO DE EMPRÉSTIMO - **02/2026**

CENÁRIO 2

* COMPETÊNCIA ATUAL DA BASE - **03/2026**
* COMPETÊNCIA PARAMETRIZADOR - **03/2026**
* INICIO DESCONTO **- MENOR OU IGUAL 01/03/2026**
* COMP FINAL DESC - **MAIOR OU IGUAL 01/03/2026**
* COMPETÊNCIA CADASTRO DE EMPRÉSTIMO - **04/2026**

CENÁRIO 3

* COMPETÊNCIA ATUAL DA BASE - **03/2026**
* COMPETÊNCIA PARAMETRIZADOR - **03/2026**
* INICIO DESCONTO **- 01/04/2026**
* COMP FINAL DESC - **01/04/2026**
* COMPETÊNCIA CADASTRO DE EMPRÉSTIMO - **04/2026**

IMPORTANTE:

01 - O lançamento do empréstimo diretamente no envelope de pagamento não é feita a validação de datas, o cálculo do desconto sempre é feito se for lançado diretamente o evento no envelope de pagamento

02 - Quando usa o **gerenciador de movimento** e cancelar o movimento no envelope de pagamento deve também cancelar os dados do gerenciador porque existirá valor no gerenciador que será lançado indevidamente se não for cancelado.

**Exemplo**

* Lançamento do empréstimo existindo no cadastro do empréstimo na data de 03/2026
* Cancelar somente o envelope
* Não cancelar o lançamento no  gerenciador de movimento
* Mudar a data no cadastro de empréstimo para 04/2026
* Lançar novamente o grupo de eventos
* Lançar o gerenciador de movimento, nesse momento o valor do desconto do empréstimo foi lançado novamente no envelope porque estava no gerenciador
05. DOCUMENTAÇÃO

## **05. DOCUMENTAÇÃO**
