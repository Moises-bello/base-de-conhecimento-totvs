---
article_id: 9788644766615
category: eSocial - Gerar XML/ Integração Evento
content_hash: afbc25fe16325885f719a87cccd433a3a4ef2bcb5d7c361dbd5641940f0d8c73
fetched_at: '2026-06-28T22:47:12.087655+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 106 na integração do S-2200 com Governo: Foi
  localizado no sistema um evento em duplicidade com o evento a ser enviado, mesmo
  Tipo de Inscrição, Numero de Inscrição, CPF, Matrícula'
type: support-article
updated_at: '2024-12-30T13:51:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9788644766615-RH-RM-FOP-eSocial-Erro-106-na-integra%C3%A7%C3%A3o-do-S-2200-com-Governo-Foi-localizado-no-sistema-um-evento-em-duplicidade-com-o-evento-a-ser-enviado-mesmo-Tipo-de-Inscri%C3%A7%C3%A3o-Numero-de-Inscri%C3%A7%C3%A3o-CPF-Matr%C3%ADcula
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00****:01:30 min****Ocorrência**Ao transmitir o evento S-2200 para o governo é retornado a inconsistência **O evento ID 'ID xxxxxxxxxxxxxxxxxxxxxxxxxxx' foi rejeitado pelo RET. Erro código 106. Foi localizado no sistema um evento em duplicidade com o evento a ser enviado, mesmo Tipo de Inscrição, Numero de Inscrição, CPF, Matrícula**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9804312932759)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Esse incidente ocorre ao enviar o evento S-2200 e, ao recepciona-lo o governo identifica que o cadastramento já consta no portal do eSocial (com a mesma matrícula, CPF, Tipo de Inscrição e Número de Inscrição), causando assim duplicidade.  
  
**Solução**Para solucionar é necessário sincronizar o evento que já consta na base de dados do eSocial, trazendo-o para o sistema RM e/ou TAF ou realizar retificação se necessário conforme orientações abaixo:  
**• Envio pelo** **Middleware**  
1. Acesse **Esocial** | **Fila de Eventos Não Periódicos** e realize um filtro para chapa do funcionário para consultar se existe um S-2200 Aceito RET, além do rejeitado pelo RET;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9981339917591)

2. Caso já exista o S-2200 na Fila de Eventos de inclusão aceito pelo RET, verifique a necessidade de encaminhar uma [retificação do S-2200;](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005056141-RH-RM-FOP-eSocial-Retifica%C3%A7%C3%A3o-dos-eventos-de-funcion%C3%A1rios-S-2200-S-2205-S-2206-S2300-e-S-2306?source=search)   
3. Caso não identifique outro S-2200 na **Fila de Eventos Não Periódicos,** poderá ajustar o recibo no evento que foi Rejeitado pelo RET.  
     3.1. Para isso, acesse o **Portal do eSocial** e consulte o **Número do recibo** daquele correspondente ao que se encontra rejeitado. O número do recibo estará disponível ao final da página que exibe as informações do evento em questão;

![](https://nasajon-atendimento.s3.us-west-2.amazonaws.com/atendimento/imagens/5df7d95aa50a0.png)

     3.2. No evento que está rejeitado, deverá incluir o recibo diretamente no evento no campo **Recibo** e  salve. Já o status deverá ajustar para Aceito RET via banco de dados pelo seu T.I.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9981580294551)

**• Envio pelo TAF**No TAF não é possivel incluir um evento em duplicidade com as mesmas informações, pois será validado ao tentar integrar com do RM para TAF. Dessa forma, o evento rejeitado deve possuir as mesmas informações que estão no Governo. Será necessário ajustar o recibo deste evento no TAF para modificar o status para aceito pelo RET conforme abaixo:  
1. Acesse o TAF no menu **Atualizações | Eventos eSocial | Trabalhador | Cadastro Trabalhador** e localize o funcionário em questão e realize o [ajuste de recibo;](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019678672-TAF-FUNCIONALIDADES-Como-realizar-ajuste-de-recibo-do-e-Social-no-TAF?source=search)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9981883573911)

2. Após salvar, poderá executar o processo [**Atualização de Status da Integração com o TAF**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015722272-RH-RM-FOP-eSocial-Status-do-evento-no-RM-divergente-do-status-do-evento-no-TAF?source=search) para ajustar o recibo e status na **Fila de Eventos** no RM.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9982086742039)
