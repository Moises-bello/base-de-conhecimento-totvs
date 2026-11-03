---
article_id: 4411591442583
category: RH - Cálculo Adiantamento
content_hash: ff32c8f4c6673de0af49ea620755f9ef4f3b801fa0e3283a46ddadfd566df606
fetched_at: '2026-06-28T22:43:14.185145+00:00'
product: protheus
section_id: 360011983213
source: central-protheus
title: RH - Linha Protheus - GPE - Adiantamento de comissão no adiantamento com o
  mnemônico  P_PROVADIF = .F.
type: support-article
updated_at: '2024-07-02T18:36:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411591442583-RH-Linha-Protheus-GPE-Adiantamento-de-comiss%C3%A3o-no-adiantamento-com-o-mnem%C3%B4nico-P-PROVADIF-F
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24594927933335) Tempo aproximado para leitura: **00:01:30 min****Dúvida**Adiantamento de comissão no adiantamento com o mnemônico P\_PROVADIF = .F.  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12  
  
**Solução**Para adiantar o valor de comissão, prêmio, gratificação etc., através de verbas **sem Identificadores** **de cálculo** e que tenham incidência de **IR** no adiantamento, é necessário ativar o mnemônico **P\_PROVADIF** (GERAR PROVENTO DE ADIANTAMENTO NA FOLHA - OUTRAS VERBAS) que serve para ser **enviado** para a **folha de pagamento** esse valor **adiantado** no roteiro **ADI** de forma **automática,** porém quando esse mnemônico estiver configurado com **.F**., essa verba de provento **não** será apresentada. Nesta situação o usuário deverá **criar** uma verba de **provento** referente ao valor adiantado e **lançar manualmente** na **RGB** em **atualizações > lançamentos > por funcionários** com o valor adiantando.  
  
Ao calcular a folha de pagamento do período, o valor entrará como **provento** com as devidas incidências configuradas e passarão a compor a base de cálculo do **INSS, IR** e **FGTS** da competência se assim estiver configurada. De contra-partida será gerado **mesmo valor** na verba com id **0007** como **desconto** que terá vindo do cálculo do adiantamento.

**Exemplo de cálculo**Verba para Adiantamento

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24602339819159)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24602339833623)

Verba para Folha de Pagamento

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24602339838487)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24602339847959)

Mnemônico P\_PROVADIF

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24602339851671)  
  
Lançamento da verba de provento 013 no roteiro de Adiantamento (ADI)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24602405954711)  
  
Cálculo do Adiantamento

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24602309235095)  
  
Lançamentos por Funcionário (RGB) após fechamento do roteiro ADI

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24602309240855)

Lançamento da verba de comissão na Folha para abater o valor já adiantado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24602309254039)

Cálculo da folha de pagamento 10/2021

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24602339885207)

Desta forma será **pago** o **valor adiantado,** entrando para a base de IR do período, e caso a mesma verba entre para a base de INSS e FGTS entrará na folha de pagamento para os devidos recolhimentos.

**Observações**Lembrando que o **exemplo** acima é para **demonstrar** a funcionalidade do mnemônico **P\_PROVADIF** com **.F..** As **incidências** cadastradas nas verbas envolvidas é de **responsabilidade da empresa.** Em caso de dúvidas, deve ser solicitado apoio ao jurídico da empresa.

**Saiba Mais**

[RH - Linha Protheus - GPE - Adiantamento Salarial - Configurações e Conceitos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052166714-RH-Linha-Protheus-GPE-Adiantamento-Salarial-Configura%C3%A7%C3%B5es-e-Conceitos?source=search)

[RH - Cálculo Adiantamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983213-RH-C%C3%A1lculo-Adiantamento)
