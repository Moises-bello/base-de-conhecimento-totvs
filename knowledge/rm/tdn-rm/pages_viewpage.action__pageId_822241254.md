---
content_hash: 79f2ec71c39c4512073c93d2c5fc0a74214b78afe2d64b09687818651b3562a7
fetched_at: '2026-06-29T00:11:46.024947+00:00'
page_id: '822241254'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Shopping - Confissão de Dívida
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822241254
version: 148
---

## Introdução

📌 **Confissão de Dívida** é uma funcionalidade que permite ao devedor reconhecer formalmente um débito junto ao credor, estabelecendo condições negociadas para pagamento.

🔐 Para utilizar essa funcionalidade, é necessário conceder acesso ao menu: **Shopping > Confissão de Dívida**, no perfil dos usuários responsáveis pelo processo.

3

---

## Cadastrando uma nova Confissão de Dívida

---

### Etapa 1: Renegociação

Ao clicar em **Novo**, será exibida a tela inicial para criação da confissão de dívida, permitindo a inclusão do contrato a ser renegociado, na aba **Renegociação**.

* 📝 **Descrição**: Informe o nome da confissão de dívida.
* 📅 **Data da confissão**: Data de início da confissão (editável enquanto estiver em *Preparação*).
* 🔄 **Situação**: Indica o status atual da renegociação.
* 🔎 **Buscar por Contrato**: Permite localizar o contrato informando coligada e contrato de locação.
* 👤 **Buscar por Locatário**: Pesquisa pelo cliente, independentemente dos contratos associados.
* ⬇️ **Carregar**: Carrega todos os lançamentos financeiros negociáveis (em aberto).
* 💰 **Lançamentos Financeiros**: Seleção das parcelas que farão parte da renegociação.
* 📊 **Totalizadores**:

  + Total da dívida (valor líquido atualizado)
  + Total da renegociação (somente parcelas selecionadas)

**ℹ️ Importante:**O sistema permite a atualização do valor líquido dos lançamentos de confissão de dívida. Para realizar esta alteração, basta editar a data de confissão informando uma nova data. Ao carregar a confissão de dívida, durante sua edição ou ao salvá-la com a data da confissão alterada, o sistema realizará automaticamente o cálculo e atualizará o valor líquido na tela. É importante observar que a alteração da data da confissão só é possível em confissões com status em preparação.

### Etapa 2: Configurações

Nesta etapa, na aba **Configurações**, o usuário define **descontos, acréscimos, forma de pagamento e regras de parcelamento**, garantindo flexibilidade na renegociação.

#### 📄 Template de Confissão de Dívida

Permite selecionar um template previamente cadastrado, preenchendo automaticamente os campos padrão.

