---
article_id: 360018926292
category: RH - 13º salário
content_hash: 2698ffb2870537f3a17f20ef8e636d39108e013f93fcd28e385f25e7486109aa
fetched_at: '2026-06-28T22:44:00.362400+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE -  Como considerar verbas de valor que incorporam
  ao salário no roteiro FOL para o cálculo do complemento da 2ª parcela do 13º
type: support-article
updated_at: '2026-06-24T19:36:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018926292-RH-Linha-Protheus-GPE-Como-considerar-verbas-de-valor-que-incorporam-ao-sal%C3%A1rio-no-roteiro-FOL-para-o-c%C3%A1lculo-do-complemento-da-2%C2%AA-parcela-do-13%C2%BA
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17959805092887) Tempo aproximado para leitura: 00:03:00 min  
  
Dúvida**Como considerar verbas de valor que incorporam ao salário no roteiro FOL para o cálculo do **complemento/ diferença** da 2ª parcela do 13º?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

É necessário verificar a configuração do mnemônico **P\_INCCOMPL** em **Atualizações>Definição de Cálculo>Mnemônico  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18736397221399)**

Ele permite considerar **verbas de valor que incorporam ao salário no roteiro** **FOL** para o **cálculo do complemento da 2ª parcela do 13º**. Para alterar o conteúdo do mnemônico pesquise pelo mnemônico **P\_INCCOMPL** e clique em **Alterar** e preencha o campo **Conteúdo** que deve ser preenchido com **.F.** (falso) ou **.T.** (verdadeiro). 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18736405802903)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18736397239063)  
  
Caso configurado com **.T.** (verdadeiro) e houver verbas de valor lançadas **(RGB)** no roteiro **FOL** que incorporam ao salário, o sistema utilizará essa incorporação para o cálculo do complemento do 13º salário.

**Exemplo**  
Funcionário com salário base de R$ 1.000,00 e incluída uma verba de comissão no valor de R$ 500,00 no roteiro **FOL**.

Se o mnemônico estiver configurado com **.T.**, o sistema utilizará **R$ 1.500,00** como salário/mês para o cálculo do complemento do 13º salário; dessa forma, verbas que são calculadas sobre o salário incorporado serão calculadas sobre o valor de **R$ 1.500,00**.

Se o mnemônico estiver configurado com **.F.**, o sistema não irá verificar as verbas **lançadas** no roteiro **FOL** e, dessa forma, fará o cálculo sobre o salário de **R$ 1.000,00**.  
  
**Saiba Mais**

[RH - 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)  
**Essas documentações também podem ser acessadas através da Carolina, veja como acessar a assistente virtual, via Protheus ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>**
