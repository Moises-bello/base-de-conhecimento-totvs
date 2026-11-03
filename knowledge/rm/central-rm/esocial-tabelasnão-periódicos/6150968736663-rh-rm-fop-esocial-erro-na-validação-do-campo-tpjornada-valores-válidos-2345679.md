---
article_id: 6150968736663
category: eSocial - Tabelas/Não Periódicos
content_hash: 0dc5fbf8eec4b2ea370c8184bbc817d7305240fab4dcfcc463d5820c5e061d62
fetched_at: '2026-06-28T22:47:10.441162+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro na validação do campo ''tpJornada'': Valores
  válidos: 2,3,4,5,6,7,9'
type: support-article
updated_at: '2024-06-26T17:48:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6150968736663-RH-RM-FOP-eSocial-Erro-na-valida%C3%A7%C3%A3o-do-campo-tpJornada-Valores-v%C3%A1lidos-2-3-4-5-6-7-9
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao realizar a geração do XML dos eventos S-2200 e/ou S-2206, ocorre o erro: **Erro na validação do campo 'tpJornada': Valores válidos: 2,3,4,5,6,7,9**.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial  - Todas as versões  
  
**Causa**O erro ocorre pois no leiaute S-1.0 foram excluídos alguns tipos de jornada, que eram válidos no leiaute 2.5. Assim, o erro é apresentado quando o campo **Tipo de jornada eSocial**não está com os valores válidos previsto no leiaute S-1.0, sendo eles:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6150274620183/mceclip0.png)

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. No cadastro do funcionário, acesse o menu lateral **Salário/Jornada** e clique no ícone abaixo presente ao lado do campo **Horário**;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6150661285783/mceclip2.png)

2. Selecione o horário do funcionário e clique no ícone de edição;

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6150738096663/mceclip4.png)

3. Acesse a aba **eSocial** e selecione o **Tipo de jornada eSocial** desejada:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6150821180439/mceclip5.png)

4. Gere novamente o XML.  
  
**Importante**  
Para cadastrar o tipo de jornada será necessário considerar:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6150647465495/mceclip1.png)
