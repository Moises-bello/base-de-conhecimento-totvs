---
article_id: 360040496994
category: RH - Contabilização
content_hash: 80559315831d1ff576fd952411b3b83861de894784f17c92bcb71a91069300e6
fetched_at: '2026-06-28T22:43:46.084329+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Como efetuar a contabilização da provisão sem rateio
type: support-article
updated_at: '2025-07-30T13:40:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040496994-RH-Linha-Protheus-GPE-Como-efetuar-a-contabiliza%C3%A7%C3%A3o-da-provis%C3%A3o-sem-rateio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:01:30 min  
  
Dúvida**Como efetuar a contabilização da provisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**1. Ter cadastrado no sistema verbas relacionadas aos identificadores de calculo específicos para cada provisão conforme abaixo:  
 **Identificadores – Provisão de Férias**

**Provisão**   
0130  -  Valor  da Provisão  
0131  -  INSS  
0132  -  FGTS  
0254  -  Adicional  
0255  -  Um Terço         
  
**Baixa Férias**  
0233  -  Valor  da Provisão  
0234  -  INSS  
0235  -  FGTS  
0258  -  Adicional  
0259  -  Um Terço  
  
**Baixa Rescisão**  
0262  -  Valor Provisão  
0263  -  Adicional  
0264  -  Um Terço     
0265  -  INSS  
0266  -  FGTS  
  
**Baixa Transf.**  
0239 - Valor Provisão   
0240 - INSS  
0241 - FGTS  
0260 - Adicional  
0261 - Um Terço     
  
**Identificadores – Provisão de 13º Salário**

**Provisão**  
0136 - Provisão 13º Salário  
0137 - INSS Provisão 13º Salário  
0138 - FGTS Provisão 13º Salário   
0267 - Adicional Provisão 13º Salário  
0268 - Adiantamento 1ª Parcela e 13º Salário na Provisão  
  
**Baixa Rescisão**  
0274  -  Valor Provisão  
0275  -  Adicional  
0276  -  INSS  
0277  -  FGTS

**Baixa Transf.**  
0270  -  Valor Provisão  
0271  -  Adicional  
0272  -  INSS  
0273  -  FGTS  
  
**Baixa 13º Sal**  
0332  -  Valor  da Provisão  
0333  -  Adicional  
0334  -  1ª Parcela          
0335  -  INSS  
0336  -  FGTS  
1854 - Baixa antecipação 1ª parcela do 13º Salário Resc.   
  
2. Após realizar o cadastro das verbas relacionadas aos Identificadores de cálculo, deve vincular um lançamento padrão as verbas, na aba Contabilização:  
**IMPORTANTE:** Os lançamentos padrões são específicos de cada empresa, então não existe um cadastro padrão para isso, mas temos um exemplo de lançamento padrão.

Exemplo de LP: [RH - Linha Protheus - GPE - Como configurar Lançamento Padrão para Folha de Pagamento do Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021101152-RH-Linha-Protheus-GPE-Como-configurar-Lan%C3%A7amento-Padr%C3%A3o-para-Folha-de-Pagamento-do-Protheus-)  
  
Vamos usar a verba P51 como exemplo de amarração com LP:   
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5121282474007/mceclip0.png)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5121286457879/mceclip1.png)  
  
3. Após o cadastro das verbas e vinculo dos lançamentos padrões, é necessário calcular a provisão:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5121327263639/mceclip2.png)

Na visualização do calculo, verificamos as verbas apresentadas abaixo (P51, P61,P66,P71,P03,P11,P15). Considerando que será contabilizada todas as verbas apresentadas, vincule o LP em todas as verbas listadas:   
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5121355387415/mceclip3.png)

As informações de provisão estão na tabela SRT - Movimento de Provisões.

**ATENÇÃO:** Caso a empresa possua programação de rateio (MV\_RATPROV=S), as informações serão gravadas na tabela SRT e também na tabela RHT, sendo a RHT preponderante para a contabilização. 

4. Na rotina de contabilização informe nas perguntas que deseja contabilizar a provisão:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5121360785431/mceclip4.png)  
  
Tela lançamentos contábeis:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5121399796887/mceclip5.png)  
Os valores apresentados devem ser exatamente conforme relatório de provisão, considerando a linha no Mês:

Provisão de Férias:![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5121439092375/mceclip6.png)  
Provisão de 13º:  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5121395034007/mceclip7.png)

**IMPORTANTE:**Por padrão, os valores das provisões só serão apresentados de forma acumulada em transferências ou quando for efetuado cálculo para funcionário que já possui avos de férias e 13º adquiridos e não possuem cálculo na competência anterior.  
  
Veja o exemplo abaixo:

Funcionário admitido em 01/10/2021 e primeiro cálculo de provisão na competência 10/2022:  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5121474329239/mceclip8.png)

O valor apresentado corresponde aos 4/12 avos de direito e está acumulado na competência pois não existe cálculo anterior:![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5121458499607/mceclip9.png)  
  
Na competência seguinte, o sistema voltará a provisionar apenas 1/12 de férias e 13º.
