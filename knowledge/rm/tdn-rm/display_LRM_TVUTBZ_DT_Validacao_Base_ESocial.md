---
content_hash: 6ed87cf93927233d17a49021994036cbd16498610c40d4470371d8303d15a510
fetched_at: '2026-06-29T00:08:18.920277+00:00'
page_id: '266977925'
product: rm
source: tdn-rm
title: TVUTBZ_DT_Validacao_Base_ESocial
type: documentation
url: https://tdn.totvs.com/display/LRM/TVUTBZ_DT_Validacao_Base_ESocial
version: 109
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Validação da base - ESocial* |
| **Situação/Requisito:** | *Ao realizar o processo de validação da base de dados do E-Social, marcando o evento S2100, e existia na base de dados, funcionários com Nome com mais de 100 caracteres, o sistema apresentava um erro não tratado informando que o nome do funcionário havia excedido o tamanho máximo permitido.*  *Isto acontecia, pois havia uma limitação no código para o nome de somente 100 caracteres, porém no banco a limitação do nome era de 120.* |
| **Solução/Implementação:** | *Foi ajustado o sistema para suportar nomes com até 120 caracteres e não mais somente 100, assim o erro deixou de acontecer.* |
| **Chamados relacionados:** | TVUTBZ |

divs
