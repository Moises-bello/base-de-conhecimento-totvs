---
content_hash: 042f61c8569cca38b2fd96117bf4ebf4a1c3ba1b3f5124126c81052bf3c6b947
fetched_at: '2026-06-29T00:08:38.222259+00:00'
page_id: '285641481'
product: rm
source: tdn-rm
title: INT0006_Erros_Comuns_da_Integracao_com_o_Fluig
type: documentation
url: https://tdn.totvs.com/display/LRM/INT0006_Erros_Comuns_da_Integracao_com_o_Fluig
version: 5
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Versões:** | 12.1.xx |
| **Ocorrência:** | Integração RM x Fluig |
| **Ambiente:** | Integração RM x Fluig |
| **Passo a passo:** | Erros Comuns   **Não foi possível encontrar o serviço 'WSCONSSQL'**    Este erro ocorre    Acesse a página de visualização dos WebServices do RM (http://<IP ou HostName da máquina em que o Host está configurado>:<porta informada no arquivo de configuração do host, tag HTTPPORT>/wsPageIndex) e copie o link do WebService necessário, neste caso, o de Consultas SQL (print).  Obs.: Caso não esteja configurado o WebService, acesse a documentação a seguir: <http://tdn.totvs.com/x/HoFXBQ>    Acesse o TDS ou Eclipse, e na visão inicial acesse a opção Visualização de Serviços - Incluir Serviço.    Configure o serviço conforme print abaixo:    Feito essa configuração, tente novamente incluir o movimento.     ---     **NOK Usuário não encontrado!**    Este erro ocorre quando o usuário logado no RM não está corretamente sincronizado com o usuário do Fluig.      Cadastro de usuário no Fluig    Para acertarmos os cadastros é necessário executarmos o processo "**Sincroniza usuários do Corpore com o GED**" |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
