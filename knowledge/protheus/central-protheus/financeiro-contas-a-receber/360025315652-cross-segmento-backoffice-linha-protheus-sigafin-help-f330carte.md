---
article_id: 360025315652
category: Financeiro - Contas a Receber
content_hash: 268da7af5ef2ad5359e51043f550df28c6610e8d476615b180134a9e66f49f40
fetched_at: '2026-06-28T22:38:13.792830+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - HELP F330CARTE
type: support-article
updated_at: '2026-01-06T12:35:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025315652-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-HELP-F330CARTE
---

**Dúvida**  
Ao realizar a compensação é apresentado HELP **F330CARTE** - Este título foi negociado com agente financeiro. Apenas títulos em carteira (Situação=0) podem ser compensados.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
  
1**º Cenário**

Caso o parâmetro da rotina "**FINA330 - Compensação Contas a Receber**" esteja com o conteúdo "**Comp. Transferidos ?   = NÃO**" e o título exemplo do tipo: NF  esteja na situação de carteira "**2 - Descontada**" que significa (que o título foi vendido para o banco, para a empresa obter o valor antecipado) irá apresentar o HELP

"**F330CARTE** - Problema: Este título foi negociado com agente financeiro. Apenas titulos em carteira (Situação = 0) podem ser compensados"

**Solução para o 1º Cenário**

Terá que alterar o conteúdo do parâmetro para "**Comp. Transferidos ?  = SIM**" ou efetuar o estorno do título que esteja na situação de carteira **2 descontada**, transferindo para a situação "**0 - Carteira**" com isso o valor recebido pela empresa também será estornado.

**2º Cenário**

Na rotina "**FINA022 - Situação de Cobrança**" (tabela **FRV**) é necessário que tenha as situações de carteira padrões cadastradas que são:

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/37471203136791)](https://centraldeatendimento.totvs.com/hc/article_attachments/37471203136791)

Código | Descrição  
0      | CARTEIRA  
1      | SIMPLES  
2      | DESCONTADA  
3      | CAUCIONADA  
4      | VINCULADA  
5      | COM ADVOGADO  
6      | JUDICIAL  
7      | CAUÇÃO DESCONTADA  
F      | CARTEIRA PROTESTO  
G      | CARTEIRA ACORDO  
H      | CARTÓRIO  
I      | CARTEIRA CAIXA LOJA  
J      | CARTEIRA CAIXA GERAL  
K      | PIX

Segue as propriedades de configuração do código "0 - Carteira"

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/37471179330967)](https://centraldeatendimento.totvs.com/hc/article_attachments/37471179330967)

Código = 0

Descrição = CARTEIRA

Usa Banco = 2 - Não

Descontada = 2 - Não

Protesto = 2 - Não

Perc. Desc. = 0,00

Natureza = (em branco)

Bloqueio Mov = 2 - Não

Situação PDD = (em branco)

Situação PIX = (em branco)

Caso a situação "**0 - Carteira**" seja deletada na rotina "**FINA022 - Situação de Cobrança**", ao tentar compensar pela rotina "**FINA330 - Compensação Contas a Receber**" uma NF que esteja na situação **"0 - Carteira"** com um título do tipo NCC que esteja na mesma situação 0, irá apresentar a mensagem

"**HELP F330CARTE** - Problema: Este título foi negociado com agente financeiro. Apenas titulos em carteira (Situação = 0) podem ser compensados"

ou outro help como:

"Help: **F330BLOQD**  - Problema: Não é possível realizar a operação pois o título se encontra em situação de cobrança que não permite manutenção ou movimento financeiro do titulo."

Ou outros erros não previsto no sistema, já que o protheus espera que a situação **"0 - Carteira"** deve existir no sistema.
