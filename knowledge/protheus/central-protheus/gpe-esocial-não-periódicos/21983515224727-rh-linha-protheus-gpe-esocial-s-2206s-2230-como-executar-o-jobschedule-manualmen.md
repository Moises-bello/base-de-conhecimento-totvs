---
article_id: 21983515224727
category: GPE - eSocial - Não Periódicos
content_hash: 8d496161dbd4a29968f2078abf244fca6445d39e2e580040cfa3ac0141ade134
fetched_at: '2026-06-28T22:45:04.795912+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2206/S-2230 - Como executar o Job/Schedule
  manualmente na tela PO UI
type: support-article
updated_at: '2026-06-16T11:47:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21983515224727-RH-Linha-Protheus-GPE-eSocial-S-2206-S-2230-Como-executar-o-Job-Schedule-manualmente-na-tela-PO-UI
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21983501397783)** Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como executar o *Job/Schedule* manualmente?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**O *Job/Schedule* pode ser executado manualmente, basta acessar pelo o SIGACFG para acessar a rotina.  
Caminho: Ambiente > *Schedule* > *Schedule*.   
  
Verifique se o status do schedule encontra-se 'em execução' na *Home*:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21983515162263)

O status do Agente deve estar iniciado:  
![iniciar agentes.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/21983515166103)

Nos agendamentos, pressione 'Executar Agora' nas opções da rotina que deseja executar manualmente, conforme imagem abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21983501413655)  
  
Importante: Antes de realizar a configuração, é importante realizar as seguintes validações:  
  
- Para que o S-2206 gere com a tag <dtAlteracao> utilizando a data da alteração salarial (R3\_DATA), o parâmetro **MV\_DTALTSA** deve estar falso:  
[RH - Linha Protheus - GPE - eSocial - S-2206 - Como utilizar o parâmetro MV\_DTALTSA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9295167803287-RH-Linha-Protheus-GPE-eSocial-S-2206-Como-utilizar-o-par%C3%A2metro-MV-DTALTSA?source=search)  
  
- Sempre que integrado com o TAF os eventos S-2206/S-2306 (Alteração de contrato ou salário) e S-2230 (Término de afastamento temporário com data futura), o campo de integração com o TAF será preenchida. Caso não haja informação de integração com o TAF no SIGAGPE, quando executado o *job schedule* irá integrar essas informações, mesmo que já tenha as informação no SIGATAF e/ou eSocial.   
Por exemplo: No histórico de salário o campo 'Campo Integ. TAF (R3\_INTGTAF)' está vazio, ao executar o *job shedule* será integrada a informação e o campo 'Campo Integ. TAF (R3\_INTGTAF)' será preenchido.  
  
Para saber como parametrizar o *Job/Schedule* acesse os artigos:

* [RH - Linha Protheus - GPE - eSocial - S-2206/S-2230 - Como configurar o job schedule GPEM026B](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5220215589527-RH-Linha-Protheus-GPE-eSocial-S-2206-S-2230-Como-configurar-o-job-schedule-GPEM026B)
* [RH - Linha Protheus - GPE - eSocial - S-2206 - Transmissão de Eventos - Alteração de Cargos e Salários - Job (Schedule) para integração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017458232/)

Para saber como funciona o *Job/Schedule* na prática acesse o artigo:

* [RH - Linha Protheus - GPE - eSocial - S-2206/S-2230 - Como funciona o Job/Schedule na prática referente a integração das Alterações Salariais, fim de afastamento, trocas de turno e alteração na função com o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035063413)

Para problemas de integração com o *Job/Schedule* após realizar as configurações mencionadas em nossas documentações, nos retorne com as validações e com o arquivo [console.log](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035487834-RH-Linha-Protheus-GPE-Como-gerar-o-Console-log-para-an%C3%A1lise-do-Suporte)

**Saiba Mais**Para saber mais consulte os *links*abaixo:   
[Artigos S-2206](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055237854)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
  
Próximos Treinamentos  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
