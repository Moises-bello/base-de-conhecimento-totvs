---
article_id: 11230791972503
category: eSocial - Gerar XML/ Integração Evento
content_hash: fe969147bc15ca67daff869a20e99e8440cc54dff54c6c0c1057acf0330df309
fetched_at: '2026-06-28T22:47:12.132181+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 459 na integração com governo: Nao foi localizado
  um evento para o recibo de entrega informado ou o mesmo foi excluído/retificado'
type: support-article
updated_at: '2024-06-20T16:22:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11230791972503-RH-RM-FOP-eSocial-Erro-459-na-integra%C3%A7%C3%A3o-com-governo-Nao-foi-localizado-um-evento-para-o-recibo-de-entrega-informado-ou-o-mesmo-foi-exclu%C3%ADdo-retificado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24315513822871) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao encaminhar o XML S-3000 ou algum XML de retificação ao governo, é apresentada a mensagem **Erro código 459: Não foi localizado um evento para o recibo de entrega informado ou o mesmo foi excluído/retificado. Ação Sugerida: Deverá existir um Evento já recebido, quot;Ativoquot; (não excluído ou retificado), com número de recibo de entrega igual ao informado no campo.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11230144162199)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Este erro ocorre quando um evento que já consta no governo está sendo excluído, através do evento S-3000, ou retificado, porém, o **número do recibo** que está sendo informado não é o mesmo que consta no eSocial para o evento original.  
  
**Solução**  
As validações para o caso dos erros são:  
  
**• Se o erro ocorrer ao encaminhar o S-3000**  
1. Identifique no XML o número do recibo, na *tag* **nrRecibo**;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11230286315543)

2. Verifique no portal do governo se o número do recibo do evento original, o qual deseja excluir, está de acordo com o XML que está encaminhando.  
  
**• Se o erro ocorrer ao encaminhar uma Retificação**

1. Identifique no XML o número do recibo, na *tag* **nrRecibo**;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11230286315543)

2. Verifique no portal do governo se o número do recibo do evento original, o qual deseja retificar, está de acordo com o XML que está encaminhando.

3. Caso o evento original não conste no governo, será necessário encaminhar o XML desejado como inclusão, sendo preenchido na *tag* **indRetif = 1**.   
  
**Observação**  
Verifique também, se o evento original, que deseja retificar/excluir, foi selecionado corretamente ao gerar o evento de retificação ou S-3000;  
O governo só aceitará a exclusão/retificação dos evento que ainda estivem cadastrados no portal na forma original. Caso o evento já tenha sido excluído/retificado por dentro do portal, não será possível realizar o envio do S-3000 ou retificação através do sistema, deverá realizar tais intervenções diretamente no ambiente do Governo.

**Saiba Mais**Para maiores informações acesse:[- Utilização do S-3000 para exclusão de eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034224074-RH-RM-FOP-eSocial-Utiliza%C3%A7%C3%A3o-do-S-3000-para-exclus%C3%A3o-de-eventos)  
[- Retificação do evento S-1200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028334171-RH-RM-FOP-eSocial-Retifica%C3%A7%C3%A3o-do-evento-S-1200)
