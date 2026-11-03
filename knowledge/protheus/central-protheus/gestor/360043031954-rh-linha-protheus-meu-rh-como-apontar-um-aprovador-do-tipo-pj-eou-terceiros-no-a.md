---
article_id: 360043031954
category: GESTOR
content_hash: 8eec5b2ab2b2a766d2b223b88c3b533231c79f3adad05a550a6a49c81bda23a0
fetched_at: '2026-06-28T22:44:35.634205+00:00'
product: protheus
section_id: 10299702833303
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como apontar um aprovador  do tipo  PJ e/ou
  terceiros no aplicativo MEU RH
type: support-article
updated_at: '2022-11-18T17:04:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043031954-RH-Linha-Protheus-MEU-RH-Como-apontar-um-aprovador-do-tipo-PJ-e-ou-terceiros-no-aplicativo-MEU-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: 00:02:00 min****Dúvida**Como apontar um aprovador do tipo PJ e/ou terceiros no aplicativo MEU RH?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Meu RH – A partir da versão 12.1.27  
  
**Solução**Não temos como apontar um aprovador, sem existir uma matrícula vinculada. Para exercer o controle de aprovação é obrigatório este vinculo.  
  
Existe uma forma de realizar este cadastro sem interferir em suas movimentações de folhas, envio ao TAF. Cabe a empresa avaliar se a proposta é viável e se atende a expectativa da empresa. Abaixo apresento a forma que temos para contornar esta situação.  
  
Quando um aprovador não faz parte da SRA e não possui uma matricula ativa não temos como aponta-lo como gestor, responsável por um processo de aprovação. É necessário o registro na SRA para exercer este controle.  
  
Podemos sugerir a empresa cadastra-lo através da rotina de contribuinte individual.  
  
Para isso deve ser ativo o parâmetro MV\_AUTPART =1  
  
Orientamos que inclua o CPF neste registro pois poderá ter impactos no uso do portal/aplicativo.  
  
Mesmo que a empresa não execute calculo de folha a este aprovador e caso não queira enviar esses registros ao  TAF , ao executar seu cadastro utilize a  categoria 701 Contribuinte individual, desta forma não será enviado este contribuinte ao TAF.  
  
Importante apontar no parâmetro  MV\_NTSV as categorias que não serão enviadas ao TAF.  
  
Documentação complementar:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020220871-MP-GPE-eSocial-S-2300-Como-integrar-o-evento-nos-casos-em-que-ele-%C3%A9-Opcional->
