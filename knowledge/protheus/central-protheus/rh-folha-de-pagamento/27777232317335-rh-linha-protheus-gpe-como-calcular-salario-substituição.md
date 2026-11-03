---
article_id: 27777232317335
category: RH - Folha de Pagamento
content_hash: 04143ca6f00f1c9063743b22d99e1c1b5d79d6d752779333f4f7352264719c75
fetched_at: '2026-06-28T22:44:13.219837+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular Salario Substituição
type: support-article
updated_at: '2025-04-15T14:36:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27777232317335-RH-Linha-Protheus-GPE-Como-calcular-Salario-Substitui%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27777232266135) Tempo aproximado para leitura: **02:00:00 min** **Dúvida**Como calcular Salario Substituição.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.1.2310.  
  
**Solução**Para calcular o Salario Substituição realize os passos abaixo;

**1° passo:**  
Acesse Atualizações > Definições de calculo > Roteiros de calculo > FOL  e habilite a formula de calculo para Salario Substituição.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27777248634135)

**2° passo:**  
Criar uma verba sem ID de calculo para pagamento do Salario Substituição.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27777232272663)

**3° passo:**  
Acesse Atualizações > Funcionários > Período de Substituição.  
Seleciona o funcionário substituto para informar o período e o funcionário a ser substituído.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27777232274583)

4° passo:  
Realize o calculo da folha de pagamento

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27777248641431)

**Cálculo:**Salário diário Empregado substituto: R$ 2.500,00 / 31 = **R$ 80,65**  
Salário diário Empregado substituído: R$ 2.900,00 / 31 = **R$ 93,55**Diferença entre salário diário do substituto e substituído: R$ 80,65 – R$ 93,55 = **R$12,90**Valor a pagar para o substituto: R$ 12,90 \* 4 = 51,60

**Importante**

- Não será permitido o cadastro de mais de uma substituição para o mesmo período e o cálculo será feito SOMENTE se o salário de substituição for maior que o salário do funcionário substituto.  
  
- A divisão do salário para apuração do salário dia, será sempre com base nos dias do período (28, 29, ou seja, não será utilizado o parâmetro MV\_DIASPER para divisão com base em 30 ou quantidade de dias do mês.

**Essas implementações terão efeito apenas após a execução do UPDDISTR para criação da tabela **RUE - Períodos de Substituição** com o pacote de expedição continua do RH liberado a partir de 24/05/2024 para Release igual ou superior a 12.1.2310.**

**Documentação tecnica:**<https://tdn.totvs.com/pages/viewpage.action?pageId=842273181#DTC%C3%A1lculodeSal%C3%A1rioSubstitui%C3%A7%C3%A3o-exemplo1>

**Saiba Mais:**

[RH - Linha Protheus - GPE - Como incluir a Rotina Período de Substituição GPEA946 no Menu](https://centraldeatendimento.totvs.com/hc/pt-br/articles/24138032613015-RH-Linha-Protheus-GPE-Como-incluir-a-Rotina-Per%C3%ADodo-de-Substitui%C3%A7%C3%A3o-GPEA946-no-Menu)

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
