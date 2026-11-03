---
content_hash: 73a3db13323ca160e2919a3b3f2b848e68de83df46f33c08051a06726f4d64ee
fetched_at: '2026-06-29T00:08:07.000140+00:00'
page_id: '236600428'
product: rm
source: tdn-rm
title: TUTHZ8_DT_Controle_Compensacao_Guia_INSS
type: documentation
url: https://tdn.totvs.com/display/LRM/TUTHZ8_DT_Controle_Compensacao_Guia_INSS
version: 2
---

# PARÂMETROS PARA CONTROLE DE COMPENSAÇÃO DA GUIA DE INSS ESTÁ CONFUSO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Guia de INSS* |
| **Situação/Requisito:** | *O controle de compensação da Guia de INSS está muito confuso para o entendimento do usuário.*  *Quando é desmarcado o parâmetro "Movimento por Tomador", no lookup do código de recolhimento aparece as opções 150 e 155, dando a entender que a Guia será gerada por tomador.*  *Estes códigos não podem constar no lookup, já que são utilizados somente com a opção de "Movimento por Tomador" marcada.* |
| **Solução/Implementação:** | *Melhorar a disposição dos parâmetros de controle de compensação na tela da Guia de INSS.*  *Os códigos 150 e 155 não serão mais exibidos no lookup do código de recolhimento.* |
| **Chamados   relacionados:** | *TUTHZ8, TUWEVV* |
| **Versões/Release:** | *11.82.44, 12.1.12* |
