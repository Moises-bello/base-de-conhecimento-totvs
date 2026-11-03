---
content_hash: f011c31fa7599a8080d69f858872d3e85407c6f79a14569a280218fcad7b4333
fetched_at: '2026-06-29T00:06:15.325792+00:00'
page_id: '210052406'
product: rm
source: tdn-rm
title: DT_Novo_Método_de_Importação_de_Tabela_de_Preços
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=210052406
version: 4
---

# Novo Método Para Importação de Tabela de Preços

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Utilitários |
| **Rotina:** | |  | | --- | | **Rotina** | | Utilitários do RM Saúde |  |  | | --- | | **Rotina(s) envolvida(s)** | | Importação de tabelas de MATMED de Convênios. | |
| **Requisito (ISSUE):** | [PCREQ-7611](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-7611 "PCREQ-7611") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | ORACLE, MSSQL |
| **Tabelas Utilizadas:** | SZITEMESTQPRECO, SZITEMESTOQESPECIFICO |
| **Sistema(s) Operacional(is):** | Windows |
| **Versões/Release:** | 12.1.8 |

## Descrição

Implementada melhoria que possibilita um novo método para importação de tabelas de preços de MATMED para convênios.

   Este novo método visa garantir a integridade na atualização dos preços nos casos em que o usuário tenha os códigos específicos de seus produtos baseados na TUSS, onde em alguns casos, o mesmo código TUSS pode ser aplicado para produtos diferentes.

## Procedimento para Implantação

 Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):  
   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.8 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.8.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:  
   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).   
   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros conforme campos abaixo:  
   a. Linha: RM  
   b. Versão: RM 12.1.8  
   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.  
   Importante: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

1. Acesse o menu “Cadastros / Estoques / Produto”.
2. Abra para edição um produto que deseje posteriormente lançar na conta do paciente.
3. Acesse “Anexos / Informações TOTVS Saúde”.
4. Acesse “Anexos / Tabelas de Preços” e selecionar a tabela na qual deseja modificar o produto.
5. Altere o código específico do produto (Apenas para que seja verificado que, o código específico não influenciará na codificação lançada no XML).
6. Abra o arquivo que será utilizado para a importação. Lembrando que para a importação pelo CODIGOPRD, o sistema agora necessita da seguinte estrutura de arquivo.
7. Cada coluna corresponde ao seguinte valor:  
   A = CODIGOPRD  
   B = CODESPECIFICO  
   C = DESCRICAO  
   D = CODUNIDADE  
   E = PRECO  
   F = CODTUSS  
   G = DESCTUSS
8. Acesse o menu “Utilitários / Utilitários do RM Saúde / Importação de Tabelas de MATMED de Convênios”.
9. Selecione tabela e convênio que será atualizado.
10. Clique em Importar.
11. Selecione o tipo de arquivo – Arquivo Excel (Com CODIGOPRD).
12. Selecione o arquivo e a vigência desejados e clicar em importar.
13. Após o fim da atualização, marque a opção “Atualizar produtos com código e descrição TUSS” e clique no botão “Atualizar”.
14. Durante a atualização, é realizada uma verificação na qual o sistema, caso encontre algum item com nenhuma ou mais de uma correspondência com a SZITEMESTQPRECO, pula a atualização deste produto, evitando assim uma possível inconsistência na atualização.
15. Se algum item se encaixar no caso citado acima, uma tela de relatório, com os itens que não foram atualizados, é mostrada para o usuário:
16. Este problema pode ser resolvido através da manutenção na própria página. Para isto, basta buscar o item na grid, clicar com o botão direito sobre ele e clicar em relacionar ou atualizar preço. Selecionar o item e clicar em OK:
17. Feito isto, para que esta manutenção deste ultimo produto surta efeito, é necessário clicar em “Atualizar” novamente.
18. Caso o relatório de erros não seja apresentado e apenas a mensagem “Preços atualizados com sucesso” seja mostrada, a atualização ocorreu sem erros.
19. Abra um novo atendimento externo através do menu “Atendimento / Pronto Atendimento / Ambulatório / Registro de Atendimentos Externos / Botão Novo Atendimento”.
20. Selecione o mesmo convênio para o qual foi editado o medicamento, preencher todos os dados obrigatórios e clicar em “Registra”.
21. Acesse a aba “Guia / Autorização” e incluir uma nova guia de SP/SADT.
22. Acesse o menu “Lançamento em Conta / Aba MatMed”.
23. Lance o produto que foi alterado anteriormente. E clique em Grava.
24. Encerre a conta.
25. Acesse a nova MDI e navegar até o menu “Faturamento > Faturamento Para Convênios”.
26. Crie uma nova remessa para o convênio desejado e incluir a conta recém fechada no faturamento desta remessa.
27. Execute o processo até a finalização e verificar o arquivo XML gerado. O mesmo deve conter o código TUSS correspondente ao medicamento.

divs
