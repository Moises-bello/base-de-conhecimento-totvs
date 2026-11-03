---
article_id: 37341307894423
category: Ativo fixo - Reforma Tributária
content_hash: b1494305eeabd99b6f2178cdb2bdcd84bb0f740b5847c81fccdc5ca7777881b9
fetched_at: '2026-06-28T22:41:35.597372+00:00'
product: protheus
section_id: 37095895776791
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - Valor do Ativo Imobilizado
  considerando o Imposto Seletivo (IS)
type: support-article
updated_at: '2025-12-30T16:38:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37341307894423-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Valor-do-Ativo-Imobilizado-considerando-o-Imposto-Seletivo-IS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37341307886615) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Como é composto o custo de aquisição do Ativo Imobilizado considerando a incidência do Imposto Seletivo (IS) e do IVA-Dual (IBS/CBS) no contexto da Reforma Tributária?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Fixo - Todas as versões  
  
**Solução**  
Com a Reforma Tributária, a composição do custo do Ativo Imobilizado sofre alterações dependendo da característica cumulativa ou não cumulativa dos novos tributos.

1. Para determinar o valor a ser imobilizado, deve-se observar a seguinte regra prevista na Lei Complementar nº 214/2025:

   1. **IBS e CBS (Não Cumulativos):** Por serem impostos recuperáveis, eles **não** incorporam o custo de aquisição do ativo imobilizado. O contribuinte poderá apropriar créditos desses impostos, desde que a operação seja comprovada por documento fiscal idôneo.
   2. **Imposto Seletivo - IS (Cumulativo):** O IS incide apenas uma vez sobre o bem ou serviço e não gera direito a crédito. Portanto, ele **incorpora** o custo de aquisição do ativo imobilizado.

      Documentação oficial da consultoria tributária:  
      [Orientações Consultoria de Segmentos - Reforma Tributária - Ativo Imobilizado - Consultoria de Segmentos - TDN](https://tdn.totvs.com.br/pages/releaseview.action?pageId=969131216)
2. **Exemplo Prático de Cálculo**

   Considere a aquisição de um veículo com os seguintes valores hipotéticos:

   **Valor da mercadoria (Veículo):** R$ 100.000,00

   **Alíquota IS:** 25%

   **Alíquota IVA-Dual (IBS+CBS):** 26,5%

   * **Cálculo do Imposto Seletivo (IS):** O IS é calculado sobre o valor da mercadoria e, por ser cumulativo, soma-se ao custo.  
       
     R$ 100.000,00 \* 25% = R$ 25.000,00
   * **Cálculo do IVA-Dual (IBS/CBS)** A base de cálculo do IVA-Dual inclui o valor do IS.

     Base: R$ 100.000,00 + R$ 25.000,00 (IS) = R$ 125.000,00

     Valor do Imposto: R$ 125.000,00 \* 26,5% = R$ 33.125,00  
       
     *Nota: Este valor é recuperável e não compõe o custo do bem.*
   * **Valor Final do Ativo Imobilizado:** O valor a ser ativado no sistema será a soma do valor da mercadoria mais os impostos não recuperáveis (IS).

     R$ 100.000,00 + R$ 25.000,00 = R$ 125.000,00
3. **Configuração no sistema para que seja considerado o IS:**

   * Cadastro da Regra de Alíquota - Imposto Seletivo (IS)  
       
     ![](https://tdn.totvs.com/download/attachments/977838440/Cadastro%20Aliquota%20IS.gif?version=1&modificationDate=1755545641517&api=v2)
   * Cadastro da Regra Base de Cálculo - Imposto Seletivo (IS)  
       
     ![](https://tdn.totvs.com/download/attachments/977838440/cadastro%20base%20IS%20-%202.gif?version=1&modificationDate=1755545642540&api=v2)
   * Cadastro da Regra de Cálculo - Documentos Fiscais -  Imposto Seletivo (IS)  
       
     ![](https://tdn.totvs.com/download/attachments/977838440/Cadastro%20regra%20documentos%20fiscais%20IS.gif?version=1&modificationDate=1755545643513&api=v2)
   * Cadastro da Regra de Alíquota - IVA-Dual (IBS/CBS)  
       
     ![](https://tdn.totvs.com/download/attachments/977838440/Aliquota%20CBS%20E%20IBS.gif?version=1&modificationDate=1755545646923&api=v2)
   * Cadastro da Regra Base de Cálculo -  IVA-Dual (IBS/CBS)  
       
     ![](https://tdn.totvs.com/download/attachments/977838440/base%20de%20calculo%20CBS%20E%20IBS.gif?version=1&modificationDate=1755545649180&api=v2)
   * Cadastro da Regra de Cálculo - Documentos Fiscais -  IVA-Dual (IBS/CBS) - o IBS e CBS não incorporam o custo de aquisição do ativo imobilizado.   
       
     ![](https://tdn.totvs.com/download/attachments/977838440/CADASTRO%20REGRA%20CBS%20E%20IBS.gif?version=1&modificationDate=1755545652657&api=v2)
4. **Contabilização (Sugestão)**  
     
   Para a contabilização, os valores devem ser segregados entre Ativo (Custo), Impostos a Recuperar e Fornecedor/Caixa.  
     
   Exemplo de lançamento:

   * **D - Ativo Imobilizado:** R$ 125.000,00 (Mercadoria + IS)
   * **D - CBS a Recuperar:** R$ 11.000,00 (Proporcional conforme alíquota)
   * **D - IBS a Recuperar:** R$ 22.125,00 (Proporcional conforme alíquota)
   * **C - Caixa/Banco:** R$ 158.125,00 (Total da Nota)

   **Dica para Fórmula de Lançamento Padrão:** Para buscar valores de tributos calculados pelo Configurador de Tributos na contabilização, pode-se utilizar a função POSICIONE na tabela F2D, utilizando o índice 6. Exemplo:   
     
   POSICIONE("F2D",6,SD1->D1\_IDTRIB+"CBSATF","F2D\_VALOR")

**Saiba Mais**

[Valor do Ativo Imobilizado considerando o Imposto Seletivo (IS)](https://tdn.totvs.com/pages/viewpage.action?pageId=977838440)  
[Cross Segmento - Backoffice Linha Protheus - SIGACTB - Contabilização com Base na Classificação do Tributo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37097599152663-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Contabiliza%C3%A7%C3%A3o-com-Base-na-Classifica%C3%A7%C3%A3o-do-Tributo)  
[Cross Segmento - Backoffice Linha Protheus - SIGACTB - Contabilização com Base na Sigla do Tributo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37100272710039-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Contabiliza%C3%A7%C3%A3o-com-Base-na-Sigla-do-Tributo)
