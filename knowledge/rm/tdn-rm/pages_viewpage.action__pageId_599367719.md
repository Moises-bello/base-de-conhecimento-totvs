---
content_hash: 7025f03fdfc6577bbf4d5d40e1d5aeb7a49636990177a5df773a83bfacc41ef1
fetched_at: '2026-06-29T00:10:57.692612+00:00'
page_id: '599367719'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Controle de Despesas - Informações Adicionais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=599367719
version: 22
---

## 🧾 Cadastro de Despesas

A criação das despesas é realizada por meio de umcadastro simples, que possui particularidades de acordo com o tipo de despesa.

## 🧩 Campos referentes à Despesa

false

🏷️ **Origem**

Define a origem da despesa e é **preenchido automaticamente pelo sistema**, de acordo com o local da chamada.  
Pode assumir os seguintes valores:

* **Aluguel**
* **Venda**
* **Seguro**

---

**🔄 Status**

Campo preenchido automaticamente pelo sistema. Os status possíveis são:

⏳ **Não Integrado**  
Status inicial, definido por padrão no momento da criação da despesa.

✅ **Integrado**  
A despesa tem seu status alterado para este valor quando os movimentos e os lançamentos financeiros são gerados.

⚠️ **Parcialmente Integrado**  
O status é alterado para este valor quando são gerados apenas os movimentos ou apenas os lançamentos financeiros.

---

📅 **Ano Base**

Ano de referência da cobrança da despesa.  
Utilizado para **facilitar os filtros e consultas do usuário**.

---

📆 **Competência**

Define a competência da despesa.  
Exemplo: uma despesa pode ter vencimento em julho, mas ser referente à competência de junho.

---

🔢 **Código**

Campo chave do cadastro, **não pode ser repetido**.  
É gerado automaticamente pelo sistema de forma incremental.

---

**📝 Descrição**

Campo de texto livre, com limite máximo de **50 caracteres**, utilizado para facilitar a consulta e a busca da despesa.  
Exemplo: *Despesa de IPTU*.

---

📄 **Número do Documento**

Número da guia a ser paga como despesa.  
Normalmente corresponde ao **mesmo número informado no documento de cobrança**.

---

🗂️ **Tipo de Despesa**

Define o tipo da despesa cadastrada.  
É utilizado para:

* Agrupar despesas;
* Definir a **natureza financeira** a pagar e a receber.

---

**💳 Tipo de Pagamento**

Define o tipo de pagamento que será utilizado no processo de: Geração das parcelas integradas ao movimento; ou Geração direta do lançamento financeiro.

**⚙️ Parâmetros de Movimento**

