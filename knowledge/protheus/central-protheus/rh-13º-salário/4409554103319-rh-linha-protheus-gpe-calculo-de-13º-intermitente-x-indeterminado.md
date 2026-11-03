---
article_id: 4409554103319
category: RH - 13º salário
content_hash: 3628ce8eb8b386d08362333a8ead901cbff3f530be6f6b36b6e20492fddba33e
fetched_at: '2026-06-28T22:44:00.449180+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Calculo de 13º intermitente X indeterminado
type: support-article
updated_at: '2026-06-25T11:39:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409554103319-RH-Linha-Protheus-GPE-Calculo-de-13%C2%BA-intermitente-X-indeterminado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26732029642519) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**  
Como funciona o calculo de 13º quando o contrato anterior era intermitente e passou a ser indeterminado?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Funcionário entrou na empresa com contrato intermitente e alguns meses depois mudou para contrato por tempo indeterminado, ao calcular a segunda parcela do13º salário os valores pagos referente ao período de quando estava no contrato intermitente são **deduzidos do valor calculado** pela rotina.  
  
No caso de 1ª parcela, só haverá pagamento caso esteja selecionado o pagamento de **complemento** e caso exista valor superior ao já pago em folha para o intermitente.  
  
Desta forma, o sistema levará o **identificador 0183** (antecipação de decimo terceiro) contendo os valores pagos como contrato intermitente.  
  
**Exemplo de cálculo**:  
Através da ficha financeira conseguimos conferir o valores gerados de 13º no período de contrato intermitente:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409547211415)  
  
O sistema carrega no ID 0183 o valor da soma dos proventos de 13º:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409553962903)

**Importante:**  
Como não há previsão legal explicita quanto ao pagamento das férias, 13° salário e suas médias, mediante a conversão do tipo de contrato de trabalho, serão computados e pagos normalmente ao trabalhador já no contrato vigente ‘indeterminado’, considerando contagem de tempo **a partir do primeiro contrato ativo** com este Empregador, deduzindo assim o valor já pago anteriormente na vigência do contrato intermitente.  
  
Por exemplo, se o funcionário foi admitido em **01/01/2024** como [intermitente](https://totvssuporte.zendesk.com/knowledge/editor/01HEJTM16FKY0JA8W792VBM3PE/pt-br?brand_id=1509248&return_to=%2Fhc%2Fpt-br%2Farticles%2F4418877287703) e alterou o seu contrato para [indeterminado em 01/08/2024](https://totvssuporte.zendesk.com/knowledge/editor/01HEJTM16FKY0JA8W792VBM3PE/pt-br?brand_id=1509248&return_to=%2Fhc%2Fpt-br%2Farticles%2F4418877287703), a contagem de direito ao 13º será baseado em sua [data oficial de admissão](https://totvssuporte.zendesk.com/knowledge/editor/01HEJTM16FKY0JA8W792VBM3PE/pt-br?brand_id=1509248&return_to=%2Fhc%2Fpt-br%2Farticles%2F4418877287703) que foi em [01/01/2024](https://totvssuporte.zendesk.com/knowledge/editor/01HEJTM16FKY0JA8W792VBM3PE/pt-br?brand_id=1509248&return_to=%2Fhc%2Fpt-br%2Farticles%2F4418877287703). O sistema calculará 12 avos e [abaterá os valores já pagos](https://totvssuporte.zendesk.com/knowledge/editor/01HEJTM16FKY0JA8W792VBM3PE/pt-br?brand_id=1509248&return_to=%2Fhc%2Fpt-br%2Farticles%2F4418877287703) de 13º enquanto [intermitente](https://totvssuporte.zendesk.com/knowledge/editor/01HEJTM16FKY0JA8W792VBM3PE/pt-br?brand_id=1509248&return_to=%2Fhc%2Fpt-br%2Farticles%2F4418877287703). ([Orientações Consultoria de Segmentos - Empregado Intermitente](https://tdn.totvs.com/pages/releaseview.action?pageId=636952260))

**Saiba Mais**  
[RH - 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)  
[RH - Linha Protheus - GPE - Como emitir Relatório Ficha Financeira](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiX1INgAQQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBiGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDM5NjA3MzA3NzUtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tZW1pdGlyLVJlbGF0JUMzJUIzcmlvLUZpY2hhLUZpbmFuY2VpcmEGOwhUOg5zZWFyY2hfaWRJIik3MTFlMGUzZi1mYWU3LTRlMzAtYTllMi05NjRiZjQ5YzgxNjkGOwhGOglyYW5raQw6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhVmaWNoYSBmaW5hbmNlaXJhBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--e3ac585b6849691f12b57408bc6737c48587dc71)  
[RH - Linha Protheus - GPE - Como é considerado o cálculo do 13° salário para funcionário com contrato intermitente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058666654-RH-Linha-Protheus-GPE-Como-%C3%A9-considerado-o-c%C3%A1lculo-do-13-sal%C3%A1rio-para-funcion%C3%A1rio-com-contrato-intermitente)
