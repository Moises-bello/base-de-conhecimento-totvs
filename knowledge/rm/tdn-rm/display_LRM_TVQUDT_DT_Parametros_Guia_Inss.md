---
content_hash: 523e73db2c6f001601b5817d98ae73bdcfc9a9556116980d6ad424e150a31d03
fetched_at: '2026-06-29T00:08:16.936510+00:00'
page_id: '248583701'
product: rm
source: tdn-rm
title: TVQUDT_DT_Parametros_Guia_Inss
type: documentation
url: https://tdn.totvs.com/display/LRM/TVQUDT_DT_Parametros_Guia_Inss
version: 104
---

# PARAMETROS GUIA DE INSS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Parâmetros Guia de INSS* |
| **Situação/Requisito:** | Quando é salvo um perfil no processo da Guia de INSS e é informado um mês/ano da competência de um período diferente da base, ao acessar a tela do processo o sistema carrega as informações da competência de acordo com o perfil que foi salvo não as da base de dados.  As demais rotinas como SEFIP isso não acontece. |
| **Solução/Implementação:** | O sistema foi Ajustado para que no momento de iniciar a tela de processo da Guia de INSS o mesmo preencha as informações da competência buscando as informações da base de dados utilizada e não do perfil que foi salvo. |
| **Chamados relacionados:** | TVQUDT |

divs
