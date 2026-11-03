---
content_hash: b9044f6b1fc693cedd60f8bad4a53ec027468177d60108646b12240314a185c1
fetched_at: '2026-06-29T00:09:21.908994+00:00'
page_id: '422545928'
product: rm
source: tdn-rm
title: Operações das Instituições Financeiras, Seguradoras, Previdência Privada e
  Planos de Saúde
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545928
version: 2
---

**Origem dos Dados**

A escrituração do Bloco I só é de natureza obrigatória em relação aos fatos ocorridos a partir de 01 de Janeiro de 2014, conforme disposto na IN RFB Nº 1.387, de 2013. Somente será gerado para os clientes que possuem integração com o produto [TOTVS Gestão Contábil](http://tdn.totvs.com.br/pages/viewpage.action?pageId=198948832), onde serão considerados os valores para a geração do registro do bloco.

**Parametrizações necessárias**

Para a correta geração das informações das Instituições Financeiras, Seguradoras, Previdência Privada e Planos de Saúde, deverão ter cadastradas todas as contas contábeis cadastradas no [Plano de Contas](http://tdn.totvs.com.br/display/LRM/Plano+de+Contas+-+Cadastro) do produto [TOTVS Gestão Contábil](http://tdn.totvs.com.br/pages/viewpage.action?pageId=198948832) e com todas as informações relevantes para sua correta geração do Bloco I.  
 Além dos lançamentos contábeis, deverão ser informados os respectivos dados de acordo com a obrigatoriedade do contribuinte na criação do processo através do produto Gestão Fiscal.   
 Para a criação do processo acesse Opções | Parâmetros | Processos.   
 Selecione o processo EFD PIS/COFINS e clique no botão Grupos e Subgrupos.  
 Selecione Bloco I – na parte esquerda da tela e dê um duplo clique no processo que será apresentada na parte direita da tela para o registro ser aberto para edição.  
 Em seguida acesse a guia Tributos. Nesta guia deverão ser incluídos os tributos PIS e COFINS e as respectivas CST. Além disso deve ser informado o Código da Natureza da Receita para geração dos registros M410 e M810.  
 Na guia Contas deve ser criado um Filtro de Conta Contábil onde deve ser selecionados os seguintes dados:

* Conta Contábil: Selecione as Contas Contábeis do plano de contas cadastro no [TOTVS Gestão Contábil](http://tdn.totvs.com.br/pages/viewpage.action?pageId=198948832).
* Tipo: Faturamento ou Receita Bruta, Deduções e Exclusões de Caráter Geral e Deduções e Exclusões de Caráter Específico
* Tipo de Totalização da Conta: Informe que tipo de totalização que será feita com base Contas Contábeis, ou seja, o que será considerado para totalização e composição dos Campos (Faturamento ou Receita Bruta\Deduções e Exclusões de Caráter Geral\ Deduções e Exclusões).
* Código do Tipo de Detalhamento: Neste campo deve ser informado os códigos válidos de acordo com as Tabelas "7.1.1. - Composição das Receitas" e/ou Tabela "7.1.2 - Composição das Deduções e Exclusões", informação necessária para a geração do registro I200
* Código da Visão Analítica/Referenciada: Neste campo deve ser informado os códigos conforme as Tabelas "7.1.3 - Receitas" e/ou "7.1.4-Deduções e Exclusões", informações necessárias para a geração do registro I300.

Sub Pasta Histórico Padrão/Fechamento: Nesta pasta poderá ser definido os Históricos Padrão que deverão ser desconsiderados no cálculo dos valores, sendo que o Histórico Padrão mais correto a serem utilizados e o do tipo "Fechamento".  
***Observação***: Deve ser selecionada a opção 3-Atividade Financeira no campo Indicador da Atividade Preponderante no processo da geração do arquivo, onde o sistema irá desabilitar os registros dos Blocos A, C, D e F que são específicos para a escrituração das receitas pelas PJ em geral e assim habilitando somente os registros do Bloco I de todas as operações geradoras de receitas tributáveis ou não.

**Arquivo Gerado**

* Neste Bloco temos as seguintes opções de geração:
* Contabilização Centralizada na Filial Matriz.
* Descentralizada que é detalhada por Filial.

Neste primeiro momento o sistema gera somente da forma Descentralizada, onde o arquivo dever ser gerado na filial Matriz detalhando as informações por Filiais.  
 **Observação**: Futuramente vamos disponibilizar a opção "Contabilização Centralizada na Filial Matriz" de forma que seja possível o usuário escolher a forma desejada de geração.
