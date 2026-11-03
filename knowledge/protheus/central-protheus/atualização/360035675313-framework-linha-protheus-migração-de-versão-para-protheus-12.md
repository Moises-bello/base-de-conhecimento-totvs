---
article_id: 360035675313
category: Atualização
content_hash: eb7edfa8050bfc212ebcbaf7a67929655fc12c332d3e7697eae1d929b126fd21
fetched_at: '2026-06-28T22:42:21.264740+00:00'
product: protheus
section_id: 360000076747
source: central-protheus
title: Framework - Linha Protheus  - Migração de Versão - Para Protheus 12
type: support-article
updated_at: '2024-05-08T11:11:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035675313-Framework-Linha-Protheus-Migra%C3%A7%C3%A3o-de-Vers%C3%A3o-Para-Protheus-12
---

**Dúvida**Como efetuar a migração da versão 11, para a versão 12 do Protheus?  
   
 **Ambiente**Protheus - Servidor de Aplicação - A partir da versão 11  
   
**Solução**Segue abaixo procedimento de migração de versão:  
 **PREPARANDO A VERSÃO ATUAL PARA MIGRAÇÃO**

|  |
| --- |
| **Notas**:   * O Protheus 12 não suporta arquivos no formato DBF. Se sua base atual é DBF (localfiles=ADS / arquivos .dbf), deve ser feito *migração*para Ctree (.dtc) antes de efetuar a migração para a versão 12. * Link com a informação do suporte aos arquivos: [Arquivos DBF sem suporte no Protheus 12](https://tdn.totvs.com/pages/createpage.action?spaceKey=PROT&title=Arquivos+DBF+sem+suporte+no+Protheus+12&linkCreation=true&fromPageId=271659404) * Link para o procedimento demigração de arquivos .DBF para .DTC: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034352153-MP-FRAME-Converter-arquivos-DBF-para-DTC> * Verifique se o espaço disponível no servidor que hospeda a base de dados do sistema Protheus 12 é pelo menos 3x superior ao tamanho da base de dados do sistema Protheus (Versão atual). |

1. Prepare uma base teste, efetuando **cópia fria** (todos os serviços parados) e **consistente** (das pastas adequadas e banco de dados) da base de produção.  
2. Caso sua Base de Dados seja Relacional (utiliza DBACCESS) será necessário rodar o processo de verificação dos registros duplicados para todas as empresas. Assistente executado a partir da rotina **CHECKDUPL** via Configurador, que tem como pré-requisito a atualização do dicionário de dados padrão na pasta SYSTEMLOAD. Para fazer o download do dicionário, siga os procedimentos do seguinte link: <http://tdn.totvs.com/pages/viewpage.action?pageId=271415266>  
3. Crie dentro da pasta Protheus\_Data, a pasta *UPDATE* e nela descompacte o dicionário de dados Completo da versão 12. Na verificação de duplicidade será solicitado o **SX2.UNQ**, utilize o da versão 12 como referência para a checagem.  
4. Vide Instruções para **verificação de duplicidades** no link:  <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025732213-MP-FRAME-CheckDupl-Verifica%C3%A7%C3%A3o-de-Duplicidade-de-Registros>  
5. Desinstale as **Stored Procedures** através do **Configurador** pela versão atual. Lembrando que tal procedimento deve ser realizado juntamente com o DBA responsável pelo banco de dados, pois pode haver customizações nas **Stored Procedures**, e se for o caso o DBA pode realizar o backup para reaplicar tais customizações após a migração para a versão 12. Caso tenha dúvida sobre a desinstalação/instalação de **Stored Procedures**, favor abrir novo chamado com a equipe de Framework.  
6. Após efetuar o processo, pare os serviços do Protheus e renomeie a pasta raiz do Protheus. Por exemplo, se a pasta chamava-se TOTVS 11, renomeie-a para TOTVS 12.  
  
  
**ATUALIZANDO O SISTEMA E O DICIONÁRIO DE DADOS**  
1. É necessário atualizar **Binário, RPO, LIB, Dbaccess** e **Pacote Acumulados** do Protheus 12. Procedimento de atualização no link: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024983272-MP-FRAME-Atualiza%C3%A7%C3%A3o-de-arquivos-do-Protheus-12>**Obs.:** ao atualizar os arquivos de **Binário**, na pasta **bin**, renomeie as pastas APPSERVER, SMARTCLIENT e SMARTCLIENTACTIVEX, que poderão ser removidas posteriormente. Após baixar o binário do Protheus 12 e descompactar na pasta **bin**, copie os seguintes arquivos das pastas renomeadas para as pastas novas:  
APPSERVER: arquivo appserver.ini  
SMARTCLIENT: arquivo smartclient.ini  
  
Após atualizar o binário e copiar os arquivos .ini, abra o arquivo appserver.ini e faça as adequações de caminhos de pastas. Por exemplo, onde indicava o caminho como TOTVS 11, alterar para TOTVS 12.  
2. É necessário também atualizar os arquivos de Dicionário de Dados (**sxsbra.txt**) e **Help de Campos** na pasta Systemload  
Procedimento de atualização no link:  
Dicionário de dados: http://tdn.totvs.com/pages/viewpage.action?pageId=271415266  
Help de Campos: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028969891-MP-FRAME-Atualiza%C3%A7%C3%A3o-de-Help>

|  |
| --- |
| **Informação**:  Se você utilizar o Appserver em Linux, transfira o arquivo compactado para o Linux, e só descompacte-o no Linux. Descompactar o arquivo no Windows e depois transferir o .txt para o Linux pode causar erros. |

|  |
| --- |
| **Importante**:  Caso o servidor onde o Protheus está sendo executado possuir antivírus, deve ser adicionada a pasta raiz do Protheus às exceções do antivírus, caso contrário podem ocorrer erros de acesso a exclusão de alguns arquivos temporários, como no exemplo de erro abaixo:  Ctree Error (Disk Manager) - Create Index - DelTree 118 - It was not possible to delete file c:\protheus 12\protheus\_data\system\n01sx31.idx - The directory is not empty. |

**LIMPEZA DAS PASTAS**  
1. Exclua os arquivos **\*.DBF**e**\*.DTC** da pasta SYSTEMLOAD  
2. Exclua os arquivos **\*.IDX** da pasta SYSTEMLOAD  
3. Exclua os arquivos **\*.LOG** da pasta SYSTEM  
4. Exclua os arquivos **TOTVSP\*.\*** da pasta SYSTEM  
5. Exclua os arquivos **\*.TSK** e .**LOG** da pasta APPSERVER\_X32

|  |
| --- |
| **Nota**:  Ao preparar o ambiente para a migração, **não** é recomendável abrir o Protheus após atualizar os arquivos, mas sim, rodar direto o compatibilizador (MP710TO120) |

**EXECUTANDO O COMPATIBILIZADOR DE MIGRAÇÃO**1. No Smartclient da versão 12, execute no Programa Inicial: **MP710TO120  
  
![M12_01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046610573)**2. Clique em **Avançar**. Insira a senha do **Admin**, e pressione **TAB**  
  
![M12_02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046610593)  
  
3. Aparecerá uma janela, questionando de qual versão será feita o *update* para a versão 12. Marque a versão e clique **OK**  
  
![M12_03.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045752674)  
  
4. É recomendável manter a opção **Sobrepõe inicializador** marcada

|  |
| --- |
| **Obs**.: se você criou um inicializador padrão manualmente, em um campo que não tinha inicializador padrão, e agora este campo possui um inicializador padrão, o que foi criado manualmente será sobrescrito |

5. Clique em **Avançar**  
6. Na tela **Diretório de Dados**, clique em **Avançar  
  
![M12_04.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045753234)**7. Em **Configuração de execução do Update,** indicamos manter apenas as opções **Log de Critical Error**e **Corrigir erros automaticamente** habilitadas, lembrando que a opção de corrigir os erros automaticamente executará as alterações de base pelo próprio sistema  
8. **NÃO**marque a opção **Manter o arquivo de log existente  
  
![M12_05.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045754274)**9. Clique em **Avançar** / **Avançar**  
10. Aguarde o processo de compatibilização. Se durante o processo surgirem erros críticos que não puderam ser corrigidos automaticamente, estes devem ser corrigidos MANUALMENTE utilizando como base o link de **Erros Críticos** (mais abaixo), ou consultando o **Suporte** caso o erro não esteja listado  
  
**ATUALIZANDO O MENU DOS MÓDULOS**  
**Para baixar os arquivos, acesse:**  
1. Portal do Cliente: [http://suporte.totvs.com](http://suporte.totvs.com/)  
2. Menu Downloads e Atualizações  
3. Linha Protheus  
4. Microsiga Protheus Versão 12.1.XX (onde XX é a versão da Release)  
5. Todos  
6. Categoria: Menu de módulo  
7. Baixe o arquivo MENUS - BRASIL 12.1.XX

|  |
| --- |
| **Obs.**: se não estiverem aparecendo as versões, em "Filtros de pacotes" selecione "Todos pacotes disponíveis" e selecione a categoria novamente. |

**Para atualizar:**1. Pare o servidor do Protheus (**Appserver**)  
2. Efetue backup dos arquivos **\*.xnu** da pasta \Protheus\_Data\system  
3. Remova todos os arquivos de menu da pasta system (**\*.xnu**).  
4. Copie os arquivos **.xnu** baixados do portal para esta pasta.  
5. Reinicie o servidor do Protheus (**Appserver**)  
  
Lembrando que **menus personalizados** precisam ser refeitos, pois há rotinas da versão 11 que não existem no **RPO** da versão 12.  
  
**ERROS CRÍTICOS**  
Quando ocorrer erro crítico, o cliente deverá efetuar as devidas correções e executar a rotina **MP710TO120** novamente.  
Link com a correção dos erros críticos mais comuns: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025450971-MP-FRAME-Erros-cr%C3%ADticos-em-migra%C3%A7%C3%B5es-de-vers%C3%A3o>

|  |
| --- |
| **Observações**:  ¹ Para o módulo SIGAGPE é necessário aplicar o [GPECONV](http://tdn.totvs.com/pages/viewpage.action?pageId=274842204)(Conversor de base de dados do módulo Gestão de Pessoal). Caso tenha dúvidas sobre o GPECONV, favor consultar a equipe do SIGAGPE.  ² Para o módulo SIGAFIN é necessário aplicar o [FINXSE5](http://tdn.totvs.com/pages/viewpage.action?pageId=185754496)(Migrador Off-line (SE5 - FKs)). Caso tenha dúvidas sobre o FINXSE5, favor consultar a equipe do Financeiro. |
