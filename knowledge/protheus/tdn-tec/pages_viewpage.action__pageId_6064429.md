---
content_hash: 822894cb772315e643233e5fb9b19ace0d427460ca274637eb09268622180524
fetched_at: '2026-07-02T19:24:26.770697+00:00'
page_id: '6064429'
product: protheus
source: tdn-tec
title: Como fazer uma restauração a partir de um Dynamic Dump Backup
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=6064429
version: 4
---

BLOCK

Como fazer uma restauração a partir de um Dynamic Dump Backup

## Como fazer uma restauração a partir de um Dynamic Dump (Backup)

```
É possível realizar uma restauração de arquivos de dados e índices, em um arquivo stream de Dump Dinâmico, a partir do utilitário ctrdmp.
```

### Ambiente Windows

A partir do diretório de instalação do c-tree Server®, é possível realizar a restauração utilizando o aplicativo **ctrdmp.exe**, localizado na pasta \ctreeTools\ctreeAdmin\Standalone.

### Ambiente Linux

A partir do diretório de instalação do c-tree Server®, é possível realizar a restauração utilizando o aplicativo **ctrdmp**, localizado na pasta /util/.

A seguir, observe os seguintes detalhes antes de executar o aplicativo ctrdmp:

O aplicativo **ctrdmp** gera versões temporárias de registros de transações e outros arquivos associados com o c-tree Server® (isto é, arquivos com extensão FCS). Portanto, o arquivo contendo o *script* de *dump* dinâmico e o utilitário ctrdmp devem ser movidos para um diretório diferente do diretório de trabalho c-tree Server®. Desta forma, os arquivos de sistema criados pelo programa de recuperação não irão regravar sobre arquivos de trabalhos do c-tree Server®. Os arquivos temporários são automaticamente excluídos quando a recuperação for concluída.

Além disso, certifique-se que o c-tree Server®, para o qual os dados estão sendo recuparados, não esteja operando quando o ctrdmp for iniciado ou, se estiver em execução, se os arquivos que estão sendo restaurados não estão em uso pelo servidor.

### Restaurando um *dump* dinâmico

| Observação |
| --- |
| Esta documentação foi elaborada num ambiente Linux. No entanto, o comportamento do aplicativo de *dump* dinâmico é igual para ambos os ambientes Windows e Linux. |

