---
content_hash: 1cf202faf7f6e15ab79378b4135507f54bec490ec665efaa1becb0e1dda95836
fetched_at: '2026-06-29T00:06:20.306302+00:00'
page_id: '221551803'
product: rm
source: tdn-rm
title: RMFIS00002_Geração dos registros - 1100/1500 Controle de Créditos Fiscais Pis\Pasep
  - Cofins
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=221551803
version: 125
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS GESTÃO FISCAL |
| **Versões:** | 12.1.7.x ou superior |
| **Ocorrência:** | Geração dos Registros 1100 / 1500 |
| **Ambiente:** |  |
| **Passo a passo:** | Sobre os registros **1100** - Controle de Créditos Fiscais PIS\PASEP e **1500** - Controle de Créditos Fiscais COFINS:  Estes registros têm por objetivo realizar o controle de saldos de créditos fiscais de períodos anteriores ao da atual escrituração, bem como eventual saldo credor apurado no próprio período da escrituração.  Para mais informações sobre a rotina EFD Contribuições e os registros mencionados acima, acesse o Guia Prático de orientação do leiaute e da escrituração fiscal digital da Contribuição para o PIS /PASEP, da COFINS e da Contribuição Previdenciária Sobre a Receita Bruta (CPRB), disponível no site da Receita Federal.  (<http://www1.receita.fazenda.gov.br/sistemas/efd-contribuicoes/download/download.htm>)    **Geração dos registros 1100 e 1500**  **1 -** Acesse o TOTVS Gestão Fiscal | Obrigações Principais | Apuração Pis\Cofins | Controle de Créditos Fiscais de Tributos.    Os créditos podem ser cadastrados manualmente ou geradas com base nos lançamentos fiscais do período considerado. Para esse fim, foi criado o processo “Geração de Créditos Fiscais de Tributos”.  Os valores serão originados da **soma do valor do tributo dos itens dos lançamentos fiscais de entrada** **das filiais de mesmo CNPJ da filial corrente**, para o mês e ano informados na tela do processo, agrupados pelo Tipo de Crédito.    **1.1** Geração dos créditos pelo processo “Geração de Créditos Fiscais de Tributos”, o sistema irá consistir os lançamentos fiscais que possuam o Pis e Cofins destacado no Item do lançamento e o código do Tipo Credito preenchido.  Tributos Pis e Cofins destacados no Item do lançamento Fiscal:      O código Tipo Crédito será preenchido no Item do lançamento Fiscal | Aba Informações Adicionais | Sub aba Outros Dados:      **1.2** Quanto ao Processo:  Após inserir o lançamento com as informações acima, execute o processo de Geração de Créditos Fiscais de Tributos:    Créditos criados após a execução do processo:      **2.** O sistema também permite que os créditos sejam inseridos manualmente, para isso acesse o TOTVS Gestão Fiscal | Obrigações Principais | Apuração Pis\Cofins | Controle de Créditos Fiscais de Tributos | incluir, preencha as informações solicitadas    Lançamento de crédito criado manualmente      **3.** Arquivo da EFD Contribuições gerado, no mês seguinte aos créditos, com os registros 1100 e 1500.      **OBS:** Lembre-se que para correta geração da rotina é necessário utilizar o layout e sistema atualizados de acordo com a última versão disponível no Portal do Cliente, para acessar o Portal clique [aqui](https://suporte.totvs.com/download). |
| **Observações:** | Compatível com a versão 11.82.41.x ou superior |

divs
