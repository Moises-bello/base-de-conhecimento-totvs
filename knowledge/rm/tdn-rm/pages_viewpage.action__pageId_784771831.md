---
content_hash: dd48c68be2e25a9a0340f8637c88f1c5f40d577e46fc49ac1b96d7f61942d909
fetched_at: '2026-06-29T00:11:38.352147+00:00'
page_id: '784771831'
product: rm
source: tdn-rm
title: 01.02 Parâmetros financeiros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=784771831
version: 15
---

Ao utilizar a opção de geração de contrato o candidato ou seu responsável financeiro serão utilizados para geração do cliente/fornecedor, porém, antes é feito uma busca para validar a existência de um cliente/fornecedor com os mesmos dados, sendo assim o sistema irá filtrar somente cliente/fornecedores que estejam ativos no TOTVS Gestão Financeira. 

**Sobre a Flexibilização do Plano de Pagamento [Clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=728646916) (disponível a partir da versão 12.1.2302).**

Importante

Para planos de pagamento que contenham parcelas em que a cobrança é feito por créditos, é necessário que seja informado uma turma na aba "Acadêmicos", caso não seja informado uma turma ou essa turma não possua disciplinas com as definições corretas de créditos, o plano de pagamento não será exibido na central de candidatos.

RA Global

Se o TOTVS Educacional estiver parametrizado (Parâmetros >> Secretária >> Geral 1/6) para utilizar RA Global, e a opção “Candidato que já são alunos" estiver definida para aproveitar o RA existente, será verificando se o aluno já está cadastrado em outras coligadas e caso o aluno já exista em outra coligada o RA do aluno será preservado/reaproveitado.

Se a coligada da matricula do processo seletivo for diferente da coligada que o aluno já possui outra matricula, e o responsável financeiro já definido no aluno não for global, será gerado um novo cadastro para o responsável financeiro na coligada em que a matricula está sendo efetivada.

É importante ressaltar que se o responsável financeiro for global a coligada em que a matricula está sendo efetivada deve estar com o TOTVS Gestão Financeiro parametrizado para permitir cadastros de cliente como global.

Responsável financeiro para candidato que já é aluno

Para que um candidato que já é aluno, possa ter seu responsável financeiro efetivamente alterado, quando a matrícula estiver parametrizada para utilizar o RA existente, é preciso que o parâmetro "Substituir responsável financeiro quando utilizar RA existente" esteja habilitado. Desta forma o aluno terá o novo responsável financeiro cadastrado para o contrato e para os próximos a serem firmados. Os contratos já existentes permanecerão com o responsável financeiro cadastrado anteriormente.

Relatório do Contrato

Na execução do relatório será passado parâmetros com informações do contexto selecionado pelo candidato, para que estes dados sejam utilizados crie os parâmetros abaixo nos relatórios:

Nome dos parâmetros:

**CODCOLIGADAPARAM**: código da coligada do contexto.  
**CODFILIALPARAM** : código da filial do contexto.  
**CODTIPOCURSOPARAM**: código do nível de ensino do contexto.

**CODUSUARIOPSPARAM**: código do usuário do Processo Seletivo.  
**IDPERLETPARAM**: identificador do período letivo.  
**IDHABILITACAOFILIALPARAM**: identificador da matriz aplicada.  
**IDPSPARAM**: identificador do processo seletivo.

**NUMEROINSCRICAOPARAM**: número de inscrição do candidato.

Obs.: Os relatórios não precisam ter obrigatoriamente os parâmetros citados.

Avisos importantes para a criação do relatório

* Os relatórios para a matrícula via central do candidato, **NÃO DEVEM** ser parametrizados com provedores.
* Nesse momento da matrícula, o candidato ainda não possui RA, somente os parâmetros acima estão disponíveis para consulta no relatório.
* Relatórios criados especificamente para matrícula no TOTVS Educacional, **NÃO DEVEM** ser utilizados para a matrícula via central do candidato, pois, os parâmetros disponibilizados são diferentes.
Parâmetro: Somente o responsável financeiro pode aceitar o contrato

Disponível a partir da versão 12.1.2402

O novo parâmetro poderá ser habilitado apenas se forem atendidas as seguintes condições:

* O usuário selecionar a opção Cadastrar Contrato.
* O usuário informar um relatório para a assinatura do contrato.
* O usuário marcar uma das opções **Responsável Financeiro = Próprio Aluno**; **Utilizar token para validação da assinatura do contrato**.
* O parâmetro **Utilizar TOTVS Assinatura Eletrônica para assinatura do contrato** estiver desmarcado.

Caminho: **Processo Seletivo** > **Área de interesse ofertada** > **Matrícula** > **aba Financeiro**

### Processo de Aceite com Token na Central do Candidato

Para mais informações [clique aqui](https://tdn.totvs.com/display/public/LRM/02.06+Assinatura+do+contrato).

#### Parâmetro Ativado

Quando o parâmetro **"Somente o responsável financeiro pode aceitar o contrato"** estiver ativado, na etapa de assinatura do contrato, será necessário que o usuário solicite um token para realizar o aceite. Nesse caso:

* O sistema enviará o e-mail contendo o token **exclusivamente para o responsável financeiro da matrícula**.
* A matrícula deve obrigatoriamente possuir um responsável financeiro cadastrado para que o processo de aceite seja concluído.

#### Regras Adicionais:

1. **E-mails distintos**:
   * Caso o responsável financeiro não seja o próprio candidato ou o responsável pela inscrição, o e-mail cadastrado para o responsável financeiro **não pode ser o mesmo** do candidato ou responsável pela inscrição.

#### Parâmetro Desativado

Se o parâmetro **"Somente o responsável financeiro pode aceitar o contrato"** estiver desativado:

* O sistema continuará enviando o e-mail com o token para o e-mail do candidato ou do responsável pela inscrição, conforme configurado previamente.
