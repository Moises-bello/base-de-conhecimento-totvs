---
content_hash: a8b57e067b6058a998865687a5689d3330f58850573150e4f8957f82e15faf82
fetched_at: '2026-06-29T00:09:47.652136+00:00'
page_id: '435105036'
product: rm
source: tdn-rm
title: Relatório - Relatório de Vendas Canceladas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105036
version: 1
---

**Relatório - Relatório de Vendas Canceladas**

---

**Dados retornados:**  
   
Dados do Empreendimento: Tais informações serão lidas da tabela Empreendimento, para os Empreendimentos selecionados no filtro do processo. Serão lidas as colunas:

* Área Construída
* Área do Terreno
* Área Total
* Área de Venda
* Coligada
* Código do Empreendimento
* Nome do Empreendimento
* Nome Fantasia do Empreendimento
* CNPJ do Empreendimento
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
* Nome do Bairro do Empreendimento
* CEP do Empreendimento
* Cidade do Empreendimento
* Estado do Empreendimento
* Dados das vendas: Tais informações serão lidas das tabelas:
* Situação da venda: Recupera os dados desta tabela apenas para as vendas canceladas. os códigos são :
  + 30-Cancelada
  + 60-Cancelada
  + 61-Distrato Bilateral
  + 62-Distrato Unilateral
  + 63-Outros
  + 64-Inadimplência
  + 70-Desistência Cliente)
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

**Parcela Componente:** Desta tabela, serão selecionados os valores que irão compor as demais colunas do relatório. Para isto, será feito o relacionamento com a tabela Componente, que define o tipo do componente e assim teremos:

* **Valor de Venda:** Será o somatório das parcelas que sejam de  componentes de tipos "1-Entrada" e "2-Principal". Este campo ficará disponível para customização e não estará visivel no relatório padrão.
* **Valor de Venda Atualizado:** Será o somatório das parcelas que sejam de  componentes de todos os tipos, desconsiderando os componentes que sejam de tipo "a pagar".
* **Total Pago:** Será o somatório dos valores pagos de  componentes de todos os tipos, desconsiderando os componentes que sejam de tipo "a pagar".
* **Valor Devolução:** Será o somatório das parcelas de componentes que sejam de tipo "a pagar".

**Distrato:** Irá buscar os dados dos distratos dos Empreendimentos selecionados no filtro:

* **Valor Devolução:** Será o valor do campo Valor total do Distrato. Situações diferentes, em que o valor de devolução será preenchido, como item de "Condições do Plano", deverão ser customizados utilizando consulta SQL.
* **Data Cancelamento:** Será o valor do campo Data Base do Distrato.

   
   
Voltar
