---
content_hash: 351b418cb38710f01d146258f9f89e00e97558a050ef39f697885862137b9649
fetched_at: '2026-06-29T00:09:44.450138+00:00'
page_id: '433238291'
product: rm
source: tdn-rm
title: DT Estoque de Terceiros - RM Factor
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Estoque+de+Terceiros+-+RM+Factor
version: 44
---

# Estoque de Terceiros - RM Factor

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | BackOffice. |
| **Módulo:** | Gestão de Planejamento e Controle da Produção [RM Factor]. |
| **Rotina:** | Estoque de Terceiros. |
| **Cadastros Iniciais:** | N/A. |
| **Parâmetro(s):** | Tipos de Movimentos: RM Factor | Opções | Parâmetros | Produção | Movimentações de Estoque. |
| **Requisito:** | Estoque de Terceiros. |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | SQL Server e Oracle. |
| **Tabela(s) Utilizadas:** | KPARAMETROSFACTOR  KORDEM  KATVORDEMMPTERCEIRO  KATVORDEMPERDAMPTERCEIRO  KATVORDEMPRODUCAOTERCEIRO  KATVORDEMSUBPRODUTOTERCEIRO |
| **Sistema(s) Operacional(is):** | Windows 7 e superiores. |

## Descrição

O controle de Estoque de Terceiros na Ordem de Produção permite consumir produtos de terceiros na produção e gerar produção para estoque de terceiros, esse processo está disponível para o Apontamento Convencional (menu Produção | Andamento das Ordens de Produção) e Apontamento Simplificado (menu Produção | Apontamento Simplificado).

## **Restrições**

* O processo de controle de Estoque de Terceiro na Ordem de Produção não contempla produtos controlados por lote e/ou número de série. Ou seja, não é possível utilizar no Material Consumido de Terceiro, Perda de Material de Terceiro, Subproduto de Terceiro e/ou Acabado/Semiacabado de Terceiro, produtos que possuam controle de lote e número de série.

* Não é possível controlar materiais de terceiros ao utilizar os Apontamentos Múltiplos (por Estrutura e Atividade) e Apontamento via Código de Barras.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações Biblioteca RM versão 12.1.23.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

**Tipos de Movimentos de Terceiros**

No **RM.exe** acesse o "BackOffice | Gestão de Estoque, Compras e Faturamento | Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento e configure faça as configurações

**Configurações da Gestão de Estoque:**

Ao configurar para trabalhar com estoque de terceiros é obrigatório trabalhar apenas com saldo positivo.

* 04.04 - Gestão de Estoque | 04.04.01 - Definições de Estoque | Saldos de Estoque 1/3
  + Saldo Atual: Barra

**Configurações dos tipos de movimento:**

* **Tipo Mov. registro de produção (TERCEIRO):** movimento utilizado para realizar entrada em estoque de terceiros dos produtos acabados produzidos.
  + Parametrização do tipo de Movimento no TOTVS Gestão de Estoque, Compras e Faturamento:
    - Código Tipo de Movimento: 1.2.XX
    - Etapa Mov - Emitente/Destinatário 1/2: Emitente = Empresa; Destinatário = Fornecedor; Edição do Local de Emissão = Edita ou Mostra; Filial = Informar uma filial default; Local de Estoque = Informar um local de estoque default.
    - Etapa Mov - Datas 1/2: Data do Movimento Default: Data de Emissão.
    - Etapa Item - Identificação 2/2: Permite Item Repetido = Marcado; Unidade de Medida Padrão = Unidade de Controle.
    - Etapa Estoque - Estoque 1/3: Efeito Sobre os Saldos Físicos > Todos devem estar definidos como "Não Altera".
    - Etapa Estoque - Estoque 2/3: Saldo Financeiro | Efeito Sobre o Saldo Atual = "Não Altera".
    - Etapa Estoque - Estoque 2/3: Tipo Controle de Estoque de Terceiros = Movimentação Interna (PCP); Efeito Sobre o Saldo de Terceiros = Aumenta.
    - Etapa Produção: Entrada de Produtos Acabados a Partir do RM Factor = Marcado.
