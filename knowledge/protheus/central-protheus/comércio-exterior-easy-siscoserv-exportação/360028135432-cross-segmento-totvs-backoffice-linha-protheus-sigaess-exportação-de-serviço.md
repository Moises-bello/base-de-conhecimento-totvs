---
article_id: 360028135432
category: Comércio Exterior - Easy Siscoserv - Exportação
content_hash: 3513cabf0d596b5b01dad2317467dd58ccb6a48d0bdf06e6769a504836c30623
fetched_at: '2026-06-28T22:39:38.916113+00:00'
product: protheus
section_id: 1500001549402
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAESS - Exportação de
  Serviço
type: support-article
updated_at: '2022-06-21T20:43:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028135432-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAESS-Exporta%C3%A7%C3%A3o-de-Servi%C3%A7o
---

**Dúvida**Como criar o Processo de exportação de serviço?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Easy Siscoserv – A partir da versão 11.80  
  
**Solução**

**Pré-Requisitos:**

* Possuir um cliente de serviço cadastrado na manutenção de **Clientes**;
* Possuir um serviço cadastrado na manutenção de **Produtos**;

**Sequência 001:**

1. No **Easy Siscoserv (SIGAESS)**, acesse: **Atualizações \ Exportação \ Processo Venda**.
2. Clique na opção **Incluir**.
3. Será apresentada a rotina de **Processo de Serviço**, digite os dados desejados.
4. Clique sobre o botão **Confirmar**para gravar.

**Nota:** Caso o parâmetro **MV\_ESS0003** apresente conteúdo **“.T.”**, o sistema irá gerar os **Registros de Venda de Serviços** de forma automática a partir da inclusão de um processo, desde que o mesmo possua todas as informações necessárias para tal. Se mesmo assim o sistema não conseguir gerar o **Registros de Venda de Serviços** de forma automática, será informado ao usuário o motivo por meio do campo **Msg. Log** presente no **Processo de Venda**.

**Sequência 002**

1. No **Easy Siscoserv (SIGAESS)**, acesse: **Atualizações \ Exportação \ Processo Venda**.
2. Clique na opção **Faturamento**.
3. Será apresentada a tela **Faturamento**, na parte superior da tela, clique na opção **Incluir**, será apresentada a tela **Invoices de Serviços**, digite os dados desejados.

**Nota:** Caso o campo **Cond. Pag.** seja informado, o sistema irá gerar as parcelas de câmbio de forma automática, de acordo com a especificação da condição de pagamento. Caso contrário, o sistema permite a inclusão manual das parcelas.

**Sequência 003:**

1. No **Easy Siscoserv (SIGAESS)**, acesse: **Atualizações \ Exportação \ Processo Venda**
2. Clique no botão **Outras Ações / Faturamento**.
3. Será apresentada a tela **Invoices**, na parte inferior da tela, selecione a parcela de câmbio, clique no botão **Outras Ações** / **Liquidar**, será apresentada a tela **Liquidação da Parcela**.
4. Na pasta **Dados Gerais**, preencha as informações necessárias.
5. Na pasta **Contrato de Câmbio**, preencha as informações necessárias.
6. Clique sobre o botão **Confirmar** para gravar.

**Nota:** Diferentemente do módulo de Aquisição, neste caso, a liquidação das parcelas não irá gerar o **Faturamento** (anteriormente chamado de **Pagamento**). Este será gerado no momento que o Processo apresentar Invoice e algum item contido em um **Registro de Venda de Serviço**, sendo assim, o **Faturamento** está relacionado diretamente a essas três etapas.

**Sequência 004:**

1. No **Easy Siscoserv (SIGAESS)**, acesse: **Atualizações \ Exportação \ RVS**.

**Nota:** Caso o parâmetro **MV\_ESS0003** apresente conteúdo **“.T.”**, o sistema terá gerado os registros de forma automática a partir da inclusão de um processo, desde que o mesmo possua todas as informações necessárias para tal. Porém, também é possível incluir um novo Registro de forma manual, desde que haja processos que ainda não apresentam status **Em fase de** **Registro** no cadastro de **Processos Venda**, ou seja, processos que não possuem um RVS gerado.

1. Clique na opção **Incluir**.
2. Será apresentada a tela **Registro de Serviços**.
3. Na pasta **Dados Gerais**, digite os dados desejados.

**Nota**: O campo **Processo Base** é um facilitador cujo objetivo é completar alguns dados da capa do registro de serviços e/ou o(s) serviço(s) incluído(s) a partir de um processo. Ao selecionar um processo, o sistema apresentará a seguinte mensagem: **Deseja selecionar todos os serviços pertencentes a este processo?**. Ao escolher a opção “**Sim**” o sistema trará todos os serviços ainda não vinculados a outro processo, ao escolher a opção “**Não”**, só atualizará as informações da capa do registro.

**Observações**: Caso queira preencher os detalhes com as informações do outro processo, clique em **Seleção de Processos**. Será apresentada a tela **Parâmetros**, onde é possível selecionar um processo específico por meio do campo **Processo Base?** Ou todos os processos que possuam serviços com o mesmo código **N.B.S** por meio do campo **Código N.B.S.?**.

Neste exemplo usaremos o filtro por processo, portanto, selecione o processo de serviço criado anteriormente e clique em **OK**. O sistema irá carregar as informações do(s) serviço(s) do processo selecionado.

1. Verifique que na pasta **Financeiro** as informações de valores foram preenchidas automaticamente.

**Nota:** Caso o serviço esteja vinculado à importação de bens, deve-se preencher o número da RE na tela de **Documentos**(localizada no canto superior direito). Esta tela estará disponível caso o parâmetro **MV\_ESS0004** apresentar conteúdo **“.T.”**.

1. Clique sobre o botão **Confirmar** para gravar.

**Nota**: Os status dos registros e dos faturamentos são atualizados conforme a fase do processo. Caso o **Registro de Venda de Serviços**já possua uma invoice, o mesmo possui um faturamento que fica visível na parte inferior da tela **Registro de Serviços.**