🔗 **Para mais informações, acesse:** [TOTVS Construção Gestão de Imóveis - Shopping - Template de Confissão de Dívida](https://tdn.totvs.com/pages/viewpage.action?pageId=825295895)

#### ➖ Desconto

* **Taxa (%)**: Percentual aplicado sobre todas as entidades.
* **Valor**: Valor fixo rateado entre as entidades participantes.

#### ➕ Acréscimo

* **Taxa (%)**: Percentual aplicado sobre todas as entidades.
* **Valor**: Valor fixo rateado proporcionalmente.

#### 💳 Forma de pagamento

* **Linear**: Distribui o valor igualmente entre todas as entidades.
* **Prioridade**: Define a ordem de pagamento das entidades:

  + Locação
  + Fundo Promocional
  + Condomínio

ℹ️ O sistema respeita a prioridade definida até atingir o valor confessado.

**ℹ️ Importante:**Quando o cálculo é por prioridade, o sistema tentará ao máximo obedecer a quantidade de parcelas selecionadas. Entretanto, devido a prioridade e diferentes origens numa mesma competência, pode ocorrer da confissão gerar um plano de pagamento com um número maior de parcelas, justamente por termos selecionado uma prioridade maior a determinada origem.

#### **📈** Usar juros futuros

* Define que as novas parcelas terão incidência de juros e multa sobre o tempo. Todo o valor líquido calculado na data da confissão será distribuído para compor as parcelas geradas.

#### **🗓️** Multa e juros na última parcela

* As parcelas intermediárias são calculadas apenas sobre o valor original da dívida. Todo o montante acumulado de juros e multas da negociação será concentrado exclusivamente no **último vencimento**.

#### **⚪** Sem multa e juros

* Isenta as parcelas geradas de qualquer encargo extra. A nova dívida é calculada estritamente sobre o **valor original** dos lançamentos financeiros selecionados.

#### **⚠️** Última parcela condicional

* Permite especificar uma condição de pagamento diferenciada apenas para o encerramento da dívida. *Nota: Esta opção só fica disponível quando a regra de "Multa e juros na última parcela" estiver ativa.*

🧮 Exemplo de aplicação de valor e taxa

**⚙️ Configuração definida**

* 📈 Acréscimo percentual: **10%**
* 💰 Acréscimo em valor: **R$ 300,00**

**🏷️ Entidades participantes da renegociação**

* 🏠 Locação
* 🎯 Fundo Promocional
* 🏢 Condomínio

---



**📊 Resultado da aplicação**

* ➕ Aplicação de **10%** de acréscimo nas parcelas de:
  + Locação
  + Fundo Promocional
  + Condomínio
* 💵 Distribuição do valor fixo de **R$ 300,00**:
  + R$ 100,00 acrescido às parcelas de **Locação**
  + R$ 100,00 acrescido às parcelas de **Fundo Promocional**
  + R$ 100,00 acrescido às parcelas de **Condomínio**

---



ℹ️ **Observação:**  
Esta lógica é aplicada tanto para **acréscimos** quanto para
**descontos**, respeitando sempre as entidades participantes da renegociação.

]]>

🔢 Exemplo de cálculo por prioridade

**📌 Regra de funcionamento**

No cálculo por prioridade, o sistema prioriza o pagamento da entidade definida
nas configurações.

Ao atingir o **valor confessado** de uma entidade e ainda existir saldo
para a mesma competência, é gerada automaticamente **uma nova parcela**
para a próxima entidade conforme a ordem de prioridade.

---

**📊 Exemplo prático de distribuição por prioridade**

| Prioridade | Locação | Condomínio | Fundo | Total |
| --- | --- | --- | --- | --- |
| 1 | R$ 7.500,00 | R$ 0,00 | R$ 0,00 | R$ 7.500,00 |
| 2 | R$ 7.500,00 | R$ 0,00 | R$ 0,00 | R$ 7.500,00 |
| 3 | R$ 7.500,00 | R$ 0,00 | R$ 0,00 | R$ 7.500,00 |
| 4 | R$ 2.500,00 | R$ 5.000,00 | R$ 0,00 | R$ 7.500,00 |
| 5 | R$ 0,00 | R$ 7.500,00 | R$ 0,00 | R$ 7.500,00 |
| 6 | R$ 0,00 | R$ 7.500,00 | R$ 0,00 | R$ 7.500,00 |
| 7 | R$ 0,00 | R$ 5.000,00 | R$ 2.500,00 | R$ 7.500,00 |
| 8 | R$ 0,00 | R$ 0,00 | R$ 7.500,00 | R$ 7.500,00 |
| 9 | R$ 0,00 | R$ 0,00 | R$ 7.500,00 | R$ 7.500,00 |
| 10 | R$ 0,00 | R$ 0,00 | R$ 7.500,00 | R$ 7.500,00 |
| Total | R$ 25.000,00 | R$ 25.000,00 | R$ 25.000,00 | R$ 75.000,00 |

---

ℹ️ **Observação:**  
O sistema respeita rigorosamente a ordem de prioridade definida.
Sempre que o valor máximo de uma entidade for atingido, o saldo remanescente
será automaticamente direcionado para a próxima prioridade dentro da mesma competência.

]]>

#### 📅 Vencimento

* **Qtd. vencimentos no mês:** Há a possibilidade de efetuar até quatro vencimentos num mesmo mês.
* **Competência inicial:** Competência da data da emissão da primeira parcela da confissão de dívida.
* **Dia vencimento:** Campo que permite a definição do dia de vencimento da parcela. Este campo irá respeitar a competência inicial.

