---
content_hash: c79ca46d1107106417097d44e636222b9abea4610a4f801ac59fa495959a6ad4
fetched_at: '2026-06-29T00:06:02.898891+00:00'
page_id: '198949870'
product: rm
source: tdn-rm
title: DT_Realocacao_Orcamentaria
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Realocacao_Orcamentaria
version: 8
---

# REALOCAÇÃO ORÇAMENTÁRIA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Transferência de Valores do Orçamento. | MovTransfValOrcamentoProcAction. | | Transferência de Valores do Orçamento para Itens de Períodos Posteriores | MovTransfValOrcamentoPeriodoPosteriorProcAction | | Reprocessar Movimento Bloqueado por Orçamento | MovReprocessarMovBloqueadoOrcProcAction | | Liberar Movimento Bloqueado por Orçamento | MovLiberarMovBloqueadoOrcProcAction |          |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Transferência de Orçamentos. |  | | Realocação Orçamentária | MovRealocaOrcamentoAction | |
| **Parâmetro(s):** | Usa Grupo Orçamentário. |
| **Requisito (ISSUE):** | PCREQ-6359 |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | SQL Server e Oracle. |
| **Tabelas utilizadas:** | TORCAMENTO - Controle Orçamentário  TMOVORCAMENTO - Movimentação do Orçamento  TEXCEDEORCAMENTO - Valores Excedentes do Orçamento  TITMPERIODOORCAMENTO - Item do Período do Controle Orçamentário  TTBGRUPOORCAMENTO - Tabela de Grupo Orçamentário  TMOV - Movimentos  TITMMOV - Itens de Movimento |
| **Sistema(s) operacional(is):** | Windows 7 SP1 ou superior. |
| **Versões/Release:** | 12.1.7. |

## Descrição

Foram criados novos processos relacionados ao Controle Orçamentário. São eles:

* Transferência Orçamentos
  + Transferência de Valores do Orçamento
  + Transferência de Valores do Orçamento para Itens de Períodos Posteriores
* Reprocessar Movimento Bloqueado por Orçamento.
* Liberar Movimento Bloqueado por Orçamento.

**Transferência de Valores do Orçamento**

Trata a transferência de valores entre orçamentos do mesmo período, ou seja, tanto o orçamento de origem quanto o orçamento de destino devem ter o mesmo período. O usuário poderá selecionar Itens de Período  
diferentes para os Orçamentos de Origem e Destino.

Esta nova funcionalidade possui quatro níveis de permissão, sendo que quando o usuário possuir todas as permissões de acesso,sempre será considerada a maior.

Os níveis de permissão são:

* + **Nível 1 - Transfere entre Naturezas do Centro Custo:** Só será permitido transferir saldo entre Naturezas do mesmo Centro de Custo. O  item de período do orçamento de destino será carregado automaticamente.
  + **Nível 2 - Transfere entre Naturezas e Centros de Custo que está Associado:**Permitirá transferir saldo entre Naturezas e Centros de Custo que está associado. O  item de período do orçamento de destino será carregado automaticamente.
  + **Nível 3 - Transfere entre Naturezas e Centros de Custo que está Associado, com Valores dos Períodos Anteriores:**Permitirá transferir saldo entre Naturezas e Centros de Custo que está associado, mas que tenham itens de período inferiores aos do orçamento de origem.
  + **Nível 4 - Transfere entre Naturezas e Centros de Custo que está Associado, com Valores de Todos os Períodos:**Permitirá transferir saldo entre Naturezas e Centros de Custo que está associado ao orçamento de origem, para todos os itens de período disponíveis.

**Transferência de Valores do Orçamento para Itens de Períodos Posteriores**

Trata a transferência de valores entre orçamentos do mesmo período, ou seja, tanto o orçamento de origem quanto o orçamento de destino devem ter o mesmo período.  
O usuário poderá selecionar Item de Período para o Orçamento de Origem e esses dados serão replicados para o Orçamento de Destino, permitindo ao usuário a alteração apenas do Item de Período do Orçamento de Destino, contanto que o mesmo seja posterior ao Item de período do Orçamento de Origem.

Esta funcionalidade possui dois níveis de permissão, sendo que quando o usuário possuir todas as permissões de acesso, sempre será considerada a maior.

Os níveis de permissão são:

* ****Nível 1 -**Transfere entre Naturezas e Centros de Custo que está Associado****:**Permitirá transferir saldo entre Naturezas e Centros de Custo que está associado.
* **Nível 2 - Transfere entre qualquer Natureza e Centro de Custo:**Permitirá transferir saldo entre todas as Naturezas e todos os Centros de Custo, independente de estar associado.

**Reprocessar Movimento Bloqueado por Orçamento**

Verifica se o movimento pode ser desbloqueado, pois pode ter recebido uma transferência.

**Liberar Movimento Bloqueado por Orçamento**

O usuário poderá liberar o movimento, sem que seja necessário realizar uma transferência. Neste caso o sistema irá aumentar o saldo orçado do centro de custo / natureza / item de período no valor do movimento, para que o mesmo seja liberado.

