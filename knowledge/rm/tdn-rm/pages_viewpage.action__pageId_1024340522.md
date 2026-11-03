---
content_hash: 39ec714316773533de54c0433703c03c3fe44f2d43eb821954058ca895faf0f0
fetched_at: '2026-06-29T00:05:48.246856+00:00'
page_id: '1024340522'
product: rm
source: tdn-rm
title: Cadastro de Redutores da Base de Cálculo do IVA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1024340522
version: 51
---

![Reforma Tributária](https://tdn.totvs.com/download/attachments/1025239488/1025239500/ReformaTributaria.png)


# Cadastro de Redutores da Base de Cálculo

Reforma tributária
Gestão de Imóveis

A regra redutora foi criada no contexto da **Reforma Tributária** para
conceder benefícios fiscais em determinadas operações imobiliárias, reduzindo
a base de cálculo sobre a qual os tributos são calculados.

Isso é especialmente relevante em contratos de locação residencial, em que o
redutor social pode impactar diretamente o valor tributável do contrato.

  


## 📌 Conceito da Regra Redutora

A regra redutora atua diminuindo a base sobre a qual o **IVA (Imposto sobre
Valor Agregado)** será calculado, de acordo com os critérios definidos pela
legislação aplicável à Reforma Tributária.

No módulo de Gestão de Imóveis, essa regra é utilizada para ajustar corretamente
os valores tributáveis de contratos de aluguel, especialmente residenciais, em que
há previsão legislativa de aplicação de redutor social.

  


## 📊 Exemplos Práticos

### 🏠 Exemplo 1 – Imóvel Residencial com Redutor Social

**Valor do aluguel:** R$ 1.000,00
  
**Tipo de imóvel:** Residencial
  
**Redutor social cadastrado:** R$ 600,00

**Cálculo da base de tributos:**  
`Base de cálculo do IVA = 1.000,00 – 600,00 = 400,00`
  
➡️ Os tributos serão calculados sobre R$ 400,00, não sobre o valor total do aluguel.

### 🏢 Exemplo 2 – Imóvel Comercial sem Redutor

**Valor do aluguel:** R$ 1.000,00
  
**Tipo de imóvel:** Comercial
  
**Redutor aplicável:** Nenhum

**Cálculo da base de tributos:**  
`Base de cálculo do IVA = 1.000,00`
  
➡️ Neste caso, o redutor social não se aplica e o tributo é calculado sobre o valor bruto.

  


## ⚙️ Funcionalidades do Cadastro

Para configurar a regra no sistema, o usuário deve acessar o módulo
**Serviços Globais**, entrar em **Perfis** e, em seguida,
navegar até o menu:
**02– Aluguel** > **02.05 – Cadastros** > **02.05.01.24 - Informações Tributárias**,
onde estarão disponíveis as opções de **Regras Redutora**.

![Informações Tributárias](https://tdn.totvs.com.br/download/attachments/1024340522/image-2026-1-20_15-11-40.png?version=1&modificationDate=1768932701044&api=v2)

  
- Para acessar o Menu de Regra Redutora acesse o sistema: Gestão de imóveis > Aluguel > Cadastros Aluguel > Informações Tributárias > **Regra Redutora**;
  , estarão disponíveis os campos para definição das regras.

![Informações Tributárias](https://tdn.totvs.com.br/download/attachments/1024340522/image-2026-1-20_15-20-14.png?version=1&modificationDate=1768933214507&api=v2)

  

No módulo de Gestão de Imóveis (Aluguel), o foco principal é o contrato do tipo
**Aluguel**, especialmente quando o imóvel for residencial e houver
aplicação do redutor social.

  


## 🔍 Detalhes do Cadastro

No cadastro, o usuário poderá informar os seguintes dados:

* **Tipo de Contrato:** Aluguel, Venda, Condomínio ou Empreendimento
* **Tipo de Redutor:** Social (imóveis residenciais), Utilizado para aplicação de benefícios fiscais previstos para operações com imóveis residenciais de caráter social, abrangendo venda e locação, conforme legislação vigente.
* **Outros:** Utilizado para demais reduções legais da base de cálculo do IVA que não se enquadram como redutor social.
* **Descrição:** Identificação do redutor (ex.: “Redutor social residencial”)
* **Tipo de Moeda:** Moeda/índice que será utilizado para reajustar o valor
* **Defasagem:** Período de defasagem irá utilizar o índice para o reajuste
* **Data de Início:** Data inicial em que o redutor passa a valer
* **Valor:** Valor monetário definido para o redutor

![Configuração de Informações Tributárias](https://tdn.totvs.com.br/download/attachments/1024340522/image-2026-1-20_15-41-33.png?version=1&modificationDate=1768934493146&api=v2)

  


## 🔄 Processos > Reajuste de Redutoras

Os **reajustes de redutoras da regra tributária** servem para atualizar
ou adequar os **valores de redução** aplicados no cálculo dos tributos,
garantindo que os valores cobrados estejam em conformidade com a
**legislação vigente** e com as **regras fiscais** definidas
para cada operação.

  


### 📘 Explicando de forma simples

* A **regra tributária** define como os impostos serão calculados;
* As **redutoras** são valores que diminuem a base de cálculo ou o valor do imposto;

O **reajuste das redutoras** é necessário quando ocorre:

* Mudança na legislação;
* Atualização de índices oficiais;
* Alteração de regras fiscais aplicáveis ao contrato ou à operação.

  


### ⚙️ Formas de realizar o reajuste

O reajuste pode ser realizado de duas formas:

* **Automaticamente pelo sistema**  
  Utilizando um índice de reajuste (opcional). O sistema calcula e aplica o novo valor automaticamente.
* **Manual**  
  O usuário informa diretamente o novo valor que passará a valer a partir de uma determinada data.

Também é possível **agendar o reajuste**, para que o sistema execute a atualização
automaticamente na data programada, quando o ambiente estiver devidamente parametrizado via Job Server 3 camadas.

  


### 📊 Onde o reajuste é utilizado

O valor reajustado passa a ser considerado automaticamente:

* Na base de cálculo;
* Nos lançamentos financeiros;
* Nos valores exibidos na visão do financeiro.

Ou seja, **não é necessário ajustar os lançamentos manualmente**
após a realização do reajuste.

  


### 📅 Quando o novo valor passa a valer

Cada reajuste possui uma **data de início (vigência)**.
A partir dessa data, o sistema passa a utilizar automaticamente o novo valor
nos lançamentos financeiros.

  


### 🧾 Exemplo na prática

* Valor inicial cadastrado: **R$ 600,00** (vigente em janeiro);
* Reajuste realizado em fevereiro para: **R$ 650,00**;

**📌 Resultado:**

* Lançamentos de janeiro utilizam **R$ 600,00**;
* Lançamentos de fevereiro em diante utilizam **R$ 650,00**.

Dessa forma, o sistema garante que cada mês utilize o valor correto,
de forma **automática** e **sem erros**.

  


## ⚠️ Regras e Consistências Importantes

Para evitar inconsistências no cálculo fiscal:

* Não deve ser permitido cadastrar mais de um redutor:

+ para o mesmo tipo de contrato
+ com o mesmo tipo de redutor
+ na mesma competência (data)

* Cadastros duplicados podem causar ambiguidade no cálculo de tributos

  


## 📚 Saiba Mais

* [Reforma Tributária – Espaço Legislação](https://espacolegislacao.totvs.com/reforma-tributaria/)
* [Reforma Tributária – Linha RM (Visão Geral)](https://tdn.totvs.com/pages/viewpage.action?pageId=923573484)

]]>
