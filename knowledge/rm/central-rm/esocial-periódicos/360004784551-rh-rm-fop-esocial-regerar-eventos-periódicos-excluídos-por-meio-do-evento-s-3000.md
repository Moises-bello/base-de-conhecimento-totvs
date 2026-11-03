---
article_id: 360004784551
category: esocial - Periódicos
content_hash: 57e3111183181790ded5dcb12fbf448be770ff2cfa83d755554bd88a5e0f0947
fetched_at: '2026-06-28T22:47:09.462314+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Regerar eventos periódicos excluídos por meio do
  evento S-3000
type: support-article
updated_at: '2026-06-01T14:14:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004784551-RH-RM-FOP-eSocial-Regerar-eventos-peri%C3%B3dicos-exclu%C3%ADdos-por-meio-do-evento-S-3000
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27876810871447)****Tempo aproximado para leitura: 00:02:30 min**

**Dúvida**  
Qual o procedimento para excluir e regerar os eventos periódicos no TOTVS Folha de Pagamento?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
Foi implementado em versões anteriores às atuais de mercado a possibilidade de regerar registros dos eventos periódicos que foram excluídos.

Para efetuar a exclusão através do S-3000, siga os seguintes passos:  
1. Acesse **eSocial | Eventos Periódicos**;  
2. Selecione o registro de evento desejado e clique em  **Processos | Gerar Evento de Exclusão (S-3000)**;  
3. Acesse **eSocial | Fila de Eventos** para localizar o evento S-3000 gerado e transmiti-lo ao governo.  
  
O evento **S-3000** irá referenciar o evento a ser excluído inserindo na estrutura de XML os dados do ID (identificação do evento) bem como o tipo de evento, período de apuração e outros dados relevantes.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045249953)

Após transmitir o evento **S-3000**com sucesso poderá ser gerado, caso necessário, um novo XML do evento excluído. Para isso, siga os passos abaixo:  
1. Acesse **eSocial | Gerar XML( Eventos Periódicos)**;  
2. Selecione a opção **Gerar novo XML para evento excluído através do S-3000** juntamente com o tipo do evento a ser gerado;  
3. Execute o processo para que seja criado o evento correspondente.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044395554)

**Importante**  
Apesar de ser possível excluir eventos não-periódicos através do S-3000, o processo supracitado só é possível para eventos periódicos.  
  
**Saiba Mais**  
Para mais informações acesse:  
      • [S-3000 - Exclusão de Eventos](http://tdn.totvs.com/pages/releaseview.action?pageId=364908560)  
      • [Como realizar a geração dos Eventos Periódicos?](http://tdn.totvs.com/pages/releaseview.action?pageId=382543401)
