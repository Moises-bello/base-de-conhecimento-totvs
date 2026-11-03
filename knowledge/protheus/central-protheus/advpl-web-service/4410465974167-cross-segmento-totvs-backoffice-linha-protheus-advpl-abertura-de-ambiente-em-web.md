---
article_id: 4410465974167
category: ADVPL - Web Service
content_hash: 303b3ebd742bd6dd337649d1b578a4d7857e6c25feb47b4e3649f2b9dc9c4d70
fetched_at: '2026-06-28T22:40:10.364046+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Abertura de ambiente
  em Web Service
type: support-article
updated_at: '2024-07-04T14:58:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410465974167-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Abertura-de-ambiente-em-Web-Service
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24653211880983) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Pode se utilizado **RPCSetEnv**() para efetuar a abertura de ambiente em Web Service?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - a partir da versão 12.1.27  
  
**Solução**Não se deve utilizar funções de abertura e fechamento de ambiente em **API** (**RpcSetEnv**/ **RpcClearEnv** e **Prepare Environment**/**Reset Environment**), a abertura do ambiente é efetuada através do **PREPAREIN** informado no **AppServer.ini**.  
As informações de empresa/filial devem ser passadas no *header* da requisição no **TenantId**.  
A definição do **PREPAREIN** no **REST** é diferente do conceito utilizado nos webservices convencionais.  
Cada valor da chave **PREPAREIN** representa um grupo de empresas diferente para acesso ao serviço.  
  
**Por exemplo:**  
A chave **PREPAREIN** configurada com o valor **19** (PREPAREIN=19) avisa ao serviços **REST** que o grupo de empresa 19 vai receber requisições, e deve então ter *threads* preparadas para isso.  
Para que todos os grupos possam receber requisição, a chave **PREPAREIN** deve estar configurada como **PREPAREIN**=**ALL**  
Cada *thread* é montada com a primeira filial válida para aquele grupo. Para que o valor da filial seja trocada pela camada do REST é necessário enviar, no cabeçalho da requisição **REST** o parâmetro **tenantid**, conforme abaixo:

```
tenantid: 19,D MG 02. //EMPRESA,FILIAL
```

Neste caso, o servidor **REST** irá buscar uma *thread* disponível para o grupo 19 e a execução será realizada na filial D MG 02. Se o **tenantid** não for enviado no header da requisição ela será processada na primeira filial válida.  
  
**Obs**.: O **REST** passará a receber o header ***x-erp-module***, que representa o módulo do **Protheus**, esse header suporta os valores de módulos do Protheus válidos, como: **FIN**, **EST**, **FAT**, **ATF**.

**Exemplo:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8879333408151)

**Saiba mais**[REST com ERP Microsiga Protheus](https://tdn.totvs.com/display/framework/02.+REST+com+ERP+Microsiga+Protheus)  
[Rest](https://tdn.totvs.com/display/framework/Entendendo+as+novidades+do+REST)
