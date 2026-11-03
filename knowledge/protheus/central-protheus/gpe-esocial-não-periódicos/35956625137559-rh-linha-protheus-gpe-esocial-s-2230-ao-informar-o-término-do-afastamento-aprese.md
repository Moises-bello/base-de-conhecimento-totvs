---
article_id: 35956625137559
category: GPE - eSocial - Não Periódicos
content_hash: ce0f0b843124ecdaff2e157cd8a19a6a7896272130f2aa540d838a96881c7cff
fetched_at: '2026-06-28T22:45:06.054945+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-2230 - Ao informar o término do afastamento
  apresenta mensagem: Problema 000007'
type: support-article
updated_at: '2025-10-29T18:37:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35956625137559-RH-Linha-Protheus-GPE-eSocial-S-2230-Ao-informar-o-t%C3%A9rmino-do-afastamento-apresenta-mensagem-Problema-000007
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35956640238999) Tempo aproximado para leitura: **00:03:00**  
  
**Dúvida**  
Ao informar o término de um afastamento apresenta a mensagem 'Problema: 000007'  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35956625130519)  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**  
Sempre que integrado o afastamento do GPE para o TAF é preenchido no cadastro de ausência no GPE o campo 'TAF Key' com a mesma chave gravada nas tabelas do TAF.  
  
Quando realizado alguma alteração no afastamento somente no TAF (não sendo realizada do GPE para o TAF) a 'TAF Key' do TAF com GPE ficam diferente, perdendo a integridade dessa informação  
  
**Solução**  
Realizar os seguinte passos:

* Altere o cadastro de ausência do GPE e excluindo a chave do campo 'TAF Key Inicio' desse afastamento e grave;
* Acesse novamente o cadastro de ausência no GPE e informe somente a data término do afastamento;
* Verifique se o registro foi gravado e integrado com o TAF corretamente.

**Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[RH - Linha Protheus - GPE - eSocial - S-2230 - Erro de Predecessão, não foi possível encontrar o registro predecessor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029010132-RH-Linha-Protheus-GPE-eSocial-S-2230-Erro-de-Predecess%C3%A3o-n%C3%A3o-foi-poss%C3%ADvel-encontrar-o-registro-predecessor)   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "**Eventos**".*
