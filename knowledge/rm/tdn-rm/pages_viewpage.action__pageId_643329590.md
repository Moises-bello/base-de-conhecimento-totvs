---
content_hash: a25166cb979b41f947a5852835039e2d2726474c0908a0f103e7edb3f6e7dc15
fetched_at: '2026-06-29T00:11:10.358024+00:00'
page_id: '643329590'
product: rm
source: tdn-rm
title: Lançamento Especial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=643329590
version: 14
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Validações**
3. **Validações Específicas do Lançamento Especial**
4. **Campos**
   1. **Fora da Conta**
   2. ****Conta particular****
   3. **Desconto**
5. **Tipos de Lançamentos**
   1. **Honorários**
   2. **Diárias**
   3. **Taxas e Serviços**
   4. **Material e Medicamento**
   5. **Diagnose e Terapia**
6. **Tela Lançamento Especial**
   1. **Outras Ações / Ações relacionadas**
7. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Nesta aba poderá ser incluído qualquer tipo de lançamento ao **Grupo de Gasto** sem a necessidade que estejam cadastrados no sistema, ou que foram acordados entre o Convênio e o Prestador Principal ou entre o Paciente e o Prestador Principal.

Para utiliza-lo, basta primeiro escolher um **Tipo de Lançamento**, preencher os campos específicos e salvar, neste momento o sistema irá inserir o lançamento no respectivo **Grupo de Gasto** escolhido.

Estes lançamentos podem ser visualizados ou estornados nas respectivas abas dos **Grupos de Gastos da Elaboração de Contas**.

## **02.****VALIDAÇÕES**

Os campos em negrito são de preenchimento obrigatório.

Durante a inclusão de um item, as seguintes validações podem ocorrer:

* **Atendimento:**
  + Deverá estar com o status diferente de "Cancelado".
* **Parcial:**
  + Deverá estar com o status diferente de "Faturada", "Liberada" ou "Cancelada".
  + Não poderá ter nota fiscal emitida e o convênio particular.
* Item estornado não pode ser alterado
* O item especial não pode ser alterado. Deve ser estornado e incluído novamente pela página Especial
* A data do lançamento deve estar dentro do período da parcial.

* **Data:**
  + esta regra é valida somente para Taxas, Serviços, Diagnose, Terapia e MatMed.
  + A data do lançamento deve estar dentro do período da parcial.
  + A data/hora de início não pode ser maior que a data/hora final.
  + A hora não pode ser igual 24:00. Deve-se lançar com a hora igual a 00:00 e acrescentar 1 dia na data
* **Código:**
  + É permitido lançar um código fixo de procedimento ou produto.
  + É permitido pesquisar um procedimento ou produto na tabela do convênio.
* **Quantidade:**
  + Esta regra é válida somente para Taxas, Serviços e MatMed.
  + Caso o parâmetro **Limita quantidade máxima definida pela TISS** configurado nas condições contratuais (aba Eletrônico III - TISS) esteja marcado, e a quantidade informada for maior ou igual a 1000, o sistema não permitirá salvar o registro.
* **Custo Unitário:**
  + Se o custo unitário for preenchido, ele deverá ser igual ou menor que o valor.
* **Fator/Unidade:**  
  + Obrigatório para os lançamento de taxa, serviços, materiais, medicamentos, órtese e prótese.
* **Código Prestador:**
  + Obrigatório para Honorário, somente prestador ativo.
* **Código Função do Médico:**
  + Obrigatório para Honorário e deve ser válido conforme a versão TISS.
* **CBO:**
  + Obrigatório para Honorário e deve ser válido conforme a versão TISS.
* **Técnica:**
  + Habilitado somente para Honorário.
* **Tipo de Procedimento**:
  + Habilitado somente para Honorário.

## **03.****LANÇAMENTO FORA DA CONTA**

Ao marcar o campo “Fora da Conta”, o lançamento será gravado no grupo de gasto específico como fora da conta.

Habilita somente para o tipo de lançamento **Honorário**, **Diagnose e Terapia** e **Kit Lançamentos**.

### **Validações:**

* Não pode haver fora da conta para o prestador principal. Se o prestador do lançamento especial for igual ao prestador principal, e marcar Fora da Conta: emitirá mensagem de erro.
* Quando o prestador é indiretamente credenciado ao convênio, o lançamento deve ser dentro da conta (convênios que não sejam particular)
  + Se escolher um prestador credenciado indireto e marcar Fora da Conta: emitirá mensagem e altera para Dentro da conta.
  + Prestador selecionado é credenciado indiretamente ao Convênio.
  + O lançamento será realizado dentro da conta.'

## **04.****LANÇAMENTO CONTA PARTICULAR**

**Para o lançamento para Particular, temos dois comportamentos distintos nessa tela, onde um deles pode ser o lançamento de um item ao Particular, quando o convênio for um específico TISS ou demais convênios**

### Se o convênio for ESPECÍFICOS (TISS e demais convênios):

* A opção Conta Particular ficará habilitada .
  + Se marcar Honorário e marcar campo Particular: vai lançar o honorário na aba de gastos particulares.
  + Se marcar Honorário e desmarcar o campo Particular: vai lançar o honorário na aba de honorário.

É lançado como Gasto Particular, o tipo de grupo de gastos escolhido (honorário, d)

**Validações:**

