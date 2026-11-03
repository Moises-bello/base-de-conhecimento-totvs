---
content_hash: 5d0862414b28ab0056a363ac1c9aa5a5abc086009cc8f4125e687571ea44132b
fetched_at: '2026-06-29T00:09:24.540604+00:00'
page_id: '423937949'
product: rm
source: tdn-rm
title: Natureza Orçamentária Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937949
version: 7
---

Atualmente já existe no TOTVS Gestão de Estoque, Compras e Faturamento, uma tabela de Natureza do Orçamento.   
Identificamos que essa tabela tem o mesmo conteúdo que a Tabela de Natureza Financeira, portanto, decidimos evoluir a Tabela de Natureza do Orçamento tendo em vista que as duas teriam as mesmas informações tanto no Gestão de Estoque, Compras e Faturamento através do processo de controle orçamentário quanto no TOTVS Gestão Financeira através do processo de Fluxo de Caixa.   
**Natureza**: Referente a visualização da natureza financeira nos lançamentos classificados a pagar, receber ou ambos.  
***Observação***: Naturezas do tipo "ambos" podem ser utilizadas tanto para receita quanto para despesa (caso de mercadoria para revenda). Desta forma no Fluxo de Caixa do financeiro para os lançamentos financeiros com a natureza orçamentária financeira classificada como "ambos", o sistema levará em consideração o tipo do lançamento, a pagar ou receber, para separação dos valores no fluxo de caixa.  
Sintético/Analítico: Analítica é uma natureza orçamentária/financeira inteiramente interligada a uma natureza principal (Sintética), exemplo:

* Natureza 01 (Sintética)
* Natureza 01.01 (Analítica)

Não Permite transferir Valores: Com este parâmetro habilitado o sistema não permite transferir valores de uma natureza a outra. Muito útil no processo de realocação orçamentária no modulo TOTVS Gestão de Estoque, Compras e Faturamento.  
Defaults Contábeis: Campo a ser informado as contas de debito e/ou credito referente a contabilização do movimento.   
**Associação**: A vinculação da natureza orçamentária/Financeira com o produto é através do cadastro de produto – detalhes – classificação.  
***Observações***: Associando a Natureza Orçamentária/Financeira no cadastro de produto e parametrizando o tipo de movimento para editá-la o sistema retorna automaticamente a natureza após inserir o produto no movimento e posteriormente no lançamento financeiro (caso o tipo de movimento esteja parametrizado para gerar lançamento financeiro para o TOTVS Gestão Financeira).  
Ao criar a natureza orçamentária/Financeira (cadastro – tabelas auxiliares – natureza orçamentária/Financeira) o sistema permite a vinculação da natureza analítica ao centro de custo baseado no processo de controle orçamentário (Cadastros – Tabelas de Orçamento – Vinculo da natureza orçamento e Centro de custo).

Parametrização

Acesso a edição da natureza Orçamentária/Financeira no item do movimento é parametrizado em Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | selecione 04.09 - Outras Movimentações.

---
