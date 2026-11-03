---
content_hash: 88f5a1d3e51b8fc4bc038eb82eb096c13e8aaa37fdd8892b3cef85684bf58888
fetched_at: '2026-06-29T00:05:49.367222+00:00'
page_id: '1040976062'
product: rm
source: tdn-rm
title: 3 - Parametrização do cadastro de Convênios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1040976062
version: 9
---

Para utilizar o **Boleto Híbrido**, é necessário realizar a ativação no cadastro do **Convênio Bancário**.

No menu do sistema, acesse:

**Movimentações Bancárias → Convênio**

Localize o convênio desejado e clique em **Editar**.

No cadastro do convênio, acesse a aba **Boleto Híbrido**.

Em seguida:

1. Marque a opção **Permite registro de boleto híbrido**
2. Informe a **chave PIX fornecida pelo banco**
3. Informe quantos em quantos dias uteis o valor será creditado, para pagamentos efetuados com o **Código de barras**.

⚠️ **Ponto de Atenção**

* Não é permitido utilizar **a mesma chave PIX em convênios diferentes**.
* Cada convênio deve possuir **uma chave PIX exclusiva**.

Após habilitar o boleto híbrido, acesse a aba **Dados Adicionais**.

No campo **Valor código de barras**, selecione uma das opções disponíveis

# Configuração: Valor do Código de Barras

Esta configuração define qual valor será utilizado na geração do código de barras do boleto bancário.

> **Importante:** A opção selecionada impacta diretamente o valor apresentado ao pagador e a forma como descontos, juros, multas e demais componentes financeiros serão considerados durante a cobrança e liquidação do título.

---

# 📋 Opções Disponíveis

| Opção | O que considera? | O que desconsidera? |
| --- | --- | --- |
| **Valor Original** | Apenas o valor original do lançamento. | Todos os descontos, juros, multas, correções e valores opcionais. |
| **Valor Líquido** | Todos os componentes financeiros do lançamento. | Nenhum componente financeiro é ignorado. |
| **Valor Parcial** | Valor original e componentes financeiros não condicionais. | Juros, multa, descontos condicionais e acréscimos condicionais. |

---

## 1️⃣ Valor Líquido

### Como funciona?

O sistema gera o código de barras utilizando o **valor líquido do lançamento na data de vencimento**.

### Considera:

✅ Descontos incondicionais

✅ Descontos condicionais

✅ Juros

✅ Multa

✅ Correção monetária

✅ Valores opcionais e de integração

### Indicação de uso

Quando o boleto deve refletir exatamente o valor calculado pelo motor financeiro na data de vencimento.

---

## 2️⃣ Valor Original

### Como funciona?

O sistema gera o código de barras utilizando exclusivamente o valor originalmente registrado no lançamento.

### Considera:

✅ Valor original do lançamento

### Não considera:

❌ Descontos

❌ Juros

❌ Multa

❌ Correção monetária

❌ Valores opcionais

❌ Valores de integração

### Indicação de uso

Quando a instituição deseja que o boleto apresente apenas o valor nominal da parcela.

---

## 3️⃣ Valor Parcial

### Como funciona?

O sistema gera o código de barras utilizando um valor intermediário entre o valor original e o valor líquido.

### Considera:

✅ Valor original

✅ Descontos incondicionais

✅ Componentes financeiros não condicionais

### Não considera:

❌ Juros

❌ Multa

❌ Acréscimos condicionais por atraso

❌ Descontos condicionais até o vencimento

### Indicação de uso

Quando a instituição deseja permitir que descontos condicionais sejam aplicados somente no momento da liquidação do título.

---

# 🧮 Exemplo Prático

### Dados do lançamento (FLAN)

| Componente | Valor |
| --- | --- |
| Valor Original | R$ 1.150,01 |
| Desconto Incondicional | R$ 50,00 |
| Juros/Multa | R$ 30,00 |
| Desconto Condicional | R$ 20,00 |

---

# 📊 Resultado por Configuração

