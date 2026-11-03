---
content_hash: 7d727545c97dfc5c5d0e81e7253b6b5ba531c85732d22acea28a4767f6163ecc
fetched_at: '2026-06-29T00:10:06.754721+00:00'
page_id: '452719336'
product: rm
source: tdn-rm
title: Dados do Residente ou Domiciliado no Exterior
type: documentation
url: https://tdn.totvs.com/display/LRM/Dados+do+Residente+ou+Domiciliado+no+Exterior
version: 12
---

Este histórico armazena todos os registros de **residente ou domiciliado no exterior** de um beneficiário, que serão utilizados na **Declaração de Imposto de Renda de Pessoa Física (DIRF)** para identificar os pagamentos realizados no exterior.

Para realizar o cadastro, acesse o menu Administração de Pessoal | Cadastros | Funcionários | Anexos | Folha de Pagamento | Dados do Residente ou Domiciliado no Exterior.

Preencha os campos com as informações referentes à alocação do beneficiário no exterior e salve o registro.

---

**PONTOS DE ATENÇÃO:**

**Vinculação ao cadastro do funcionário**

* + - Para que o sistema identifique que o pagamento foi feito ao exterior, é necessário:  
      Informar o registro de alocação no cadastro do funcionário, na aba Situação, no campo “Alocação do residente ou domiciliado no exterior”.
    - Essa vinculação deve ser feita antes do lançamento dos eventos que compõem os rendimentos pagos ao residente ou domiciliado no exterior.

Após essa associação, durante o lançamento de eventos na Ficha Financeira, a alocação será automaticamente considerada no período, identificando corretamente os pagamentos realizados ao exterior.

**Ficha Financeira**  
Também é possível inserir ou remover a alocação diretamente na Ficha Financeira, através da aba “Domiciliado no Exterior”.

⚠️ **Atenção:** Pagamentos realizados ao exterior não são informados no Informe de Rendimentos.

**Comportamento na geração da DIRF**  
Na geração da DIRF em arquivo, o sistema irá:

* + - Identificar todos os eventos pagos ou descontados no período relacionado à alocação informada na ficha financeira.
    - Classificar esses eventos como rendimentos pagos a residentes ou domiciliados no exterior.
    - Não incluir esses valores nos rendimentos tributáveis da DIRF em arquivo nem no Informe de Rendimentos.

**Importante:**  
Caso o funcionário possua rendimentos não pagos no exterior, mesmo que com a mesma data de pagamento, esses devem ser lançados em um período diferente da ficha financeira, sem a alocação informada no cadastro. Para isso, remova a vinculação no campo “Alocação de residentes ou domiciliados no exterior” no cadastro do funcionário antes do lançamento.

**Gerando a DIRF para Residentes ou Domiciliados no Exterior**  
Para gerar a DIRF em arquivo contendo informações de pagamentos a residentes ou domiciliados no exterior, acesse os parâmetros da Coligada, na aba DIRF em arquivo | Declarante, marque a opção: “Pagou rendimentos a residentes ou domiciliados no exterior”.

**Observações importantes:**

* + - * Mesmo que o beneficiário tenha pagamentos realizados no exterior registrados na ficha financeira, se a opção **“Não pagou rendimentos a residentes ou domiciliados no exterior”** estiver marcada, o processo de geração da DIRF **c**onsiderará todos os pagamentos do beneficiário segundo o tipo de tributação específico de cada um, ignorando a identificação de pagamento no exterior.
      * Caso a opção **“Pagou rendimentos a residentes ou domiciliados no exterior”** esteja marcada, mas o beneficiário não tiver período na ficha financeira com alocação de residente ou domiciliado no exterior, o processo não irá informar nenhum rendimento como pago no exterior. Todos os pagamentos serão informados conforme o tipo de tributação específico, sem classificação como rendimento pago no exterior.

---

### **Aba Identificação**

**Dados Cadastrais**

Nesta aba são preenchidos os dados cadastrais do beneficiário residente ou domiciliado no exterior. As informações são utilizadas para compor o relatório da DIRF em arquivo, conforme exigências da Receita Federal.

**Campos da Tela**

* + **País** *(Obrigatório)*: Informa o país de residência fiscal do beneficiário do rendimento. Para este campo, o sistema envia à DIRF o código do país conforme tabela oficial da Receita Federal.
  + **Estado/Província**: Informa o estado ou província do país informado, onde reside o beneficiário.
  + **Município**: Informa o município de residência, vinculado ao estado/província informado.
  + **Logradouro**: Nome da rua, avenida ou via onde o beneficiário reside.
  + **Número**: Número do endereço da residência do beneficiário.
  + **Complemento**: Informações adicionais do endereço, como bloco, apartamento etc.
  + **Bairro / Distrito**: Bairro ou distrito de residência.
  + **Código Postal**: Código postal (CEP ou equivalente) do endereço informado.
  + **Telefone**: Número de telefone de contato do beneficiário.

**Como cadastrar o código de país corretamente para envio na DIRF**  
Para que o campo "País" seja corretamente interpretado na geração da DIRF em arquivo, é necessário seguir os seguintes passos de parametrização:

