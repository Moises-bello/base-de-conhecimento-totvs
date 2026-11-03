---
content_hash: 4ce54504a8a4b848f18678b144928bb36f3048356a955900567247f9e35d7d31
fetched_at: '2026-06-29T00:09:53.820655+00:00'
page_id: '442043111'
product: rm
source: tdn-rm
title: Atualizador RM - Como fazer
type: documentation
url: https://tdn.totvs.com/display/LRM/Atualizador+RM+-+Como+fazer
version: 2
---

### Atualizador RM

|  |  |
| --- | --- |
| **Produto:** | Banco de Dados |
| **Versões:** | 12.1 |
| **Ocorrência:** | SQL Server e Oracle |
| **Ambiente:** | Auxílio no processo de conversão da base de dados |
| **Passo a passo:** | **INTRODUÇÃO**  Este documento objetiva orientar os procedimentos de Atualização da base de dados da versão 12.1 dos produtos RM.  **DESENVOLVIMENTO/PROCEDIMENTO**  **Portabilidade**:  • É importante a leitura da Portabilidade antes da Atualização da base de dados.  Atualização da base de dados versão 12.1:  <http://tdn.totvs.com/display/public/LRM/GLB0015_PORTABILIDADE>  **Requisitos**:  1. A base de dados deverá estar na versão 11.82.30 ou 11.83.54. Para saber a versão da sua base de dados, execute o comando "**SELECT VERSAOBASE FROM GPARAMS**" no seu Gerenciador de Banco de Dados.  2. Instalação da BibliotecaRM 12.1 [Clique aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=172297669) para acessar o documento de instalação.  **Atualizando a Base de Dados:** 1. Execute o arquivo "**RM.Atualizador.exe**" no diretório **"...\CorporeRM\RM.Net\"**    2. Na tela “**Bem-Vindo ao Atualizador de Base de Dados TOTVS RM**”, insira o usuário e senha de acesso ao Banco de Banco, escolha o alias de acesso ao banco e clique no botão "OK":  • Caso não tenha um Alias criado, clique no ícone, apontado pela seta abaixo, do contrário, vá para o **passo 3.**    • Na tela "**Gerenciador de Alias**", clique no ícone com o sinal de mais (+), no canto superior esquerdo da tela, e preencha as informações de acesso ao Banco de Dados. Após o preenchimento, clique no botão "**Testar**" para validar as informações. Clique no botão "**OK**" para fechar a tela.    3. Na tela "**Atualizações Disponíveis**", clique no botão "**Avançar**". **Observação**: Todas atualizações são obrigatórias e não podem ser desmarcadas.    4. Ao clicar no botão "Avançar" da tela anterior, o processo de Análise de Requisitos será exibido. Aguarde até o término do processo.    • Na tela "**Análise de Requisitos a Atualização"**, verifique se todos os requisitos estão atendidos. Para saber mais sobre os Requisitos de Atualização, [clique aqui](http://tdn.totvs.com/display/public/LRM/Requisitos)    5. Na tela "**Análise de Impactos da Atualização de Versão**", verifique todos os impactos, clicando no link **"Analisar Impactos".**    • Aguarde até que todos os impactos sejam validados pelo Atualizador. Caso não haja impactos, vá para o **passo 6.**    • Para prosseguir marque a opção **"Não desejo analisar os possíveis impactos ou já realizei este procedimento anteriormente"** e clique no botão "**Avançar**".    6. Na tela **"Backup e Customização"** certifique que você possui uma cópia de segurança (backup) antes do processo de Atualização e que as Customizações, caso possua, já foram analisadas. Neste momento é **MUITO IMPORTANTE** se atentar para qual ambiente está sendo convertido, marcando uma das opções **Produção ou Homologação** (essa informação fica gravada no **log**). Em seguida, clique em "**Avançar**".      7. Nessa tela é necessário se atentar para todas as informações e verificar os links de **portabildiade**, **banco de dados e performance:**      8. Na tela "**Opções**" marque as opções, conforme desejado.        9.Na tela "**Execução**", clique no link "**Iniciar Atualização**" para iniciar a Atualização da Base de Dados.    • Certifique-se de que realmente deseja iniciar o processo clicando no botão "**Sim**".    • Durante a conversão, é possível visualizar o comando que está sendo executado no momento, clicando no link "**Comando em execução..."**    • Ao finalizar a conversão, a mensagem abaixo será exibida, caso não ocorra erros. Do contrário uma mensagem informando de erros será exibida com as devidas orientações.    • Após clicar no botão "**OK**" da tela anterior, clique no botão "**Avançar**" para ver o resumo da Atualização.    9. Na tela "**Resumo**" é possível verificar as informações consolidadas das Atualização em "**Visualizar Log**". Em seguida clique em "Avançar" para concluir a Atualização.    **Somente em casos de erros, acione o Suporte da TOTVS.**    10. Clique em "**Concluir**" para fechar o Atualizador.        11. Após a conversão, **em caso de erros,** enviar o log para análise. O log fica neste caminho: C:\totvs\CorporeRM\RM.Net\Atualizador\Log Como característica o nome inicia por "RM.Upgrade..." |
| **Observações:** | Para mais informações:  **COMUNIDADE** [R@Tecnologia](http://fluig.totvs.com/portal/p/10097/post/rtecnologia-community/1639774)   **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 8 – (Tecnologia), 2 – (Banco de Dados) |

[Ir para o final dos metadados](http://tdn.totvs.com/display/public/rm/Atualizador++V.12#page-metadata-end)

* Criado por [Leonardo Rodrigues Costa](http://tdn.totvs.com/display/~leonardo.costa), última alteração por Usuário desconhecido (mitchell.gonzaga) em [12 jun, 2015](http://tdn.totvs.com/pages/diffpagesbyversion.action?pageId=173082887&selectedPageVersions=16&selectedPageVersions=17)

[Ir para o início dos metadados](http://tdn.totvs.com/display/public/rm/Atualizador++V.12#page-metadata-start)

**Atualizador 12.1.5**

|  |  |  |
| --- | --- | --- |
| **Produto** | : | TOTVS Banco de Dados |
| **Versão RM** | : | Versão 12.1.5 |
| **Banco de Dados** | : | SQL Server e Oracle |
| **Processo** | : | Atualizador de base de dados para a versão 12.1.5 |
| **Sub Processo** | : | Auxílio no processo de conversão da base de dados |
| **Data da Publicação** | : | 11/06/2015 |

**INTRODUÇÃO**

Este documento objetiva orientar os procedimentos de Atualização da base de dados da versão 12.1.5 dos produtos RM.

**DESENVOLVIMENTO/PROCEDIMENTO**

**Portabilidade:**

* É importante a leitura da [Portabilidade](http://tdn.totvs.com/pages/releaseview.action?pageId=165282824) antes da Atualização da base de dados.

**Atualização da base de dados versão 12.1.5:**

**Requisitos:**

1. A base de dados deverá estar na versão 11.82.30 ou 11.83.54. Para saber a versão da sua base de dados, execute o comando "**SELECT VERSAOBASE FROM GPARAMS**" no seu Gerenciador de Banco de Dados.
2. Instalação da BibliotecaRM 12.1.5 [Clique aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=172297669) para acessar o documento de instalação.

**Atualizando a Base de Dados:**

1. Execute o arquivo "**RM.Atualizador.exe**" no diretório "**...\CorporeRM\RM.Net\**"

          

    2. Na tela “**Bem-Vindo ao Atualizador de Base de Dados TOTVS RM**”, insira o usuário e senha de acesso ao Banco de Banco, escolha o alias de acesso ao banco e clique no botão "**OK**":

        

* Caso não tenha um Alias criado, clique no ícone, apontado pela seta abaixo, do contrário, vá para o **passo 3**.

* Na tela "**Gerenciador de Alias**", clique no ícone com o sinal de mais (+), no canto superior esquerdo da tela, e preencha as informações de acesso ao Banco de Dados. Após o preenchimento, clique no botão "**Testar**" para validar as informações. Clique no botão "**OK**" para fechar a tela.

    3. Na tela "**Atualizações Disponíveis**", clique no botão "**Avançar**". **Observação:** Todas atualizações são obrigatórias e não podem ser desmarcadas.

    4. Ao clicar no botão "Avançar" da tela anterior, o processo de Análise de Requisitos será exibido. Aguarde até o término do processo.  
         

* Na tela "**Análise de Requisitos a Atualização**", verifique se todos os requisitos estão atendidos. Para saber mais sobre os Requisitos de Atualização, [clique aqui](http://tdn.totvs.com/display/rm/Requisitos)

    5. Na tela "**Análise de Impactos da Atualização de Versão**", verifique todos os impactos, clicando no link "**Analisar Impactos**".

* Aguarde até que todos os impactos sejam validados pelo Atualizador. Caso não haja impactos, vá para o **passo 6**.

* Para prosseguir marque a opção "**Não desejo analisar os possíveis impactos ou já realizei este procedimento anteriormente**" e clique no botão "**Avançar**".

    6. Na tela "**Backup e Customização**" certifique que você possui uma cópia de segurança (backup) antes do processo de Atualização e que as Customizações, caso possua, já foram analisadas. Em seguida,     clique em "**Avançar**".  
          

    7. Na tela "**Opções**" marque as opções, conforme desejado. Recomendamos aos clientes TOTVS marcarem as duas opções.O envio do **Log de Atualização** para a TOTVS serve de base de conhecimento         para aprimoramento da ferramenta. sem eliminar a abertura de chamados em caso de erros.

 

* + **Observação:**

    8. Na tela "**Execução**", clique no link "**Iniciar Atualização**" para iniciar a Atualização da Base de Dados.  
         

* Certifique-se de que realmente deseja iniciar o processo clicando no botão "**Sim**".
* Durante a conversão, é possível visualizar o comando que está sendo executado no momento, clicando no link "**Comando em execução...**"..

* Ao finalizar a conversão, a mensagem abaixo será exibida, caso não ocorra erros. Do contrário uma mensagem informando de erros será exibida com as devidas orientações.
* Após clicar no botão "**OK**" da tela anterior, clique no botão "**Avançar"** para ver o resumo da Atualização.

    9. Na tela "**Resumo**" é possível verificar as informações consolidadas das Atualização em "**Visualizar Log**". Em seguida clique em "**Avançar**" para concluir a Atualização. Somente em casos de erros, acione     o Suporte da TOTVS.

    10. Clique em "**Concluir**"para fechar o Atualizador.
