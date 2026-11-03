---
article_id: 360029297451
category: RH - Provisão
content_hash: 1bf4574d29fd99fc5ba2e9d44e63443614a13c8da433e6bc8d2fca6b763333b4
fetched_at: '2026-06-28T22:43:56.821906+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Relatório de Provisão de Férias
type: support-article
updated_at: '2025-09-22T14:18:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029297451-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-Provis%C3%A3o-de-F%C3%A9rias
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27336253201175) Tempo aproximado para leitura: 00:03:00 min***

**Dúvida**Campos do Relatório de provisão de férias .  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O que corresponde cada campo do relatório de provisão de férias:  
  
1. **Cabeçalho** – São apresentadas as informações como a Data Base do Cálculo (Competência), Filial, Centro de Custo, Nome, Salário, Data Base das Férias, Data de Admissão e Demissão do Funcionário:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27336228641175)

2. **Dias de Férias e Faltas no Período Aquisitivo**: A coluna que fica na lateral esquerda do relatório**,** informa se o cálculo foi realizado para férias à vencer e férias vencidas, e a quantidade de faltas que o funcionário teve no período calculado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27336253206167)  
Observação: A linha em Azul não existe no relatório original, foi utilizada para uma melhor demonstração.  
  
**3. Linhas do Relatório de provisão:**

**Anterior** – Valores de Provisão calculados na competência anterior.  
  
**No Mês** – Será a diferença entre o valor atual e o valor anterior.  
  
**Atual** – Valores que o funcionário tem direito no mês calculado. Será utilizada a data base de férias como referência para o cálculo.  
 **4. Colunas do Relatório de provisão:**

**Valor** –  Serão apresentados os valores de provisão de férias referentes à parte fixa (salário bruto);  
   
**Adicionais** – Serão apresentados os valores variáveis como médias de horas extras, comissões, bonificações e gratificações, somados aos adicionais por tempo de serviço, periculosidade, Insalubridade, adicional de confiança ou transferência.  
  
**1/3 Constit.** – Sistema soma as colunas "Valor" e "Adicionais", divide por 3 (1/3)**,**e apresentará o resultado na coluna em questão.

**Total de Férias** –  Soma das três colunas anteriores (Valor + Adicionais + 1/3 Constit.).

**INSS** – Apresentará o Total das Férias x o percentual de INSS Patronal (Soma dos percentuais definidos nas tabelas S037 e S038, nos campos "% empresa", "% Acidente de trabalho" e "% Terceiros e Desoneração, quando houver").

**FGTS** – Percentual que consta no campo % FGTS da Tabela S037.

**Total encargos** – Soma das duas ultimas colunas (INSS + FGTS).

**Total Geral** – Soma das colunas que apresentam os totais (Total Férias + Total Encargos).

**5. Relatório de Provisão de Férias - Totalizador**

Ao final do relatório de provisão de férias, será exibido o Totalizador com os valores referentes à Filial e/ou Grupo de Empresas.

A linha **"No Mês Baixas"** apresentará o ajuste da provisão referente ao mês, considerando o saldo do mês subtraído das baixas da mesma competência.

No exemplo abaixo, a linha **"No Mês Baixas"** será calculada da seguinte forma:

Saldo do mês - Valor Baixas Férias - Valor Baixas Transferências de Saída

**Memória de cálculo da coluna Valor:**  
21.239,92 - 18.996,33 - 18.132,98 = -15.889,39

A mesma regra deve ser aplicada para conferência das demais colunas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35110609016727)

**Observação:** Quando houver baixas por rescisão, estas também deverão ser consideradas no cálculo.

**Saiba Mais:**

[RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o) **[-](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)** [Pr](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)[ovisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)

[Manual](https://tdn.totvs.com/pages/releaseview.action?pageId=754967312) [das](https://tdn.totvs.com/pages/releaseview.action?pageId=754967312) [Provisões](https://tdn.totvs.com/pages/releaseview.action?pageId=754967312)
