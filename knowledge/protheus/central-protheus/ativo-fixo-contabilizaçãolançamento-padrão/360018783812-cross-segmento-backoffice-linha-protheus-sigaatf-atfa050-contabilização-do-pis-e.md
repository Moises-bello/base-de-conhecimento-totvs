---
article_id: 360018783812
category: Ativo Fixo - Contabilização/Lançamento padrão
content_hash: 37472d69150dc5b4ddceb8c6fbcf8a7a9f156b28289970f9bd9423bd0828a0cb
fetched_at: '2026-06-28T22:41:42.359830+00:00'
product: protheus
section_id: 1500001536421
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA050 Contabilização
  do Pis e Cofins ao realizar a depreciação '
type: support-article
updated_at: '2023-11-17T17:55:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018783812-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA050-Contabiliza%C3%A7%C3%A3o-do-Pis-e-Cofins-ao-realizar-a-deprecia%C3%A7%C3%A3o
---

**Dúvida**

Contabilização do Pis e Cofins ao realização da depreciação   
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - Ativo Fixo - Todas as versões  
  
  
  
**Solução**

Para que o sistema realize a contabilização do Pis e do Cofins durante a depreciação , se faz necessário realizar a configuração no lançamento padrão , segue abaixo o exemplo da configuração para contabilizar o PIS

* Rotina ATFA012 : Cadastro do bem
* N3\_VORIG1 = 10.000,00

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014799651)

* N1\_ALIQPIS = 1,65 (o sistema não permite alterar o tamanho das casas decimais , com isso não é possível colocar o valor Divido por 100 , Sendo necessário colocar na formula)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014799811)

* Campo **N1\_MESCPIS = 12** deve estar preenchido

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014768752)**

* **Configuração lançamento padrão 820**

IIF (SN4->N4\_TIPOCNT== "4",SN3->N3\_VORIG1/SN1->N1\_MESCPIS\*SN1->N1\_ALIQPIS/100,0)

Se for N4\_TIPOCNT igual a 4 fará o seguinte calculo: 10.000/12  = 833,33  \*  1,65  = 1375  /100 = 13,75

Esse filtro na SN4 é necessário para que o sistema não gere o valor dobrado conforme a documentação: [Valores duplicados na contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006600272-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA050-Valores-duplicados-na-contabiliza%C3%A7%C3%A3o?source=search) indica.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9319055085847)

* Através da rotina ATFA050 : Ao realizar a Depreciação o sistema apresenta a contabilização

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014800171)

Saiba mais :

[MV\_ATFCONT – Configuração do parâmetro para cálculos do Ativo Online ou Offline](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11563614676375-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-MV-ATFCONT-Configura%C3%A7%C3%A3o-do-par%C3%A2metro-para-c%C3%A1lculos-do-Ativo-Online-ou-Offline?source=search)
