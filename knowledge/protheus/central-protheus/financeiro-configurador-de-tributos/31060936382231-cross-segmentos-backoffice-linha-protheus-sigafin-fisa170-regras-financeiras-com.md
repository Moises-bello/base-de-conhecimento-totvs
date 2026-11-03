---
article_id: 31060936382231
category: Financeiro - Configurador de Tributos
content_hash: 7901f1ea5a6ace3f4359d7fe7e2ab8b2351be6bc9dd3162bad1b8a1b3df29be4
fetched_at: '2026-06-28T22:37:46.181371+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos Backoffice Linha Protheus - SIGAFIN - FISA170 - Regras financeiras
  - Como criar uma regra de vencimento de título de IR no Contas a Pagar
type: support-article
updated_at: '2025-10-06T19:55:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31060936382231-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Regras-financeiras-Como-criar-uma-regra-de-vencimento-de-t%C3%ADtulo-de-IR-no-Contas-a-Pagar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31060936351127) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Como criar uma regra de vencimento de título de IR ao Contas a Pagar?

**Ambiente**  
 Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da versão 12.1.2210

**Solução**  
Para definir o **vencimento de um título de IR** ao **Contas a Pagar** por meio do **Configurador de Tributos (FISA170)**, é necessário que os cadastros de **Fornecedor e Natureza** estejam previamente criados.

Ressalta-se que os cadastros de **fornecedor** e **natureza** não devem conter parametrizações de impostos, uma vez que toda a configuração é realizada exclusivamente nas **Regras Financeiras**, conforme ilustrado no exemplo a seguir:

**1.  FISA710 - Regras Financeiras > Regra do Título**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35447062056343)

Para esse cenário, crie a **regra de título** considerando os campos indicados a seguir:

**Preenchimento dos campos**:

* **Código**
* **Descrição**
* O **Tipo de Movimento (Tp. Movto)**, selecionando a opção **Impostos**
* **O****código do participante** (fornecedor) para o qual será gerado o título;
* A **carteira**, que neste caso deve ser definida como **Pagar**;
* A **natureza** previamente criada para vinculação do tributo;
* O **tipo de título**, aplicável aos três impostos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35056729538711)

**1.2 Regra de Cálculo:**

Para esse cenário, crie a **regra de cálculo** considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **% Base**: 100%
* **% Alíquota**: conforme a necessidade.
* **Edita Cálculo**: Sim.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35055959415831)

**1.3 Regra de vencimento:**

Para esse cenário, crie a **regra de cálculo** considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Dia do Vencimento**: conforme a necessidade.
* **Data base p/ vencto. do imposto (emissão)** define o critério para a geração do **IRRF**, permitindo a seleção entre as seguintes opções:

1. Data de emissão do título principal;

2. Data de vencimento real do título principal;

3. Data de emissão contábil do título principal (data de entrada do documento no sistema).

Manteremos a definição na **opção "Emissão"**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35055907126039)

**1.4 Regra de Retenção:**

Para este cenário, crie a **regra de retenção** considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Cumulatividade**
* **Valor Mínimo de Retenção.**
* **Valor máximo de retenção.**
* **Demais campos**: conforme a necessidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35055907127063)

**1.5 Regras Financeiras:**

Este cadastro tem a finalidade de estabelecer a regra de retenção do tributo aplicada aos títulos gerados diretamente no módulo Financeiro, vinculando-se às regras previamente configuradas.

Adicionalmente, sua função é identificar o tributo ao qual a regra se refere, relacionando a regra financeira ao respectivo imposto definido pela legislação federal, estadual ou municipal.

Para este cenário, é necessário criar a regra financeira correspondente ao imposto na aba **Dados Gerais**, preenchendo os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Início de Vigência**: data inicial
* **Fim da Vigência**: data final
* **Fato Gerador:** 1 – Competência (emissão) | 2 – Caixa (baixa)
* **Aplica-se à Carteira**: (1 – Pagar ou 2 – Receber; neste caso, selecionar a opção *Pagar*)
* **Valor do Título**: (1 – Subtrair, 2 – Somar ou 3 – Sem ação. Neste caso, selecionar a opção Subtrair)
* **Parcelamento**: opcional, conforme a necessidade.
* **Tributo**: imposto a ser cadastrado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35055907128087)

**1.6** Na aba **Regras Gerais**, vincule todas as regras criadas anteriormente nas **regras financeiras**, considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Regra de Vencimento**
* **Regra de Título**
* **Regra de Cálculo**
* **Regra de Retenção**

```
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35055907129623)  
  
 
```

**1.7 Cadastro de Fornecedor**

**1.7.1** No **cadastro do fornecedor**, criado sem configuração de impostos, vincule a **regra financeira** em **Outras Ações → Tipos de Retenções**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35055907130903)

**1.7.2** Vincule o código da **Regra Financeira** conforme exemplo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35055959424151)

**1.8 Cadastro da Natureza**

No **cadastro de** **natureza,** criado sem parametrização de impostos, vincule a **regra financeira** em **"Tipo de retenção x natureza",** conforme exemplo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35055907132951)

1.9 **Financeiro**

No financeiro, lançar o título, especificando o fornecedor e a natureza relacionados aos impostos gerados pelo Configurador de Tributos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35055907133847)

**Importante**

Para o cálculo da retenção de IRRF em notas de entrada e saída, por meio do Configurador de Tributos, é necessário cadastrar a respectiva Regra Fiscal.

**Saiba mais**

[Configurador de Tributos - Regras Financeiras](https://tdn.totvs.com.br/display/public/PROT/Configurador+de+Tributos+-+Regras+Financeiras)
