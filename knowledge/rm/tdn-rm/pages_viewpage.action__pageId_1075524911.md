---
content_hash: f220d672c76701f79b147fb0cc5b31e67e3b0cbac4b88c82e203dafe3df2ed10
fetched_at: '2026-06-29T00:05:54.145119+00:00'
page_id: '1075524911'
product: rm
source: tdn-rm
title: EFD Contribuições - Registros M220/M225 e M620/M625
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1075524911
version: 7
---

# Contexto

A Receita Federal do Brasil publicou a Lei Complementar nº 224/2025 e a Nota Técnica nº 012/2026, estabelecendo novas orientações para a recomposição parcial dos benefícios fiscais relacionados ao PIS e à COFINS.

Conforme a Nota Técnica nº 012/2026, os ajustes de acréscimo decorrentes da redução linear dos benefícios fiscais devem ser informados na EFD-Contribuições por meio dos registros:

* M220/M225 – PIS/Pasep
* M620/M625 – Cofins

Além disso, a legislação determina que os registros de detalhamento (M225 e M625) sejam gerados por documento fiscal, não sendo permitida a consolidação das operações em um único ajuste para o período de apuração.

Esta orientação aplica-se às operações de saída que possuam incidência de PIS e COFINS com os seguintes CSTs:

| CST | Descrição |
| --- | --- |
| 06 | Operação Tributável a Alíquota Zero |
| 07 | Operação Isenta da Contribuição |

Atualmente, o TOTVS Gestão Fiscal não realiza a geração nativa dos registros M220/M225 e M620/M625.

A implementação dessa funcionalidade demandaria uma reestruturação significativa da lógica de apuração da EFD-Contribuições, envolvendo alterações estruturais no processamento fiscal, elevado volume de validações e extensiva cobertura de testes.

Adicionalmente, considerando a descontinuação da obrigação EFD-Contribuições prevista para janeiro de 2027, a rotina correspondente do TOTVS Gestão Fiscal encontra-se em ciclo de manutenção.

Por esse motivo, não estão previstas novas implementações ou evoluções relacionadas à geração automática desses registros.

---

# Alternativa Disponibilizada

Com o objetivo de auxiliar os clientes no cumprimento da obrigação acessória dentro dos prazos legais, será disponibilizado um relatório de apoio através de uma Visão de Dados SmartView que utiliza internamente uma Consulta SQL;.

A solução disponibilizará todas as informações necessárias para preenchimento manual dos registros M220/M225 e M620/M625 diretamente no Programa Validador e Assinador (PVA) da EFD-Contribuições.

O relatório será composto a partir dos Lançamentos Fiscais de Saída.

Serão consideradas exclusivamente as operações que possuam CST de PIS ou COFINS igual a:

* CST 06 – Operação Tributável a Alíquota Zero;
* CST 07 – Operação Isenta da Contribuição.

O relatório retornará os seguintes campos:

### 1. Indicador do Tipo de Ajuste

Valor fixo: **1 – Ajuste de Acréscimo**

### 2. Código do Ajuste

Valor fixo: **11 – Ajuste referente à redução linear dos incentivos e benefícios de natureza tributária, financeira ou creditícia – alíquota zero**

### 3. Data de Referência do Ajuste

Origem: Data de Entrada/Saída do Lançamento Fiscal.

### 4. Data do Lançamento

Origem: Data do Documento Fiscal.

### 5. Número do Documento

Origem: Número do Documento Fiscal.

### 6. CST PIS/COFINS

Origem: CST do tributo informado no item do lançamento fiscal.

### 7. Base de Cálculo

Origem: Base de cálculo do respectivo tributo (PIS ou COFINS).

### 8. Alíquota do PIS

Informada pelo usuário no momento da execução da consulta ou relatório.

Exemplos:

* 1,65%
* 0,65%

### 9. Valor do Ajuste do PIS

Calculado automaticamente pela consulta.

Fórmula: Valor do Ajuste PIS = Base de Cálculo do PIS × Alíquota informada

### 10. Alíquota da COFINS

Informada pelo usuário no momento da execução da consulta ou relatório.

Exemplos:

* 7,60%
* 3,00%

### 11. Valor do Ajuste da COFINS

Calculado automaticamente pela consulta.

Fórmula: Valor do Ajuste COFINS = Base de Cálculo da COFINS × Alíquota informada

### 12. Descrição Resumida do Ajuste

Valor fixo: **Ajuste de Acréscimo**

---

# Utilização das Informações

As informações apresentadas no relatório deverão ser utilizadas pelo contribuinte para inclusão manual dos registros:

* M220 – Ajuste de Acréscimo do PIS;
* M225 – Detalhamento do Ajuste de Acréscimo do PIS;
* M620 – Ajuste de Acréscimo da Cofins;
* M625 – Detalhamento do Ajuste de Acréscimo da Cofins.

A inclusão deverá ser realizada diretamente no Programa Validador e Assinador (PVA) da EFD-Contribuições, observando as orientações previstas na Nota Técnica nº 012/2026.

---

# Como gerar o Relatório

## ✅ Pré-requisito

Importar o Objeto Gerencial, de acordo com a base de dados utilizada

Os dois Objetos Gerenciais estão disponíveis aqui mesmo nesta página!

falsefalse

---

# 🔹 Executar o recurso SmartView

* Após importar o recurso na Visão do SmartView basta executá-lo e informar os parâmetros necessários:

* A Visão de Dados será gerada e pode ser exportada para XLSX, por exemplo, para que seja manipulada

---
