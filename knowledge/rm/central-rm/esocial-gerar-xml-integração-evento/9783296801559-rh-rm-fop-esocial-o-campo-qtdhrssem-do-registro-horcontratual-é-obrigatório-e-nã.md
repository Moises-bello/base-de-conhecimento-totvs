---
article_id: 9783296801559
category: eSocial - Gerar XML/ Integração Evento
content_hash: d045adc858ab281dc7c2997af607982d27e7e37fd139a2cf3bd37ec03caff84c
fetched_at: '2026-06-28T22:47:13.088938+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - O campo 'qtdHrsSem' do registro 'horContratual' é
  obrigatório e não está preenchido
type: support-article
updated_at: '2024-12-30T13:05:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9783296801559-RH-RM-FOP-eSocial-O-campo-qtdHrsSem-do-registro-horContratual-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24266724834839)**Tempo aproximado para leitura: **00:01:30 min****Ocorrência**Ao realizar a geração do XML dos eventos **S-2200**, **S-2206** ou a validação da base de dados do **S-2200**, é apresentada a mensagem de erro **O campo 'qtdHrsSem' do registro 'horContratual' é obrigatório e não está preenchido.****Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Esse erro geralmente é apresentado quando o campo **N****úmero de Horas** no cadastro de horário vinculado ao funcionário não está preenchido.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesso o cadastro do funcionário **Administração de Pessoal | Funcionário;**1.1. Acesse a aba **Salário/Jornada** no cadastro do funcionário e edite o **Horário;**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9776344834327)

1.2. Certifique que o campo **Número de Horas** do horário esteja preenchido. Caso não esteja, verifique na aba **Jornada** se existe jornada informadas para o horário em questão;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9776454755863)

2. Ainda no cadastro do horário, verifique na aba **eSocial** o campo **Tipo de jornada e-Social**;  
2.1. Se tiver informado os tipos 3 ou 9, acesse o menu **Configurações | Parametrizador | eSocial | Configurações Gerais 3/7** ;  
2.2. Caso o parâmetro **Considerar jornada mensal do funcionário para cálculo da média de horas da Jornada semanal** **(Tipo da Jornada: 3 e 9)** esteja marcado, deve ser preenchido o campo **Divisor da Jornada Mensal** ou **Fórmula do Divisor da Jornada Mensal.**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9776566038935)

**Saiba mais**Para outras informações, acesse:[- Erro O campo 'tpJornada' do registro 'horContratual' é obrigatório e não está preenchido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005166742-RH-RM-FOP-eSocial-Erro-O-campo-tpJornada-do-registro-horContratual-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido?source=search)
