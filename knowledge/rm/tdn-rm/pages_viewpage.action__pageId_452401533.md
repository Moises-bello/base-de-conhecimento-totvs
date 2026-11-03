---
content_hash: cbdd79d433b341d2b43aee4cc746c609ad4a31503d433ae0244b5e5522c748c3
fetched_at: '2026-06-29T00:09:58.275158+00:00'
page_id: '452401533'
product: rm
source: tdn-rm
title: S-2221 - Exame Toxicológico do Motorista Profissional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452401533
version: 16
---

O envio do evento S-2221 tem a finalidade de registrar as informações relativas ao exame toxicológico realizado pelo motorista profissional.  
A obrigatoriedade desse evento é apenas para empregadores que possuam no quadro de funcionários motoristas profissionais do transporte rodoviário de passageiros e/ou do transporte rodoviário de cargas.

O prazo de envio deste evento, é até o dia 15 (Quinze) dias subsequente ao da obtenção do resultado. Porém, só será possível realizar este envio caso já exista na base do governo os eventos S-2200 ou S-2300.

Primeiramente, para geração do evento deve realizar a alteração da Versão do Leiaute para S-1.2 NT 04/2024 em Folha de Pagamento | Configurações | Parametrizador | Etapa eSocial | Configurações Gerais 1/7:

Atualmente existe algumas  possibilidades do envio deste evento S-2221 através do módulo "Segurança e Saúde Ocupacional | PCMSO"

* Prontuário Médico do funcionário
* Folha de Pagamentos nos Anexos do funcionário
* Assistente de Lançamento de Resultado de Exames
* Assistente de Importação de Resultado de Exames
* Agenda de Exames

Para a correta configuração do sistema a fim de possibilitar a geração do evento S-2221, o usuário deve realizar os passos abaixo:

##### **01)**  Cadastrar o Exame Toxicológico:

##### Segurança e Saúde Ocupacional | PCMSO | Exames

##### **2)** Definição de Motorista Profissional:

O gatilho para o evento S-2221, só será gerado caso o funcionário seja Motorista Profissional e essa definição se dá com base no CBO da Função do Funcionário.  
Essa informação do CBO deve ser informada no cadastro da função em Segurança e Saúde Ocupacional | Cadastro | Funções no campo "CBO 2002".  
Abaixo a lista de CBO's considerados:

* 782310 - Motorista de furgão ou veículo similar;
* 782320 - Condutor de ambulância;
* 782405 - Motorista de ônibus rodoviário;
* 782410 - Motorista de ônibus urbano;
* 782415 - Motorista de trólebus;
* 782510 - Motorista de caminhão (rotas regionais e internacionais) e
* 782515 - Motorista operacional de guincho.

##### **3 )** Realizar o cadastro de uma Entidade:

##### Gestão de Pessoas | Desenvolvimento | Entidades

##### **4)** Convênio

##### Segurança e Saúde Ocupacional | PCMSO | Convênios

Aqui é necessário também configurar os Períodos de Atendimento.

##### 5) Tipos de Atendimento

##### Segurança e Saúde Ocupacional | PCMSO | Tipo de Atendimento:

**Importante:** "O tipo de procedimento *Consulta para Exame Toxicológico*" será exibido apenas quando a flag "*Controlar o registro de Exames Toxicológicos no TOTVS Folha de Pagamento (Labore)*" não esteja marcada *(Item 7 deste documento)*.  Desta forma este passo não é necessário caso o controle dos registros seja realizado através da folha de pagamento.

Observação: Os exames toxicológicos serão custeados pelo empregador e realizados em três momentos:

* Antes da admissão (Admissional)
* Periodicamente (Periódico)
* Desligamento (Demissional)

##### **6)** Profissional de Saúde

##### Cadastros | Profissional de Saúde

##### **7)** Parametrização

##### Segurança e Saúde Ocupacional | Opções | Parametrizador | Exames | Exames Toxicológicos

Informar aqui o exame cadastrado para ser o exame toxicológico.

Ao marcar o parâmetro "Controlar o registro de Exames Toxicológicos no TOTVS Folha dePagamento” o controle de registro do exame toxicológico será realizado através do TOTVS Folha de Pagamentos no cadastro de Funcionários | Anexos | Folha de Pagamento | Exame Toxicológico. Caso o parâmetro esteja desmarcado, o controle de registro do exame toxicológico será realizado através do Prontuário Médico.

**Observação:** O sistema exibirá um aviso na tela confirmando a opção selecionada sempre que marcar ou desmarcar essa opção!

# **Pontos de Gatilho do Evento S-2221 no sistema**

* Anexo do Funcionário | Exame Toxicológico (Somente se o parâmetro de controle na Folha de Pagamento estiver marcado)
* Prontuário Médico (Somente se o parâmetro de controle na Folha de Pagamento **"NÃO"** estiver marcado)
* Assistente de Lançamento de Resultado de Exames
* Importação de Resultado de Exames
* Processo de Lançamento de Resultados de Exames da Agenda de Exames

##### > Anexo do Funcionário:

##### **Cadastro | Funcionários | Anexos | Folha de Pagamento | Exame Toxicológico**

Em seguida, ao incluir um novo registro selecione exame toxicológico e preencha com as informações conforme imagem abaixo:

**Atenção!**O campo "Código do exame toxicológico" deve ser um código válido, composto por 2 Letras e seguido de 9 números.

##### **> Prontuário Médico**

##### Segurança e Saúde Ocupacional | PCMSO | Prontuário Médico

##### > Assistente de Lançamento de Exames

##### Segurança e Saúde Ocupacional | PCMSO | Assistente de Lançamento de Exames

##### > Assistente de Importação de Resultado de Exames

##### Segurança e Saúde Ocupacional | PCMSO | Assistente de Importação de Resultado de Exames

##### > Processo de Lançamento de Resultados da Agenda de Exames

##### Segurança e Saúde Ocupacional | PCMSO | Agenda de Exames | Processos | Lançamento de Resultados de Exames

# **Geração do gatilho S-2221**

Todos os processos acima citados terão a geração de um gatilho na Fila de Eventos para o evento S-2221, se o funcionário possuir a função de motorista profissional.   
O usuário poderá visualizar os registros de eventos no TOTVS Folha de Pagamento | eSocial | Fila de Eventos.

 Veja mapeamento dos campos que serão informados:

 - Evento [S-2221](http://tdn.totvs.com/pages/viewpage.action?pageId=490980363).
