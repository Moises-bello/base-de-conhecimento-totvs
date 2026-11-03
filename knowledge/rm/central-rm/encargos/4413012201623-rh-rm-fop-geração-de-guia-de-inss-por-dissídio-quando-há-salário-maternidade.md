---
article_id: 4413012201623
category: Encargos
content_hash: 93fe68cd240b83b63edd08ebf1c6f77735e05d631f2fb644d68a4e68b9be0c34
fetched_at: '2026-06-28T22:46:53.220313+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Geração de Guia de INSS por Dissídio quando há Salário Maternidade
type: support-article
updated_at: '2025-03-13T11:17:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413012201623-RH-RM-FOP-Gera%C3%A7%C3%A3o-de-Guia-de-INSS-por-Diss%C3%ADdio-quando-h%C3%A1-Sal%C3%A1rio-Maternidade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:20 min****Ocorrência**  
 Ao gerar a guia de INSS por dissidio de diferença salarial, o sistema não esta deduzindo a parte patronal sobre o evento Salário Maternidade.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa** O que ocorre é que a SEFIP não está preparada para receber a dedução da diferença de salário licença-maternidade para o recolhimento 650. Portanto o sistema não lança a dedução de Salário Maternidade, atualmente o sistema segue o layout da SEFIP. Para a SEFIP, existe diferença de salário que é recolhida na SEFIP 650, mas a SEFIP 650 não trata a **diferença salarial de licença de salário maternidade**.

Se considerar o Código de Cálculo 17 para o cálculo de diferença salário maternidade, o sistema irá recalcular a licença-maternidade alterando o valor do evento de diferença conforme o histórico de afastamento encontrado. No sistema, quando é informado um evento para lançar o valor de diferença de licença Maternidade e o evento original é o 17, o sistema não permite informar um evento com o mesmo código de cálculo. No momento do cadastro para que não ocorra esse recálculo o sistema retorna uma mensagem para o usuário.  
  
**Importante**O sistema não impede a criação do evento, mas o evento não é recalculado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414532248343/mceclip0.png)

**Solução**  
Para ajustar a guia de INSS com a dedução, no momento da geração do lançamento financeiro, poderá alterar o valor da diferença do salario maternidade no campo de compensação. Quanto ao valor da diferença, deverá  informar manualmente na SEFIP no campo compensação, que pode ter outros valores de controle da empresa.

Atualmente no sistema, para que este campo na SEFIP seja preenchido de forma automática, o mesmo pode utilizar o recurso de **Parâmetros INSS/FGTS,**para mais informações **acesse o link** [SEFIP .Net.](https://tdn.totvs.com/display/public/LRM/SEFIP+.Net)  
Outro recurso disponibilizado, foi a criação de um campo na Folha Analítica por Dissídio, onde retorna o Valor da Base de diferença de Maternidade, que irá ajudar a apurar o valor para ser informado na SEFIP e Guia de INSS, para mais informações **acesse o link [DT-Folha Analítica por Dissídio - Diferença Licença Maternidade.](https://tdn.totvs.com/pages/releaseview.action?pageId=578626292)**

**Caso o campo não esteja disponível será necessário atualizar o relatório, além de estar em alguma versão de mercado.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414581373079/mceclip1.png)

**Importante**Para o eSocial hoje já é tratado a dedução, pois o mesmo não tem esta limitação da SEFIP e busca a informação da tabela de verbas geradas por diferença, que tem o evento com o Código de Cálculo original, fazendo a dedução sem necessidade de intervenção do usuário.

Após alterar a guia de INSS, não se deve Recalcular Valores da Guia.  
  
**Saiba mais****[Guia de INSS por Dissídio](https://tdn.totvs.com/pages/releaseview.action?pageId=351020560)****[COMO FAZER - Diferença Salarial e SEFIP por Dissídio](https://tdn.totvs.com/pages/releaseview.action?pageId=126714055)**
