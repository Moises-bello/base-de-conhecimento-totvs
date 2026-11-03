---
article_id: 360033304194
category: GPE - eSocial - Não Periódicos
content_hash: e0a0caa41eb2a1180fdd30626239afa6aa2c5cc108b55123c282985ff62e504a
fetched_at: '2026-06-28T22:45:04.317689+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE -  Integrar data fim no evento no S-2230
type: support-article
updated_at: '2026-06-16T13:34:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033304194-RH-Linha-Protheus-GPE-Integrar-data-fim-no-evento-no-S-2230
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29485621778327) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Como integrar data fim de um afastamento sem usar o schedule?

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para fazer o afastamento reintegrar com o TAF, o campo a seguir deve ser deletado: R8\_TAFKF(TAFKEYFINAL) caso tenha dados ;  
Após deletar a informação, devem ser alterados os campos, **R8\_DURACAO** e confirme.  
A data da integração deve ser a data da integração do inicio do afastamento( R8\_INTGTAF).  
  
Faça este processo e coloque novamente a quantidade de dias da duração do afastamento para que o sistema consiga integrar o dado, lembrando que deve ser a data fim menor que a data atual.  
  
Na abertura da rotina é possível identificar a informação de que a data de fim do afastamento deve ser **INFERIOR** a data base do sistema, neste caso que avaliamos , a integração manual só ocorre um dia após a data fim.  
  
![](https://totvssuporte.zendesk.com/attachments/token/h5J3QLzRfZzvbHA9gChcoHNIV/?name=inline931265266.png)​

**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "****Eventos****".*
