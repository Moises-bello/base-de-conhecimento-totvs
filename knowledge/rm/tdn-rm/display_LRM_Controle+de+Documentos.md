---
content_hash: 23833d3ed067ef36a801334dfd37ad8b9c77534180bb0e14800e03195f9555e4
fetched_at: '2026-06-29T00:11:56.769745+00:00'
page_id: '871521283'
product: rm
source: tdn-rm
title: Controle de Documentos
type: documentation
url: https://tdn.totvs.com/display/LRM/Controle+de+Documentos
version: 10
---

## 

Controle de documentoVisão Geral

## **Ambiente**

TOTVS Gestão Hospitalar 12.1.27 e superiores.

**Solução**

O **Controle de Documentos** tem por objetivo gerar os Protocolos dos documentos de forma automática durante a utilização do Sistema, facilitar o processo de envio e recepção dos Malotes de documentos e checar a execução de alguns processos para envio do documento para outro setor.

* Autorização Emitida?
* Checagem realizada?
* Todos os medicamentos não checados foram devolvidos?

A funcionalidade tem por vantagens o monitoramento e garantia de vários processos além de identificar quais setores/usuários estão “represando” receita com o não envio de documentos, pois os processos Hospitalares dependem muito da documentação estar correta e completa.

Cadastro de Tipos de Documentos

## **Cadastro de Tipos de Documentos**

1. No RM, acesse **Cadastros > Registro e Controle > Outros Cadastros > Tipos de Documento**
2. Clique em **Incluir**.
3. Informe a **descrição** do Tipo de Documento.
4. Selecione um **tipo** para ser associado.
5. Para gerar pendência ao movimentar os documentos, deve-se informar o **código da pendência** no tipo de documento. Se não existir, a pendência não é gerada.
6. Clique em **OK**.

Tipos de Pendência da Conta

## **Tipos de Pendência da** **Conta**

No RM, acesse **Cadastros > Faturamento > Outros Cadastros > Pendências**

Neste cadastro, defina os tipos de pendências da conta:

* **Impeditivo**: caso este tipo seja definido, no encerramento da conta, o sistema verifica se existem pendências desse tipo. Caso existam, a conta/parcial não será liberada.
* **Risco gerenciável**.
Setores de Pendência

## **Setores de Pendência**

No RM, acesse **Cadastros > Faturamento** > **Outros Cadastros > Setor de controle de pendências**.

Neste cadastro, são incluídos os setores que podem possuir pendências.

Nele devem ser associados perfis do sistema para identificar quais usuários pertencem ao setor.

Além disso, deve-se cadastrar os outros setores que para os quais podem ser transferidas as pendências. Se não existirem setores cadastrados, ao repassar o documento, nenhum setor será exibido, e o mesmo não poderá ser repassado.

1. No campo Setor é exibido o código do setor, gerado automaticamente pelo sistema.
2. Informe a descrição do setor de pendência de conta.
3. Clique em OK.

Criando um Controle de Documentos

## **Criando um Controle de Documentos**

Para criar um controle de documentos, acesse o menu **Faturamento > Outros > Outros > Controle de Documentos,** configure o filtro e clique no botão Incluir.

**Status do documento:**Escolha o tipo de documento e preencha as informações necessárias e salve. Neste momento, o documento ficará com o status **Em aberto**.

1. Selecione o **tipo de documento**.
2. Pesquise o paciente, as informações de Código, Nome, Prontuário, Atendimento e Convênio serão carregadas.
3. Selecione o **local de Armazenamento** do documento.
4. Caso deseje informe uma observação.
5. Atendendo ao SAME (Serviço de Arquivo Médico e Estatística) para o prontuário é necessário informar o local de armazenamento
6. Salve o cadastro.
Digitalizando um Documento

## **Digitalizando um documento**

Para digitalizar um documento será necessario acessar o **Anexos > Arquivo e clicar no botão Escanear Documentos.**

Após a conclusão do escaneamento, clicar em Salvar para o documento ser armazenado.

Repasse de documento

## **Repasse de documento**

Para realizar o repasse de um documento realize o processo a seguir:

1.    No Controle de Documentos clique em **Processos** e em **Repassar**.

2.    Selecione um usuário ou um setor para transferir o documento atual e, caso deseje, informe uma observação.

3.    Selecione o usuário para o qual deseja repassar o documento.  
4.    Selecione o setor do usuário para o qual deseja transferir o documento.  
5.    Informe uma observação para sobre o repasse do documento se desejar.

Confirmação de recebimento do documento

## **Confirmação de recebimento do documento**

Para confirmar o recebimento do documento:

1. Acesse a tela de Controle de Documentos e clique em **Processos**.
2. Selecione a opção **Confirmar**.

## **Criando Malote e Confirmando Itens do Malote**

**Criando Malote**

O malote é um conjunto de documentos que ficam agrupados.

* **Opções para se gerar o malote**.

Através no grid, selecione os itens desejados com o mesmo status e clique no processo **Gerar Malote**.

* Através do Wizard, pode-se pesquisar pelo prontuário, código do atendimento, parcial ou a referência do documento.  
    
  **Controle** de **Documentos** - **Processos**e selecione **Gerar Malote com Wizard**.

**Motivo de recusa do documento**

Caso algum item não seja confirmado, deve-se informar o motivo da recusa do documento.

**ID de malote**

Um novo ID de malote é gerado para facilitar a conferência e o envio dos itens movimentados.

**Confirmação de itens do malote**

Verifique, a seguir, como realizar a confirmação de itens do malote e como informar o motivo de recusa do documento.  
  
**Confirmando itens do malote**

1. Selecione um item de um malote na tela de visão.
2. Clique no processo **Confirmar Malote**.
3. Serão exibidos os itens daquele malote.
4. Confirme os itens recebidos e clique em **Avançar**.
Remoção de Itens do Malote

## **Remoção de itens do Malote**

**Processo para remoção de itens (documentos do malotte)**

Caso o status do documento seja "A Confirmar" ou "Em aberto" é possível remover através do Processo "Remover documento do malote" o item do malote. Será registrada esta ação com o histórico no campo Motivo da aba de Transferência.

Encerramento do Controle

## **Encerramento do Controle**

Acesse o Controle de Documentos para encerrar o Controle. Para se encerrar o controle do documento, o status atual deve estar em **Confirmado**.

Ao se encerrar um controle de documento que tenha gerado uma pendência, o sistema encerrará também a pendência.  
  
**Repassar documento para outro setor**  
  
Para repassar um documento para outro setor onde será recebido por um usuário diferente do **mestre** e diferente do **criador de documento**. Existe um parâmetro para permitir, acesse:  
  
**Ambiente** - **Gestão Hospitalar** - **Faturamento** e marque a opção:   
  
**° Permite repassar documentos quando usuário pertencer ao mesmo setor**.
