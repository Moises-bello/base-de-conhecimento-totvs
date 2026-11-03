---
article_id: 360016597051
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: dadd70ad729ccf25386c7e9dfdd8a6225aa7ffc4641dc49b91981342c902072f
fetched_at: '2026-06-28T22:40:44.567676+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBS001 - Erro na geração
  da ECD HELP: BALANCETE PARCIAL '
type: support-article
updated_at: '2023-06-23T18:39:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016597051-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Erro-na-gera%C3%A7%C3%A3o-da-ECD-HELP-BALANCETE-PARCIAL
---

**Dúvida**

 Erro na geração da ECD HELP: BALANCETE PARCIAL ?  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
  
**Solução**

Para validação : **BALANCETE PARCIAL**  

* [LAYOUT 1 ao 6 Como gerar o arquivo da ECD com Apuração trimestral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016231592-MP-SIGACTB-ECD-LAYOUT-1-ao-6-Como-gerar-o-arquivo-da-ECD-com-Apura%C3%A7%C3%A3o-trimestral-?source=search) A geração da ***ECD*** independente do tipo de apuração, trimestral ou anual o calendário utilizado deve ser anual (contendo 12 períodos).  
  Caso não possua um calendário criado nesta estrutura, crie com 12 períodos e não amarre a moeda. Informe o código deste novo calendário ao gerar uma revisão da ECD.
* [PARTIR DO LAYOUT 7 TRIMESTRAL UNIFICADA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025347591-MP-SIGACTB-ECD-A-PARTIR-DO-LAYOUT-7-TRIMESTRAL-UNIFICADA-?source=search)Necessário criar um calendário Trimestral   
  Caso não possua um calendário criado nesta estrutura, crie com 4 períodos e não amarre a moeda. Informe o código deste novo calendário ao gerar uma revisão da ECD.

No passo 5 da Wizard (CTBS001 )

Para empresas apuradas anualmente, no parâmetros da ECD informar da seguinte maneira:  
- Período Inicial Lcto ? = 01/01/20XX  
- Período Final Lcto ? = 31 /12/20XX  
- Apuração do Exercício(L/P) ? = 31/12/20XX

Para empresas apuradas trimestralmente, no parâmetros da ECD informar da seguinte maneira:  
- Período Inicial Lcto ? = 01/01/20XX  
- Período Final Lcto ? = 31 /03/20XX  
- Apuração do Exercício(L/P) ? = Em Branco.

Veja mais :

[Parâmetros para geração da ECD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009296382-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Como-preencher-os-par%C3%A2metros-para-gera%C3%A7%C3%A3o-da-ECD-)

[Balancete Parcial](http://tdn.totvs.com/display/public/PROT/ECD0013_ECD_BALANCETE_PARCIAL_PERIODO_INVALIDO)

[Indicador Situação Especial- Campo IND\_SIT\_ESP](https://tdn.totvs.com/pages/releaseview.action?pageId=547876652) (DSERCTR1-26950)
