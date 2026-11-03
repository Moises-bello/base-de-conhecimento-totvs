---
article_id: 1500005080301
category: eSocial - Tabelas/Não Periódicos
content_hash: 9d80c10f880b151cef1177ecc6eb10e7d3d7b2d5e731903d1c17d891f7e3867c
fetched_at: '2026-06-28T22:47:10.487835+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial - Grupo horContratual no S-2200 ou S-2206
type: support-article
updated_at: '2024-06-27T19:25:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005080301-RH-RM-FOP-eSocial-Grupo-horContratual-no-S-2200-ou-S-2206
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17280595585687)**Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como realizar a parametrização necessária para o leiaute do evento S-2200 ou S-2206, relacionada a jornada do funcionário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões.  
  
**Solução**Para a correta amarração da jornada do funcionário, devemos nos atentar não só ao cadastro do funcionário mas também ao cadastro de horários. Acompanhe as orientações abaixo:

1. Em **Administração de Pessoal | Horários**, efetue o cadastramento do horário;  
1.1. Na aba **eSocial**,  informe o **Tipo de jornada e-Social**;  
1.2. Cadastre as jornadas relacionadas ao horário;  
2. Acesse **Administração de Pessoal | Funcionários;**   
2.1. Acesse o menu lateral **Salário/Jornada** e preencha o campo **Jornada**. Este campo será considerado na geração da quantidade média de horas semanais caso o tipo da jornada do horário seja **3** ou **9**;2.2. Ainda em **Salário/Jornada,**vincule o horário ao funcionário e preencha os campos **Contrato de trabalho em regime de tempo parcial** e **Tipo de regime da jornada**;  
3. Transmita os eventos S-2200 para o RET.

Na integração com o TOTVS Educacional será necessário configurar jornadas de professores. Após realizar toda a parametrização de jornada de professores , o parâmetro **Considera horário planejado do Chronus para o professor** deverá estar desmarcado, em **Administração Pessoal | Funcionários | Processos | Parametrizar Funcionário | Horário**.  
  
**Importante**  
Caso **Configurações | Parametrizador | eSocial | Registros Inativos a Desconsiderar** o parâmetro **Desconsidera Horários Inativos** esteja marcado, o sistema não irá visualizar as informações do horários inativos na geração do S-2200 ou S-2206. O mesmo irá ocorrer se no item Horários a Desconsiderar for indicado determinado evento.  
  
**Saiba mais**  
Para mais informações, acesse:  
      • [Configurações das jornadas](http://tdn.totvs.com/pages/releaseview.action?pageId=185741914)
