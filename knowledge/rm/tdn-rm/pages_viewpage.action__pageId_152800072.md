---
content_hash: 62c76937e38b9565debc224aeb1f8bfa275339b50233e20bde9ea45bfba62183
fetched_at: '2026-06-29T00:05:56.537982+00:00'
page_id: '152800072'
product: rm
source: tdn-rm
title: RMPAT00002_Executar permissões
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=152800072
version: 3
---

|  |  |  |
| --- | --- | --- |
| Produto | : | TOTVS Gestão Patrimonial – Versão: 11.52 |
| Processo | : | Executar Permissões |
| Subprocesso | : | Globais |
| Data da publicação | : | 14/08/2014 |

**Introdução**   
 Procedimento a seguir refere-se à execução de permissão de acesso a menus e campos.  
 Para executar as permissões, basta seguir os passos abaixo:

**Desenvolvimento/Procedimento**   
 As permissões devem ser executadas na MDI antiga (executável) e nova MDI, para que não haja conflito destas informações.

**Primeiramente deveremos identificar o perfil associado ao usuário.**   
 Acesse o menu Cadastros > Segurança > Usuários > Edite o respectivo usuário >   
 Aba Segurança > Verifique qual o perfil associado e certifique-se que possui apenas um perfil.

Após verificar o perfil associado, deveremos executar as permissões:   
 Acesse: Cadastros > Segurança > Perfis > Edite o respectivo perfil associado ao usuário > Aba Acesso a Menus > Recolher Tudo > Permitir Acesso (Ou procure o menu desejado).

Para acessar a MDI: Acesse o Disco local C: > totvs > CorporeRM > RM.Net > RM.exe.   
   
   
   
   
   
 Na MDI, deve-se acessar a opção SERVIÇOS GLOBAIS > Aba 'Segurança' e realizar o mesmo processo informado acima.

Ressaltamos que no momento de executar a permissão na MDI, deve-se atentar ao 'Sistema' informado logo acima dos botões de 'Incluir, Editar Excluir'.

Realize um logou/login para validar as permissões.

Para maiores informações:

[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE****[R@Controladoria](http://fluig.totvs.com/portal/p/10097/subject/rcontbil)**

**Canais** **de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 2 – (Controladoria e Finanças), 2 – (Ativo Fixo).
