---
article_id: 360025734453
category: RH - Rescisão
content_hash: 136e0fe78dc046e6026f2d30e5c6c60fd45bcb46e0676985e50fafa9b668f7c3
fetched_at: '2026-06-28T22:43:50.934296+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Valor do campo 23 não corresponde ao salário do
  funcionário no termo de rescisão
type: support-article
updated_at: '2025-05-07T11:27:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025734453-RH-Linha-Protheus-GPE-Valor-do-campo-23-n%C3%A3o-corresponde-ao-sal%C3%A1rio-do-funcion%C3%A1rio-no-termo-de-rescis%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26398318505239)***Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Valor do campo 23 não corresponde ao salário do funcionário no termo de rescisão. Como realizar a conferência?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) GPE Gestão de Pessoal – A partir da versão 12  
  
**Solução**O campo 23 do termo de rescisão corresponde ao valor da verba vinculada ao identificador 0318 no mês anterior ao cálculo da rescisão. Esse identificador demonstra o valor do salário + adicionais padrões (periculosidade, insalubridade, adicional por tempo de serviço, adicional de transferência e confiança) + todas as verbas configuradas para incorporar salário (RV\_INCORP = S).  
  
Caso o funcionário receba algum valor caracterizado como remuneração, mas a verba não possa estar configurado com Sim para incorpora salário, será necessário incluí-la em um Grupo de Verbas conforme abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042829293)  
  
Após incluir a verba em um Grupo de Verbas, deverá ser informado o código desse grupo na pergunta **Grup. Verb. Comp. Remuneração** que fica localizado na impressão do Termo de Rescisão conforme abaixo:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041988714)  
  
Exemplos de valores que normalmente não incorporam salário, mas que são considerados remuneração: ajuda de custo, as gorjetas, gratificações, participação no lucro e resultados, adicionais, abonos, entre outros.

Concluímos que, o campo 23 apresenta o valor da verba vinculado ao identificador 0318 do mês anterior a rescisão + valores do grupo de verbas informado nos parâmetros de impressão do termo de rescisão.  
  
Para conferência:  
1. Saiba qual o mês de cálculo da rescisão;  
2. Entre atualizações/ definições de cálculo/ verbas. Pesquise o identificador 0318 e anote o código dessa verba;  
3. Entre em consulta/ cadastro/ acumulados e veja qual o valor atribuído a verba anotada no passo anterior. Importante que a parametrização para consulta dessa verba corresponda ao mês anterior a rescisão;  
  
**Saiba mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)

*<http://tdn.totvs.com/pages/releaseview.action?pageId=128681667>*
