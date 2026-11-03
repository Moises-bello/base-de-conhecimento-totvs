---
article_id: 360017801111
category: Faturamento - Cadastros
content_hash: 451bf594628741d1b2c8fa0f1ee66d32c782a8a80689fa12fa230de915e27a95
fetched_at: '2026-06-28T22:38:35.400231+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - BackOffice Protheus - SIGAFAT -  Clientes Estrangeiros e
  Pedido de Venda de Exportação
type: support-article
updated_at: '2025-10-14T20:31:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017801111-Cross-Segmentos-BackOffice-Protheus-SIGAFAT-Clientes-Estrangeiros-e-Pedido-de-Venda-de-Exporta%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31493969563799) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**

Qual a tratativa correta para cadastrar cliente estrangeiro e emitir Nota Fiscal de Exportação no faturamento?

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - todas as versões  
  
**Solução**

Para incluir clientes de origem estrangeira, os seguintes campos no cadastro devem ser preenchidos conforme abaixo:

* Estado (A1\_EST): 'EX'
* CEP (A1\_CEP): '00000000'
* Tipo (A1\_TIPO): 'X - Exportação', é importante para a **geração das Notas Fiscais de Exportação**
* Código do País (A1\_PAIS): Deve ser diferente de branco e '01058' (Brasil).
* Bairro (A1\_BAIRRO): Pode permanecer em branco; caso o campo seja obrigatório, preencher com um valor genérico.
* Município (A1\_MUN): 'ESTRANGEIRO' É possível cadastrar o código de município 999999 diretamente na tabela de municípios do IBGE (CC2) caso necessário.
* RG/Ced.Estr (A1\_PFISICA) Este campo permite que na inclusão de clientes que não possuem CPF/CNPJ (Exemplo: cliente estrangeiro), seja gerado o código do cliente.
* Código do Município (A1\_COD\_MUN): Deixar em branco \*
* Inscrição Estadual (A1\_INSCR): Deixar em branco \*
* CNPJ (A1\_CGC): Deixar em branco (cliente estrangeiro não possui CNPJ) \*

**\*Observação 1:** Por padrão, esse campos não são de preenchimento obrigatório. Caso tenha alterado as definições, avaliar o impacto ao seu negócio de retirar a obrigatoriedade de preenchimento visto que a recomendação é deixá-los em branco.

Caso a obrigatoriedade seja julgada imprescindível, retirar em modo exclusivo, cadastrar o Cliente em questão e voltar a obrigatoriedade após salvar (Neste caso, qualquer alteração nesse cadastro que se faça necessária não poderá ser confirmada sem preenchimento do campo).

Caso a obrigatoriedade seja julgada desnecessária, basta desabilitar a obrigatoriedade:

Acessar o Configurador CFG > Base de Dados > Dicionário > Bases de Dados > Dicionário de Dados; > Localizar e Editar a Tabela em questão > Localizar e Editar o campo em questão > Aba "Uso" > Desabilitar a opção "Obrigatório" > Confirmar e Salvar.

**Pedido de venda de exportação via faturamento:**

* Para uma Nota Fiscal de Exportação, gerar o pedido normal para o cliente EX, isso fará com que o CFOP inicie por 7.
* Apenas a alíquota do ICMS difere das demais, sendo equivalente a 13%.
* Os demais requisitos segue o padrão de faturamento (liberação, liberação de crédito/estoque/faturamento).

**Observação 2:** No Protheus há o módulo SIGAEEC específico para gerenciamento das exportações. Caso não possua o módulo e precise emitir uma Nota de Exportação pelo SIGAFAT o processo de emissão é realizado pelo processo de Faturamento habitual do FAT; ou seja, por meio de Emissão de Pedido de Vendas e Preparação do Documento de Saída.

Não há no SIGAFAT tratamento específico para exportação.

**Saiba mais:**

[FAT0075\_Cadastro de Clientes Estrangeiros (Campo A1\_PAIS) e Emissão de Nota de Exportação no SIGAFAT](https://tdn.totvs.com/x/zCMwDg)

[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Uso Moeda Modulo Faturamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000731448-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Uso-Moeda-Modulo-Faturamento?source=search)
