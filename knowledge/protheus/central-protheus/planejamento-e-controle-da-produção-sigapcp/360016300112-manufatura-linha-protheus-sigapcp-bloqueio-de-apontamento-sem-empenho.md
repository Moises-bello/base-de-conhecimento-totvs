---
article_id: 360016300112
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: bbb12a581be325bf5d1e979c0bd863ee21022a3a4a15b4eb934abd96c3cbea2f
fetched_at: '2026-06-28T22:42:40.912318+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Bloqueio de apontamento sem empenho
type: support-article
updated_at: '2021-12-01T12:08:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016300112-Manufatura-Linha-Protheus-SIGAPCP-Bloqueio-de-apontamento-sem-empenho
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura**: 00:01:10 min****Dúvida**Como bloquear a inclusão de um apontamento de produção quando não foram gerados os empenhos?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - A partir da versão 12.1.17  
  
**Solução**Para bloquear a inclusão do apontamento de produção, quando não houver empenhos gerados, deve configurar o parâmetro **MV\_APTEMP - Indica se é possível gerar apontamento para uma ordem de produção mesmo que não exista empenho para a OP em questão** igual a **.F.**, ou seja, o Sistema valida a tabela **SD4 - Tabela de requisições empenhadas** para verificar se o empenho existe.  
  
Caso configure o parâmetro **MV\_APTEMP** igual a **.T.**, será exibida a mensagem, porém permite que o usuário opte por prosseguir ou não com o processo. Para inibir esta mensagem sem bloquear o processo é necessário utilizar o ponto de entrada **MT650PISC**.  
  
**Saiba mais**Para conhecer mais sobre esse assunto, acesse os *links* abaixo:  
*Release Notes*: [Definição para inclusão de apontamentos com OP sem empenho](http://tdn.totvs.com/pages/viewpage.action?pageId=351021518)Documento de Referência: [Parâmetro MV\_APTEMP](http://tdn.totvs.com/display/PROT/MV_APTEMP)Ponto de Entrada: [MT650PISC - Controla a geração de OPs intermediárias](http://tdn.totvs.com/pages/viewpage.action?pageId=325845355)
