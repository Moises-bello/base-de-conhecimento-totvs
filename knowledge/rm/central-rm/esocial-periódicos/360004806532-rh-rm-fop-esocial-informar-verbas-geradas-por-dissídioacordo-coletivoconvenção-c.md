---
article_id: 360004806532
category: esocial - Periódicos
content_hash: 113e8d7765105a79d01f41c00e8dbcefbbbe06e4a4df4bf4fd144d7bd0a74ccf
fetched_at: '2026-06-28T22:47:09.418969+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Informar verbas geradas por dissídio/acordo coletivo/convenção
  coletiva no eSocial
type: support-article
updated_at: '2025-02-03T16:44:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004806532-RH-RM-FOP-eSocial-Informar-verbas-geradas-por-diss%C3%ADdio-acordo-coletivo-conven%C3%A7%C3%A3o-coletiva-no-eSocial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24072319685783) Tempo aproximado para leitura: 00:01:30 min**

**Dúvida**Como gerar o evento S-1200 informando verbas geradas por dissídio/acordo coletivo/convenção coletiva no eSocial?  
  
 **Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas versões  
  
**Solução**Ao efetuar o pagamento de uma rescisão complementar por dissídio ou o pagamento de uma diferença salarial a um funcionário é necessário informar ao eSocial, por meio do evento **S-1200**, a movimentação referente a esta rescisão complementar/diferença salarial assim como os dados do acordo coletivo ou sentença normativa.  
A principal *tag* a ser observada no evento **S-1200** é a **infoPerAnt**, que levará as informações do acordo coletivo ou dissídio bem como a divisão por período em que existir diferença a ser paga.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29714393100823)

Antes de efetuar o cálculo da rescisão complementar ou diferença salarial é necessário cadastrar os dados do acordo coletivo através do menu **eSocial | Acordo Coletivo/ Reajuste por Lei**. Feito o cadastro do acordo coletivo, este poderá ser informado no momento da rescisão complementar ou diferença salarial. 

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043505213)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042664274)

Uma vez calculada a diferença salarial/rescisão complementar, basta gerar o evento S-1200. No grupo **infoPerAnt**, as informações do dissídio serão apresentadas dentro do grupo **ideADC**, que por sua vez conterá o grupo **idePeriodo** que irá apresentar cada um dos períodos de referência a que se referem os eventos remuneratórios, bem como as verbas por diferença geradas em cada período.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042663874)

**Importante**Conforme consta no **Manual de Orientação do eSocial**, o pagamento de parcelas salariais de natureza rescisória apuradas depois do envio do evento **Desligamento** requer a retificação deste evento, exceto aquelas decorrentes de fatos jurídicos posteriores ao desligamento, provenientes de sentenças normativas, convenções ou acordos coletivos de trabalho e participação de lucros e resultados.  
  
**Saiba mais**  
Acesse os *links* abaixo para mais informações:  
   • [Envio das informações de rescisão complementar via eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007746631)  
   • [Diferença Processo de Rescisão Complementar - Retificação de Rescisão e Acordo Coletivo](http://tdn.totvs.com/pages/viewpage.action?pageId=419535691)
