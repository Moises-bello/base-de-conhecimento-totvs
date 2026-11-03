---
article_id: 360010379511
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 265b0e27b07b1ed00cce726ad53a9ad81b89ab834153d489067d9437c46f82e1
fetched_at: '2026-06-28T22:42:02.225083+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Como gerar os registros 0500 e 0600
type: support-article
updated_at: '2025-02-11T21:07:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010379511-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-os-registros-0500-e-0600
---

**Dúvida**Como gerar os registros **0500** e **0600** do **SPED FISCAL**.  
  
**Ambiente**  
Microsiga Protheus - Livros Fiscais - A partir da versão 11.80  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
**REGISTRO 0500: Plano de contas**  
Este registro identifica as contas contábeis utilizadas pelo contribuinte, com referência no **Registro** **0300**, tendo origem no cadastro do **Plano de Contas** **(CT1)**. Podendo ser utilizado a partir de janeiro de 2011.  
  
1. Para lançamentos de notas fiscais de entrada com origem na rotina **MATA103** o registro **0500** considera o campo Conta Contábil (**B1\_CONTA**) do cadastro do produto, preenchendo o campo **D1\_CONTA** e **FT\_CONTA** da Nota Fiscal com origem na tabela **CT1**;  
  
2. Para lançamentos manual do Bem,  com a origem da rotina **MATA905**, o campo **F9\_ROTINA = MATA905.**O registro **0500** considera Conta Contábil do campo Plano de Contas (**F9\_PL**) que deverá ser criado na tabela **SF9** com consulta padrão na tabela **CT1**.

Crie o campo via configurador conforme exemplo abaixo:  
Campo: F9\_PLTipo: Caractere  
Tamanho: 20  
Decimal: 0  
Formato: @!  
Contexto: Real  
Título: Conta Contábil   Texto: Informa conta contábil    
Help: Informa a conta contábil da tabela **CT1** plano de contas para preenchimento do campo 06.  
  
3. Vincule os campos aos parâmetros: **MV\_F9PL** = **F9\_PL****Importante:** Crie uma consulta padrão para pesquisa dos códigos das tabelas.  
Ao efetuar a criação dos campos na tabela **SF9**, realize a configuração para a seleção padrão "criação da lupa - de pesquisa padrão".  
  
4.Caminho: **Configuração -> Base de Dados -> Tabela SF9 -> Editar ->Aba Opções -> Campo Cons. Padrão**   
  
5. Selecione a tabela que será consultada para preenchimento do campo.

**REGISTRO 0600: Centro de Custos**  
Este registro identifica os centros de custos com referência no **Registro 0305**. As informações têm origem do cadastro de **Centros de Custos (CTT)**. É gerado a partir de janeiro de 2011.  
  
1.Para lançamentos de notas fiscais de entrada com origem na rotina **MATA103.**O registro **0600** considera do campo Centro de Custo (**B1\_CC**) do cadastro do produto alimentado o campo **D1\_CC** nota fiscal com origem na tabela **CTT**.  
  
2. Para lançamentos manual do Bem, com origem na rotina **MATA905** campo **F9\_ROTINA = MATA905.**O registro **0600** considera centro de custo do campo centro de custo (**F9\_CC**) que deverá ser criado na tabela **SF9** com consulta padrão na tabela **CTT**.  
  
Crie o campo via configurador conforme exemplo abaixo:  
Campo: **F9\_CC**Tipo: Caractere  
Tamanho: 9  
Decimal: 0  
Formato: @!  
Contexto: Real  
Título: C. Custo     
Texto: Informa Centro de Custo  
Help: Informação do centro de custo para preenchimento do campo 02 **COD\_CCUS** registro **0305.**  
3. Vincule os campos aos parâmetros:**MV\_F9CC** = **F9\_CC****Importante:**Crie uma consulta padrão para pesquisa dos códigos das tabelas.  
Ao efetuar criação dos campos na tabela **SF9**, realize a configuração para a seleção padrão "criação da lupa - de pesquisa padrão".  
  
4. **Caminho:** Configuração -> Base de Dados -> Tabela **SF9** -> Editar ->Aba Opções -> Campo Cons. Padrão ->   
  
5. Selecione a tabela que será consultada para preenchimento do campo.
