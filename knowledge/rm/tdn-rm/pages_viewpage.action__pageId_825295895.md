---
content_hash: e1b5f57acf507ab8fcdd0a2ad8aa449fa99a04debef2b69f59425d4f81c43345
fetched_at: '2026-06-29T00:11:48.666534+00:00'
page_id: '825295895'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Shopping - Template de Confissão de Dívida
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=825295895
version: 15
---

---

## 📘 Introdução

Este cadastro permite registrar e definir padrões para os detalhes da negociação, incluindo informações como o tipo de juros aplicado, se haverá cobrança de multa e juros, a possibilidade de desconsiderar esses encargos e até mesmo condições especiais para a última parcela, como descontos, forma de pagamento e ordem de prioridade.

Não há limite para a criação destes templates, entretanto, somente um template pode ser associado em uma confissão.

---

## 🔐 Acesso à funcionalidade

Para acessar esta funcionalidade, será necessário conceder acessos ao perfil destes usuários que irão atuar com a Confissão de dívida.

Para conceder acesso à funcionalidade, siga estes passos:

1️⃣ **Acesse o módulo de Serviços Globais**  
Navegue em **Segurança > Perfis**.

2️⃣ **Edite o perfil do usuário**  
Selecione o perfil do usuário que necessita acessar o Template de confissão de dívida.

3️⃣ **Configure o acesso ao menu**  
Na guia **"Acesso a Menus"**, navegue até:  **Gestão de Imóveis > Shopping > Template de confissão de dívida**

4️⃣ **Salve as permissões realizadas**  
Após configurar os acessos, salve as alterações do perfil.

5️⃣ **Acesso ao módulo pelo usuário**  
Solicite ao usuário que acesse o módulo de **Gestão de Imóveis**.

6️⃣ **Acesso à funcionalidade**  
Agora, o usuário poderá acessar o menu:  **Shopping > Template de confissão de dívida**.

\*Identificação

## 🧾 Template de Confissão de Dívida – Campos da Tela

Ao acessar esta tela, será possível realizar a inclusão de um Template de Confissão de dívida, veja abaixo os campos disponíveis nesta tela com suas respectivas ações:

---

## 📝 Descrição

**Descrição:**  
Informe a descrição deste registro.

---

## 🤝 Negociação

### ⚙️ Parâmetro: Separar o valor de juros e multas (valor de integração)

Esse parâmetro foi desenvolvido para permitir que, na confissão de dívida, os valores passem a ser gerados de forma individualizada. Com a criação do novo parâmetro, também foi desenvolvido o tratamento correto da distribuição dos valores de juros e multa durante a geração das parcelas da confissão de dívida.

Para isso, foi realizado um tratamento nas opções já existentes que define como os juros e multa devem ser distribuídos (quando o parâmetro estiver marcado).

---

### 💰 Tipo de Juros

**Multa e Juros:**  
Este campo indica se a renegociação inclui multas e juros sobre a dívida original.

Quando a opção **Separar o valor de juros e multa (valor de integração)** estiver ativada juntamente com este parâmetro, o sistema:

* Distribui o valor original, juros e multa proporcionalmente em todas as parcelas.
* Mantém a separação dos valores de forma clara em cada lançamento.

---

**Multa e Juros na última parcela:**  
Determina se multas e juros serão aplicados apenas na última parcela, em vez de distribuídos ao longo do pagamento.

Quando a opção **Separar o valor de juros e multa (valor de integração)** estiver ativada juntamente com este parâmetro, o sistema:

* As primeiras parcelas recebem apenas o valor original da dívida.
* Todos os juros e multa são concentrados somente na última parcela.
* Ainda assim, o sistema mantém a separação individualizada dos valores.

---

**Desconsiderar multa e juros:**  
Se marcado, indica que as multas e juros não serão considerados na renegociação.

---

**Última parcela condicional:**  
Quando selecionada permite especificar uma condição especial apenas para o pagamento da última parcela.

---

## 📦 Parcelas

**Quantidade de parcelas:**  
Neste campo o usuário define o número total de parcelas para pagar a dívida renegociada.

**Primeira parcela (%):**  
Define a porcentagem do valor total da dívida que será paga na primeira parcela.

**Permitir alterar quantidade de parcelas:**  
Se marcado, permite que o usuário altere a quantidade de parcelas durante o processo de renegociação.

---

## 📅 Vencimento

**Quantidade de vencimentos no mês:**  
Indica a frequência com que as parcelas vencem em um mês (por exemplo, uma vez por mês, duas vezes por mês, etc.). Num máximo de 4 vencimentos ao mês.

**Permitir alterar vencimento:**  
Se habilitado, permite ao usuário alterar a data de vencimento das parcelas durante a renegociação.

---

## ➕ Acréscimo

**Valor acréscimo:**  
Neste campo o usuário poderá especificar se o acréscimo será uma quantia fixa.

**Mínimo %:**  
Mínimo percentual de acréscimo que será aplicado na confissão.

**Máximo %:**  
Máximo percentual de acréscimo que será aplicado na confissão.

**Aplicar em:**  
Permite escolher onde essas configurações de acréscimo serão aplicadas, seja em lançamentos de locação, fundo promocional ou condomínio.

**Permite alterar aplicação:**  
Marcando essa opção o usuário poderá definir em quais entidades serão aplicados os acréscimos definidos acima.

---

## ➖ Desconto

**Valor desconto:**  
Neste campo o usuário poderá especificar se o desconto será uma quantia fixa.

**Mínimo %:**  
Mínimo percentual de desconto que será aplicado na confissão.

**Máximo %:**  
Máximo percentual de desconto que será aplicado na confissão.

**Aplicar em:**  
Permite escolher onde essas configurações de desconto serão aplicadas, seja em lançamentos de locação, fundo promocional ou condomínio.

**Permite alterar aplicação:**  
Marcando essa opção o usuário poderá definir em quais entidades serão aplicados os descontos definidos acima.

---

## 💳 Forma de Pagamento

### 🔄 Tipo de Pagamento

**Linear:**  
Indica que o pagamento das parcelas será feito de forma constante, ou seja, o mesmo valor em todas as parcelas.

**Prioridade:**  
Define a ordem de prioridade para os pagamentos. Quando há dívidas de diferentes entidades, poderá então ser definido aqui qual entidade será quitada primeiro.

**Ordem de prioridade:**  
Somente disponível quando o pagamento é por prioridade, aqui o usuário irá especificar então, a ordem em que as dívidas serão pagas, isto é, qual entidade tem maior prioridade sobre as outras.

---

## 🔓 Permissões

**Permite alterar o plano da confissão de dívida:**  
Indica se o plano de renegociação da dívida pode ser alterado posteriormente, dando flexibilidade ao devedor caso suas circunstâncias mudem.

Aplicação

## 📄 Aplicação de Template de Confissão de Dívida

Para aplicar um template previamente cadastrado, basta criar ou editar uma confissão no sistema.

---

## 🧾 Seleção do Template

No campo **"Template de confissão de dívida"** deve ser selecionado o template que será utilizado.

Assim que selecionado, todos os valores pré-configurados, bem como suas regras serão padrão para a confissão.

Somente poderão ser alterados os campos, onde, no template, foram definidos com a opção **"Permitir alterar"**.

## ⚠️ Importante

Os valores mínimos e máximos definidos no template já são restritivos.

Dessa forma, caso sejam definidos valores mínimos e máximos para acréscimos e descontos, somente valores dentro dessa faixa serão aceitos.
