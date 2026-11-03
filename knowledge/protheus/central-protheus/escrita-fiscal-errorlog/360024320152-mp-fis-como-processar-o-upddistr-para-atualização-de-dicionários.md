---
article_id: 360024320152
category: Escrita Fiscal - Error.log
content_hash: 626c3a29553609c05967f03340fed9b1200a39c52c439b7bd6b4f5d0d9b3520d
fetched_at: '2026-06-28T22:39:32.898950+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: MP - FIS - Como Processar o UPDDISTR para atualização de dicionários
type: support-article
updated_at: '2022-04-27T14:05:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024320152-MP-FIS-Como-Processar-o-UPDDISTR-para-atualiza%C3%A7%C3%A3o-de-dicion%C3%A1rios
---

**Dúvida**

Como atualizar o ambiente com o compatibilizador **UPDDISTR**

**Ambiente**  
Protheus – A partir da versão 12.1.17  
   
**Solução**  
 Para solucionar essa dúvida, realize os seguintes passos:

1. **Limpeza das Pastas**

- Exclua os arquivos **\*.DBF**e**\*.DTC** da pasta SYSTEMLOAD  
- Exclua os arquivos **\*.IDX** da pasta SYSTEMLOAD  
- Exclua os arquivos **\*.LOG** da pasta SYSTEM  
- Exclua os arquivos **TOTVSP\*.\*** da pasta SYSTEM  
- Exclua os arquivos **\*.TSK** e .**LOG** da pasta APPSERVER\_X32

2.

Trocar os arquivos abaixo da pasta *SystemLoad*:

**hlpdfpor.txt**  
**sdfbra.txt**

Atualizar o menu:

1. Copiar o arquivo SIGAFIS.XNU contido no pacote de atualização.
2. Colar o arquivo SIGAFIS.XNU no diretório padrão SYSTEM (O nome do diretório pode ter sido alterado a chave *StartPath*do respectivo ambiente no arquivo appserver.ini ).

 Nem sempre é disponibilizado o menu para atualização, somente é necessário atualização caso houver menu no pacote de atualização.

Obs: Só irar trocar os arquivos se no pacote de atualização, conter os arquivos mencionados.

3. Em seguida executar compatibilizador **UPDDISTR**:

**Executando o compatibilizador de migração de release**  
- Abra o Smartclient, e no Programa Inicial, digite: **UPDDISTR***\* Maiores detalhes sobre a funcionalidade do UPDDISTR podem ser encontrados neste link:<http://tdn.totvs.com/pages/viewpage.action?pageId=181965468>*

![](http://tdn.totvs.com/download/attachments/286020348/2017-08-07_15-31-45.png?version=1&modificationDate=1502287639000&api=v2)

- Selecione a(s) empresa(s) que deseja migrar a Release e clique em **OK**.

![](http://tdn.totvs.com/download/attachments/286020348/2017-08-07_15-33-01.png?version=1&modificationDate=1502287639000&api=v2)

- Após selecionar a(s) empresa(s), será exibida uma tela com as recomendações de **backup** e **espaço livre**. Clique em **Avançar**.

![](http://tdn.totvs.com/download/attachments/286020348/2017-09-22_028.png?version=1&modificationDate=1506089085000&api=v2)

Em seguida, serão exibidas as telas do **Termo de Aceite** que é **necessário** para o prosseguimento do processo. Leia atentamente, **marque** os **aceites**, e vá **avançando**.

![](http://tdn.totvs.com/download/attachments/286020348/2017-09-22_029.png?version=1&modificationDate=1506089085000&api=v2)

![2017-09-22_030.png](http://tdn.totvs.com/download/attachments/286020348/2017-09-22_030.png?version=1&modificationDate=1506089086000&api=v2)

![2017-09-22_031.png](http://tdn.totvs.com/download/attachments/286020348/2017-09-22_031.png?version=1&modificationDate=1506089086000&api=v2)

![2017-09-22_032.png](http://tdn.totvs.com/download/attachments/286020348/2017-09-22_032.png?version=1&modificationDate=1506089087000&api=v2)

![2017-09-22_033.png](http://tdn.totvs.com/download/attachments/286020348/2017-09-22_033.png?version=1&modificationDate=1506089087000&api=v2)

![2017-08-07_15-34-08.png](http://tdn.totvs.com/download/attachments/286020348/2017-08-07_15-34-08.png?version=1&modificationDate=1502287639000&api=v2)

![2017-08-07_15-34-44.png](http://tdn.totvs.com/download/attachments/286020348/2017-08-07_15-34-44.png?version=1&modificationDate=1502287639000&api=v2)

![2017-08-07_15-35-56.png](http://tdn.totvs.com/download/attachments/286020348/2017-08-07_15-35-56.png?version=1&modificationDate=1502287639000&api=v2)

![2017-08-08_15-42-24.png](http://tdn.totvs.com/download/attachments/286020348/2017-08-08_15-42-24.png?version=1&modificationDate=1502287639000&api=v2)

**Importante:** Para atualização do dicionario de dados e das rotinas envolvidas o requisito é a utilização do arquivo **sdfbra.txt e do arquivo .ptm** disponibilizados.
