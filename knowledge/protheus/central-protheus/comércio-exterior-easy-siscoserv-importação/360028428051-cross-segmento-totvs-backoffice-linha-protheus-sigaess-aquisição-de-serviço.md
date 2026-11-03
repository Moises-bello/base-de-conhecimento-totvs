---
article_id: 360028428051
category: Comércio Exterior - Easy Siscoserv - Importação
content_hash: 48bfa3a2db33ccd6d46f5a527c58ce512a55d78e248c870a14d026ee4c3e9f23
fetched_at: '2026-06-28T22:39:39.585395+00:00'
product: protheus
section_id: 1500001538321
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAESS - Aquisição de Serviço
type: support-article
updated_at: '2022-06-21T20:52:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028428051-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAESS-Aquisi%C3%A7%C3%A3o-de-Servi%C3%A7o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:05:00 min  
  
Dúvida**Como crio o Processo de aquisição de serviço?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Easy Siscoserv – A partir da versão 11.80  
  
**Solução****Pré-Requisitos:**Possuir um fornecedor de serviço estrangeiro cadastrado na manutenção de **Fornecedores (Fabricante/Forn.)**;

* Possuir um serviço cadastrado na manutenção de **Produtos**;

**Sequência 001:**

1. No **Easy Siscoserv (SIGAESS)**, acesse: **Atualizações \ Importação \ Processo Aquisição**.
2. Clique na opção **Incluir**.
3. Digite os dados desejados na tela de **Processo de Serviço.**
4. Clique no botão **Confirmar** para gravar.

**Nota:** Caso o parâmetro **MV\_ESS0003** apresente o conteúdo **“.T.”**, o sistema irá gerar automaticamente o **Registro de Aquisição de Serviços (RAS)**, mas para isso é necessário que as informações referente ao **RAS** sejam preenchidas corretamente na tela de **Processo de Aquisição**. Caso haja algum problema na geração do **RAS,** de forma automática, o motivo será informado ao usuário por meio do campo **Msg. Log** presente no **Processo de Aquisição**.

**Sequência 002**

1. No **Easy Siscoserv (SIGAESS)**, acesse: **Atualizações \ Importação \ Processo Aquisição.**
2. Clique na opção **Invoices**.
3. Será apresentada a tela **Invoices**, na parte superior da tela, clique na opção **Incluir**, será apresentada a tela **Invoices de Serviços**, digite os dados desejados.

**Nota:** Caso o campo **Cond. Pag.** seja informado, o sistema irá gerar as parcelas de câmbio de forma automática, de acordo com a especificação da condição de pagamento. Caso contrário, o sistema permite a inclusão manual das parcelas.

**Sequência 003:**

1. No **Easy Siscoserv (SIGAESS)**, acesse: **Atualizações \ Importação \ Processo Aquisição**.
2. Clique no botão **Outras Ações / Invoices.**
3. Será apresentada a tela **Invoices**, na parte inferior da tela, selecione a parcela de câmbio e clique no botão **Outras Ações / Liquidar,**a tela Liquidação da Parcela será exibida.
4. Na pasta **Dados Gerais**, preencha as informações necessárias.
5. Na pasta **Contrato de Câmbio**, preencher os dados bancários.
6. Clique no botão **Confirmar** para gravar.

**Nota:** No módulo Aquisição, a liquidação das parcelas gerará o **Pagamento** correspondente, que poderá ser visualizado por meio da tela de **Registro de Aquisição de Serviço**.

**Sequência 004:**

1. No **Easy Siscoserv (SIGAESS)**, acesse: **Atualizações \ Importação \ RAS**.

**Nota:** Caso o parâmetro **MV\_ESS0003** apresente conteúdo “**.T.**”, o sistema terá gerado os registros de forma automática a partir da inclusão de um processo, desde que o mesmo possua todas as informações necessárias para tal. Porém, também é possível incluir um novo Registro de forma manual, desde que haja processos que ainda não apresentam status **Em fase de Registro** no cadastro de **Processos de Aquisição**, ou seja, processos que não possuem um RAS gerado.

1. Clique na opção**Incluir**.
2. Será apresentada a tela **Registro de Serviços**.
3. Na pasta **Dados Gerais**, digite os dados desejados.

**Nota**: O campo **Processo Base**é um facilitador cujo objetivo é completar alguns dados da capa do registro de serviços e/ou o(s) serviço(s) incluído(s) a partir de um processo. Ao selecionar um processo, o sistema apresentará a seguinte mensagem: **Deseja selecionar todos os serviços pertencentes a este processo?**. Ao escolher a opção **“Sim”** o sistema trará todos os serviços ainda não vinculados a outro processo, ao escolher a opção **“Não”**, só atualizará as informações da capa do registro.

**Observações**: Caso queira preencher os detalhes com as informações do outro processo, clique no botão**Outras Ações /** **Seleção de Processos**. Será apresentada a tela **Parâmetros**, onde é possível selecionar um processo específico por meio do campo **Processo Base?** Ou todos os processos que possuam serviços com o mesmo código **N.B.S** por meio do campo **Código N.B.S.?**.

Neste exemplo usaremos o filtro por processo, portanto, selecione o processo de serviço criado anteriormente e clique no botão **OK**. O sistema irá carregar as informações do(s) serviço(s) do processo selecionado.

1. Observe que as informações de valores foram preenchidas automaticamente na pasta **Financeiro.**

**Nota:** Caso o serviço esteja vinculado à importação de bens, deve-se preencher o número da DI na tela de **Documentos**(localizada no canto superior direito). Esta tela estará disponível caso o parâmetro **MV\_ESS0004** apresentar conteúdo **“.T.”**.

1. Clique no botão **Confirmar** para gravar.

**Nota**: Os status dos registros e dos pagamentos são atualizados conforme a fase do processo. Caso o **Registro de Aquisição de Serviços** esteja vinculado a um **Processo**que já possua uma parcela de câmbio liquidada, o mesmo possui um pagamento, que fica visível na parte inferior da tela **Registro de Serviços.**
