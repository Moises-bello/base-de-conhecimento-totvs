---
article_id: 4417430118551
category: Faturamento - Integrações
content_hash: 6feff2d769084177cb17a87290e203949b73f352bbe9cee90229b7d4be643cca
fetched_at: '2026-06-28T22:38:26.384390+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ajuda: Regnois
  - Não existe registro relacionado a chave informada no alias SE4, ordenação 1'
type: support-article
updated_at: '2021-12-29T14:03:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417430118551-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ajuda-Regnois-N%C3%A3o-existe-registro-relacionado-a-chave-informada-no-alias-SE4-ordena%C3%A7%C3%A3o-1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao efetuar  a importação do XML pelo Importador XML é gerado o registro no arquivo deliveryxml\_salesorder: **Ajuda: Regnois - Não existe registro relacionado a chave informada no alias SE4, ordenação 1.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417441514903/mceclip0.png)  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat -a partir do release 12.1.25.  
  
**Causa**O problema ocorre por que o XML está indicando uma determinada condição de pagamento e a mesma não existe no cadastro de condições de pagamento (SE4), no índice 1 que é Filial+código.

Neste exemplo, veja que tag de condição de pagamento "**conditionpay**", está sendo apontado a condição 001 e vejam que no arquivo **deliveryxml\_salesorder**, indica justamente que a informação de condição de pagamento 001 que está inválida, facilitando na análise do problema, se é o caso de criação da condição ou o ajuste do XML para a condição correta:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417441559703/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417429929367/mceclip2.png)  
  
**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:  
**1.** Verifique a condição de pagamento que o **XML** está tentando integrar e certifique-se que a mesma existe no cadastro de condição de pagamento (**SE4**);

**2.** Caso não exista a condição indicada, crie a condição de pagamento (**MATA360**) e posteriormente, efetue a atualização da tarefa schedule para que o sistema processo o XML para integração do pedido de venda (**Mata411**);

**3.** Caso a informação da condição de pagamento esteja incorreta no XML, ajuste a tag  **conditionpay** para o código da condição de pagamento correta, e posteriormente efetue a atualização da tarefa schedule para que o sistema leia o XML novamente, processando a integração.

**Obs. as divergências de integração do pedido serão geradas nos arquivos Order e deliveryxml\_salesorder dentro da pasta XML, criada na pasta System.**
