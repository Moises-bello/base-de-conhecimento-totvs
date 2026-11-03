---
content_hash: 9a8914faa8bf25c509bf1e8c98a0345a94fbbbed3bb7165db5c8f975f1dd9f7a
fetched_at: '2026-06-29T00:08:44.525399+00:00'
page_id: '309036738'
product: rm
source: tdn-rm
title: Artigo 71 Paragrafo 4º - Intevalo Intrajornada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=309036738
version: 3
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | RM Chronus / RM Labore |
| **Versões:** | 12.1.17 |
| **Ocorrência:** | **Artigo 71**  Artigo 71 § 4º A não concessão ou a concessão parcial do intervalo intrajornada mínimo, para repouso e alimentação, a empregados urbanos e rurais, implica o pagamento, de natureza indenizatória, apenas do período suprimido, com acréscimo de 50% (cinquenta por cento) sobre o valor da remuneração da hora normal de trabalho. |
| **Ambiente:** | Concessão ou Concessão parcial do intervalo intrajornada |
| **Passo a passo:** | Para atender o artigo 71 paragrafo 4º, foi realizado as seguintes parametrizações no sistema:   * Acessar Cadastros>Funcionários>Horário por Intervalo>Novo>Cadastrar um horário rígido de 08:00 às 17:00 com uma hora de intervalo planejado.          * Acessar cadastro funcionário>Anexos>Horário Planejado>Histórico de Horário>Associar o horário em questão para o funcionário.        * Funcionário não realizou intervalo de ausência (refeição) e em alguns dias, realizou trabalho inferior ao intervalo cadastrado, conforme importação de batidas.        * Pelo fato de que o comportamento padrão do horário rígido é não calcular extras quando as batidas do intervalo de ausência planejada não forem efetuadas, não serão por padrão geradas as extras.        * Portanto, caso nesses dias o intervalo tenha que ser considerado como trabalhado e serem geradas extras, basta acessar: Espelho>anexo>“Ignorar ausência planejada”> incluir um registro para esses dias.          * Após a alteração no espelho do funcionário, deverá  recalcular o espelho do funcionário, onde serão geradas extras referentes aos intervalos.       **Sem Integração Chronus e Vitae:**     * Acessar Administração de Pessoal>Eventos>Foi inserido o evento 9007>Provento>Tipo Hora>Percentual Incidência 1,5%      * Caso o evento seja uma verba indenizatória, verificar as incidências quanto ao INSS/FGTS/IRRF. Caso o evento seja considerado como horas extras, terá todas as incidências INSS/FGTS/IRRF, marcadas.        * Acessar o envelope do funcionário e inserir a verba 9007 com o total de horas extras interjornada. |
| **Observações:** |  |
