---
content_hash: 813f8f30428399b70c919b9affde05dd96fca41464f1ca4a1a327b81df56599c
fetched_at: '2026-06-29T00:08:20.064451+00:00'
page_id: '267812011'
product: rm
source: tdn-rm
title: TVRWRJ_DT_Funcionario_Nao_Processado_Encargos
type: documentation
url: https://tdn.totvs.com/display/LRM/TVRWRJ_DT_Funcionario_Nao_Processado_Encargos
version: 111
---

# GERAÇÃO DE ENCARGOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos.* |
| **Módulo:** | *Folha de Pagamento.* |
| **Função:** | *Geração de encargos.* |
| **Situação/Requisito:** | Ao realizar a geração de encargo para um funcionário que não atendia as condições definidas na formula de seleção informada no encargo, o sistema mostrava no log de execução o funcionário, porém não dava nenhuma informação para indicar que o funcionário não teve nenhum encargo processado, não era possível descobrir por qual motivo o histórico de encargo não havia sido preenchido. |
| **Solução/Implementação:** | Foi Ajustado o sistema para que quando houver um funcionário que não for processado nenhum encargo para o mesmo, que o sistema emita uma mensagem informando que nenhum encargo foi processado para o funcionário. |
| **Chamados relacionados:** | TVRWRJ |

divs
