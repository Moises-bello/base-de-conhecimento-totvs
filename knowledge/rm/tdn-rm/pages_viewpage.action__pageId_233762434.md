---
content_hash: 9a93e9f9172f48e58ad7613b5b4c578ed8550bf8d459aecbc2ada9947c763b42
fetched_at: '2026-06-29T00:06:28.841580+00:00'
page_id: '233762434'
product: rm
source: tdn-rm
title: RMFIS00003_Geração dos registros 1300/1700 Controle de Valores Retidos na Fonte
  Pis\Pasep - Cofins
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=233762434
version: 6
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS GESTÃO FISCAL |
| **Versões:** | 12.1.9x e 11.82.42.x |
| **Ocorrência:** | Geração dos Registros 1300 / 1700 |
| **Ambiente:** |  |
| **Passo a passo:** | Sobre os registros **1300** - Controle de Valores Retidos na Fonte PIS\PASEP e **1700** - Controle de Valores Retidos na Fonte COFINS:   Este registro tem por objetivo realizar o controle dos saldos de valores retidos na fonte, de períodos anteriores e do período da atual escrituração.   Para mais informações sobre a rotina EFD Contribuições e os registros mencionados acima, acesse o Guia Prático de orientação do leiaute e da escrituração fiscal digital da Contribuição para o PIS /PASEP, da COFINS e da Contribuição Previdenciária Sobre a Receita Bruta (CPRB), disponível no site da Receita Federal.   (<http://www1.receita.fazenda.gov.br/sistemas/efd-contribuicoes/download/download.htm>)    **OBS:** Certifique-se sempre que o Layout utilizado é o mais atualizado. Para identificar a data do mesmo, na tela de geração da rotina, o campo Data do Layout, detém a data atualizada do arquivo. Caso tenha dúvidas sobre sua hodiernidade, entre em contato com o Suporte Técnico.   O layout atualizado está disponível no Portal do Cliente (<https://suporte.totvs.com/download>).    **- Geração do registro 1300 / 1700**   **1 -** Acesse o TOTVS Gestão Fiscal | Obrigações Principais | Apuração Pis\Cofins | Controle de Créditos Fiscais de Tributos Retidos.  Os créditos podem ser cadastrados manualmente ou geradas com base nos lançamentos Financeiros do período considerado. Para esse fim, foi criado o processo “Geração de Valores Retidos na Fonte”.  Os valores serão originados da **soma do valor do tributo dos lançamentos financeiros a receber** das filiais de mesmo CNPJ da filial corrente, para o mês e ano informados na tela do processo (o filtro será feito pelo campo Data da Baixa), agrupados pela Natureza da Retenção informada no cadastro do Cliente Fornecedor.  **1.1 -** Geração dos créditos pelo processo “Geração de Valores Retidos na Fonte”:  O sistema irá consistir o campo “Natureza da Retenção na Fonte” preenchido no cadastro do Cliente Fornecedor vinculado ao lançamento financeiro.   Cadastros | Cliente\Fornecedor | Edite o cadastro do Cliente\Fornecedor | Dados Fiscais | Tributos.        Serão selecionados os lançamentos financeiros a receber e baixados que possuam o Pis-RF e Cofins-RF destacado.      **1.2  -** Quanto ao Processo:   Após inserir o lançamento financeiro com as informações acima, execute o processo de Geração de Valores Retidos na Fonte:        Créditos criados após a execução do processo:         **2.** O sistema também permite que os créditos sejam inseridos manualmente, para isso acesse o TOTVS Gestão Fiscal | Obrigações Principais | Apuração Pis\Cofins | Controle de Créditos Fiscais de Tributos Retidos | incluir, preencha as informações solicitadas.       **3 -**  Arquivo da EFD Contribuições gerado com os registros 1300 e 1700. |
| **Observações:** |  |