1. Inicie o aplicativo **ctrdmp**.
2. Informe o **nome do arquivo**, que contém o *script* de *dump* dinâmico, que será utilizado para a recuperação (este parâmetro pode ser fornecido na linha de comando).  
    O mesmo arquivo *script*, utilizado para realizar o *dump* pode ser utilizado para restaurar o *dump*. A recuperação do *dump* inicia automaticamente e produz uma série de mensagens relatando o progresso da recuperação.

   |  |
   | --- |
   | * Cada arquivo recuperado ou recriado será listado ao término de sua criação. * Após a recuperação de todos os arquivos especificados, um mensagem indica que o arquivo de registro (*recovery log* ou *transaction log*) está sendo verificado e que os arquivos recuperados foram restaurados ao seu estado a um momento especificado, isto é, momento em que *dump* dinâmico foi gerado. * O aplicativo **ctrdmp** indica que o processo de recuperação do *dump* terminou com sucesso escrevendo a seguinte mensagem: "**DR: *Successful Dump Restore Termination***" no arquivo **CTSTATUS.FCS**. * No caso de recuperar apenas um ou alguns arquivos do *backup*, deve-se editar o arquivo *script* do *dump*, nesse momento utilizado para *restore* dos dados e especificar apenas os arquivos a serem recuperados.  No entanto, é importante lembrar que o *path* desses arquivos neste *script* não pode ser alterado. Para especificarmos um local alternativo de restauração, deve-se implementar a instrução !REDIRECT no *script*. * Entre os arquivos especificados a restaurar no *script* do *dump* dinâmico, apenas serão restaurados (por padrão) os arquivos que não existirem em seus locais originais. Por padrão, se o arquivo a restaurar já existe, ele é ignorado. Para forçar a restauração do arquivo, mesmo que ele já exista, insira no *script* do *dump* dinâmico a instrução !DELETE. Desta forma, todos os arquivos especificados no *script* serão restaurados e os arquivos existentes serão sobrescritos. * Caso o *backup* contenha arquivos do tipo SuperFile (por exemplo, arquivo sigapss.spf ou arquivos de help (sigahlp.hlp) do ERP) e o c-tree Server não tenha sido configurado corretamente para *backup* desse tipo de arquivo, a operação de restauração está sujeita a ocorrência do erro 14 (*FileCorrupt*), não sendo possível a restauração desse tipo de arquivo utilizando o *backup* atual. Para mais informações sobre a configuração, consulte o documento [Como fazer *backup* *on-line* (*dump* dinâmico) com c-tree Server](http://tdn.totvs.com/pages/viewpage.action?pageId=6064426). |

### Utilização da instrução !DELETE

Por padrão, no momento da restauração, os arquivos existentes nos seus locais originais não serão restaurados. Caso a instrução !DELETE seja especificada no *script* a ser utilizado na restauração dos dados, isto fará com que os arquivos em seus locais de destino sejam sobrescritos com a versão do arquivo contido no *backup*.

### Utilização da instrução !REDIRECT

Por padrão, a operação de *restore* retorna os arquivos especificados no *script* do *dump* dinâmico nos seus diretórios originais. Através da configuração !REDIRECT, inserida no arquivo *script* do *dump* dinâmico, é possível redirecionar o *path* de recuperação dos arquivos.

Este comando deve ser colocado no arquivo utilizado para criar o *dump* dinâmico, que será utilizado para restauração. Além disso, é possível editar o arquivo para que o utilitário restaure apenas um ou um bloco de arquivos do *dump* original, com a seguinte sintaxe de instrução: !REDIRECT.

#### Exemplo

```
 !REDIRECT /microsiga/ap7/ap_data/sigaadv/ temp/// Restaura os arquivos compactado a partir do path absoluto especificado, dentro da pasta “temp”, a partir do path em uso pela aplicação ctrdmp.
```

```
!REDIRECT /microsiga/ap7/ap_data/sigaadv/ /microsiga/restore   // Restaura os arquivos compactado a partir do path absoluto especificado como primeiro argumento, no path absoluto especificado como segundo argumento.
```

| Observação |
| --- |
| O redirecionamento exige que o *path* de destino, que será utilizado, seja criado no disco antes da operação que será executada. Caso o *path* de destino não exista, o *restore* é encerrado com o Erro #444. |

#### Exemplo prático de restauração de arquivos

Em um determinado ambiente, configuramos o *dump* dinâmico no c-tree Server®, com os parâmetros especificados no arquivo "dynamic.dmp", conforme especificado abaixo:

Arquivo: dynamic.dmp

```
!TIME 01:00:00  
!Dump /microsiga/ctreebkp/msdump.bak  
!Delay 60   
!FREQ 24   
!PROTECT  
!FILES    
/microsiga/ap_data/sigaadv/sigamat.emp  
/microsiga/ap_data/sigaadv/siga*.hl?  
/microsiga/ap_data/sigaadv/sigapss.spf  
/microsiga/ap_data/sigaadv/six*.dtc  
/microsiga/ap_data/sigaadv/sx*.dtc  
/microsiga/ap_data/profile/profile.usr  
!END
```

Tendo como base a necessidade de recuperação de um *dump* dinâmico, apenas os arquivos sigamat.emp (empresas do ERP Microsiga Protheus) e sigapss.spf (arquivos de senhas), em um *path* diferente do original utilizado na cópia.

Realize o seguinte procedimento:

1. Crie uma pasta temporária para esta operação.
2. Copie para esta pasta o utilitário **ctrdmp**, o arquivo de *script* **dynamic.dmp**, e o último arquivo de *dump* **msdump.bak** que será utilizado.
3. Renomeie o arquivo de *script* **dynamic.dmp** para outro nome (por exemplo, restore.bmp), apenas para sinalizar que este arquivo será utilizado para a operação de restauração de dados.
4. Na pasta criada, edite o arquivo *script* **retore.dmp**, que será utilizado para restaurar os dados, e elimine as linhas desnecessárias e especifique apenas os arquivos que serão restaurados, além de um *path* alternativo a ser utilizado para criação dos arquivos restaurados.

#### Exemplo

```
!Dump msdump.bak  
!REDIRECT /microsiga/ap_data/sigaadv/ sigatmp/  
   
!FILES    
/microsiga/ap_data/sigaadv/sigamat.emp  
/microsiga/ap_data/sigaadv/sigapss.spf  
!END
```

Desta forma, apenas os arquivos sigamat.emp e sigapss.spf serão restaurados na pasta sigatmp. No entanto, essa pasta deve ser criada a partir da pasta temporária de trabalho atual antes de executarmos o aplicativo ctrdmp.

Para isso, é necessário:

1. Criar a pasta **sigatmp** a partir da pasta atual, onde será executado o aplicativo **ctrdmp**.
2. Executar o aplicativo **ctrdmp**, passando como parâmetro o nome do arquivo de *script* que será utilizado pelo *restore* (restore.dmp).  
    Realizado isso, será verificado o arquivo que contém o *dump* das tabelas (msdump.bak), e apenas serão restaurados os arquivos que se enquadram na lista de arquivos especificados no arquivo restore.dmp, sendo os mesmos restaurados na pasta sigatmp.

A seguir, observe as mensagens apresentadas ao executar a aplicação no ambiente Linux.

As mensagens apresentadas em negrito estão destacadas para mostrar que apenas os dois arquivos especificados (sigamat.emp e sigapss.spf) foram executados, os demais foram ignorados por não terem sido especificados para restauração.

./ctrdmp restore.dmp

```
DR: file will be redirected....  
        /microsiga/ap_data/sigaadv/sigaadv/sigamat.emp -> temp/sigamat.emp  
DR: recreating file: /microsiga/ap_data/sigaadv/sigaadv/sigamat.emp  
DR: not in !FILES list.../microsiga/ap_data/sigaadv/sigaadv/sigahlp.hlp  
DR: file will be redirected....  
        /microsiga/ap_data/sigaadv/sigaadv/sigahlp.hlp -> temp/sigahlp.hlp  
DR:       skip file: /microsiga/ap_data/sigaadv/sigaadv/sigahlp.hlp  
DR: file will be redirected....  
        /microsiga/ap_data/sigaadv/sigaadv/sigapss.spf -> temp/sigapss.spf  
DR: recreating file: /microsiga/ap_data/sigaadv/sigaadv/sigapss.spf  
DR: not in !FILES list.../microsiga/ap_data/sigaadv/sigaadv/six990.dbf  
DR: file will be redirected....  
        /microsiga/ap_data/sigaadv/sigaadv/six990.dbf -> temp/six990.dbf  
DR:       skip file: /microsiga/ap_data/sigaadv/sigaadv/six990.dbf  
DR: not in !FILES list.../microsiga/ap_data/sigaadv/sigaadv/sxo990.dbf  
DR: file will be redirected....  
        /microsiga/ap_data/sigaadv/sigaadv/sxo990.dbf -> temp/sxo990.dbf  
DR:       skip file: /microsiga/ap_data/sigaadv/sigaadv/sxo990.dbf  
DR: not in !FILES list.../microsiga/ap_data/sigaadv/sigaadv/sxg990.dbf  
DR: file will be redirected....  
        /microsiga/ap_data/sigaadv/sigaadv/sxg990.dbf -> temp/sxg990.dbf  
DR:       skip file: /microsiga/ap_data/sigaadv/sigaadv/sxg990.dbf  
DR: not in !FILES list.../microsiga/ap_data/sigaadv/sigaadv/sxb990.dbf  
DR: file will be redirected....  
        /microsiga/ap_data/sigaadv/sigaadv/sxb990.dbf -> temp/sxb990.dbf  
DR:       skip file: /microsiga/ap_data/sigaadv/sigaadv/sxb990.dbf  
DR: not in !FILES list.../microsiga/ap_data/sigaadv/sigaadv/sx7990.dbf  
DR: file will be redirected....  
        /microsiga/ap_data/sigaadv/sigaadv/sx7990.dbf -> temp/sx7990.dbf  
DR:       skip file: /microsiga/ap_data/sigaadv/sigaadv/sx7990.dbf  
DR: not in !FILES list.../microsiga/ap_data/sigaadv/sigaadv/sx2990.dbf  
DR: file will be redirected....  
        /microsiga/ap_data/sigaadv/sigaadv/sx2990.dbf -> temp/sx2990.dbf  
DR:       skip file: /microsiga/ap_data/sigaadv/sigaadv/sx2990.dbf  
DR: not in !FILES list.../microsiga/ap_data/sigaadv/sigaadv/sxd990.dbf  
DR: file will be redirected....  
        /microsiga/ap_data/sigaadv/sigaadv/sxd990.dbf -> temp/sxd990.dbf  
DR:       skip file: /microsiga/ap_data/sigaadv/sigaadv/sxd990.dbf  
DR: not in !FILES list.../microsiga/ap_data/sigaadv/sigaadv/sxe.dbf  
DR: file will be redirected....  
        /microsiga/ap_data/sigaadv/sigaadv/sxe.dbf -> temp/sxe.dbf  
DR:       skip file: /microsiga/ap_data/sigaadv/sigaadv/sxe.dbf  
DR: not in !FILES list.../microsiga/ap_data/sigaadv/sigaadv/sx9990.dbf  
DR: file will be redirected....  
        /microsiga/ap_data/sigaadv/sigaadv/sx9990.dbf -> temp/sx9990.dbf  
DR:       skip file: /microsiga/ap_data/sigaadv/sigaadv/sx9990.dbf  
DR: not in !FILES list.../microsiga/ap_data/sigaadv/sigaadv/sxf.dbf  
DR: file will be redirected....  
        /microsiga/ap_data/sigaadv/sigaadv/sxf.dbf -> temp/sxf.dbf  
DR:       skip file: /microsiga/ap_data/sigaadv/sigaadv/sxf.dbf  
DR: not in !FILES list.../microsiga/ap_data/sigaadv/sigaadv/sx4990.dbf  
DR: file will be redirected....  
        /microsiga/ap_data/sigaadv/sigaadv/sx4990.dbf -> temp/sx4990.dbf  
DR:       skip file: /microsiga/ap_data/sigaadv/sigaadv/sx4990.dbf  
DR: not in !FILES list.../microsiga/ap_data/sigaadv/sigaadv/sxa990.dbf  
DR: file will be redirected....  
        /microsiga/ap_data/sigaadv/sigaadv/sxa990.dbf -> temp/sxa990.dbf  
DR:       skip file: /microsiga/ap_data/sigaadv/sigaadv/sxa990.dbf  
DR: not in !FILES list.../microsiga/ap_data/sigaadv/sigaadv/sx6990.dbf  
DR: file will be redirected....  
        /microsiga/ap_data/sigaadv/sigaadv/sx6990.dbf -> temp/sx6990.dbf  
DR:       skip file: /microsiga/ap_data/sigaadv/sigaadv/sx6990.dbf  
DR: not in !FILES list.../microsiga/ap_data/sigaadv/sigaadv/sx1990.dbf  
DR: file will be redirected....  
        /microsiga/ap_data/sigaadv/sigaadv/sx1990.dbf -> temp/sx1990.dbf  
DR:       skip file: /microsiga/ap_data/sigaadv/sigaadv/sx1990.dbf  
DR: not in !FILES list.../microsiga/ap_data/sigaadv/sigaadv/sxp990.dbf  
DR: file will be redirected....  
        /microsiga/ap_data/sigaadv/sigaadv/sxp990.dbf -> temp/sxp990.dbf  
DR:       skip file: /microsiga/ap_data/sigaadv/sigaadv/sxp990.dbf  
DR: not in !FILES list.../microsiga/ap_data/sigaadv/sigaadv/sx3990.dbf  
DR: file will be redirected....  
        /microsiga/ap_data/sigaadv/sigaadv/sx3990.dbf -> temp/sx3990.dbf  
DR:       skip file: /microsiga/ap_data/sigaadv/sigaadv/sx3990.dbf  
DR: not in !FILES list.../microsiga/ap_data/sigaadv/profile/profile.usr  
DR:       skip file: /microsiga/ap_data/sigaadv/profile/profile.usr  
DR: recreating system file: S0000000.FCS  
DR: recreating system file: S0000001.FCS  
DR: recreating system file: L0000016.FCS  
DR: restore files to dump time...Thu Nov 11 13:52:00 2004  
   
DR: Absolute path names -  
DR:   deleting system file: /home/siga0984/space/temprestore/S0000000.FCS  
DR:   deleting system file: /home/siga0984/space/temprestore/S0000001.FCS  
DR:   deleting system file: /home/siga0984/space/temprestore/L0000016.FCS  
DR: Successful Dump Restore Termination
```
