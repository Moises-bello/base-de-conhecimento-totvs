---
article_id: 26684403076247
category: LOGIN
content_hash: 7b42d25e739a45b7f92d5d573d961367dd9521a0f758164fdbc2c2705acb930b
fetched_at: '2026-06-28T22:44:40.401195+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - MEU RH - Qual o cenário correto quando há uma readmissão
  de funcionário antigo, que já pertenceu àquela filial
type: support-article
updated_at: '2025-11-06T20:39:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26684403076247-RH-Linha-Protheus-MEU-RH-Qual-o-cen%C3%A1rio-correto-quando-h%C3%A1-uma-readmiss%C3%A3o-de-funcion%C3%A1rio-antigo-que-j%C3%A1-pertenceu-%C3%A0quela-filial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26684403041303) Tempo aproximado para leitura: **00:04:00 min****Ocorrência**Meu RH apenas apresenta dados de Envelope de Pagamento e Informe de Rendimentos  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26684417151895)  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**O Erro ocorre devido a vinculação incorreta entre **RD0xRDZxSRA**, aonde a RD0 encontra-se amarrada na matricula inativa.  
  
**Solução**Para solucionar essa ocorrência, realizar os seguintes passos:  
  
**1.** Localizar as Matriculas existentes com o mesmo CPF na **SRA**.  
Acessar dentro do **Módulo 07 SIGAGPE** a rotina **Atualizações > Funcionários > Funcionários**  
  
Efetuar um filtro utilizando o CPF para **identificar a matrícula ativa.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26684417152407)  
Conforme filtro efetuado, a matricula ativa é a de código 000036.  
  
**2.** Localizar as Matriculas existentes com o mesmo CPF na **RD0**.  
Acessar dentro do **Módulo 18 SIGATCF**, a rotina **Atualizações > Configurações > Cadastro de Participantes**  
  
Efetuar um filtro utilizando o CPF  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26684403062295)  
  
Analisar se o Cadastro de Participantes está Ativo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26684417154327)  
  
Clicar em Outras Ações > Relacionar Participante  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26684417155479)  
  
Selecionar Ambos e Salvar.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26684403064215)  
  
Será apresentada a tela contendo os parâmetros para preenchimento, selecionar a **Matricula Ativa do funcionário por meio da LUPA no campo Matrícula De? / Matrícula Até?**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26684417158167)  
  
Tela de Parâmetros após preenchimento, clicar em OK.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26684417159703)  
  
Após vinculação efetuar o processo de Iniciar Usuário e Gerar Senha  
[RH - Linha Protheus - MEU RH - Como “Iniciar usuário” e “Gerar Senhas” para o primeiro acesso ao MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiZEE%2FUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA0NDIzNjk1My1SSC1MaW5oYS1Qcm90aGV1cy1NRVUtUkgtQ29tby1JbmljaWFyLXVzdSVDMyVBMXJpby1lLUdlcmFyLVNlbmhhcy1wYXJhLW8tcHJpbWVpcm8tYWNlc3NvLWFvLU1FVS1SSAY7CFQ6DnNlYXJjaF9pZEkiKWM3Zjg2NTY1LTVjYTctNGU1MS1hMGIyLTkyZjkxZDU5ZGViZgY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkidVJIIC0gTGluaGEgUHJvdGhldXMgLSBNRVUgUkggLSBDb21vIOKAnEluaWNpYXIgdXN1w6FyaW%2FigJ0gZSDigJxHZXJhciBTZW5oYXPigJ0gcGFyYSBvIHByaW1laXJvIGFjZXNzbyBhbyBNRVUgUkgGOwhUOhJyZXN1bHRzX2NvdW50aQL%2FAw%3D%3D--4502c5ee86e7fb6ad315e83d1f3da2fbfbe62ac9)

**3.** Localizar as Matriculas existentes com o mesmo CPF na **RDZ**.  
**Acessar: Modulo 07 - Consultas > Cadastros > Genéricos**  
  
Selecionar a tabela RDZ e clique em OK  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26684417160727)  
  
Efetuar um filtro utilizando a coluna Pessoa, **preenchendo o código da RD0**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26684417161367)  
  
**Será apresentada a vinculação da matricula 000021 (Inativa) e 000036 (Ativa).**  
  
Ressaltamos que, quando o funcionário anteriormente, já pertenceu àquela filial, e foi recontratado, será gerado uma nova Matrícula a ele, porém não poderá ser gerado um novo código de Participante, **sendo este único dentro daquele Grupo de Empresa.**  
  
**Saiba Mais:**[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
