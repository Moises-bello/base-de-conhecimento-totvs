---
article_id: 11271267628055
category: eSocial - Middleware
content_hash: 48cc74f405bf20dafb0b5d932420a2192dd9db5655836b5cf6a1b9edc709583f
fetched_at: '2026-06-28T22:47:05.561743+00:00'
product: rm
section_id: 1500000834541
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 170 na integração do S-2200 com Governo: O
  contrato de trabalho já se encontra cadastrado na base de dados do Ambiente Nacional
  do eSocial'
type: support-article
updated_at: '2026-01-02T17:16:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11271267628055-RH-RM-FOP-eSocial-Erro-170-na-integra%C3%A7%C3%A3o-do-S-2200-com-Governo-O-contrato-de-trabalho-j%C3%A1-se-encontra-cadastrado-na-base-de-dados-do-Ambiente-Nacional-do-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22566132124951) Tempo aproximado para leitura: **00:02:30 min**  
  
**Ocorrência**  
Ao transmitir o evento S-2200 para o governo é retornado a inconsistência: **O evento ID 'ID xxxxxxxxxxxxxxxxxxxxxxxxxxx' foi rejeitado pelo RET. Erro código 170: O contrato de trabalho já se encontra cadastrado na base de dados do Ambiente Nacional do eSocial. Ação Sugerida: Verificar a matricula informada e, se já utilizada em S-2190, S-2200 ou S-2300 de outro trabalhador, gerar uma nova matricula**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
Esse incidente ocorre ao enviar o evento S-2200 e, ao recepciona-lo o governo identifica que o cadastramento já consta no portal do eSocial (com a mesma matrícula, CPF, Tipo de Inscrição e Número de Inscrição), causando assim a mensagem.  
  
**Solução**  
Para solucionar é necessário sincronizar o evento que já consta na base de dados do eSocial, trazendo-o para o sistema RM e/ou TAF ou realizar retificação se necessário conforme orientações abaixo:  
**• Envio pelo Middleware**  
1. Acesse **Esocial** | **Fila de Eventos Não Periódicos** e realize um filtro para chapa do funcionário para consultar se existe um S-2200 Aceito RET, além do rejeitado pelo RET;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22566126941591)

2. Caso já exista o S-2200 na Fila de Eventos de inclusão aceito pelo RET, verifique a necessidade de encaminhar uma [retificação do S-2200;](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005056141-RH-RM-FOP-eSocial-Retifica%C3%A7%C3%A3o-dos-eventos-de-funcion%C3%A1rios-S-2200-S-2205-S-2206-S2300-e-S-2306?source=search)  
3. Caso não identifique outro S-2200 na **Fila de Eventos Não Periódicos,** poderá ajustar o recibo no evento que foi Rejeitado pelo RET.  
     3.1. Para isso, acesse o **Portal do eSocial** e consulte o **Número do recibo** daquele correspondente ao que se encontra rejeitado. O número do recibo estará disponível ao final da página que exibe as informações do evento em questão;

![](https://nasajon-atendimento.s3.us-west-2.amazonaws.com/atendimento/imagens/5df7d95aa50a0.png)

     3.2. No evento que está rejeitado, deverá incluir o recibo diretamente no evento no campo **Recibo** e  salve. Já o status deverá ajustar para Aceito RET via banco de dados pelo seu T.I.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22566132154647)

**• Envio pelo TAF**  
No TAF não é possivel incluir um evento em duplicidade com as mesmas informações, pois será validado ao tentar integrar com do RM para TAF. Dessa forma, o evento rejeitado deve possuir as mesmas informações que estão no Governo. Será necessário ajustar o recibo deste evento no TAF para modificar o status para aceito pelo RET conforme abaixo:  
1. Acesse o TAF no menu **Atualizações | Eventos eSocial | Trabalhador | Cadastro Trabalhador** e localize o funcionário em questão e realize o [ajuste de recibo;](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019678672-TAF-FUNCIONALIDADES-Como-realizar-ajuste-de-recibo-do-e-Social-no-TAF?source=search)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22566126970647)

2. Após salvar, poderá executar o processo [**Atualização de Status da Integração com o TAF**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015722272-RH-RM-FOP-eSocial-Status-do-evento-no-RM-divergente-do-status-do-evento-no-TAF?source=search) para ajustar o recibo e status na **Fila de Eventos** no RM.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22566132183831)
