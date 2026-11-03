---
article_id: 360013456932
category: RH - Banco De Horas
content_hash: cf0facfd221985a00e23bbe8cae73c73493220c8742b3e0087c1b4c757ebdc48
fetched_at: '2026-06-28T22:44:54.245835+00:00'
product: protheus
section_id: 32405029751063
source: central-protheus
title: RH - Linha Protheus - PON - Como zerar o Banco de Horas sem realizar o pagamento
  ou desconto das horas em Folha
type: support-article
updated_at: '2025-09-16T13:18:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013456932-RH-Linha-Protheus-PON-Como-zerar-o-Banco-de-Horas-sem-realizar-o-pagamento-ou-desconto-das-horas-em-Folha
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32616360935319) Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**Como zerar o Banco de Horas através da rotina **PONA200** sem realizar o pagamento ou desconto das horas em Folha?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Para zerar o Banco de Horas sem realizar o pagamento ou desconto das horas em Folha, execute o seguinte procedimento:  
  
Acessar a rotina PONA200 em **Atualizações > Lançamentos > Banco de Horas**, informar no campo **Status (PI\_STATUS**) = Baixado, e no campo **Dt.Baixa (PI\_DTBAIX)** = informar a data em que será considerado a baixa (exemplo abaixo), assim o sistema irá zerar a informação no banco de horas:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32066387160599)  
  
Após efetuar este procedimento, o sistema não deixará essas horas disponíveis para serem baixadas para desconto ou pagamento em Folha, sendo assim, serão apenas zeradas do histórico.  
  
**Obs.**: Para que a baixa seja realizada no padrão do sistema, e posteriormente os valores sejam pagos ou descontados em Folha, deve ser executado o Fechamento de Banco de Horas, através da rotina PONM080. Para mais detalhes sobre o fechamento do banco de horas **[clique aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013670411-RH-Linha-Protheus-PON-Como-efetuar-o-fechamento-do-banco-de-horas)****Saiba mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
