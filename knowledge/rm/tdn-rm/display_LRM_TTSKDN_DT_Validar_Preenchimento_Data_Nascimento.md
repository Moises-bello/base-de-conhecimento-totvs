---
content_hash: 19519a77182c3cde8dbf857ea7fb6031d33c4c4f7c0b03cca33eadf5e1393d6e
fetched_at: '2026-06-29T00:06:19.508644+00:00'
page_id: '219698486'
product: rm
source: tdn-rm
title: TTSKDN_DT_Validar_Preenchimento_Data_Nascimento
type: documentation
url: https://tdn.totvs.com/display/LRM/TTSKDN_DT_Validar_Preenchimento_Data_Nascimento
version: 1
---

# DIRF/Informe de Rendimentos

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *DIRF/Informe de Rendimentos* |
| **Situação/Requisito:** | Ao gerar a DIRF quando existe um dependente cadastrado com a data de nascimento em branco o sistema realiza a geração da DIRF sem mostrar nenhum erro ou aviso e preenche a data de nascimento como 00010101 porém ao importar o arquivo no validador é apresentado um erro informando que a data de nascimento está incorreta. |
| **Solução/Implementação:** | *Sistema passa a registrar no log o dependente que não tem a data de nascimento informada.* |
| **Chamados relacionados:** | *TTSKDN* |
| **Versões/Release:** | *11.82.43* |

divs
