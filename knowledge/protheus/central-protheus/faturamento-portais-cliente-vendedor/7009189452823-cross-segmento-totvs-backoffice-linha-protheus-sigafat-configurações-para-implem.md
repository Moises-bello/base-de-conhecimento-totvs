---
article_id: 7009189452823
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: 83d591b388e8b9641113ff0f2501af35cdaa1642e056e07aa9940ad7d75153d3
fetched_at: '2026-06-28T22:38:23.845017+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Configurações
  para Implementar o Portal  Gestão de Vendas (PGV)
type: support-article
updated_at: '2025-07-24T18:16:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7009189452823-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Configura%C3%A7%C3%B5es-para-Implementar-o-Portal-Gest%C3%A3o-de-Vendas-PGV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15286044684055) Tempo aproximado para leitura: **00:04:00 min****Dúvida**Como realizar Implementação do novo Portal Gestão de Vendas?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.1.33;

**Solução**

Quer um passo a passo, com vídeos, sobre a implementação dessa funcionalidade? [Acesse: Implementação Portal Gestão de Vendas](https://tdn.totvs.com/x/Etk1LQ)

### Requisitos para Utilização do Portal Gestão de Vendas;

Para utilizar o **Portal Gestão de Vendas**, os seguintes pré-requisitos devem ser atendidos:

1. **Versão do Protheus**

   * É necessário que o ambiente Protheus esteja na **Release 12.1.33 ou superior**.
   * Os **binários** utilizados devem ter **data de expedição igual ou Superior a outubro de 2021**.
2. **Atualizações do Ambiente**

   * O ambiente deve estar atualizado com o **último Pacote de Atualizações (Pacote de BackOffice)** disponível.
3. **Configuração do Appserver**

   * O Portal requer o uso do **Appserver REST 2.0** para funcionar corretamente.
4. **Integração com o TOTVS Mingle**

   * Para configurar o TOTVS Mingle, o **servidor Appserver deve possuir um IP público** acessível.
5. **Licenciamento**

   * Para que o **Portal Gestão de Vendas (PGV)** funcione corretamente, é necessário que o ambiente esteja licenciado com **quantidade suficiente de licenças** em pelo menos uma das seguintes modalidades:

     + **0217 – APP TOTVS Gestão de Vendas (TGV)**
     + **3004 – APP Backoffice Vendas**
     + **4001 – TOTVS I** (Acesso a Portal, Web Services, BI, T-REPORTS)

     ---

     **Importante sobre a licença 4001 – TOTVS I:**

     Essa licença é utilizada para integrações com outras rotinas e ferramentas do Protheus. Caso o ambiente possua **apenas a licença 4001**, é necessário observar os seguintes pontos:

     1. **Verificar se outras aplicações no ambiente também utilizam essa mesma licença**, o que pode impactar a disponibilidade de acesso.
     2. **Configurar a chave `Stateless` com valor igual a 1** nos WebServices do REST:

**Passo a Passo da Configuração do Portal Gestão de Vendas;****DBAccess;**

* Para sincronizar os dados as APIs do Portal Gestão de Vendas, utilizam o campo **S\_T\_A\_M\_P\_** como parâmetro de busca, sendo necessária a inclusão da chave **UseRowStamp** e **Memoinquery** no **TOTVS DBAccess**.

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Configuração do DBACCESS para utilização TOTVS Gestão de Vendas (TGV)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7004507364503-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Configura%C3%A7%C3%A3o-do-DBACCESS-para-utiliza%C3%A7%C3%A3o-TOTVS-Gest%C3%A3o-de-Vendas-TGV-)

**Appserver;**

* O Portal Gestão de Vendas efetua comunicação com o servidor Protheus através de requisições HTTP. Para que essa comunicação ocorra será necessário efetuar algumas configurações no servidor APPServer.

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Configuração do Appserver para utilização TOTVS Gestão de Vendas (TGV)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7008345717527-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Configura%C3%A7%C3%A3o-do-Appserver-para-utiliza%C3%A7%C3%A3o-TOTVS-Gest%C3%A3o-de-Vendas-TGV-)

**TOTVS Mingle;**

* A plataforma Portal Gestão de Venda é armazenada em uma nuvem TOTVS. Para que a aplicação possa se comunicar com o servidor Protheus é necessário efetuar a configuração do TOTVS Mingle, que executa o papel de um gateway entre a aplicação é o servidor Protheus. Além disso, ao configurar o TOTVS Mingle, a aplicação passa a utilizar os dados de Autenticação padrão do Protheus.

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Configuração TOTVS Mingle para implantação do TOTVS Gestão de Vendas (TGV)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7009044495895-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Configura%C3%A7%C3%A3o-TOTVS-Mingle-para-implanta%C3%A7%C3%A3o-do-TOTVS-Gest%C3%A3o-de-Vendas-TGV-)

**Vinculo de Vendedor;**

* Para acessar o Portal Gestão de Vendas, é necessário que o Usuário(Protheus) esteja vinculado a um Vendedor.

[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Configuração de Usuário para acesso ao Portal Gestão de Vendas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11142404398999-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Configura%C3%A7%C3%A3o-de-Usu%C3%A1rio-para-acesso-ao-Portal-Gest%C3%A3o-de-Vendas)

**Primeiro acesso ao Portal Gestão de Vendas;**

* O **Portal Gestão de vendas**pode ser acessado diretamente por um navegador, tanto por desktop ou mobile pois as telas do TGV são responsivas e podem ser acessadas normalmente em um **smartphone**pelos Vendedores;
* E para acessar o **Portal Gestão de vendas** basta utilizar o endereço: [https://gestaodevendasprotheus.totvs-solucoes.com.br](https://gestaodevendasprotheus.totvs-solucoes.com.br/#/login)

Primeiro acesso ao Portal Gestão de Vendas, tem que ser realizada, a limpeza do **Cache do Navegador** e o acesso **"Exclusivo"** ao ambiente**,** para que seja criado os campos **S\_T\_A\_M\_P** e os vínculos com o Protheus.

[Limpeza do Cache e DevTools para acesso ao PGV](https://centraldeatendimento.totvs.com/hc/pt-br/articles/26733327137687-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-ERRO-PGV-Schemas-403-OK)

**Saiba Mais**

[Consumo de Licença Webservice REST](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018606751-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Consumo-de-Licen%C3%A7a-Webservice)

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat- Ao incluir o pedido no portal TGV , não aparece a carteira de clientes do vendedor.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6455673044119-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-Ao-incluir-o-pedido-no-portal-TGV-n%C3%A3o-aparece-a-carteira-de-clientes-do-vendedor-)

[DT Descontinuação do programa SetupTGV](https://tdn.totvs.com/pages/releaseview.action?pageId=716359906)

[Webinar | MP - SIGAFAT - Novo Portal Gestão de Vendas #TOTVSBackofficeLinha\_Protheus](https://www.youtube.com/watch?v=1-rCrgb4kQQ&list=PLXa8l0dq5zRlXZWTyj15Nr6nMhW0gpyiC)
