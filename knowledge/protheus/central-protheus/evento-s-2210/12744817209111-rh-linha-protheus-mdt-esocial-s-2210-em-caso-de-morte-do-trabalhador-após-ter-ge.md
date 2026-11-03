---
article_id: 12744817209111
category: Evento S-2210
content_hash: f8ebb42589d8bd5872197a60b9846c83827bea9ff33978fc9dda2b8dd0cc0dd8
fetched_at: '2026-06-28T22:45:24.466283+00:00'
product: protheus
section_id: 8260521640983
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2210 - Em caso de morte do trabalhador
  após ter gerado CAT inicial como gerar CAT por óbito
type: support-article
updated_at: '2024-04-29T12:34:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12744817209111-RH-Linha-Protheus-MDT-eSocial-S-2210-Em-caso-de-morte-do-trabalhador-ap%C3%B3s-ter-gerado-CAT-inicial-como-gerar-CAT-por-%C3%B3bito
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23085404473367) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Em caso de morte do trabalhador após ter gerado CAT inicial, como gerar CAT por óbito.  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução****1-** No módulo TAF (84), na rotina *Atualizações - Eventos eSocial - Não Periódicos - CAT Comun.Acid.Trab.* (**TAFA257**) deve constar o registro inicial com protocolo gerado pelo Governo.   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12744936986519)  
  
**2-** No módulo SIGAMDT (35), na rotina *Atualizações - Acidente Trabalho - Acidentes* (**MDTA640**) no registro inicial, deve conter a informação do protocolo no campo TNC\_RECIBO (mesmo código da rotina do TAF):  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12745020617111)  
  
Após certificar as informações citadas, deverá incluir um novo Acidente, informando os campos **Tipo CAT** (TNC\_TIPCAT), **Data Óbito** (TNC\_DTOBIT) e **Houve Morte** (TNC\_MORTE):  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12745096490647)  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12745209349911)  
  
Lembrando que o registro deve estar com o Número de Protocolo da CAT Origem, conforme citado acima.   
  
Após clicar em Salvar, é apresentado mensagem que o registro foi integrado com TAF:  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12745221363863)  
  
**3-** Ao acessar a rotina de CAT do módulo TAF, o registro foi criado como "Comunicação de Óbito", veja que o número da CAT origem esta preenchido e esta aguardando o envio desse registro para gerar um novo protocolo:   
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12745271213335)  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12745327148567)  
 **Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
