---
article_id: 4413328440983
category: Rescisão
content_hash: e4a36f720602b0f1a0d042950a540975e7e31f12f8adab0aea4175fe2d55ea4c
fetched_at: '2026-06-28T22:46:54.456628+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: RH - RM - FOP - Retificação de rescisão
type: support-article
updated_at: '2024-09-16T18:59:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413328440983-RH-RM-FOP-Retifica%C3%A7%C3%A3o-de-rescis%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:04:00 min****Dúvida**Como realizar retificação de rescisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para realizar a retificação da folha de pagamento é necessário que as parametrizações estejam ativas e corretas. Portanto, realize os seguintes passos:  
  
1. Acesse: **Serviços Globais | Segurança | Perfis**. Logo, com o sistema **Folha de pagamento** selecionado, edite o perfil desejado, vá em acesso aos menus e permita o acesso **02.01.05.09 Retificação da Folha de Pagamento.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10563203835927)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10563252895383)**2. Em seguida, cadastre o período inicial da retificação. Para isso, acesse: **RH | Folha de Pagamento | Configurações | Parametrizador | eSocial | Configurações Gerais | Configurações 5\7.**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10563294830999)  
  
3. Lembrando que, os eventos de **códigos de cálculo 382, 383, 384, 385, 386, 392, 393, 402, 403, 404, 405, 406, 407, 408, 424, 425, 426 e 426** são necessários, para que atenda o processo de retificação. Para maiores informações quanto parametrização e funcionalidades desses códigos de cálculos, [CLIQUE AQUI.](https://tdn.totvs.com/pages/releaseview.action?pageId=452719279)  
  
4. Cadastre o\os eventos que deseja retificar. No exemplo abaixo, iremos retificar um evento de gratificação, que o colaborador deveria ter recibo na rescisão original e não foi lançado.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413342351127/mceclip5.png)  
  
5. Cadastre a retificação, acessando a rotina: **Rescisão | complementar,** que é referente a rescisão original, exemplo: 01/10/2021.  
  
Na rescisão complementar marque o parâmetro **Retificar rescisão**. A **Data de Último Movimento** e o parâmetro **Pagamento de verbas de natureza salarial ou não salarial devidas após o desligamento** ficarão desabilitados quando o parâmetro **Retificar rescisão** estiver marcado. Escolha o período de lançamento que será gravado no mês competência da rescisão, ou seja, será inserido novo período no mesmo mês em que a rescisão original foi calculada. Este período será por default o período selecionado em: **Parametrizador / eSocial / Configurações / Configurações 5/7**.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10563627319319)  
  
Logo, na tela Eventos Adicionais, informe o evento a ser retificado.  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413328004631/mceclip6.png)  
  
6. Após as parametrizações, avance e lance a retificação da rescisão. Na competência da rescisão original, será criado o período 10000 e lançado o evento com o valor retificado. O evento 3041- valor retificado, o evento com código de cálculo 383- desconto do líquido de retificação e o código de cálculo 382- estorno de base de IRRF.  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413328147991/mceclip7.png)  
  
Na competência atual, serão lançados os eventos de código de cálculo 384- provento do líquido de retificação, código de cálculo 385- base de IRRF retificação e o código de cálculo 4- desconto de IRRF. Lançou o desconto de IRRF, devido a flag de incidência marcada dentro do evento 3041.  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413328267287/mceclip8.png)  
  
**Importante**A diferença entre outras verbas de natureza salarial ou não salarial devidas após o desligamento e a retificação da rescisão.  Uma apuração de comissão após a rescisão será devida e cabe a tratativa do processo,  pagamento outras verbas de natureza salarial ou não salarial devidas após o desligamento. Quando houver uma valor pago indevidamente ou  que foi deixado de pagar por esquecimento, cabe a tratativa de  retificação de rescisão.  
  
**Saiba Mais**[Rescisão Complementar](https://tdn.totvs.com/pages/releaseview.action?pageId=452718921#:~:text=Para%20retificar%20uma%20rescis%C3%A3o%20no,no%20m%C3%AAs%20compet%C3%AAncia%20da%20rescis%C3%A3o.)  
[S-2299/S-2399 - Como gerar Retificação de desligamento?](https://tdn.totvs.com/pages/releaseview.action?pageId=417700835)
