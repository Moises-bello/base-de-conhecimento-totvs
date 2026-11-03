---
article_id: 360053516414
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: cbaac80bb62312e8f7285e12f474ed283ec764f86c6eb81c323b0a89bb0d6f32
fetched_at: '2026-06-28T22:39:36.985355+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: 'MP - FIS - Cumulatividade Pis, Cofins e CSLL '
type: support-article
updated_at: '2021-04-28T19:08:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053516414-MP-FIS-Cumulatividade-Pis-Cofins-e-CSLL
---

**Dúvida**  
Como funciona a cumulatividade dos impostos Pis, COFINS e CSLL retenção?

**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
De acordo com a legislação 13137/15 | Lei nº 13.137, de 19 de junho de 2015 vigente a partir do dia 22/06/2015.   
O  valor mínimo para retenção passa a ser a soma do valor calculado do Pis, Cofins e Csll, que deverá ser maior que **R$10,00** e a **cumulatividade passa a ser diária.** A data de vencimento dos impostos foi alterada para o segundo decêndio do mês subsequente. 

Para isto, foi criado o parâmetro **MV\_VL13137** que define o novo valor mínimo para retenção. 

Desta forma todos os pagamentos e recebimentos efetuados a partir do dia **22/06/2015** devem considerar as novas regras vigentes, exceto em casos em que o imposto tenha sido calculado na emissão do título, para estas situações como todo o calculo foi efetuado baseado na inclusão, não é possível recalcular os impostos, esta ação pode ocasionar duplicidade, pois os títulos que não possuem impostos calculados podem fazer parte da composição do calculo de um título posterior no qual foram calculado os impostos.

Para casos onde a dataBase seja alterado para uma data anterior a **22/06/2015** prevalecerá as regras da **Lei Nº 10.925, de 23 de julho  2004**. Mantendo-se válido o parâmetro **MV\_VL10925** para validação do mínimo, as regras de cumulatividade e data de vencimento dos impostos. 

O parâmetro **MV\_AB10925** continua com a sua funcionalidade, sendo necessário configurar com o valor em **2** para efetuar a cumulatividade na emissão das notas. 

Para situações em que o Pis/Cofins/Csll estejam configurados na **Emissão**, foi disponibilizado um parâmetro para que seja configurado qual a data que será considerada para realizar a cumulatividade. Por padrão estes parâmetros são considerados como 1=Emissão, pois na regra anterior a verificação para cumulatividade era de acordo com a data de emissão do título.

Contas a pagar: **MV\_VCPCCP**

Contas a Receber: **MV\_VCPCCR**

Possibilidades de configuração: **1=Emissao**, **2=Venc.Real**, **3=Dt Contab**.

Mais informações referente as alterações e interpretações da Lei podem ser encontrados em: [PIS - COFINS - CSLL - Novas Regras de Retenção - Lei 13.137/2015](http://tdn.totvs.com.br/pages/viewpage.action?pageId=190519714)

Abaixo link contendo maiores detalhes referente as informações descritas acima:

<https://tdn.totvs.com/pages/releaseview.action?pageId=192092055>