* + Define o **tipo de movimento da despesa**, responsável por determinar as configurações que serão consideradas no movimento gerado.  
    Para mais informações sobre **Parâmetro de Tipo de Movimento**, consulte a documentação correspondente.  [Cadastros - Parâmetro de Movimento Aluguel](https://tdn.totvs.com/pages/viewpage.action?pageId=435105352)

💰 **Parâmetros Financeiros**

* + Define os parâmetros financeiros que serão considerados na geração dos **lançamentos financeiros** da despesa.  
    Para mais detalhes sobre **Parâmetros Financeiros**, consulte a documentação. [Cadastros - Parâmetro de Movimento Aluguel](https://tdn.totvs.com/pages/viewpage.action?pageId=435105352)

---

**🏢 Imóvel**

Imóvel ao qual a despesa será vinculada.  
Uma despesa pode ter **apenas um imóvel associado**. 📌 Este campo é utilizado somente quando a Origem da despesa estiver definida como **“Aluguel”**.

false

**🗒️** Caso ocorra **encerramento ou rescisão** do contrato de locação vinculado ao imóvel da despesa, os **lançamentos financeiros de reembolso** com data de vencimento **posterior** ao encerramento ou rescisão **serão cancelados automaticamente**.

**🏢 Empreendimento / Unidade / Subunidade**

Define a associação da **Subunidade** para a qual a despesa será gerada.  
Uma despesa pode ter **apenas uma Subunidade associada**.  📌 Este campo é utilizado **somente quando a Origem da despesa estiver definida como “Venda”**.

false

**🗒️**Caso a Subunidade esteja **vendida** e exista a necessidade de realizar **Distrato**, **Aditivo de Troca de Subunidade** ou **Troca de Comprador** no contrato, esses processos **somente poderão ser efetivados se não existir nenhum lançamento de Reembolso da Despesa em aberto**.

---

🏛️ **Inscrição Municipal**

Define a associação da despesa com a **Inscrição Municipal do imóvel selecionado**.

---

👥 **Cliente / Fornecedor**

Define o fornecedor para o qual será gerado o movimento da despesa.

📌 Quando o **Tipo de Despesa** informado for **IPTU** ou **ITBI**, o Cliente/Fornecedor será buscado automaticamente do cadastro da Subunidade, no campo **Código da Prefeitura**, informado em **Controle de IPTU / Registro**.

---

## 👤 Campos do Responsável pela Despesa

false

👔 **Responsável pela Despesa**

Define se o responsável será **Cliente** ou **Empresa**.

---

📅 **Responsável a Partir**

Quando o responsável for definido como **Cliente**, o sistema permite informar a data a partir da qual a obrigação passou a ser do cliente.

---

## 💰 Campos de Valor da Despesa

false

**💲 Tipo de Valor da Despesa**

Este campo possui duas opções:

* **Valor à vista**
* **Valor a prazo**

📌 Ao selecionar **Valor à vista**, os campos **Nº de parcela(s)** e **Intervalo em dias** ficam desabilitados.  
📌 Ao selecionar **Valor a prazo**, os campos **Nº de parcela(s)** e **Intervalo em dias** ficam habilitados para preenchimento.

---

**💵 Valor à Vista**

Campo utilizado para informar o **valor à vista** da despesa a ser gerada.

---

**💳 Valor a Prazo**

Campo utilizado para informar o **valor a prazo** da despesa a ser gerada.

---

**📆 Primeiro Vencimento**

Neste campo, o usuário deve informar o **primeiro vencimento da despesa** a ser gerada.

false

⚠️ **Atenção**  
Quando a despesa for agregada ao lançamento de aluguel, o **primeiro vencimento** deve estar **sempre dentro do mês de vencimento da primeira parcela do contrato**.

📌 **Exemplo**

* Primeiro Período: 01/01/2025
* Fim do Primeiro Período: 31/01/2025
* Vencimento da Primeira Parcela: 05/02/2025

➡️ O vencimento da primeira parcela do reembolso deverá ser em **Fevereiro/2025**.

**🔢 Nº de Parcela(s)**

Permite informar a quantidade de parcelas que serão geradas para a despesa.

---

🔁 **Periodicidade**

Define a periodicidade das parcelas a partir da data de **Primeiro Vencimento**:

* **Mensal**  
  As parcelas vencem sempre no mesmo dia, variando apenas os meses.
* **Personalizada**  
  As parcelas possuem um intervalo fixo de dias entre elas.

---

**⏱️ Intervalo em Dias**

Permite informar o intervalo de dias entre uma parcela e outra quando a **Periodicidade** estiver definida como **Personalizada**.

---

## 🔄 Campos Referentes ao Reembolso

false

♻️ **Permite Reembolso**

Ao marcar este parâmetro, **todos os demais campos da tela** relacionados ao reembolso serão habilitados para preenchimento.

---

📜 **Regra de Reembolso**

Campo utilizado para armazenar a **regra de reembolso da despesa**.  
Para mais detalhes sobre **Regra de Reembolso**, consulte a documentação específica. [Controle de Despesa - Regra de Reembolso](https://tdn.totvs.com/display/LRM/Controle+de+Despesa+-+Regra+de+Reembolso)

---

💲 **Tipo de Valor do Reembolso**

Assim como o campo **Tipo de Valor da Despesa**, possui duas opções:

* **Valor à vista**
* **Valor a prazo**

📌 Ao selecionar **Valor à vista**, os campos **Nº de parcela(s)** e **Intervalo em dias do reembolso** ficam desabilitados.  
📌 Ao selecionar **Valor a prazo**, esses campos ficam habilitados para preenchimento.

---

📆 **Primeiro Vencimento do Reembolso**

Neste campo, o usuário deve informar o **primeiro vencimento da parcela de reembolso** a ser gerada.

---

🔢 **Nº de Parcela(s) do Reembolso**

Permite informar o número de parcelas que serão geradas para o reembolso.

---

🔁 **Periodicidade do Reembolso**

Define a periodicidade das parcelas de reembolso a partir da data de **Primeiro Vencimento do Reembolso**:

* **Mensal**  
  As parcelas vencem no mesmo dia, variando apenas os meses.
* **Personalizada**  
  As parcelas possuem um intervalo fixo de dias entre elas.

---

⏱️ **Intervalo em Dias do Reembolso**

Permite informar o intervalo de dias entre uma parcela de reembolso e outra quando a **Periodicidade do Reembolso** estiver definida como **Personalizada**.

---

**⚙️ Código do Parâmetro de Integração Financeira**

Utilizado para armazenar o **parâmetro de integração financeira de aluguel**, que será usado na geração dos lançamentos de reembolso.  
Para mais detalhes sobre **Parâmetros de Integração Financeira**, consulte a documentação correspondente. [Cadastros - Parâmetros de Integração Financeira para Aluguel](https://tdn.totvs.com/pages/viewpage.action?pageId=435105050)

---

## ⚠️ **Importante**

**Centro de Custo nos Lançamentos de Reembolso**

Na geração dos lançamentos de reembolso, o sistema realiza a definição do **Centro de Custo** de forma automática, seguindo uma **ordem lógica de prioridade**, conforme prioridade abaixo informada:

---

🎯 **Regra de Prioridade Aplicada**

1️⃣ **Cadastro do Imóvel**  
Caso o imóvel não possua áreas fracionadas **ou** as áreas não tenham Centro de Custo informado, o sistema buscará o **Centro de Custo cadastrado diretamente no imóvel**.

3️⃣ **Parâmetros de Integração Financeira da Despesa**  
Se não houver Centro de Custo informado no imóvel, o sistema utilizará o **Centro de Custo definido nos Parâmetros de Integração Financeira da despesa**.

---

📷 **Abaixo é apresentada a tela de Despesas** **de Aluguel**

Clicando no botão **Salvar**, o sistema irá gravar as parcelas vinculadas à despesa.

Importante: Não será possível integrar uma despesa, isto é, gerar movimentos de despesa ou lançamentos de reembolso, caso o seguro associado não esteja com o status de "Efetivado".

Informações Complementares

---

* [Despesa - Anexo - Parcela de Despesa](https://tdn.totvs.com/pages/viewpage.action?pageId=435105347)
* [Despesa - Anexo - Parcela de Reembolso](https://tdn.totvs.com/pages/viewpage.action?pageId=435105348)

Recursos Adicionais

---

* [Parcela de Reembolso - Processo - Gerar Lançamentos de Reembolso](https://tdn.totvs.com/pages/viewpage.action?pageId=435105323)
* [Parcela de Reembolso - Processo - Cancelar Lançamentos Financeiros](https://tdn.totvs.com/pages/viewpage.action?pageId=435105350)
* [Parcela de Despesa - Processo - Gerar Movimento de Despesa](https://tdn.totvs.com/display/LRM/Parcela+de+Despesa+-+Processo+-+Gerar+Movimento+de+Despesa)
* [Parcela de Despesa - Processo - Cancelar Integração de Despesa](https://tdn.totvs.com/pages/viewpage.action?pageId=435105282)
