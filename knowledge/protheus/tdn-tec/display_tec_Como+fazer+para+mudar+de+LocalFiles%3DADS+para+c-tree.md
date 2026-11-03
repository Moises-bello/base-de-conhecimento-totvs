---
content_hash: a27570d2c4de848204461c88ada06d5aa5a0f1ad005ec7e3db1dad69835801cf
fetched_at: '2026-07-02T19:24:26.754122+00:00'
page_id: '6064427'
product: protheus
source: tdn-tec
title: Como fazer para mudar de LocalFiles=ADS para c-tree
type: documentation
url: https://tdn.totvs.com/display/tec/Como+fazer+para+mudar+de+LocalFiles%3DADS+para+c-tree
version: 3
---

BLOCK

Como fazer para mudar de LocalFiles=ADS para c-tree

## Como fazer para mudar de LocalFiles=ADS para c-tree

```
Através da chave LocalFiles, na seção [Environment], do arquivo de configuração do TOTVS | Application Server, pode-se definir qual RDD será responsável pelo gerenciamento dos arquivos locais no ERP - Enterprise Resource Planning, SXs e tabelas temporárias.
```

Ao utilizar banco de dados TOTVS | DBAccess, pode-se optar por RDDs ADS ou c-tree para controle de dicionários.

Neste ambiente, caso o cliente opte por utilizar c-tree Server®, para controle dos dicionários, os arquivos SXs e alguns arquivos auxiliares devem ser convertidos inicialmente para o formato do arquivo c-tree. Para isso, é necessário utilizar a opção de importação de dados do APSDU.

### Procedimento

Para importar os dados e homologar o ambiente c-tree.

1. Crie um novo *environment*, no TOTVS | Application Server, com o *RootPath* diferenciado.  
    Não adianta apenas criar um outro ambiente com *StartPath* diferente, pois existem outros arquivos fora do *StartPath* que também dever ser convertidos ou utilizarão o formato c-tree.
2. Para criar o ambiente, copie a pasta \ERP\_Data e as subpastas para outro diretório, por exemplo: \ERP\_Datactree.
3. No arquivo de configuração (appserver.ini), do TOTVS | Application Server, configure a chave LocalDbExtension, da seção [Environment], para .dtc (o valor padrão dessa chave é .dtc, quando utilizado LocalFiles=ctree).
4. Crie um *path* temporário, no ambiente ADS, para ser utilizado na conversão dos arquivos de ADS para c-tree.   
    Exemplo: \tempctree.
5. Acesse o APSDU (Microsiga Protheus), no ambiente ADS, e selecione todos os arquivos \*.dbf , incluindo os SXs, para serem convertidos.

   |  |
   | --- |
   | **Procedimento**  1. Acesse a aplicação **APSDU**, do Microsiga Protheus,  no ambiente configurado para ADS. 2. Acesse **Arquivo** + **Importar**. 3. Preencha os seguintes campos:  **Rdd Origem** - Selecione a opção DBF.  **Arquivo(s) origem** - Especifique o diretório onde estão os arquivos SXs.  **Máscara** - Informe \*.dbf. 4. Clique **Avançar**. 5. Selecione a tabelas desejada. 6. Clique **Avançar**. 7. Preencha os seguintes campos:  **Rdd destino** - Selecione **c-tree (CTREECDX)**.  **Arquivos(s) origem** - Especifique o diretório temporário criado no seu ambiente ADS para os arquivos c-tree. Exemplo: tempctree. 8. Clique **Finalizar**.    Selecione para conversão os arquivos SXs e demais arquivos padrão DBF utilizados pelo ambiente. Não é necessário converter arquivos SC\*.dbf (temporários).    Terminado esse processo, deve-se converter o arquivo de empresas do ERP (sigamat.emp). Para isso, abra o arquivo, através do RDD DBF, e utilize Copy To, do APSDU, especificando como destino o arquivo sigamat.emp, com RDD CTREECDX, para uma outra pasta (exemplo: \tempctree).    Além disso, fora da pasta *RootPath* existem outros arquivos que devem ser convertidos, por exemplo, o arquivo PROFILE.USR, que armazena as definições da *profile* por usuário. Caso este arquivo não seja convertido, ele deve ser apagado no ambiente c-tree para ser recriado com RDD apropriado. |
6. Após realizar a conversão, na pasta \ERP\_Datactree, exclua todos os arquivos \*.DBF, \*.CDX e \*.IND.
7. Copie os arquivos convertidos da pasta \tempctree, do ambiente ADS, para a pasta correspondente no ambiente c-tree.
8. Acesse o ERP e homologue o ambiente c-tree.   
    Algumas rotinas podem precisar que outros arquivos específicos sejam convertidos. Caso as rotinas tentem abrir um arquivo no formato c-tree e o arquivo físico, no disco, estiver no formato DBF, a aplicação irá falhar com ocorrência de erro ***Ctree Error 13 - Unknow File Type***.
