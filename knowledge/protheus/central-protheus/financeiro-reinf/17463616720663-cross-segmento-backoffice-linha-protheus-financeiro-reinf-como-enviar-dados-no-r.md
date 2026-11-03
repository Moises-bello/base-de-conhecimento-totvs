---
article_id: 17463616720663
category: Financeiro - Reinf
content_hash: aa2886d443a3069fb923e69d50df1773883dff7ee392482ada3c01b18ceb63e9
fetched_at: '2026-06-28T22:37:51.646263+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - Financeiro REINF - Como enviar
  dados no R-4000 inseridos antes da atualização do sistema
type: support-article
updated_at: '2026-03-04T17:19:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17463616720663-Cross-Segmento-Backoffice-Linha-Protheus-Financeiro-REINF-Como-enviar-dados-no-R-4000-inseridos-antes-da-atualiza%C3%A7%C3%A3o-do-sistema
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17463643349911) Tempo aproximado para leitura 00:08 min**

**Dúvida**

Ajuste - Vínculo da Natureza de Rendimento para títulos lançados antes da vigência do EFD-Reinf

Bloco 40. Como enviar dados no R-4000 inseridos antes da atualização do sistema?

**Ambiente**  
Cross Segmento - TOTVS Backoffice Linha Protheus - Financeiro REINF - Todas as versões.  
  
**Solução**

Caso alguma das informações solicitadas nos eventos da serie **R-4000** tenham sido inseridas no **Backoffice Protheus** antes da atualização do ambiente para a **EFD-Reinf 2.1.1**, e portanto não tendo as pré-condições necessárias para o envio dos dados ao **TAF**, uma alternativa é a montagem de um *Rkmake*para processamento e geração da tabela **FKW**.

Visando facilitar esse procedimento, a seguir passaremos um exemplo de *Rkmake*, cujo intuito é fazer o vínculo automático das **Naturezas de Rendimento** com os **títulos a pagar**/**receber** que devem ser considerados no **EFD-Reinf Bloco 40**.

**Importante**

* O **fonte de exemplo** está utilizando o conceito de preenchimento da(s) Natureza(s) de Rendimento dos facilitadores abaixo:
  + [**Documento de Entrada - Preenchimento automático da Natureza de Rendimento**](https://tdn.totvs.com/pages/releaseview.action?pageId=761500629)
  + [**Pedido de Vendas - Preenchimento automático da Natureza de****Rendimento**](https://tdn.totvs.com/pages/releaseview.action?pageId=747314010)
  + [**Títulos do financeiro e demais origens - Preenchimento automático da Natureza de Rendimento**](https://tdn.totvs.com/display/public/PROT/Facilitador+de+preenchimento+-+Natureza+de+Rendimento+X+Natureza+Financeira)
* Portanto, para utilizar esse modelo de preenchimento das **Naturezas de Rendimento**, revise o **cadastro de Produto** (para **Doc. de Entrada**/**Saída**) e o **cadastro de Naturezas Financeiras** (para títulos sem vinculo com nota fiscal);
* O fonte possui um filtro de data de emissão do título a partir de 01/01/2022, mas caso queira modificar a data, basta ajustar a atribuição da variável "*cDtIni*";
* O fonte buscará títulos em todas as filiais cadastradas (tabela **SM0**). Caso necessário mudar esse comportamento, adicione ou remova as filiais desejadas do array *aRecnoSM0*;
* O processamento não terá efeito sobre títulos que já foram totalmente baixados. A proposta do *Rdmake*é que seja executado antes de realizar as baixas dentro do período de vigência do **EFD-Reinf Bloco 40**, pois irá gerar dados na tabela **FKW**, que é pré-condição para gravar os dados na tabela **FKY** (**Baixas** x **Natureza de Rendimento**);
* Recomendamos que seja aplicado o ajuste primeiramente em ambiente de homologação antes de efetivá-lo no ambiente de produção do Protheus;

**Exemplo de utilização**

**Saiba Mais**

[FAQ - 0015 - Como enviar dados no R-4000 inseridos antes da atualização do sistema?](https://tdn.totvs.com/pages/releaseview.action?pageId=736955879)
