---
article_id: 360025027553
category: RH - Provisão
content_hash: d2846dddd60dd402b1645523114b170639fc4f40b5aba7f038a13eb16b0fed35
fetched_at: '2026-06-28T22:43:55.782240+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como Conferir os Relatórios de Provisão com Transferência
type: support-article
updated_at: '2025-06-17T19:44:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025027553-RH-Linha-Protheus-GPE-Como-Conferir-os-Relat%C3%B3rios-de-Provis%C3%A3o-com-Transfer%C3%AAncia
---

**Dúvida**Como Conferir os Relatórios de Provisão com Transferência?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**O parâmetro **MV\_TRFAMES** indica o Ano/Mês (deve ser preenchido no formato AAAAMM) inicial de utilização, na demonstração das transferências na **Provisão**.  
  
Exemplo : Funcionário com Transferência entre Centros de Custos em 01/09/2023.

Independente do preenchimento do parâmetro MV\_TRFAMES, ao consultar o Acumulado de Provisões (GPEA070), no mês da transferência serão apresentadas duas linhas com o cálculo de provisão.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20861345551127)

O movimento 5, refere-se à Baixas de Transferências, e será calculada para o Centro de Custo Origem.  
O movimento 6, refere-se à Entrada do saldo de Transferência, e será calcula para o Centro de Custo Destino.

Relatório de Provisão com o Parâmetro Em Branco:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20861372940567)

No Relatório de Provisão do Centro de Custo, Empresa ou Filial de Origem, os valores provisionados até o mês anterior são apresentados como Baixa de Transferência, zerando o Saldo Atual para este Centro de Custo, Empresa ou Filial .  
No Centro de Custo, Empresa ou Filial de Destino, o Protheus provisiona todos os avos de direito do funcionário. Todo o direito que o funcionário tem será provisionado de uma só vez, na linha **"No Mês"** e a partir do mês seguinte passará a calcular com informações na linha **"Anterior"**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20861372956183)

Relatório de Provisão com o Parâmetro Preenchido:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20861345620503)  
  
No Relatório de Provisão do Centro de Custo, Empresa ou Filial de Origem, os valores provisionados até o mês anterior são baixados na linha "**Transf. Sld. Saída**", zerando o Saldo Atual para este Centro de Custo, Empresa ou Filial.  
No Centro de Custo, Empresa ou Filial de Destino, os os valores de Provisão serão apresentados na linha "**Transf. Sld. Entr**" para que o Saldo baixado na movimentação seja provisionado no novo Centro de Custo, Empresa ou Filial do funcionário:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20861345637911)

**Saiba Mais:**

[Provisão com Transferência](https://tdn.totvs.com/pages/releaseview.action?pageId=233744464)   
[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
