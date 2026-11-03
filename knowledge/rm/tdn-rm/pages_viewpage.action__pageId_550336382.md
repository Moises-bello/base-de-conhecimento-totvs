---
content_hash: c524d53dbff679e4f68076dc16110613fc61aaeb78ccbd3b0e7e70ee2f43a301
fetched_at: '2026-06-29T00:10:43.813645+00:00'
page_id: '550336382'
product: rm
source: tdn-rm
title: Taxa de Inscrição - SENAI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=550336382
version: 16
---

|  |  |
| --- | --- |
| Descrição | Processo Seletivo |
| Observações | Cobrança de Taxa de Inscrição |

Esta página se destina à explicação detalhada do processo de seleção de alunos com cobrança de taxa de inscrição. O diferencial de um *Processo Seletivo com Taxa* é de que o processo acontece por meio do pagamento da Taxa de Inscrição, ao candidato ao se inscrever.

**PREMISSAS:**

É necessário que já exista uma conta caixa

**Acesse**: Educacional | Processo Seletivo | Cadastros | Processo Seletivo / Venda Online de Cursos.

 Acesse a guia *Identificação| Valor da inscrição*

# Informações Financeiras

 Processo Seletivo | Informações Financeiras

Nesta aba são configuradas diversas informações utilizadas na integração com o Módulo Gestão Financeira. Os serviços do Módulo Gestão Financeira são necessários para inclusão de lançamentos financeiros, servindo de base para emissão e baixa de boletos da inscrição. Os lançamentos financeiros também são realizados para o pagamento de Fornecedores que tenham trabalhado em um determinado Processo Seletivo.

O campo “nosso número” pertencente ao lançamento e será gerado com base no *Id Boleto* (Código sequencial utilizado para gerar o campo nosso número).

“Informações Financeiras – Inscrições”, devem ser definidos os parâmetros para geração dos lançamentos e boletos de inscrição por meio da integração com o Módulo Gestão Financeira.

***Cliente/Fornecedor*** - Deve ser selecionado um registro de cliente a partir do cadastro de clientes/ fornecedores. Esse registro compõe o lançamento financeiro de cada uma das inscrições,

evitando a necessidade de se criar uma entrada no cadastro de clientes/fornecedores para cada um dos candidatos.

***Conta/Caixa*** - Identifica a conta corrente utilizada no processo de recebimento dos boletos. Ex: “Caixa Econômica Federal”.

***Tipo de Documento*** - Deve ser selecionado um tipo de documento a partir da lista de “Tipos de Documento” disponível. Um tipo de documento, é um registro que armazena uma série de parâmetros que caracterizam um lançamento financeiro. Uma das funções de um registro de “Tipo de Lançamento” é parametrizar o lançamento a ser feito, informando se ele é um lançamento “A pagar” ou “A Receber”. Para os lançamentos de inscrição devem ser usados tipos de registro a “A Receber”. Ex: “Recebimento de Taxas”.

Os tipos de documentos tratados aqui não devem ser confundidos com os tipos de documentos presentes na tabela auxiliar documentos.

***Moeda*** - Moeda corrente utilizada na geração dos boletos. Ex: “Real”.

***Histórico***: Informação textual que compõe o campo histórico dos lançamentos.

***Testar geração de lançamento*** - Através deste recurso, é possível simular uma geração de lançamento para a inscrição, verificando se os parâmetros financeiros configurados são válidos, segundo as regras do Módulo Gestão Financeira. Após a simulação do lançamento, uma mensagem informará se a configuração é válida ou se houve algum erro, informando o motivo.

***Disponibilizar pagamento de cartão de crédito no portal*** - Este parâmetro tem como objetivo, permitir que os candidatos do processo seletivo possam efetuar o pagamento da inscrição através do portal utilizando cartão de crédito. O pagamento ficará disponível nos serviços de Impressão após a inscrição do candidato e em 2ª via de boleto e será exibido um ícone, possibilitando ao usuário clicar na tela para informação dos dados de cartão de crédito, caso o processo seletivo esteja configurado. Caso contrário, será exibido somente o código IPTE do boleto e a opção de impressão do boleto.

Importante: Para realizar o pagamento da inscrição via cartão de crédito é preciso que seja parametrizado no RM Fluxus as configurações do cartão de crédito.

***Gerar lançamentos /boletos com registro online*** - Este parâmetro tem como objetivo permitir aos candidatos a impressão do boleto de inscrição registrado.

***Apresentar boleto de cobrança registrada ainda não registrado no Portal*** - Este parâmetro tem como objetivo permitir que os boletos provenientes de convênios com cobrança registrada sejam impressos, mesmo que os boletos não tenham sido registrados.

Os tipos de documentos tratados aqui não devem ser confundidos com os tipos de documentos presentes na tabela auxiliar Documentos.  
Esse campo, fica visível após “salvar” todo o cadastro do processo seletivo.

* Filial do Lançamento - Filial que irá realizar os lançamentos.
* Departamento do lançamento  - Departamento da filial (Unidade Operacional) responsável pelos lançamentos.
* Centro de Custo: Identifica o centro de custo que é o responsável pela receita gerada com as inscrições.
* Tipo Contábil - Define o status contábil do lançamento que será criado. As opções disponíveis são: “Não contábil”, “Contábil”, “Baixa contábil” e “A contabilizar”.
* Evento Contábil de inclusão” - Identifica o registro contábil que será gerado em decorrência do lançamento de inscrição.

# Baixa manual do boleto de inscrição

TOTVS Processo Seletivo |Selecionar o Processo Seletivo desejado| Anexo| Candidato Inscrito

Selecionar o aluno que terá a taxa baixada manualmente | Guia Inf. complementares

Clicar no numero do lançamento, (você será direcionado para o modulo do BACKOFFICE Financeiro) neste momento o usuário deverá seguir a baixa do lançamento;

Clicar em Processo| Baixa| Baixa de Lançamentos  neste momento o DR deve agir de acordo com as orientações do Financeiro e Contabilidade da unidade.

Neste momento o DR deve agir de acordo com as orientações do Financeiro e Contabilidade da unidade.
