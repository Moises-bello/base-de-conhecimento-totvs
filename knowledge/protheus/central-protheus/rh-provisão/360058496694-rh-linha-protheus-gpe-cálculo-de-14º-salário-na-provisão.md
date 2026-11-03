---
article_id: 360058496694
category: RH - Provisão
content_hash: d56985f29c82d5aab528112b97b137da36f4c3387d443ec57176544eb63b3b1e
fetched_at: '2026-06-28T22:43:55.664445+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de 14º Salário na Provisão
type: support-article
updated_at: '2025-06-17T20:31:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058496694-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-14%C2%BA-Sal%C3%A1rio-na-Provis%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32881423646999)** Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como calcular o 14º salário na provisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Para calcular a **provisão de 14º salário** deverá realizar os seguintes procedimentos:  
  
1. Verifique se existem verbas cadastradas com **tipo Base Provento** atrelados aos identificadores de cálculo abaixo:  
  
**Provisão de 14º Salário:**  
0142 - Provisão 14º Salário  
0143 - INSS Provisão 14º Salário  
0144 - FGTS Provisão 14º Salário  
0278 - Adicional Provisão de 14º Salário  
  
**Baixas:**  
1666 - Baixa Provisão 14o Salário  
1667 - Baixa Adicionais Provisão 14o Salário  
1668 - Baixa Antecipação 1a Parcela 14o Salário  
1669 - Baixa INSS Provisão 14o Salário  
1670 - Baixa FGTS Provisão 14o Salário

**Transferência:**0280-Baixa Provisão 14ºSalário Transferido  
0281-Baixa Adicional Provisão de 14º Salário Transferido   
0282-Baixa INSS Provisão 14º Salário Transferido   
0283-Baixa FGTS Provisão 14º Salário Transferido

**PIS Sobre Folha:**0426 - PIS Provisão 14º Salário  
1671 - Baixa PIS Provisão 14o Salário.

2. O provisionamento será realizado através da pergunta **"índice 14º salário"**. Neste exemplo vamos preencher o percentual com **100,000**.

A caixa abaixo é apresentada nos parâmetros que são preenchidos para o cálculo de provisão.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000023741)

3. O valor é provisionado mês a mês e tem como base o valor do 13º Salário. Logo, se na pergunta "Índice 14º Salário" estiver configurado com 100,00 (100%), o 14º salário será que uma cópia do 13º.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17382684738455)

4. Os Valores de 14º Salário serão apresentados no Relatório de Provisão de 13º Salário:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17382780786583)

5. Caso a pergunta **"Desc. 1a Parc. 13o Sal"** esteja configurado com **SIM**, ao calcular a provisão do 13º salário é gerada a verba **id 0268**. Essa mesma verba será gerada para o 14o Salário. Caso o cliente entenda que essa deva gerar a verba para o 13o, mas não para o 14o, poderá modificar os valores através dos pontos de entrada que foram disponibilizados para a rotina.

Haverão 2 (dois) pontos de entrada (PE), onde será possível modificar, de acordo com a necessidade de cada cliente, tanto o valor provisionado quanto o valor baixado.

4.1 - **PE GP090F13** → permite modificar os valores de provisão mensal de 13º e/ou 14º Salário. → Link da documentação: [http://tdn.totvs.com/x/yw0rGw](https://tdn.totvs.com/x/yw0rGw)

4.2 - **PE GP090B13** → permite modificar os valores de baixa do 13º e/ou 14º Salário. → Link da documentação: [http://tdn.totvs.com/x/oQwrGw](https://tdn.totvs.com/x/oQwrGw)

5. **Provisão rateada** não está contemplada nessa melhoria.

**Saiba Mais:**  
<https://tdn.totvs.com/pages/viewpage.action?pageId=455806039>
