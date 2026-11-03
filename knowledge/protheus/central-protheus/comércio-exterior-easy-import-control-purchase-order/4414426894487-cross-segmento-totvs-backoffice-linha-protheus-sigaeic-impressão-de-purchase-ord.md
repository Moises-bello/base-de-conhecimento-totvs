---
article_id: 4414426894487
category: Comércio Exterior - Easy Import Control - Purchase - Order
content_hash: 8ad2700eb01521659890b48da667245453619cc06600cb1a1b951df3451c9695
fetched_at: '2026-06-28T22:39:41.181537+00:00'
product: protheus
section_id: 1500001538481
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Impressão de Purchase
  Order "Função de usuário não esta compilada no repositório (EICPO150)".
type: support-article
updated_at: '2023-08-16T19:23:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414426894487-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Impress%C3%A3o-de-Purchase-Order-Fun%C3%A7%C3%A3o-de-usu%C3%A1rio-n%C3%A3o-esta-compilada-no-reposit%C3%B3rio-EICPO150
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16817115427479)** Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Ao tentar acessar o relatório do Purchase Order (**EICPO150**) esta sendo exibido a mensagem NO\_IX - Problema: Função de usuário não esta compilada no repositório.

![EICPO150_RDM.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4414426603415)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  –*Easy Import Control* – Todas versões  
  
**Solução**O rdmake responsável em executar o relatório não esta disponível no repositório do cliente. Será necessário:

1) Baixar o rmadke **Eicpo150\_RDM** que fica disponível no pacote de expedição continua do comex, link: <https://tdn.totvs.com/pages/releaseview.action?pageId=526987588>.  
2) Procure o fonte **Eicpo150\_RDM.prw** dentro da pasta compactada  **Rdmakes**.  
3) Será necessário  compilar o rdmake no repositório do cliente para que o relatório seja disponível para uso.  
4) Efetuado este procedimento a rotina estará disponível para uso.  
  
**Saiba mais**[Pacote de Atualizações Comércio Exterior](https://tdn.totvs.com/pages/releaseview.action?pageId=526987588)
