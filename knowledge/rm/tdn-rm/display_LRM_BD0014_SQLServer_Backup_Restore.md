---
content_hash: bb1a9a181b410cc63fb82929d326fd01a9c6b6de463d6bb6688218a9631c4797
fetched_at: '2026-06-29T00:08:18.050448+00:00'
page_id: '261062825'
product: rm
source: tdn-rm
title: BD0014_SQLServer_Backup_Restore
type: documentation
url: https://tdn.totvs.com/display/LRM/BD0014_SQLServer_Backup_Restore
version: 5
---

|  |  |
| --- | --- |
| **Produto:** | Banco de Dados |
| **Versões RM:** | Todas |
| **Ocorrência:** | SQL Server Backup e Restore |
| **Ambiente:** | SQL Server 2014 |
| **Passo a passo:** | **Backup:** **1.       Siga os procedimentos abaixo:**  Acesse o Menu Iniciar > Todos os Programas/Programas > Microsoft SQL Server 2014 > SQL Server Management Studio:    Expanda a árvore até o nome da base de dados, clique com o botão direito do mouse e selecione a opção **Tasks > Backup:**    Irá abrir a tela de **Backup Database.**  Marcar opção "Copy-only backup"  Clique no botão **ADD**:    Irá abrir a tela de **Select Backup Destination**, clique no botão **(...)**:    Irá abrir a tela de **Locate Database Files**. No campo Select Path aponte o destino onde o arquivo será salvo. No campo **File Name**, informe o nome do arquivo com a extensão **.bak**:    Após indicar o arquivo e o diretório do backup clique em ok e vá até a aba “Backup Options”:    Na opção “Compression” selecione “Compress backup” e clique no botão **ok**:     **Restore:**   **1.       Siga os procedimentos abaixo:**  Acesse o Menu Iniciar > Todos os Programas/Programas > Microsoft SQL Server 2014 > SQL Server Management Studio:    Clique com o botão direito do mouse na pasta **Databases** e clique em **Restore Database:**    Irá abrir a tela de **Restore Database**, marque o campo D**evice** e clique sobre o botão **(...)**:    Na tela de **Specify Backup**, no campo **Backup media** selecione a opção **File** e clique em **ADD:**    Na tela de **Locate Database Files**. Localize o arquivo.bak e selecione-o. Clique em ok:    Após o arquivo de backup ser selecionado, a tela de Restore aparecerá novamente. Digite o nome da base, selecione o arquivo de backup e clique em Options a direita:    Na opção **Relocate all files to folder**, indique o caminho onde os arquivos da nova base que está sendo restaurada serão salvos e clique em ok.         ---  Após a migração recomendamos fortemente que faça as seguintes configurações/otimizações em seu ambiente: Banco de dados - Otimização  <http://tdn.totvs.com/x/usiFDg>    Sistema Operacional - Otimização <http://tdn.totvs.com/x/ttbuDQ> |
| **Observações:** | Para mais informações:  **COMUNIDADE** [R@Tecnologia](http://fluig.totvs.com/portal/p/10097/post/rtecnologia-community/1639774)   **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 8 – (Tecnologia), 2 – (Banco de Dados) |
