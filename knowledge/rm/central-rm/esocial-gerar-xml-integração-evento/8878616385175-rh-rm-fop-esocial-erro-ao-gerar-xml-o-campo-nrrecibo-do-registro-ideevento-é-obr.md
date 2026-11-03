---
article_id: 8878616385175
category: eSocial - Gerar XML/ Integração Evento
content_hash: 520800e4b1bded1b0924fde0a91e712386f29db2aff45fdcfd1ab1929b1f6008
fetched_at: '2026-06-28T22:47:12.231371+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar XML: O campo ''nrRecibo'' do registro
  ''ideEvento'' é obrigatório e não está preenchido'
type: support-article
updated_at: '2024-06-20T16:15:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8878616385175-RH-RM-FOP-eSocial-Erro-ao-gerar-XML-O-campo-nrRecibo-do-registro-ideEvento-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura:**00:01:00 min  
  
Ocorrência**A mensagem de erro: **O campo 'nrRecibo' do registro 'ideEvento' é obrigatório e não está preenchido**, ocorre ao gerar o XML.   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O erro geralmente ocorre quando não consta no XML a *tag* **nrRecibo** do grupo **ideEvento**, cujo preenchimento é obrigatório em caso de retificação de evento.  
  
**Solução**  
Conforme leiaute do eSocial, a *tag* **nrRecibo**, do grupo **ideEvento**, deve ser preenchida sempre que o indicativo de retificação for igual a 2, ou seja, quando o evento for de **retificação**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8878352778135/mceclip0.png)

Deve-se verificar se o processo de retificação foi corretamente seguido, conforme documentos de orientação abaixo, visto que o número do recibo será puxado automaticamente pelo RM (em caso de Middleware) ou TAF:  
- [Retificação dos eventos de funcionários - S-2200, S-2205, S-2206, S2300 e S-2306](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005056141)  
- [Retificação do evento S-2230 ou S-2231](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003089812)  
- [Retificação do evento de rescisão/desligamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017501692)  
- [Retificação do evento S-1200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028334171)  
  
**- Cliente Middleware**  
Caso a coligada esteja com o Middleware cadastrado, é necessário validar a existência do evento original na base de dados. O evento original precisa existir na base juntamente com seu protocolo, conforme retorno do governo, para que o sistema busque automaticamente o valor do recibo na *tag* **nrRecibo**.

Caso o evento original não exista na base de dados, o usuário poderá:  
- [Importar o evento original para a fila de eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409754644759) e, após importação, gerar o processo de retificação  
- [Editar o XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409629817111) de retificação incluindo manualmente a *tag* **nrRecibo**  
  
**- Cliente TAF**  
Caso a coligada esteja configurada com a integração padrão com o TAF, deve-se validar o XML do TAF. Isso porque, em alguns casos, o RM irá gerar a retificação com a *tag* **nrRecibo** vazia ou com o ID do evento, ficando o TAF responsável por alterar o XML posteriormente com o recibo do evento original.  
  
**Saiba mais**  
Para mais informações, acesse:  
     - [Mapeamento dos eventos eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409020102679)
