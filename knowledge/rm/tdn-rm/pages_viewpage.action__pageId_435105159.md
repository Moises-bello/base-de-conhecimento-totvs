---
content_hash: 0150cc16774fa3618bfac26d2f49f1d764c144956a816184ce87826f8c0c6c85
fetched_at: '2026-06-29T00:09:48.453709+00:00'
page_id: '435105159'
product: rm
source: tdn-rm
title: Relatório - Ficha Financeira Sintética (FF002)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105159
version: 11
---

O objetivo deste relatório é exibir informações das vendas para possibilitar análise dos financiamentos e também uma ferramenta para gerar os dados para que possam ser passados para os clientes.  Além disso, este relatório deverá ser utilizado no lugar do relatório de Regras de Venda, por conter as mesmas informações e ser mais amplo e completo.

**Observação:** O Relatório pode ser executado para um empreendimento, para um cliente ou para um conjunto de vendas. Para acessar a partir das vendas, basta ir em Processos -> Relatórios -> Ficha Financeira.

Ao abrir a tela aparecerá os seguintes campos:

* **Relatório:** Escolha o layout do relatório que será gerado.
* **Data base**: Escolha a data base do relatório. As parcelas serão calculadas e reajustadas para esta data.
* **Imprimir resíduo**: Caso marcado o relatório irá trazer o valor de resíduo calculado da venda, se existir.
* **Considerar Multa e Juros**: Com este parâmetro marcado, o relatório irá trazer calculado o valor de multa de atraso e Juros de mora.
* **Considerar Deságio**: Para as vendas com modalidade PRICE, será possível escolher se o deságio será calculado para a quitação da venda. Lembrando que o valor gerado é somente válido para a data base selecionada.
* **Posição atual da base**: Com este parâmetro habilitado, a ficha financeira apresenta os valores atuais que estão na base e portanto não utiliza a data base. Quando o ambiente NÃO estiver configurado com o reajuste online, então este parâmetro estará obrigatoriamente habilitado.

**Observação:** Para o parâmetro "Considerar deságio" apareça, é necessário ativar os parâmetros de deságio do TIN e Financeiro, ou seja, no Gestão financeira deve-se habilitar o reajuste online e no TIN selecionar a forma de cálculo do deságio.

Serão recuperados no relatório dados das tabelas de:  
   
**Dados do Empreendimento**

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
* Data do habitese
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

**Dados das vendas**

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
* Multa rescisória do distrato (VRMULTA)

**Resumo do Plano**

* Grupo
* Tipo da Parcela
* Quantidade de Parcelas
* Valor Unitário
* Valor Original
* Moeda
* 1º vencimento
* Ultimo Vencimento
* Próximo Reajuste
* Datebase
* Juros
* Tipo de Juros
* Quantidade de Parcelas em Atraso
* Valor das Parcelas em Atraso
* Quantidade de Parcelas Pagas
* Valor das Parcelas Pagas
* Quantidade de Parcelas a vencer
* Valor das Parcelas a vencer

**Detalhes do Plano / Parcelas**

* Tipo
* Situação
* Grupo
* Parcela
* Vencimento
* Valor Original
* Valor Principal
* Juros
* Correção Monetária
* Outros valores
* Encargos
* Desconto do Plano
* Valor Parcela Atualizado
* Juros de Mora
* Multa de Atraso
* Valor Total
* Data Pagamento
* Pagamentos
* Valor Principal
* Juros de Mora
* Multa de Atraso
* Desconto Financeiro
* Valor pago
