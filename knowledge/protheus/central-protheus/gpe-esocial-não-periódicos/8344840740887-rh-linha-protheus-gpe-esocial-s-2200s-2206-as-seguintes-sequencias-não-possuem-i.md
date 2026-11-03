---
article_id: 8344840740887
category: GPE - eSocial - Não Periódicos
content_hash: 395ba1c9bb0e60186ab075478b3cc2721c93f6f380561d1c8a65f5bb2d546d04
fetched_at: '2026-06-28T22:45:04.595152+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2200/S-2206 - As seguintes sequencias
  não possuem intervalo definido. Rever cadastro de tabela de horário padrão.
type: support-article
updated_at: '2026-06-16T11:52:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8344840740887-RH-Linha-Protheus-GPE-eSocial-S-2200-S-2206-As-seguintes-sequencias-n%C3%A3o-possuem-intervalo-definido-Rever-cadastro-de-tabela-de-hor%C3%A1rio-padr%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41259508446743) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
As seguintes sequencias não possuem intervalo definido. Rever cadastro de tabela de horário padrão  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**  
Essa mensagem é uma advertência e não é impeditiva, ocorre porque na tabela de horário padrão não está definido qual o intervalo corresponde a intrajornada.   
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8344539225751)  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Verificar se o ambiente encontra-se com o último acumulado do RH conforme *link*:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
  
2. Acessar a rotina no SIGAGPE, localizada no menu **Atualizações > Cadastro do Ponto > Tabela de Horário Padrão**  
  
3. Determinar qual dos intervalos será intrajornada e realizar o preenchimento do campo (Interv.SREP) destacado na imagem abaixo:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8344665786775)  
  
Esse campo Indica o intervalo do horário contratual a ser considerado na geração do arquivo de controle de jornada para efeitos fiscais -**ACJEF**.  
  
O sistema válida o campo informado PJ\_INTSREP, o campo indica o intervalo do horário contratual.  
Se sua primeira saída PJ\_INTERV1 for o seu intervalo deixa o campo PJ\_INTSREP como '1° intervalo', caso sua segunda saída PJ\_INTERV2 for seu intervalo, deixe o campo PJ\_INTSREP como '2° intervalo'.  
  
Segue documentação de auxílio:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=630840052>  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
[ChatBot Carol](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
