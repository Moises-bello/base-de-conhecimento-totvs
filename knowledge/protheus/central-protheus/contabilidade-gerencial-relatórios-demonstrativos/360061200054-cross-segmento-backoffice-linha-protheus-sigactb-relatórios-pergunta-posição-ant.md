---
article_id: 360061200054
category: Contabilidade Gerencial - Relatórios Demonstrativos
content_hash: edc8a7e367d04176fc17a48df838e6856b7dd88030115d17d4e623ecfc1ba78d
fetched_at: '2026-06-28T22:40:38.845436+00:00'
product: protheus
section_id: 1500001548882
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Relatórios - Pergunta
  Posição antes de L/P
type: support-article
updated_at: '2024-11-27T14:33:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061200054-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Relat%C3%B3rios-Pergunta-Posi%C3%A7%C3%A3o-antes-de-L-P
---

**Dúvida**

Comportamento do pergunta **Posição antes de L/P**  nos relatórios.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101389534)

**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 11.80  
  
**Solução**

Conceito da pergunta " Posição antes de L/P"

* Ao informar  **NÃO,**  as **contas de resultados** **(Receita e Despesa)**ficaram zeradas e o relatório considera a apropriação da **conta patrimonial /Lucros e Perdas****(Conta apuração)** que recebeu o lucros e perdas.
* Se a pergunta estiver  **SIM**,  significa que o relatório não irá considerar a apuração, ou seja, as **contas de resultado (Receita e Despesa)** demonstrarão os saldos e o lote de apuração não será considerado, neste caso a **conta patrimonial /Lucros e Perdas****(Conta apuração)** que recebeu os valores de lucros e perdas também não terá o valor de apuração.

Com isso

Para as **contas de resultado (Receita e Despesa)**

* Pergunta Posição antes de L/P? = SIM  - o sistema apresenta a situação da **entidade (Receita e Despesa)** antes da apuração (desconsiderando o lançamento de zeramento / apuração a entidade) , e o relatório é gerado  com saldo
* Pergunta Posição antes de L/P? = NAO  - o sistema  apresenta a situação atualmente da **entidade (Receita e Despesa)** ( considerando o lançamento de zeramento / apuração a entidade) ,e o relatório é gerado   Zerado

Para a **conta patrimonial /Lucros e Perdas (Conta apuração)**

* Pergunta Posição antes de L/P? = SIM  - o sistema apresenta a situação da **conta patrimonial /Lucros e Perdas** **(Conta apuração)** antes da apuração (desconsiderando o lançamento de zeramento / apuração a entidade) , e o relatório é gerado Zerado , pois antes a apuração as contas de Apuração não tinha saldo
* Pergunta Posição antes de L/P? = NAO  - o sistema  apresenta a situação atualmente da **conta patrimonial /Lucros e Perdas (Conta apuração)** ( considerando o lançamento de zeramento / apuração a entidade) ,e o relatório é gerado  com saldo que recebeu da apuração.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23508429074455)  Caso o lançamento que zerou a entidade não tenha sua origem na [rotina CTBA211](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005048472-MP-SIGACTB-Como-realizar-Apura%C3%A7%C3%A3o-de-resultados-dentro-do-Protheus-?source=search) o paramento não surtirá nenhum efeito , com isso caso o lançamento de zeramento da entidade tenha sido realiza manualmente (CTBA101 ou CTBA102) e não através da rotina de apuração de resultado [(CTBA211)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005048472-MP-SIGACTB-Como-realizar-Apura%C3%A7%C3%A3o-de-resultados-dentro-do-Protheus-?source=search) não irá desconsiderar o lançamento de zeramento da entidade.

Com isso para que o parâmetro realize sua função é necessário que :

* Seja realizada apuração de resultado (zeramento das contas de receita e despesa)  através da rotina [de apuração de resultado (CTBA211)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005048472-MP-SIGACTB-Como-realizar-Apura%C3%A7%C3%A3o-de-resultados-dentro-do-Protheus-?source=search)
* [o sistema gravar no lote de apuração o campo CT2\_ROTINA= CTBA211](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042028234-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-PREENCHIMENTO-DOS-CAMPOS-CT2-MANUAL-E-CT2-ROTINA-?source=search)
* O  sistema gravar na tabela [CW0 registro de apuração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024134092-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA007-CTBA211-CHAVE-DE-APURA%C3%87%C3%83O-CW0-?source=search)

[Balancetes (CTBR040) - Como emitir o relatório anual, com apurações trimestrais/semestrais/mensais.](https://tdn.totvs.com/pages/releaseview.action?pageId=718409259)

<https://tdn.totvs.com/display/public/PROT/CTB0152_Conta_X_12_MESES_CTBR265>
