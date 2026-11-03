---
content_hash: 6225aa02e2230645ff89236f2241ba26de0b603a3d99f1336ae3e3dbe78dce84
fetched_at: '2026-06-29T00:08:08.478463+00:00'
page_id: '238037669'
product: rm
source: tdn-rm
title: TUXLXS_DT_Antecipacao_Salarial_Dissidio
type: documentation
url: https://tdn.totvs.com/display/LRM/TUXLXS_DT_Antecipacao_Salarial_Dissidio
version: 116
---

# ALTERAÇÃO GLOBAL DE SALÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Alteração Global de Salário* |
| **Situação/Requisito:** | *Foi feito uma Antecipação salarial de dissídio no mês 04 de 7% porém o Dissídio foi referente ao mês 03 de 11%.*  Ao aplicar o aumento do dissídio, o funcionário fica com o Histórico Salarial incorreto no mês 03.  Exemplo:  01/01/2016 – Salário 1000  01/03/2016 – Salário 1037,38 (Dissídio 3,74%) O valor desse Histórico deveria ser 1100 pois ao efetuar a Diferença Salarial, será pago a menor.  01/04/2016 – Salário 1070 (Antecipação 7%)  01/04/2016 – Salário 1100 (Ajuste Dissídio) |
| **Solução/Implementação:** | *Implementado o parâmetro 'Definir competência final para o reajuste de aumentos posteriores' para que seja possível aplicar apenas o aumento complementar em um determinado período.*  *Sobre o parâmetro:*  Deve ser utilizado quando a empresa já realizou antecipação de parte do dissídio em competência diferente da data base.  Exemplo:  Data base da categoria: 01/09/2016 Data da antecipação   : 01/10/2016 - Percentual de antecipação: 7% Data do acordo do Dissídio: 01/11/2016 (retroativo a 01/09/2016) - Percentual do dissídio: 11%  Como fazer o aumento salarial:   Devem ser realizadas 2 execuções da rotina:   1ª - Correção salarial de SET/2016 em 11%        Percentual: 11%       Data de Mudança: 01/09/2016       Competência final para o reajuste: 09/2016   2ª - Correção salarial de OUT/2016 em diante em 3,738317757% (percentual aplicado sobre 7% que completará 11% de aumento)        Percentual: 3,738317757%        Data de Mudança: 01/10/2016      Competência final para o reajuste: (não precisa marcar esse parâmetro uma vez que a correção será até a competência atual) |
| **Chamados relacionados:** | *TUXLXS* |

divs
