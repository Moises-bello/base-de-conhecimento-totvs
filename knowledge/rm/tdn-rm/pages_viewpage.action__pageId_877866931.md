---
content_hash: 2f1dec47aa1d4e5ea74c71b89607f6e6dd99af98368f0257b8fce1ba21974acc
fetched_at: '2026-06-29T00:12:00.017016+00:00'
page_id: '877866931'
product: rm
source: tdn-rm
title: Integração RM X Ahgora
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=877866931
version: 139
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Parametrização e Exemplo de utilização**

## **01. DOCUMENTAÇÃO**

## **01.1 -****FOLHA DE PAGAMENTO RM**

false

**A PARTIR DOS PATCHES:**

* + - * [DT - Integração RM X Ahgora](https://tdn.totvs.com/pages/viewpage.action?pageId=867821195)
      * [DT - Integração RM X Ahgora - Disponibilização do campo "Utiliza Ponto Ahgora" e do "Histórico Utiliza Ponto Ahgora"](https://tdn.totvs.com/pages/viewpage.action?pageId=874201500)
      * [DT - Integração RM X Ahgora - API de Eventos/Verbas](https://tdn.totvs.com/pages/viewpage.action?pageId=945397449)
      * [DT - Integração RM X Ahgora - API de Sindicato](https://tdn.totvs.com/pages/viewpage.action?pageId=945396604)
      * [DT - Integração RM X Ahgora - Adequação da Matrícula na Transferência](https://tdn.totvs.com/pages/viewpage.action?pageId=950277578)
      * [DT - Integração RM X Ahgora - Opção para Não Enviar Funcionários que Não Batem Ponto](https://tdn.totvs.com/pages/viewpage.action?pageId=960999204)
      * [DT - Integração RM X Ahgora - Hierarquia por Posição](https://tdn.totvs.com/pages/viewpage.action?pageId=967104711)
      * [DT - Integração RM X Ahgora - Processo "Alterar Data Início do Afastamento"](https://tdn.totvs.com/pages/viewpage.action?pageId=969990523)
      * [DT - Integração RM X Ahgora - Melhoria no filtro "Data de Afastamento"](https://tdn.totvs.com/pages/viewpage.action?pageId=969995016)
      * [DT - Integração RM X Ahgora - Gerar gatilho automático para Chefe e Supervisor](https://tdn.totvs.com/pages/viewpage.action?pageId=980985473)
      * [DT - Integração RM X Ahgora - Nome Social](https://tdn.totvs.com/pages/viewpage.action?pageId=982918520)
      * [DT - Integração RM x Ahgora - Envio de Alteração de Chefia da Hierarquia por Posição](https://tdn.totvs.com/pages/viewpage.action?pageId=1063925320)

## **01.2 -** **PONTO WEB AHGORA**

false

* + - * [Layout de campos RM Nativa x Ahgora Ponto Web](https://tdn.totvs.com/display/public/AHINT/ITG2.0-TN11+Layout+de+campos+RM+Nativa+x+Ahgora+PontoWeb)

## **02. VISÃO GERAL**

Disponibilizamos um processo nativo no produto em interface POUI que permite a integração entre **TOTVS** **Folha de Pagamento RM** e o **Ponto Web (Ahgora)**. Através desse processo, é possível integrar três tipos de cadastros:

* **Funcionários**: Todos os funcionários serão integrados conforme o filtro de seleção, incluindo alterações nos dados cadastrais.
* **Afastamentos**: Os afastamentos e férias serão integrados ao sistema Ponto Web da Ahgora, conforme o filtro de seleção.
* **Resultados**: Toda a movimentação existente na Ponto Web  Ahgora, como horas extras e faltas, será integrada ao sistema de Folha de Pagamento RM.
* **Eventos/Verbas:** Todas as verbas existentes no menu Administração de Pessoal | Eventos existentes na coligada.
* **Sindicatos:** Todos os cadastros existentes no menu Administração de Pessoal | Sindicatos existentes na coligada.

## **03. PARAMETRIZAÇÃO E EXEMPLO DE UTILIZAÇÃO**

11ParametrizaçãoParametrização

1) Acesse o menu Serviços Globais | Segurança | Perfis, selecione o sistema Folha de pagamento, edite o perfil desejado, vá em acesso a menus e permita o acesso 01.06 - Ahgora.

2) Acesse RH | Folha de pagamento | Configurações | Parametrizador | 06.02 - Integrações | 06.02.11 - Ahgora

2.1)  **Na aba Gerais:**  Marque a opção "ativa" e cadastre os dados para a integração.

**Tipo de Ambiente:**

* + Produção ou Homologação

**Configurações conexão Ahgora:**

* + **Usuário**
  + **Senha**
  + **Endereço do servidor:** Endpoint da Ahgora. Campo é de preenchimento obrigatório, caso tenha envio especifico para envio de funcionário ou afastamento é necessário o preenchimento dos campos completos abaixo. 
    - Exemplo: https://api.ahgora.com.br/
  + **Serviço Funcionário**: Endpoint da Ahgora para o envio do Funcionário. Não é obrigatório o preenchimento.  Caso não seja preenchido será considerado o default da Ahgora (people). 
    - Exemplo: [https://api.ahgora.com.br/people](https://api.ahgora.com.br/)
  + **Serviço Afastamento:** Endpoint da Ahgora para o envio do Afastamento. Não é obrigatório o preenchimento.  Caso não seja preenchido será considerado o default da Ahgora (absences). 
    - Exemplo.: [https://api.ahgora.com.br/absences](https://api.ahgora.com.br/)

ATENÇÃO:

1. As informações de acesso ao ambiente da Ahgora devem ser solicitadas ao responsável do contrato da Ahgora.
2. Caso possua restrição em seu firewall, verifique se o endereço **[https://api.ahgora.com.br](https://api.ahgora.com.br/)** possuem liberação para conexão externa.
3. Para utilização das integrações de Resultados, Sindicatos e Eventos é necessário a habilitação da licença I, que permite o acesso às APIs que disponibilizam estes dados. Caso você não possua a licença I, entre em contato com seu ESN.
4. É possível enviar múltiplas coligadas para um único ambiente da Ahgora, bem como direcionar cada coligada para ambientes específicos, conforme a necessidade e dependendo da configuração de conexão.

**⚠️ ATENÇÃO:**

**Gerar Funcionários**

Gerar todos os funcionários, incluindo líderes e líderes externos, independentemente de baterem ponto  
Ao selecionar esta opção, serão gerados gatilhos para todos os funcionários, sem exceção, que batem ou não ponto.

Gerar somente funcionários e líderes que batem ponto  
Essa opção gera gatilhos apenas para funcionários e líderes (funcionários) que realizam marcação de ponto.

Gerar funcionários e líderes que batem ponto, além dos líderes que não batem ponto  
Com essa opção, serão gerados gatilhos para todos os funcionários e líderes que batem ponto.

**⚠️ ATENÇÃO:**

* + - Esses parâmetros estão disponíveis a partir dos patches mencionados no [DT - Integração RM x Ahgora – Opção para Não Enviar Funcionários que Não Batem Ponto](https://tdn.totvs.com/pages/viewpage.action?pageId=960999204)
    - A identificação de colaboradores que batem ponto ou não será realizada por meio da marcação disponível no menu Menu Funcionários | Aba Registro | Aba Ahgora.
    - A opção **"Integrar todos os colaboradores: Gerar todos os funcionários, incluindo líderes, que batem ou não ponto"** será definida como opção padrão (default) no sistema.

2.2) **Na aba** **Agendamento:** Você pode programar a integração dos registros que foram gravados para ocorrerem automaticamente, sem a necessidade de interação do usuário, tornando o processo mais dinâmico e produtivo. Isso funciona com o JobServer configurado para execução em modo 3 Camadas. Para mais informações sobre a configuração, clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=270085915).

2.3) **Na aba Fórmula para localizações:** Nesta aba será realizada a vinculação de fórmulas onde o usuário poderá definir qual campo do funcionário deseja enviar no campo "Localização" da integração com o Ponto Web (Ahgora).

Para isso o usuário deverá criar uma fórmula através do menu Administração de Pessoal | Fórmulas e incluir a fórmula nessa aba:

**Exemplos de fórmulas que podem ser criadas:**

1) Retornar o campo NOME do funcionário, deverá criar a formula abaixo:

2) Retornar um texto livre "DESENVOLVIMENTO RM", deverá criar a formula abaixo:

**⚠️ ATENÇÃO:**

1. 1. * Após a vinculação das fórmulas no parametrizador, sempre que houver integração de um funcionário (Inclusão/Alteração) as localizações serão enviadas.
      * Essa aba está disponível a partir dos patches mencionados no

2.4) **Na aba Filiais:** A partir da inclusão do registro da filial, o sistema realiza a geração dos gatilhos de Funcionários e Afastamentos exclusivamente para as filiais cadastras nessa aba.

**Exemplo:**

O Funcionário **00001** está lotado na **Filial 01**, enquanto o Funcionário **00002** está lotado na **Filial 09**.

Com a parametrização conforme o print acima, **apenas** o gatilho de integração para o Funcionário **00001** será gerado.

3) **Utiliza Ponto Ahgora**

3.1) Acesse Administração de Pessoal | Funcionários | Submenu Registros, será exibida a nova aba "**Ahgora**", onde você poderá marcar a opção de utilização de ponto.(A aba só será exibida após a parametrização do item 2).

3.2) Alteração Global: Caso deseje realizar a marcação do campo para um grupo especifico de funcionários acesse  Administração de Pessoal | Alterações Cadastrais | Alteração Campos do Cadastro selecione o campo "**O funcionário utiliza ponto ahgora: - UTILIZAPONTOAHGORA**", cadastre a fórmula para a alteração sendo "**true"** parâmetro marcado e "**false"** parâmetro desmarcado e selecione os funcionários desejados, e execute o processo.

**Exemplo da fórmula SQL**

**Exemplo da fórmula ORACLE**

3.3) Acesse o menu Serviços Globais | Segurança | Perfis, e conceda permissão para acesso ao histórico da aba "**Ahgora**".

3.4) Acesse Administração de Pessoal | Funcionários | Anexos | Históricos | Histórico Utiliza Ponto Ahgora, para visualizar o histórico cadastrado para o campo "**Utiliza Ponto Ahgora**".

2Parametrização AhgoraParametrização Ahgora

Antes da integração, é necessário que os cadastros básicos já existam no sistema da Ahgora. Abaixo estão os dados e onde encontrá-los no RM:

* **Sindicatos - Tabela PSINDIC**

**Importante:** Código precisa ser igual ao cadastro do RM

* **Horários no RM => Escala Ahgora - Tabela AHORARIO**

**Importante:** Código precisa ser igual ao cadastro do RM

* **Eventos no RM => Rubrica na Ahgora- Tabela PEVENTO**

**Importante:** código precisa ser igual ao cadastro do RM

* **Centro de Custos - Tabela PCCUSTO**

**Importante:** código precisa ser igual ao cadastro do RM.

* **Tipo de Afastamentos - Tabela PCODAFAST**

3TabelaTabela

A tabela **PINTEGRACAOENVIOAHGORA** é utilizada pela integração entre a Folha RM e o Ponto Web da Ahgora, sendo responsável por armazenar os registros de alterações que serão sincronizados com o Ahgora.

Após a parametrização da integração, o sistema passa a gerar um registro sempre que ocorrerem alterações nos dados cadastrais ou de afastamento dos funcionários.

Os registros são armazenados na tabela **PINTEGRACAOENVIOAHGORA**, que mantém **apenas um registro pendente por funcionário**. Dessa forma, caso novas alterações sejam realizadas antes que o envio seja processado, o registro existente será atualizado com as informações mais recentes, evitando o acúmulo de registros pendentes e garantindo que apenas a última situação do funcionário seja enviada ao Ahgora.

### Exemplo: Alteração de horário

Suponha que o horário de um funcionário seja alterado três vezes no mesmo mês e que o registro de integração ainda permaneça com status **Pendente**. Nesse cenário, o sistema não criará novos registros. Em vez disso, atualizará o registro existente na **PINTEGRACAOENVIOAHGORA** com os dados da última alteração realizada. Assim, quando a integração for executada, somente a informação mais recente será enviada ao Ahgora.

### Fluxo da integração

O processo de integração ocorre da seguinte forma:

1. É realizada uma alteração no RM (admissão, alteração contratual, férias, afastamento, entre outras).
2. O sistema cria ou atualiza o registro correspondente na tabela **PINTEGRACAOENVIOAHGORA**.
3. O processo de integração consulta os registros com status **Pendente**.
4. As informações são enviadas para a API do Ahgora.
5. Após o processamento, o status do registro é atualizado para **Sucesso** ou **Erro**.
6. Em caso de falha, a mensagem retornada pela API é armazenada no registro, permitindo a análise da ocorrência e o posterior reprocessamento.

| CAMPO DA TABELA | REGRA PREENCHIMENTO DO CAMPO | OBSERVAÇÃO |
| --- | --- | --- |
| ID |  |  |
| CODCOLIGADA | PFUNC.COLIGADA |  |
| CODFILIAL |  |  |
| CHAPA | PFUNC.CHAPA |  |
| MATFUNCIONARIO | PFUNC.COLIGADA + PFUNC.CHAPA |  |
| CODUNIQUE |  |  |
| CODSUBUNIQUE |  |  |
| ERROENVIO |  |  |
| ERRODETALHES |  |  |
| STATUS | 0 - Não Integrado | * **Status:** Correspondente na tela de integração:   + NI - Integrados   + 0 => IN => Não Integrados   + CI - Com Inconsistências   + AR - Aguardando Retorno |
| SERVIÇO |  |  |
| PAYLOAD |  |  |
| DATAINICIOAFASTAMENTO |  |  |
| CODINTERNO |  |  |
| CODCOLIGADAANTERIOR | É preenchido durante o processamento de transferências do **tipo 5** (transferência entre coligadas). | **Exemplo:**   * **Origem:** Coligada **1**, Filial **3**, Chapa **010106132** * **Destino:** Coligada **2**, Filial **1**, Chapa **020104908**   **Valor preenchido:** `1` |
| CHAPAANTERIOR | É preenchido durante o processamento de transferências do **tipo 5** (transferência entre coligadas). | **Exemplo:**   * **Origem:** Coligada **1**, Filial **3**, Chapa **010106132** * **Destino:** Coligada **2**, Filial **1**, Chapa **020104908**   **Valor preenchido: `010106132`** |
| CODFILIALANTERIOR | É preenchido durante o processamento de transferências do **tipo 5** (transferência entre coligadas). | **Exemplo:**   * **Origem:** Coligada **1**, Filial **3**, Chapa **010106132** * **Destino:** Coligada **2**, Filial **1**, Chapa **020104908**   **Valor preenchido:** **3** |

falseATENÇÃO:

Foram implementados os campos `CODCOLIGADAANTERIOR`, `CHAPAANTERIOR` e `CODFILIALANTERIOR` na tabela **PINTEGRACAOENVIOAHGORA**.

Esses campos permitem que, na **primeira integração após o funcionário ser transferido**, as informações de origem sejam enviadas corretamente para o sistema **Ponto Web (Ahgora)**, garantindo o tratamento adequado da alteração.

As versões contendo essa atualização estão disponíveis no [DT - Integração RM X Ahgora - Adequação da Matrícula na Transferência](https://tdn.totvs.com/pages/viewpage.action?pageId=950277578).

4IntegraçãoIntegração

Através do menu Administração de Pessoal | Ahgora, é possível realizar a integração dos dados , utilizando os filtros disponíveis na tela.

Ao acessar o novo menu criado, abre-se uma nova tela com as opções:

Integração3-1FuncionáriosFuncionários

Nessa nova tela, será exibido o menu para integração dos funcionários

Na tela inicial são apresentados filtros básicos para a seleção do funcionários que serão enviados. Como sugestão, a 'Data Admissão De' vem preenchida com um mês anterior que a data atual e a 'Data Admissão Até' com a data atual. Filtros de 'Filial' e 'Data Admissão De' são obrigatórios.

Para mais filtros, é necessário acessar a opção de 'Filtros Avançados'. Na opção de 'Filtros Avançados', é possível realizar mais alguns filtros específicos além dos filtros já apresentados na primeira tela.

Selecionando os filtros na tela de filtros avançados ou na tela inicial, e ao clicar no botão 'Aplicar Filtros', o sistema buscará as informações dos funcionários.

### Apresentação das Informações

Ao aplicarmos os filtros será apresentada a seguinte tela:

#### Lista de Funcionários

Ao obter a lista de funcionários, temos as colunas:

* **Status:** Correspondente ao status do registro
  + Legenda verde, Tag 'NI' - Integrados
  + Legenda azul, Tag 'IN' - Não integrados
  + Legenda vermelha, Tag 'CI' - Com Inconsistências
  + Legenda laranja, Tag 'AR' - Aguardando Retorno

* **Matrícula Ahgora:** Codigo da coligada + Chapa do funcionário
* **Nome:** Nome do funcionário
* **Dt. Admissão**: data de admissão
* **Dt. Demissão:** data de demissão
* **Horário:** codigo do horário do funcionário
* **Função:** Função do funcionário
* **Movimento:** Inclusão/Alteração (status alteração ocorrerá sempre que o primeiro cadastro ja tenha sido enviado para ahgora)
* **Dt. Movimento:** Data da movimentação (envio a ahgora)

Serão listados 100 registros por página, ao final da página será mostrado o botão para "carregar mais resultados" .

Para realizar o envio, selecione o registro desejado e clique em "integrar funcionários" .

Ao integrar o registro, se ocorrer tudo certo, o registro será alterado para 'Aguardando Retorno'. Basta selecioná-lo novamente e atualizar o status para verificar o retorno da integração.

Ao final da atualização do status, o registro será alterado:

**'IN' - Integrado**: o registro foi integrado com sucesso.

**'CI' - Com Inconsistências:** Registro com erro fica com a legenda em vermelho, e você pode consultar o erro, na opção status que está localizada ao clicar nos 3 pontinhos na parte direita da tabela.

Erro é apresentado na tela

Na tela acima ao integrar um funcionário o sistema verifica na estrutura do cadastro de chefe/supervisor da estrutura das seções para preencher a tag "nome \_chefia" no Json.

**Exemplo1:**

Funcionário **A**, está alocado na seção 01.03 e possui em seucadastro o código de equipe **"01"** (CODEQUIPE.PFUNC). Na tabela de chefe/supervisor a seção 01.03 não possui nem chefe/supervisor direto.  Ao enviar o cadastro deste funcionário para a Ahgora, será enviado na tag o chefe da seção superior.

**Exemplo 2:**

Funcionário **B**, está alocado na seção 02.01 e possui em seucadastro o código de equipe **"01"** (CODEQUIPE.PFUNC). Na tabela de chefe/supervisor a seção 02.01 possui o chefe  **X** e o supervisor **Y** está com o código de equipe 01. Ao enviar o cadastro deste funcionário para a Ahgora, será enviado na tag o chefe da seção 02.01.

**Exemplo 3:**

Funcionário **C**, está alocado na seção 03.01 e possui em seucadastro o código de equipe **"01"** (CODEQUIPE.PFUNC). Na tabela de chefe/supervisor a seção 03.01 não possui o chefe **X** e o supervisor **Y** está com o código de equipe 01. Ao enviar o cadastro deste funcionário para a Ahgora, será enviado na tag o supervisor que está com o mesmo código de equipe associado.

### **⚠️ Importante:**

* + 1. Ao editar, adicionar ou remover um supervisor, será atualizado o gatilho dos funcionários que estão na mesma equipe para o status "**NI**".
    2. Critérios para desempate no envio de Chefe/supervisor:

**Exemplo:**

* + - * Supervisor e Chefe com o master desmarcado: Será priorizado o envio do Chefe.
      * Supervisor e Chefe com o master marcado: Será priorizado o envio do Chefe.
      * Supervisor com o master marcado e Chefe desmarcado: Será priorizado o envio do Supervisor.
      * 2 Chefes no mesmo nível de seção com o master desmarcado: Será enviado o Chefe com a menor chapa.
      * 2 Chefes no mesmo nível de seção com o master marcado: Será enviado o Chefe com a menor chapa.
      * 2 Supervisores com o mesmo código de equipe e com o master marcado: Será enviado o supervisor com a menor chapa.
      * 2 Supervisores com o mesmo código de equipe e com o master desmarcado: Será enviado o supervisor com a menor chapa.

falseATENÇÃO:

Foram implementados os campos `CODCOLIGADAANTERIOR`, `CHAPAANTERIOR` e `CODFILIALANTERIOR` na tabela **PINTEGRACAOENVIOAHGORA**.

Esses campos permitem que, na **primeira integração após o funcionário ser transferido**, as informações de origem sejam enviadas corretamente para o sistema **Ponto Web (Ahgora)**, garantindo o tratamento adequado da alteração.

As versões contendo essa atualização estão disponíveis no [DT - Integração RM X Ahgora - Adequação da Matrícula na Transferência](https://tdn.totvs.com/pages/viewpage.action?pageId=950277578).

3-2AfastamentosAfastamentos

Nessa nova tela, será exibido o menu para integração dos Afastamentos

Na tela inicial são apresentados filtros básicos para a seleção dos afastamentos que serão enviados. Como sugestão, a 'Data Afastamento De' vem preenchida com um mês anterior que a data atual e a 'Data Afastamento Até' com a data atual. Filtros de 'Filial' e 'Data Afastamento De' são obrigatórios.

Para mais filtros, é necessário acessar a opção de 'Filtros Avançados'. Na opção de 'Filtros Avançados', é possível realizar mais alguns filtros específicos além dos filtros já apresentados na primeira tela.

Selecionando os filtros na tela de filtros avançados ou na tela inicial, e ao clicar no botão 'Aplicar Filtros', o sistema buscará as informações dos afastamentos dos funcionários.

### Apresentação das Informações

Ao aplicarmos os filtros será apresentada a seguinte tela:

#### Lista de Afastamentos

Ao obter a lista de funcionários, temos as colunas:

* **Status:** Correspondente ao status do registro
  + Legenda verde, Tag 'NI' - Integrados
  + Legenda azul, Tag 'IN' - Não integrados
  + Legenda vermelha, Tag 'CI' - Com Inconsistências
  + Legenda laranja, Tag 'AR' - Aguardando Retorno

* **Matrícula Ahgora:** Código da coligada + Chapa do funcionário
* **Nome:** Nome do funcionário
* **Tipo do afastamento:** Tipo e descrição do afastamento
* **Dt. Início:** Inicio do afastamento
* **Dt. Fim:** Fim do afastamento
* **Movimento:** Inclusão/Alteração  (status alteração ocorrerá sempre que o primeiro cadastro já tenha sido enviado para Ahgora)
* **Dt. Movimento:** Data da movimentação (envio a Ahgora)

Serão listados 100 registros por página, ao final da página será mostrado o botão para "carregar mais resultados" .

Para realizar o envio, selecione o registro desejado e clique em "Integrar Afastamentos" .

  

Ao integrar o registro, se ocorrer tudo certo, o registro será alterado para 'Aguardando Retorno'. Basta selecioná-lo novamente e atualizar o status para verificar o retorno da integração.

Ao final da atualização do status, o registro será alterado:

**'IN' - Integrado**: o registro foi integrado com sucesso.

**'CI' - Com Inconsistências:** Registro com erro fica com a legenda em vermelho, e você pode consultar o erro, na opção status que está localizada ao clicar nos 3 pontinhos na parte direita da tabela.

Erro é apresentado na tela:

3-3Exclusão AfastamentosExclusão Afastamentos

Nessa nova tela, será exibido o menu para integração das Exclusões dos Afastamentos

Na tela inicial são apresentados filtros básicos para a seleção das exclusões dos afastamentos que serão enviados. Como sugestão, a 'Data Exclusões De' vem preenchida com um mês anterior que a data atual e a 'Data Exclusões Até' com a data atual. Filtros de 'Filial' e 'Data Exclusões De' são obrigatórios.

Para mais filtros, é necessário acessar a opção de 'Filtros Avançados'. Na opção de 'Filtros Avançados', é possível realizar mais alguns filtros específicos além dos filtros já apresentados na primeira tela.

Selecionando os filtros na tela de filtros avançados ou na tela inicial, e ao clicar no botão 'Aplicar Filtros', o sistema buscará as informações das Exclusões de afastamentos dos funcionários.

### Apresentação das Informações

Ao aplicarmos os filtros será apresentada a seguinte tela:

#### Lista de Afastamentos

Ao obter a lista de funcionários, temos as colunas:

* **Status:** Correspondente ao status do registro
  + Legenda verde, Tag 'NI' - Integrados
  + Legenda azul, Tag 'IN' - Não integrados
  + Legenda vermelha, Tag 'CI' - Com Inconsistências
  + Legenda laranja, Tag 'AR' - Aguardando Retorno

* **Matrícula Ahgora:** Código da coligada + Chapa do funcionário
* **Nome:** Nome do funcionário
* **Tipo do afastamento:** Tipo e descrição do afastamento
* **Dt. Início:** Inicio do afastamento
* **Dt. Fim:**Fim do afastamento
* **Movimento:** Exclusão
* **Dt. Movimento:** Data da movimentação (envio a Ahgora)

Serão listados 100 registros por página, ao final da página será mostrado o botão para "Carregar mais resultados" .

**Atenção:** serão gravadas as exclusões dos afastamentos que possuam o status 'NI' - Integrados

Para realizar o envio, selecione o registro desejado e clique em "Integrar Exclusões" .

Ao integrar o registro, se ocorrer tudo certo, o registro será alterado para 'Aguardando Retorno'. Basta selecioná-lo novamente e atualizar o status para verificar o retorno da integração.

Ao final da atualização do status, o registro será alterado:

**'IN' - Integrado**: o registro foi integrado com sucesso.

**'CI' - Com Inconsistências:**Registro com erro fica com a legenda em vermelho, e você pode consultar o erro, na opção status que está localizada ao clicar nos 3 pontinhos na parte direita da tabela.

Erro é apresentado na tela

Ao selecionar um funcionário

3-4Agendamento do processoAgendamento do processo

Após a realização da ativação da integração com a Ahgora, o sistema começa a registrar automaticamente os novos eventos de admissão, alteração e exclusão relacionados aos funcionários e seus afastamentos. Para o envio a Ahgora.

Para realizar o agendamento desses envios acesse: Acesse RH | Folha de pagamento | Configurações | Parametrizador | 06.02 - Integrações | 06.02.11 - Ahgora.

Na aba **Agendamento**, você pode programar a integração dos registros que foram gravados para ocorrerem automaticamente, sem a necessidade de interação do usuário, tornando o processo mais dinâmico e produtivo. Isso funciona com o JobServer configurado para execução em modo 3 Camadas. Para mais informações sobre a configuração, clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=270085915).

Para consultar os envios basta acessar RH | Folha de pagamento | Ambiente | Gerenciador de Jobs.

Serão criados dois jobs **FopEnviarFuncionariosAfastamentosAhgoraProcess** (envio dos funcionários/afastamento e exclusões) e **FopAtualizarStatusAhgoraProcess** (Solicitação de atualização de status);

3-5Apuração de ResultadosApuração de Resultados

Para gerar as credenciais de Resultados para cadastro na Ahgora.

* Realize a configuração do DefaultDB. Informações em [Configurando DefaultDB](https://tdn.totvs.com/display/LRM/Configurando+DefaultDB)
* Usuário e senha que serão fornecidos: Criar um usuário do sistema Folha de pagamento que possua permissão (01.06 - Ahgora), conforme aba "Parametrização"
* API para recebimento da apuração é composta por **servidor**: maquina onde o RM está instalado + **Api****Port** do host e o caminho fixo "**/api/rh/v1/ahgora/results**".

**Exemplo:** http://servidor:ApiPort/api/rh/v1/ahgora/results 

* API para listagem de sindicatos é composta por **servidor**: maquina onde o RM está instalado + **Api****Port** do host e o caminho fixo "**/api/rh/v1/ahgora/sindicatos**".

**Exemplo:**http://servidor:ApiPort/api/rh/v1/ahgora/sindicatos

* API para listagem de eventos/verbas é composta por **servidor**: maquina onde o RM está instalado + **Api****Port** do host e o caminho fixo "**/api/rh/v1/ahgora/verbas**".

**Exemplo**: http://servidor:ApiPort/api/rh/v1/ahgora/verbas

**IMPORTANTE:**

* Método de autenticação Basic;
* Será utilizado método post para entrega de dados;
* Ao criar a URL, liberar porta para acesso externo;
* Caso tenha restrição de IPs, liberar para a lista abaixo, para entrega da apuração pelo Ponto Web:  
  + [107.22.93.4/32](http://107.22.93.4/32)
  + [50.19.246.167/32](http://50.19.246.167/32)
  + [138.219.88.0/23](http://138.219.88.0/23)

Após a apuração do ponto na Ahgora, realize o envio para o RM das informações.

A Folha de Pagamento RM guardará as informações recebidas em Folha Mensal | Consulta | Consulta Movimento da Integração.

Poderá ser encontrada com o tipo de lançamento **Ahgora**.

Caso o parâmetro "Utiliza controle de faltas para cálculo de avos" esteja marcado, o sistema guardará as faltas no histórico de faltas.

Acesse Administração de pessoal | Funcionários | Anexos | Movimento | Controle de Faltas para Cálculo de Avos.

Para processar os eventos para a folha de pagamento será necessário o processamento no grupo de eventos com o novo tipo criado. Acesse Folha Mensal | Lançamentos | Grupo de eventos.

Selecione o grupo de eventos que irá lançar o movimento e clique em editar.

Marque o parâmetro "Lançar eventos da integração com outros aplicativos" na aba Identificação.

Será criado a aba "Integração com outros aplicativos ", selecione a nova integração "TOTVS Ahgora" e faça o lançamento.

Verifique que os valores foram lançado corretamente para o envelope de pagamento.

**Importante:**

* + Caso seja necessário remover algum evento, será preciso realizar uma nova carga de envio dos eventos da Ahgora. Em seguida, será necessário reprocessar os passos descritos anteriormente para garantir a correção dos lançamentos no envelope de pagamento.
  + Sempre que a integração for processada, o sistema substituirá os eventos existentes com base nos seguintes campos: **coligada, chapa, ano, mês e origem do evento**.

3-6LocalizaçõesLocalizações

A **localização** é uma propriedade criada no envio do funcionário.

Para possibilitar o envio deste campo é necessário a vinculação de fórmulas através do menu RH | Folha de pagamento | Configurações | Parametrizador | 06.02 - Integrações | 06.02.11 - Ahgora | Aba Fórmula para Localizações.

**ATENÇÃO:**

* Caso não seja definida nenhuma localização, não será enviada a propriedade 'localizacoes' no json do funcionário.
* Para o desenvolvimento das fórmulas será possível utilizar funções retornando campos do cadastro do funcionário ou a criação de novos campos, desde que estes retornem em string até 100 caráteres.
* Campos strings do banco que possuem mais de 100 caracteres serão truncados.
* O gatilho não será acionado se o contexto da fórmula for alterado. Se for necessário fazer alguma alteração, crie uma nova fórmula e substitua a atual.

**Exemplo de criação de Fórmula:**

Após a vinculação das fórmulas no parametrizador, sempre que houver integração de um funcionário (Inclusão/Alteração) as localizações serão enviadas.

4DE-PARADE-PARA1De-ParaDe-Para

### **1 - FUNCIONÁRIOS**

| DESCRIÇÃO NA AHGORA | CAMPO DA TABELA RM | DESCRIÇÃO | REGRA |
| --- | --- | --- |
| Identificação do colaborador | PFUNC.CODICOLIGADA + PFUNC.CHAPA | Coligada + Chapa do Funcionário Não pode haver matricula repetida na mesma coligada. As matrículas serão enviadas sem caracteres especiais. |
| Nome do Funcionário | PPESSOA.NOME | Nome do Funcionário. É permitido acentuação e caracteres especiais. |
| Nome Social | PPESSOA.NOMESOCIAL | Para os funcionários que possuem **Nome Social**, o json será gerado conforme o detalhamento abaixo:   * "nome": "NOME SOCIAL", * "checkbox\_nome\_social": true, * "nome\_registro": "NOME" |
| PIS do Funcionário | PFUNC.PISPASEP | Numero do PIS do Funcionário. Enviar somente números. Quando não houver, deverá preencher o campo "sem\_pis" com true |
| Matrícula do E-Social | PFUNC.MATRICULAESOCIAL | Matricula do eSocial |
| Data em que o Funcionário foi Admitido | PFUNC.DATAADMISSAO | Data de Admissão. YYYY-MM-DD |
| Data de Demissão | PFUNC.DATADEMISSAO | Data de Demissão. YYYY-MM-DD Transferência do tipo "5" não é considerado como demissão, mandar esse campo em branco para esse tipo. |
| Localizações do funcionário | Formula na tela do processo | Adicionar um campo na interface onde o usuário possa informar uma fórmula personalizada. Este campo será aberto, permitindo que qualquer campo do cadastro do funcionário seja utilizado. A funcionalidade visa facilitar a criação de filtros e a geração de relatórios no sistema Ahgora. Trata-se de um campo flexível, definido pelo usuário, que oferece maior liberdade e precisão na manipulação de dados e relatórios. |
| Código da escala/ turno do funcionário | PFHSTHOR.CODHORARIO | Horário do Funcionário - Histórico Horário Preencher com o último existente no histórico de horário. Coligada + Código |
| Data da alteração de escala/turno | PFHSTHOR.DTMUDANCA | Data da Mudança do Horário do Funcionário. YYYY-MM-DD Preencher com o último existente no histórico de horário. |
| Tipo de Escala de Trabalho | NÃO ENVIAR | Não existe essa informação na folha de pagamento. |
| Carteira de Trabalho | PPESSOA.CARTEIRATRAB PPESSOA.SERIECARTTRAB PPESSOA.UFCARTTRAB | Carteira de Trabalho Concatenar os 3 campos (numero, série e UF), separando os campos com barra "/". Exemplo: 9999/999/MG |
| Título do Cargo | PHSTFCO.CODFUNCAO | Função do Funcionário => Histórico de Função Preencher com o último existente no histórico de função. Concatenar o Código + Descrição, separando com traço "-". Exemplo: 001-ANALISTA DE SISTEMAS |
| Descrição do departamento do Funcionário | PFUNC.CODSECAO | Seção do funcionário Concatenar o Código + Descrição, separando com traço "-". Exemplo: 01.01.03-DEPARTAMENTO PESSOAL |
| Gênero do Funcionário | PPESSOA.SEXO | Sexo do Funcionário. Preencher com F ou M. |
| E-mail do Funcionário | PPESSOA.EMAIL | E-mail do funcionário. Múltiplos vínculos ter um e-mail por funcionário, não pode ser repetido. |
| CPF do Funcionário | PPESSOA.CPF | CPF do Funcionário. Preencher sem caracteres. Exemplo: 11122233344. |
| RG do Funcionário | PPESSOA.CARIDENTIDADE | Carteira de Identidade. Preencher apenas com o RG, podendo ter caracteres. Exemplo: M-7.7777 |
| CNPJ da filial do Funcionário | PSECAO.CGC (JOIN) PFUNC.CODSECAO | CNPJ da Seção do funcionário. Preencher apenas com números, sem caracteres. |
| Data da atribuição do CNPJ da empresa ao funcionário | PFUNC.DTTRANSFERENCIA | Data da Transferência entre filiais ou coligada. YYYY-MM-DD |
| Código do centro de custo do funcionário | PSECAO.NROCENCUSTOCONT | Coligada + Número do Centro de Custo da Seção do Funcionário. **Caminho Seções | Dados Contábeis | Número do Centro de Custo** |
| Regime de Trabalho do Funcionário | DE/PARA NO PARAMETRIZADOR DO RM | É realizado um DE/PARA interno pelo produto, considerando os campos:   * Tipo de Recebimento * Código Recebimento * Categoria   Veja o mapeamento do DE/PARA no item **1-1** abaixo. |
| Data de Nascimento do Funcionário | PPESSOA.DTNASCIMENTO | Data de Nascimento. YYYY-MM-DD |
| Data de Alteração de Cargo | PHSTFCO.DTMUDANCA | Data da Mudança da Função do Funcionário. YYYY-MM-DD Preencher com o último existente no histórico de função. |
| Definição de carga horária | PFUNC.JORNADA\_MENSAL | Jornada Mensal do Funcionário. Preencher com a quantidade de horas mensais. Exemplo: 220 |
| Ponto Obrigatório | PFHSTUTILIZACAMPOAHGORA.UTILIZAPONTO | Enviar true ou false. |
| Data de troca da elegibilidade do registro de ponto | PFHSTUTILIZACAMPOAHGORA.DTMUDANCA | Enviar a data quando passou a utilizar ponto, ou quando deixou de utilizar ponto. YYYY-MM-DD |
| Matrícula Chefia Imediata | PFUNC.CODICOLIGADA + PFUNC.CHAPA | Coligada + Chapa do chefe/supervisor do funcionário ou código do chefe/supervisor externo.  As matrículas serão enviadas sem caracteres especiais.  Para identificar o chefe/supervisor, é feita a verificação nas seguintes tabelas:   * **Chefe/Supervisor interno** (quando o chefe/supervisor é um funcionário): PSUBSTCHEFE e PSUBSTSUP * **Chefe/Supervisor externo** (quando o chefe/supervisor não é funcionário): PCHEFEEXTERNO e PSUPERVEXTERNO |
| Nome Chefia Imediata | PFUNC.NOME | Nome do chefe/supervisor do Funcionário, ou nome do chefe/supervisor externo. É permitido acentuação e caracteres especiais.  Para identificar o chefe/supervisor, é feita a verificação nas seguintes tabelas:   * **Chefe/Supervisor interno** (quando o chefe/supervisor é um funcionário): PSUBSTCHEFE e PSUBSTSUP * **Chefe/Supervisor externo** (quando o chefe/supervisor não é funcionário): PCHEFEEXTERNO e PSUPERVEXTERNO |
| e-mail Chefia Imediata | PPESSOA.EMAIL | E-mail do chefe/supervisor do funcionário ou e-mail do chefe/supervisor externo.  Para identificar o chefe/supervisor, é feita a verificação nas seguintes tabelas:   * **Chefe/Supervisor interno** (quando o chefe/supervisor é um funcionário): PSUBSTCHEFE e PSUBSTSUP * **Chefe/Supervisor externo** (quando o chefe/supervisor não é funcionário): PCHEFEEXTERNO e PSUPERVEXTERNO |
| Código do Sindicato | PFUNC.CODSINDICATO | Código do Sindicato do funcionário |
| Data da alteração do código do sindicato |  | Não enviamos este campo, pois não existe essa data no produto. |
| Telefone | PPESSOA.TELEFONE2 | Número do Telefone Celular. Permite caracteres especiais. |
| Pis | PFUNC.PISPASEP | Preencher com true quando não tiver o PIS cadastrado e false quando tiver PIS cadastrado. |
| codInterno | PFUNC.CHAPA | Coligada + Chapa Chapa do Funcionário. Não pode haver matricula repetida na mesma coligada. |
| matricula\_anterior | PFUNC.CHAPAORIGEM | Preencher com a chapa do registro demitido. Este campo deve ser preenchido quando houve transferência do tipo "5" e o funcionário ativo tiver uma nova chapa.  Veja mais detalhes no link |
| Define o custo hora do funcionário, utilizado para cálculos financeiros. | PFUNC.SALARIO / PFUNC.JORNADA | Salario hora |
| Valor do salário do colaborador | PFUNC.SALARIO | Salario do funcionário |

### **1-1 - MAPEAMENTO (DE/PARA) DO CAMPO REGIME DE TRABALHO DO FUNCIONÁRIO**

| DESCRIÇÃO NA AHGORA | RM - CAMPO TIPO DE RECEBIMENTO |
| --- | --- |
| autonomo | A - Autônomo |
| CLT | N - Normal (Exceto para **Categoria 106** ou **Tipo de Recebimento H**) R - Rural ou U - Outros ou I - Cedido ou V - Contrato verde/Amarelo ou  X - Expatriado |
| comissionado | O - Comissionista ou  M - Misto |
| conselheiro | C - Conselheiro |
| estagiario | T - Estagiário |
| estatutario | E - Estatutário |
| folhaconfidencial | D - Diretor |
| horista | N - Normal e **Tipo de Recebimento H** |
| intermitente | N - Normal e **Categoria 106** |
| menoraprendiz | Z - Aprendiz |
| pensaovitalicia | S - Pensionista ou  W - Beneficiário |
| rda | Não tem mapeamento no RM |
| temporario | P - Temporário ou  B - Temporário ou  F - Temporário/Comissionista |
| terceirizado | Não tem mapeamento no RM |

### **2 - AFASTAMENTOS**

| DESCRIÇÃO AHGORA | CAMPO DA TABELA RM | DESCRIÇÃO | REGRA |
| --- | --- | --- |
| Identificação do colaborador | PFHSTAFT.CHAPA PFUFERIASPER.CHAPA | Coligada + Chapa (As matrículas serão enviadas sem caracteres especiais) Matricula do Funcionário. Busca da tabela de Afastamento e de Férias. |
| Motivo do Afastamento | PFHSTAFT.TIPO ou F quando for férias | Coligada + Tipo de Afastamento.  Quando for férias enviar F Terá um cadastro prévio na AHGORA igual do RM. |
| Data e/ou hora Inicial do Afastamento | PFHSTAFT.DTINICIO PFUFERIASPER.DATAINICIO | Data inicio do afastamento ou do gozo das férias.  Informar a hora 00:00. **YYYY-MM-DDTHH:MM** |
| Data e/ou hora Final do Afastamento | PFHSTAFT.DTFINAL PFUFERIASPER.DATAFIM | Data inicio do afastamento ou do gozo das férias. **YYYY-MM-DDTHH:MM** Informar 24:00 quando for o dia integral. Caso não tenha data fim, deverá enviar vazio. A Ahgora irá preencher com da fim 31/12/2050, quando chegar vazio. |
| Código interno do Afastamento | CHAVE | Informar a chave única para definir se a operação será de inclusão ou alteração. Verificar se a chave pode ser composta por **Coligada + Chapa + Data de Início**.  **Tratativa na Ahgora:** Se a chave já existir, o sistema substitui; caso contrário, realiza a inclusão. |

### **3 - RESULTADO**

| CAMPO DA TABELA RM | DESCRISÇÃO NA AHGORA | DESCRIÇÃO | REGRA |
| --- | --- | --- |
| PFMOVTEMP.CHAPA | matricula | Pode ser alfanumérica Campo matrícula(As matrículas serão enviadas sem caracteres especiais) |
| PFMOVTEMP.ANOCOMP | anocom | Padrão AAAA |
| PFMOVTEMP.MESCOMP | mescom | Padrão MM Exemplo: Janeiro enviar 01 |
| - | campoAdicional | Informação do campo adicional no PW Não é obrigatório |
| PFMOVTEMP.;CODEVENTO | rubrica | Será cadastrado no PW igual o sistema de destino |
| PFMOVTEMP.HORA PFMOVTEMP.REF | Horas ou Referencia | Poderá enviar em horas ou dias, dependente da configuração do evento no RM.  **Exemplo:**   * + **Dias:** 3 dias => enviar 3. Número inteiro.   + **Horas:**  1h30min => enviar 1,30. As horas são**sexagesimal (separador ",")**   **ATENÇÃO:** Ao salvar a hora neste campo, o sistema realiza a conversão automática de horas para minutos.  **Exemplo:** Caso o Ponto Web Ahgora envie **1,04 horas**, ao gravar na tabela **PFMOVTEMP.HORA**, o sistema fará o seguinte cálculo de conversão:   * + - 1 hora = 60 minutos     - 0,04 horas = 4 minutos     - Total: **64 minutos**     Esse valor (64) será salvo no campo **PFMOVTEMP.HORA**. No entanto, na visualização do menu Folha Mensal | Consulta | Consulta Movimento da Integração, continuará aparecendo como **1,04**, pois o sistema converte os minutos de volta para o formato hora.decimal apenas para exibição. |

### **4 - LISTAGEM DE EVENTOS/VERBAS**

| CAMPO DA TABELA RM | DESCRISÇÃO NA AHGORA | DESCRIÇÃO | REGRA |
| --- | --- | --- |
| PEVENTO.CODIGO | Código da rubrica | Campo alfanumérico. |
| PEVENTO.DESCRICAO | Descrição da rubrica | Descrição do evento. |
| GCOLIGADA.CGC | CNPJ da empresa | CNPJ da coligada. |
| PEVENTO.PROVDESCBASE | Categoria da rubrica | Provento/Desconto - Utilizado para compor campo 'categoria' da api 'api/rh/v1/ahgora/verbas'; PEVENTO.PROVDESCBASE + **'-'** + PEVENTO.VALHORDIAREF).  **Exemplo:** 'Provendo-Valor'. |
| PEVENTO.VALHORDIAREF | Categoria da rubrica | Valor/Hora/Dia/Referência - Utilizado para compor campo 'categoria' da api 'api/rh/v1/ahgora/verbas'; PEVENTO.PROVDESCBASE + **'-'** + PEVENTO.VALHORDIAREF).  **Exemplo:** 'Provendo-Valor'. |

### **5 - LISTAGEM DE SINDICATOS**

| CAMPO DA TABELA RM | DESCRISÇÃO NA AHGORA | DESCRIÇÃO | REGRA |
| --- | --- | --- |
| PSINDIC.CODIGO | Código do sindicato | Campo alfanumérico |
| PSINDIC.NOME | Descrição do sindicato | Nome do sindicato |
| GCOLIGADA.CGC | CNPJ da empresa | CNPJ da coligada |

4VideosVideos

**Vídeos RM**

|  |  |
| --- | --- |
| How To | Linha RM integração com a Ahgora Parte 1 #TOTVS\_RH\_Linha\_RM - Parametrizações | <https://youtu.be/4DIaY1flp50> |
| How To | Linha RM integração com a Ahgora Parte 2 #TOTVS\_RH\_Linha\_RM - Integração Folha X Ponto Web | <https://youtu.be/h9i8oQWtARE> |
| How To | Linha RM integração com a Ahgora Parte 3 #TOTVS\_RH\_Linha\_RM - Exclusão dos Envios | <https://youtu.be/HFS_U7A4gho> |
| How To | Linha RM integração com a Ahgora Parte 4 #TOTVS\_RH\_Linha\_RM - Agendamento Job | <https://youtu.be/XahxvJGw-vo> |
| How To | Linha RM integração com a Ahgora Parte 5 #TOTVS\_RH\_Linha\_RM - Apuração de Resultados | <https://youtu.be/RCYPyp3MWtc> |
| How To | Linha RM integração com a Ahgora Parte 6 #TOTVS\_RH\_Linha\_RM - Campo Localizações | <https://youtu.be/K7_k1CNMJ7k> |

**Vídeos Ahgora - Ponto Web**

|  |  |
| --- | --- |
| How To | PW - Ponto Web Ahgora integração com Linha RM Parte 1 #TOTVS\_RH\_Linha\_RM - Cadastros de Códigos Internos das Escalas | <https://youtu.be/QhUh7WPoZI4> |
| How To | PW - Ponto Web Ahgora integração com Linha RM Parte 2 #TOTVS\_RH\_Linha\_RM - Cadastros de Códigos dos Centros de Custos | <https://youtu.be/8gEbO6oYM4M> |
| How To | PW - Ponto Web Ahgora integração com Linha RM Parte 6 #TOTVS\_RH\_Linha\_RM - Cadastros de Códigos Internos dos Motivos de Afastamentos | <https://youtu.be/pv15MK8ZLGA> |
| How To | PW - Ponto Web Ahgora integração com Linha RM Parte 7 #TOTVS\_RH\_Linha\_RM - Cadastros de Códigos Contábeis das Horas Adicionais dos Sindicatos | <https://youtu.be/sRQXBuo0uGs> |
