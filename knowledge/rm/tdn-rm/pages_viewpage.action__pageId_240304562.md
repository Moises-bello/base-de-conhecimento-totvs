---
content_hash: 148faac2f2c81225dc54fbfa9d0ca95bd9192f71dff9b18c5bca4dd4455281ab
fetched_at: '2026-06-29T00:08:10.485563+00:00'
page_id: '240304562'
product: rm
source: tdn-rm
title: GLB0049_Utilização_da_ferramenta _superv.exe
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240304562
version: 8
---

# Orientações de utilização da ferramenta “superv.exe”

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 11.XX; 12.1.XX |
| **Ocorrência:** | Orientações para utilização da ferramenta superv.exe |
| **Ambiente:** |  |
| **Passo a passo:** | O “superv” é um aplicativo que concede permissão de supervisor em todas as coligadas e sistemas ao usuário “mestre” quando não há nenhum outro usuário supervisor na coligada em questão e existe licença para o módulo na tabela GLICENCA.  1º Execute o aplicativo, aponte a base de dados no campo “Alias” e preencha os campos de usuário e senha (Por default é Usuário “rm”; Senha “rm”)     Obs.: No campo "Alias" serão apresentados todos os Alias criados no BDE confirme se o alias selecionado é o mesmo que deseja realizar o processo.    2º Após executar o aplicativo com os dados corretos, será apresentado uma mensagem similar à mensagem abaixo, informando as permissões concedidas nas respectivas coligadas:      3º Caso já exista um usuário supervisor em todos os sistemas e em todas as coligadas apresentará a seguinte mensagem:      **Aplicativo para download disponível abaixo:**    **250** |
| **Observações:** | **Usuários Supervisores**  ---  Os usuários que possuírem a condição de Supervisor nos aplicativos terão como diferencial, o acesso autorizado em algumas opções que demais usuários comuns não possuirão.  Dessa forma, somente usuários na condição de supervisor terão acesso completo ao cadastro de usuários.  Esta operação deverá ser repetida para cada Coligada que o usuário poderá ter acesso.  Todas as coligadas em todos os sistemas devem possuir pelo menos um usuário supervisor cadastrado e este só terá autorização de alterar permissões de usuários das coligadas em que for supervisor.  <http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.UsuariosSupervisores.aspx> |
