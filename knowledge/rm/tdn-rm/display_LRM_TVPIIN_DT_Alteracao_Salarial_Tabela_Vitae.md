---
content_hash: 5400c10588fd1a58a6d8490fabebff956ed7a443cb93b7659f805f9b775a719e
fetched_at: '2026-06-29T00:08:18.627215+00:00'
page_id: '266963191'
product: rm
source: tdn-rm
title: TVPIIN_DT_Alteracao_Salarial_Tabela_Vitae
type: documentation
url: https://tdn.totvs.com/display/LRM/TVPIIN_DT_Alteracao_Salarial_Tabela_Vitae
version: 112
---

# ALTERAÇÃO SALARIAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Alteração salarial* |
| **Situação/Requisito:** | Ao realizar o processo de alteração salarial utilizando tabela salarial do RMVitae, e o percentual deste aumento ultrapassava seis zeros depois da virgula, o sistema truncava e não encontrava nenhum percentual.  Exemplo: Percentual :0.000000954141115525684   Percentual truncado :0.000000  Desta forma o sistema não encontrava nenhum aumento e não realizava o ajuste. |
| **Solução/Implementação:** | Foi ajustado o sistema para poder utilizar o percentual que for calculado com todas as casas decimais para que o valor não seja mais truncado e o percentual seja encontrado corretamente. |
| **Chamados relacionados:** | TVPIIN |

divs
