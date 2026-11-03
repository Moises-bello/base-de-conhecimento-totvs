---
article_id: 360028751952
category: RH - Benefícios
content_hash: d1bad689256e84c8ea41810cb2dc97bd60c90dd57d44842a493854a6f73353d4
fetched_at: '2026-06-28T22:44:03.571440+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Calcular desconto do Vale Refeição com Percentual
  do Salário do Funcionário
type: support-article
updated_at: '2025-09-05T17:21:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028751952-RH-Linha-Protheus-GPE-Calcular-desconto-do-Vale-Refei%C3%A7%C3%A3o-com-Percentual-do-Sal%C3%A1rio-do-Funcion%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29532487918231) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como calcular o desconto do Vale Refeição com base em um Percentual do salário do funcionário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**

No Roteiro VRF **não é possível calcular** o desconto do vale refeição com base no percentual do salário. Para esse tipo de cálculo, recomenda-se utilizar a rotina de **Outros Benefícios - Roteiro BEN.**

Para cadastrar e calcular o vale-refeição com base em um percentual do salário do funcionário, siga os passos abaixo:

1. Acesse: **Atualizações** > **Definições** > **Manutenção de Tabelas** > **Tabela S011 (GPEA320)** e cadastre o benefício VR.![](https://centraldeatendimento.totvs.com/hc/article_attachments/34730381260183)  
  
2. Acesse: **Atualizações** >**Benefícios** > **Outros Benefícios** > **Definição de Benefícios (GPEA067)** e defina as regras de cálculo do benefício.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34730376957975)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34730381262743)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34730376960407)

Campos:  
**Cod. Benef.**: Informe o código do benefício.  
**Desc. Benef.**: Informe uma descrição para o benefício.  
**Salário Até**: Informe o valor do limite da faixa de salário.  
**Tipo Ref.**: Informe o tipo de cálculo (Valor Fixo, Percentual Salário ou Percentual Salário Mínimo).  
**Referência**: Informe o valor de referência.  
**Tp Desconto:** Informe qual será a forma de desconto (Percentual sobre o benefício, percentual sobre salário base ou percentual sobre salário mínimo)  
**% Pgto. Func.**: Informe o percentual de pagamento do benefício.  
**% Desc. Funcionário**: Informe o percentual de desconto do funcionário.  
**% Empresa**: Informe o percentual de desconto da empresa.  
**Desc. Mínimo**: Informe o valor do desconto mínimo.  
**Desc. Máximo**: Informe o valor do desconto máximo.  
**Cód. Verba:** Informe o Código da Verba para pagamento do Benefício. Caso o benefício não seja pago em folha, este campo deverá permanecer em branco.  
**Verba Desc.**: Informe o código da verba para desconto do benefício correspondente a parte do funcionário.  
**Verba Empres**: Informe o código da verba, verba tipo “base”, para demonstração do valor do benefício correspondente a parte empresa.  
**Proporc.**: Informe se o valor do benefício deverá ser calculado baseado nos dias trabalhados no mês.  
**Pag. Falta:** Informe se irá apurar o número de faltas para realizar o pagamento ou não do benefício. 

3. Acesse: **Atualizações** > **Benefícios** > **Outros Benefícios** > **Manutenção de Benefícios** **(GPEA065)** e inclua o benefício para os funcionários.![](https://centraldeatendimento.totvs.com/hc/article_attachments/29532519315607)

![](https://i.imgur.com/LdO1Jm1.png)

4. Acesse: **Atualizações** > **Benefícios** > **Outros Benefícios** > **Cálculo** **(GP131CALCA)**e realize o cálculo do benefício.![](https://centraldeatendimento.totvs.com/hc/article_attachments/34730376964503)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29532487946519)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29532519326999)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29532519338903)  
  
5. Acesse: **Atualizações** > **Benefícios** > **Outros Benefícios** > **Relatório de Cálculo (GPER065)**, para imprimir o relatório de conferência.![](https://centraldeatendimento.totvs.com/hc/article_attachments/29532519348631)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29532487964951)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29532519363991)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29532519370263)  
  
  
6. Acesse: **Atualizações** / **Benefícios** / **Outros Benefícios** / **Integração com a Folha** para integrar o Roteiro BEN a folha de pagamento. 

**Saiba Mais**[RH - Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597251-RH-Benef%C3%ADcios)  
[Verificação de faltas no Roteiro BEN](https://tdn.totvs.com/pages/viewpage.action?pageId=729236877)
