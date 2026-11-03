---
article_id: 11899514808983
category: Financeiro - Contas a Receber
content_hash: e67cf82df2eecf157cb6e5979ca70d7ca126397ac858bfcfa30331d36b471c76
fetched_at: '2026-06-28T22:38:12.755244+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA040 - Como utilizar
  o desdobramento de títulos com retenção do imposto PCC?
type: support-article
updated_at: '2023-01-24T20:44:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11899514808983-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA040-Como-utilizar-o-desdobramento-de-t%C3%ADtulos-com-reten%C3%A7%C3%A3o-do-imposto-PCC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como utilizar o desdobramento de títulos com retenção do imposto PCC no contas receber?  
  
**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) - Financeiro - FINA040 - Todas as versões  
  
**Solução**Será necessário acessar o modulo Configurador do Protheus e alterar o parâmetro **MV\_NRASDSD** para o conteúdo **“.F.”** (false – falso), conforme exemplo abaixo:

![1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/11898800858007)

**Observação:** Após alteração, deve reiniciar o Appserver do ambiente.  
  
Acessar a rotina FINA040 e realizar a inclusão do titulo com a retenção do PCC (é necessário que o sistema esteja configurado com os parâmetros e configurações para a geração do calculo do imposto).  
  
Acessar a aba Administrativo e clicar no campo Desdobramento = Sim, preencher o número de parcelas e o Período de Vencto e clicar no OK, conforme exemplo:

![3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/11899136993559)

Ao Salvar o titulo, O valor das retenções do imposto serão diluídos nas parcelas|  
  
**Exemplo 1**

![4.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/11899278225175)

**Exemplo 2**

![5.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/11899335003671)  
  
**Saiba mais**[Geração de Títulos por Desdobramento (FINA040 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=306856119)   
[DOC0016- Retenção de PIS COFINS CSLL](https://tdn.totvs.com/pages/releaseview.action?pageId=6076816)
