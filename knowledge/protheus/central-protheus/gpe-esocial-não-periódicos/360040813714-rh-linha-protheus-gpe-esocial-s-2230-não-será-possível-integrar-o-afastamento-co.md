---
article_id: 360040813714
category: GPE - eSocial - Não Periódicos
content_hash: a4bf7733330785531b9336102948d4c20380951589dad9527662f23f66d78b08
fetched_at: '2026-06-28T22:45:05.770993+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2230 – Não será possível integrar o
  afastamento com o TAF pois o registro de Admissão/Carga inicial deste funcionário
  ainda não foi efetivado no TAF ou não foi transmitido para o RET
type: support-article
updated_at: '2026-06-16T11:47:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040813714-RH-Linha-Protheus-GPE-eSocial-S-2230-N%C3%A3o-ser%C3%A1-poss%C3%ADvel-integrar-o-afastamento-com-o-TAF-pois-o-registro-de-Admiss%C3%A3o-Carga-inicial-deste-funcion%C3%A1rio-ainda-n%C3%A3o-foi-efetivado-no-TAF-ou-n%C3%A3o-foi-transmitido-para-o-RET
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41259349848215) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Ao cadastrar um afastamento para o funcionário ocorre a mensagem abaixo:   
"Não será possível integrar o afastamento com o TAF pois o registro de Admissão/Carga inicial deste funcionário ainda não foi efetivado no TAF ou não foi transmitido para o RET"  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053908494)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**  
O mensagem é apresentada devido SIGAGPE não estar encontrando o evento S-2200/S-2300 do funcionário no TAF. Este erro pode ocorrer devido a diversas divergências.  
  
1 - Verifique se o evento S-2200/ S-2300 encontra-se com no TAF com número de protocolo.   
  
2 - Verifique se o código de matrícula do funcionário no SIGAGPE está igual no TAF:  
[MP - GPE - eSocial - S-2200 - Como visualizar a matricula eSocial (RA\_CODUNIC) no SIGAGPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045583393-MP-GPE-eSocial-S-2200-Como-visualizar-a-matricula-eSocial-RA-CODUNIC-no-SIGAGPE?source=search)  
O campo que guarda o código de matrícula do colaborador no TAF fica gravado na aba "informações do vínculo".  
Caminho SIGATAF: Atualizações > Eventos esocial > Trabalhador > Cadastro Trabalhador   
  
![](https://totvssuporte.zendesk.com/attachments/token/R3tOLUFly4N4XKOJGCr90M95l/?name=inline316381243.png)​  
  
3 - Em alguns casos, identificamos que o erro também ocorre devido divergência na data de admissão do GPE e TAF.   
  
**Solução**  
Para a mensagem mencionada, verifique se de fato o funcionário já foi transmitido, possui registro na base do governo com mesmo número de protocolo do sistema e garanta que todas as informações estejam idênticas entre os módulos.  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)
