---
content_hash: 7b5ce7e36d481f2288d95257bd8377a00607e9ae6e515baf0f7e2ed6041bff0a
fetched_at: '2026-06-29T00:09:16.268346+00:00'
page_id: '421385498'
product: rm
source: tdn-rm
title: Integração Financeiro Parâmetros do Projeto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385498
version: 5
---

---

**Geral**

**Integrado com o Financeiro:**  
Caso esta opção esteja habilitada, a integração com o Financeiro estará ativa.  
   
**Doc. de Lançamento na Lib. de Medição:**  
Informe o tipo de documento para o qual será gerado um lançamento ao liberar uma medição.  
   
**Doc. de Lançamento no Cronog.:**  
Informe o tipo de documento para o qual serão gerados os lançamentos através do Cronograma (ícone Gerar Lançamento no Financeiro).  
   
**Considera prazo de ressuprimento no cronograma de desembolso:**  
Com o parâmetro ativo ao gerar o cronograma de desembolso, serão listados os períodos considerando o prazo de ressuprimento e condição de pagamento.  
   
Se o parâmetro não estiver ativo ao gerar o cronograma de desembolso, serão listados os períodos ignorando o prazo de ressuprimento, respeitando condição de pagamento.  
   
**Natureza Orçamentária Financeira:** Valor da Natureza Financeira a ser enviada em todo lançamento financeiro efetuado pelo TOP. Este campo deve ser utilizado apenas quando a parametrização do lançamento exigir que o campo de Natureza Financeira seja preenchido.

**Saldo para Fluxo de desembolso**

Habilitar geração do saldo de fluxo de desembolso d projeto: Habilita a utilização do processo de gerar lançamento para controle de saldo e fluxo de desembolso do projeto.

**Tipo de documento de Lançamento de linha base:**

Definir qual o tipo de documento da linha base de controle de saldo.

**Tipo de documento de Lançamento de saldo:**

Definir qual o tipo de documento da linha base de controle de saldo.

**Código do cliente : (Receita)**

Informar cliente default para receita.

**Código do fornecedor (Despesa):**

Informar cliente default para despesa.

**Calcular o projeto automaticamente antes da execução do processo**

Por default vem desabilitado.

**Agrupar os lançamentos financeiros por obra.**

Por default esse parâmetro não vem habilitado. Ele agrupa os lançamentos por obra seguindo alguns critérios:

Quando a tarefa e de valor cotado no mesmo período

Quando a tarefa possui o mesmo insumo no mesmo período.

Exemplo:

As tarefas na figura abaixo são de valor cotado com mesmo período e mesma data de vencimento. Por isso quando o parâmetro estiver ativo será agrupado em um unico lançamento na visão do processo de saldo de fluxo de desembolso e na visão de lançamentos financeiros. Porém não serão agrupados na base de dados permanecedendo com identificador unico de lançamentos.
