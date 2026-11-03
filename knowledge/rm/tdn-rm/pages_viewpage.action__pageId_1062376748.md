---
content_hash: 3b9e40309f7fc62507a880d9b4f604f7863a1b3eed836d56d31ca1c91a0559d7
fetched_at: '2026-06-29T00:05:52.958694+00:00'
page_id: '1062376748'
product: rm
source: tdn-rm
title: Shopping - Boleto - Negociação de Boleto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1062376748
version: 27
---

---

# Introdução

A **Negociação de Boleto** é o processo utilizado para regularizar débitos em atraso ou facilitar o pagamento de títulos de um cliente. Em termos simples, ela permite que você pegue um boleto vencido (ou a vencer) e estabeleça novas condições de pagamento.

---

# Configurações Iniciais

## 1) Permissões

Antes de iniciar o processo de negociação de boletos, é necessário dar permissões aos usuários. Verifique os parâmetros de perfil abaixo em Serviços Globais / Segurança / Perfil:

* **[04.02.02]** Boleto
  + **[04.02.02.01]** Negociar boleto
* **[04.02.03]** Negociação de boletos
  + **[04.02.03.01]** Parâmetros de valores de integração

    - **[04.02.03.01.01]** Visualizar
    - **[04.02.03.01.02]** Inserir
    - **[04.02.03.01.03]** Excluir
    - **[04.02.03.01.04]** Editar
  + **[04.02.03.02]** Visualizar
  + **[04.02.03.03]** Inserir
  + **[04.02.03.04]** Excluir
  + **[04.02.03.05]** Editar
  + **[04.02.03.06]** Lançamentos do boleto negociado
  + **[04.02.03.07]** Lançamentos gerados pela negociação de boletos
  + **[04.02.03.08]** Efetivar
  + **[04.02.03.09]** Atualizar saldo
  + **[04.02.03.10]** Concluir
  + **[04.02.03.11]** Cancelar
  + **[04.02.03.12]** Negociar saldo restante

---

## 2) Cadastro de Parâmetros de Valores de Integração

Esta funcionalidade é pré-requisito e necessária para a efetivação da negociação. Ela permite parametrizar quais valores de integração serão utilizados para **Juros**, **Multa** e **Baixa** na Negociação de Boletos, associando estes valores aos novos lançamentos gerados.

O diferencial desta tela é o conceito **Multi-Coligada**. Você não precisa trocar o contexto da coligada no sistema para realizar o cadastro; é possível gerenciar os parâmetros de diferentes unidades em uma única visualização.

**Campos do Cadastro:**

* **Coligada: Selecione a coligada para a qual deseja definir os parâmetros.**
* **Vlr. Integração Juros: Código/Identificador do valor de integração destinado aos juros.**
* **Vlr. Integração Multa: Código/Identificador do valor de integração destinado à multa.**
* **Vlr. Integração Baixa: Código/Identificador do valor de integração destinado à baixa principal.**

**Regras de Negócio e Restrições**

Para garantir a integridade dos dados contábeis e financeiros, o sistema aplica as seguintes validações automáticas:

* **Unicidade por Coligada:** Só é permitido cadastrar **um único registro** para cada combinação de Coligada. Se tentar inserir um segundo registro para a mesma coligada o sistema bloqueará a operação.

Passo a Passo para Inclusão

