---
article_id: 12096839964311
category: Encargos
content_hash: 8d55a97a2b00ab5a9f5ba6269dcc62d0e77c40bbb6a0dda42d1b9ad00f378ac2
fetched_at: '2026-06-28T22:46:52.358459+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Código da Filial Contábil
type: support-article
updated_at: '2025-05-07T19:29:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12096839964311-RH-RM-FOP-C%C3%B3digo-da-Filial-Cont%C3%A1bil
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**No módulo Folha de Pagamento, ao gerar a contabilização de encargos ocorre o erro: **O código da filial não foi informado, não é permitido incluir partida sem filial.****Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**O erro está associado a falta da filial contábil no cadastro do Agrupamento de Contas Contábeis, seção ou centro de custo utilizado.  
  
**Solução**

É necessário verificar em qual local o código da filial esta preenchido, e assim conferir se existe alguma parametrização que não contém a filial informada.  
  
Primeiro acesse: **Encargos | Cadastros | Cadastros Contábeis | Agrupamento de contas**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12098192880407)**

Verificar se a filial consta no cadastro das contas contábeis, ou seja nos Agrupamentos Contábeis, pois mesmo que tenha informação na seção ou no Centro de Custo, irá retornar a filial da conta contábil.  
  
![](https://totvssuporte.zendesk.com/attachments/token/BqhEyagP0CIoZkoEMcYxlJDfH/?name=image.png)  
  
Se a empresa trabalhar com centro de custo, o sistema irá retornar a filial do centro de custo, mesmo tendo informação nas seções. Para acessar o centro de custo, acesse: **Administração de Pessoal | Centro de Custo.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12098229352855)  
  
![](https://totvssuporte.zendesk.com/attachments/token/A5bB2JVFS7NoiMAjUd0CB1dhE/?name=image.png)

**Importante**  
Para que o sistema reconheça a filial da seção, a empresa não poderá trabalhar com centro de custo no cadastro do funcionário e nem poderá ter filial no cadastro das contas contábeis, onde irá retornar o centro de custo da seção. O cadastro de seção esta localizado em: **Administração de Pessoal | Seções**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12098275677335)  
  
![](https://totvssuporte.zendesk.com/attachments/token/m3wS3IttsjvFgeVZoBRzpnGTz/?name=image.png)
