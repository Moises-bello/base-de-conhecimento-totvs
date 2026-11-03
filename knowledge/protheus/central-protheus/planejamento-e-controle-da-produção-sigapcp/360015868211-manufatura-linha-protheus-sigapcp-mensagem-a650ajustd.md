---
article_id: 360015868211
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 916b35b8b1564267bb6091646e98157787c09d9aaa3130752f9829ed4f12632c
fetched_at: '2026-06-28T22:42:43.603706+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem A650AJUSTD
type: support-article
updated_at: '2024-08-27T23:57:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015868211-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-A650AJUSTD
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25935644429079)***Tempo aproximado para leitura: **00:02:58 min  
  
Ocorrência**Por que na inclusão ou alteração da **OP** , ao alterar o conteúdo do campo **C2\_DATPRI** ou **C2\_DATPRF** é apresentada a mensagem **A650AJUSTD?**  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - A partir da versão 11.80  
  
**Causa**Essa mensagem é apresentada em algumas situações de acordo com o conteúdo do parâmetro **Calcula Datas Previstas** da rotina **MATA650**.  
Se o parâmetro **Calcula Datas Previstas** tem o conteúdo **Pela Data Início**:  
1. Quando o usuário altera o conteúdo do campo **C2\_DATPRI** é considerando o novo valor deste campo mais o prazo de entrega a data preenchida no campo **C2\_DATPRF** precisa ser alterada para uma data posterior, o Sistema apresenta a mensagem e muda a informação do campo **C2\_DATPRF** para a nova data;  
2. Quando o usuário altera o conteúdo do campo **C2\_DATPRF** porém a data informada neste campo não coincide com **C2\_DATPRI** mais o prazo de entrega o Sistema apresenta a mensagem e corrige o campo **C2\_DATPRF** considerando o conteúdo do campo **C2\_DATPRI** mais o prazo de entrega.  
Se o parâmetro **Calcula Datas Previstas** tem conteúdo **Pela Data Fim**:  
1. Quando o usuário altera o conteúdo do campo **C2\_DATPRF** e o novo valor menos o prazo de entrega é diferente do conteúdo do campo **C2\_DATPRI** o sistema apresenta a mensagem e muda o conteúdo do campo **C2\_DATPRI** considerando **C2\_DATPRF** menos o prazo de entrega;  
2. Quando o usuário altera o conteúdo do campo **C2\_DATPRI** porém essa data é maior do que a calculada pela informação do campo **C2\_DATPRF** menos o prazo de entrega, o Sistema apresenta a mensagem e corrige o campo **C2\_DATPRI** considerando o conteúdo do campo **C2\_DATPRF** menos o prazo de entrega.  
  
**Solução**Reavalie o parâmetro **Calcula Datas Previstas** e também o prazo de entrega do item da **OP.****Glossário  
OP** - Ordem de produção  **MATA650** - Ordens de produção **A650AJUSTD** - As datas previstas foram ajustadas de acordo com o prazo de entrega do produto  **C2\_DATPRI** - Data prevista de início **C2\_DATPRF** - Data prevista de entrega  
  
**Saiba mais**  
Para maiores informações sobre o cálculo do prazo de entrega acesse o link [Manufatura - Linha Protheus - SIGAPCP - Cálculo da previsão de entrega ou previsão inicial de um produto na geração da OP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029130031-Manufatura-Linha-Protheus-SIGAPCP-C%C3%A1lculo-da-previs%C3%A3o-de-entrega-ou-previs%C3%A3o-inicial-de-um-produto-na-gera%C3%A7%C3%A3o-da-OP)
