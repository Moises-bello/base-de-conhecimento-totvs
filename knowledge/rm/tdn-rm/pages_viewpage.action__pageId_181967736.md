---
content_hash: 9677885f263c0bac694c68d4f00c91683be6416650f4aeca36fc554c5837964d
fetched_at: '2026-06-29T00:05:57.799145+00:00'
page_id: '181967736'
product: rm
source: tdn-rm
title: Gerenciar permissão no cadastro de usuários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=181967736
version: 5
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Framework                       **Versão:**11.xx |
| **Processo** | **:** | Cadastro de usuários |
| **Subprocesso** | **:** | Gerenciar permissões no cadastro de usuários |
| **Data da publicação** | **:** | 20/01/2015 |

Para que o usuário consiga gerenciar as permissões dos demais usuários, faz-se necessário logar no aplicativo e coligada em questão com um usuário supervisor.

Os usuários que possuírem a condição de Supervisor nos aplicativos terão como diferencial, o acesso autorizado em algumas opções que demais usuários comuns não possuirão.

Dessa forma, somente usuários na condição de supervisor terão acesso completo ao cadastro de usuários.

Consulte a tabela **GPERMIS,** para identificar quais usuários são supervisores no aplicativo em questão, conforme exemplo abaixo:

Para identificar o sistema (aplicativo), consulte a tabela **GSISTEMA:**

Para gerenciar as permissões dos usuários, siga as orientações abaixo. No exemplo abaixo, serão gerenciadas as permissões para o sistema TOTVS Gestão Patrimonial (RM Bonum):

Acesse o cadastro de usuários:

Logue na MDI (RM.exe, localizado em C:\totvs\CorporeRM\RM.Net).

Selecione o Menu iniciar – Serviços Globais:

Selecione a aba Segurança -> Usuários:

Selecione o Sistema referente ao qual deseja alterar as permissões:

Pesquise pelo usuário desejado:

Gerencie as permissões, conforme desejado:

**Observação:**

Esta operação deverá ser repetida para cada Coligada que o usuário poderá ter acesso.  
  
Todas as coligadas em todos os sistemas devem possuir pelo menos um usuário supervisor cadastrado e este só terá autorização de alterar permissões de usuários das coligadas em que for supervisor.

Para maiores informações:

Icon

Consulte o[Wikihelp](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.LogAuditoria.aspx) TOTVS.

**COMUNIDADE**[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)

**Canais de Atendimento:**

**Telefônico:** 4003-0015 escolhendo as opções 02 – dois (Software), 02 – dois (Suporte Técnico), 03 – três (RM), 09 – nove (Demais Áreas), 04 – quatro (BI) e 03 – três (Gerador de Relatórios e Planilha);

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)