#### 🧾 Parcelas

* **Quantidade:** Permite selecionar a quantidade de parcelas do plano de pagamento.
* **Percentual Primeira Parcela:** Define a porcentagem do valor total da dívida que será paga na primeira parcela.

#### **📈** Desconto sobre juros ou multa

A confissão também pode possuir descontos específicos no montante de juros ou no montante de multa, ou ambos, preenchendo os campos abaixo. Os descontos são sempre proporcionais aos lançamentos que fazem parte da confissão, independente de origem.

* **Desconto em Juros:** Campo para informar o valor (R$) ou percentual (%) que será reduzido exclusivamente dos juros acumulados.
* **Desconto em Multa:** Campo para informar o valor (R$) ou percentual (%) que será reduzido exclusivamente da multa acumulada.

### Etapa 3: Plano de Pagamento

O plano de pagamento será gerado de forma automática, refletindo os valores definidos na etapa de configuração.

É de suma importância realizar a conferência destes valores, bem como a distribuição entre as parcelas da renegociação.

O Plano de pagamento também poderá ser editado, através do botão **Editar**. Ao editar uma parcela o sistema irá proporcionalizar automaticamente os valores restantes para as parcelas da mesma entidade selecionada e que sejam da mesma coligada.

---

**A edição do plano de pagamento pode ser realizada de duas formas:**

* Ao alterar as configurações da confissão de dívida, o plano será refeito conforme as informações inseridas em configuração. Essa atualização se dará ao clicar em **"Salvar"**.
* Existe também a possibilidade de edição de uma parcela, ou várias parcelas específicas de uma confissão.

**Cenário exemplo:**

* Entidade Locação → 5 Parcelas de R$ 1.000,00
* Entidade Condomínio → 5 Parcelas de R$ 500,00
* Entidade Fundo Promocional → 5 Parcelas de R$ 1.500,00

Neste caso, será editada a primeira parcela de locação, adicionando o valor a maior de **R$ 500,00**, totalizando **R$ 1.500,00** para pagamento em determinada competência.

Para isso, é necessário selecionar a parcela e clicar no botão **"Editar"**.

Ao editar essa parcela, pode-se inserir um novo valor e também uma nova data de vencimento. Importante notar que esta data de vencimento altera também a competência da cobrança.

Ao editar e salvar essa parcela, o sistema realizará o rateio entre as parcelas da mesma entidade. O rateio será feito apenas entre as parcelas que possuem cálculo automático, ou seja, que não foram editadas manualmente.

Teremos então o seguinte cenário para as parcelas de locação:

✏️ Edição de Parcelas – Exemplo Prático

📄 Antes da edição

* Parcela Locação – Competência 03/24: **R$ 1.000,00** (Cálculo Automático)
* Parcela Locação – Competência 04/24: **R$ 1.000,00** (Cálculo Automático)
* Parcela Locação – Competência 05/24: **R$ 1.000,00** (Cálculo Automático)
* Parcela Locação – Competência 06/24: **R$ 1.000,00** (Cálculo Automático)
* Parcela Locação – Competência 07/24: **R$ 1.000,00** (Cálculo Automático)

---



✅ Após a edição

* Parcela Locação – Competência 03/24: **R$ 1.500,00** (Cálculo Manual)
* Parcela Locação – Competência 04/24: **R$ 875,00** (Cálculo Automático)
* Parcela Locação – Competência 05/24: **R$ 875,00** (Cálculo Automático)
* Parcela Locação – Competência 06/24: **R$ 875,00** (Cálculo Automático)
* Parcela Locação – Competência 07/24: **R$ 875,00** (Cálculo Automático)

---

ℹ️ O botão "Refazer Parcelas" irá voltar ao status inicial do plano de pagamento, ou seja, todas as parcelas com seus cálculos de forma automática, sobrescrevendo quaisquer ajustes manuais nas mesmas.

]]>

