---
article_id: 1500004935141
category: Folha Mensal
content_hash: 3cbe9028d8160863712931fd4bdaa83f63e14d3883f11f3883e241790da029fb
fetched_at: '2026-06-28T22:46:59.417265+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Licença Maternidade conforme Portaria Conjunta n. 28 de 19
  de Março de 2021
type: support-article
updated_at: '2025-03-07T14:34:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004935141-RH-RM-FOP-Licen%C3%A7a-Maternidade-conforme-Portaria-Conjunta-n-28-de-19-de-Mar%C3%A7o-de-2021
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:02:00 min****Dúvida**Foi publicada em 23 de março de 2021, no Diário Oficial da União, a Portaria Conjunta n. 28 de 19 de Março de 2021, que comunica o cumprimento da prorrogação do benefício salário maternidade para todas as mulheres trabalhadoras que recolhem a contribuição para o INSS, em virtude da prematuridade. Como parametrizar essa informação no sistema RM?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Atualmente, o sistema já atende à Portaria Conjunta n. 28 de 19 de Março de 2021, conforme orientações a seguir:  
  
O tratamento de cálculo é o mesmo para licença maternidade, independente do motivo, pois é validado o tipo de afastamento e não o motivo. Estes motivos são somente para tratamento do SEFIP.  
  
Os campos estão localizados em Folha de Pagamento | Configurações | Parametrizador | Folha Normal | Salário Maternidade 2/2:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006919101/mceclip0.png)  
  
**Motivo de afastamento ref. a licença maternidade por antecipação:**Neste campo deve ser informado um motivo de afastamento de licença maternidade por antecipação. Esse motivo específico será utilizado nos eventos S-2200 e S-2230 do eSocial. Ao incluir um afastamento do tipo E - Licença Maternidade com o motivo especificado nesse campo, será considerado o motivo 35 - Licença Maternidade - Antecipação e/ou prorrogação mediante atestado médico nesses eventos.  
  
**Motivo de afastamento ref. a licença maternidade por prorrogação:**Neste campo deve ser informado um motivo de afastamento de licença maternidade por prorrogação. Esse motivo específico será utilizado nos eventos S-2200 e S-2230 do eSocial. Ao incluir um afastamento do tipo E - Licença Maternidade com o motivo especificado nesse campo, será considerado o motivo 35 - Licença Maternidade - Antecipação e/ou prorrogação mediante atestado médico nesses eventos.

Para maiores orientações acessar os links abaixo:

* [Salário Maternidade 2/2](https://tdn.totvs.com/pages/releaseview.action?pageId=452719874)
* [Licença Maternidade - Ampliação da licença Maternidade para parto prematuro](https://tdn.totvs.com/pages/releaseview.action?pageId=570044459)

**Importante**O motivo informado nos campos do Parametrizador deverá ser o mesmo motivo utilizado no cadastro do afastamento para o funcionário.  
  
Caso for de interesse do usuário, poderá criar um motivo de afastamento de sua preferência utilizando a tabela dinâmica INT 28.  
  
**Saiba mais**  
[RM - FOP - Afastamento: Como criar um novo motivo de afastamento?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015217811-RM-FOP-Afastamento-Como-criar-um-novo-motivo-de-afastamento-)