* **Tipo Mov. registro de subproduto (TERCEIRO):** movimento utilizado para realizar entrada em estoque de terceiros dos subprodutos gerados na produção.
  + Parametrização do tipo de Movimento no TOTVS Gestão de Estoque, Compras e Faturamento:
    - Código Tipo de Movimento: 1.2.XX
    - Etapa Mov - Emitente/Destinatário 1/2: Emitente = Empresa; Destinatário = Fornecedor; Edição do Local de Emissão = Edita ou Mostra; Filial = Informar uma filial default; Local de Estoque = Informar um local de estoque default.
    - Etapa Mov - Datas 1/2: Data do Movimento Default: Data de Emissão.
    - Etapa Item - Identificação 2/2: Permite Item Repetido = Marcado; Unidade de Medida Padrão = Unidade de Controle.
    - Etapa Estoque - Estoque 1/3: Efeito Sobre os Saldos Físicos > Todos devem estar definidos como "Não Altera".
    - Etapa Estoque - Estoque 2/3: Saldo Financeiro | Efeito Sobre o Saldo Atual = "Não Altera".
    - Etapa Estoque - Estoque 2/3: Tipo Controle de Estoque de Terceiros = Movimentação Interna (PCP); Efeito Sobre o Saldo de Terceiros = Aumenta.
    - Etapa Produção: Entrada de Produtos Acabados a Partir do RM Factor = Marcado.
* **Tipo Mov. consumo de matéria prima (TERCEIRO)**: movimento utilizado para realizar o consumo de matéria prima de terceiros apontada na produção.
  + Parametrização do tipo de Movimento no TOTVS Gestão de Estoque, Compras e Faturamento:
    - Código Tipo de Movimento: 2.2.XX
    - Etapa Mov - Emitente/Destinatário 1/2: Emitente = Empresa; Destinatário = Fornecedor.
    - Etapa Mov - Datas 1/2: Data do Movimento Default: Data de Emissão.
    - Etapa Item - Identificação 2/2: Permite Item Repetido = Marcado; Unidade de Medida Padrão = Unidade de Controle.
    - Etapa Estoque - Estoque 1/3: Efeito Sobre os Saldos Físicos > Todos devem estar definidos como "Não Altera".
    - Etapa Estoque - Estoque 2/3: Saldo Financeiro | Efeito Sobre o Saldo Atual = "Não Altera".
    - Etapa Estoque - Estoque 2/3: Tipo Controle de Estoque de Terceiros = Movimentação Interna (PCP); Efeito Sobre o Saldo de Terceiros = Diminui; Local de Estoque por Item = Marcado.
    - Etapa Produção: Baixa de Matéria Prima no RM Factor = Marcado.
* **Tipo Mov. registro consumo material perdido (TERCEIRO):** movimento utilizado para realizar o consumo de materiais perdidos de terceiros apontados na produção.  
  + Parametrização do tipo de Movimento no TOTVS Gestão de Estoque, Compras e Faturamento:
    - Código Tipo de Movimento: 2.2.XX
    - Etapa Mov - Emitente/Destinatário 1/2: Emitente = Empresa; Destinatário = Fornecedor.
    - Etapa Mov - Datas 1/2: Data do Movimento Default: Data de Emissão.
    - Etapa Item - Identificação 2/2: Permite Item Repetido = Marcado; Unidade de Medida Padrão = Unidade de Controle.
    - Etapa Estoque - Estoque 1/3: Efeito Sobre os Saldos Físicos > Todos devem estar definidos como "Não Altera".
    - Etapa Estoque - Estoque 2/3: Saldo Financeiro | Efeito Sobre o Saldo Atual = "Não Altera".
    - Etapa Estoque - Estoque 2/3: Tipo Controle de Estoque de Terceiros = Movimentação Interna (PCP); Efeito Sobre o Saldo de Terceiros = Diminui; Local de Estoque por Item = Marcado.
    - Etapa Produção: Baixa de Matéria Prima no RM Factor = Marcado.

No **RM Factor.exe** acesse o menu Opções | Parâmetros | Produção | Aba Movimentação de Estoque e defina os tipos de movimento:

Diferente das movimentações com estoque próprio, os movimentos que envolvem estoque de terceiros são gerados exclusivamente no momento do Apontamento da Ordem de Produção, desta forma o estoque sai diretamente do Local de Estoque de Terceiros no TOTVS Gestão de Estoque, Compras e Faturamento e é consumido no TOTVS Planejamento e Controle de Produção sem passar pelo Estoque Intermediário (Chão de Fábrica) utilizado em movimentações com estoque próprio.

Consistência para Tipos de Movimento que utilizam controle de Industrialização:

