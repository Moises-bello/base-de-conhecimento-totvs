---
content_hash: dcaf964d3eb810d107414424fd22ec46bd71345a27b413d451acf89f930525e0
fetched_at: '2026-06-29T00:11:04.609290+00:00'
page_id: '627995679'
product: rm
source: tdn-rm
title: Rascunho_EDU0009 - Cadastro de Ativos e Lançamento a Receber
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=627995679
version: 47
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Totvs Educacional - Fluig - Protheus |
| **Versões:** | 12.1.9 |
| **Ocorrência:** |  |
| **Ambiente:** | SQL |
| **Passo a passo:** | **Cadastro de Ativos e Lançamentos a pagar  – Integração Protheus**  Descrição  Foi disponibilizado através do pacote de integração "TOTVS Educacional x BackOffice Protheus" a sincronização de cadastro de Ativos Fixos (Patrimônio) realizados no sistema Protheus, e também foi disponibilizado o envio de lançamentos a pagar para o sistema Protheus através de Mensageria Única.  **Cadastros que são precisos para integração de Ativos e lançamentos a Receber - Protheus - Fluig e RM**   * **Plano de contas** * **Centro de Custos** * **Fornecedor** * **Banco e Agência** * **Natureza Financeira**       Adapter do Cadastro de ATIVO ( Assets )        Enviando Plano de Contas                Enviando Centro de Custos        Fornecedor cadastrado no Protheus -        Fornecedor enviado para o RM        Cadastro de Banco com Agência no Protheus        Enviados dados bancários para o RM        Cadastrada Natureza Financeira no Protheus        Natureza Financeira enviada para o RM.        Editar o cadastro do Fornecedor no RM - Dados Adicionais        Rateios > Centro de Custos        Inserida a Natureza e centro de custo.  Cadastros importados do Protheus      Anexo > Defaults de Cli/For        Inserida a Filial e Tipo de Documento        Anexos > Dados Bancários        Default de Dados Bancários - Tem que ser inserido , se não for inserido , não será enviado via mensageria os dados Bancários no Lançamento.        Banco ITAU inserido como Default        Inserido os dados do banco enviado pelo Protheus        Logar no Fluig com usuário – Permissão de visualizar o Cadastro de proposta de pesquisa        Processos > Iniciar Solicitações        Cadastro de proposta de pesquisa  Cadastro de Ativos no RM        BackOffice > Gestão Patrimonial        Patrimônio        Mensagem processada        Patrimônio enviado para o RM        Verificar cadastro do Patrimônio no FLUIG        Marcar - Incluir Itens de Patrimônio.  Patrimônio enviado para o FLUIG      **Teste.. lançamento a Pagar – Fluxo Fluig**      Usuário : helysson  - Usuário que irá fazer solicitação do lançamento        Vinculado ao : Henrique Neves Gomes        Verificar o cadastro do Pesquisador / Extensionista        Localizado o : Henrique Neves Gomes        Clicar sobre o nome de Henrique para entar em seu Cadastro da PESSOA        Usuário vinculado a Henrique – Helysson – ( Usuário do Fluig )        Processos > Vincular / Desvincular Cli/For  Vinculado fornecedor ao Henrique . que foi enviado pelo Protheus        Fornecedor vinculado        Vinculado o Fornecedor cadastrado no Protheus        Iniciar o processo  Iniciar Solicitações        Acompanhamento de Bolsista        Movimentar            Logar com usuário Franciel no FLUIG para que possa se liberar o Pagamento solicitado pelo usuário Helysson        Central de Tarefas        Localizar a Tarefa e clicar em seguida        Staus : Aprovado e inserir uma Justificativa        Solicitar Pagamento        Em seguida: Coordenador de Pesquisa        Usuário Franciel : Assumir a Tarefa para dar prosseguimento ao processo do Lançamento a pagar        Movimentar        Inserir o Parecer e em seguida : Movimentar        Realizar pagamento Interno  > Movimentar em seguida        Finalizada Solicitação        Lançamento gerado para o Fornecedor            Mensagem levando o código do lançamento        Titulo enviado para o Protheus      Att,    Adriano Astoni Ferreira |
| **Observações:** |  |

divs
