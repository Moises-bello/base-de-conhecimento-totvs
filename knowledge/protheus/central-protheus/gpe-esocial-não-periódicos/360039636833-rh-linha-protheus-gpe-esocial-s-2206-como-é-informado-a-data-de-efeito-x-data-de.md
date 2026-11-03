---
article_id: 360039636833
category: GPE - eSocial - Não Periódicos
content_hash: 25e3c139a13d7715ff3cc13b791c9582e990983efdc2024e746da50e38e1dd89
fetched_at: '2026-06-28T22:45:04.681782+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2206 - Como é informado a Data de Efeito
  x Data de Alteração na alterações realizadas no GPE
type: support-article
updated_at: '2026-06-16T11:26:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039636833-RH-Linha-Protheus-GPE-eSocial-S-2206-Como-%C3%A9-informado-a-Data-de-Efeito-x-Data-de-Altera%C3%A7%C3%A3o-na-altera%C3%A7%C3%B5es-realizadas-no-GPE
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19462866085655)**Tempo aproximado para leitura: 00:**02:00 min**  
  
**Dúvida**  
S-2206 - Como é informado a Data de Efeito x Data de Alteração na alterações realizadas no GPE?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**  
Quando informado no cadastro do Trabalhador a alteração salarial ao gravar a informação o GPE gera o evento S-2206 levando a informação da **data de alteração** (tag <dtAlteracao>) igual a data preenchida no campo RA\_DATAALT, que também será a mesma informação alimentadas nas tabelas SR3 e SR7.  
  
![](https://totvssuporte.zendesk.com/attachments/token/aIycjFAq50oPbCUsWs4QTIOd8/?name=inline-383424045.png)​  
  
Para quem utiliza a rotina de Dissidio Retroativo ou Reajuste do GPE e demais disponíveis no módulo de Cargos e Salários, ao integrar os aumentos Salariais com o GPE a informação não é enviada automaticamente com o TAF, para isso será necessário parametrizar o **Job/Schedule** e assim que executado ele leva as informações também com a **data de efeito** que é alimentada com os parâmetros do Dissidio.  
  
![](https://totvssuporte.zendesk.com/attachments/token/JS1tdbPpMVynalt5tFzQHKvxl/?name=inline498813165.png)​​  
  
O fato é que a **data de alteração** é obrigatória para o evento S-2206 e a **data de efeito** não, justamente por ela ser necessária somente em alguns cenários de alteração com efeito retroativo e para isso será necessário utilizar a rotina de Dissidio Retroativo.  
  
Segue a documentação de nossa consultoria de segmentos relacionado ao evento S-2206 nessa situação:  
[**http://tdn.totvs.com/x/F5xWFw**](http://tdn.totvs.com/x/F5xWFw)**.**  
  
Acesse o artigo disponível no link abaixo para mais informações sobre o **Job/Schedule** e como parametriza-lo:  
[MP - GPE - eSocial - S-2206/S-2230 - Como funciona o Job/Schedule na prática referente a integração das Alterações Salariais e Fim de Afastamento com o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035063413)  
  
**Importante:** Caso não queira utilizar o Job/Schedule para realizar essa integração poderá utilizar a rotina [Geração de S-2206/S-2306 em lote,](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039570633) porém é importante lembrar que a utilização dessa rotina não será integrado a data efeito e descrição com a informação alteração salarial  
  
  
**Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[Artigos S-2206](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055237854)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
  
Próximos Treinamentos  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
