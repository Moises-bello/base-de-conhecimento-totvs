---
article_id: 24661516033943
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 3cbe5c258043c74a17e7462017fc40bd2a99f8486ef6b6dd672e32840a1385e5
fetched_at: '2026-06-28T22:40:47.528874+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 ECF O registro
  não deve ser informado para esse perfil e/ou tipo de operação. Consulte o guia prático
  da ECF e verifique a obrigatoriedade dos registros na 3.1.2. Tabela de Registros.
type: support-article
updated_at: '2026-06-19T18:49:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24661516033943-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-O-registro-n%C3%A3o-deve-ser-informado-para-esse-perfil-e-ou-tipo-de-opera%C3%A7%C3%A3o-Consulte-o-guia-pr%C3%A1tico-da-ECF-e-verifique-a-obrigatoriedade-dos-registros-na-3-1-2-Tabela-de-Registros
---

**Ocorrência**

O registro não deve ser informado para esse perfil e/ou tipo de operação. Consulte o guia prático da ECF e verifique a obrigatoriedade dos registros na 3.1.2. Tabela de Registros.  
   
   
![](https://totvssuporte.zendesk.com/attachments/token/XRXdt2lthqF74yYRqeRDHkkxJ/?name=image.png)  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice  - Microsiga Protheus - Todas as versões   
  
**Causa**

Situação é apresentada quando os parâmetros

* MES\_BAL\_RED ([Registro 0010 Forma de apura. da Estimativa??](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415471717655-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Registro-0010-Forma-de-apura-da-Estimativa?source=search)) foi informado igual E
* ou FORMA\_TRIB\_PER ([Registro 0010 Forma de trib. no Período ?)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415486620695-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Registro-0010-Forma-de-trib-no-Per%C3%ADodo?source=search) foi informado igual 0

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24670332639511)

* Vejamos no arquivo txt a linha onde o erro é apresentado  
    
  ![](https://totvssuporte.zendesk.com/attachments/token/XRXdt2lthqF74yYRqeRDHkkxJ/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/earzdyvdRKM003ikC8gbYWaBs/?name=image.png)  
 

* No arquivo txt o parâmetro MES\_BAL\_RED foi informado BBBBEEEEBBBB

   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41355728089879)  
 

* Veja como o parâmetro pode ser preenchido
* [Registro 0010 Forma de apura. da Estimativa??](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415471717655-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Registro-0010-Forma-de-apura-da-Estimativa?source=search)

![](https://totvssuporte.zendesk.com/attachments/token/TkP0pORVWxncBnlTRBf9p23CK/?name=image.png)  
   
 

* Conforme manual da receita , só deve gerar o L100 ou o L300 quando  MES\_BAL\_RED = B

   
![](https://totvssuporte.zendesk.com/attachments/token/Ihfs2Lw1oqnD2brt5zUR9LaoO/?name=image.png)  
 

* Com isso, ao informar  "E" sistema não irá gerar para o período informado com E
* Como MES\_BAL\_RED foi informado BBBBEEEEBBBB

   
BBBB(JAN/FEV/MARÇ/ABRIL) - Deve existir os registro  L030 ,L100 ,L210 e L300  
EEEE (MAIO/ JUN/JUL./AGOST) - Não deve existir os registro  L030 ,L100 ,L210 e L300  
BBBB (SET./OUT./NOV./DEZ.)- Deve existir os registro  L030 ,L100 ,L210 e L300  
 

* Ao avaliar o arquivo txt gerado

   
![](https://totvssuporte.zendesk.com/attachments/token/i2tnBioobMm5UeEh30Y0QsUeW/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/lPJftXjASY8peHO3NnPBNrP9j/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/CoP7RQwp2B5ZcKFCKcJcsGPcE/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/C8ewZHsdHTuTY9XqaFaBFewVF/?name=image.png)  
 

* Veja que foi gerado o mês de Agosto , porem como o MES\_BAL\_RED foi informado BBBBEEEEBBBB - esse mês não deveria ter sido gerado no arquivo

   
![](https://totvssuporte.zendesk.com/attachments/token/AKBqoYboc0G2K8fZ0cs4OG7er/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/QU4TGjhkhCha9oOsXAUT1NJCo/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/cliEGtQOy9IK4tmy95L3lwRq0/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/MZn78QPDviM3wvdgcnajyZW2w/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/7EsCSBbRDwu0uQgQWhlIktaew/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/nxlaILw3FWJ7M0spa1sdqzjoq/?name=image.png)  
 

* A situação apresentada pois em algum momento foi importado para o TAF com o parâmetro MES\_BAL\_RED foi informado BBBBEEEBBBBB , com isso a Rotina - TAFA361 (Bloco L - Lucro Líquido)  possui registro do L para o mês de agosto

**Solução**

* Para correção necessário acessar a rotina e excluir o lançamento do período do mês de agosto
* ou Excluir todos os registros, através da rotina TAFTICKET ou [através da rotina Exclusão Por Período Fiscal - TAFAEXCPER](https://tdn.totvs.com/pages/releaseview.action?pageId=273986947)

   
![](https://totvssuporte.zendesk.com/attachments/token/BApFHBrn2Q5ZY4xiwMcCRKGWf/?name=image.png)  
 

* Posteriormente gerar o arquivo TXT
* Caso queira analisar se esse período (agosto) foi importado na ultima revisão, é possível acompanhar os passos abaixo :

   
[Cross Segmento - Backoffice Linha Protheus- SIGACTB - ECF – L300 COMO GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054288214-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-L300-COMO-GERAR?source=search)  
[Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF – L100 COMO GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054165034-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-L100-COMO-GERAR?source=search)
