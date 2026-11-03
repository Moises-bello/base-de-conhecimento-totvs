---
article_id: 4403859205271
category: RH - Cálculos
content_hash: 88cca260a82c7985fca25e8ddbe4f300bb79893f8aa6231e75017b4596eff3ef
fetched_at: '2026-06-28T22:44:51.611473+00:00'
product: protheus
section_id: 32419138773655
source: central-protheus
title: RH - Linha Protheus - PON -  É possível realizar o calculo de férias módulo
  do Ponto Eletrônico
type: support-article
updated_at: '2026-02-10T18:58:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403859205271-RH-Linha-Protheus-PON-%C3%89-poss%C3%ADvel-realizar-o-calculo-de-f%C3%A9rias-m%C3%B3dulo-do-Ponto-Eletr%C3%B4nico
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38306125587863)****Tempo aproximado para leitura: 00:01:30 min**  
  
**Dúvida**  
É possível realizar calculo férias através do modulo de Ponto Eletrônico?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Não é possível realizar o calculo de férias no modulo do Ponto Eletrônico (SIGAPON), pois esse procedimento deve ser realizado no módulo de Gestão de Pessoal (SIGAGPE).

No modulo de Gestão de Pessoal após realizar o calculo de férias o sistema alimentará a tabela SR8, que também é utilizada no módulo do Ponto Eletrônico.

Com esse fluxo o sistema atualiza todas as rotinas envolvidas, como por exemplo a integração das verbas de férias com a folha de pagamento, o envio correto dos eventos para o e-social, e atualização do controle de dias de direito, entre outras rotinas.  
  
Nos casos que não é utilizado o módulo Gestão de Pessoal e utiliza somente o modulo Ponto Eletrônico, é possível realizar o lançamento de forma manual através da rotina de Afastamentos em **Atualizações > Cadastro de Funcionários > Afastamentos** que alimenta direto a SR8.

Exemplo:

Incluir na rotina de afastamentos o motivo "Férias" no campo "Cod. Ausenc." e informar o período que o funcionário estará de férias:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31354258639383)

Dessa forma o calendário do funcionário será atualizado, onde será possível visualizar através da rotina de Integrados, em **Atualizações > Lançamentos > Integrados** os dias em que o funcionários estará de  férias com legenda em cinza:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31354281653655)

Obs.: Outra opção caso não queira incluir as férias na rotina e Afastamentos, pode ser criado um motivo de abono como "Férias" e lançar um abono coletivo para os colaboradores que gerou falta por estarem de férias.

**Saiba Mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Como efetuar um Abono Coletivo no Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050762134-RH-Linha-Protheus-PON-Como-efetuar-um-Abono-Coletivo-no-Ponto-Eletr%C3%B4nico)  
[RH - Linha Protheus - PON - Cadastro Motivos De Abono/Justificativa](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000047328)
