---
article_id: 23133343239959
category: Financeiro - Reinf
content_hash: fc87b35830d7a3305bb9b3ff3f4e088508a4c448745591f45a3db49f392dbd45
fetched_at: '2026-06-28T22:37:51.755244+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA985 - Como informar
  o código de isenção IRRF no Evento R-4010  '
type: support-article
updated_at: '2024-04-29T20:23:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23133343239959-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA985-Como-informar-o-c%C3%B3digo-de-isen%C3%A7%C3%A3o-IRRF-no-Evento-R-4010
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23133332874391) Tempo aproximado para leitura: **05:00 min**

**Dúvida**Como informar código de isenção IRRF no Evento R-4010?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**

Este cenário se enquadra para situação de um título a pagar com dedução na base de calculo do IR de pessoa física onde é necessário apresentar as informações de dedução e de código de isenção de IRRF para o evento R-4010 do REINF, tanto as deduções como o código de senção são aplicados no titulo a pagar através da aba Complemento de Imposto x Titulo (tabela FKG).

**Procedimento:**

1. No módulo Financeiro (SIGAFIN), acesse Atualizações / Cadastro / Complemento do Imposto (FINA985). O sistema apresenta a janela de complementos cadastrados.

2. Clique em Incluir para incluir um novo cadastro.

3. Na tela de cadastro, preencha os seguintes campos.

4. Confira os dados e confirme.

Exemplo de Complemento de Imposto - Dedução do IRF por pensão alimentícia:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23133332875927)

6. No módulo Financeiro (SIGAFIN), acesse Atualizações / Funções Contas a Pagar / Outras Ações / Complemento de título / Complemento de impostos x Títulos.

1. Informe o código cadastrado no titulo.

2. Salva o registro com o complemento do titulo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23133343216663)

As informações de complemento de titulo foram populadas na tabela FKG e estarão contidas no evento R-4010 do REINF.

**Saiba mais:**

[Cadastro de Complemento do Imposto - FINA985](https://tdn.totvs.com/display/public/PROT/Cadastro+de+Complemento+do+Imposto+-+FINA985)

[Reinf\_R-4010\_inclusão\_de\_título](https://tdn.totvs.com/pages/releaseview.action?pageId=736178352#Cen%C3%A1rios--264919855)

##