Para Tipos de Movimento que utilizam o Tipo Controle de Estoque de Terceiros (Etapa Estoque 2/3 da parametrização do Tipo de Movimento ) igual a "Remessa/Entrada para Industrialização" não é permitido utilizar integração com o RM Factor, ou seja, não se pode marcar qualquer parâmetro da Etapa Produção da parametrização do Tipo de Movimento simultaneamente com o tipo de controle Remessa/Entrada para Industrialização.

É possível utilizar o Tipo Controle de Estoque de Terceiros igual a "Remessa/Entrada para Industrialização" e integração com RM Factor em tipos de movimentos diferentes.

## Procedimento para Utilização

* **Definir Cliente/Fornecedor na Ordem de Produção**

Acessar o menu Produção | Ordem de Produção e incluir nova Ordem de Produção.

Na aba Identificação da Ordem de Produção informe o Cliente/Fornecedor para qual será gerada a produção.

O campo "Cli/For" é habilitado somente quando os tipos de movimentos de "Registro de Produção (TERCEIRO)" e "Consumo de Matéria Prima (TERCEIRO)" estão parametrizados.

É possível alterar esse campo somente quando a Ordem de Produção ainda não foi iniciada, ou seja, a Ordem de Produção está em um dos seguintes status: "Criada", "Aguardando Recursos" ou "Pronta pra Iniciar".

Quando o Cliente/Fornecedor está informado é possível usar na produção materiais que estão em Estoque de Terceiros e são do Cliente/Fornecedor vinculado a Ordem de Produção. Toda a produção gerada a partir dessa Ordem de Produção (Perda, Subproduto, Semiacabado, Acabado) será definida como produção para terceiros e vai ser vinculada exclusivamente ao Cliente/Fornecedor informado na Ordem de Produção.

**Observação:**  Quando a Ordem de Produção é criada a partir de Pedido (Movimento) o campo "Cli/For" NÃO é preenchido automaticamente com o Cliente/Fornecedor do Pedido, caso a ordem de produção gerada a partir de Pedido também seja uma Ordem de Produção para terceiros, após a criação da Ordem de Produção é necessário editar a Ordem e informar o campo "Cli/For".

### **Apontamento**

No apontamento de Material Consumido de Terceiro, Perda Material de Terceiro, Subproduto e Acabado/Semiacabado é gerado o respectivo movimento parametrizado para cada tipo de material. Ao realizar apontamentos parciais, a partir do segundo apontamento, são incluídos novos itens no movimento criado no primeiro apontamento.

Ao fazer um apontamento parcial, se o movimento no qual está sendo inserido o novo item estiver em alguma situação que não permite alteração (movimento que já foi faturado, por exemplo), é exibida mensagem de consistência do movimento ao tentar realizar o apontamento, nessa situação deve-se primeiro retornar o movimento para uma situação em que permite alteração e em seguida prosseguir com o apontamento.

Caso o movimento criado inicialmente esteja em um período anterior a data de fechamento de estoque, não é permitido realizar um novo apontamento.

* **Material Consumido de Terceiro**

Quando informado o Cliente/Fornecedor na Ordem de Produção é apresentada no apontamento de atividade (Menu Produção | Andamento das Ordens de Produção | Termina Atividade) a aba "Material Consumido de Terceiro". Nessa aba são apresentados para inclusão somente os produtos em estoque de terceiros do Cliente/Fornecedor definido na Ordem de Produção. São listados produtos em todos locais de estoque (da Coligada/Filial da Ordem de Produção) onde houver saldo do Cliente/Fornecedor, entretanto, não é permitido incluir o mesmo produto duas vezes em um único apontamento, mesmo que o produto esteja em locais de estoque diferentes.

Este comportamento é o mesmo para Correção de Apontamento e também para o Apontamento Simplificado.

Após incluir o material consumido de terceiro e salvar o apontamento, o movimento de consumo de matéria prima de terceiro é incluído automaticamente e os dados do mesmo são gravados na tabela KATVORDEMMPTERCEIRO.

* **Perda Material de Terceiro**

Quando informado o Cliente/Fornecedor na Ordem de Produção é apresentada no apontamento de atividade (Menu Produção | Andamento das Ordens de Produção | Termina Atividade) a aba "Perda Material de Terceiro". Nessa aba são apresentados para inclusão somente os produtos em estoque de terceiros do Cliente/Fornecedor definido na Ordem de Produção. São listados produtos em todos locais de estoque (da Coligada/Filial da Ordem de Produção) onde houver saldo do Cliente/Fornecedor, entretanto, não é permitido incluir o mesmo produto duas vezes em um único apontamento, mesmo que o produto esteja em locais de estoque diferentes.

