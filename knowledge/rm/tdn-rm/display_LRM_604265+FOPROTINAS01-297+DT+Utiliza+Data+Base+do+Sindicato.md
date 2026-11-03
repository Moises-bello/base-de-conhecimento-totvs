---
content_hash: 7a779d3b3211acbc69eedf05644babcd0de2ffbc1225a083795b4ccbfea6774b
fetched_at: '2026-06-29T00:08:40.895554+00:00'
page_id: '286516805'
product: rm
source: tdn-rm
title: 604265 FOPROTINAS01-297 DT Utiliza Data Base do Sindicato
type: documentation
url: https://tdn.totvs.com/display/LRM/604265+FOPROTINAS01-297+DT+Utiliza+Data+Base+do+Sindicato
version: 102
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Homolognet |
| **Situação/Requisito:** | O RM Está levando no campo DTBaseCategoriaProfissional do Homolognet o mês e dia no campo Data Base do funcionário indevidamente. No Layout do homolognet é solicitado a “Data base da categoria profissional”, entende-se como a data destinada a correção salarial e a discussão e revisão das condições de trabalho fixadas em acordo, convenção ou dissídio coletivo. |
| **Solução/Implementação:** | Foi criado a check box ''Utiliza Data Base do Sindicato'' na geração do Homolognet a qual quando marcado será levado o campo "Data base da correção salarial" do cadastro do sindicato. Caso não marcado o processo continua o mesmo, será pego a data base do cadastro de funcionário e caso marcado e no sindicato não possuir data informada continuará a data base da tela do funcionário.  Acesse Folha de Pagamento | Rescisão | HomologNet   * Verifique o check box criado ''Utiliza Data Base do Sindicato''        * O check acima marcado pegará a data informada no campo "Data base da correção salarial" |
| **Tickets relacionados:** | 604265 |
| **Requisito:** | Homolognet |

divs
