---
article_id: 38943888801175
category: Meu RH - Instalação, configuração, qrcode, permissões e erros
content_hash: 816b35011cdd8e85b63eafe6df57dc532e2c920cc9597b71c6e5326e2c653f2c
fetched_at: '2026-06-28T22:47:29.436037+00:00'
product: rm
section_id: 1500000961062
source: central-rm
title: RH - RM - Meu RH - Como utilizar Formula Visual no Meu RH?
type: support-article
updated_at: '2026-03-11T17:36:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38943888801175-RH-RM-Meu-RH-Como-utilizar-Formula-Visual-no-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38943888784663) Tempo aproximado para leitura: **00:02:45 min**  
  
**Dúvida**  
Como utilizar Formula Visual no aplicativo Meu RH?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH – Todas as versões  
  
**Solução**  
O Meu RH possibilita a utilização de **Fórmulas Visuais**. No entanto, é importante destacar que essas fórmulas não são executadas diretamente no aplicativo Meu RH, mas sim no back-office RM. Dessa forma, para que uma regra configurada em **Fórmula Visual** seja aplicada nas ações realizadas no aplicativo, é necessário **vincular o gatilho da fórmula ao DataServer correspondente à rotina utilizada pelo Meu RH**.

A seguir demonstramos um exemplo de utilização de Fórmula Visual no Meu RH para validação do abono pecuniário em solicitações de férias.

Primeiramente, acesse a aba “**Gatilhos**” da Fórmula Visual e inclua uma ação, como por exemplo **“Após salvar o registro**”. No campo “**Localizar**”, informe o nome do **DataServer** relacionado à rotina que será executada no aplicativo. Neste exemplo será utilizado o **FopPFUFeriasPerDATA**, que corresponde à rotina de férias.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38943856651927)

Em seguida, na coluna **“Tipo”**, selecione a opção de validação desejada, iremos utilizar a  **“Ativado com Exceções”.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38943888785559)

A regra desta formula exemplo, foi criada para impedir o registro das férias no Meu RH quando a quantidade de dias de abono pecuniário informada for diferente de 0 ou 10 dias.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38943856653335)

Após realizar essa configuração da Formula Visual, ao tentar efetuar a **solicitação de férias no Meu RH** informando uma quantidade de **dias de abono pecuniário** que não esteja de acordo com a **regra declarativa**, a **exceção da fórmula será acionada**, impedindo o registro da solicitação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38943856654231)

Para baixar este formula exemplo e consultar o passo a passo detalhado sobre sua criação, [clique aqui.](https://drive.google.com/drive/folders/1LTfMQnF9ZK6l57rG-qUdkwxKmXpazZNc?usp=sharing)

Para consultar as documentações disponíveis sobre Formula Visual, [clique aqui.](http://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000863022-F%C3%B3rmula-Visual?page=1#articles)

**Importante:** Nosso suporte padrão não abrange a criação de Formula Visual, esta documentação serve apenas como guia. Portanto, caso necessite de apoio este tipo de serviço poderá solicitar através da consultoria tarifada.
