---
content_hash: 7444d7bde47b924caa3aad3f5b12046b70e9913cd96dce59d8e883e0277466d1
fetched_at: '2026-06-29T00:08:20.709408+00:00'
page_id: '268584979'
product: rm
source: tdn-rm
title: TVZUWC_DT_TRCT_CAMPO_95_115_ACEITAR_MAIS_DE_UMA_RUBRICA
type: documentation
url: https://tdn.totvs.com/display/LRM/TVZUWC_DT_TRCT_CAMPO_95_115_ACEITAR_MAIS_DE_UMA_RUBRICA
version: 111
---

# TRCT

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Tratamento campo 95 e 115 para aceitar mais de uma rubrica* |
| **Situação/Requisito:** | Podemos informar para eventos diferentes a mesma rubrica e na geração do TRCT informamos essa  rubrica para o campo 95. Ao gerar o TRCT o sistema faz uma subdivisão dos eventos criando os campos 95.1, 95.2, 95.3, etc.  Para o homolognet é necessário criar uma rubrica diferente a cada evento e esta rubrica também deve ser criada no site do homolognet. O próprio sistema do homolognet irá criar a mesma subdivisão do campo 95 de acordo com a quantidade de rubricas informadas.  Isto faz com que o cliente tenha que alterar as rubricas do evento dependendo de qual rotina irá utilizar (TRCT x Homolognet.) |
| **Solução/Implementação:** | Para que o cliente não tenha que alterar as rubricas para emissão do TRCT e HomologNet, O sistema passa a permitir que nos campos 95 e 115 possam ser informados mais de uma Rubrica separadas por ';' no TRCT. Uma vez que é obrigatório discriminar cada rubrica para um evento no HomologNet. |
|  |  |
| **Chamados relacionados:** | TVZUWC*.* |
| **Requisito (ISSUE):** |  |

divs

Podemos informar para eventos diferentes a mesma rubrica e na geração do TRCT informamos essa rubrica para o campo 95. Ao gerar o TRCT o sistema faz uma subdivisão dos eventos criando os campos 95.1, 95.2, 95.3, etc.

Para o homolognet é necessário criar uma rubrica diferente a cada evento e esta rubrica também deve ser criada no site do homolognet. O próprio sistema do homolognet irá criar a mesma subdivisão do campo 95 de acordo com a quantidade de rubricas informadas.

Isto faz com que o cliente tenha que alterar as rubricas do evento dependendo de qual rotina irá utilizar (TRCT x Homolognet.)
