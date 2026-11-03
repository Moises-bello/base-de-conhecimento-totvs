---
content_hash: 59bd10993c4d8994f009d1cdb3764f05ea95560adfb9cd95d6a34879b979adf3
fetched_at: '2026-06-29T00:08:52.378837+00:00'
page_id: '339510331'
product: rm
source: tdn-rm
title: 1854304 FISCAL01-2842 DT EFD Contribuições Parâmetro "Gerar operações sem direito
  a crédito (PIS/COFINS)"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=339510331
version: 2
---

# EFD Contribuições

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Geração de Arquivo - EFD Contribuições |
| **Situação/Requisito:** | Orientações da RFB sobre a escrituração de documentos na EFD Contribuições:    (11) "No tocante às aquisições do período, só precisam ser escriturados os documentos referentes a operações geradoras de crédito  (CST 50 a 56, no caso de créditos básicos; e CST 60 a 66, no caso de créditos presumidos)."    (12) "No tocante às notas fiscais de saída, só precisam ser relacionados os documentos fiscais referentes a receitas. Os documentos fiscais representativos de transferência de mercadorias e produtos entre estabelecimentos da pessoa jurídica, bem como outras operações que não se caracterizam transações comerciais (geradores de receitas) não precisam ser escrituradas."    (46) Qual CST utilizar nas operações de remessa e transferências de mercadorias? "Como não trata-se de uma operação geradora de receita e tampouco de créditos, utilize nas saídas o CST 49 (outras operações de saída) e nas entradas o CST 98 (outras operações de entrada). Documentos com estas operações não precisam ser informados na EFD CONTRIBUIÇÕES".    Fonte: Perguntas e Respostas EFD Contribuições, páginas 10, 11 e 25.    Para atender ao disposto acima, faremos as seguintes implementações no sistema:   * Na tela de geração da EFD Contribuições altera o nome do parâmetro "Gerar no Registro C100 notas de entrada sem direito a crédito (PIS/COFINS)" para "*Gerar operações sem direito a crédito (PIS/COFINS)*". * Na geração da rotina a seleção dos dados deve aplicar o parâmetro (SIM ou NÃO) para *todos* os Registros. * Serão desconsiderados na seleção os lançamentos fiscais que possuírem os CSTs: 49, 70, 71, 72, 74, 75, 98 e 99.     OBSERVAÇÕES IMPORTANTES:   * O CST 08 não entrou na lista porque existem receitas sem incidência da Contribuição Social (Tabela 4.3.15) e, conforme a própria orientação transcrita acima, TODAS as operações geradoras de receita devem ser escrituradas. Logo, não poderemos filtrar as saídas pelo CST 08. Para que estas operações não sejam listadas no arquivo os tributos PIS e COFINS não devem ser informados no item/lançamento fiscal.  * Neste caso, para clientes que integração pela Gestão de Materiais, os tributos em questão não devem ser informados no movimento ou serem informados com a Base de Cálculo zerada. Dessa forma, não serão escriturados. * As orientações acima não impactam NF-e uma vez que, quando não há os tributos no movimentos no sistema automaticamente inclui esses tributos na NF-e como não tributado (CST08). |
| **Solução/Implementação:** | Ajuste na EFD Contribuições   * Na tela de geração da EFD Contribuições foi alterado o nome do parâmetro "Gerar no Registro C100 notas de entrada sem direito a crédito (PIS/COFINS)" para "Gerar operações sem direito a crédito (PIS/COFINS)".  * Quando o parâmetro "Gerar operações sem direito a crédito (PIS/COFINS)" estiver como "Sim" serão considerados na seleção os lançamentos fiscais que possuírem os CSTs: 49, 70, 71, 72, 74, 75, 98 e 99.   Registros Contemplados com o parâmetros "Gerar operações sem direito a crédito (PIS/COFINS)".    **Bloco A**: A010, A100  **Bloco C**: C010, C100, C380, C395, C400, C500, C600, C860  **Bloco D**: D010, D100, D200, D300, D300, D350, D500, D600  **Bloco F**: F550  **Bloco 1**: 1900A "Gerado Baseado nos Itens do Lançamento Fiscal"    Observação:   * Os filhos dos registros quando houver também serão afetados pelo parâmetro. * Para os registros do Bloco F e 1 menos os registros F550 e 1900A o parâmetro "Gerar operações sem direito a crédito (PIS/COFINS)" não será aplicado, também não será aplicado nos registros do Bloco I,M e P. |
| **Conversores e Parâmetros:** | Não se Aplica |
| **Tickets relacionados:** | Não se Aplica |
| **Requisito:** | FIS000385 |
| **Documento de Referência:** | <http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.EfdPisCofins.aspx> |
