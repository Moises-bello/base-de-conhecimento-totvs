---
article_id: 360006850892
category: Contabilidade Gerencial - Relatórios Demonstrativos
content_hash: 6d7c58898130e4cf97d6ee508b277c08f1a8019330a9ce3bd474d13c37ba3807
fetched_at: '2026-06-28T22:40:38.864165+00:00'
product: protheus
section_id: 1500001548882
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBR510 - Dre trimestral
type: support-article
updated_at: '2024-06-20T13:44:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006850892-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR510-Dre-trimestral
---

***Dúvida***Como gerar DRE (CTBR510) sem acumular saldo de um trimestre para outro  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 11.80  
  
  
**Requisitos**

* Mesmo se o calendário for trimestral, se não houver a apuração de resultados (CTBA211) o sistema irá trazer o valor acumulado.
* Quando a apuração tiver sido feita para todos os trimestres, só será permitido ver o saldo das contas de resultados, antes da apuração, de um trimestre conforme parametrização.
* [Pergunta Posição antes de L/P](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061200054-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Relat%C3%B3rios-Pergunta-Posi%C3%A7%C3%A3o-antes-de-L-P-?source=search)  
    
  ![](https://totvssuporte.zendesk.com/attachments/token/zTLiQk4menI1aM6AZh79oPIzb/?name=inline-30674436.png)
* Necessário que o calendário amarrado a moeda seja trimestral

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081512933)

* Realize a apuração de resultado trimestralmente
* [Exemplo - Apuração Trimestral : Apuração Sem conta PONTE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041554693-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Trimestral-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search)  
  [APURAÇÃO DAS ENTIDADES CENTRO DE CUSTO,ITEM CONTABIL E CLASSE DE VALOR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046635074-MP-SIGACTB-CTBA211-APURA%C3%87%C3%83O-DAS-ENTIDADES-CENTRO-DE-CUSTO-ITEM-CONTABIL-E-CLASSE-DE-VALOR?source=search)
* Através da rotina [CTBA007](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024134092-MP-SIGACTB-CHAVE-DE-APURA%C3%87%C3%83O-CTBA211?source=search) o sistema grava os 4 registro de apuração com a letra "Z" de zerado

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080452574)

**Solução**

* Neste exemplo apuração de 2018 foi anual e 2019 foi trimestral
* Criamos o calendário anual 2018 e trimestral 2019

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080452394)

* Lançamento realizados

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081512773)

* Através da rotina CTBA102 possível verificar os lançamentos contábeis de 2018 e 2019

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080453854)

* Ao emitir o relatório com o mesmo parâmetro evidenciado pelo cliente no acesso remoto o sistema não apresentou saldo em meu relatório

![](https://totvssuporte.zendesk.com/attachments/token/dnLhjMi2WBi7E8OpNj8WiMHZz/?name=inline275393417.png)​

* Veja que não é apresentado saldo

![](https://totvssuporte.zendesk.com/attachments/token/NlZ5LAqrhT2Js4Mg7KiP30YgQ/?name=inline272679807.png)

* Ao emitir o relatório com parâmetro abaixo o sistema apresentou os valores corretos

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081514553)

* Veja que o sistema gerou os dados corretamente em 30/06/2019 ( 01/04 a 30/06) sem acumular (01/01 a 30/06)

![](https://totvssuporte.zendesk.com/attachments/token/GyntoovY70GwrtptwbdaXAtLA/?name=inline-1986565698.png)

* Veja que o sistema gerou os dados corretamente em 30/09/2019 ( 01/07 a 30/09) sem acumular (01/01 a 30/09)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081514633)

**Saiba mais**

[DRE parâmetros](https://tdn.totvs.com/pages/viewpage.action?pageId=347445199)

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBR040 TRIMESTRAL/ANUAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055860033-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR040-TRIMESTRAL?source=search)
