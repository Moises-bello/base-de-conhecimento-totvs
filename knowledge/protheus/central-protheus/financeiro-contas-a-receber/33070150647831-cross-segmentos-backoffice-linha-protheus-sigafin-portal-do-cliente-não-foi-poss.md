---
article_id: 33070150647831
category: Financeiro - Contas a Receber
content_hash: 085f176ecbacd12ed785c975af06e43cbf2f57e596e05d8aeec77aea04193b8d
fetched_at: '2026-06-28T22:38:14.163310+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Portal do cliente -
  Não foi possível baixar a Danfe e XML
type: support-article
updated_at: '2025-06-26T14:35:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33070150647831-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Portal-do-cliente-N%C3%A3o-foi-poss%C3%ADvel-baixar-a-Danfe-e-XML
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33070176366871) Tempo aproximado para leitura: **00:08:00 min**

**Ocorrência**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33070176367639)  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.33

**Causa**  
Caso as premissas estabelecidas anteriormente não sejam atendidas, o Portal do Cliente exibirá uma mensagem informando que o ambiente está desatualizado para o usuário.

**Solução**  
O Portal do Cliente permitirá o download do DANFE e do XML apenas para as notas fiscais que foram devidamente transmitidas e autorizadas pela SEFAZ (Secretaria de Estado da Fazenda).

Para notas do tipo NFS-e (Nota Fiscal de Serviço Eletrônica), essa funcionalidade será desabilitada.

Ressaltamos que algumas premissas devem ser previamente atendidas para o correto funcionamento deste recurso. Tais configurações são de responsabilidade do administrador do ambiente.

**Protheus**

1. O serviço REST do Protheus deve estar devidamente ativo.
2. A integração com o TSS (TOTVS Service SOA) deve estar corretamente configurada.

**Para mais informações, acesse a documentação oficial.**

[Configurações Gerais do TSS](https://tdn.totvs.com/pages/releaseview.action?pageId=590613669)

O parâmetro MV\_FNPCTSS deve ser configurado com o endereço do servidor REST do TSS, no seguinte formato:  
**[seu\_ip]:[sua\_porta]/[caminho\_rest]**

Exemplo: `192.168.0.1:8080/tss/rest/`

3- O parâmetro MV\_SPEDGRV deve ter conteúdo igual a 2

**Para mais informações, acesse a documentação oficial.**

[Criação do parâmetro MV\_SPEDGRV para preencher a tag GRVDOCAUX do método DISTRIBUICAODEDOCUMENTOS.](https://tdn.totvs.com/pages/releaseview.action?pageId=814528388)  
  
**4-** **Para Protheus 12.1.2310 ou versões anteriores:**  
O ambiente deve estar atualizado com o Pacote de Expedição Contínua (PEC) do Backoffice, conforme as seguintes datas mínimas:

* **Superior a 15/01/2024** para integração com o TSS 12.1.2310.
* **Superior a 15/09/2024** para integração com o TSS 12.1.2410.

Além disso, a autenticação via segurança de socket deve estar habilitada, configurando o parâmetro **security=1**.

Para mais informações, consulte a documentação oficial.

[**WebServices REST/Server - Configuração)**](https://tdn.totvs.com/pages/viewpage.action?pageId=185747842)

### TSS

1. O serviço REST do TSS deve estar devidamente ativo.
2. **Para o TSS 12.1.2310 ou versões anteriores:**
   * O ambiente deve possuir o endpoint `end-point tssapidoc/v1/nfe/retornadoc/`.  
     Para validar a existência do endpoint, acesse pelo navegador o endereço:  
     `http://[seu_ip]:[sua_porta]/[caminho_rest]/tssapidoc/v1/nfe/retornadoc/`
   * É necessário que o ambiente esteja atualizado com o Pacote de Expedição Contínua (PEC) com data superior a **04/01/2024**.
   * A autenticação via segurança de socket deve estar **desabilitada**, configurando o parâmetro **security=0**.

Importante  
A partir da release **12.1.2410**, a autenticação via segurança de socket será obrigatoriamente habilitada, tanto no Protheus quanto no TSS.

Para mais informações, consulte a documentação oficial.

[Framework - Bloqueio de REST e SOAP sem security](https://tdn.totvs.com/display/public/framework/DFRM1-35680+DT+Bloqueio+de+REST+e+SOAP+sem+security)[)](https://tdn.totvs.com/display/public/framework/DFRM1-35680+DT+Bloqueio+de+REST+e+SOAP+sem+security)

### Resumo das Ações Necessárias em Relação ao TSS:

1. Validar se, ao acessar o serviço REST do TSS, o endpoint `EndPoint tssapidoc/v1/nfe/retornadoc/` está disponível.

   Caso o endpoint **não seja apresentado**, será necessário realizar a atualização do **RPO do TSS**.

**Resumo das ações a serem tomadas quanto ao TSS:**

1 - Validar se ao acessar o Rest do TSS ira apresentar o EndPoint tssapidoc/v1/nfe/retornadoc/

Se não apresentar este EndPoint, significa que será necessário atualizar o RPO do TSS.

**Como validar:** Acesse, através do navegador, o seguinte endereço:  
 <http://seuip:suaporta/caminhorest/tssapidoc/v1/nfe/retornadoc/>   
  
2. O endereço do serviço REST do TSS deve ser configurado no parâmetro**MV\_FNPCTSS****.**

**Importante**

 O endereço informado deve ser o mesmo utilizado na validação descrita no item 1 (REST do TSS).

**Saiba mais**

[**Portal do Cliente**](https://tdn.totvs.com/display/public/PROT/Portal+do+Cliente)  
[**Funcionalidades - Portal do cliente**](https://tdn.totvs.com/display/public/PROT/Funcionalidades+-+Portal+do+cliente#FuncionalidadesPortaldocliente-03.NOTASFISCAIS)
