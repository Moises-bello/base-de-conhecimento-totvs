---
article_id: 360007117092
category: Anuais
content_hash: 6e78fa88d97e7a86e46c166a0cff362bd4abf85df6528317299c5256a6734894
fetched_at: '2026-06-28T22:46:51.234552+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: RH - RM - FOP - DIRF/Informe de Rendimentos: Ficha Financeira divergente do
  movimento de Pensão
type: support-article
updated_at: '2025-01-21T19:43:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007117092-RH-RM-FOP-DIRF-Informe-de-Rendimentos-Ficha-Financeira-divergente-do-movimento-de-Pens%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:02:00 min****Dúvida**  
Quando na geração da DIRF surge mensagem de divergência entre a ficha financeira e a movimentação de pensão dos dependentes, como fazer para corrigir? Veja a mensagem abaixo:  
  
*Erros encontrados para a chapa: 00001 - ITAMAR MENDES DA SILVEIRA*  
 *- O valor do evento 0013 com data de pagamento em 28/02/2018 na ficha financeira está divergente do movimento de pensão dos dependentes. Necessário realizar o ajuste dos valores no anexo **movimentação da pensão de dependentes!***  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para solucionar essa dúvida, realize os passos a seguir:  
  
1. Acesse o menu **Administração de Pessoal | Funcionários**, edite o funcionário com a mensagem de erro e acesse **Anexos | Folha de Pagamento | Dependentes**;  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10985579533335)

02. Acesse o cadastro do dependente, clique em **Anexos | Movimentação da Pensão dos Dependentes** e depois acesse a movimentação de acordo com a competência que estiver ocorrendo a mensagem de erro, conforme a data de pagamento;  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10985722979991)

03. Na tela que será aberta todos os campos deverão ser verificados em busca do erro **mês de competência, mês caixa, período, valor e o tipo de movimento**. No caso do tipo de movimento para cada tipo específico o sistema valida o código de calculo, conforme abaixo:  
  
Tipo 0 - Movimento - Código de cálculo 13.  
Tipo 1 - Férias - Código de cálculo 113 **lembrando que o caixa, será de acordo com o pagamento das férias e não da folha.**  
Tipo 5 - Diferença de Férias - Código de cálculo 197.

**Saiba mais**Abaixo segue os códigos de cálculos para cada tipo de movimento e lançamento referente a pensão que o sistema valida.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12434369184535)  
  
**Importante**  
Quando a pensão alimentícia é calculada pelo código de cálculo 53, Pensão Alimentícia Judicial Informada **Folha**, o sistema não alimenta o histórico **Movimento da Pensão** e por isso o usuário terá que inserir os valores manualmente.
