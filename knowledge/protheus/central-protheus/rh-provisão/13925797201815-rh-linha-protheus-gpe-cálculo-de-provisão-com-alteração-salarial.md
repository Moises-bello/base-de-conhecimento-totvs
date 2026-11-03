---
article_id: 13925797201815
category: RH - Provisão
content_hash: 1826a6bf7dcd04546006485ff1198fc782968192445f6d0d84b3781a5a93140e
fetched_at: '2026-06-28T22:43:55.672259+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de Provisão com Alteração Salarial
type: support-article
updated_at: '2025-06-18T18:22:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13925797201815-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-Provis%C3%A3o-com-Altera%C3%A7%C3%A3o-Salarial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32903378260887) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como conferir os valores de Provisão de Férias e 13º Salário quando o funcionário teve Alteração Salarial no mês?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**

Quando o funcionário tem uma Alteração Salarial, sendo ela por qualquer motivo (Promoção, Equiparação, Dissídio ...), nos cálculos de provisão será aplicado o ajuste dos valores provisionados considerando o novo salário.

Para realizar a conferência dos valores realizados, siga os passos abaixo:  
  
1. Acesse: Miscelânea / Provisões / Provisões de Férias/13º Salário (GPEA070) , localize o funcionário e clique em Visualizar;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13924253279639)  
Veja que no Cabeçalho das Provisões é apresentado o Salario Atual do funcionário.  
  
2. Acesse: Atualizações / Funcionários / Histórico Salário (GPEA250), localizee o funcionário e clique em Visualizar:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13924466436247)

3. Acesse: Relatórios / Provisões / Provisões de Férias (GPER070) , e preencha os parâmetros para emissão do relatório de provisão:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13924878883991)

Realize as conferências conforme indicado abaixo:  
   
**Anter:** A linha Anterior não deve sofrer alteração do saldo calculado no mês anterior.  
   
**No Mês:** Diferente dos cálculos de provisão onde não há altgeração de salário, neste exemplo, veja que o valor apresentado na linha "No Mês" não é exatamente o valor de 1/12 avo de férias. Esta linha apresenta o ajuste entre o mês Atual e o Mês Anterior.  
Considerando o salário de R$ 2.500,00, 1/12 avo sobre este valor é R$ 208,33, porém com a alteração de salário a linha "No Mês" apresenta o resultado entre o Saldo Anterior e o Saldo Atual.  
Férias Vencidas = 2.500 - 2.000 = **500**  
Férias Proprocionais = 625,00 - 333,33 = **291,67**

**Atual:** Cálculo do valor que o funcionário tem direito no mês de cálculo considerando o novo Salário.

4. A mesma regra é aplicada para conferência ds valores de Provisão de 13º Salário. Acesse: Relatórios / Provisões / Provisões de 13º Salário (GPER090) , e preencha os parâmetros para emissão do relatório de provisão:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13925417156375)

**Saiba Mais**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
