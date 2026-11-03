---
article_id: 20026019768727
category: Escrita Fiscal - Configurador de Tributos
content_hash: bdd1b511b181b3aed3e1024a17a04f2b0dd61396a611f4c817d33f8fa1b0c251
fetched_at: '2026-06-28T22:39:17.230426+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como configurar
  o calculo do diferencial de alíquotas entradas pelo conv. 52/91 no FISA170?
type: support-article
updated_at: '2025-12-10T12:59:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20026019768727-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-calculo-do-diferencial-de-al%C3%ADquotas-entradas-pelo-conv-52-91-no-FISA170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20026013843991) Tempo aproximado para leitura: 05:00**min** **Dúvida**  
Como configurar o calculo do diferencial de aliquotas entradas  pelo conv 52/91 no fisa170?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões]  
  
**Solução**MV\_ESTADO = GO  
   
Fornecedor = SP  
   
Calculo anexo I  
![](https://atendimento.totvs.com/attachments/token/7dpIS43wtjkfcaL2HJSoB4PIg/?name=image001.png)  
Valor da mercadoria = 2310,33 / 0,912 = 2.533,26  
2533,26 \* 36,92% = 935,27  
935,27\*17% = 159,00  
   
Imposto a deduzir  
2533,26 \* 36,92% = 935,27  
935,27\*4% = 37,41  
   
Valor do diferencial de alíquotas = 159,00 - 37,41 = 121,59  
   
Configurações no Fisa170  
   
![](https://totvssuporte.zendesk.com/attachments/token/GaBQvQKFQVcckf3oj4iKG0swL/?name=image.png)  
   
Perfil do Produto  
   
![](https://totvssuporte.zendesk.com/attachments/token/lZHhc9l4rCGQb1Ky2ZMzisWx2/?name=image.png)  
   
Cadastro de produtos  
![](https://totvssuporte.zendesk.com/attachments/token/W0RzG76tR7t893fBT8OKmwoes/?name=image.png)  
   
Perfil de Operação  
   
![](https://totvssuporte.zendesk.com/attachments/token/lyGH9JzkQomGuHLqcez4b9Scr/?name=image.png)  
   
   
Perfil de Participante  
![](https://totvssuporte.zendesk.com/attachments/token/lJAMn0BMhlVmi1JAZkguhovCa/?name=image.png)  
   
Perfil Origem / Destino  
   
![](https://totvssuporte.zendesk.com/attachments/token/c3OiPOAzhCOWBt8SKslmljvxz/?name=image.png)  
   
Regra de Base de Calculo - Entradas conv 52/91 anexo I  
   
![](https://totvssuporte.zendesk.com/attachments/token/ewwzibwyrTq9bwm3Sv9jWMITp/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/IhX6OFoWnkUrc1qvtOX1C0BOB/?name=image.png)  
   
Regra de Aliquota 17%  
![](https://totvssuporte.zendesk.com/attachments/token/5c20c4scqrlb4WPP2pQXVms8k/?name=image.png)  
Regra de aliquota 8,80%  
![](https://totvssuporte.zendesk.com/attachments/token/VtJZ6asPZgsgwYYO0qVeCdXda/?name=image.png)  
   
Regra de Escrituração  
   
![](https://totvssuporte.zendesk.com/attachments/token/keqN860c0yFJySeKCDYPeI4IU/?name=image.png)  
   
Regra de calculo  documentos fiscais  
   
![](https://totvssuporte.zendesk.com/attachments/token/VuzV7nOV7QOoi4z1b2kBgdk21/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/gMMj56MJ16RpAsdjrx3W1KpUd/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/73EzkN7AXNFUt4W8h5gkiPiam/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/1j5Om9cedkMjwmwhHXDkMJaog/?name=image.png)  
Formula , após criar o imposto para deduzir alterar de forma manual a formula do calculo  
   
![](https://totvssuporte.zendesk.com/attachments/token/xWMdbVrik7oUg4w5WtsR5VWxG/?name=image.png)  
   
   
Calculo do Imposto para deduzir conv 52/91  
   
![](https://totvssuporte.zendesk.com/attachments/token/njC74BSnYSl0HY0rKTc8MRho0/?name=image.png)  
   
Perfis os mesmos  
   
Regra de Base de calculo imposto para deduzir conv 52/91  
![](https://totvssuporte.zendesk.com/attachments/token/KQsbUO1R1EA6bCkHRgAyFonQi/?name=image.png)  
Formula  
![](https://totvssuporte.zendesk.com/attachments/token/Wz9H6cGiW4DnswI6Ec6CkG7T2/?name=image.png)  
   
Regra de Alíquota  
![](https://totvssuporte.zendesk.com/attachments/token/nrcYcCZJwPZQPK4EgOcqIyH0n/?name=image.png)  
   
Regra de escrituração não tem  
   
Regra de calculo Documentos Fiscais do imposto a deduzir da base das entradas conv 52/91  
![](https://totvssuporte.zendesk.com/attachments/token/h6Jon3DgiquYIRTN0X4iSpdII/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/ClJu1tAuqLCvPEtyfE31kODdm/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/31OUp91dW8ldZdgcHrns8wbZt/?name=image.png)  
Formula  
![](https://totvssuporte.zendesk.com/attachments/token/4sp0k5xkIROnUT2oMhdSVaAZM/?name=image.png)  
   
TES  
Calcula icms = sim  
L fiscal icms = outros  
CFOP = 2556  
Sit trib icm = 20  
Mat consumo = sim  
   
Documento de entradas  
   
![](https://totvssuporte.zendesk.com/attachments/token/aeMreRvJvBTWGVvetYOm5d8yQ/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/IFNoDu87c8ca0101irk5I9rUz/?name=image.png)  
   
Escrituração  
![](https://totvssuporte.zendesk.com/attachments/token/Km1EIGgbpwu7sv6SKvoLCHD1z/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/r5SJOUzcVuFzzM2TKc2evEE7v/?name=image.png)  
   
Apuração do ICMS  
![](https://totvssuporte.zendesk.com/attachments/token/gZmoPX48udzA7XVPCFaAK2cxy/?name=image.png)  
Segue anexos
