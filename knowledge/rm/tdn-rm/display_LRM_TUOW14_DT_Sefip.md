---
content_hash: 165e22e001341a4aa772c70614ced179c5e49e0768545404229af7285fbac0ee
fetched_at: '2026-06-29T00:08:04.046054+00:00'
page_id: '235334091'
product: rm
source: tdn-rm
title: TUOW14_DT_Sefip
type: documentation
url: https://tdn.totvs.com/display/LRM/TUOW14_DT_Sefip
version: 116
---

# SEFIP

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *SEFIP* |
| **Situação/Requisito:** | Envelope de pagamento original  Valor do evento de CC324 = 496,08  Sefip gerada com o valor do evento de CC324 no campo de Dedução de 13º salário maternidade, corretamente.  Envelope de pagamento da rescisão complementar, evento de CC325 no valor 170,58.  Valor do evento de cc325 não é levado para o campo de dedução |
| **Solução/Implementação:** | Otimizado SEFIP, ajuste na regra de cálculo do campo de dedução de 13 salário maternidade, fazendo com que o valor seja calculado quando a geração do SEFIP é posterior ou igual à data de rescisão do funcionário |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUOW14 |
| **Requisito (ISSUE):** | *Informe o requisito relacionado.* |

divs
