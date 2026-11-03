---
article_id: 360035069294
category: GPE - eSocial - Não Periódicos
content_hash: 7c870608679297aad11d51f51563f0730ea608339b6e3a76d881c09e1a520df6
fetched_at: '2026-06-28T22:45:04.614076+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-2200/S-2206/S-2299 - Transferência:
  Não foi possível efetuar a integração. O trabalhador possui um turno de trabalho
  inválido para o eSocial.'
type: support-article
updated_at: '2026-06-16T11:26:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035069294-RH-Linha-Protheus-GPE-eSocial-S-2200-S-2206-S-2299-Transfer%C3%AAncia-N%C3%A3o-foi-poss%C3%ADvel-efetuar-a-integra%C3%A7%C3%A3o-O-trabalhador-possui-um-turno-de-trabalho-inv%C3%A1lido-para-o-eSocial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19450780207127)**Tempo aproximado para leitura: 00:**02:00 min**  
  
**Ocorrência**  
Na rotina de Transferência é gerado a mensagem "**Não foi possível efetuar a integração. O trabalhador possui um turno de trabalho inválido para o eSocial.**"  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19450780225175)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois não existe o turno de trabalho na empresa de destino que esta transferindo o funcionário, ou o mesmo não está com a configuração correta para os campos  [R6\_TPJORN](https://tdn.totvs.com/pages/releaseview.action?pageId=639938616) e [R6\_ESNOTU](https://tdn.engpro.totvs.com.br/display/public/PROT/DRHESOCP-20467+DT+Cadastro+de+Turno+de+Trabalho)  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acessar a rotina de transferência(**GPEA180**).  
Caminho SIGAGPE: *Atualizações > Funcionários > Transferências*  
  
2. Selecione o campo: **Outras Ações > Config.Campos;**  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046434533)  
  
3. Selecionar os campos referente ao turno de trabalho;  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045579794)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045579854)  
  
4. Na rotina de transferência, selecione a aba "Dados Cadastrais" e informe para qual turno o funcionário será transferido.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045581234)  
  
  
**Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[Artigos S-2200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052505613)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
  
Próximos Treinamentos  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
