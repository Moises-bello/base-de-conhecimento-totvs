---
article_id: 4406151311511
category: RH - Cadastros
content_hash: d3181a5bd5c832706aaf1212ac052f6951eb85561efb4379785e94c709adaf22
fetched_at: '2026-06-28T22:44:53.007242+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Funcionalidade do evento de Nona Hora no Ponto
  Eletrônico
type: support-article
updated_at: '2026-02-24T20:47:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406151311511-RH-Linha-Protheus-PON-Funcionalidade-do-evento-de-Nona-Hora-no-Ponto-Eletr%C3%B4nico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29394090943767) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Como funciona o apontamento de evento de Nona Hora no Ponto Eletrônico?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico – todas as versões  
  
**Solução**  
A Nona Hora do Ponto Eletrônico serve para apontar em evento específico a primeira hora extra que o funcionário fez no dia.  
  
O evento de Nona Hora possui um **ID específico** para tratamento, que é o **025A**, e pode ser ativado através da Tabela de Horário Padrão, no campo Nona Hora.   
  
Para configurar siga as instruções abaixo:  
  
- Cadastrar o evento 025A em **Atualizações > Cadastro do Ponto > Eventos**.  
- Como o evento de Nona Hora trata sobre Horas Extras, ele deve ser de tipo Provento**,** mas a Classificação deve ser ZZ - Outros. Ele   
- Não deve ser vinculado aos Tipos de Horas Extras pois como citado, possui ID específico (025A), e eventos de Horas Extras não possuem ID.  
- O cliente determina se ele deverá ser pago em Folha ou Banco de Horas, conforme esta documentação: [RH - Linha Protheus - PON - Como cadastrar os eventos para Folha de Pagamento ou Banco de Horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013459532-RH-Linha-Protheus-PON-Como-cadastrar-os-eventos-para-Folha-de-Pagamento-ou-Banco-de-Horas?source=search)  
  
Exemplo de cadastro para gerar o evento em resultados para integrar com a folha:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31649546074135)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31649546076311)  
  
  
Exemplo de cadastro para gerar o evento no banco de horas (SPI):  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31649546076695)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31649574418839)  
  
  
Após cadastro do evento de acordo com a necessidade, para demonstrar sua utilização, configurar a Tabela de Horário Padrão, em **Atualizações > Cadastro do Ponto > Tabela de Horário Padrão**, filtre o cadastro desejado e clique no botão alterar.  
  
Abaixo exemplo com horário das 08h - 12h - 13h - 17h, **coluna Nona Hora** deixar a opção **SIM**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31649574419607)  
  
  
Na rotina de integrados exemplo no dia 01.07, o funcionário iniciou o expediente às 06h30 e finalizou às 18h, portanto, o sistema apontou 01h no evento de Nona Hora e as demais, em evento de Hora Extra Normal de acordo com o cadastro dos Tipos de Horas Extras ([RH - Linha Protheus - PON - Regras importantes para o cadastro dos Tipos de Horas Extras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060489314-RH-Linha-Protheus-PON-Regras-importantes-para-o-cadastro-dos-Tipos-de-Horas-Extras?source=search)):  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406143774743)  
  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Tabela de Horário Padrão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047920293-RH-Linha-Protheus-PON-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o)
