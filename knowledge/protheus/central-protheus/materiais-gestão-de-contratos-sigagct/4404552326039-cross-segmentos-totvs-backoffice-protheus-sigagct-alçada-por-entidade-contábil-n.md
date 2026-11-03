---
article_id: 4404552326039
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: e06fa8cb92ddd85e4cc14aa4741ed2e092eb0b2c6daba89f453144174ccff926
fetched_at: '2026-06-28T22:37:20.337198+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Alçada Por Entidade
  Contábil na Mudança de Situação do Contrato e / ou  Revisão do Contrato
type: support-article
updated_at: '2026-01-15T14:07:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404552326039-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Al%C3%A7ada-Por-Entidade-Cont%C3%A1bil-na-Mudan%C3%A7a-de-Situa%C3%A7%C3%A3o-do-Contrato-e-ou-Revis%C3%A3o-do-Contrato
---

**Dúvida**  
Como configurar Alçada por Entidade Contábil na Mudança de Situação de Contratos(CNTA300) e / ou Revisão ( CNTA300R ) do Contrato no Gestão de Contratos ?  
  
**Ambiente**  
Microsiga Protheus – Gestão de Contratos – A partir da versão 11.80  
  
**Solução**

* **MV\_APRCTEC** - Configurar o parâmetro para ativar o controle de alçadas contábeis nos itens do Contrato podendo assumir os seguintes valores: **0**- Desativado, **1**- Somente Contrato de compras, **2**- Somente contrato de vendas, **3**- Todos os contratos
* Caso se queira que esta alçada seja também para as Revisões do Contrato realizadas deve-se habilitar o Parâmetro **MV\_APRRVEC** onde deve ser informado o(s) número(s) do tipo de revisão desejado(s), conforme ordem apresentada na tela da rotina (CNTA010-Tipos de revisões) e exemplo abaixo , separados por ;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404552106647)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6988151805591)

* No cadastro de Tipo de Contrato informar o campo Alc. Contrato (**CN1\_ALCCTR**) igual a "Entidade Contábil"
* **MV\_ALTPDOC** - Configurar o parâmetro para mostrar os tipos de documentos no cadastro de**Grupos de Aprovação(MATA114)**
* Cadastrar um **Perfil de Aprovação(COMA210)** para Vincular no Grupo de Aprovação
* Cadastrar os **Aprovadores(MATA095)** que serão vinculados no Grupo de Aprovação.
* Cadastrar o**Grupo de Aprovação(MATA114)** com alguma informação contábil na aba "**Entidades Contábeis**" (conta contábil, centro de custos, classe de valor, item contábil ou alguma outra entidade contábil.  
  configurada no ambiente) e marcar a opção "**Tp. Contrato**" na aba "**Tipos de Documentos**";

Uma vez realizadas essas configurações, todos contratos e/ou Revisão (cujas planilhas possuam algum item com informação contábil compatível com a configuração realizada no grupo de aprovação) e o valor do documento for dentro do valor do Perfil de Aprovação Cadastrado irá gerar um

documento de bloqueio do tipo "**IC**" para a aprovação de alçada de Item de Contrato e "**IR**" para Aprovação de Alçada Item da Revisão.

***Saiba Mais:***

* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Característica da Alçada por Entidades Contábeis em Contratos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024947511)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual a utilidade do Cadastro de Aprovadores (MATA095)??](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025179531-MP-SIGACOM-Qual-a-ultilidade-do-cadastro-de-Aprovadores-?source=search)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual a utilidade do cadastro do Perfil de Aprovação ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024881732-MP-SIGACOM-Qual-a-utilidade-do-cadastro-do-Perfil-de-Aprova%C3%A7%C3%A3o-?source=search)
* [PCOM09010 - Grupo de Aprovação (MATA114)](https://tdn.totvs.com/pages/releaseview.action?pageId=274637723)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Conceito do Tipo de Liberação no Grupo de Aprovação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018595131-MP-SIGACOM-Conceito-do-Tipo-de-Libera%C3%A7%C3%A3o-no-Grupo-de-Aprova%C3%A7%C3%A3o?source=search)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Em quais processos o Grupo de Aprovação (MATA114) é validado ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024652012-MP-SIGACOM-Em-quais-processos-o-Grupo-de-Aprova%C3%A7%C3%A3o-MATA114-%C3%A9-validado-?source=search)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Grupo de Aprovação irá considerar ou não os valores do Perfil de Aprovação?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058057973-MP-SIGACOM-Grupo-de-Aprova%C3%A7%C3%A3o-ir%C3%A1-considerar-ou-n%C3%A3o-os-valores-do-Perfil-de-Aprova%C3%A7%C3%A3o-?source=search)
* [Cross Segmentos - TOTVS Backoffice Protheus - SIGAGCT - Como habilitar o processo de alçadas por Documento na inclusão da medição ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018317752-Cross-Segmentos-TOTVS-Brackoffice-Protheus-SIGAGCT-Como-habilitar-o-processo-de-al%C3%A7adas-por-Documento-na-inclus%C3%A3o-da-medi%C3%A7%C3%A3o-?source=search)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Alçada de Contrato Semi-fixo pelo Total da Planilha do Contrato (CT) e por Entidades Contabeis (IC)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25857238434327-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-%C3%89-poss%C3%ADvel-gerar-a-al%C3%A7ada-de-Contrato-Semi-fixo-pelo-Total-da-Planilha-do-Contrato?source=search)
* [Alçada nas medições de contrato no módulo de Gestão de Contrato](http://tdn.totvs.com/pages/viewpage.action?pageId=268579126)
* [Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001545522)