**Informações sobre Valores Excedentes do Orçamento (**Tabela - TEXCEDEORCAMENTO**)**

* **Tipo do Valor Excedente (**TEXCEDEORCAMENTO.TIPO**)**

**B** - Barra;  
**A** - Avisa;  
**L** - Bloqueia;  
**N** - Não Avisa.

**Informações sobre Orçamento (**Tabela - TMOVORCAMENTO**)**

* **Tipo de Orçamento (**TMOVORCAMENTO.TIPO**)**

**N** - Nenhum;  
**I** - Inclusão;  
**A** - Estorno;  
**E** - Efeito Inverso;  
**T** - Transferência;  
**C** - Cancelamento.

## Procedimento para Configuração

**Configuração de Segurança**

Para utilizar o novo recurso de **Transferência Orçamento** é necessário habilitar as permissões no cadastro de Perfis do Usuário.

1. Acesse o módulo **Serviços Globais**, acesse **Segurança / Perfis / Contexto Sistema: Gestão de Estoque, Compras e Faturamento.**
2. Posicione o cursor em um perfil e clique em **Editar**.
3. Na pasta **Acesso a Menus** selecione a opção **Orçamento / Transferência Orçamento** e habilite a permissão para o perfil de usuário.
4. Confira os dados e confirme.

Para utilizar **Reprocessar Movimento Bloqueado por Orçamento:**

1. No módulo **Serviços Globais**, acesse **Segurança / Perfis / Contexto Sistema: Gestão de Estoque, Compras e Faturamento.**  
   O sistema apresenta a janela dos perfis cadastrados.
2. Posicione o cursor em um perfil e clique em **Editar**.
3. Na pasta **Acesso a Menus** selecione a opção **Orçamento / Realocação Orçamentária de Movimentos** e habilite a permissão **Reprocessar Movimento Bloqueado por Orçamento**para o perfil de usuário.
4. Confira os dados e confirme.

Para utilizar **Liberar Movimento Bloqueado por Orçamento:**

1. No módulo **Serviços Globais**, acesse **Segurança / Perfis / Contexto Sistema: Gestão de Estoque, Compras e Faturamento.**  
   O sistema apresenta a janela dos perfis cadastrados.
2. Posicione o cursor em um perfil e clique em **Editar**.
3. Na pasta **Acesso a Menus** selecione a opção **Orçamento / Realocação Orçamentária de Movimentos** e habilite a permissão **Liberar****Movimento Bloqueado por Orçamento**para o perfil de usuário.
4. Confira os dados e confirme.

## Procedimento para Utilização

****Transferência de Valores do Orçamento**:**

       1. Acesse o módulo **BackOffice / Gestão de Estoque, Compras e Faturamento** / **Orçamento / Controle Orçamentário / Transferência Orçamento / Transferência de Valores do Orçamento**.

O sistema apresenta a janela Transferência de Valores do Orçamento.

       2. Informe o Período do Orçamento.

       3. Informe o Item de Período do Orçamento Origem.

Neste momento escolha um orçamento de origem com saldo.

       4. Informe o Item de Período do Orçamento Destino.

Neste momento escolha os orçamentos de destino.

       5. Informe o Valor a Transferir para cada orçamento.

       6. Informe uma Observação, caso necessário.

 7. Clique no botão Executar.

O sistema executa a transferência orçamentaria.

**Transferência de Valores do Orçamento para Itens de Períodos Posteriores**

1. Acesse o módulo **BackOffice / Gestão de Estoque, Compras e Faturamento** / **Orçamento / Controle Orçamentário / Transferência Orçamento / **Transferência de Valores do Orçamento para Itens de Períodos Posteriores****.

O sistema apresenta a janela Transferência de Valores do Orçamento para Itens de Períodos Posteriores.

       2. Informe o Período do Orçamento.

       3. Informe o Item de Período do Orçamento Origem.

Neste momento escolha um orçamento de origem.

       4. Informe o Item de Período do Orçamento Destino.

       5. Informe uma Observação, caso necessário.

       6. Clique no botão Executar.

O sistema executa a transferência orçamentaria.

**Reprocessar Movimento Bloqueado por Orçamento:**

       1. Acesse o módulo **BackOffice / Gestão de Estoque, Compras e Faturamento** / **Orçamento / Controle Orçamentário / Realocação Orçamentária de Movimentos**.

O sistema apresenta a janela Realocação Orçamentária (Movimentos Bloqueados).

       2. Selecione os registros na visão.

       3. Acesse **Processos / Reprocessar Movimento Bloqueado por Orçamento**.

Neste momento o sistema libera o movimento bloqueado.

**Liberar Movimento Bloqueado por Orçamento:**

       1. Acesse o módulo **BackOffice / Gestão de Estoque, Compras e Faturamento** / **Orçamento / Controle Orçamentário / Realocação Orçamentária de Movimentos**.

O sistema apresenta a janela Realocação Orçamentária (Movimentos Bloqueados).

       2. Selecione os registros na visão.

       3. Acesse **Processos / Liberar Movimento Bloqueado por Orçamento**.

Neste momento o sistema libera o movimento bloqueado.