* Se o convênio for PARTICULAR:  ficará invisível o campo “Conta Particular”. Se escolher o tipo de lançamento “Hotelaria” será gravado na aba gastos particulares com o codgasto = 00.

Caso a conta do paciente utilize um Convênio diferente do tipo Particular, será possível realizar lançamentos ao Particular, bastando marcar o campo Conta Particular.

### **DESCONTO**

**Esta função poderá ser utilizada para lançamentos de descontos, bastando marcar o campo Desconto no momento do lançamento.**

É lançado no grupo de gasto específico, um valor negativo para ser considerado como desconto sobre um lançamento já existente.

Na guia Lançamento Especial, somente aceitará o Tipo de Lançamento = Desconto se existir o código do procedimento lançado a aba da elaboração e o mesmo o centro custo e prestador. Caso contrário dará mensagem de erro.

Importante!

O Lançamento  que sofrerá do desconto, não pode possuir repasse.

## **05.****LANÇAMENTOS DE HONORÁRIO**

Para lançamento de **Honorários**, a opção **Tipo de Lançamento** devera estar selecionada **Honorários**.

Em seguida deve-se informar o **Prestador**, a **Função** do mesmo no procedimento, o **Código** do item, a **Especialidade do Prestador**, o **Centro de Custo/Resultado** de apuração do lançamento, a **Data da Realização**  hora de início e fim, a **Descrição,** a **Quantidade,**o**Valor.**

O tipo do Procedimento (se **Principal, Mesma Via** ou **Outra Via**).

Valores Fixados ao lançar honorário pelo Especial:

* ESPECIAL = E
* CodGGasto = 01

### **Validações Específicas para Honorário:**

Não é permitido lançar Honorários fora da conta para o Prestador Principal.

### **Lançamentos de Diárias**

Deve-se informar  para taxas e serviços os campos  o **Código** do item, a **Descrição, a Quantidade,** o **Centro de Custo/Resultado** de apuração do lançamento, a **Data**, o **Valor**.

O campo código e descrição podem vir da busca ou serem preenchidos manualmente.

Valores Fixados ao lançar uma diária pelo Especial:

* CodGGasto = 02
* CHDIARIAS e VALORCHDIARIAS = 0

### **5.3.****Lançamentos de Taxas e  Serviços**

Informações

O módulo de Lançamento Especial não suporta o registro de minutos de gasoterapia. Para lançar uma TAXA DE OXIGÊNIO, é necessário informar o código do procedimento e o valor total calculado com base no consumo de oxigênio.

Deve-se informar para incluir um item de taxas ou serviços os campos o **Código** do item, a **Descrição, a Quantidade,** o**Fator/unidade, Local de uso**, o **Centro de Custo/Resultado** de apuração do lançamento, a **Data**, o **Valor**.

O campo código e descrição podem vir da busca ou serem preenchidos manualmente.

Valores Fixados ao lançar um taxou serviço  pelo Especial:

- CodGGasto = 03

### **5.3.1. Lançamento de Serviços**

### **5.3.2.** **Lançamento de Taxas**

### **5.3.3.**Aba taxa e serviços

### **5.4.****Material e Medicamento**

Nesta pasta serão lançados os Materiais e Medicamentos somente para efeito de cobrança na conta do paciente.

Deve-se informar para incluir um item basta selecionar o **Local de Uso** do mesmo, pesquisar o item de estoque, informar a **Quantidade** a ser lançada, a **Data** e o **Centro de Custos** de apuração do lançamento, o **Fator/Unidade,** o **Código** do item, a **Descrição** o **Valor.**

Valores Fixados ao lançar matmed pelo Especial:

- ESPECIAL = E

- CodGGasto =

- FATORCONVERSAOMATMED =  1;

**- Não habilitará o campo “Fora da conta”, hora, prestador.**

### **Validação específica matmed especial:**

- Se marcado o Parâmetro Geral ExibeFabricante -> campo Fabricante habilitado (CODFAB).

- Órtese e prótese -> somente digitar códigos que estejam na codificação do convênio, ou emitirá mensagem de erro: “Código não definido para Órtese no padrão de Informação utilizado para este Convênio”.

- Fator/Unidade deve ser informado

### **5.4.1. Materiais**

### **5.4.2. Medicamentos**

### **5.4.3. Órtese**

### **5.4.4.**Prótese

### **5.4.5.**Aba MatMed

### **5.5.****Diagnose e Terapia**

Deve-se para incluir informar um item para diagnose e terapia os campos o **Código**do item, a **Descrição**, a **Quantidade**, o **Prestador, o****Local de uso**, a **Data** hora de início e fim , o **Valor.**

Valores Fixados ao lançar SADT pelo Especial:

- ESPECIAL = E

- CodGGasto = ‘09’

- CHSADT  = 0;

## **06. TELA LANÇAMENTO ESPECIAL**

**Outras Ações / Ações relacionadas**

| Ação | Descrição |
| --- | --- |
| Cálculo do Valor Total | * Cálculo do item :  Valor da unidade: R$150,00  Quantidade lançada : 2   **Valor Total** = Quantidade lançada  \* Valor = R$300,00 |
| Inclua a ação | Inclua a descrição relacionada |
| Inclua a ação | Inclua a descrição relacionada |

## **07. TABELAS UTILIZADAS**

* **SZATENDSADT**
* **SZATENDMATMED**
* **SZATENDHONORARIO**
* **SZATENDDIARIAS**
* **SZATENDTAXASERV**
