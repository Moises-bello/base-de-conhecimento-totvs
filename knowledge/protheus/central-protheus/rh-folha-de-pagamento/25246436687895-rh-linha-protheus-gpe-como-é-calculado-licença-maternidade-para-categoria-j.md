---
article_id: 25246436687895
category: RH - Folha de Pagamento
content_hash: 83109e7556a50df77508d0a71f3781a8c80df68298b70d1ebe377874ce38a95f
fetched_at: '2026-06-28T22:44:13.376354+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como é calculado licença maternidade para Categoria
  J?
type: support-article
updated_at: '2025-08-22T19:56:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25246436687895-RH-Linha-Protheus-GPE-Como-%C3%A9-calculado-licen%C3%A7a-maternidade-para-Categoria-J
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25246457234327) Tempo aproximado para leitura: **02:00:00min****Dúvida**Como é calculado licença maternidade para Categoria J?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

**1**. Necessário ter o ID de calculo 0147 atrelado a uma verba.   
**Atualizações > Definições de Cálculos > Verbas**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25246457236247)

**2**. No cadastro do Tipo de Ausência padrão 006 - Licença Maternidade, defina os campos **N.Mes.C.Medias e Cat.Calc.Med****;  
Atualizações > Definições de Calculo > Tipos de Ausências**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25246457238679)

**3**. O calculo para Categoria J deve acontecer através da rotina de Tarefeiro.   
Para parametrização siga as orientações do artigo [RH - Linha Protheus - GPE - Cálculo para tarefeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037394713-RH-Linha-Protheus-GPE-C%C3%A1lculo-para-tarefeiro?source=search)

4. Calculo da Folha

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25246457239959)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25246436654871)

O sistema soma as tarefas executadas no período indicado pela pergunta Taref. Período De/Até para calcular a média.

**Valor da Média = R$ 1.440,56 / 30 \* 22 = R$ 1.056,41**

Nesse exemplo temos definido;   
1 - Verba 387 - Hora Aula definido com S para médias.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25246457245079)

2. Mnemônico P\_MCOMISS = 6  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25246457248535)

3. Mnemônico P\_MEDDIREN = N

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25246457254039)

**Saiba mais**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como utilizar o parâmetro MV\_SALMGRP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037912214-RH-Linha-Protheus-GPE-Como-utilizar-o-par%C3%A2metro-MV-SALMGRP?source=search)

[RH - Linha Protheus - GPE - Contribuição previdenciária patronal sobre o salário-maternidade NT 20/2020.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060446574-RH-Linha-Protheus-GPE-Contribui%C3%A7%C3%A3o-previdenci%C3%A1ria-patronal-sobre-o-sal%C3%A1rio-maternidade-NT-20-2020?source=search)

[RH - Linha Protheus - GPE - Cálculo para tarefeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037394713-RH-Linha-Protheus-GPE-C%C3%A1lculo-para-tarefeiro?source=search)

[RH - Linha Protheus - GPE - Como cadastrar professor categoria J](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051143753-RH-Linha-Protheus-GPE-Como-cadastrar-professor-categoria-J?source=search)