**ℹ️ Importante:  
Não será possível editar o plano de pagamento** quando a confissão de Dívida estiver com status " ✅ Efetivada"

### Etapa 4: Parâmetros financeiros

Após a edição e conferência dos valores através do plano de pagamento, deveremos inserir os parâmetros de integração financeira que irão compor a geração dos lançamentos.

Estes parâmetros devem existir em cada coligada que será gerada a dívida. Ou seja, se estou renegociando uma dívida pertencente a coligada 6, eu preciso, necessariamente, ter um parâmetro de integração financeira da coligada 6 associado ao cadastro dessa confissão.

⚠️ **Não será possível gerar lançamentos caso os parâmetros correspondentes as coligadas não estejam associados à confissão.**ℹ️ Informações sobre configuração de parâmetros financeiros acesse: **[Cadastros - Parâmetros de Integração Financeira para Aluguel](https://tdn.totvs.com/pages/viewpage.action?pageId=435105050)**

---

#### Incluindo um Parâmetro Financeiro na confissão

Esta tela é utilizada para configurar as regras que o sistema seguirá ao gerar os lançamentos financeiros da confissão.

* **Identificador:** Campo preenchido automaticamente pelo sistema com o código interno do registro de parâmetro.
* **Identificador da Confissão de Dívida:** Exibe o código numérico e a descrição da Confissão de Dívida à qual este parâmetro está vinculado (ex: `16 | CONF 001`).
* **Cód. Coligada:** Define a qual coligada este parâmetro financeiro se aplica. O usuário deve selecionar o código e a descrição da unidade de negócio correspondente.
* **Origem Parâmetro:** Permite segmentar a regra por tipo de receita, como **Locação, Condomínio, Fundo ou Outros**. Se selecionado "Todas as origens", o parâmetro funcionará como a regra geral (global) para a coligada.

  + **Múltiplas Configurações por Coligada:** O sistema agora permite cadastrar mais de um parâmetro de integração para a mesma coligada, desde que possuam origens diferentes.
  + **Regra de Aplicação (Efetivação da Confissão):** Ao efetivar uma Confissão de Dívida, o sistema identifica automaticamente a **Coligada** e a **Origem** dos lançamentos para aplicar as regras financeiras. A aplicação segue uma ordem de prioridade:
  + **Parâmetro Específico:** O sistema busca primeiro o parâmetro configurado exatamente para aquela **Origem** (ex: se o lançamento é de "Locação", ele busca o parâmetro de "Locação").
  + **Parâmetro Global (Default):** Caso não exista um parâmetro específico para aquela origem, o sistema utilizará o **Parâmetro Global/Geral** do contrato de locação como regra.

* **Parâmetro de Integração Financeira:** Campo para selecionar o modelo ou a regra de integração previamente cadastrada que define como os títulos serão gerados no módulo financeiro.

Nesta seção, definem-se os campos ou fórmulas que o sistema utilizará para compor os valores específicos de cada lançamento:

* **Valor de integração para juros:** Define qual campo ou regra de cálculo será utilizada para identificar o valor referente aos juros na integração financeira.
* **Valor de integração para multa:** Define qual campo ou regra de cálculo será utilizada para identificar o valor referente à multa na integração financeira.
* **Valor de integração para baixa:** Define o valor de integração utilizado no processo **“Cancelar Confissão de Dívida”**.  
  Esse parâmetro é responsável por registrar os valores pagos relacionados aos lançamentos confessados, representando e atualizando o valor da dívida nos lançamentos de origem. O valor de integração configurado deve possuir ação do tipo **“Desconta”**.  
  Durante o processo de cancelamento, o sistema identifica os valores pagos nos lançamentos gerados pela confissão e atualiza automaticamente o saldo da dívida, refletindo a situação atual de forma correta.
* **Valor de integração para acréscimo:** Define qual campo ou regra de cálculo será utilizada para identificar o valor referente aos acréscimos na integração financeira.
* **Valor de integração para desconto:** Define qual campo ou regra de cálculo será utilizada para identificar o valor referente aos descontos na integração financeira.

⚠️ Importante

* Os valores de integração devem sempre ser definidos dentro do parâmetro de integração financeira, quando o cálculo de juros e multa da confissão for realizado de forma separada. Dessa forma, os valores de integração não podem ser de ações diferentes;
* É importante ressaltar que não será possível cadastrar valores de integração idênticos para juros, multa, acréscimo ou desconto.
* Não será possível cadastrar o parâmetro sem os valores de integração associados, quando a opção de **"Separar o valor de Juros e Multas da Confissão (Valor de Integração)"** estiver habilitada.

### Etapa 5: Dados do Reajuste (Opcional)

Esta funcionalidade tem como objetivo facilitar o processo de reajustes financeiros nas confissões de dívidas.

As opções de reajuste disponíveis na confissão de dívida refletem as mesmas disponíveis no contrato de locação, garantindo consistência e conformidade com os acordos estabelecidos.

Possibilita o usuário escolher os tipos de reajuste, tais como **IPCA, IGPM, IGP-M acumulado**, entre outros. Isso proporciona adaptação às diferentes condições contratuais e às necessidades específicas de cada situação.

Além disso, em **Anexos / Valores de integração** é obrigatório inserir o valor de integração que será utilizado para compor os valores reajustados dos lançamentos. Esse cadastro deve ser feito por coligada.  
  
⚠️**Não será possível efetivar a confissão de divida quando houver dados do reajuste cadastrado e a mesma não possuir seus valores de integração respectivos.**

## Processos da Confissão de Dívida

---

### Efetivando a Confissão de Dívida

O processo de Efetivar confissão de dívida poderá ser acessado selecionando a confissão de dívida e abrindo o menu *Processos / Efetivar confissão de dívida.*

Ao concluir a efetivação, os lançamentos financeiros serão gerados em sua totalidade, ou seja, todas as parcelas serão geradas de acordo com as configurações do plano de pagamento.

A data de emissão dos lançamentos financeiros será igual a data da confissão de dívida para todas as parcelas geradas.

Os lançamentos de origem terão seu status de bloqueio igual a **"Bloqueado pela confissão de dívida"**.

Não é possível gerar somente uma parte dos lançamentos e também não será possível editar a confissão de dívida no status de **"Efetivada"**.

Para visualizar os lançamentos gerados, o usuário pode selecionar a confissão de dívida em questão e acessar o menu: **Anexos / Lançamentos Financeiros**.

### Alteração da Data de Vencimento

Esta opção permite aos usuários alterar a data de vencimento em lançamentos financeiros de confissão de dívida no sistema.

Antes de efetuar essa alteração, o sistema valida se não existem boletos gerados em aberto para o lançamento em questão e se não houve nenhuma baixa parcial. Isso garante a integridade das operações financeiras, assegurando que não haja inconsistências durante o processo de alteração de vencimento.

Além disso, para que a funcionalidade esteja disponível, é necessário conceder a permissão correspondente no menu do perfil associado ao usuário.

### Cálculo do valor líquido

Esta opção permite que o usuário selecione os lançamentos da visão e realize o cálculo do valor líquido para conferências.

Este processo deve ser acessado diretamente na visão de lançamentos, na área inferior da visão. Há a possibilidade também de alterar a data do cálculo do valor líquido, por exemplo, utilizando uma data futura.

O cálculo pode ser realizado selecionando vários lançamentos e de coligadas distintas.

### Baixando lançamentos

Após a efetivação e geração dos lançamentos, o usuário poderá efetuar a baixa destes lançamentos através da visão de  
**recebíveis / lançamentos**.

Quando todas as parcelas geradas forem baixadas e o processo de conclusão de confissão for realizado, os lançamentos de origem terão seu status alterados para **"Baixado por Acordo"**.

Em resumo, a baixa do lançamento original da confissão somente irá ocorrer no final do processo de conclusão de confissão de dívida, ou seja, quando a confissão de dívida estiver no status de **"concluída"**.

O Status destes lançamentos que fizeram parte da confissão de divida pode ser observado em **Anexos / Lançamentos Confessados**.

### Cancelamento de baixa

Após a baixa dos lançamentos, pode ocorrer a necessidade de um cancelamento de uma baixa realizada de uma parcela da confissão.

O cancelamento da baixa irá sempre ser realizado na parcela gerada pela confissão, através do processo financeiro de cancelamento de baixa.

O item de baixa do lançamento gerado pela confissão não será excluído, ficando com o status de **"Cancelado"**.

### Cancelando a confissão de dívida

O cancelamento da confissão de dívida é um processo que consiste em cancelar uma confissão que já esteja no status **"Efetivado"**.

#### Passos para cancelar:

1. Verifique primeiro se a opção **"Cancelar Confissão de Dívida"** está habilitada nas permissões de usuário.
2. Selecione uma confissão de dívida no status **"Efetivado"**.
3. Vá em processos **"Cancelar Confissão de Dívida"**.

#### Processamento do Cancelamento da Confissão de Dívida

* A confissão de dívida terá seu status como **"Cancelado"**, não podendo mais sofrer alterações.
* Todos os lançamentos baixados parcialmente terão seu status atualizados para **"Baixado"** e o valor original ajustado de acordo com o total baixado do lançamento.
* Estes lançamentos não serão excluídos da confissão cancelada, mostrando assim um histórico do que já foi pago.
* Todos os outros lançamentos gerados pela confissão e em aberto serão cancelados e excluídos do sistema.
* Os lançamentos de origem que fizeram parte da confissão cancelada e ainda possuem valores em aberto poderão então ser associados a uma nova confissão de dívida.

#### Sobre os lançamentos confessados no cancelamento

* Ao processar o cancelamento, os valores baixados dos lançamentos serão somados sem considerar juros e multas.
* O valor resultante será utilizado e rateado entre os lançamentos de origem (confessados), respeitando o limite de valor de cada lançamento.
* Quando o valor baixado for igual ao valor do lançamento original, este terá seu status atualizado para **"Baixa por Acordo"**.
* Os valores baixados de cada lançamento são registrados no valor de integração, identificado conforme o parâmetro financeiro definido na confissão.

false

⚠️ Importante

O lançamento original que já possui uma associação a uma confissão de dívida, ou seja, com status **"Bloqueado por confissão de dívida"**, só poderá ser quitado através de uma nova confissão.

### Concluindo a confissão de dívida

O processo de **"Conclusão da confissão de dívida"** é a última etapa do módulo de confissão.

Este processo consiste em alterar o status da confissão de dívida para **concluído**, quando não existirem mais pendências de pagamento por parte do cliente.

Para executar o processo, é necessário conceder a permissão correspondente no menu do perfil associado ao usuário.

❌ Não será possível concluir a confissão quando:

* Existirem parcelas com status **"Em Aberto"** ou **"Baixada Parcialmente"**.
* Existirem parcelas condicionais em aberto juntamente com outras parcelas em aberto.

✔️ Será possível concluir quando:

* Todos os lançamentos estiverem com status **"Baixado"**.
* Ou quando todos os lançamentos estiverem baixados e as parcelas condicionais estiverem em **"Em Aberto"**.

### Aplicando reajuste na confissão de dívida

O processo de efetivar reajuste consiste em atualizar os valores das parcelas da confissão de dívida de acordo com os parâmetros definidos nos **Anexos / Dados do reajuste**.

O reajuste da confissão de dívida sempre será efetuado sobre os lançamentos gerados, preservando os valores dos lançamentos que deram origem a confissão.

Ao efetivar o reajuste, será demonstrado no final do processo os novos valores reajustados para todos os lançamentos da confissão. Lançamentos baixados ou baixados parcialmente não terão seus valores reajustados.

É importante ressaltar que os valores reajustados serão sempre distribuídos nos lançamentos através de um valor de integração que deverá ser inserido nos **Anexos / Dados do reajuste**.

* O reajuste não pode ser realizado por entidade.
* O reajuste só poderá ser efetivado em lançamentos com status **"Em Aberto"**.
* O processo de reajuste de confissão também pode ser agendado.

📚 Para entender mais sobre o reajuste consulte:

* [Contrato de Locação - Reajustes](https://tdn.totvs.com/pages/viewpage.action?pageId=435104980)
* [Contrato de Locação - Agendar Reajuste](https://tdn.totvs.com/pages/viewpage.action?pageId=718424579)

### Desfazendo o reajuste

Desfaz os reajustes realizados para o último período reajustado da confissão.

false

⚠️ Importante

* O sistema não permitirá desfazer reajuste quando algum lançamento estiver baixado ou baixado parcialmente.
* O processo sempre irá desfazer o último reajuste efetuado.
* Para verificar os reajustes, consulte **Anexo / Dados Reajustes Vigentes**.

### Atualizando o Saldo da Confissão de Dívida

#### Introdução

O **Processo de Atualização de Saldo** tem como objetivo atualizar os valores dos lançamentos financeiros originais vinculados a uma **confissão de dívida**, considerando as baixas realizadas nos lançamentos gerados por essa confissão.

Quando uma baixa é identificada em um lançamento gerado pela confissão de dívida, o processo registra esse valor como **desconto por meio de valor de integração** no lançamento original confessado.

Além disso, o sistema calcula o **valor líquido do lançamento** utilizando como referência a **data da confissão de dívida**, garantindo que o valor negociado no momento da confissão seja considerado no cálculo.

* Este processo pode também ser agendado, ocorrendo automaticamente conforme configuração.
* Este processo só irá atualizar o saldo de confissões que foram criadas separando Juros e Multa através de valor de integração.

#### Quando utilizar

Este processo deve ser utilizado quando houver:

* **Baixa de lançamentos financeiros gerados por confissão de dívida**
* Necessidade de **refletir corretamente o saldo líquido dos lançamentos originais**
* Necessidade de **atualizar automaticamente o saldo do valor de integração relacionado às baixas dos lançamentos da confissão**

Esse processo ajuda a manter os valores do **contas a receber atualizados e consistentes** com as negociações realizadas.

#### Pré-requisitos

Antes de executar o processo, é necessário:

1. Existirem **confissões de dívida registradas no sistema**.
2. Os lançamentos gerados pela confissão de dívida possuírem **baixa registrada**.
3. A confissão de dívida que será processada deve ser **selecionada no momento da execução do processo**.

#### Passo a passo para execução

##### Executar o processo manualmente ou por agendamento

1. Acesse o menu de **Processos;**
2. Localize o processo **Atualizar Saldo de Confissão de Dívida**.
3. Selecione a **confissão de dívida que deseja processar**.
4. Execute o processo.
5. Aguarde a conclusão do processamento.

#### Funcionamento interno do processo

Durante a execução, o sistema realiza as seguintes etapas:

1. Localiza as **baixas dos lançamentos financeiros gerados pela confissão de dívida**.
2. Identifica os **lançamentos originais confessados**.
3. Registra o valor da baixa como **desconto via valor de integração** no lançamento original.

#### Resultado esperado

Após a execução do processo:

* Os lançamentos originais terão o **valor de integração atualizado** com base nas baixas realizadas.
* O **valor líquido do lançamento** será recalculado considerando o desconto do valor de integração atualizado.
* O sistema refletirá corretamente o **valor atual da confissão**.

#### Dicas ou observações importantes

* O processo **atualiza apenas o valor de integração de baixa**.
* **O valor de baixa do lançamento original não será preenchido ou alterado.**
* Caso ocorra **cancelamento de baixa**, o sistema deverá reduzir automaticamente o valor integrado no lançamento original.
* O processo registra os dados da baixa que geraram atualização de saldo na tabela: **XALGCONFISSAODIVIDABAIXA**
* Essa tabela armazena as informações das baixas utilizadas no cálculo do saldo.

### Incluindo e definindo parcelas condicionais

A funcionalidade da Parcela Condicional permite que a última parcela de um contrato seja cancelada sob determinadas condições, conforme especificado no contrato.

O sistema realiza verificações para garantir que todas as parcelas da confissão de dívida tenham sido pagas antes da data de vencimento para permitir o cancelamento da parcela condicional.

#### Critérios validados pelo sistema:

* **Verificação das Parcelas Pagas:**  
  O sistema realiza uma verificação para garantir que todas as parcelas da confissão de dívida tenham sido pagas antes da data de vencimento. Se todas as parcelas forem pagas dentro do prazo estipulado, o sistema permitirá o cancelamento da última parcela condicional.
* **Parcelas em Aberto ou Pagas Fora do Vencimento:**  
  Se houver parcelas pendentes ou pagas após a data de vencimento, o sistema não permitirá o cancelamento da última parcela condicional.

#### Benefícios

* **Flexibilidade para o Devedor:**  
  Oferece ao devedor a oportunidade de cancelar a última parcela do contrato, desde que todas as obrigações tenham sido cumpridas.
* **Segurança para o Credor:**  
  Garante que o credor receba todos os pagamentos devidos antes de permitir o cancelamento da parcela condicional.

#### Passos necessários para inclusão de Parcela Condicional em Confissão de Dívidas

##### 1️⃣ Verificação dos Lançamentos Financeiros

* Certifique-se de que existam lançamentos financeiros com data de vencimento vencida (e que calculem multa ou juros).

##### 2️⃣ Efetivação do Registro de Confissão de Dívida

* Após a verificação dos lançamentos financeiros, proceda com a efetivação do registro de confissão de dívida.

##### 3️⃣ Inclusão de Parcelas Automáticas

* No processo de Efetivação da confissão de dívida, o sistema incluirá automaticamente as parcelas condicionais.
* Esta parcela condicional conterá o valor correspondente à multa ou juros acrescentados nas parcelas vencidas que possuem esses valores.

##### 4️⃣ Confirmação e Conclusão

* Caso as parcelas sejam baixadas sem multa ou juros, a parcela condicional será cancelada. Caso contrário, a parcela ficará aberta para pagamento.
* Caso exista alguma negociação da confissão de dívidas, será possível cancelar a parcela condicional ou mesmo forçar o cancelamento da mesma através do menu de processos.

#### Funcionalidades específicas para parcelas condicionais

* **Cancelamento de Parcelas Condicionais:**  
  Permite realizar o cancelamento da parcela condicional quando todas as parcelas financeiras estiverem baixadas (com exceção da parcela condicional) e sem alteração do valor original.
* **Forçar cancelamento de parcelas condicionais:**  
  Permite cancelar as parcelas condicionais mesmo existindo baixas com vencimentos.  
  ⚠️ Esta opção requer permissão específica no perfil do usuário.

false

* Após realizar o processo de Cancelar parcelas condicionais, a situação da confissão será alterada para **concluído**.
* No processo de Cancelar parcelas condicionais, o sistema sempre concluirá a confissão de dívida, visto que as parcelas condicionais foram canceladas e não existem mais pendências de cobrança nesta confissão.

Atendendo as premissas acima, o processo irá ser concluído com sucesso e o status da confissão de dívida passará a ser **"Concluído"** não possibilitando mais alterações em seus cadastros.

Os lançamentos originais confessados terão seu status alterado para **"Baixado por Acordo".**

### Contabilização dos lançamentos confessados

É importante notar que os lançamentos contábeis confessados terão seus itens de baixa preenchidos com itens de baixa contábeis no caso onde a confissão é cancelada e alguns lançamentos relacionados a este lançamento de origem já tiveram uma baixa contábil efetuada.

Para este processo, de cancelamento de confissão onde já existe baixa de parcelas, o sistema irá se valer da configuração de contabilização padrão do TOTVS Gestão Financeira, podendo ser definida nas tabelas opcionais ou no tipo de documento.

Para a correta contabilização dos lançamentos confessados, o evento contábil cadastrado no campo **"Evento Contábil para Baixa por Acordo"** deve estar preenchido e funcional.

Para entender como realizar a configuração da contabilidade apontando o default para o tipo de documento, [veja a documentação aqui. (clique aqui)](https://tdn.totvs.com/pages/viewpage.action?pageId=728658149)
