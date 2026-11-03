---
article_id: 360046479594
category: RH - Contabilização
content_hash: 32e6f72736288f08882f38eaee5b673908b745aaf9cebef509e9bb8cd263bd12
fetched_at: '2026-06-28T22:43:46.104948+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Contabilização das verbas de baixa de transferência
type: support-article
updated_at: '2021-06-07T13:37:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046479594-RH-Linha-Protheus-GPE-Contabiliza%C3%A7%C3%A3o-das-verbas-de-baixa-de-transfer%C3%AAncia
---

**Dúvida**Como contabilizar as verbas **de baixa de transferência?**

Exemplo:  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**

**1) Conferir se o parâmetro MV\_TRFAMES está vazio.**  
 **Conceito do parâmetro:  
Situação 1 = Parâmetro vazio, disponibiliza os valores para a contabilização.**  
**Situação 2 = Parâmetro preenchido, não será contabilizado. Serve apenas pra demonstrar as linhas de baixa de transferência no relatório.** **![](https://tdn.totvs.com/download/attachments/364914692/image2018-5-25_16-19-28.png?version=1&modificationDate=1527276934000&api=v2)**

**2. Cadastrar verbas (tipo base), que estejam vinculadas aos Identificadores de Cálculo para Baixa de Transferência na Provisão:**

*Baixa Transf. Férias*

*0239  -  Baixa provisão de ferias trans*

*0260  -  Baixa Adicional provisão de ferias trans*

*0261  -  Baixa 1/3 provisão de ferias trans*

*0240  -  Baixa INSS provisão de ferias trans*

*0241  -  Baixa FGS provisão de ferias trans*

*Baixa Transf. 13º*

*0270  -  Baixa provisão de 13º trans*

*0271  -  Baixa adicional provisão de 13º trans*

*0272  -  Baixa INSS provisão de 13º trans*

*0273  -  Baixa FGTS provisão de 13º trans*

**3. Conferir se foram apuradas as verbas de baixa, depois da transferência e do cálculo da provisão (Miscelânea / Provisões /Provisões Férias/13°/Visualizar :**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360066597534/mceclip1.png)

**4***. Verificar se existe lançamento padrão para as verbas que deseja contabilizar (Atualizações/ Definições de Cálculo/Verbas - Aba Contabilização):*  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067639573/mceclip0.png)

**5. Efetuar o processamento da contabilização (Miscelânea/Fechamentos/Contabilização):**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067639713/mceclip1.png)

**6. É possível consultar o resumo da provisão do Mês na tabela SRZ. Lembrando que as verbas serão apresentadas de acordo com a configuração, impactando na visualização mas nunca nos resultados dos valores:**

Ex: verba 729 = Valor total de R$ 5942,15  
Na provisão:    R$ 3.100,25 + R$ 2841,90 =R$ 5.942,15  
Na tabela SRZ: R$ 5.347,94 + R$ 594,21   =R$ 5.942,15

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360066597754/mceclip2.png)

**7.  Apresentação dos lançamentos contábeis da contabilização das baixas de provisão:**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067653213/mceclip4.png)

**Importante :**

Mais informações sobre o parâmetro MV\_TRFAMES:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067639793/mceclip3.png)
