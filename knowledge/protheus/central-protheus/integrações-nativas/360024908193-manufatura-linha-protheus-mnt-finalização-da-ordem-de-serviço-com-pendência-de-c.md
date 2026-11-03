---
article_id: 360024908193
category: Integrações Nativas
content_hash: 10bb879c7e31a655edd1094316b2e1c09e8531b240b64496258b284387596140
fetched_at: '2026-06-28T22:42:35.381856+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Finalização da Ordem de Serviço com pendência
  de Compras/Estoque
type: support-article
updated_at: '2021-06-02T14:43:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024908193-Manufatura-Linha-Protheus-MNT-Finaliza%C3%A7%C3%A3o-da-Ordem-de-Servi%C3%A7o-com-pend%C3%AAncia-de-Compras-Estoque
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: 00:01:00 min.****Dúvida**Por que é permitido finalizar a **Ordem de Serviço** com pendência de **Compras/Estoque**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - Todas as versões  
  
**Solução**Trata-se como pendência de **Compras** e **Estoque** uma **Solicitação de Compra -****SC** ou **Solicitação de Armazém -****SA** relacionada a uma **Ordem de Serviço**, a qual ainda não retornou como insumo aplicado. Essa funcionalidade é importante para não afetar os **I****ndicadores da Manutenção - MTBF/MTTR** e manter a rastreabilidade de produtos garantindo a integração entre os módulos.  
Porém existem casos onde esta regra não se aplica. Por exemplo: empresas que possuem contratos com fornecedores que emitem nota fiscal, somente após a entrega do produto ou serviço. Para estes casos que fogem a regra, recomenda-se a utilização do ponto de entrada [DT PE NGFINALI Realiza validacao que antecede a finalizacao da OS](http://tdn.totvs.com/display/PROT/DT+PE+NGFINALI+Realiza+validacao+que+antecede+a+finalizacao+da+OS).
