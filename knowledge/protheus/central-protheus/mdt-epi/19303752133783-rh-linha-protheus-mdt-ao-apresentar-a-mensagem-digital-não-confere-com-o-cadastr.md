---
article_id: 19303752133783
category: MDT - EPI
content_hash: 02e863d937ad6524539f7abe9cedf8f6afa62be0e8512ae88c7f3f69136a945e
fetched_at: '2026-06-28T22:44:25.208619+00:00'
product: protheus
section_id: 360010945554
source: central-protheus
title: RH - Linha Protheus - MDT - Ao apresentar a mensagem "Digital não confere com
  o cadastro deste funcionário" o que deve ser avaliado
type: support-article
updated_at: '2023-11-27T17:10:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19303752133783-RH-Linha-Protheus-MDT-Ao-apresentar-a-mensagem-Digital-n%C3%A3o-confere-com-o-cadastro-deste-funcion%C3%A1rio-o-que-deve-ser-avaliado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19303736849175) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Digital não confere com o cadastro deste funcionário  
![Erro.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19303752113943)  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**  
Esse erro é gerado quando o leitor biométrico não identifica a digital cadastrada do funcionário, seja por falha na hora do cadastro, utilização do dedo que não foi cadastrado no leitor, entre outros.  
  
**Solução**  
Para solucionar esse problema, será necessário realizar novo cadastro das digitais do funcionario na rotina **Ficha Médica**. No módulo de Medicina e Segurança do Trabalho **(SIGAMDT - opção 35),** acesse a rotina através do caminho **Atualizações > Atendimento Médico > Ficha Medica.** Encontre o cadastro do funcionario e clique no botão **Alterar**, confira se o campo **Biometria (TM0\_INDBIO)** esta como **"Sim".   
  
![ficha.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19303758773271)**Clique no botão **"Outras Ações > biometria",** ira apresentar a mensagem **"Este colaborador já possui digitais cadastradas, deseja refazer o cadastro?",** clique em **Sim** e realize novamente o processo de cadastro da biometria conforme o help do leitor, ao finalizar clique no botão **Salvar**, para que seja gravado as novas informações.  
  
![Bio.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19303736851863)  
  
**Saiba mais**[Como efetuar a instalação do aparelho FingerTech para biometria no MDT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11169895277207)  
[Como configurar o uso da Biometria no SIGAMDT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11169895277207)[Quais os principais documentações sobre Biometria](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419842630935)[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)
