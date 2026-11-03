---
article_id: 360000766347
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 375d71d708ae645f5ac82ad1157fae56c5c30ec107b6b1ac9928f6f03c83f8b0
fetched_at: '2026-06-28T22:37:20.014225+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como habilitar controle
  de alçada na mudança de situação / revisão do contrato ?
type: support-article
updated_at: '2026-06-15T13:57:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000766347-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-habilitar-controle-de-al%C3%A7ada-na-mudan%C3%A7a-de-situa%C3%A7%C3%A3o-revis%C3%A3o-do-contrato
---

O artigo explica como habilitar o controle de alçada na mudança de situação e revisão de contratos no Microsiga Protheus (versão 12). A configuração gera pendências para aprovação na rotina MATA094 e o bloqueio para as Rotinas de Contrato/Revisão, válida para contratos de Compras e Vendas.

**Dúvida**  
Como habilitar controle de alçada na mudança de situação / revisão do contrato ?

**Ambiente**

Microsiga Protheus - Gestão de Contratos - A partir da versão 12

**Solução**  
Neste artigo poderá ser verificado o processo de habilitação do Fluxo de Aprovação de Contrato e Revisão no módulo de Gestão de Contratos.

Ao realizar este procedimento lembre-se que na alteração do contrato para os status: Vigente e Aprovação de Revisão, será gerado na rotina de documentos **CNTA300** - Tabela **SCR**, uma pendência para aprovação!

**Importante**: A configuração de alçada é **válida** para contrato de **Compras e Vendas.**

Verificar o artigo abaixo do TDN em ***Saiba Mais***.

[GCT0115 - Alçada no gestão de contratos em mudança de situação / revisão](https://tdn.totvs.com/x/elRnF)

***Pontos de Atenção:***

1 - Complementando as informações do artigo, habilitar também no cadastro no Grupo de Aprovação a ser vinculado no Tipo de Contrato, o tipo de Documento "Tp Contrato" na aba "Tipo de Documentos".

Para que apareça esta aba no cadastro de Grupo de Aprovação deve-se habilitar o parâmetro ***MV\_ALTPDOC***.

![](https://totvssuporte.zendesk.com/attachments/token/PCl3CTl4ZroDkSGexaCPAUJf7/?name=inline1580938156.png)

2 - Atentar também para que o Valor do Contrato esteja contemplado o range "de-até" de valores do(s) Perfil(s) de Aprovação, contido no Grupo de Aprovação utilizado.

3 - Para utilização de Alçada em Contratos Flexíveis, que não possuem itens em Planilha, utilizar no Grupo de Aprovação vinculado ao Tipo de Contrato, um "Perfil de Aprovação" que contenha no range de valores, um valor inicial "0,00":

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6961782262167)

4 - Cadastrar um Tipo de Contrato que possua o campo de Alçada de Contrato com **0 - Todos ou 1 -Documentos** dessa forma o campo de Grupo de aprovação de Situação será habilitado para edição.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31286339547799)

5 - Observar que utilizando o Tipo de Contrato cadastrado que possui Grupo de Aprovação Vinculado, ao vincular este Tipo de Contrato no cadastro de Contrato serão gravados também os Grupos de Aprovação para os respectivos campos da tabela CN9 (CN9\_APROV e CN9\_GRPAPR). Dessa forma o contrato deverá ter os grupos de aprovação vinculados tanto no Tipo de Contrato (CN1) quanto no Cadastro do Contrato (CN9).

**Dúvidas frequentes:**

**Obs1:**

Só será permitido movimentações no contrato após a aprovação da Revisão.

**Obs2**:

O contrato só entrara em processo de aprovação quando alterada a situação para **Aprovação 04** ou **Vigente 05**

**Obs3:**

Nesta configuração de alçada são gerados na tabela de alçada SCR no Tipo de Documento (CR\_TIPO), e browse da rotina de Liberação de Documentos (MATA094) os Documentos do Tipo "**CT**" (para Mudança de Situação/Inclusão do contrato) e "**RV**" (para Revisão de Contrato).

**Obs4:**

No processo de bloqueio de alçada na Revisão existe a possibilidade de configuração da alçada tanto para quando a revisão altera valor da planilha do contrato como também para quando não altera valor. Para isso, orientamos verificar as informações sobre o parâmetro **MV\_CNALCRV** no quadro e exemplos no final do artigo abaixo da funcionalidade:

[GCT0115 - Alçada no gestão de contratos em mudança de situação / revisão](https://tdn.totvs.com/x/elRnF)

**Obs5:**

O campo ***CN1\_CTRAPR*** contido na tabela de cadastro de Tipos de Contrato, está descontinuado, e atualmente não possui funcionalidade, devendo ficar em seu padrão como "Não Usado" no dicionário de dados, e corretamente não mais aparece no cadastro de Tipos de Contrato.

**Obs6:**

Para situação de alçada de Revisão de contrato/planilha sem saldo disponível, pode-se a possibilidade de configuração da alçada através das possibilidade do quadro de exemplos de cenários (cenário 4 por exemplo) utilizando o parâmetro **MV\_CNALCRV**junto com **MV\_CNRVDIF,** no final do artigo abaixo da funcionalidade:

[GCT0115 - Alçada no gestão de contratos em mudança de situação / revisão](https://tdn.totvs.com/x/elRnF)

Sendo que caso não atenda a necessidade, a possibilidade é apenas através da customização do processo de alçada.

Abaixo artigo com os pontos de entrada disponíveis do processo de alçada para que possa avaliar algum que melhor possa atender conforme a necessidade.

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Pontos de Entrada no Controle de Alçadas - MATXALC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053600534-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Pontos-de-Entrada-no-Controle-de-Al%C3%A7adas-MATXALC)

**Obs7:**

Qual processo ou rotina do Protheus é responsável por atualizar o campo do Grupo do aprovador Grup. Aprov CN9\_APROV na tabela CN9, ou, no gestão de contratos como faço para preencher o aprovador no contrato?

**R:** O campo  Grupo do aprovador Grup. Aprov **CN9\_APROV** é gravado  no padrão do sistema na inclusão do contrato quando o Tipo de Contrato possui o campo **Grp.Apr.Situação (CN1\_GRPSIT)** preenchido com o **Grupo de aprovação**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797908534935)

É necessário vincular o Tipo de contrato no contrato com essa informação na inclusão do contrato, e dessa forma é preenchido o campo Grup. Aprov **CN9\_APROV,** conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797908536343)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797931970455)

***Saiba Mais:***

[GCT0115 - Alçada no gestão de contratos em mudança de situação / revisão](https://tdn.totvs.com/x/elRnF)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - É possível gerar a alçada de Contrato Semi-fixo pelo Total da Planilha do Contrato?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25857238434327-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-%C3%89-poss%C3%ADvel-gerar-a-al%C3%A7ada-de-Contrato-Semi-fixo-pelo-Total-da-Planilha-do-Contrato?source=search)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Alçada Por Entidade Contábil na Mudança de Situação do Contrato e / ou Revisão do Contrato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404552326039-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Al%C3%A7ada-Por-Entidade-Cont%C3%A1bil-na-Mudan%C3%A7a-de-Situa%C3%A7%C3%A3o-do-Contrato-e-ou-Revis%C3%A3o-do-Contrato?source=search)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)

[GCT0113 - Configuração para aprovação de revisão por alçada por diferença de valor ou saldo contrato.](https://tdn.totvs.com/pages/releaseview.action?pageId=342298486)
