---
article_id: 34523404365207
category: Materiais - Compras (SIGACOM)
content_hash: 969ba77271706e99a3cc68584e5950f7c6cc4228594c52464b3dbea68aeb3874
fetched_at: '2026-06-28T22:41:24.302910+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual o conceito do
  campo Filial de Entrega e parâmetro MV_PCFILEN e sua interferência na numeração
  de Solicitação de Compras ?
type: support-article
updated_at: '2026-02-26T11:47:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34523404365207-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-o-conceito-do-campo-Filial-de-Entrega-e-par%C3%A2metro-MV-PCFILEN-e-sua-interfer%C3%AAncia-na-numera%C3%A7%C3%A3o-de-Solicita%C3%A7%C3%A3o-de-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34523404335127) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Qual o conceito do campo Filial de entrega em conjunto com o parâmetro MV\_PCFILEN e sua interferência na numeração de Solicitação de compras ?  
  
**Ambiente**  
  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus compras - Todas as versões  
  
**Solução**  
Com este recurso, a empresa matriz pode centralizar a colocação das solicitações de compras para todas as filiais, obtendo, desta forma, maior poder de negociação em função do volume da compra, porém, distribuir o controle da previsão de entrada da solicitação, do saldo do pedido, do documento de entrada e do cálculo dos impostos por filial. Para isso, é necessário configurar o parâmetro [MV\_PCFILEN](https://tdn.totvs.com/pages/viewpage.action?pageId=312157906) com **T**, que habilita a informação do campo **Filial de Entrega** na **Solicitação de Compra,** além da numeração sequencial única das solicitações de compras.

* Se a tabela SC1 estiver com o X2\_MODO como **Compartilhado**, o **MV\_PCFILEN** deve obrigatoriamente estar preenchido = T (por empresa) e o controle de numeração da Solicitação de Compras vai ser por empresa, o**C1\_FILENT** ficará em branco e o campo **Filial de Entrega** do cabeçalho da Solicitação de Compras não permitirá digitação;
* Se a tabela SC1 estiver com o X2\_MODO como **Exclusivo** (Padrão do sistema) e o **MV\_PCFILEN** for igual a F, a Solicitação de Compras também não permite a digitação da filial de entrega (assume a filial corrente) e a numeração da solicitação de compras vai ser controlada por filial, neste caso o **C1\_FILENT** será Gravado com a Filial Corrente;
* Já se o SC1 for **Exclusivo** (Padrão do sistema) no X2\_MODO e o **MV\_PCFILENT** for igual a T, a Solicitação de Compras permite a digitação da Filial de Entrega no cabeçalho e o controle da numeração da Solicitação de Compras vai ser por empresa, neste caso o **C1\_FILENT** passará a ser gravado com a filial indicada no cabeçalho a Solicitação de Compras.

***Obs1:***

Abaixo configuração padrão do Inicializador Padrão do campo C1\_NUM:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38602037982871)

|  |
| --- |
| ***Importante:***  • Em caso de qualquer acerto, realizar primeiramente em base de homologação para a devida validação. • Verificar se a sequência desejada para a numeração já não foi utilizada em registros de SC gravados na SC1, pois, caso já esteja em uso ao tentar incluir uma SC será apresentado help sobre inconsistência na numeração. |

***Saiba Mais:***

* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual o conceito do MV\_PCFILEN e sua interferência na numeração do Pedido de Compras?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022158251-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-o-conceito-do-MV-PCFILEN-e-sua-interfer%C3%AAncia-na-numera%C3%A7%C3%A3o-do-Pedido-de-Compras)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
