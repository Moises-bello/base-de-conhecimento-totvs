---
content_hash: 19dce253c8b3a77ffa61c2b5b9806e323b38dec560c4d69da12ee27ab150dccc
fetched_at: '2026-06-29T00:06:27.346255+00:00'
page_id: '232820078'
product: rm
source: tdn-rm
title: TUGRNW_DT_Guia_Inss
type: documentation
url: https://tdn.totvs.com/display/LRM/TUGRNW_DT_Guia_Inss
version: 119
---

# GUIA DE INSS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Guia de inss* |
| **Situação/Requisito:** | Ao gerar a guia de INSS considerando a importação de autônomos através de layout, as informações contidas no arquivo não são consideradas.  No processo de geração da Guia de INSS, marcamos a opção de Importar arquivo de autônomos, ele gera a Guia de INSS e desconsidera o arquivo, porque não dá nenhuma mensagem de aviso ou erro com relação ao layout do arquivo. Ele ignora o arquivo de autônomos que estamos incluindo. |
| **Solução/Implementação:** | Otimizada geração da guia de inss, incluída mensagem de validação ao ler arquivo de autônomos com layout incorreto. O arquivo de importação de autônomos precisa ter 9 colunas, independente se há valor nessas colunas ou não. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUGRNW TUJF84 |
| **Requisito (ISSUE):** |  |

divs
