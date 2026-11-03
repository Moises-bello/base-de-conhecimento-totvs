---
article_id: 1500002572321
category: SIGAEST - CUSTOS
content_hash: 4fe2a7f6b1d5dc5154f2f7a594809e74582634caee66cb9840e18dc920883876
fetched_at: '2026-06-28T22:39:02.446027+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - SIGAEST - MATA330/MATA331 -
  HELP CTGNOCAD
type: support-article
updated_at: '2025-03-12T11:41:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002572321-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAEST-MATA330-MATA331-HELP-CTGNOCAD
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30504171732119)** Tempo aproximado para leitura: **00:01:40 min**

**Dúvida**Ao executar o Recálculo do Custo Médio (MATA330) ou Contabilização do Custo Médio (MATA331), ocorre o HELP CTGNOCAD. Como resolver para que seja processado as rotinas sem erro?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAEST - A partir da versão 12.1.17

**Solução**Para resolver, siga os passos abaixo:

1º - Acesse ao módulo de **34 - SIGACTB -** **Contabilidade Gerencial**;

2° - Caso não tenha o Calendário cadastrado, acesse em **Cadastros -> Calendário Contábil** **(CTBA010)**, Incluindo e preenchendo as informações conforme a sua regra contábil;

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101376374)**

3º - **Cadastros** > **Moedas X Calendários (CTBA200);**

4º - Efetue a amarração da **Moeda** com o **Calendário** **Contábil.**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002489562)**

Após efetuar os cadastros, efetue novamente o processo que ocasionou o HELP para concluir o seu processamento.

Este HELP é causado devido à falta de amarração da moeda com o calendário contábil. Normalmente ocorrem em períodos de começo de ano, quando o usuário acaba esquecendo de cadastrar o novo Calendário Contábil.

**Caso a empresa não tenha acesso ao Módulo 34 - Contabilidade Gerencial**

Para evitar que ocorra o HELP, no Recálculo do Custo Médio parametrize a pergunta "Gerar Lançamento Contábil?" = "Mantém Lançamento"

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103542853)

Assim também não gerará o HELP, entretanto não tera contabilização das movimentações.

**Saiba mais:**

* [Mensagem CTGNOCAD no Recálculo do Custo Médio / Contabilização](https://tdn.totvs.com/x/GeAKDg)
* [*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)
