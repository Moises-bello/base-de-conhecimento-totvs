---
article_id: 39152963991959
category: Assinatura Eletrônica
content_hash: 3b64991287bb86bd6d8b044cbbe590944072ae44cb5b68f4d54b89c9a3335340
fetched_at: '2026-06-28T22:46:25.760388+00:00'
product: rm
section_id: 39151284716695
source: central-rm
title: RH - RM - PTO - Assinatura Eletrônica - Erro na integração do arquivo ao enviar
  o espelho de ponto do RM para o TAE
type: support-article
updated_at: '2026-03-19T17:29:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39152963991959-RH-RM-PTO-Assinatura-Eletr%C3%B4nica-Erro-na-integra%C3%A7%C3%A3o-do-arquivo-ao-enviar-o-espelho-de-ponto-do-RM-para-o-TAE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39152963986583) Tempo aproximado para leitura: **00:01:50 min**  
  
**Ocorrência**

Ao realizar o envio do espelho do cartão para assinatura eletrônica, o processo é finalizado com erro e apresenta a seguinte mensagem: "Erro na integração do arquivo".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152963987095)

**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 12.1.33 e/ou superiores

**Causa**

Este erro ocorre quando existem funcionários selecionados para o processo que não possuem o campo de e-mail preenchido no cadastro ou que estão com endereços de e-mail inválidos.

**Solução**

Para realizar o rastreio e a correção dos cadastros, siga as instruções abaixo:

**Para funcionários com e-mail não preenchido:**

1. Acesse a tela de funcionários.
2. Crie um filtro utilizando a condição **"Email is null"**.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152963987735)
3. Atualize o cadastro dos funcionários listados, informando um endereço de e-mail válido no campo E-mail da aba Identificação.

**Para funcionários com e-mail incorreto/inválido:**

1. Acesse o [**monitor de relatórios**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11004793854359-RH-RM-FOP-Assinatura-Eletr%C3%B4nica-Monitor-de-Relat%C3%B3rios) através do menu **Assinatura Eletrônica** do módulo **Automação de Ponto**.
2. Filtre pelos status **"Job não iniciado"** e **"Id. arquivo assinatura = 0"**.
3. Verifique a coluna **'valor campo chave'**. Nela será possível identificar a chapa do funcionário que gerou o erro.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152963988247)
4. Acesse o cadastro da chapa identificada e faça a correção do e-mail.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39152956262423)

**Saiba mais:**

[**RH - RM - PTO - Relatório do espelho do cartão de ponto x TOTVS Assinatura Eletrônica**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6632723301911-RH-RM-PTO-Relat%C3%B3rio-do-espelho-do-cart%C3%A3o-de-ponto-x-TOTVS-Assinatura-Eletr%C3%B4nica)
