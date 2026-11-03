---
article_id: 28155862452759
category: Cadastros
content_hash: c2f47f90264d0734a81dc59185519b1262d0320c5cbcafac3e375b5ed94c3a24
fetched_at: '2026-06-28T22:46:28.438709+00:00'
product: rm
section_id: 1500000861582
source: central-rm
title: RH - RM - PTO - Criar horário 24x72
type: support-article
updated_at: '2025-01-31T19:54:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28155862452759-RH-RM-PTO-Criar-hor%C3%A1rio-24x72
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28155862438935) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como criar horário com escala 24x72?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - Todas as versões  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Acesse o módulo de **Automação de Ponto** na guia **Cadastros I Horários por Intervalo:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29007426024599)  
  
2. Na tela de cadastro de horários, selecione a opção, **Incluir;**

3. A janela de inclusão de horários será apresentada e defina o **Código do Horário**, **Descrição, Data base** (data de referência) e o **Tipo do Horário**. E informe as demais parametrizações conforme a regra de negócio a ser seguida;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29007442034839)  
  
4. Ao criar uma nova jornada planejada, crie a jornada planejada de 24:00 conforme a hora início desejada, e depois crie 3 índices de descanso:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29007426031639)

**Obs.:** No exemplo acima foi criado no índice 1 uma jornada de 24:00 de 09:00 da manhã do dia 06/01/2025 à 09:00 da manhã do dia 07/01/2025.

Depois no índice 2 o descanso inciando as 09:01 do dia 07/01/2025, depois que a jornada  terminou.

E nos índices 3 e 4 o descanso de de 00:00 às 23:59.

**Saiba mais**

Como complemento de informações de cadastro de horários acesse também a documentação:

[RH - RM - PTO - Horários Automação de](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021943091-RH-RM-PTO-Hor%C3%A1rios-Automa%C3%A7%C3%A3o-de-Ponto#:~:text=11%3A00%20%C3%A0s%2013%3A00,extras%20em%20caso%20de%20atraso.) [Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021943091-RH-RM-PTO-Hor%C3%A1rios-Automa%C3%A7%C3%A3o-de-Ponto#:~:text=11%3A00%20%C3%A0s%2013%3A00,extras%20em%20caso%20de%20atraso.)
