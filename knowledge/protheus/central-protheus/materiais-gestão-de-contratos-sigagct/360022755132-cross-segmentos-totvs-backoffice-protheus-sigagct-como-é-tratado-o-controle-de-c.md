---
article_id: 360022755132
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: e06fe7bd1e0eb2a254d952ab8010d62d58d8a62a74bea00ef833ad172705cc70
fetched_at: '2026-06-28T22:37:19.959957+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como é tratado o Controle
  de Cauções do Gestão de Contratos ?
type: support-article
updated_at: '2025-05-27T11:43:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022755132-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-%C3%A9-tratado-o-Controle-de-Cau%C3%A7%C3%B5es-do-Gest%C3%A3o-de-Contratos
---

**Dúvida**Como é tratado o Controle de Cauções do Gestão de Contratos ?  
  
**Ambiente**Microsiga Protheus – Gestão de Contratos – A partir da versão 11.80  
  
**Solução**As cauções no ambiente de Gestão de Contratos representam as garantias solicitadas ao fornecedor ou pagas aos clientes pelos materiais/serviços contratados. A caução é um bem ou valor que se dá em garantia ao cumprimento das obrigações assumidas no ato da contratação, tais como: ativos, recursos financeiros, direitos, contratos e outros instrumentos depositados para assegurar o cumprimento das obrigações dos participantes.

Existem cauções do Tipo Manual e Caução por Retenção, sendo assim:

* **CAUÇÃO MANUAL**

→ No uso da Caução Manual, na inclusão do contrato deverão ser informados os campos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24731677382167)

Na Caução Manual, enquanto o contrato ainda está "Em Elaboração", ou seja, antes de se tornar "Vigente", é necessário que se utilize a rotina de "Cauções" em Atualizações->Contratos->Cauções.

Nesta rotina é cadastrado a(s) caução(s) vinculada ao contrato, e que necessita(m) ter seus valores com no mínimo o valor do percentual informado no campo "% Caução" (***CN9\_MINCAU***) do "valor total" do contrato para que se possa passar o contrato para "Vigente".

Este tipo de caução é utilizado quando não existe uma regra fixa para baixa e retenção e se faz necessário o controle manual. Neste tipo de caução quando necessário é possível realizar a baixa do saldo, sendo que após a baixa o sistema gera um titulo a pagar ou a receber dependendo do tipo de contrato utilizado.

No cadastro da caução manual, o preenchimento do campo ***CN8\_DTFIVI*** (Data Fim), é habilitado a depender do **Tipo de Cauções(CNTA040)** utilizado.

Para este preenchimento o **Tipo de Cauções(CNTA040)** o campo **Financeiro? (CN3\_LIGFIN)** precisa estar como **"Não"**.

Neste cenário, o processo de caução não integrará com o ambiente financeiro, sendo apenas informativo para o gestão de contratos.

Dessa forma, o Campo "Financeiro?"(***CN3\_LIGFIN***) = 2-Não no Tipo de Cauções, habilita no Cadastro da Caução (CNTA090) para edição os campos **CN8\_EMITEN (Emitente), CN8\_NUMDOC (Documento), CN8\_DTINVI (Data Inicio), CN8\_DTFIVI (Data Fim)**.

Após a caução cadastrada estes campos podem ser visualizados a aba "Cauções" da Visualização do Contrato:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30258845270807)

A baixa da Caução Manual, pode ser realizada após o contrato se tornar Vigente, pela própria rotina de inclusão da caução, através da opção "Outras Ações->Baixar":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28792504713879)

* **CAUÇÃO RETENÇÃO:**

→ No caução de retenção, na inclusão do contrato deverão ser informados os campos:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6443879900439)

Na utilização do Caução do **Tipo Retenção** existe o parâmetro ***MV\_CNRETNF*** que pode ser configurado para que a retenção ocorra na **geração do Pedido** (compra/venda) **ou**  na geração do título no financeiro gerado a partir da NF feita com esse pedido da medição.

**MV\_CNRETNF = N -> Desconta no Pedido.**

Nos itens da planilha, ao selecionar o campo **Nota/Título = Nota Fiscal**, o valor do abatimento da retenção do caução ocorrerá na **geração do pedido** de compra e/ou venda, conforme percentual informado no contrato.

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6443971604375)**

**MV\_CNRETNF = S  -> Desconta somente no Título gerado da NF incluída com o Pedido gerado na medição.**

Ao selecionar o campo **Nota/Título = Nota Fiscal,** o valor do abatimento da retenção do caução ocorrerá na geração do **título no financeiro** gerado a partir da NF feita com esse pedido da medição.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6443971604375)

**Obs1:**

Para se realizar a baixa e estorno (se necessário) da Caução do tipo Retenção podem ser utilizadas as opções "Cauções Retidas" e "Estorno Retenção" contidas em "Outras Ações" na rotina de "Manutenção" do Contrato, que podem ser utilizadas após a retenção da Caução realizada na Mediçâo do Contrato:

![](https://totvssuporte.zendesk.com/attachments/token/kDAsZNdkAg8O3DdLs1Fzp4uwe/?name=image.png)

Usando opção "Cauções Retidas":

![](https://totvssuporte.zendesk.com/attachments/token/JKWgtAyC4gQIPnvNFI2TfV0lf/?name=image.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17820917172119)

Usando a opção "Estorno Retenção" para estornar esta baixa realizada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17820955367063)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17820956285207)

**Obs:**

Ao selecionar o campo **Nota/Título = Título,  não ocorrerá** o valor do abatimento da retenção do caução na geração do **título no financeiro diretamente da medição, pois não existe a funcionalidade  da retenção para título gerados diretamente no financeiro.**

As movimentações de cauções podem ser contabilizadas através dos Lançamentos Padrões:

* 690 - Inclusão de caução
* 691 - Exclusão de caução
* 692 - Baixa de caução

***Saiba Mais:***

[GCT0138\_Cenários de caução manual](https://tdn.totvs.com/pages/releaseview.action?pageId=520120626)

[Tipos de Cauções (CNTA040)](https://tdn.totvs.com.br/pages/viewpage.action?pageId=224452002)

[Caução (CNTA090)](https://tdn.totvs.com/pages/releaseview.action?pageId=233762142)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Caução de Retenção - Como abater o valor da Caução não do Pedido gerado na Medição mas do título gerado pela NF deste Pedido ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404860413847)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Quais são os Lançamentos Padronizados do módulo Gestão de Contratos e como Funciona?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015864572-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Quais-s%C3%A3o-os-Lan%C3%A7amentos-Padronizados-do-m%C3%B3dulo-Gest%C3%A3o-de-Contratos-e-como-Funciona)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
