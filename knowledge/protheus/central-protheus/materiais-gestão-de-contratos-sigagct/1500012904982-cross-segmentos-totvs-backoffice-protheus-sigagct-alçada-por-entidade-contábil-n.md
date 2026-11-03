---
article_id: 1500012904982
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 3a5458204304b7b25771159e2c658b4c5dd9016a0e7f576bbcd1b591bc8ea033
fetched_at: '2026-06-28T22:37:20.344457+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Alçada por entidade
  Contábil na Rotina Nova Medição
type: support-article
updated_at: '2025-12-24T11:33:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012904982-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Al%C3%A7ada-por-entidade-Cont%C3%A1bil-na-Rotina-Nova-Medi%C3%A7%C3%A3o
---

**Dúvida**  
  
Como configurar Alçada por Entidade Contábil na Rotinas Nova Medição(CNTA121)?  
  
**Ambiente**  
  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Gestão de Contratos - Todas as versões  
  
**Solução:**

* **MV\_APRMDEC** - Configurar o parâmetro para ativar o controle de alçadas contábeis na medição;
* No cadastro de Tipo de Contrato informar o campo Alc. Contrato (**CN1\_ALCCTR**) igual a "Entidade Contabil"
* **MV\_ALTPDOC** - Configurar o parâmetro para mostrar a Aba com os "Tipos de Documentos" no cadastro de **Grupos de Aprovação**.
* Cadastrar um **Perfil de Aprovação(COMA210)** para Vincular no Grupo de Aprovação
* Cadastrar os **Aprovadores(MATA095)** que serão vinculados no Grupo de Aprovação.
* Cadastrar o **Grupo de Aprovação(MATA114)** com informação informação de entidade contábil na aba "**Entidades Contábeis**" (centro de custos/conta contábil/classe de valor/item contábil existente no ambiente) e marcar a opção "**Medições**" na aba "**Tipos de Documentos**";
* **MV\_CNMDALC** → Habilitar o parâmetro. Informa se o controle de alçada é ativo para as medições de contrato.

Uma vez realizadas essas configurações, toda medição (cujas planilhas possuam algum item com informação contábil compatível com a configuração realizada no grupo de aprovação) e o valor do documento for dentro do valor do Perfil de Aprovação Cadastrado irá gerar um

documento de bloqueio do tipo "**IM**" para a aprovação de alçada.

**Obs1:**

Essa funcionalidade não está disponível para medições realizadas através da rotina CNTA120.

**Obs2:**

Quando utilizada alçada por Entidades Contábeis na Medição, caso seja informado um desconto na aba "Descontos" da medição, este valor de desconto não será considerado no valor de aprovação da alçada:

***Explicação:*** Na alçada por entidade contábil o sistema verifica linha a linha dos itens da medição e verifica se a linha possui entidade contábil preenchida, desse jeito chega ao valor do Documento de Aprovação de alçada por Item da Medição (IM).

A Aba de Desconto(CNTA250) tem como objetivo dar desconto na hora da Medição e se irá refletir ou não no valor do pedido. Abaixo link explicando a funcionalidade da Aba Desconto.

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como informar um Desconto na Medição de Contratos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016084231-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-informar-um-Desconto-na-Medi%C3%A7%C3%A3o-de-Contratos)

Com isso, a Aba Desconto não irá interferir no valor total do documento criado na SCR.

Há disponivel dois pontos de entrada que pode-se customizar para atender a necessidade de alteração.