1. 1. **Classificação de País:** Acessar o menu eSocial | Cadastros | Endereços | Classificação de Países, clicar em **"**Novo", informar um Identificador e uma Descrição e clicar em Salvar;
   2. **Codificação de País:** Acessar o menu eSocial | Cadastros | Endereços | Endereços | Países | Anexos | Codificação de Países, no anexo, clicar em "Novo", informar o código da classificação criado anteriormente, o código do país, conforme tabela da Receita Federal e clicar em Salvar.
   3. **Parâmetro de Conceito de Classificação:** Acessar o menu Configurações | Parâmetros | Parametrizador | 06.07 – eSocial | Configurações Gerais, no campo "Conceito de Classificação para Códigos de Países", informar o código de classificação criado anteriormente e concluir a parametrização seguindo os passos do sistema.

✅ **Importante:** Somente após esse cadastro e parametrização, o sistema conseguirá gerar corretamente o código do país no arquivo da DIRF, conforme exigido pela Receita Federal.

**Dados Fiscais**  
Nesta aba são informados os dados fiscais do beneficiário residente ou domiciliado no exterior. Essas informações são essenciais para a correta geração da DIRF em arquivo, conforme regras da Receita Federal.

**Campos Obrigatórios**

* + **Indicador de Beneficiário:** Informa se o beneficiário está dispensado ou não de apresentar o NIF – Número de Identificação Fiscal.
  + **Indicador de que o País não exige NIF:** Indica se o país de residência fiscal do beneficiário exige ou não a apresentação do NIF.
  + **Tipo de Rendimento:** Informa o tipo de rendimento pago ao beneficiário residente no exterior, de acordo com a tabela da Receita Federal.
  + **Nº de Identificação Fiscal – NIF:** Campo obrigatório quando o beneficiário e/ou o país não são dispensados de apresentar o NIF.  
    O NIF é o número fornecido pelo órgão de administração tributária do país de residência, identificando a pessoa física ou jurídica.
  + **Código da Receita:** Código do tipo de pagamento realizado ao beneficiário, conforme tabela da Receita Federal.
  + **Forma de Tributação:** Define como será feita a tributação do pagamento ao beneficiário, conforme opções previstas na tabela da Receita Federal.

**Regras de Preenchimento – NIF**

* + Se for selecionada a opção “Não é dispensado do NIF” nos campos Indicador de Beneficiário e/ou Indicador de que o País não exige NIF, o campo “Nº de Identificação Fiscal – NIF” passa a ser obrigatório.
  + Se for selecionada a opção “É dispensado do NIF”,  o campo “Nº de Identificação Fiscal – NIF” não deve ser preenchido.

**Período**  
Campos utilizados para informar o período de residência do beneficiário no exterior.

🔹 **Atenção:** Essas datas são apenas informativas e não interferem na identificação dos pagamentos realizados ao exterior.

* **Data Inicial:** Data de início da alocação do beneficiário no exterior.
* **Data Final:** Data de término da alocação.

### **Aba Dados do Residente ou Domiciliado no Exterior no Período**

Esta aba foi criada para atender às exigências doeSocial e deve ser utilizada para informar períodos específicos em que o funcionário teve tributação diferenciada.

Atendendo ao item 14.7 do documento "Perguntas e Respostas do eSocial" (disponível neste link), foi implementada a funcionalidade que permite ao usuário informar, por envelope/período, os seguintes campos do evento S-1210:

* `<indNIF>` – Indicador de obrigatoriedade do NIF
* `<nifBenef>` – Número de Identificação Fiscal do beneficiário
* `<frmTribut>` – Forma de tributação

Essa estrutura garante a correta geração das informações conforme exigido pelo eSocial, especialmente em casos de **tributações distintas dentro da mesma competência**.

**Exemplo:**  
Um funcionário teve cálculo de férias em uma competência com 20 dias, com retenção de IRRF. Porém, no período 1, quando as férias foram lançadas, o salário do funcionário não atingiu a base para retenção do IRRF. Nesse caso, como o período possui tributação diferenciada, é necessário cadastrar esse período na aba **Dados do Residente ou Domiciliado no Exterior no Período**.

Na geração do evento **S-1210**, o sistema irá buscar primeiro as informações cadastradas para os períodos nesta aba. Se não houver nenhum dado, os dados serão gerados com base nas informações da aba **Identificação**.

**Campos**

* + **Mês Competência:** Mês de referência para a tributação diferenciada.
  + **Ano Competência:** Ano de referência para a tributação diferenciada.
  + **Período:** Período específico da tributação diferenciada.
  + **Indicador de Beneficiário:** Campo obrigatório que indica se o beneficiário está dispensado ou não de apresentar o Número do NIF (Número de Identificação Fiscal).
  + **Indicador de que o País não exige NIF:** Campo obrigatório que informa se o país exige ou não o Número do NIF.
  + **Nº de Identificação Fiscal – NIF:** Campo obrigatório quando o beneficiário e/ou o país não estão dispensados de apresentar o NIF.  
    Este número é fornecido pelo órgão tributário do país e identifica pessoa física ou jurídica.
  + **Forma de Tributação:** Campo obrigatório onde o usuário informa a forma de tributação do pagamento realizado ao beneficiário residente ou domiciliado no exterior, conforme tabela da Receita Federal.

|  |  |
| --- | --- |
|  | Informações Complementares |
