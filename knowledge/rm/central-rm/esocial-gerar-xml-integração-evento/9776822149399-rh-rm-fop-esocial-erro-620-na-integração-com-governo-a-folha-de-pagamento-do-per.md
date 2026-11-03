---
article_id: 9776822149399
category: eSocial - Gerar XML/ Integração Evento
content_hash: fca0b2860843076087f69401c6c6af7440fa8858c6a77fdc9ba4b470bb499579
fetched_at: '2026-06-28T22:47:12.159117+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 620 na integração com governo: A folha de pagamento
  do período já foi fechada, para alterá-la será necessário reabri-la'
type: support-article
updated_at: '2026-06-01T14:11:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9776822149399-RH-RM-FOP-eSocial-Erro-620-na-integra%C3%A7%C3%A3o-com-governo-A-folha-de-pagamento-do-per%C3%ADodo-j%C3%A1-foi-fechada-para-alter%C3%A1-la-ser%C3%A1-necess%C3%A1rio-reabri-la
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20200251162263) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao transmitir ao governo evento com remuneração (S-1200, S-1202, S-1207, S-1210, S-1260, S-1270, S-1280, S-2299, S-2399) para o governo é retornado o erro **Código da Ocorrência: 620 - Descrição: A folha de pagamento do período XXXX-XX  já foi fechada, para altera-la será necessário reabri-la.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9776755769495)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
Essa mensagem de erro ocorre quando o envio do evento periódico é realizado após já possuir um registro **S-1299 - Fechamento dos Eventos Periódicos** processado para o período nessa empresa e **aceito pelo RET.**  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o menu **eSocial | Gerar XML Eventos Periódicos;**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9778495345175)**

2. Selecione somente o evento **S-1298**, e a competência que deseja reabrir;

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9778545114903)

3. Caso já tenha enviado um S-1298 anteriormente no mesmo período de apuração, selecione também o parâmetro **Regerar eventos S-1298 e S-1299**;  
4. Avance o processo para execução;  
5. Acesse a fila de eventos e integre o evento S-1298 com o governo.  
  
**Saiba mais**  
Para mais informações, acesse:  
     - [Geração dos eventos periódicos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003044711)
