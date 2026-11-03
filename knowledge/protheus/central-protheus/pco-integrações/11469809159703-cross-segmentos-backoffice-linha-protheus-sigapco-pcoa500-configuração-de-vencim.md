---
article_id: 11469809159703
category: PCO - Integrações
content_hash: 2e5c3b3599f3015157d8a6611bfbe567cab157053197319830b5cc1b8d87c884
fetched_at: '2026-06-28T22:37:10.179033+00:00'
product: protheus
section_id: 1500001550902
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAPCO - PCOA500 - Configuração
  de Vencimento para contingencia.
type: support-article
updated_at: '2023-01-10T13:41:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11469809159703-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAPCO-PCOA500-Configura%C3%A7%C3%A3o-de-Vencimento-para-contingencia
---

**Dúvida**Como configurar o vencimento de Contingencia.

**Ambiente**Cross Segmento - Backoffice Linha Protheus -Planejamento e Controle Orçamentário.

#### **Solução:**

O processo de bloqueio de solicitação de contingencia vencida é executado a partir da rotina PCOA500  → (Botão Outras ações → Blq. vencidas), caso não seja feito este processo a contingencia ainda estará disponível para uso, terá apenas uma data de referencia de validade.

**Bloqueio solicitação de contingência Vencida :** Acessar a rotina PCOA500   e executar o processo :

(**Outras açôes**-**Bloq. Vencidas)**->  Bloquear as **CONTIGENCIAS VENCIDAS** que **NÂO FORAM LIBERADAS**;

Este processo  acima  filtra todas as solicitações de contingência que estejam vencidas com LEGENDA VERMELHA  não liberadas (Aguardando liberação de usuário ) ,mudando para legenda CINZA (cancelado)

**A solicitação de contingência LIBERADA/APROVADA**:  A solicitação com **legenda VERDE  Liberada aprovada**, sempre estará disponível independentemente se a validade estive vencida, pois, a mesma encontra-se liberada.

**Premissas :**

O SIGAPCO  Planejamento controle Orçamentário ( PCO )  deve estar configurado: Parâmetros, Cubos, Processos, bloqueios e aprovadores;

Abaixo exemplificaremos  o  de bloqueio de solicitação de contingência vencida, a partir de um pedido de compra.

Parâmetro :  MV\_PCOVENC = 2 define os dias pra vencimento da Contingência.

![](https://tdn.totvs.com/download/attachments/547852831/image2020-5-6_15-52-22.png?version=1&modificationDate=1588791142660&api=v2)

Exemplo : Incluindo um pedido de compra  (MATA121)

![](https://tdn.totvs.com/download/attachments/547852831/image2020-5-6_15-5-23.png?version=1&modificationDate=1588788559367&api=v2)

Selecionar o botão Contingência

![](https://tdn.totvs.com/download/attachments/547852831/image2020-5-6_15-5-46.png?version=1&modificationDate=1588788559313&api=v2)

Outras ações -> Solicitar

![](https://tdn.totvs.com/download/attachments/547852831/image2020-5-6_15-6-49.png?version=1&modificationDate=1588788559260&api=v2)

Selecionar o botão Enviar

Observe que gerou a contingência 000006

![](https://tdn.totvs.com/download/attachments/547852831/image2020-5-6_15-9-9.png?version=1&modificationDate=1588788558993&api=v2)

Acessando o sistema com data posterior a  digitação do pedido e solicitação de contingência 25/05/2020

![](https://tdn.totvs.com/download/attachments/547852831/image2020-5-6_15-18-40.png?version=1&modificationDate=1588789120657&api=v2)

**Observe acima que a legenda é vermelha (aguardando liberação do usuário)**

ALI\_DTSOLI = DATA DA MAQUINA

ALI\_DTVALI = DATA DA VALIDADE CONSIDERANDO DATA BASE DE ENTRADA NO PROTHEUS + MV\_PCOVENC

ALJ\_DATA  = DATA BASE DE ENTRADA NO PROTHEUS

![](https://tdn.totvs.com/download/attachments/547852831/image2020-5-6_15-19-26.png?version=1&modificationDate=1588789166800&api=v2)

   Posicionaremos na  solicitação 000006 e  clicar em Outras Ações -> Bloquear vencidas

![](https://tdn.totvs.com/download/attachments/547852831/image2020-5-6_15-23-16.png?version=1&modificationDate=1588789396800&api=v2)

![](https://tdn.totvs.com/download/attachments/547852831/image2020-5-6_15-24-41.png?version=1&modificationDate=1588789481790&api=v2)

A contingência será Cancelada

![](https://tdn.totvs.com/download/attachments/547852831/image2020-5-6_15-25-18.png?version=1&modificationDate=1588789518667&api=v2)

![](https://tdn.totvs.com/download/attachments/547852831/image2020-5-6_15-26-21.png?version=1&modificationDate=1588789581993&api=v2)

Mata121 - Ao  inserir um pedido de compra veja que não aparecerá a contingência vencida 000006

![](https://tdn.totvs.com/download/attachments/547852831/image2020-5-6_15-26-56.png?version=1&modificationDate=1588789616167&api=v2)

Observe abaixo  que a contingência 000006 não aparece na tela ao clicar no botão Contingência ou seja, não é possível vincular ao pedido.

![](https://tdn.totvs.com/download/attachments/547852831/image2020-5-6_15-27-27.png?version=1&modificationDate=1588789647787&api=v2)

![](https://tdn.totvs.com/download/attachments/547852831/image2020-5-6_15-28-7.png?version=1&modificationDate=1588789687967&api=v2)

**Saiba mais:**

[Cross Segmento - Backoffice Linha Protheus - SIGAPCO Utilização de Contingência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018523352-MP-SIGAPCO-Como-utilizar-a-conting%C3%AAncia-no-m%C3%B3dulo-PCO-)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Principais parâmetros do módulo PCO - Principais parâmetros do módulo PCO - Planejamento e Controle Orçamentário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017496452-MP-SIGACOM-Principais-par%C3%A2metros-do-m%C3%B3dulo-PCO-?source=search)

[Controladoria - PCO - Protheus 12](https://tdn.totvs.com/display/public/PROT/Controladoria+-+PCO+-+Protheus+12)

[Cross Segmento - Backoffice Linha Protheus - SIGAPCO - CheckList para utilização do modulo Planejamento de Custos Orçamentários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038998854-MP-SIGAPCO-CheckList-para-utiliza%C3%A7%C3%A3o-do-modulo-Planejamento-de-Custos-Or%C3%A7ament%C3%A1rios)
