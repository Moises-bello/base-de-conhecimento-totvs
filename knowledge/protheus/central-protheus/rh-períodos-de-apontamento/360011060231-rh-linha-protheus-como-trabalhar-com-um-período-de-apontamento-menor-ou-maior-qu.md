---
article_id: 360011060231
category: RH - Períodos de Apontamento
content_hash: 2d076729605bb63586869d66191ca0edba588476b53a082bee340b0ff032a030
fetched_at: '2026-06-28T22:44:45.073705+00:00'
product: protheus
section_id: 32419304439959
source: central-protheus
title: RH - Linha Protheus - Como trabalhar com um período de apontamento menor ou
  maior que 30 dias no Ponto Eletrônico
type: support-article
updated_at: '2026-03-20T20:02:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011060231-RH-Linha-Protheus-Como-trabalhar-com-um-per%C3%ADodo-de-apontamento-menor-ou-maior-que-30-dias-no-Ponto-Eletr%C3%B4nico
---

**Dúvida**  
Como trabalhar com um **período de apontamento** menor ou maior que **30 dias** no Ponto Eletrônico?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Para que o Ponto Eletrônico consiga fazer a correta montagem de um calendário de período **menor ou maior que 30 dias,** o usuário deverá acessar: **Atualizações - Cadastro do Ponto - Período de Apontamento - Outras Ações - Modificar Período de Apontamento** - escolher a opção **PERÍODO:**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19120442400023)**   
  
  
Informar manualmente o dia **inicial/final** do período. Com esta ação, o conteúdo dos parâmetros **MV\_PAPONTA e MV\_PONMES** ficarão iguais:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19139644836503)  
  
  
**OBS:** Antes de fazer a **primeira leitura** do período seguinte, é de **extrema importância** que após o fechamento deste período menor ou maior que 30 dias, o usuário acesse esta mesma rotina, mas selecione a opção de **DIA INICIAL/FINAL**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19139485196183)  
  
  
Informe o **primeiro** e **último** dia do novo período, por exemplo: 01/31, 16/15, etc:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19139485203095)  
  
  
Após isso, informe apenas o **último dia** do novo período para salvar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19139622512663)  
  
  
Com este ajuste, o período ficará dessa forma:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19139622515351)  
  
Este processo é necessário, pois o período anterior foi aberto manualmente e com uma quantidade de dias fora do habitual, os próximos fechamentos feitos com períodos de 30 dias não precisarão de ajuste por parte do usuário.  
  
**\*\*É importante que não possua nenhuma marcação lida/nas tabelas no período a ser alterado para não gerar futuros problemas.**  
  
**Saiba Mais:**  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)