| Configuração | Fórmula Aplicada | Valor no Boleto |
| --- | --- | --- |
| **Valor Original** | 1.150,01 | **R$ 1.150,01** |
| **Valor Líquido** | 1.150,01 - 50,00 + 30,00 - 20,00 | **R$ 1.110,01** |
| **Valor Parcial** | 1.150,01 - 50,00 | **R$ 1.100,01** |

---

# 🔍 Comparativo Visual

| Componente | Valor Original | Valor Líquido | Valor Parcial |
| --- | --- | --- | --- |
| Valor Original | ✅ | ✅ | ✅ |
| Desconto Incondicional | ❌ | ✅ | ✅ |
| Desconto Condicional | ❌ | ✅ | ❌ |
| Juros | ❌ | ✅ | ❌ |
| Multa | ❌ | ✅ | ❌ |
| Acréscimos por atraso | ❌ | ✅ | ❌ |

---

## 🎯 Resumo

| Objetivo | Opção Recomendada |
| --- | --- |
| Cobrar exatamente o valor calculado pelo motor financeiro | **Valor Líquido** |
| Exibir apenas o valor nominal da parcela | **Valor Original** |
| Aplicar descontos condicionais somente na liquidação | **Valor Parcial** |

Para que o banco receba corretamente as informações do boleto híbrido, é necessário associar os **layouts de registro online**.

Acesse:

**Anexos → Associação do Layout de Registro Online**

