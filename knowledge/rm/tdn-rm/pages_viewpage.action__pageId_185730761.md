---
content_hash: 63e8034cdeab1f2668ed886fbc818e972acac4b6c077491bc4bc20d8a41e8db0
fetched_at: '2026-06-29T00:05:58.126940+00:00'
page_id: '185730761'
product: rm
source: tdn-rm
title: Aprovar Espelho do Cartão do Ponto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185730761
version: 10
---

|  |  |  |
| --- | --- | --- |
| **Produto** | : | Totvs Automação de ponto  **Versão**: 11.83 ou Superior |
| **Processo** | : | Aprovação do Ponto |
| **Subprocesso** | : | Aprovação do Ponto pelo Portal |

A Aprovação de Espelho de Ponto tem como objetivo a redução da necessidade de impressão do Relatório de Espelho do Ponto para assinatura do Funcionário. Sendo possível realizar a Visualização /  Aprovação do espelho utilizando a integração com ECM ou Fluig.

## Habilitando a Funcionalidade

O Processo de Aprovar o Espelho do Cartão do Ponto, estará disponível no sistema mediante a execução do script de liberação do mesmo e após realizar a configuração da integração do Conector com o ECM. Este script está disponível no conversor, e tem como finalidade a criação do campo USERID na tabela GUSUARIO.

## Configurando o Conector

* Acessar o módulo **Integração | Ferramentas | Parâmetros**.
* No *parametrizador* acessar o processo **50.07 – Linha RM x GED (Gerenciamento Eletrônico de Documentos)**.

* Informar as configurações necessárias para conexão com o ECM.

* Confirme a execução do processo e finalize o *parametrizador*.

## Habilitando permissão de acesso a funcionalidade

* Acessar o módulo **Serviços Globais | Segurança | Perfis**;
* Alterar o  **Sistema** para **Automação de Ponto**:

* Selecione o perfil desejado e navegue para a aba **Acesso a Menus**;
* Para liberar o acesso ao **Acompanhamento de Aprovações** e demais processos via aplicativo navegue na árvore de menus nos seguintes itens **[06] Relatórios -> [06.01] Básicos -> [06.01.03] Acompanhar Aprovações do Ponto**.

* Para liberar acesso para a aprovação via portal, tanto para o funcionário quanto para o gestor, navegue na árvore de menus nos seguintes itens **[11] Portal RH -> [11.01] Permissões Web -> [11.01.21] Aprovar Espelho do Ponto Funcionário / [11.01.22] Aprovar Espelho do Ponto Gestor**.

## Escolhendo pasta no GED

* Navegue para o módulo **Automação de Ponto**, em seguida **Gestão | Ferramentas de Análise | RM Reports | Totvs Automação de Ponto | PTOREL01.0001 – Espelho de Cartão de Ponto | Anexos | GED | Gerenciar,** e escolha a pasta onde será salvo o arquivo no Fluig.

## Gerando o Espelho do Cartão de Ponto e exportando para o Portal

* Acesse **Relatórios | Básicos | Espelho do Cartão**.
* Execute os passos normalmente do processo até o passo 3.
* Para executar a exportação para aprovação do portal deve ser marcado a caixa de seleção **Exportar Relatório para aprovação via portal** presente no grupo **Aprovação via Portal**.
* Caso deseje sobrescrever uma exportação existente (apenas para o mesmo período), marque também a caixa de seleção **Sobrescrever relatórios existentes**.

* Finalize a execução do processo.

## Visualizar Documento

* Na tela de **Acompanhamento de Aprovações do Ponto**, em **Relatórios | Básicos**, selecione o documento a ser visualizado;
* Selecione o processo **Visualizar Documento**.

* Será aberto o browser para visualização ou aprovação do documento no Fluig.

* Ao selecionar o botão **Aprovar Documento**, será aberto janela para confirmação dessa aprovação.
* Após aprovação do documento a janela de Visualização é fechada automaticamente. E este documento passa a ficar salvo no Fluig, na pasta selecionada no Gerenciamento do GED.

## Aprovação do Documento pelo Fluig

* Ao acessar a visão do Fluig, o espelho gerado poderá ser aprovado em **Central de Tarefas** através da aba **Documentos a aprovar**.

* É possível visualizar na aba **Meus Documentos** todos os documentos gerados (aprovados ou não).

OBS.: No menu **Documentos** do Fluig, os relatórios serão gerados para a pasta designada anteriormente no GED.   
Neste menu, é possível somente a visualização de documentos já **aprovados**.   
No exemplo abaixo, foi designada a pasta **nova** como diretório.

## Atualizar Status do Documento

* Na tela de **Acompanhamento de Aprovações do Ponto** selecione os documentos para atualização do status;
* Selecione o processo **Atualizar Status do Documento**.

* O Sistema irá atualizar o status de todos os documentos selecionados.

## Excluindo um documento Exportado

* Na tela de **Acompanhamento de Aprovações do Ponto** selecione os documentos que deseja excluir;
* Selecione o processo **Excluir Documentos**.

* O sistema excluirá os documentos selecionados.

## Aprovação de Espelho de Ponto pelo Funcionário

* Após logar no portal acesse o módulo **Recursos Humanos | Meus Dados | Automação de Ponto | Aprovação do Ponto**.
* Selecione o período desejado e clique sobre **Editar**.

* Clique sobre o botão **Visualizar/Aprovar**. O sistema irá abrir a tela de exibição do documento no Fluig.

* Clique no botão **Aprovar Documento**. Insira a observação de aprovação e clique sobre o botão **Confirmar**.

* Após aprovação do documento, a janela de Visualização é fechada automaticamente. E este documento passa a ficar salvo no Fluig, na pasta selecionada no Gerenciamento do GED.
* Ao atualizar a visão da tela no portal, o campo **Status da Aprovação** é atualizado para **Aprovado**.
