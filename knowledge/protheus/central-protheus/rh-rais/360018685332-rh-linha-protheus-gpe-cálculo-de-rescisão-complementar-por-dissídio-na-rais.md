---
article_id: 360018685332
category: RH - RAIS
content_hash: e03fb8e454344d6c0481b9b70827cfdd267d66b613e99baded5a7ee29adc23d0
fetched_at: '2026-06-28T22:44:05.660063+00:00'
product: protheus
section_id: 360000030327
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de rescisão complementar por dissídio na
  RAIS
type: support-article
updated_at: '2025-09-09T14:17:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018685332-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-rescis%C3%A3o-complementar-por-diss%C3%ADdio-na-RAIS
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34808167697559) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**No cálculo de uma rescisão complementar por dissídio como faço para que o sistema identifique os valores de **dissídio** e sua referência de meses, apresentando os valores nas colunas **Acréscimo Salarial** e **Meses Ref. Acréscimo**?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 11.80  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Data base do dissídio – Atualizações > Cadastros > Sindicatos:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014623891)

2. Cálculo da rescisão original - Miscelânea > Cálculo > Rescisão > Visualizar:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014623951)

3. Cálculo do dissídio retroativo - Miscelânea > Reajuste > Dissídio Retroativo:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014602532)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014602612)

Como o funcionário está demitido, esses valores são gerados na rotina de valores futuros - Atualizações > Lançamentos > Valores futuros:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014602812)

4. Atualização do histórico salarial - Atualizações > Funcionários > Histórico salário:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014624511)

5. Cálculo da rescisão complementar - Miscelânea > Cálculo > Rescisão

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014624791)

6. Geração da RAIS - Miscelânea > RAIS > Geração Arquivo:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014625011)

Manutenção do arquivo:

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014625091)

O sistema identifica e demonstra o valor dentro da coluna Acréscimo Salarial a partir da configuração de verba - identificador 0341:

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014625411)

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014625451)

A quantidade de meses é identificada a partir do número de ocorrências da verba dentro da tabela RHH:

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014603452)

**Saiba mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