Este comportamento é o mesmo para Correção de Apontamento e também para o Apontamento Simplificado.

Após incluir a perda de material de terceiro e salvar o apontamento, o movimento de consumo de material perdido de terceiro é incluído automaticamente e os dados do mesmo são gravados na tabela KATVORDEMPERDAMPTERCEIRO.

* **Subproduto Gerado**

Quando informado Subproduto gerado, ao salvar o apontamento, o movimento  de entrada de subproduto de terceiro é incluído automaticamente e os dados do mesmo são gravados na tabela KATVORDEMSUBPRODUTOTERCEIRO.

O movimento será criado com a Filial e Local de Estoque default definidos nos parâmetros do "Tipo de movimento de entrada de subproduto (TERCEIRO)". Caso seja utilizada Ordem de Produção em mais de uma Filial no RM Factor, deve ser parametrizado um tipo de movimento para cada Filial.

* **Apontamento de Produção (Acabado/Semiacabado)**

Ao realizar apontamento de produção, ao salvar o apontamento, o movimento de registro de produção de terceiro é incluído automaticamente e os dados do mesmo são gravados na tabela KATVORDEMPRODUCAOTERCEIRO.

O movimento será criado com a Filial e Local de Estoque default definidos nos parâmetros  do "Tipo de movimento de registro de produção (TERCEIRO)". Caso seja utilizada Ordem de Produção em mais de uma Filial no RM Factor, deve ser parametrizado um tipo de movimento para cada Filial.

**Observação:** Quando a Ordem de Produção é de Terceiro (ou seja, possui cli/for informado), o apontamento de Perda de Produção não gera movimentação de estoque de terceiros. Essa informação da Perda de Produção fica registrada somente na Ordem de Produção.

### **Correção de Apontamento**

Ao corrigir o apontamento de Material Consumido de Terceiro, Perda de Material de Terceiro, Subproduto Gerado e/ou Entrada de Produção, as alterações realizadas são refletidas diretamente nos movimentos incluídos inicialmente no apontamento. A quantidade do item do movimento pode ser alterada, para mais ou para menos, conforme a correção realizada. Quando o item é excluído do apontamento, este também é excluído do movimento e, caso o movimento possua somente um item adicionado, é realizada também a exclusão do movimento ao excluir o material na correção de apontamento.

Se o movimento que estiver sendo corrigido estiver em alguma situação que não permite alteração (movimento que já foi faturado, por exemplo), é exibida a mensagem de consistência do movimento ao tentar realizar a correção de apontamento, nessa situação deve-se primeiro retornar o movimento para uma situação em que permite alteração e posteriormente realizar a correção de apontamento.

A ordem de produção de terceiro registra movimento de forma automática durante os apontamentos das atividades, para controle de fechamento de estoque é considerado a data do primeiro apontamento realizado em qualquer atividade da ordem. A ordem de produção de terceiros deve iniciar e terminar em período aberto (sem interrupção) para que os apontamentos e movimentos possam ser registrados e alterados corretamente. Caso o movimento criado inicialmente esteja em um período anterior a data de fechamento de estoque, ao tentar realizar o Apontamento em atividades parcialmente concluídas e/ou a correção de apontamento, o sistema deve bloquear a operação, apresentando uma exceção de consistência entre as datas de Início Efetivo da Ordem e a Data de Fechamento de Estoque. Se a Ordem nunca foi apontada e a data de fechamento for data atual, será possível realizar apenas um apontamento e em seguida, a ordem vai estar travada pela data de fechamento, caso o registro de trabalho efetivo seja anterior ou igual a data de fechamento. Se a data de Trabalho Efetivo for posterior a data de fechamento, todas as ações de apontamento e correção poderão ser realizadas normalmente.

**Histórico de Movimentação:**

No histórico de movimentação é possível visualizar os movimentos de terceiros junto com os demais movimentos já exibidos no histórico, a descrição do movimento exibi informação de que trata-se de um movimento de terceiro.

**Composição de Custo**

A composição de custo do item da ordem e da atividade foram ajustados para levar em conta os materiais de terceiros envolvido na ordem de produção, não existe diferenciação na composição entre material próprio e de terceiros, o valor é sumarizado. A origem do custo dos materiais de terceiro é diretamente do movimento/item, quantidade x preço unitário do item.

**Composição de Custo**

A composição de custo do item da ordem e da atividade foram ajustados para levar em conta os materiais de terceiros envolvido na ordem de produção, não existe diferenciação na composição entre material próprio e de terceiros, o valor é sumarizado. A origem do custo dos materiais de terceiro é diretamente do movimento/item.

