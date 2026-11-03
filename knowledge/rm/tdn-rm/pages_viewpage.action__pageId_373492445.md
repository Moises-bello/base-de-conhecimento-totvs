---
content_hash: 878abf4a643524019b416523fdc4abb98f955c3b670e757437598892cc49be0d
fetched_at: '2026-06-29T00:09:01.558166+00:00'
page_id: '373492445'
product: rm
source: tdn-rm
title: 3107600 FOPCALCULO01-3934 - Cadastro de Funcionários - Campo Indicador de Contribuição
  Substituída
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=373492445
version: 1
---

# Funcionários

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Cadastro de Funcionários |
| **Situação/Requisito:** | Ao criar um novo cadastro de funcionário, a data de mudança do campo indicador de contribuição substituída no menu Parâmetros está ficando com uma data preenchida, mas ao retirar a data para salvar o cadastro do funcionário apresenta a mensagem de erro informando que a data é obrigatório. O funcionário não possui a informação de indicador de contribuição substituída, pois essa informação é somente para empresa que possui simples nacional, no qual não seria o caso desse cliente, sendo assim, não deve ser preenchido. |
| **Solução/Implementação:** | No Totvs Folha de Pagamento foi identificado que ao criar um novo funcionário, o campo "Data da mudança" do "Indicador de contribuição substituída" está sendo preenchido automaticamente mesmo o indicador estando vazio e se for feito a tentativa de apagar a data, o cadastro do funcionário não é salvo pois o sistema informa que é obrigatório. Foi feito o ajuste para que o campo não seja preenchido e se torne obrigatório somente quando o indicador for preenchido. |
| **Tickets relacionados:** | 3107600 |
