---
article_id: 5700420152471
category: eSocial - Gerar XML/ Integração Evento
content_hash: d58340e49cc451973f5b200b6fdc97e7e91c269001ccaa1ce2cde05289a5ecbe
fetched_at: '2026-06-28T22:47:11.839383+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: ' RH - RM - FOP - eSocial - O campo ''cnaePrep'' do registro ''dadosEstab''
  é obrigatório e não está preenchido'
type: support-article
updated_at: '2024-04-05T14:49:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5700420152471--RH-RM-FOP-eSocial-O-campo-cnaePrep-do-registro-dadosEstab-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **02:00:00 min****Dúvida**Ao gerar XML é apresentada a mensagem **O campo 'cnaePrep' do registro 'dadosEstab' é obrigatório e não está preenchido.**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**Para correção da ocorrência favor realizar as validações abaixo:  
• Parâmetro **Utiliza tomadores de serviço** estiver **marcado**  
1. Deverá verificar  no cadastro do Cliente Fornecedor em **Anexos | eSocial** se o parâmetro **Considera dados da filial** estiver marcado buscará da seção que está vinculada a Filial.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9191572544279/mceclip2.png)

2. Se o parâmetro **Considera dados da filial** no cadastro de cliente fornecedor estiver desmarcado buscará do campo **Atividade Econômica (CNAE 2.0).**

*![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9191491323927/mceclip0.png)*

*•* Parâmetro **Considera dados da filial** no cadastro CEI/Cliente Fornecedor    
1.  Quando há CEI vinculado, o sistema considera da seção que vinculada a Filial caso parâmetro esteja marcado.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9191829065367/mceclip3.png)

2. Se o parâmetro **Considera dados da filial** no cadastro de CEI do Cliente/fornecedor estiver desmarcado buscará do campo **Atividade Econômica (CNAE 2.0).  
  
*•*** Parâmetro **Utiliza tomadores de serviço** estiver **desmarcado**Quando não utiliza tomadores de serviço, o sistema buscará da seção vinculada ao funcionário do campo **CNAE Preponderante** se este estiver preenchido, senão recupera valor do campo **CNAE 2.0.**

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9194953627927/mceclip4.png)**

**Saiba mais**Para mais informações acesse:

***•*** [Evento S-1005](https://tdn.totvs.com/display/public/LRM/Evento+S-1005)
