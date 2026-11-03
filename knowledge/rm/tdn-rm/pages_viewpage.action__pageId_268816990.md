---
content_hash: eb683439cb48a4a33a3bd058dfb1e14d20811f4b16db049b1e6dc116c069218d
fetched_at: '2026-06-29T00:08:21.376771+00:00'
page_id: '268816990'
product: rm
source: tdn-rm
title: TVZCGK_DT_Erro_Limites_Valores_Validação_Base_Dados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268816990
version: 113
---

# VERIFICA BASE DE DADOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Verificar Base de Dados* |
| **Situação/Requisito:** | *Marcando a flag "Usa Salário Composto", o Sistema automaticamente inibe o preenchimento do Salário e da Jornada, deixando os campos salário e jornada com o valor zerado:* *Ao gerar a Rotina de Validação de Base de Dados é listado erro de Jornada e salário fora dos limites.* *Nesse caso não é um erro, pois é seguido o próprio procedimento do sistema, aonde posteriormente poderá ser informado o Salário Composto Manualmente ou Utilizado a Rotina de Integração Educacional.* |
| **Solução/Implementação:** | *Quando a flag "Usa Salário Composto" estiver marcada a validação de Base de Dados ignorará o erro de limites de valores para os campos JORNADA e SALÁRIO* |
| **Chamados relacionados:** | *TVZCGK* |

divs
