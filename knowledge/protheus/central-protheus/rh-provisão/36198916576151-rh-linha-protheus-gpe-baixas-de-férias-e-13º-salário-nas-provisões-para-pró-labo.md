---
article_id: 36198916576151
category: RH - Provisão
content_hash: 01d84e1e897981814c8e8bbbd9491a5a2ea44ab434244c380ae1b4007f244aaf
fetched_at: '2026-06-28T22:43:56.870043+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Baixas de Férias e 13º Salário nas Provisões para
  Pró-Labores
type: support-article
updated_at: '2025-11-10T12:20:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36198916576151-RH-Linha-Protheus-GPE-Baixas-de-F%C3%A9rias-e-13%C2%BA-Sal%C3%A1rio-nas-Provis%C3%B5es-para-Pr%C3%B3-Labores
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36198916573079) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como Realizar as Baixas de Férias e 13º Salário nas Provisões para Pró-Labores?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**

Por padrão, o Protheus realiza o cálculo de provisões para todos os funcionários, incluindo os Autônomos e Pró-Labores.  
Quando existir um Período Aquisitivo Ativo na rotina Controle de Dias de Direito (tabela SRF), ao calcular as provisões para funcionários com a categoria P, o sistema processará dias de férias para o Pró-Labore.  
Além disso, a provisão de 13º salário será gerada automaticamente sempre que houver cálculo da folha de pagamento, independentemente da categoria do funcionário.

Como o Pró-Labore não possui pagamentos de férias, 13º salário ou rescisão, as baixas não são realizadas automaticamente.

Nesses casos, é necessário efetuar o procedimento manual conforme as opções abaixo.

#### 1. Baixa de Férias

Quando houver necessidade de baixa, altere o período aquisitivo para Pago.

Dessa forma, no cálculo de provisões, o saldo acumulado até o mês anterior será apresentado com valor negativo na linha **"No Mês"**, zerando o **Saldo Atual** e abatendo corretamente o valor provisionado de férias.

Acesse: Atualizações / Funcionários / Controle Dias de Direito (GPEA050), Localize o Pró-Labore e clique em **Alterar**.

Encontre o período aquisitivo desejado e altere o campo Situação (RF\_STATUS) para **3 - Pago**.

O relatório de provisão ficará conforme o exemplo abaixo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36198908623255)

---

#### 

#### 2. Baixa de 13º Salário

Na competência de dezembro, caso não haja pagamento de 13º no roteiro 132, o saldo provisionado até o mês anterior será automaticamente lançado com valor negativo na linha **"No Mês"**, zerando o **Saldo Atual** e abatendo o valor provisionado do 13º salário, como no exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36198916573591)

---

#### 

#### 3. Baixas em Casos de Desligamento

Quando for necessário gerar as verbas de baixa mesmo sem pagamento de rescisão, as verbas de férias e 13º salário podem ser incluídas manualmente nas provisões.

Acesse: Miscelanea / Provisões / Provisões de Férias e 13º Salário (GPEA070), Localize o Pró-Labore e clique em Outras Ações e Alterar.

Clique em Incluir e preencha os dados do cabeçalho (competência, centro de custo, data-base das férias, dias de férias vencidas e proporcionais, Tipo de Movimento, dias de faltas, salário e avos do 13º) e clique em Salvar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36198916573719)

**Importante:** Para o mês de desligamento, o **tipo de movimento** deve ser **1 - Demitido**.

Em seguida, inclua as verbas de Baixas e valores de baixa nos **Itens das Provisões**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36198916573847)

Para saber quais são as verbas para incluir as Baixas de Rescisão [Identificadores de Cálculo de Baixas de Rescisão nas Provisões](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029244891-RH-Linha-Protheus-GPE-Identificadores-de-C%C3%A1lculo-de-Baixas-de-Rescis%C3%A3o-nas-Provis%C3%B5es)

**Saiba Mais:**  
[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
