---
content_hash: b5f083915e9338a2b26e8be4f686fd2758162b8ec75402ea04dd42a5bf98dd54
fetched_at: '2026-06-29T00:10:14.509061+00:00'
page_id: '461908174'
product: rm
source: tdn-rm
title: 11.0.0 (Estoque, Compras e Faturamento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=461908174
version: 3
---

**Implementado o cálculo da MVA/IVA Ajustada**

A partir dessa versão será possível calcular a Margem de valor Agregado por produto.  
Para isso foi criado o campo “Margem S.T (%)” no Cadastro de Produto | Anexo Dados Fiscais por UF.  
A opção pela utilização ou não da MVA/IVA Ajustada é identificada pelo Cadastro de Naturezas de Operação, aonde foi criado o Flag “Utiliza MVA Ajustada”. Este Flag foi evoluído para que possa ser escolhido entre três opções: “Não Utiliza”, “Utiliza por Natureza” e “Utiliza por Produto”.  
Caso a Natureza de Operação esteja parametrizada para utilizar a MVA Ajustada por Produto, o Módulo TOTVS Gestão de Estoques, Compras e Faturamento irá considerar para o cálculo da MVA/IVA Ajustada, os dados de “Margem S.T. (%)” e a “Alíquota Interna de ICMS” do Anexo de Dados Fiscais por UF do Produto.

**Apresentação de mensagem de sucesso por Saldo Regerado**

Foi disponibilizado no Processo de Regerar Saldos e Custos a opção “Apresentar mensagem de sucesso por saldo” que tem por finalidade definir se a mensagem de regeração de cada saldo foi concluída.

**Classificação do Período do Orçamento**

Implementação de uma determinada classificação de um mesmo período associado ao Controle Orçamentário.

**Consistência da Numeração do Movimento em Relação à Notas Fiscais Eletrônicas Inutilizadas**

Implementado o tratamento da consistência da numeração do movimento no momento da inclusão, evitando a utilização de numerações que estejam em processo de inutilização na Secretaria da Fazenda.  
Isto torna robusto o tratamento das inclusões de movimentações, evitando inconsistências entre a base de dados e as informações repassadas para a Secretaria da Fazenda.

**Consistência do Cancelamento de Movimentos com NF-e Autorizada**

Foi implementada a consistência no cancelamento de movimentos integrados à Nota Fiscal Eletrônica. Deste modo, ao tentar cancelar um movimento associado à uma NF-e Autorizada, o sistema não permitirá seu cancelamento. Caso a parametrização do tipo de movimento definir que o envio das NF-e's é automático, ao tentar cancelar o movimento associado à uma NF-e Autorizada o sistema não permitirá o cancelamento, mas irá disparar o processo de cancelamento da NF-e junto à SEFAZ.

**Contrato por Medição**

Ao replanejar um Contrato por Medição que já tenha sido parcialmente faturado, será considerado apenas o valor não faturado. Previsões de Medição vinculadas a uma Medição faturada não serão excluídas, mas a diferença entre o valor faturado e o provisionado será somada ao valor a provisionar.

**Cotação**

Melhoria realizada na rotina de geração do Quadro Comparativo da Cotação.

**Data Referente a Contagem do Item a ser Inventariado**

Implementado nesta versão a Data e Hora registrada no momento da inserção ou alteração dos campos referente a 1ª Contagem , 2ª Contagem e 3ª Contagem dos itens a serem inventariados.

**Desmembramento do Produto Composto Relacionando a Natureza Orçamentária**

Ao inserir um produto composto em um movimento que trabalha com Controle Orçamentário e logo em seguida informar a Natureza Orçamentária para esse produto, a Natureza Orçamentária será copiada para os itens que fazem parte do Produto Composto.

**Disponibilizado o Campo CODIGO EX (NCM) no Layout de Importação de Arquivos-Texto de Produtos**

O campo CODIGO EX, utilizado para o tratamento de informações de NCM (Nomenclatura Comum do Mercosul), foi disponibilizado na versão 3.0 do Layout de importação de Arquivos-Texto de Produtos.  
Para saber como montar o arquivo contemplando esta informação, acesse Menu Utilitários | Importações / Exportações | Importar Arquivo Texto, selecionando a versão do Layout 3.0 e, na parte superior esquerda, selecione a opção Produtos.A

**Editar Município por Item**

O campo Editar Município por Item foi alterado de localização no parametrizador do Tipo de Movimento para a pasta de Dados Fiscais.

**Escrituração de Movimentos**

Na inclusão de uma NF-e Municipal o campo ‘Data Saída’ será tratado como sendo a data de competência do movimento, podendo este ser anterior à efetiva data de emissão do movimento.

**Faturamento de Contratos**

Melhoria realizada no Módulo de Faturamento de Contratos com comissão de vendedores.

**Contratos - Faturamento de Medições**

Caso os campos Município e UF não sejam informados na Medição e o movimento usado para o Faturamento da Medição utilize Município por Item, será considerado o Município e UF informados na pasta “Faturamento” do item de contrato.

**Implementada a Usabilidade de Função de Fórmula de Campos da TMOVFISCAL e TITMMOVFISCAL**

Foi implementada no sistema a Função de Fórmula TABITMMOVFISCAL, para que os dados da tabela TITMMOVFISCAL possam ser utilizados em contextos de fórmulas, inclusive em fórmulas de bases de cálculo de tributos.  
Os dados a serem utilizados na Função de Fórmula somente estarão disponíveis se este movimento tratar de Importação de Mercadorias (Cliente / Fornecedor estrangeiro e Natureza de Operação 3.XXX).

**Implementada Opção de 'Cotar' nas Permissões por Tipo de Movimento**

Foi implementado no Cadastro de Usuários | Acesso a Movimentos, a permissão 'Cotar', que dará permissão para que determinados usuários possam efetuar Cotação somente utilizando determinados Tipos de Movimento.  
Esta funcionalidade visa aumentar a segurança do módulo de Compras, evitando que os usuários criem Cotações utilizando de Tipos de Movimentos os quais não possuem acesso.  
***Observação***: Este parâmetro somente será visível nos Tipos de Movimento '1.1.XX', não sendo apresentados nos demais, pois não fazem parte do processo de Cotação.

**Implementado o Parâmetro 'Bloqueia Movimentação' no Assistente de Inventário**

Implementado no Assistente de criação de Inventários o parâmetro 'Bloqueia Movimentação'. Este parâmetro, quando desmarcado, permitirá que o produto continue sendo movimentado no sistema sem inviabilizar sua utilização. Terá efeitos diferentes no Inventário, dependendo da sua utilização.

**Implementados Novos Tipos de Frete: ‘Terceiros’ e ‘Nenhum’**

Foi implementado nesta nova versão, na edição de Movimentos, novas opções de Tipo de Frete (aba Transporte | Identificação): ‘Terceiros’ e ‘Nenhum Frete’.   
Estes Tipos de Frete foram implementados por uma necessidade de alinhamento ao processo de SPED Fiscal, o qual fazia consistência com estes outros 2 Tipos de Frete, além dos já existentes: ‘CIF’ e ‘FOB’.   
Estas opções estão disponíveis no Parametrizador do Tipo de Movimento na etapa ‘Mov – Transporte 2/2’ com as seguintes opções: ‘Sempre Terceiros’ e ‘Default Terceiros’.  
Além disso, foi implementado também o campo para definição de uma mensagem default quando o Frete for do tipo ‘Terceiros’, a ser definida no campo ‘Mensagem Terceiros Default’.

**Importação de Arquivos-Texto**

Melhoria realizada no módulo de importação de produtos via Arquivos-Texto referente a tabela:TPRD, campo: Pesável.

**Inclusão do Projeto/Tarefa no Movimento via Portal**

O movimento incluído via Portal obedecerá as mesmas parametrizações referente ao movimento criado no Sistema TOTVS Gestão de Estoques, Compras e Faturamento. A partir desta versão será disponibilizada a informação do projeto/tarefa neste ambiente.

**Integração do TOTVS Gestão de Estoques, Compras e Faturamento com TOTVS Gestão Bibliotecária Relacionado a Compras de Exemplares**

Com esta integração, a partir desta versão será possível realizar uma solicitação de compras de exemplares e posteriormente a compra efetivada dos mesmos.

**Integração TOTVS Gestão de Estoques, Compras e Faturamento x TOTVS Gestão de Pessoas**

Os movimentos de Empréstimo e Devolução do TOTVS Gestão de Estoques, Compras e Faturamento integrados com o TOTVS Gestão de Pessoas poderão afetar o saldo financeiro além do saldo físico.

**Parametrização do Tipo de Movimento que Integra com o TOTVS Gestão de Pessoas**

A partir desta versão será possível incluir movimentos com itens repetidos para Tipo de Movimento integrado ao TOTVS Gestão de Pessoas.

**Regeração de Saldos e Custos**

Para melhorar a performance do processo de Regerar Saldos e Custos foi criada na tela a opção "Atualizar data de Movimento". Esse parâmetro tem como objetivo deixar que o usuário defina se quer que a Data do Movimento nos movimentos que entraram na regeração seja atualizada ou não.