***CN121ESD*** - O ponto de entrada é utilizado para substituir a atualização do saldo padrão do sistema para que o usuário possa criar sua própria atualização. [(https://tdn.totvs.com/x/tQItE)](https://tdn.totvs.com/x/tQItE)

***CN121ENC*** - Possibilita ao desenvolvedor realizar operações após o encerramento da medição.  [(https://tdn.totvs.com/x/B1vDJ)](https://tdn.totvs.com/x/B1vDJ)

**Obs3**:

Qual a composição do campo CR\_NUM da Tabela SCR de Alçadas, para Documento do Tipo "IM" (Item de Medição) ?

R: Número da medição (CND\_NUMMED) + Numero da planilha (CNA\_NUMERO) + Prefixo(001).

Para cada linha de aprovação gerada, será somado +1 no prefixo.

Segue exemplo no artigo abaixo:

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Composição do Campo CR\_NUM para Documento do Tipo IM (Item de Medição)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25801539693335-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Composi%C3%A7%C3%A3o-do-Campo-CR-NUM-para-Documento-do-Tipo-IM-Item-de-Medi%C3%A7%C3%A3o?source=search)

**Obs4:**

**1. Para o cenário em que Realizar medição com item com quantidade zerada e o mesmo centro de custo preenchido. Segue abaixo:**

Considerando que o Valor mínimo do Perfil de aprovação do aprovador da medição é "0,01" e o Item com quantidade zerada possua o mesmo Centro de custo de outro item da mesma Medição que possui o campo de  quantidade preenchido.

Ao salvar, a medição o sistema gerará alçada para ambos os itens. Isso ocorre porque o sistema identifica os itens com o mesmo centro de custo e realiza o somatório dos valores correspondentes para gerar alçada.

Segue Exemplo abaixo do "somatório de itens pelo mesmo centro de custo" em outra rotina do sistema (Pedido de Compras) que possui o mesmo conceito de alçada dos somatórios dos itens com mesmo centro de custo.

Valor mínimo do **Perfil de aprovação** do aprovador do Pedido de compras = **0,02**

**Item 0001** Qtd 1  Valor unit  **0,01**       Valor total **0,01**           Centro de custo **001**

**Item 0002** Qtd 1  Valor unit 100,00    Valor Total 100,00      Centro de custo **001**

Considerando o exemplo acima: O valor do **item 0001** está fora do Range de aprovação do perfil de aprovação do aprovador que é a partir **de 0,02**, mas o que é considerado para alçada é o somatórios dos 2 itens totalizando **101,00 , para o centro de custo 001.**

**2. Para o cenário em que Realizar medição com item com quantidade zerada e que possui o centro de custo diferente dos demais itens da medição. Segue abaixo:**

Considerando que o Valor mínimo do Perfil de aprovação do aprovador da medição é "0,01" e o Item com quantidade zerada possua centro de Centro de custo diferente dos demais itens da medição. Não será gerada medição para esse item , pois o sistema verifica o centro de custo e o valor total da medição zerado por isso não cai bloqueado.

**Obs5:**

No caso da situação em que uma medição de determinada competencia é "Rejeitada" no seu processo de alçada e possui este status "Medição Rejeitada", para que a competencia em questão possa ser medida novamente, se faz necessário:

* ou a alteração da medição já incluida que esta "Rejeitada" para que ela passe novamente pelo processo de alçada e seja aprovada,
* ou que essa medição "Rejeitada" seja excluida, para inclusão de uma nova medição a ser aprovada novamente.

***Saiba Mais:***

[MP - SIGACOM - Qual a ultilidade do cadastro de Aprovadores ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025179531-MP-SIGACOM-Qual-a-ultilidade-do-cadastro-de-Aprovadores-?source=search)

[MP - SIGACOM - Qual a utilidade do cadastro do Perfil de Aprovação ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024881732-MP-SIGACOM-Qual-a-utilidade-do-cadastro-do-Perfil-de-Aprova%C3%A7%C3%A3o-?source=search)

[PCOM09010 - Grupo de Aprovação (MATA114)](https://tdn.totvs.com/pages/releaseview.action?pageId=274637723)

[MP - SIGACOM - Conceito do Tipo de Liberação no Grupo de Aprovação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018595131-MP-SIGACOM-Conceito-do-Tipo-de-Libera%C3%A7%C3%A3o-no-Grupo-de-Aprova%C3%A7%C3%A3o?source=search)

[MP - SIGACOM - Em quais processos o Grupo de Aprovação (MATA114) é validado ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024652012-MP-SIGACOM-Em-quais-processos-o-Grupo-de-Aprova%C3%A7%C3%A3o-MATA114-%C3%A9-validado-?source=search)

[MP - SIGACOM - Grupo de Aprovação irá considerar ou não os valores do Perfil de Aprovação?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058057973-MP-SIGACOM-Grupo-de-Aprova%C3%A7%C3%A3o-ir%C3%A1-considerar-ou-n%C3%A3o-os-valores-do-Perfil-de-Aprova%C3%A7%C3%A3o-?source=search)

[Alçada nas medições de contrato no módulo de Gestão de Contrato](http://tdn.totvs.com/pages/viewpage.action?pageId=268579126)

[Cross Segmentos - TOTVS Backoffice Protheus - SIGAGCT - Alçada Por Entidade Contábil na Mudança de Situação do Contrato e / ou Revisão do Contrato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404552326039-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGAGCT-Al%C3%A7ada-Por-Entidade-Cont%C3%A1bil-na-Mudan%C3%A7a-de-Situa%C3%A7%C3%A3o-do-Contrato-e-ou-Revis%C3%A3o-do-Contrato?source=search)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Composição do Campo CR\_NUM para Documento do Tipo IM (Item de Medição)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25801539693335-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Composi%C3%A7%C3%A3o-do-Campo-CR-NUM-para-Documento-do-Tipo-IM-Item-de-Medi%C3%A7%C3%A3o?source=search)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001545522)
