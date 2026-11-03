---
content_hash: dd761c4915a85d379e408fb8c43eaf9cd2269df90fb1b8585b15550e3e8cf0c9
fetched_at: '2026-06-29T00:09:47.602322+00:00'
page_id: '435105024'
product: rm
source: tdn-rm
title: Relatório - Pagamentos Efetivos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105024
version: 2
---

**Relatório - Pagamentos Efetivos**

---

Este relatório é responsável por retornar todas as parcelas de um plano de financiamento que tiveram a baixa integral do lançamento financeiro efetuado. Este relatório não retorna parcelas que tiveram a baixa do lançamento financeiro  parcialmente efetuada  
 **Pré-Condições:**  
 1- Ter efetuado baixa total em algum lançamento financeiro. 2- Ter efetuado baixa parcial em algum lançamento financeiro.  
 **Dados Recuperados**  
 Dados do Empreendimento: Tais informações serão lidas da tabela XEMPREENDIMENTO, para os empreendimentos selecionados no filtro do processo. Serão lidas as colunas:

* Área Construída
* Área do Terreno
* Área Total
* Área de Venda
* Coligada
* Código do Empreendimento
* Nome do empreendimento
* Nome Fantasia do empreendimento
* CNPJ do empreendimento
* Centro de Custo
* Departamento
* Filial
* Custo m2
* Data do Lançamento
* Data de Fundação
* Data de Entrega
* Data do habite-se
* Imagem
* Inscrição Estadual
* Inscrição Municipal
* Nome responsável
* Observações
* Quantidade de Subunidades
* Quantidade de Unidades
* Telefone
* Tipo de endereço
* Logradouro
* Número do endereço
* Complemento do endereço
* Nome do Bairro do empreendimento
* CEP do empreendimento
* Cidade do empreendimento
* Estado do empreendimento

**Dados das vendas:**

* Modalidade de Venda
* Empreendimento
* Situação da Venda
* Coligada
* Fiador
* Data Inclusão da Venda
* Data Cancelamento
* Data de vencimento da 1ª parcela
* Data da Quitação
* Data da Venda
* Data Base
* Data de assinatura na venda
* Data de entrega da chave
* Data de previsão de entrega na venda
* Data da Geração de Boleto
* Data do Reajuste da Venda
* Número do Contrato
* Número da Venda
* Saldo Devedor de CM da Venda
* Saldo Devedor Juros da Venda
* Saldo Devedor Outros da Venda
* Saldo Devedor Principal da Venda
* Valor da Venda
* Valor Desconto Quitação
* Valor da Entrada
* Valor Total Financiado
* Total Baixado da Venda
* Total de Desconto da Venda
* Multa rescisória do distrato

Com esta tabela, será feito o relacionamento com as tabelas comprador e cliente/fornecedor para buscar quem é o comprador principal da venda e seus dados, além da item de venda, onde será lida qual a subunidade compõe a venda; Também haverá o relacionamento com a tabela modalidade da venda.  
 **• Dados das parcelas:** Tais informações serão lidas da tabela Parcela pagamento, buscando dados de parcelas quitadas:

* Tipo: Será proveniente da coluna descrição do tipo de parcela da tabela tipo de Parcela. Esta tabela será relacionada com a tabela Parcela do Pagamento.
* Grupo: Será proveniente da coluna código do grupo da tabela Parcela do Pagamento.
* Parcela: Será proveniente da coluna número da parcela da tabela Parcela do Pagamento.
* Vencimento: Será proveniente da coluna data de vencimento da tabela Parcela do Pagamento.
* Pagamento: Será proveniente da coluna data de liquidação da parcela da tabela Parcela do Pagamento.
* Dias Atraso: Será Calculado, caso a data de pagamento seja maior que o vencimento, subtraindo estes campos.
* Valor original: Será proveniente da coluna valor original da tabela Parcela do Pagamento.
* Juros: Será o somatório dos componentes do tipo 3 da coluna valor do componente da tabela parcela componente.
* Correção Monetária: Será o somatório dos componentes do tipo 4 da coluna valor do componente da tabela parcela
* componente.
* Valor Parcela: Será proveniente da coluna valor da parcela da tabela Parcela do Pagamento.
* Valor Pago: Será proveniente do somatório da coluna valor da baixa da tabela parcela componente.

Voltar