1. Acesse o menu ***Shopping / Negociação de Boletos /** **Parâmetros de Valores de Integração**.*
2. Clique em **Novo**.
3. Selecione a **Coligada** desejada (independente de qual coligada você esteja logado no momento).
4. Preencha os campos de **Valores de Integração** (Juros, Multa e Baixa).
5. Clique em **Salvar**.

---

# Procedimentos para Utilização

## Como Consultar e Renegociar Boletos no Sistema

Acesse e gerencie suas pendências financeiras para regularizar débitos de forma centralizada.

**Passo a Passo**

1. Acesse o menu **Shopping > Negociação de Boletos**.
2. Clique no botão Inserir.
   1. Lembrando que a opção de **Negociação de Boletos** também está disponível no menu *Shopping > Boletos*, selecionando o boleto desejado e indo em *Processos / Renegociar Boleto*. Caso feito desta forma, o boleto em questão já vira selecionado com seus valores atualizados na data corrente (Valor Líquido)
3. Utilize os filtros de busca de boleto, na tela inicial da Negociação para localizar o título desejado ou trocar, caso necessário.

   > A tela exibe apenas títulos com o status **Em aberto**.
4. Confira as informações exibidas na tela:

   * **Descrição:** Pode ser alterada pelo usuário;
   * **Boleto:** Será carregado com o **boleto** selecionado na tela de renegociação. Entretanto o usuário poderá alterá-lo através do botão "...";
   * **Valor:** O valor do boleto e seus encargos (juros / multa) na data da renegociação;
   * **Número documento:** Campo informativo com o número do documento original do boleto
   * **Emissão:** Campo informativo exibindo a data da emissão do boleto selecionado.
   * **Vencimento:** Campo informativo com o vencimento do boleto selecionado.
   * **Data da Renegociação:** O usuário poderá alterar a data da renegociação neste campo. Entretanto, a data não poderá ser anterior ao vencimento do boleto.
5. Verifique o valor líquido calculado. O sistema considera encargos e juros automaticamente até a data de renegociação selecionada.
6. Após definida a parametrização inicial, clique em configurar para definir os novos valores, parcelas, etc.
7. Os detalhes da aba de Configuração são os abaixo:
   * **Valor dos Boletos:** O valor atualizado do boleto selecionado na data da negociação. (Valor Líquido)
   * **Quantos Boletos:** A Quantidade de Boletos. O valor sempre será proporcionalizado entre a quantidade definida de boletos.
   * **Primeiro Vencimento:** Quando ocorrerá o primeiro vencimento. Por padrão é preenchido com a data da negociação, mas este campo pode ser alterado.
   * **Intervalo em Dias:** O intervalo de dias após o primeiro vencimento que os vencimentos das parcelas subsequentes serão gerados.
   * **Juros**
     + **Taxa Desconto** **%:** Caso necessite aplicar uma taxa de desconto em cima do montante do juros do boleto, defina neste campo.
     + **Valor Desconto** **R$:** Caso necessite aplicar um valor de desconto em cima do montante do juros do boleto, defina neste campo.
   * **Multa**
     + **Taxa Desconto** **%** Idem ao acima, mas para Multa.
     + **Valor Desconto R$** Idem ao acima, mas para Multa.
   * **Gerar**: Ao clicar em gerar o sistema irá proporcionalizar o valor do boleto, dos juros e multa entre as parcelas (Campo Quantos Boletos).
8. Estando a configuração satisfatória o próximo passo é a efetivação.

**Importante:**

O sistema também permite a edição de uma ou mais parcelas, Para isso basta clicar no botão "Editar". O Botão "Restaurar" Volta a configuração padrão da negociação.

O sistema carrega automaticamente todos os lançamentos vinculados ao boleto (como locação, condomínio e fundo de promoção), mesmo que pertençam a coligadas diferentes.

**Solução de Problemas:**

**Por que não consigo desmarcar um lançamento na renegociação?** A seleção de lançamentos é bloqueada por padrão. A renegociação deve abranger obrigatoriamente todos os itens que compõem o boleto selecionado.

**O boleto que procuro não aparece na lista.** Certifique-se de que o título possui o status **Em aberto**. Boletos já quitados ou cancelados não ficam disponíveis nesta tela de consulta.

---

## Como Efetivar a Negociação de Boletos

A efetivação da negociação garante a substituição automática do boleto vencido ou a vencer por novas condições acordadas, gerando novos boletos baseados nos parâmetros da negociação vigente.

Pré-requisitos

* Parâmetros de Valores de Integração: Ao efetivar uma negociação de boleto o sistema irá utilizar o parâmetro cadastrado neste menu para definir os valores de integração de Multa, Juros e Baixa para os lançamentos originados na confissão. Não será possível a efetivação se estes parâmetros não estiverem definidos. Eles devem ser únicos e por cada coligada participante da negociação. Realize este cadastro em *Shopping / Negociação de Boletos / Parâmetros de Valores de Integração.*

Estando o pré-requisito atendido e a negociação parametrizada como vimos acima, basta selecionar o registro e ir em Processos / Efetivar

A efetivação irá ocorrer e afetará os boletos originais e lançamentos da seguinte forma:

### 1. Cancelamento do Boleto Original

Ao iniciar a efetivação, o sistema realiza a limpeza das obrigações anteriores:

* O sistema cancela a remessa de origem do boleto (caso ela já tenha sido gerada).
* O sistema altera o status do **Boleto Original** para **Cancelado**.

### 2. Bloqueio dos Lançamentos Originais

Para preservar a rastreabilidade, os lançamentos que deram origem à negociação são preservados, mas bloqueados:

* **Restrições do Bloqueio:** Lançamentos com este status não permitem baixa, cancelamento, geração de novos boletos avulsos, inclusão em confissões de dívida ou novos acordos financeiros.

### 3. Geração dos Novos Lançamentos

O sistema gera a nova estrutura financeira baseada nos critérios abaixo:

* **Proporcionalidade:** O sistema cria um novo lançamento para cada item de origem, multiplicado pela quantidade de parcelas da negociação. O valor é rateado proporcionalmente.
* **Encargos:** Proporcionaliza os valores de **Juros** e **Multa** dos lançamentos e insere nos novos lançamentos de acordo com os campos de **Integração** específicos, configurado nos parâmetros.
* **Dados Cadastrais:** O sistema replica **Filial**, **Tipo de Documento**, **Histórico**, **Centro de Custo** e **Natureza Financeira** do lançamento original.

### 4. Geração dos Novos Boletos

Após gerar os lançamentos, o sistema cria os boletos:

* Acesse os novos boletos gerados na mesma **Coligada**, **Convênio** e **Conta/Caixa** do título anterior, estarão disponíveis em S*hopping > Boletos*
* Os boletos nascem com o status **Não Remetido**.

### 5. Finalização e Consulta

* O sistema altera o status da negociação para **Efetivada**.
* Para conferir o histórico, utilize a aba **Anexos** para visualizar quais lançamentos originaram a renegociação e quais foram gerados por ela pelos anexos:

  + Lançamentos do boleto negociado
  + Lançamentos gerados pela negociação de boletos

### Solução de Problemas

**O sistema não permite cancelar o novo boleto na tela de boletos?** Isso ocorre para garantir a integridade financeira. Para cancelar boletos de renegociação, você deve obrigatoriamente utilizar o processo **Cancelar Negociação**. Isso garantirá que os novos lançamentos também sejam estornados e o bloqueio dos originais seja removido automaticamente.

---

## Baixa e Atualização de Saldo Baixado

O **Processo de Atualização de Saldo** da negociação tem como objetivo atualizar os valores dos lançamentos financeiros originais vinculados a uma **negociação de boleto**, considerando as baixas realizadas através das baixas dos novos boletos gerados.

Quando uma baixa é identificada em um lançamento gerado pela negociação, o processo registra esse valor como **desconto por meio de valor de integração** (Valor de Integração para Baixa no parâmetro financeiro) no lançamento original negociado.

* Este processo pode também ser agendado, ocorrendo automaticamente conforme configuração.

#### Quando utilizar

Este processo deve ser utilizado quando houver:

* **Baixa de lançamentos financeiros gerados por negociação de boleto.**
* Necessidade de **refletir corretamente o saldo líquido dos lançamentos originais do boleto negociado.**
* Necessidade de **atualizar automaticamente o saldo do valor de integração relacionado às baixas dos boletos negociados.**

Esse processo ajuda a manter os valores do **contas a receber atualizados e consistentes** com as negociações realizadas.

#### Pré-requisitos

Antes de executar o processo, é necessário:

1. Existirem **negociações de boleto geradas**.
2. Os lançamentos gerados pela negociação possuírem **baixa registrada**.
3. A negociação que será processada deve ser **selecionada no momento da execução do processo**.

#### Passo a passo para execução

##### Executar o processo manualmente ou por agendamento

1. Selecione a negociação **que deseja processar**.
2. Acesse o menu de **Processos;**
3. Localize o processo **Atualizar Saldo**.
4. Execute o processo.
5. Aguarde a conclusão do processamento.

#### Funcionamento interno do processo

Durante a execução, o sistema realiza as seguintes etapas:

1. Localiza as **baixas dos lançamentos financeiros gerados pela negociação.**
2. Identifica os **lançamentos originais que participaram da negociação**.
3. Registra o valor da baixa como **desconto via valor de integração** no lançamento original.

#### Resultado esperado

Após a execução do processo:

* Os lançamentos originais terão o **valor de integração atualizado** com base nas baixas realizadas.
* O **valor líquido do lançamento** será recalculado considerando o desconto do valor de integração atualizado.
* O sistema refletirá corretamente o **valor atual da negociação**.

Cancelamento de baixa

Quando uma baixa é cancelada em um lançamento gerado pela negociação, o processo de **Atualizar Saldo** deve remover o registro do valor de integração descontado pela baixa que fora cancelada.

---

## Concluir Negociação de Boleto

A conclusão da negociação é a etapa final do ciclo de vida de uma negociação. Ela formaliza que o cliente cumpriu com todas as obrigações pactuadas, encerrando o processo de cobrança e atualizando o histórico financeiro.

### Quando concluir uma negociação?

O sistema permite o encerramento da negociação apenas quando o ciclo financeiro estiver 100% completo. Os pré-requisitos fundamentais são:

1. **Quitação Integral:** Todos os boletos gerados na negociação e seus lançamentos devem estar com o status **"Baixado"**.
2. **Saldo Zerado:** Não pode haver qualquer valor remanescente ou pendência de renegociação.

### O que acontece após a conclusão?

Ao executar o processo de conclusão de negociação, o sistema executa automaticamente uma série de rotinas para garantir a integridade dos dados:

#### 1. Atualização dos Lançamentos Originais

Os títulos antigos (aqueles que deram origem à dívida negociada) terão seu status alterado para **"Baixado por Acordo"**.

> **Nota:** Essa alteração é irreversível e serve para indicar que a dívida original foi substituída e devidamente quitada através da negociação de boleto.

#### 2. Bloqueio da Negociação

Uma vez com o status **"Concluída"**, a negociação entra em modo somente leitura:

* **Consulta apenas:** O registro fica disponível apenas para fins de auditoria e histórico.
* **Sem Alterações:** Não é permitido editar valores, datas ou condições.
* **Sem Emissões:** O sistema bloqueia a geração de novos boletos para este acordo.
* **Sem Cancelamento:** Um acordo concluído não pode ser cancelado, pois os valores já foram integrados ao caixa.

---

## Cancelamento de Negociação de Boleto

O cancelamento de uma negociação é o processo de "desfazer" um acordo financeiro. Ele é utilizado quando o cliente não cumpre o pactuado e você precisa que as dívidas originais voltem a ficar disponíveis para cobrança ou para uma nova renegociação.

### Quando utilizar o cancelamento?

Este recurso deve ser acionado quando:

* O cliente **desistiu do acordo** ou está inadimplente com as parcelas da negociação.
* Ainda existirem **boletos em aberto** ou saldo pendente no acordo.
* Você precisar liberar os títulos originais (Locação, Condomínio, etc.) para outros processos.

### O que o sistema faz automaticamente?

Ao confirmar o cancelamento, o sistema executa uma "limpeza" automática para garantir que não fiquem pendências residuais:

#### 1. Limpeza de Boletos e Novos Lançamentos

* Todos os boletos gerados pela negociação que ainda estiverem em aberto são **cancelados e excluídos**.
* As remessas bancárias desses boletos são canceladas para evitar protestos indevidos.
* Os lançamentos financeiros criados especificamente para este acordo são removidos.

#### 2. Recuperação dos Títulos Originais (Liberação)

Os lançamentos que foram "bloqueados" pela negociação de boletos estarão disponíveis novamente no sistema:

* **Status "Livre":** Os lançamentos que ainda possuem dívida voltam ao status "Livre", permitindo que você gere novos boletos, receba pagamentos ou faça um novo acordo.
* **Status "Baixado por Acordo":** Se o cliente chegou a pagar parte da negociação e esse valor foi suficiente para quitar algum dos lançamentos originais, este lançamento específico será marcado como baixado definitivamente.

> **Importante:** Ao liberar os lançamentos originais, o sistema desconsidera juros e multas que teriam corrido *durante* o período em que o acordo estava ativo, preservando o valor conforme estava no momento da negociação.

#### 3. Finalização do Processo

* O status da negociação é alterado para **"Cancelada"**.
* O registro permanece no sistema apenas para histórico e auditoria, não sendo possível reativá-lo.

### Regras de Integridade e Segurança

Para sua segurança e conformidade financeira, o sistema valida os seguintes pontos durante o cancelamento:

* **Bloqueio de Boletos Órfãos:** O sistema garante que nenhum boleto da negociação continue válido após o cancelamento do acordo.
* **Consistência de Saldo:** O cálculo de retorno dos títulos originais é feito de forma automática, garantindo que o saldo devedor atual seja exatamente o que restou após eventuais pagamentos parciais feitos durante o acordo.
* **Rastreabilidade:** Todas as ações de cancelamento ficam registradas no log do sistema, informando qual usuário realizou a operação e em qual data.

---

## Negociar Saldo Restante

Esta funcionalidade permite dar continuidade à negociação de um boleto quando a negociação anterior não contemplou o saldo total do título. Por meio deste processo, é possível realizar uma nova negociação sobre o saldo remanescente, desde que ainda exista valor disponível para negociação.

### Como Realizar

#### Passo 1: Selecionar a Negociação

1. Ao selecionar a negociação de boleto desejada, acesse a opção Processo → Negociar Saldo Restante.  
   Ao abrir a tela de negociação, o sistema apresentará o valor do saldo pendente atualizado e corrigido até a data atual da negociação.  
   O campo de valor exibirá o saldo disponível para negociação e a quantidade de boletos será preenchida automaticamente com o valor 1.  
   Caso necessário, o usuário poderá alterar o valor de cada boleto e informar uma quantidade diferente de novos boletos para realizar a negociação do saldo remanescente.

#### Passo 2: Definição das Parcelas da Negociação

No painel de negociação, o usuário deverá preencher as novas diretrizes de pagamento:

* **Quantidade de boletos:** Informe o número de parcelas em que o saldo será dividido.
* **1º Vencimento dos boletos:** Selecione a data de vencimento da primeira parcela.
* **Intervalo em dias entre os vencimentos:** Defina o padrão de dias entre uma parcela e outra (ex: 30 dias).
* **Desconto de Juros:** Se aplicável, informe o percentual (%) ou o valor em reais (R$) de abatimento sobre os juros originais.
* **Desconto de Multa:** Se aplicável, informe o percentual (%) ou o valor em reais (R$) de abatimento sobre a multa original.

#### Passo 3: Simulação e Ajustes

1. Após preencher os campos de configuração, clique no botão **Gerar**.
2. O sistema exibirá logo abaixo uma grade contendo o detalhamento de cada parcela simulada (Vencimento e Valor).
3. Confira na barra de valores o **Valor total dos boletos a serem gerados** antes de prosseguir.
4. Em seguida ao clicar em executar ,o sistema processará o saldo restante e o integrará à negociação original. As novas parcelas geradas serão adicionadas ao histórico da negociação existente, consolidando o saldo atualizado e o novo plano de parcelamento.  
     
   Para facilitar o entendimento, imagine o seguinte cenário:  
     
   * Situação inicial: Você tem uma dívida total de R$ 10.000,00 e já fez uma negociação para pagar em 2 parcelas.
   * Nova negociação: Você decide negociar um saldo restante de R$ 1.000,00.
   * O que o sistema faz: O sistema adiciona esse novo valor a negociação original que você já tinha.
   * Resultado: As suas 2 parcelas iniciais agora passam a ser 3 parcelas, englobando o novo valor negociado.Basicamente, o sistema mantém o histórico da negociação original e vai "anexando" as novas parcelas conforme você negocia os saldos restantes, somando tudo dentro do mesmo registro.

---

## Renegociação de Boletos Cancelados

Esta funcionalidade permite **renegociar dívidas de boletos que foram cancelados**, mas com uma regra importante de segurança: o sistema só aceita o boleto cancelado que **deu origem** a uma negociação anterior (que também acabou sendo cancelado). Ela não permitirá a seleção do boleto que foi gerado *pela* negociação, evitando duplicidade.

Na prática, o sistema recupera o saldo real que o cliente ainda deve, desconta o que ele já pagou em negociações passadas e permite criar uma nova negociação em cima apenas do valor restante.

**Resumo das Regras:**

* **O que é permitido:** Selecionar boletos cancelados que foram a origem de uma negociação cancelada por falta de cumprimento da negociação.
* **O que não é permitido:** Selecionar boletos cancelados que foram *gerados por* uma negociação.
* **Base de cálculo:** O valor da nova negociação é calculado pelo **saldo atual em aberto** dos lançamentos financeiros originais, e não pelo valor de face do boleto.
* **Abatimento automático:** Se o cliente pagou alguma parcela na negociação anterior antes de ela ser cancelada, esse valor é descontado e apenas o saldo restante fica disponível para a nova negociação.

---

## Número do documento na Geração de lançamentos na negociação de boletos

Toda vez que uma nova negociação for efetivada, serão gerados novos lançamentos financeiros (e boletos). Para que a equipe financeira consiga rastrear facilmente de onde veio aquela nova cobrança, o sistema gera o **"Número do documento"** combinando as informações da dívida original.

Para evitar erros de duplicidade ao refazer a negociação, o sistema foi atualizado: a regra de criação desse número agora junta quatro informações, incluindo o número da negociação atual:

> **Código da Dívida Original (IDLAN)** `+` **Sequência do Boleto** `+` **Número da Parcela** `+` **Número da Negociação**

*Além disso, se uma negociação for cancelada, o sistema realiza uma limpeza automática: todos os lançamentos em aberto que haviam sido gerados por aquela negociação específica são cancelados e excluídos permanentemente da base de dados. Isso garante que os números fiquem livres caso o usuário queira tentar uma nova renegociação.*

**Exemplo na Prática**

Imagine que o cliente tem duas dívidas originais no sistema: o boleto **44700** e o boleto **44701**. Ele decide renegociar essas duas dívidas juntas, parcelando o valor total em **3 vezes** (ou seja, serão gerados 3 novos boletos). Essa nova operação gerou a **Negociação nº 500.**

O sistema criará os novos lançamentos numerando o campo "Número do documento" da seguinte forma, atrelando o número do acordo no final:

* **Para a 1ª Parcela (Novo boleto 1):**

  + Vinculado ao boleto original 44700 -> Número gerado: **44700-1/1-500**
  + Vinculado ao boleto original 44701 -> Número gerado: **44701-1/2-500**
* **Para a 2ª Parcela (Novo boleto 2):**

  + Vinculado ao boleto original 44700 -> Número gerado: **44700-2/1-500**
  + Vinculado ao boleto original 44701 -> Número gerado: **44701-2/2-500**
* **Para a 3ª Parcela (Novo boleto 3):**

  + Vinculado ao boleto original 44700 -> Número gerado: **44700-3/1-500**
  + Vinculado ao boleto original 44701 -> Número gerado: **44701-3/2-500**

*Se o usuário entrar no sistema e clicar em "Cancelar" nesta Negociação 500, todos esses lançamentos gerados acima (que ainda estiverem com o saldo em aberto) serão cancelados e deletados do banco de dados imediatamente.*
