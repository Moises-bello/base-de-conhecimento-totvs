---
article_id: 360020986011
category: NFe - Nota Fiscal Eletrônica
content_hash: 6ce5d14f4ef642b0d15aae4eb26476cd6f32e8ff0fc2e7517be1bb09792c944a
fetched_at: '2026-06-28T22:40:03.636702+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Destaque de ICMS
  normal  ou ICMS-ST na Devolução da nota
type: support-article
updated_at: '2025-06-16T17:08:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020986011-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Destaque-de-ICMS-normal-ou-ICMS-ST-na-Devolu%C3%A7%C3%A3o-da-nota
---

**Dúvida**Quais são as possibilidades de destaque do ICMS normal e do ICMS-ST para nota de devolução ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**Para que seja destacado o **ICMS normal ou ICMS-ST** em **nota de devolução** na **TAG Voutro e no Danfe em outras despesas e informação complementar**há os parâmetros abaixo:

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em **editar** **MV\_ICSTDEV = .F. ,** para que o **ICMS-ST em nota de devolução**destaque na TAG Voutro em outras despesas e informação complementar.

**![MV_ICSTDEV.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11699450669975)**

2. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em **editar****MV\_ICSTDEV = .T.  O ICMS ST** será destacado na TAG VICMSST

![MV_ICSTDEV_T.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11699551614615)

3. Para que o **ICMS Normal em nota de devolução**Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em **editar**  **MV\_ICMDEVO** =**.F.** na TAG Voutro e no Danfe em outras despesas e informação complementar deixar o parâmetro **Ou MV\_ICMDEVO =** **.T.**  O ICMS será destacado no campo próprio

4. Para haver o destaque o ICMS deve ser calculado e além disso, no TES o campo **Sit. trib. ICMS****(F4\_SITTRIB)****00, 10, 20, 70, ou 90**

**![F4_SITTRIB.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11699656880023)**

5. Para que seja destacado o **ICMS-ST** é necessário utilizar a **situação tributária do ICMS 10, 30, 70 ou 90,** Altere a situação tributária no TES no campo  **Sit. trib. ICMS** **(F4\_SITTRIB)**  
  
![F4_SITTRIB.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11699656880023)  
  
6. Preencha o campo **Agrega solid = Sim (F4\_INCSOL)**

![Agrega_solid_sim.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11699845920279)

7. Após isso, exclua a nota e gere novamente  se for utilizar o mesmo pedido digite novamente a TES para que seja alterada a **situação tributária** no item do produto.

* **Importante:**

Caso seja emitente do **Simples Nacional.**

* Exemplo o XML gerou conforme abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15791424098071)

8. Para destacar o **ICMS-ST** é necessário utilizar a **situação tributária do ICMS 201, 202, 203 ou 900**  
  
Altere a situação tributária no TES no campo  **F4\_CSOSN "Campo Cod. Sit. SN"**

![F4_CSOSN.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11699950369687)

9. Preencha o  campo **Agrega solid = Sim (F4\_INCSOL):**

![Agrega_solid_sim.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11699845920279)

10. Após isso, exclua a nota e gere novamente.

* **Saiba Mais:**

Para não calcular o **ICMS-ST** deve **configurar a TES:**  
  
**MKP ICM COMP =** Sim

![MKP_ICM_COMP.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11699984943127)

**Marg. Solid =** Nunca

![MARGEM_SOLID_NUNCA.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11700066053271)

* Caso a empresa ***seja emitente do Simples Nacional,*** para o destaque correto deve ser verificado o link abaixo:

[MP - NFE - Como destacar para emitentes do Simples Nacional Base de cálculo do ICMS e Valor do ICMS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025028193-MP-NFE-Como-destacar-para-emitentes-do-Simples-Nacional-Base-de-c%C3%A1lculo-do-ICMS-e-Valor-do-ICMS?source=search)

Para emitentes da **UF de PR o parâmetro  funciona apenas para notas com calculo de ICMS próprio para notas com ICMS-ST** atende conforme a legislação abaixo, será destacado na Voutro em devoluções:

Artigo 9. do Anexo IX do RICMS-PR/2017No link abaixo **consta o parecer:**<http://tdn.totvs.com/pages/releaseview.action?pageId=317312128>

Observação: Caso esteja gravando os impostos corretamente na tabela **CD2** na linha do **CD2\_IMP** e não esteja gravando no **xml,** deve verificar se o campo **CD2\_ITEM** esta devidamente preenchido, sendo com 2 caracteres para nota de saída e 4 caracteres para nota de entrada:

Nota de saída:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13174741539735)

Nota de entrada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13174929671959)