**Bloco K**

Os materiais consumidos de terceiro na ordem de produção são reportados através do Bloco K230, juntamente com os materiais consumidos do estoque próprio. Para ambos tipos de material (próprio e de terceiro) os dados de consumo do produto no apontamento são gerados no Bloco K230 somente quando o produto está vinculado na aba Componentes do Cadastro da Estrutura produzida na Ordem de Produção.

**Recálculo de Custo**

Após a conclusão da Ordem de Produção deve ser realizado o processo de recálculo custo (Projetos | ETO | Engenharia Sob Encomenda | Controle da Produção | Recálculo de Custos). O recálculo faz a atualização dos valores do movimento de Entrada de Produção e Subproduto de Terceiros, conforme o custo médio dos materiais de terceiro consumidos na Ordem de Produção, esse custo é calculado de acordo com a média de custo entre o último momento de saldo ZERO do terceiro e último movimento de entrada anterior ao último consumo (Tabela TRELSLDTERCEIROS). A atualização também é refletida na Composição de Custo da Ordem de Produção no "Custo Recalculado".

## Dicionário de Dados

**Arquivo ou Código do Script:**/\*$Versao=FT.2018.11\_01\*/

|  |  |
| --- | --- |
| **Tabela** | KPARAMETROSFACTOR |
| **Campo(s)** | CODTMVSAIDATRCR - Tipo de Movimento de Saída no Estoque Terceiro.  CODTMVSAIDATRCR - Código do Movimento Entrada Matéria Prima Terceiro.  CODTMVENTRADASPTRCR - Código Movimento Entrada de SubProduto de Terceiro.  CODTMVENTRADAACTRCR - Código Movimento Entrada de Acabado de Terceiro.  CODTMVENTRADAPERDAMATERIALTRCR - Tipo Mov. Perda Material. |

**Arquivo ou Código do Script:**/\*$Versao=FT.2018.11\_02\*/

|  |  |
| --- | --- |
| **Tabela** | KORDEM |
| **Campo(s)** | CODCOLCFO - Código da Coligada Cliente/Fornecedor.  CODCFO - Código do Cliente/Fornecedor. |

**Arquivo ou Código do Script:**/\*$Versao=FT.2018.11\_03\*/

|  |  |
| --- | --- |
| **Tabela** | KATVORDEMMPTERCEIRO |
| **Campo(s)** | CODCOLIGADA - Código da Coligada CODESTRUTURA - Código da Estrutura CODFILIAL - Código da filial CODMODELO - Código do Modelo CODORDEM - Código da Ordem DATAAPONTAMENTO - Data de Apontamento IDATIVIDADE - ID da Atividade IDMOV - Identificador Movimento NSEQITMMOV - Número Seq. Interno do Item do Movimento |

|  |  |
| --- | --- |
| **Tabela** | KATVORDEMPERDAMPTERCEIRO |
| **Campo(s)** | CODCOLIGADA - Código da Coligada CODESTRUTURA - Código da Estrutura CODFILIAL - Código da filial CODMODELO - Código do Modelo CODORDEM - Código da Ordem DATAAPONTAMENTO - Data de Apontamento IDATIVIDADE - ID da Atividade IDMOV - Identificador Movimento NSEQITMMOV - Número Seq. Interno do Item do Movimento |

|  |  |
| --- | --- |
| **Tabela** | KATVORDEMPRODUCAOTERCEIRO |
| **Campo(s)** | CODCOLIGADA - Código da Coligada CODESTRUTURA - Código da Estrutura CODFILIAL - Código da filial CODMODELO - Código do Modelo CODORDEM - Código da Ordem DATAAPONTAMENTO - Data de Apontamento IDATIVIDADE - ID da Atividade IDMOV - Identificador Movimento NSEQITMMOV - Número Seq. Interno do Item do Movimento |

|  |  |
| --- | --- |
| **Tabela** | KATVORDEMSUBPRODUTOTERCEIRO |
| **Campo(s)** | CODCOLIGADA - Código da Coligada CODESTRUTURA - Código da Estrutura CODFILIAL - Código da filial CODMODELO - Código do Modelo CODORDEM - Código da Ordem DATAAPONTAMENTO - Data de Apontamento IDATIVIDADE - ID da Atividade IDMOV - Identificador Movimento NSEQITMMOV - Número Seq. Interno do Item do Movimento |
