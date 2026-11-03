---
article_id: 360049761294
category: Portal Facilities
content_hash: 8e5debfe1a95f41492dfd83219001b2edecdc6b33d015944562b24e5e039160c
fetched_at: '2026-06-28T22:42:36.208317+00:00'
product: protheus
section_id: 360010992234
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Implantação Portal Facilities
type: support-article
updated_at: '2022-04-26T20:23:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049761294-Manufatura-Linha-Protheus-MNT-Implanta%C3%A7%C3%A3o-Portal-Facilities
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png) Tempo aproximado para leitura: **00:02:30 min**  
**Dúvida**Como é realizada a configuração do **Portal Facilities**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Versão 12  
  
**Solução**Para utilização do **Portal Facilities** deverá seguir as configurações:  
 **HTTP**

|  |  |
| --- | --- |
| **Chave** | **Descrição** |
| *Path* | Local onde será o diretório raiz para as páginas. |
| **RPCEnv** | Nome do *Environment* usado para a conexão - **Facilities**. |
| *ResponseJob* | **Facilities\_** Seguido do nome do *Environment*. Exemplo: **Facilities\_** **Environment**. |

**ONSTART**

|  |  |
| --- | --- |
| **Chave** | **Descrição** |
| *Jobs* | **Facilities\_** Seguido do nome do *Environment*. Exemplo: **Facilities\_** **Environment**. |

**Facilities\_** **Environment**

|  |  |
| --- | --- |
| **Chave** | **Descrição** |
| *Environment* | **Facilities\_** Seguido do nome do *Environment*. Exemplo: **Facilities\_** **Environment**. |

**Exemplo de Configuração do AppServer.ini**

```
[MntPadrao]  
SourcePath=D:\NGAP10\apo\MntPadrao  
RootPath=D:\NGAP10\Protheus_Data  
StartPath=\DicMnt\  
x2_path=  
RpoDb=Top  
RpoLanguage=portuguese  
RpoVersion=101  
LocalFiles=ads  
Trace=0  
localdbextension=.dbf  
PictFormat=DEFAULT  
DateFormat=DEFAULT  
TOPDataBase=MSSQL7  
TOPServer=localhost                       
TOPAlias=Mnt  
helpserver=localhost:8081/help/padrao  
SpecialKey = P10KAROLMNTPADRAO  
  
[ONSTART]  
JOBS=Facilities_MntPadrao  
RefreshRate=120  
  
[HTTP]  
Enable=1  
Path=D:\NGAP10\http  
Environment=MntPadrao  
ResponseJob=Facilities_MntPadrao  
RpcEnable=0  
SetTimeOut=600  
SessionTimeout=600  
SigaWeb=MAK  
Cache-control=no-store  
PORT=8080   
  
[Facilities_MntPadrao]  
type=WebEx  
ONSTART=StartWebEx  
ONCONNECT=ConnectWebEx  
ONEXIT=FinishWebEx  
Environment=MntPadrao  
instances=2,3,1,1  
ExpirationTime=3600  
ExpirationDelta=600  
InactiveTimeout=1800  
WebFilial=01  
WebEmpresa=99
```

No **Portal Facilities** é permitida a personalização do *layout*, como a adição do logotipo da empresa e editando as imagens contidas na seção **HTTP**. Tornando a *interface* mais amigável ao usuário na inclusão de **Solicitações de Serviços**. Para a personalização do *layout* no **portal Facilities**, as imagens deverão ter a extensão **JPG**. Para adição do logotipo deve ser substituído o arquivo **ng\_logo1.jpg**, mantendo a mesma nomenclatura.  
  
**Procedimentos para Utilização**

1. Acesse o **Portal Facilites** através do endereço local **<http://localhost:8080/W_PORTALNG.APW>**
2. Informe os campos **Usuário** e **Senha** e tecle **Tab**, em seguida serão carregados os campos **Empresa/Filial** e **Ambiente no Servidor**, clique em **Confirmar.**
3. No campo **Bem/Localização** informe o **Código do bem**.
4. Informe os demais campos e clique em **Enviar**.
5. Será apresentada a tela com o número da **Solicitação de Serviço** aberta com a opção **incluir nova S.S**.

**Importante**

* Para a utilização do **Portal Facilites** será necessário ter os seguintes cadastros:  
  - **Bem - MNTA080**;  
  - **Árvore Lógica - MNTA902** incluir na estrutura o bem criado anteriormente e confirme.
* Para configuração do **Portal Facilities**, as imagens abaixo deverão ser adicionadas no diretório indicado em **PATH** na seção **HTTP**:  
  - **ng\_fundo1.jpg**;- **ng\_fundomenu1.jpg**;- **ng\_fundomenu2.jpg**;- **ng\_fundomenu3.jpg**;- **ng\_fundomenu4.jpg**;- **ng\_fundomenu5.png**;- **ng\_fundomenu6.png**;- **ng\_fundomenu7.jpg**;- **ng\_fundomenu8.jpg**;- **ng\_logo1.jpg**;- **ng\_topo1.png**;- **ng\_lupacons.png**.

**Saiba mais**Para acesso ao *download* das imagens, verifique o artigo [Manufatura - Linha Protheus - MNT - Imagens necessárias para utilização do Portal de Solicitação de Serviços](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024907653)
