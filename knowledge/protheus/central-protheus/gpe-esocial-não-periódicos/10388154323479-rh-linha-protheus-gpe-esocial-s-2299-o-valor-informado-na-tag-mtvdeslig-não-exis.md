---
article_id: 10388154323479
category: GPE - eSocial - Não Periódicos
content_hash: 44182b202dcb2aff8982a5063a8eb80ba26bb65fa3af234357653b8851dfc816
fetched_at: '2026-06-28T22:45:05.875152+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2299 - O valor informado na tag mtvDeslig
  não existe na base de dados
type: support-article
updated_at: '2026-06-16T11:51:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10388154323479-RH-Linha-Protheus-GPE-eSocial-S-2299-O-valor-informado-na-tag-mtvDeslig-n%C3%A3o-existe-na-base-de-dados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25159640123799) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Ao confirmar a rescisão para gerar o evento S-2299, a mensagem é apresentada "O valor informado na tag **mtvDeslig** não existe na base de dados". Motivo do desligamento não é valido.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10387791388951)  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**  
O erro ocorre por dois motivos, primeiro porque foi criado um campo na tabela S043 que deve estar atualizado e preenchido, e segundo por conta da atualização da tabela S056.   
  
**Solução**  
1.Acesse **Atualizações > Definição Calculo > Manutenção** de Tabelas, selecione a tabela S043 e clique em alterar;  
2.Verifique que existe um **novo campo** referente ao **Motivo eSocial** e um que foi descontinuado (Mot.eSoc (inativo)).  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10405136188055)  
  
Para que seja criado o novo campo, é necessário aplicar os pacotes de atualizações e atualizar o Dicionário de Dados (executar UPDDISTR). [RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
  
Após criação do novo campo na tabela S043, necessário atualizar a tabela S056 - Motivos de Desligamento.  
  
Através do modulo SIGAGPE (07), acesse o caminho: **Atualizações > Definições Cálculo > Manutenção**  
1. Selecione a **tabela S056;**  
2. Clique em Alterar;  
**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10387891075223)**  
  
**3.** Em Outras Ações, clique em **Atualizar Tabela** (F7)  
**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10387971602839)**  
  
Caso esteja na tela de rescisão, **será necessário sair da rotina e entrar novamente**. Calcule a rescisão para que o sistema o evento S-2299 corretamente.  
  
**Observação**  
Caso deseje atualizar as tabelas no TAF (autocontidas) siga as orientações do artigo: [TAF - CONFIGURAÇÃO - Atualização das tabelas autocontidas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034479973)  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[Boletim Técnico Motivo Desligamento S-1.1](https://tdn.totvs.com/display/public/PROT/DRHROTPRT-7495+DT+eSocial+Leiaute+S-1.1+Motivo+de+Desligamento)  
[Leiaute eSocial Trabalhador Temporário](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/leiautes-esocial-nt-05-2022-html/index.html#2200_vinculo_infoRegimeTrab_infoCeletista_trabTemporario)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
