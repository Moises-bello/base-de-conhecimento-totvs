---
article_id: 360022787632
category: Configurações
content_hash: 1a1bc58df62b4b49c997c7702fe7349b170dfe5bc4550012993dc8f775ffa86b
fetched_at: '2026-06-28T22:46:49.632172+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: 'RH - RM - FOP - Trabalho Intermitente: Aba pagamento não aparece'
type: support-article
updated_at: '2025-08-07T13:45:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022787632-RH-RM-FOP-Trabalho-Intermitente-Aba-pagamento-n%C3%A3o-aparece
---

**Dúvida**Como habilitar a aba **Pagamento** da opção Convocação para Trabalho Intermitente?  
   
 **Ambiente**RM - Folha de Pagamento - 12.1  
   
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
**01.**Backup da base de dados;  
 **02.**Instalar o último patch disponível;  
 **03.**Executar o **RM.Atualizador.exe** e executar o script referente ao layout 2.4.02 do eSocial;  
 **04.** Executar RM.ScriptExecutor.exe e executar o script fechado **LB.2018.05\_07**, se o banco de dados for SQL Server, ou **LB.2018.05\_07\_ora**, se for Oracle;  
 **05.** Caso ainda não esteja habilitado, acesse **Configurações | Parâmetros | Parametrizador | Folha Normal | Geral** e marque o parâmetro **Ativar alterações da Reforma Trabalhista de acordo com a Lei Nº 13.467 de 13 de Julho de 2017;** **06.** Habilitar o uso do regime intermitente, acesse **Configurações | Parâmetros | Parametrizador | 06.01.02 – Funcionário | Trabalho Intermitente,** marque **Usa Trabalho Intermitente.****Observação**Além dos procedimentos descritos acima, é necessário conceder permissão aos usuários responsáveis por cadastrar as convocações. Essa permissão é uma subpermissão do cadastro de funcionários, uma vez que o cadastro de convocação é um anexo deste.  
  
**Atenção**  
O regime de **Trabalho Intermitente** está disponível apenas a partir da versão 12.1.18.
