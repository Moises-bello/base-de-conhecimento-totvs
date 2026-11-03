---
article_id: 40667203123863
category: Gestão de Armazenagem (WMS)
content_hash: 694fc8b70ad1c23ce3f106e3365b8bcc301d50b4f339ee9b00e2b5002568cc00
fetched_at: '2026-06-28T22:45:48.044854+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Logística - Linha Protheus - WMS - Gerar ou imprimir o relatório de busca de
  endereço do Protheus WMS
type: support-article
updated_at: '2026-05-22T19:29:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40667203123863-Log%C3%ADstica-Linha-Protheus-WMS-Gerar-ou-imprimir-o-relat%C3%B3rio-de-busca-de-endere%C3%A7o-do-Protheus-WMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40667217739543) Tempo aproximado para leitura: **00:01:20 min**  
  
**Dúvida**  
Como gerar ou imprimir o **relatório de busca de endereço** do **Protheus WMS**?  
  
**Ambiente**  
TOTVS Logística - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (WMS) - Todas as versões  
  
**Solução**  
Quando o Sistema não consegue executar a ordem de serviço **WMS** de armazenagem, recomenda-se analisar o **relatório de busca de endereço**, conforme a seguinte orientação:  
  
"**Para ordens de serviço de endereçamento com problemas, execute manualmente as ordens de serviço interrompidas e analise o relatório de busca de endereço.**"  
  
Este relatório permite examinar a sequência de etapas que o Sistema seguiu para definir os endereços destinados ao armazenamento do produto, incluindo as estruturas físicas consultadas, os motivos pelos quais determinados endereços foram desconsiderados, a quantidade em uma localização já comprometida por outras movimentações, entre outros aspectos.  
  
O parâmetro **MV\_WMSRLEN** possibilita configurar se o **relatório de busca de endereços** para armazenagem deve ser exibido sempre que uma **O.S. WMS** de endereçamento for executada. Caso este parâmetro esteja configurado com o valor **.T.**, o relatório será apresentado independentemente do resultado da execução do serviço **WMS**. Por outro lado, se estiver configurado com o valor **.F.**, o relatório será exibido somente quando houver alguma inconsistência na execução do serviço.  
  
Recomenda-se, portanto, ativar o parâmetro **MV\_WMSRLEN**, executar novamente a ordem de serviço **WMS** interrompida por meio do programa **WMSA150 - Execução de Serviços**, e comparar com as configurações da sequência de abastecimento do produto indicado na mensagem, utilizando o cadastro **WMSA030 - Seq. Abastecimento**.  
  
**Saiba mais**  
A documentação do parâmetro **MV\_WMSRLEN** está disponível no *link*: [Parâmetros (Configurações - SIGAWMS)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=569475584)  
  
**Glossário**  
**WMS** - *Warehouse Management System*  
**O.S.** - Ordem de Serviço  
**.T.** - *True*  
**.F.** - *False*
