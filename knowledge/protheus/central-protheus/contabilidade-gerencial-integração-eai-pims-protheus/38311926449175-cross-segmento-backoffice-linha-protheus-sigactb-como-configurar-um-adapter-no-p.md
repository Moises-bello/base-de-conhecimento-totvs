---
article_id: 38311926449175
category: Contabilidade Gerencial - Integração EAI PIMS Protheus
content_hash: db29a41bd2594d7a2895e6d553dfad9c28bb1ab09bbf0019dd549bfc6ae6a517
fetched_at: '2026-06-28T22:40:54.177578+00:00'
product: protheus
section_id: 1500001537541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Como Configurar um Adapter
  no Protheus.
type: support-article
updated_at: '2026-02-19T19:26:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38311926449175-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-Configurar-um-Adapter-no-Protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38311949095703) Tempo aproximado para leitura: 00:10 min

**Dúvida**  
Como criar ou configurar um Adapter para integração EAI no Protheus?

**Ambiente**  
**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial (SIGACTB) -** ***Release*** **12.1.25**

**Solução**  
O recurso *Adapter* EAI (*Enterprise Application Integration*) permite estabelecer integrações entre o Microsiga Protheus® e outros ERPs ou sistemas externos. Essa relação ocorre através de *Web Services* ou ESB, respeitando um *layout* XML previamente estabelecido.

Para criar um novo apontamento de *Adapter*, o Administrador do Sistema deve definir quais rotinas serão integradas e configurar as condições de Envio e Recebimento no Configurador.

Para cadastrar um Adapter no Protheus:

1- Acesse o módulo Configurador (SIGACFG).

2 - Navegue até Ambiente > *Schedule* > *Adapter* EAI.

3 - Clique na opção Incluir.

4 - Preencha os campos obrigatórios, definindo:

* Rotina: A rotina do Protheus que manipulará os dados.
* Método: Se será enviado ou recebido.
* Mensagem: O nome da mensagem de integração.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38311949099415)  
  
5 - Salve o Cadastro.

Importante: Caso a necessidade seja utilizar as integrações nativas já existentes para a Contabilidade (SIGACTB), a TOTVS disponibiliza uma lista de *adapters* padrões.   
Para consultar quais são os *adapters* da controladoria, acesse a documentação:  
[Cross Segmento - Backoffice Linha Protheus - SIGACTB - QUAIS SÃO OS ADAPTER's DE INTEGRAÇÃO DA CONTABILIDADE? – Central de Atendimento TOTVS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018892132-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-QUAIS-S%C3%83O-OS-ADAPTER-s-DE-INTEGRA%C3%87%C3%83O-DA-CONTABILIDADE-?source=search)

**Saiba Mais**  
[Adapter EAI (CFGA020)](https://tdn.totvs.com/pages/viewpage.action?pageId=312157611)  
[EAI Protheus - Frameworksp - TDN](https://tdn.totvs.com/display/framework/EAI+Protheus)  
[Como Configurar o EAI no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410199853207-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-SIGAATF-Como-Configurar-o-EAI-no-Protheus)
