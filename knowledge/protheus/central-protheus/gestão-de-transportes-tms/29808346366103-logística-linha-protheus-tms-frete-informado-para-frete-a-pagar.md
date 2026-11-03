---
article_id: 29808346366103
category: Gestão de Transportes (TMS)
content_hash: 28f2e938980846fc9888df4b2b7a2e7d392fac7a4794f4318c9c7aaa75db31a3
fetched_at: '2026-06-28T22:45:29.212275+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Frete Informado para Frete a Pagar
type: support-article
updated_at: '2025-02-07T16:35:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29808346366103-Log%C3%ADstica-Linha-Protheus-TMS-Frete-Informado-para-Frete-a-Pagar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29808346347159) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como utilizar o **Frete Informado** para frete a pagar no **TOTVS Logística TMS**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O **Frete Informado** é utilizado em viagens onde o valor do frete a pagar já foi combinado antecipadamente com o contratado, desta forma, ao utilizar este recurso, então, na geração do **Contrato de Carreteiro**, o Sistema sobrescreve os valores calculados pela **Tabela de frete a pagar** e assume o valor do **Frete Informado** na viagem.  
  
Para isso, é necessário:

* Possuir uma tabela de frete a pagar configurada com componentes de frete com calcula sobre maiores que 51, como por exemplo, **51 - Peso Transportado,** **52 - Quantidade de documentos** ou **53 - Volume transportado,** ou qualquer outro componente desde que contenha valores na viagem.
* Acesse a rotina **TMSA130 - Configuração da tabela de frete** e inclua o componente de frete como **obrigatório** no campo **Comp.Obrig. - DVE\_COMOBR = 1 - Sim**.

Com a tabela de frete a pagar cadastrada e o componente definido como obrigatório, o processo para utilizar o **Frete Informado** a pagar na viagem é o seguinte:

* Se utilizar **viagem modelo 2**, preencha o **Frete Informado** no complemento da viagem, preenchendo o campo **Frete - DTR\_VALFRE;**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29825864924439)

* Se utilizar **viagem modelo 3**, preencha o **Frete Informado** acessando a aba **Recursos/Veículos da Viagem**, preenchendo o campo **Frete - DTR\_VALFRE**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29825896812183)

Após gerar a viagem, quando for gerar o contrato de carreteiro no **TMSA250 - Contrato de carreteiro**, o valor do **Frete Informado** será o valor do frete do contrato:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29825896814615)

**Saiba mais**  
Tabela de Frete a Pagar: [Tabela de Frete a Pagar (TMSA790 - SIGATMS)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=542152688)
