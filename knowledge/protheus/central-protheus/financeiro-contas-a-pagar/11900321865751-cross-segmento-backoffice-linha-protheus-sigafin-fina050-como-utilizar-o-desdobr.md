---
article_id: 11900321865751
category: Financeiro - Contas a Pagar
content_hash: 9014d0798a9a2f6e8cfcd7933752c68b534e76d1abfa608bb04a526724d5721a
fetched_at: '2026-06-28T22:38:07.301408+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA050 - Como utilizar
  o desdobramento de títulos com retenção do imposto PCC?
type: support-article
updated_at: '2023-01-24T20:34:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11900321865751-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Como-utilizar-o-desdobramento-de-t%C3%ADtulos-com-reten%C3%A7%C3%A3o-do-imposto-PCC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**  
Como utilizar o desdobramento de títulos com retenção do imposto PCC no contas a pagar?

**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) - Financeiro - FINA050 - Todas as versões  
  
**Solução**Será necessário acessar o módulo Configurador (SIGACFG) do Protheus e alterar o parâmetro **MV\_NRASDSD** para o conteúdo "**.F."** (false – falso), conforme exemplo abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11910835232151)  
**Observação:** Após alteração, deve reiniciar o Appserver do ambiente.Acessar a rotina FINA050 e realizar a inclusão do titulo com a retenção do PCC (é necessário que o sistema esteja configurado com os parâmetros e configurações para a geração do cálculo do imposto).  
  
Acessar a aba **Administrativo** e clicar no campo Desdobramento =1- Sim, preencher o número de parcelas e o Período de Vencto e clicar no OK, conforme exemplo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11910896106519)  
Ao salvar o titulo, o valor das retenções dos impostos serão diluídos nas parcelas:  
  
**Exemplo 1**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11910899700247)

**Exemplo 2  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11910937075607)**  
**Saiba mais**[Geração de Títulos por Desdobramento (FINA040 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=306856119)   
[DOC0016-Retenção de PIS COFINS CSLL](https://tdn.totvs.com/pages/releaseview.action?pageId=6076816)
