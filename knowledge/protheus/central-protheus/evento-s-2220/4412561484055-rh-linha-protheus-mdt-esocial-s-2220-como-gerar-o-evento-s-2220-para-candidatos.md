---
article_id: 4412561484055
category: Evento S-2220
content_hash: 72ed412795cc60814d5cfc6fa87ea61b78ec31a88964b02880bb4bb8d23ae0d7
fetched_at: '2026-06-28T22:45:25.497640+00:00'
product: protheus
section_id: 8260535758103
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2220 - Como gerar o evento S-2220 para
  candidatos que foram admitidos
type: support-article
updated_at: '2025-03-03T18:10:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412561484055-RH-Linha-Protheus-MDT-eSocial-S-2220-Como-gerar-o-evento-S-2220-para-candidatos-que-foram-admitidos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21508783243415) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar o evento S-2220 -Monitoramento da Saúde do Trabalhador para candidatos que foram admitidos?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução** **1-** Deve existir a Ficha Médica do Candidato ( o campo matricula deve ficar em branco). Os demais campos relacionados aos dados do candidato devem ser preenchidos.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412569174807)  
  
**2-** Deve ser inserido um ASO ao Candidato e realizado sua impressão, estando tudo certo com a avaliação médica e demais avaliações relacionados os processo de admissão, este Candidato será direcionado ao RH para efetuar sua admissão.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412561365655)  
  
**3-** Ao realizar sua admissão o candidato passa a ser um funcionário tendo uma matricula vinculada no sistema, essa numeração de matricula deve ser vinculada com a ficha médica do candidato.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412561389079)  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412561393047)  
  
**4-** Para realizar o disparo do evento **S-2220**, deverá retornar no cadastro do atestado **ASO** (MDTA200), selecione o registro com a opção Alterar e salve ( sem realizar qualquer alteração), e na sequencia realize a impressão novamente do Atestado **ASO**, que foi incluído originalmente pelo candidato.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412575621655)  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412569236503)  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412575634199)  
  
Dica: Compartilho as principais causas de erro na geração do evento S-2220   
Observação sobre o procedimento diagnóstico (**TM5\_OBSERV**) do exame deve ser preenchida.   
Rotina (exames do funcionário)  
  
O procedimento diagnóstico (**TM4\_PROCRE)** do exame deve ser preenchido. Rotina (cadastro de exames)  
  
A data de realização do exame (**TM5\_DTRESU**) deve ser preenchida. Rotina (exames do funcionário)   
  
No módulo Medicina é possível incluir uma ficha Médica para um candidato, este controle serve apenas para o módulo medicina para avaliar a saúde do candidato antes de sua admissão e poder gerar seu ASO admissional antes do RH de fato efetivar sua matricula.  
  
**Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)[Artigos Atendimento Médico](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945694-MDT-Atendimento-M%C3%A9dico) **[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)**
