---
article_id: 4413008256279
category: Folha Mensal
content_hash: 00a6e0c2f8afcb83128efbfe83fe2681e2cd89203475be056826fa7689aeac05
fetched_at: '2026-06-28T22:46:59.340772+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Retificação da folha de pagamento de meses anteriores
type: support-article
updated_at: '2024-10-04T18:54:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413008256279-RH-RM-FOP-Retifica%C3%A7%C3%A3o-da-folha-de-pagamento-de-meses-anteriores
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26845055826071) Tempo aproximado para leitura: **00:04:21 min****Dúvida**Como gerar retificação de folha de pagamento de meses anteriores?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para realizar a retificação da folha de pagamento é necessário que as parametrizações estejam ativas e corretas.  
  
Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Acesse: o menu **Serviços Globais | Segurança | Perfis**. Logo, com o sistema Folha de pagamento selecionado, edite o perfil desejado, vá em acesso aos menus e permita o acesso **02.01.05.09 Retificação da Folha de Pagamento.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26845055829143)  
  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26845018486679)  
  
  
2. Em seguida, cadastre o período inicial da retificação. Para isso, acesse: **RH | Folha de Pagamento | Configurações | Parametrizador | eSocial | Configurações Gerais | Configurações 5\7.**  
  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26845055831703)  
  
  
3. Lembrando que, os **eventos de códigos de cálculo 382, 383, 384, 385, 386, 392, 393, 402, 403, 404, 405, 406, 407, 408, 424, 425, 426 e 427** são necessários, para que atender o processo de retificação da folha de pagamento. Para maiores informações quanto parametrização e funcionalidades desses códigos de cálculos, [CLIQUE AQUI.](https://tdn.totvs.com/pages/releaseview.action?pageId=452719279)

4. Cadastre o\os eventos que deseja retificar. No exemplo abaixo, iremos retificar um evento de gratificação, que o colaborador deveria ter recibo e não foi lançado. É um provento, valor e com incidência em IRRF.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413000940951)  
  
5. Acesse: **Folha Mensal | Lançamento | Retificação da Folha de Pagamento.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26845018490903)  
  
6. Cadastre os dados da retificação para o lançamento.  
 **![](https://centraldeatendimento.totvs.com/hc/article_attachments/26845055834391)**7. Informe o evento a ser retificado.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26845018495895)  
  
8. Feito isso, avance e lance a retificação**.** Na competência que será retificada, no nosso exemplo a competência de Outubro, será criado o período 10000 e serão lançados os eventos, 3041 provento para o pagamento da gratificação, os códigos de cálculo 383 desconto do líquido de retificação e 382 Estorno base IRRF retificação.  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412990004247)  
  
Na competência atual, serão lançados os eventos códigos de cálculo 384 provento do líquido de retificação, 385 base de IRRF retificação e o código de cálculo 4, desconto de IRRF.  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412990025879)

**Importante**Nos dados  da retificação, no campo chapa, deverá informar a chapa a ser retificada, no campo  competência a ser retificada, já vem a competência anterior automaticamente, portanto se não for a desejada, deverá informar a competência à ser retificada**,** assim como o período deverá informá-lo, não pode ser um período sem movimentação, tem que ser o período que faltou o pagamento ou foi pago incorretamente e o período de retificação já vem automático, pois o sistema valida o que foi informado dentro do **Parametrizador | eSocial**.  
  
**Saiba Mais**[Como gerar a retificação da folha de pagamento de meses anteriores?](https://tdn.totvs.com/pages/releaseview.action?pageId=438289252#1-3)
