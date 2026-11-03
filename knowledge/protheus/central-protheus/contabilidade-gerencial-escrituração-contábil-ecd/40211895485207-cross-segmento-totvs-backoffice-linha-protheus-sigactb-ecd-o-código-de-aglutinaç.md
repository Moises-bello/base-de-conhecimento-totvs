---
article_id: 40211895485207
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 0d866a9b7a986d63272492ad4879b34f3deb838dabd0ae455e5b7988fe2bae0f
fetched_at: '2026-06-28T22:40:52.766774+00:00'
product: protheus
section_id: 1500001537561
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB - ECD -  "O código
  de aglutinação e o código de aglutinação superior da linha..."
type: support-article
updated_at: '2026-05-04T17:37:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40211895485207-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACTB-ECD-O-c%C3%B3digo-de-aglutina%C3%A7%C3%A3o-e-o-c%C3%B3digo-de-aglutina%C3%A7%C3%A3o-superior-da-linha
---

O erro na validação do arquivo ECD no código de aglutinação do Registro J100 ocorre por divergência na hierarquia ou no grupo IND\_GRP\_BAL entre códigos filho e superior. A solução envolve validar a visão gerencial, conferir totalizadoras, hierarquia e consistência do campo IND\_GRP\_BAL, garantindo que ambos pertençam ao mesmo grupo conforme a norma da ECD.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40211933880471) Tempo aproximado para leitura: **25 min**  
  
**Dúvida**  
 Erro ao validar o arquivo da ECD no código de aglutinação no Registro J100 - Balanço Patrimonial:

"O código de aglutinação e o código de aglutinação superior da linha devem pertencer ao mesmo grupo (IND\_GRP\_BAL)."

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40211895441815)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB - a partir da versão 12  
  
  
**Solução**  
O erro ocorre quando há divergência na hierarquia ou na classificação dos grupos (IND\_GRP\_BAL) entre o código de aglutinação filho e o superior. É necessário validar a estrutura da visão gerencial utilizada.

**Passos**

1. Emita os relatórios de balanço e balancete informando o mesmo código de visão gerencial utilizado para geração da ECD
2. Verifique se as entidades totalizadoras da visão gerencial estão configuradas corretamente.
3. Valide se as entidades superiores (código de aglutinação superior) estão corretamente vinculadas à hierarquia.
4. Certifique-se de que o campo IND\_GRP\_BAL esteja preenchido de forma consistente entre o código de aglutinação e seu respectivo superior, garantindo que ambos pertençam ao mesmo grupo definido na norma da ECD.

Exemplo da montagem da visão gerencial:

1. Totalizadora do Ativo:

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40211895444503)
2. Totalizadora do Passivo:

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40211895446679)
3. Quando o grupo de contas for do Ativo, o campo "Coluna" deve estar igual a 1

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40211933890967)
4. Quando o grupo de contas for do Passivo, o campo "Coluna" deve estar igual a 2

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40211933895063)
5. Ao gerar o arquivo da ECD por meio da rotina de escrituração contábil (CTBS001), verifique a visão gerencial que está sendo informada.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40211895459735)
6. Gere o arquivo e verifique se o valor apresentado corresponde ao mesmo apresentado no razão e no balancete.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40211933903383)
7. Estrutura do Registro com base no manual da receita:  
     
   |J100|001211|D|3|00121|**P**|FORNECEDORES|0,00|C|2500,00|C||  
     
   Campo 01 – Tipo de Registro: J100  
   Campo 02 – Código de Aglutinação: 001211  
   Campo 03 – Indicador do Tipo de Código de Aglutinação: D  
   Campo 04 – Nível do Código de Aglutinação: 3  
   Campo 05 – Código de Aglutinação de Nível Superior: 00121  
   Campo 06 – Indicador de Grupo do Balanço: **P (Passivo**)  
   Campo 07 – Descrição do Código de Aglutinação: FORNECEDORES  
   Campo 08 – Valor Inicial do Código de Aglutinação: 0,00 (0,00)  
   Campo 09 – Indicador da Situação do Saldo Informado no Campo Anterior: C (Credito)  
   Campo 10 – Valor Final do Código de Aglutinação: 2500,00 (2.500,00)  
   Campo 11 – Indicador da Situação do Saldo Informado no Campo Anterior: C (Credito)  
   Campo 12 – Referência à Numeração das Notas Explicativas: Não há
8. Verifique se o nível de aglutinação criado na Visão segue o mesmo conceito do plano de contas – Registro I050  
     
   [NIVEL O plano de contas com todas as suas contas sintéticas e analíticas deve conter no mínimo 4 níveis (Resolução CFC 1299/2010).](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028148692-MP-SIGACTB-ECD-I050-5-NIVEL-O-plano-de-contas-com-todas-as-suas-contas-sint%C3%A9ticas-e-anal%C3%ADticas-deve-conter-no-m%C3%ADnimo-4-n%C3%ADveis-Resolu%C3%A7%C3%A3o-CFC-1299-2010-?source=search)  
     
   Analise o que o manual da receita descreve sobre o "NIVEL\_AGL" do J100 (Balanço).

   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40211895463959)

   Com isso, o cadastro da visão gerencial sintética e analítica deve conter a somatória de no mínimo 4 níveis.

**Saiba mais:**  
[ECD - ESTRUTURA NIVEL VISÃO GERENCIAL J100 E J150](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33071442613271-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-EXTRUTURA-NIVEL-VIS%C3%83O-GERENCIAL-J100-E-J150)  
[ECD registro J005 - VL\_CTA\_INI / IND\_COD\_AGL e IND\_GRP\_BAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028866271-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACTB-ECD-registro-J005-VL-CTA-INI-IND-COD-AGL-e-IND-GRP-BAL)
