---
content_hash: ace0426140eb660e84dc274ca7cf84ecb7956cf0e7255f1101b21251bb487175
fetched_at: '2026-06-29T00:08:40.800551+00:00'
page_id: '286506657'
product: rm
source: tdn-rm
title: 1237723 PORTALMOBILE01-1374 DT Contexto de Professor no Portal Corpore.Net
type: documentation
url: https://tdn.totvs.com/display/LRM/1237723+PORTALMOBILE01-1374+DT+Contexto+de+Professor+no+Portal+Corpore.Net
version: 105
---

# Contexto de Professor no Portal Corpore.Net

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Contexto de Professor no Portal Corpore.Net |
| **Situação/Requisito:** | Ao carregar o contexto do professor, que também é um coordenador, o contexto dos professores do curso não eram carregados. |
| **Solução/Implementação:** | Foi realizado uma alteração na verificação de um usuário de funcionário/professor que esteja ativo ou não na filial do professor, e/ou usuários de coordenadores que não eram mais professores.  A verificação de permissão de acesso ao contexto sofreu alteração para atender as seguintes situações abaixo:  Serão retornados os professores do contexto do sistema:   * Pessoa que é professor, possui chapa, está ativo na filial e admitido. * Pessoa que é professor, possui chapa, está ativo na filial e está demitido, mas com prazo para acesso conforme parametrização. * Pessoa que é professor, NÃO possui chapa, e está ativo na filial. * Pessoa que é funcionário, e coordenador de curso. Sendo ou não professor.   Não terão acesso ao contexto do sistema:   * Pessoa que é professor, sem chapa, que não possui permissão na filial do professor. * Pessoa que é professor, com chapa, está demitido, e fora do prazo de acesso conforme parametrização. * Pessoas isoladas (não sendo ao menos funcionários, e não sendo professores) cadastradas como coordenadores, ainda não são tratadas pelo sistema e não terão acesso. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