Com base na documentação disponível no [Link](https://tdn.totvs.com/pages/viewpage.action?pageId=980993042)  de referência, devem ser criados **5 layouts principais**.

Esses layouts definem quais informações serão enviadas ao banco no momento do **registro do boleto**.

Os layouts necessários são:

1. Modalidade da Multa
2. Valor da Multa
3. Modalidade dos Juros
4. Valor dos Juros
5. Prazo máximo de pagamento após o vencimento

## Modalidade da Multa

Define como a multa será aplicada ao boleto.

As modalidades disponíveis são:

* **Percentage** → Multa em percentual
* **FixedAmount** → Multa em valor fixo

## Valor da Multa

Define o valor da multa que será aplicado ao boleto.

No exemplo apresentado, o layout está configurado para **1% de multa**

## Modalidade dos Juros

Define a forma de cálculo dos juros.

No exemplo abaixo, os juros são enviados como:

**Percentual ao mês (dias corridos)**

Tag utilizada:

PercentagePerCalendarMonth

Também podem ser utilizadas outras modalidades, conforme a necessidade e suporte do banco:

| Tag | Descrição |
| --- | --- |
| AmountCalendarDay | Valor por dia (dias corridos) |
| PercentagePerCalendarDay | Percentual ao dia (dias corridos) |
| PercentagePerCalendarYear | Percentual ao ano (dias corridos) |
| AmountBusinessDay | Valor por dia (dias úteis) |
| PercentagePerBusinessDay | Percentual ao dia (dias úteis) |
| PercentagePerBusinessMonth | Percentual ao mês (dias úteis) |
| PercentagePerBusinessYear | Percentual ao ano (dias úteis) |

## Valor dos Juros

Define o valor de juros aplicado ao boleto.

No exemplo apresentado:

* **1% ao mês**
* Equivalente a **0,03333% ao dia**, considerando **dias corridos**

## Prazo máximo de pagamento após o vencimento

Define quantos dias após o vencimento o boleto ainda poderá ser pago.

No exemplo apresentado:

* Pagamento permitido **até 5 dias após o vencimento**

## Modalidade do desconto

Define a modalidade do desconto condicional que será enviada ao banco.

No exemplo apresentado será utilizada a modalidade **Valor Fixo**.

### Modalidades disponíveis

* **FixedValueUntilInformedDate -** Valor fixo até a[s] data[s] informadas
* **PercentageUntilTheDateInformed -** Percentual até a data informada

⚠️ Importante: Verifique se o banco utilizado suporta a modalidade de desconto configurada. Caso a modalidade não seja suportada, o registro do boleto será rejeitado pelo banco.

## Data Limite para o primeiro desconto

Define a data limite para concessão do primeiro desconto condicional.

No exemplo apresentado, a data será obtida por meio de uma fórmula, responsável por retornar a data que será enviada ao banco.

A informação pode ser armazenada em:

* Valor Opcional;
* Valor de Integração;
* Desconto de Antecipação (Clientes Educacional).

## Valor do primeiro desconto

Define o valor do primeiro desconto condicional.

No exemplo apresentado, o valor será obtido por meio de uma fórmula, responsável por retornar o valor que será enviado ao banco.

A informação pode ser armazenada em:

* Valor Opcional;
* Valor de Integração;
* Desconto de Antecipação (Clientes Educacional).

## Descontos Condicionais Adicionais

É possível configurar até **3 descontos condicionais** para o mesmo boleto.

Para isso, deverão ser configurados os layouts correspondentes a:

* Segunda data limite de desconto;
* Segundo valor de desconto;
* Terceira data limite de desconto;
* Terceiro valor de desconto.

> ⚠️ Importante: Antes de realizar a configuração, verifique se o banco utilizado suporta o envio de múltiplos descontos condicionais. Caso a instituição financeira não disponibilize essa funcionalidade, o registro do boleto será rejeitado e retornará erro no processamento.

## Resultado da Configuração

Após concluir todas as etapas, o convênio estará preparado para:

✅ Registrar Boletos Híbridos;

✅ Gerar QR Code Pix;

✅ Aplicar regras de juros e multa;

✅ Aplicar descontos por pontualidade ou antecipação;

✅ Permitir pagamento após o vencimento, conforme configuração realizada;

✅ Integrar corretamente com o registro bancário.

# 🧮 Utilização de Fórmulas

Os campos que permitem a utilização de fórmulas podem ser configurados quando houver necessidade de realizar cálculos específicos ou personalizar as informações enviadas ao banco durante a geração dos boletos.

É fundamental que o resultado retornado pela fórmula esteja compatível com o formato e o tipo de dado esperado pelo campo correspondente. Dessa forma, garante-se o correto processamento das informações pelo banco e evita-se a ocorrência de rejeições ou inconsistências nos arquivos de remessa.

---

## 📋 Responsabilidade pela Definição das Regras

A definição das regras de negócio utilizadas nas fórmulas é de responsabilidade da instituição, uma vez que tais regras refletem particularidades dos processos financeiros, comerciais e acadêmicos de cada cliente.

Entre os principais cenários que podem demandar fórmulas personalizadas, destacam-se:

* Cálculo de Juros;
* Cálculo de Multa;
* Desconto por Pontualidade;
* Desconto por Antecipação;
* Acréscimos ou Descontos Condicionais;
* Regras específicas para integração bancária.

---

## 🤝 Apoio de Consultoria

Caso haja necessidade de apoio na construção ou validação das fórmulas, recomenda-se o acionamento da equipe de consultoria.

A consultoria poderá auxiliar nas seguintes atividades:

* Levantamento e entendimento das regras de negócio da instituição;
* Definição da lógica de cálculo;
* Construção das fórmulas no sistema;
* Validação dos resultados obtidos;
* Testes integrados com o processo de cobrança bancária.

> **Importante:** A equipe de consultoria atua como apoio técnico na implementação. A definição das regras de negócio e a validação dos cálculos permanecem sob responsabilidade da instituição.

---

## 💡 Boas Práticas

Antes de disponibilizar uma fórmula em ambiente de produção, recomenda-se:

✅ Validar a regra de negócio com as áreas responsáveis;

✅ Realizar testes em ambiente de homologação;

✅ Conferir se o retorno está no formato esperado pelo banco;

✅ Simular diferentes cenários de cobrança;

✅ Validar os resultados gerados nos arquivos de remessa e nos boletos emitidos.

> **Dica:** Pequenas divergências na fórmula podem impactar diretamente os valores cobrados dos pagadores. Por esse motivo, é recomendável que todas as regras sejam previamente homologadas pela instituição antes da utilização em produção.
