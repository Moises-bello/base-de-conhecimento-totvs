---
content_hash: 95e6b96043117de746519c79afcc29aa99902f9f5b2988d16560053ecebaa2db
fetched_at: '2026-07-02T19:24:26.748142+00:00'
page_id: '6064426'
product: protheus
source: tdn-tec
title: Como fazer backup on-line dump dinâmico com c-tree Server
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=6064426
version: 8
---

BLOCK

Como fazer backup on-line dump dinâmico com c-tree Server

## Como fazer backup on-line (dump dinâmico) com c-tree Server

```
Quando utilizamos o c-tree Server como base de dados e/ou gerenciamento das tabelas ISAM (SXs), existe a possibiliade de configurar uma rotina de backup automático, agendada no próprio servidor do c-tree, onde é gerado um arquivo denominado Dynamic Dump.
```

Esse arquivo conterá o espelho das tabelas especificadas no momento da execução do mesmo, sem ter a necessidade de parar o c-tree Server.

### Criação do arquivo de *Dump* Dinâmico

O arquivo que contém o *script* para geração do *Dump* Dinâmico consiste em um arquivo ASCII/texto.

A seguir, veja um exemplo de *script* de *Dump* Dinâmico completo, para um ambiente ERP - *Enterprise Resource Planning*, em ambiente Linux, onde o c-tree Server é utilizado para gerenciamento dos SXs.

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

Com essas configurações, o *Dump* Dinâmico está programado para execução à 01:00, com intervalos de 24 horas (!FREQ 24), aguardando 60 segundos para o encerramento das transações pendentes (!Delay 60) e arquivando os arquivos ISAM (dicionários SXs), do ERP, o cadastro de empresas, os arquivos SuperFile de *help* e senhas e o *profile* dos usuários do ERP no arquivo /erp/ctreebkp/msdump.bak.

**No exemplo acima, os *paths* dos arquivos foram configurados para uma instalação de Protheus e c-Tree Server em ambiente LINUX. Para uso no ambiente Windows, deve-se usar o *path* completo dos arquivos, usando as normas de caminho de arquivo do Windows – Unidade de disco seguida por dois pontos ":" e barra inversa "\" como separador de diretório – por exemplo c:\protheus\_data\system\sigamat.emp**

### **Como realizar a habilitação do *Dump* Dinâmico no c-tree Server®**

1. Para habilitar a execução agendada do *Dump* Dinâmico, é necessário criar um arquivo contendo o *script* do *Dump* Dinâmico e salva-lo na pasta onde está o servidor c-tree Server®.  
   Salve-o com o nome do dynamic.dmp.
2. Edite o arquivo **ctsrvr.cfg** (arquivo de configuração do c-tree) e acrescente a linha abaixo, onde especificamos ao c-tree Server® que as configurações para *Dump* Dinâmico estão no arquivo *dynamic.dmp*, na pasta atual.  
   DUMP dynamic.dmp
3. É **importante** a presença da configuração "!PROTECT" no arquivo *dynamic.dmp,* para tratar o arquivo de senhas do ERP ( sigapss.spf ) de forma diferente pelo c-tree Server®, por ser um arquivo de um tipo diferenciado (conhecido por SuperFile). A cópia deste tipo de arquivo pelo Dynamic Dump em um estado íntegro exige esta configuração. Caso a configuração !PROTECT não seja utilizada, e arquivos do tipo superfile sejam copiados pelo Dynamic Dump, a restauração desses arquivos (SuperFile) podem apresentar a ocorrência de erro 14 (File Corrupt), não sendo possível recuperá-los.
4. Se as alterações dessas configurações forem realizadas com o c-tree Server® em operação, esta configuração apenas será considerada após o c-tree Server® ser finalizado e reiniciado novamente. No entanto, recomendamos a realização dessas alterações na configuração do c-tree Server® sem que ele esteja em execução.

| Observações - Considerando o exemplo acima |
| --- |
| * Caso o arquivo (/erp/ctreebkp/msdump.bak) já exista no momento da geração do *Dump*, o mesmo será apagado e um novo arquivo será criado com o este nome. * Deve-se arquivar, junto ao *Dump*, o *script* de *Dump* utilizado para montagem do mesmo (no exemplo, *dynamic.dmp*), pois ele será utilizado também na operação de restauração dos dados. * A chave time deve respeitar o formato    ```   !TIME HH:MM:SS   ``` |
