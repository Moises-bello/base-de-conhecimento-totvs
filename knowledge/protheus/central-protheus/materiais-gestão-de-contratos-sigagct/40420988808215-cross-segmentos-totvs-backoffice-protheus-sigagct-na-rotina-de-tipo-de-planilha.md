---
article_id: 40420988808215
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 0e0685ce7eb470f44fe64347c11d2216e73eb8c61a95b4202ab0732f7c41ed66
fetched_at: '2026-06-28T22:37:23.930423+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Na rotina de Tipo
  de Planilha (CNTA230) ocorre o erro " CNA010: SetOrder - Index not found. on CN230ALCMD(CNTA230.PRW)
  "'
type: support-article
updated_at: '2026-05-12T19:25:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40420988808215-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Na-rotina-de-Tipo-de-Planilha-CNTA230-ocorre-o-erro-CNA010-SetOrder-Index-not-found-on-CN230ALCMD-CNTA230-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40420988781335) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**

Ao acessar a rotina de Tipo de Planilha (CNTA230) para inclusão, ocorre o erro " CNA010: SetOrder - Index not found. on CN230ALCMD(CNTA230.PRW) "

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

As ocorrências mapeadas deste erro na rotina de Tipos de Planilha (CNTA230) com retorno positivos de solução dos mesmo, normalmente estão relacionados a um ou mais dos pontos abaixo, que orienta-se a verificação e análise no ambiente em que ocorre:

1. A não existência no ambiente em questão, de todos os índices padrões da tabela CNA,

2. A ordem dos campos da tabela CNL conforme o padrão

3. Campo CNL\_ALCMED estar com as configurações e ordem corretas na tabela CNL:

Dessa forma orienta-se a realização da checagem dos 3 pontos, (**principalmente a existência de todos os índices conforme os padrões da tabela CNA**) conforme as imagens padrões enviadas abaixo, visto termos tido retornos positivos da não mais ocorrência após os ajustes realizados:

1. Realizar a verificação nos índices da tabela CNA, se no ambiente em questão existem os índices e se eles estão conforme o padrão da imagem abaixo, e se não existe nenhum índice diferente, onde caso haja divergência orientamos realizar um backup em ambiente de homologação e ajuste para deixar conforme padrão da imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40420956443031)

2. Caso ainda assim persista, verificar o campo CNL\_ALCMED que é um campo de ordem fixa obrigatória. Verificar se está conforme padrão, se não realize um ajuste em ambiente de teste com backup para validação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40420956443927)

3. Se ainda persistir, verificar se o campo CNL\_ALCMED está conforme ambiente padrão segue telas abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40420988783895)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40420956448279)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40420988786071)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40420988787479)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40420956451735)

***Saiba Mais:***

[Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
