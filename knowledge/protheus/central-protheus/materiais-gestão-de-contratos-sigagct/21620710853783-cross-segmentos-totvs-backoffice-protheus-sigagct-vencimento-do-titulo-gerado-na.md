---
article_id: 21620710853783
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 4fad9f75881eb0439db2053aede14534e8f84d03b0258e25fa7b164971ab16be
fetched_at: '2026-06-28T22:37:24.198918+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Vencimento do Titulo
  gerado na Medição não respeira Condição de Pagamento do Contrato '
type: support-article
updated_at: '2024-09-05T15:15:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21620710853783-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Vencimento-do-Titulo-gerado-na-Medi%C3%A7%C3%A3o-n%C3%A3o-respeira-Condi%C3%A7%C3%A3o-de-Pagamento-do-Contrato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21620758351511) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**

Vencimento do Titulo Gerado na Medição não respeita Condição de Pagamento do Contrato

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

Por Padrão do sistema, a condição de pagamento utilizada no cadastro do contrato, tem a funcionalidade apenas para ser levada para o Pedido de Compras ou de Venda gerado na medição, quando a medição gera pedido no seu encerramento, não tendo influência quando a medição gera Título Financeiro.

Quando na medição do contrato for gerado Título Financeiro, a condição de pagamento não é considerada, sendo o vencimento do titulo gerado funcionando da seguinte forma:

- Caso no contrato haja Cronograma Financeiro, o vencimento do titulo gerado irá seguir conforme o vencimento da parcela do cronograma financeiro do contrato.

- Caso o contrato for cadastrado com configuração sem Cronograma Financeiro no contrato, o vencimento do titulo é gerado conforme data da emissão do título, que é a data em que a medição for encerrada.  
  
Este se trata da forma como o sistema padrão trabalha, não havendo uma configuração para que realize de forma diferente quanto ao vencimento do título gerado na medição.  
  
Caso se deseje, para alterar informações do título no financeiro no encerramento da Medição pode-se fazer uso do ***ponto de entrada** **CN121AFN (CNTA121)*** que permite esta mudança:

[DT\_PE\_CN121AFN\_Altera informações do título financeiro no encerramento da medição](https://tdn.totvs.com/pages/viewpage.action?pageId=578632647)

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Existe uma forma de alterar a data de vencimento do titulo Financeiro ao ser gerado na Medição do Contrato ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7803297961239-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Existe-uma-forma-de-alterar-a-data-de-vencimento-do-titulo-Financeiro-ao-ser-gerado-na-Medi%C3%A7%C3%A3o-do-Contrato)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Pontos de entrada para rotina de Medição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022685112-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Pontos-de-entrada-para-rotina-de-Medi%C3%A7%C3%A3o?source=search)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
