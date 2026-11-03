---
article_id: 360027941171
category: RH - Definições de Cálculo
content_hash: 92f386344533e1b18fc2c7e6c3152d7afb9b777bbf059fb024e612b58ca483ec
fetched_at: '2026-06-28T22:43:22.223854+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE -  Como configurar verbas de férias mês seguinte
  para que não constem indevidamente nos meses subsequentes ao calculo de folha
type: support-article
updated_at: '2026-06-26T16:37:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027941171-RH-Linha-Protheus-GPE-Como-configurar-verbas-de-f%C3%A9rias-m%C3%AAs-seguinte-para-que-n%C3%A3o-constem-indevidamente-nos-meses-subsequentes-ao-calculo-de-folha
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36862836684951) Tempo aproximado para leitura: 00:02:00 min**  
  
**Dúvida**  
Como configurar as verbas de férias mês seguinte para cálculo automático nas férias e na folha de pagamento para que não constem indevidamente nos meses subsequentes ao calculo de folha?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para que sejam carregadas as verbas de férias mês seguinte na virada da folha, é necessário efetuar as configurações abaixo:  
  
No campo **V. Mes Seguinte (RV\_CODMSEG)**campo das verbas de **Férias Mês Seguinte** deve vincular a verba **Férias Mês**, conforme exemplo abaixo:

Verba com Identificador p/ Cálculo 0072: o campo V. Mes Seguinte (RV\_CODMSEG) permanecerá sem informação.  
  
![](http://tdn.totvs.com/download/attachments/245171289/image2018-3-1_20-6-13.png?version=1&modificationDate=1519945573000&api=v2)

Verba com Identificador p/ Cálculo 0073: o campo **V. Mes Seguinte** (RV\_CODMSEG) deverá ser informado com o código da verba vinculada ao Id 0072  
no caso a verba 129.  
  
![](http://tdn.totvs.com/download/attachments/245171289/image2018-3-1_20-10-31.png?version=1&modificationDate=1519945831000&api=v2)  
**Exemplo: Na verba de ID 0232 devemos associar a verba de ID 0065 no campo RV\_CODMSEG**

**Atenção:** As verbas do mês **nunca** podem ter conteúdo no campo RV\_CODMSEG somente as verbas de mês seguinte que devem conter informação nesse campo.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030097711)

**Importante:**

* As verbas de férias devem possuir **referência para férias** (campo RV\_REFFER configurado com Sim)
* As verbas que se referem a **férias do mês**, exemplo o identificador de cálculo 0072 **devem ficar com SIM** para INSS, FGTS e INSS Férias.
* As verbas de **mês seguinte,** como exemplo o identificador de cálculo 0073 **devem ficar com NÃO** para INSS e FGTS e **SIM** para **INSS Férias.**
* Para calculo do **Imposto de Renda,** as verbas de mês e de mês seguinte **devem estar com SIM** no **campo IR** na aba Incidências.

**Observação:**  
  
Não podemos orientar sobre o preenchimento de códigos de incidências legais das verbas, isso porque pode existir diferenças entre empresas, sindicatos, súmulas, etc.  
O próprio governo não fornece nenhum material com orientação para incidências de verbas, somente em casos muito específicos.

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Configuração do parâmetro MV\_DINSSFM](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhEGKfSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBj2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNjQ1MTY1Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29uZmlndXJhJUMzJUE3JUMzJUEzby1kby1wYXIlQzMlQTJtZXRyby1NVi1ESU5TU0ZNBjsIVDoOc2VhcmNoX2lkSSIpYmJiY2QwZjktNjE4Yi00NGFkLTgzM2UtZDRkYjY5Njk0YjllBjsIRjoJcmFua2kHOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIQIE1WX0RJTlNTRk0GOwhUOhJyZXN1bHRzX2NvdW50aQLyBA%3D%3D--d9f26b9a9dd9563e7db2f128f0838621f178662a)  
[RH - Linha Protheus - GPE - Verbas de férias não estão sendo integradas na folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgnX%2FDRUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBrGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAwNDQ3NjcxMS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtVmVyYmFzLWRlLWYlQzMlQTlyaWFzLW4lQzMlQTNvLWVzdCVDMyVBM28tc2VuZG8taW50ZWdyYWRhcy1uYS1mb2xoYS1kZS1QYWdhbWVudG8GOwhUOg5zZWFyY2hfaWRJIilmMGE3NGNiOS0zNDQzLTQ5YWItOGJhMi1jZWY3YzQwYmQwMWQGOwhGOglyYW5raQ06C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhhmZXJpYXMgbWVzIHNlZ3VpbnRlBjsIVDoScmVzdWx0c19jb3VudGkCrAQ%3D--e790ec1e7409ea76586b2b6598a9e0c3a6dedb09)
