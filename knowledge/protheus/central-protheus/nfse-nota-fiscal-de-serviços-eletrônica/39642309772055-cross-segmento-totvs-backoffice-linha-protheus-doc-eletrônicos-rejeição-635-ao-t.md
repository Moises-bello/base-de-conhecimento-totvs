---
article_id: 39642309772055
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 3c6c22dafe5421e6535bef6066d87f57cf8f7f72a2229a49dc7f4026392b9357
fetched_at: '2026-06-28T22:39:56.224215+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Doc. Eletrônicos - Rejeição
  635 ao transmitir RPS com itens da LC 116/2003
type: support-article
updated_at: '2026-04-17T12:15:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39642309772055-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Doc-Eletr%C3%B4nicos-Rejei%C3%A7%C3%A3o-635-ao-transmitir-RPS-com-itens-da-LC-116-2003
---

**Dúvida**

Ao transmitir um RPS com o código de tributação municipal 06298, vinculado aos itens da Lista de Serviços 10.05, 25.05, 15.09 ou 17.12, ocorre a rejeição 635: "O código do tipo de operação deve ser informado quando se tratar de uma compra governamental ou de serviços enquadrados na LC 116/2003".

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Doc. Eletrônicos - Versão 12.1.2410 ou superior

**Solução**

A rejeição ocorre devido à necessidade de adequação dos fontes e schemas para contemplar a obrigatoriedade do código do tipo de operação para os itens específicos da Lei Complementar 116/2003. Para correção, é necessário atualizar o ambiente Protheus e TSS com os pacotes oficiais.

**Atualizações**

**PROTHEUS**

* **12.1.2410**  
  Compilar o último rdmake NFSEXMLENV: <https://r.totvs.io/p/1246515>;  
  Aplicar o pacote: <https://r.totvs.io/p/1244207>.
* **12.1.2510**  
  Compilar o último rdmake NFSEXMLENV: <https://r.totvs.io/p/1246512>;   
  Aplicar o pacote: <https://r.totvs.io/p/1244208>.

**TSS**

* **12.1.2410**  
  Atualizar o RPO: [Clique aqui para download.](https://suporte.totvs.com/portal/p/10098/download?e=1171619)
* **12.1.2510**: Aplicar o pacote no RPO: <https://r.totvs.io/p/1245198>.  
    
  Além disso, **atualize** o arquivo de schema **tss\_nfse\_tipos\_v2.00.xsd** na estrutura do TSS:
* Para versão 12.1.2410: <https://r.totvs.io/p/1244003>
* Para versão 12.1.2510: <https://r.totvs.io/p/1243999>

**Procedimentos**

No ERP Protheus, foi ajustado o envio do **código do tipo de operação (**`<tpOper>`**)** para que seja informado **quando o serviço estiver enquadrado na LC 116/2003**, especificamente nos itens **25.05, 15.09, 17.12 e 10.05**.  
  
Para viabilizar esse controle, foi criado o parâmetro `MV_INDOPER`, que permite **especificar o código do serviço do ISS (**`B1_CODISS`**)**.  
  
**Mais detalhes sobre o preenchimento do parâmetro:**[Como utilizar o MV\_INDOPER que controla o envio do tipo de operação na NFS-e (tag <tpOper>).](https://tdn.totvs.com/pages/viewpage.action?pageId=1041792076)  
  
**Cód. Serv. ISS (**`B1_CODISS`**)**: informe o código do serviço do ISS. Caso não exista um código cadastrado para o serviço, ele deverá ser incluído na **Tabela 60 do Configurador**.  
  
Por último, também é necessário o preenchimento do campo **C5\_GOVOPER=1** no Pedido de Vendas:  
- <https://tdn.totvs.com/pages/viewpage.action?pageId=1041790600>  
  
  
**Exemplo**  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/39818912446487)**  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/39818912446615)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39818912447383)

XML\_TSS da SPED051

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39818912447767)  
  
XML\_ERP da SPED051  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39818945106199)  
  
  
**Pontos importantes**  
- Validar se o IBS/CBS está sendo devidamente calculado no Pedido de Vendas, visto que essa tag somente é gerada em conjunto com IBS/CBS:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39818945106455)  
  
- Gerar um novo Pedido de Vendas do zero, **sem copiar um já existente.** Caso contrário poderá ficar informações incorretas presas no sistema.  
  
- Data dos fontes envolvidos no processo e obrigatórios no Inspetor de Objetos do Protheus:  
**NFSEXMLENV**: 13/04/2026  12:22:00  
**BACKOFFICE.FISCAL.TSS.XML.TLPP:** 25/03/2026  13:53:15  
**BACKOFFICE.TSS.ENGINE.TRIBUTES.TLPP:** 12/03/2026  16:25:52
