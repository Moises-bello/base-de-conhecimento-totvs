---
article_id: 1500000578242
category: RH - Cadastros
content_hash: 18ebb00a67b9263fbb055912d047a9fcff476ea4b303fa92e08510c4923944d7
fetched_at: '2026-06-28T22:44:52.724654+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON -  Sistema não permite excluir troca de turno de
  um período já fechado
type: support-article
updated_at: '2025-12-10T12:38:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000578242-RH-Linha-Protheus-PON-Sistema-n%C3%A3o-permite-excluir-troca-de-turno-de-um-per%C3%ADodo-j%C3%A1-fechado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31752857873943) Tempo aproximado para leitura: 00:01:00 min**  
  
**Dúvida**  
O que verificar quando o sistema gera mensagem que não permite excluir troca de turno de um período do ponto que já foi fechado?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
No modulo do Ponto Eletrônico, ao tentar excluir uma troca de turno referente a um período que já consta fechado será exibido a mensagem abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31752857879575)

Para realizar a exclusão, será necessário ajustar o conteúdo do parâmetro **MV\_DLTRTNO** com **.T.** , essa configuração é através do modulo **SIGACFG - Modulo Configurador**.

Para acesso a configuração dos parâmetros siga a documentação: [Parâmetro do Sistema](https://tdn.totvs.com/pages/releaseview.action?pageId=381037132)  
  
Abaixo como deve ficar configuração do parâmetro:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31752857884183)  
**Importante:** Não recomendamos a exclusão da Troca de Turno por conta de histórico, pois para todos os períodos fechados deve ser mantido o registro de troca de turno.  
  
  
**Saiba Mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
