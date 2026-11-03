---
content_hash: 1868351c055aa96754edd129d666df956d61b6a465d1e4e5e0ede356ddb204eb
fetched_at: '2026-06-29T00:06:28.247955+00:00'
page_id: '233752878'
product: rm
source: tdn-rm
title: EDU0006 -1 Passos de como se configurar o LMS FLUIG com o WS do RM
type: documentation
url: https://tdn.totvs.com/display/LRM/EDU0006+-1+Passos+de+como+se+configurar+o+LMS+FLUIG+com+o+WS+do+RM
version: 6
---

# Assunto: Passos de como se configurar LMS FLUIG com o WS do RM

|  |  |
| --- | --- |
| **Produto:** | TOTVS Educacional x LMS FLUIG |
| **Versões:** | 12.1.10 |
| **Ocorrência:** |  |
| **Ambiente:** | SQL |
| **Passo a passo:** | [Configurando Integrações via EAI](http://tdn.totvs.com/pages/viewpage.action?pageId=212894462)**Índice** Objetivo  O objetivo deste guia é habilitar e configurar o console EAI para a utilização nas integrações com TOTVS Vitae e TOTVS Educacional.    Passos para configurar EAI no LMS FLUIG    1º ) Logar com Administrador do FLUIG    Painel de Controles      Aprendizado | Console EAI    Informar neste campo : Fluig em Hostname  Username : Usuário adm do FLUIG  Password : Senha do Usuário Fluig  OBS : tem que estar marcada a opção : SKIP VALIDATION      Clicar em Configuration | Host Application  Available Transactions ( Deixar todas as Transações Iguais entre uma coluna e outra ) como mostra a imagem acima.      Adicionar ws do RM  Clicar em ( External Applications )    Neste momento é informado o WS do RM com sua Porta , usuário e senha .  Como configurar o WS e selecionar a porta em : <http://tdn.totvs.com/pages/releaseview.action?pageId=233742226>    Conexão testada com sucesso    Clicar em : Send Routes    Selecionar em External Application ( RM ) em seguida ( Save Changes )    Clicar em ( Painel de Controle | Agendador de Tarefas )          Criar os processos :  Processar mensagem do EAI  Processar requisições de matrícula  Ambos – Processar a Cada minuto      <http://10.31.6.21:8080/lms/services/EAIService?wsdl>  EAI default enviado para o RM ( Alterando apenas o IP na qual encontra-se instalado o FLUIG ) |
| **Observações:** |  |
