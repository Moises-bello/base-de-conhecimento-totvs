---
article_id: 360055231833
category: Portal de Gestão de Capital Humano
content_hash: 99d120f937fdc1fb8ee73b9907d69dfc3a32951b463c2ae9c2dff81d8b000b0b
fetched_at: '2026-06-28T22:42:59.141988+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH - Como apontar um aprovador do tipo PJ e ou
  terceiros no portal GCH
type: support-article
updated_at: '2021-09-29T13:13:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055231833-RH-Linha-Protheus-PORTAL-GCH-Como-apontar-um-aprovador-do-tipo-PJ-e-ou-terceiros-no-portal-GCH
---

**Dúvida**Como apontar um aprovador do tipo PJ e/ou terceiros no Portal Gestão Capital Humano?  
  
**Ambiente**TOTVS RH (Linha Protheus) -  Portal Gestão Capital  Humano - Todas as versões  
  
**Solução**Não temos como apontar um aprovador, sem existir uma matrícula vinculada. Para exercer o controle de aprovação é obrigatório este vinculo.

Existe uma forma de realizar este cadastro sem interferir em suas movimentações de folhas, envio ao TAF. Cabe a empresa avaliar se a proposta é viável e se atende a expectativa da empresa. Abaixo apresento a forma que temos para contornar esta situação.

Quando um aprovador não faz parte da SRA e não possui uma matricula ativa não temos como aponta-lo como gestor, responsável por um processo de aprovação. É necessário o registro na SRA para exercer este controle.

Podemos sugerir a empresa cadastra-lo através da rotina de contribuinte individual.

Para isso deve ser ativo o parâmetro MV\_AUTPART =1

Orientamos que inclua o CPF neste registro pois poderá ter impactos no uso do portal/aplicativo.

Mesmo que a empresa não execute calculo de folha a este aprovador e caso não queira enviar esses registros ao TAF , ao executar seu cadastro utilize a categoria 701 Contribuinte individual, desta forma não será enviado este contribuinte ao TAF.

Importante apontar no parâmetro MV\_NTSV as categorias que não serão enviadas ao TAF.

Documentação complementar:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020220871-MP-GPE-eSocial-S-2300-Como-integrar-o-evento-nos-casos-em-que-ele-%C3%A9-Opcional->
