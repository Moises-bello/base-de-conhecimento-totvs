---
article_id: 360024675814
category: eSocial - Gerar XML/ Integração Evento
content_hash: 7854b955f78a9b54d5f6dce73cba341b0f1e220020cd74108d6dde9dcac76436
fetched_at: '2026-06-28T22:47:12.258432+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao transmitir S-2230: Só é permitido enviar
  fim de afastamento para trabalhadores que iniciaram o eSocial afastados'
type: support-article
updated_at: '2024-06-14T16:39:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024675814-RH-RM-FOP-eSocial-Erro-ao-transmitir-S-2230-S%C3%B3-%C3%A9-permitido-enviar-fim-de-afastamento-para-trabalhadores-que-iniciaram-o-eSocial-afastados
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24166812844439) Tempo aproximado para leitura: 00:01:00 min**

**Ocorrência**  
Ao transmitir o evento S-2230 é apresentada a mensagem de rejeição **Só é permitido enviar fim de afastamento para trabalhadores que iniciaram o eSocial afastados.**  
  
 **Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
Esse erro ocorre quando é feito o envio de um evento de afastamento para o funcionário, porém perante o governo ele já encontra-se afastado.  
  
**Solução**Primeiramente verifique no ambiente do governo a situação do funcionário. Veja se na aba **Afastamento Temporário** consta algum afastamento de início ainda sem término. Caso haja, será necessário informar o fim deste afastamento antes enviar o novo afastamento desejado. Nos casos onde existe o retorno deste afastamento no ambiente do eSocial deve atentar-se se este retorno foi feito diretamente pelo site, sendo necessário excluí-lo caso afirmativo.

Para informar o término de um afastamento, siga os passos abaixo:  
1. Identifique se o evento onde é apresentando o afastamento é o S-2230 de início ou o evento S-2200 (casos onde o funcionário está afastado desde o início da obrigatoriedade de envio ao eSocial);  
2. Para os casos onde o afastamento foi informado no S-2200 acesse **eSocial | Outros processos | Gerar gatilho afastamento / férias eSocial** e execute o processo selecionando o parâmetro **Gerar gatilho de término para funcionários afastados na carga inicial**;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10375511898519)

3. Caso o afastamento tenha sido enviado através do S-2230, acesse o histórico de afastamento do funcionário e informe a data de término do afastamento. Será gerado neste caso um gatilho de Término do S-2230 para envio ao governo.  
  
**Importante**Garanta que sua versão esteja atualizada para os últimos *patches*, para que tenha acesso as melhorias implementadas.
