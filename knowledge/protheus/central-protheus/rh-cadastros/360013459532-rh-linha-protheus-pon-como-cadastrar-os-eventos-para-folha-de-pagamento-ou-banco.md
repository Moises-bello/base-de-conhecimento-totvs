---
article_id: 360013459532
category: RH - Cadastros
content_hash: 277b7a1a66ff513a55c412c8c839c069ad60f1c00f88fda5b793f1af09393949
fetched_at: '2026-06-28T22:44:52.808751+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Como cadastrar os eventos para Folha de Pagamento
  ou Banco de Horas
type: support-article
updated_at: '2026-02-04T16:53:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013459532-RH-Linha-Protheus-PON-Como-cadastrar-os-eventos-para-Folha-de-Pagamento-ou-Banco-de-Horas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31898192178583)** **Tempo aproximado para leitura:****00:01:30 min**  
  
**Dúvida**  
Como cadastrar os eventos para Folha de Pagamento ou Banco de Horas?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Para termos um evento corretamente cadastrado para apontamento em Folha de Pagamento, devemos possuir alguns cadastros obrigatórios:  
  
Primeiramente, acesse a rotina de cadastros de eventos, em A**tualizações > Cadastro do Ponto > Eventos**, clique em incluir ou alterar e siga com a configuração de acordo com a necessidade:  
  
**Cadastros de Eventos Folha de Pagamento:**  
- Na primeira aba, **é necessário uma verba de folha cadastrada**, além do Tipo de Código (Provento, Desconto, Base Provento ou Base Desconto) e a classificação do evento.  
![41.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360009354312)  
  
- Na segunda aba, é necessário termos os campos para **Banco de Horas** cadastrados como **Não** e 0,00% com apenas o campo **Perc.F.Pagto = 100%** para indicarmos ao sistema que a totalidade daquele evento será contabilizado em Folha de Pagamento.  
![42.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360009376111)  
  
**Cadastro de evento para Banco de Horas:**  
Para termos um evento corretamente cadastrado para apontamento em Banco de Horas, devemos ter alguns cadastros obrigatórios:  
  
- Na primeira aba, **não** teremos neste caso o código da verba cadastrado.  
![43.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360009376571)  
  
- Na segunda aba, os campos obrigatórios para a contabilização em Banco de Horas são os destacados abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416032631575)  
  
**Importante:** O campo Percentual (**P9\_BHPERC**) refere-se a valorização do evento de Banco de Horas que será contabilizado, no exemplo acima deixamos como **200,00** pois esse evento é de uma Hora Extra valorizada a **100%**. Para saber mais sobre exemplo de valorização de eventos, segue a documentação:  
[RH - Linha Protheus - PON - Forma correta de cadastro para valorizar evento de Banco de Horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058922053-RH-Linha-Protheus-PON-Forma-correta-de-cadastro-para-valorizar-evento-de-Banco-de-Horas?source=search)  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Como utilizar o cadastro de evento do ponto eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407450836887-RH-Linha-Protheus-PON-Como-utilizar-o-cadastro-de-evento-do-ponto-eletr%C3%B4nico?source=search)  
[RH - Linha Protheus - PON - Configuração para Banco de Horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013674751-RH-Linha-Protheus-PON-Configura%C3%A7%C3%A3o-para-Banco-de-Horas?source=search)  
[RH - Linha Protheus - PON - Como cadastrar os eventos de Fechamento de Banco de Horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018706631-RH-Linha-Protheus-PON-Como-cadastrar-os-eventos-de-Fechamento-de-Banco-de-Horas?source=search)  
[RH - Linha Protheus - PON - Banco de Horas não é calculado e não grava registro na tabela](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047548594-RH-Linha-Protheus-PON-Banco-de-Horas-n%C3%A3o-%C3%A9-calculado-e-n%C3%A3o-grava-registro-na-tabela?source=search)
