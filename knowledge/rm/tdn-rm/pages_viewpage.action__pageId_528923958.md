---
content_hash: bd5e705106b8020b87307eab23a7544ed200601a48d49732f1b067e6f65173b8
fetched_at: '2026-06-29T00:10:35.476938+00:00'
page_id: '528923958'
product: rm
source: tdn-rm
title: Relatórios - Ficha Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=528923958
version: 46
---

## **Ficha Financeira ( Sem Data Base )**

![Reforma Tributária](https://tdn.totvs.com/download/attachments/528923958/1034802778/fichafinanceira.png)

# Ficha Financeira

]]>

# Ficha Financeira

**TOTVS Incorporação | Construção e Gestão de Imóveis**

A **Ficha Financeira** é um relatório essencial para a análise detalhada dos valores financeiros de um contrato de venda, permitindo ao usuário visualizar a composição das parcelas, reajustes, juros, multas, descontos e saldos de forma clara e organizada.

---

## Acesso ao Relatório

O relatório de **Ficha Financeira** pode ser acessado pelos seguintes caminhos:

* **Processos | Relatórios | Ficha Financeira**
* **Relatórios | Novo Gerador de Ficha Financeira**

> ℹ️ **Observação:** Ambos os caminhos levam ao mesmo relatório, diferenciando apenas a forma de navegação.

---

## Ficha Financeira **sem Data Base**

Quando o relatório é gerado **sem Data Base**, o sistema apresenta os valores com base **no Plano de Financiamento do Contrato**, sem considerar uma posição histórica específica.

---

## Parâmetros do Relatório

### Data Base Atual do Contrato

Este parâmetro permanece **bloqueado** quando a opção **Gerar por Data Base** não está sendo utilizada.

> ⚠️ **Importante:**  
> Quando a geração por Data Base não está ativa, o relatório considera apenas os valores vigentes do Plano de Financiamento.

---

### Somar Resíduos do Plano de Financiamento

Quando este parâmetro está **marcado**, o relatório apresenta a **somatória de todos os resíduos** do Plano de Financiamento na Ficha Financeira.

---

### Multa e Juros

Este parâmetro, quando marcado, acrescenta **Multa e Juros** à Ficha Financeira.

> ⚠️ **Atenção:**  
> Este parâmetro fica **bloqueado** quando a opção de **Gerar por Data Base** não está ativa.

---

### Simular Reajuste com Dados Atuais da Base

Este parâmetro realiza apenas uma **simulação**, sem buscar informações históricas e sem gravar reajustes no contrato.

> 🔎 **Observação:**  
> A simulação utiliza apenas os dados atuais da base.

---

## Gerando o Relatório

### Base de Valores pelo Plano de Financiamento

## Campos do Relatório

1. **Valor Original** – Componente principal da parcela
2. **Juros** – Juros antes e após a entrega
3. **Correção Monetária** – Aplicada pelo reajuste
4. **Outros Valores** – Seguro, IPTU, Encargos, etc.
5. **Multa de Atraso**
6. **Juros de Mora**
7. **Desconto**
8. **Valor da Parcela**
9. **Valor Baixado**
10. **Saldo Devedor**

---

## Grid Principal do Relatório

No início do relatório, é exibida a grid com os **componentes geradores de parcelas**, como:

* Sinal
* Mensal
* Bimestral

> ℹ️ **Exemplo:**  
> Componentes *Sinal* e *Mensal* exibidos como geradores de parcelas.

---

## Plano de Financiamento do Contrato

O relatório apresenta o **valor total das parcelas** conforme definido no Plano de Financiamento.

> 📌 **Exemplo:**  
> Valor total das parcelas: **R$ 22.666,14**

---

## Ficha Financeira **com Data Base**

Ao marcar esta opção, o relatório passa a refletir uma **posição exata no tempo**.

> ⚠️ **Atenção:**  
> Após marcar este parâmetro, **não é possível alterar novamente a parametrização**.

---

## Relatório Antes do Reajuste

Quando a Data Base é **anterior ao reajuste**, os valores reajustados **não são considerados**.

---

## Relatório Após o Reajuste

Quando a Data Base é **posterior ao reajuste**, o relatório **considera os valores reajustados**.

---

## Reajuste com Aditivo Contratual

Após a efetivação do aditivo, a Ficha Financeira passa a refletir os **novos valores negociados**.

---

## Baixa de Lançamentos na Ficha Financeira

A Ficha Financeira reflete corretamente:

* Baixas
* Pagamentos antecipados
* Valores de integração

> 📌 **Exemplo:**  
> Lançamento no valor de **R$ 1.153,43**, baixado antes do vencimento.

Desconto

Para exibir os valores de desconto do financeiro na ficha financeira e no plano de financiamento  é preciso cadastrar o componente do tipo 910- desconto do Financeiro para ser exibido o valor

Competência

Ao filtrar a Data  para geração da ficha Financeira, o resultado sempre será o valor da competência do mês/ano filtrado no relatório, ou seja, o retrato dos logs da(s) parcela(s) para o último dia do mês solicitado.

A ficha financeira **não** trabalha com valores pro-rata (por dia) e **não** executa o reajuste para o mês solicitado, somente se marcar a opção de posição atual com reajuste, desta forma , ela NÃO busca informação no tempo, busca os dados que estão na base.

Para considerar valores de perda financeira na ficha financeira, favor marcar o parâmetro geral => Contrato de Venda => Plano de Financiamento =>  Plano de Financiamento =>  Exibir valores de perda financeira no relatório

Portal do Cliente

Ao executar o relatório de Ficha Financeira a partir do PDC (), será sempre considerado o parâmetro de posição atual da base de dados.

Novidade!

A partir do Release 12.1.2506 é possível parametrizar os componentes que serão ignorados na geração da Ficha Financeira, para configurar esta opção informe os componentes a serem ignorados no parâmetro [*Componentes a serem ignorados na FF*](https://tdn.totvs.com/pages/viewpage.action?pageId=435105113#:~:text=Componentes%20a%20serem%20ignorados%20na%20FF%3A).
