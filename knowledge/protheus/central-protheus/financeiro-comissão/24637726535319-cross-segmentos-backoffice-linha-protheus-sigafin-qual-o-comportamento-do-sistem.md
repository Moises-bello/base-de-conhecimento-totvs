---
article_id: 24637726535319
category: Financeiro - Comissão
content_hash: 95f6a7a90282763d37641e217a817ec40ed73fc0ee94f19e7c95643cb70be66c
fetched_at: '2026-06-28T22:37:50.885744+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Qual o comportamento
  do sistema MV_COMIDEV
type: support-article
updated_at: '2025-03-19T17:19:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24637726535319-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Qual-o-comportamento-do-sistema-MV-COMIDEV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26669210588439) Tempo aproximado para leitura: **00:05:00****min**

**Dúvida**  
Qual o comportamento do sistema MV\_COMIDEV?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**

O parâmetro é responsável por gerar uma comissão negativa nos casos de devolução da nota fiscal pelo cliente, permitindo assim o controle das comissões pagas e o estorno do pagamento da comissão quando necessário.

**Exemplo:**

Ao emitir uma **NF** de devolução pelo módulo de **Faturamento**, é gerado um registro negativo de comissão na rotina de **Manutenção de Comissões (MATA490 - tabela SE3)**. Nesse caso, ao compensar a **NCC** gerada pela devolução, a comissão continua sendo calculada sobre a **NCC**.

Quando os parâmetros estão configurados da seguinte forma:

* **MV\_COMIDEV = T**
* **MV\_COMISCR = S**
* **Calc comiss s/ NCC? = SIM**

Neste cenário, ao compensar a **Nota de Crédito de Cliente (NCC)** gerada pela devolução, seja no valor parcial ou total, ao emitir uma Nota Fiscal de devolução, gera um registro negativo de comissão na rotina de **Manutenção de Comissões (MATA490)**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24637717229591)

**Importante**

A **Manutenção de Comissões**, corresponde a tabela **SE3** e a mesma deve possui o mesmo compartilhamento da **SE1 e SE2** para que não gere inconsistências.

**2º Cenário:**

Ao compensar uma **NCC** gerada por uma devolução, a comissão não é calculada sobre a **NCC**. A **comissão** é gerada apenas pela baixa parcial da NF (diferença entre o valor da **NF** e a **NCC** compensada). Nesse processo, a devolução pelo módulo de **Faturamento** gera apenas a **NCC**, sem registrar nenhum lançamento na **Manutenção de Comissões (MATA490 - Tabela SE3)**.

Quando os parâmetros estão configurados da seguinte forma:

* **MV\_COMIDEV = F**
* **MV\_COMISCR = N**

O parâmetro **MV\_COMISCR** configurado como "**NÃO**" substitui o parâmetro **F12 Calc comiss s/ NCC?**, desconsiderando o cálculo de comissão sobre a **NCC.**

**3º Cenário:**

A devolução realizada pelo módulo de **Faturamento** gera apenas a **NCC,** sem registrar qualquer lançamento na **Manutenção de Comissões (MATA490 - Tabela SE3)**. Contudo, ao compensar a **NCC** gerada pela devolução, a comissão é calculada com base na **NCC**.

Quando os parâmetros estão configurados da seguinte maneira:

* **MV\_COMIDEV = F**
* **MV\_COMISCR = S**
* **Calc comiss s/ NCC? = SIM**

A comissão será efetivamente gerada sobre a **NCC**.

**Importante**

Para que a comissão seja gerada na compensação, é essencial que o motivo de baixa esteja corretamente configurado. Para isso, acesse **Miscelânea -> Arquivos**, altere o motivo **CMP** e habilite o cálculo de comissão para o motivo de baixa.

Se a compensação for realizada manualmente através da rotina **Compensação Contas a Receber** **(FINA330)**, os parâmetros **F12** devem ser configurados da seguinte forma:

**Calc comiss s/ NCC?**

Indica se o sistema deve calcular comissão nas compensações de títulos de crédito do tipo **NCC**.

**SIM: O sistema calcula comissão.**  
**NÃO: O sistema não calcula comissão.**

**Calc comiss s/ RA?**  
Indica se o sistema deve calcular comissão nas compensações de títulos de crédito do tipo **RA**.

**SIM: O sistema calcula comissão.**  
**NÃO: O sistema não calcula comissão.**

**A comissão será gerada exclusivamente a partir das notas de débito exemplo (NF, BOL, FT e etc) e nunca a partir das notas de crédito (RA, NCC)**

**Definição dos Parâmetros relacionados a rotina**

**MV\_CMPDEVV -** Define se serão compensados automaticamente os títulos de NCC na Devolução de Venda.

**MV\_COMISCR -** Determina se o cálculo de comissão para o vendedor será permitido na compensação CR. Use "S" para permitir o cálculo e "N" para não permitir. O parâmetro

**MV\_COMISCR -** quando configurado como "NÃO", substitui o parâmetro F12 Calc comiss s/ NCC? na rotina de compensação a receber (FINA330).

**Saiba mais**

[Ponto de Entrada - FINA440](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017962152)

[Recalculo de Comissão - FINA440](https://tdn.totvs.com/pages/releaseview.action?pageId=312162528)

[Compartilhamento das tabelas envolvidas na geração da comissão](https://tdn.totvs.com/display/public/PROT/FIN0065_Compartilhamento_SE3)
