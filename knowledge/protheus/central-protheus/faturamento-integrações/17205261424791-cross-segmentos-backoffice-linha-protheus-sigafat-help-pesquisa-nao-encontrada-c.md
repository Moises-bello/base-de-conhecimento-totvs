---
article_id: 17205261424791
category: Faturamento - Integrações
content_hash: 5539e8e646e2a8b30d6f9681e3baf5589bc8939a1fd3ab454c89ea881c5086a4
fetched_at: '2026-06-28T22:38:26.636859+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Help "Pesquisa nao
  encontrada com dados acima" ao integrar
type: support-article
updated_at: '2023-09-01T15:05:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17205261424791-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Help-Pesquisa-nao-encontrada-com-dados-acima-ao-integrar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17205304492567) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Na integração EAI, ao integrar aparece o help "Pesquisa nao encontrada com dados acima", como resolver?  
  
**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**

Esse erro ocorre ao tentar integrar, informando um código que já foi excluído no Protheus.

Exemplo de HELP:

```
{"Error": "Tabela SC5 01/09/23 11:33:14C5_FILIAL := 01C5_NUM := 123458  
-----------Pesquisa nao encontrada com dados acima--------------------
```

Significa que foi informado para integrar com o pedido de dados: C5\_FILIAL = 01 e C5\_NUM = 123458, porém, no Protheus ele não existe/foi excluído.

O sistema verifica tag "InternalId" da integração e percebe que houve uma integração anterior de mesmo dado, então ele entende que tem que alterar, ao tentar alterar, ele não encontra e retorna o erro.

Como resolver:

**Opção 1:**

Incluir o registro pela rotina de inserção pelo Protheus  e depois integrar

Seguindo o exemplo do erro acima:  
Incluir o Pedido de venda "123458" na filial "01' manualmente pela rotina "MATA410" e depois integrar

(OBSERVAÇÃO: No pedido de venda manual, informe todos os campos iguais ao que irá integrar, pois se for feito um pedido de venda manual com o cliente "X" e depois integrar o registro, a integração poder alterar o cliente para "Y" por exemplo, depende dos valores da integração.)

**Opção 2:**Caso seu objetivo na integração seja incluir um novo registro e não alterar um já existe no Protheus, altere a tag "InternalId" da mensagem EAI a partir do sistema origem.

Seguindo o exemplo do erro acima:  
Caso queira incluir um novo pedido de venda, altere a tag "InternalId" a partir do sistema origem (que irá integrar no Protheus), para que a integração não tente passar o valor de pedido de venda "123458"

**Opção 3:**  
Ajuste o License Server da tabela que o erro retornou, certificando que a próxima numeração e nem a próxima da próxima seja a que aparece no erro.

Seguindo o exemplo do erro acima:

Ajuste o License Server na SC5, certificando que a próxima numeração e nem a próxima da próxima seja "123458"
