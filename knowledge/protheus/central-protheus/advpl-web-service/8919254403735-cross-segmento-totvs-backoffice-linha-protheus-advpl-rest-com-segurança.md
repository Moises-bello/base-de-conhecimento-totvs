---
article_id: 8919254403735
category: ADVPL - Web Service
content_hash: 7530a22421a984f7e4b3a59b622de3548faa4f0a18f149f5461fd41c731fbad1
fetched_at: '2026-06-28T22:40:10.511644+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - REST com segurança
type: support-article
updated_at: '2022-09-16T14:43:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8919254403735-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-REST-com-seguran%C3%A7a
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como tratar segurança em uma API REST?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - A partir da versão 12.1.27.  
  
**Solução**Começamos pela construção da **API**, se a **API** passar o **SECURITY** no no **WSRestFul**, esta **API** seguira as permissões empregadas para a rotina indicada, permitindo o acesso ou não a **API** (<https://tdn.totvs.com/display/public/framework/WSRESTFUL>).

|  |  |  |
| --- | --- | --- |
| **cSecurity** | Caracter | Informe o nome da rotina que tem relação com a API REST (exemplo MATA030 ou MATA410), esse nome será utilizado para validação dos privilégios, permitindo assim o acesso ou não a API. |

**Sobre segurança no geral:**

1. Como primeiro passo precisamos garantir que o serviço **Rest** exija a autenticação do usuário ao efetuar qualquer requisição, para isso é necessário adicionar a chave "**Security**=**1**" na seção do *socket* do **Rest**.
2. Como um segundo passo o **REST** pode ser iniciado em **HTTPS**/**SSL**, criando uma criptografia de ponta a ponta entre o *client* *server*, trazendo mais segurança para a aplicação:<https://tdn.totvs.com/display/framework/Exemplo+com+SSL>e <https://tdn.totvs.com/pages/viewpage.action?pageId=6064865>
3. Outro ponto de segurança importante é filtrarmos quais **IPs** de origem podem realizar requisições ao serviço **Rest**, conseguimos realizar o mesmo através da chave: <https://tdn.totvs.com/display/framework/Exemplo+CORS>
4. Outro ponto de segurança é definirmos quais são as **APIs** que estaria disponível para requisição: <https://tdn.totvs.com/pages/releaseview.action?pageId=632107882>

**Agora vamos verificar os métodos de autenticação:**  
**Oauth 2.0**: <https://tdn.totvs.com/pages/viewpage.action?pageId=465383509>(Nesse caso você pode fornecer o ***token*** de acesso e ***token*** de atualização para o cliente, e assim ele apenas renova o ***token*** de **X** em **X** tempo)  
Pode também utilizar o ***basic*** para autenticação porém nesse caso é passado o usuário e senha no header da requisição.  
Também pode-se habilitar logs para auditar as autenticações via **Rest**: <https://tdn.totvs.com/pages/viewpage.action?pageId=593237150>  
É recomendado a utilização da seguinte chave **XMLSaveALL** desabilitada para ocultar dados adicionados ao **console.log:** <https://tdn.totvs.com/pages/releaseview.action?pageId=599598203>
