---
content_hash: dfdaa835f23050224f4c82820fad7a439c1188ed3c17dc3188cba82f07c819eb
fetched_at: '2026-06-29T00:09:33.183629+00:00'
page_id: '425458933'
product: rm
source: tdn-rm
title: Novidades da versão 11.50
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458933
version: 1
---

**Novidades da versão 11.50**   
**Cadastros - Processo Seletivo**

* **Categorias do Processo Seletivo** No cadastro de processo seletivo foi implementado o campo "categoria do processo seletivo", ou seja, o cliente poderá criar as categorias em tabelas auxiliares e definí-las em seus processos seletivos. Este campo não é obrigatório.
* **Segurança no Processo Seletivo** No cadastro de Segurança do usuário/perfil, foi disponibilizada uma nova tabela de processo seletivo (SPSPROCESSOSELETIVO) no serviço de filtro (anexado) por usuário/perfil. Desta forma o cliente poderá definir que grupos de usuários/perfis terão acessos a quais categorias de processos seletivos. Por consequência disso, todas as tabelas e cadastros filhos/anexos do processo seletivo categorizado, terão a aplicação do filtro por usuário/perfil em suas consultas. Se o usuário/perfil não possuir este filtro, irá acessar todos os dados da filial logada como acontece atualmente.
* **Filtrar Processos Seletivos no portal** Foi Implementado a possibilidade de filtrar os processos seletivos no portal através do preenchimento da categoria na URL. Nos parâmetros do sistema no "Serviço - Gerar URL" quando necessário, basta selecionar a categoria e gerar a "URL". Ao acessar o portal do processo seletivo através do link será visualizado os processos seletivos da(s) categoria(s) utilizadas(s).
* **Forma de inscrição do Processo Seletivo com obrigatoriedade de preenchimento dos campos do ENEM** Implementada a validação da forma de inscrição com obrigatoriedade de preenchimento dos campos do ENEM. Se a forma de inscrição selecionada exigir o preenchimento de campos do ENEM e a área ofertada utilizar ENEM, então será obrigatório o preenchimento dos campos: Inscrição e Ano de referência do ENEM. Se a forma de inscrição selecionada exigir o preenchimento e a área ofertada NÃO utilizar ENEM, o usuário deverá alterar a forma de inscrição para conseguir finalizar sua inscrição.
* **Tornar o e-mail de confirmação de inscrição configurável por processo seletivo** Foi realizada a migração da configuração do envio de e-mail de confirmação de inscrição dos parâmetros do sistema para o cadastro do processo seletivo.
* **Cotas de Instituições Federais** Foi criado um anexo no cadastro do processo seletivo que permite a configuração do mesmo para utilizar sistema de cotas de acordo com a lei federal nº 12.711/2012. A partir dessas configurações, será exibido para o candidato no portal um grupo de campos adicionais para que opte se incluir ou não no sistema de cotas. No cadastro de inscrições pelo exe também será possível que o usuário, ao incluir/alterar uma inscrição, configure a inclusão do candidato no sistema de cotas.

**Cadastros - Área de interesse ofertada**

* **Testar geração de lançamento da Área ofertada** Implementado o Botão "Testar Geração de lançamentos" na aba informações financeiras da Área de interesse ofertada. Com o objetivo de testar a geração de lançamento de inscrições do processo seletivo utilizando a conta/caixa configurada na área ofertada.

**Cadastros - Atividades**

* **Colocar os horários de agendamento de atividades em ordem crescente** Os Horários da atividade agendada na inscrição foram ordenados em: dia, mês, ano e hora.
* **Intervalo de agendamentos** Foi Alterado o tempo mínimo do intervalo de agendamento de recursos (no processo de "Alocar recursos e horários para atividade agendada") para 1min com incremento de 1min.

**Inscrições - Inscrição**

* **Inscrição de candidatos estrangeiros no Portal do Processo Seletivo** Foram criados os seguintes parâmetros no sistema: - Nacionalidade do sistema: neste campo o cliente irá preencher o país de nacionalidade do sistema. Exemplo: Brasil, Argentina etc. - Obrigar preenchimento de passaporte para estrangeiros: neste campo o cliente irá definir se o preenchimento dos dados de passaporte serão obrigatórios para estrangeiros. - Utilizar parametrização dos campos de documentos sem exigir obrigatoriedade: neste campo o cliente irá definir se o sistema irá respeitar os campos de documentos que forão definidos para serem visualizados nos cadastros de responsáveis e candidatos, porém, se algum destes estiverem definidos como obrigatórios, exclusivamente para estrangeiros não serão obrigatórios. Se o cliente deixar este parâmetro desabilitado nenhum dos campos de documentos serão visualizados.
* **2ª Via de comprovante de inscrição: Texto "Local de realização de prova do candidato**" Ajuste na exibição do texto "Local de realização: O local de prova ainda não foi definido". Este texto será exibido somente se a área ofertada possuir etapa cadastrada e o candidato não esteja alocado.
* **Cancelamento/Exclusão de inscrições** A funcionalidade de cancelamento/exclusão de inscrições foram separadas para que a segurança de cada uma seja individual. Agora existem dois processos distintos para cancelamento ou exclusão da inscrição.
* **Processo "Alterar data de vencimento de lançamentos"** Implementado o processo de "Alterar data de vencimento de lançamentos" para inscrição do processo seletivo. Disponibilizado no cadastro de Inscrições do candidato como processo.
* **Cotas de Instituições Federais** Foi criado um anexo no cadastro do processo seletivo que permite a configuração do mesmo para utilizar sistema de cotas de acordo com a lei federal nº 12.711/2012.  No cadastro de inscrições aba informações complementares pelo exe também será possível que o usuário, ao incluir/alterar uma inscrição, configure a inclusão do candidato no sistema de cotas.

**Inscrições - Logs**

* **Visao do log de lançamentos com data de vencimento alteradas** Foi criado a funcionalidade de log de "Lançamentos com data de devolução alterada".

**Processos Administrativos**

* **Acrescentar tags no processo de envio de e-mail** Foi acrescentada as seguintes tags no processo de envio de e-mail: - Confirmacao de inscricao - Nome da atividade agendada - Data da atividade agendada - Horario da atividade agendada - Local de prova do candidato - Dia da prova - Horario da prova - Informações de prova

**Processos de Importação**

* **Layout de importação de notas do ENEM 2006/2008 ou 2009/2010** O sistema irá trabalhar com dois layouts, 2006/2008 ou 2009/2010. O modelo 2006/2008 oferece dois campos para nota da prova objetiva e Redação, enquanto que o modelo 2009/2010 discrimina as provas de Ciências da Natureza, Ciências Humanas, Linguagens e Matemática. No momento da importação, caso o layout 2009/2010 seja escolhido, o sistema realizará a média aritmética das quatro notas e gravará no campo "Nota Objetiva". Nele será considerado como 0 (zero) notas de provas em Branco, Anuladas ou Faltosos.

**Processos de Apuração**

* **Classificação de candidatos utilizando cotas federais.** Durante a classificação, se o processo seletivo trabalhar com cotas para instituições federais, para cada candidato serão processadas duas informações: "em qual grupo de cotas este candidato está inscrito?" e "qual a sua classificação interna deste grupo?" G1 – candidato egresso de escola pública, com RFP inferior ou igual a R$ 933,00 e que tenha se autodeclarado preto, pardo ou indígena; G2   candidato egresso de escola  pública, com RFP inferior  ou igual a R$  933,00 e que não  tenha se autodeclarado preto, pardo ou indígena; G3  candidato egresso de escola pública, com RFP superior a R$ 933,00 e que tenha se autodeclarado preto, pardo ou indígena; G4  - candidato  egresso de  escola pública,  com RFP superior  a R$  933,00  e que  não tenha  se autodeclarado  preto, pardo ou indígena; G5  –  candidato  da Ampla  Concorrência  e  candidato  que  tenha  optado  pela  Lei  de  Cotas,  mas  que  não  tenha  sido selecionado nas vagas de Ação Afirmativa, de acordo com as notas obtidas pelo candidato.
* **Chamada de candidatos utilizando cotas federais.** As vagas reservadas serão preenchidas segundo a ordem de classificação, de acordo com as notas obtidas pelo candidato, e levando em consideração sua classificação dentro de cada um dos grupos de prioridades inscritos: G1,G2,G3,G4,G5.

**Parâmetros do Sistema**

* **Processo de criptografar as senhas dos candidatos no banco de dados** Implementado o processo de criptografar as senhas dos candidatos no banco de dados. Estas serão criptografadas no momento em que os candidatos forem cadastrados. Os serviços "Esqueci minha senha", "Alteração de senha", "Login", "Inscrição pela secretaria" e "Envio de login" também foram adaptados.
* **Migração da integração do protheus de plug-in para solution** Migração da integração do protheus de plug-in para solution. Agora não será necessário a instalação em separado do Protheus para o funcionamento da integração. Para a integração acontecer, os seguintes passos entre os sistemas Classis/Fluxus e Protheus são necessários: - Parametrização da conexão com o banco de dados do Protheus: Localizado nos Parâmetros do sistema\ Integração. - Configurações financeiras de integração do Processo Seletivo: Localizado no Cadastro de processo seletivo >Anexo> Integração Protheus. - Validar se houvve importação: Para a integração entre os sistemas, os status disponíveis na tabela INT\_TITULO no campo TIT\_STATUSIMPORT são: 4- Em processamento (Executado o primeiro passo de importação) 1- Em processamento (Executado o segundo passo de importação) 2- Base do Protheus com os dados sincronizados com sucesso. 3- Houve erro durante a sincronização dos dados
* **Restrição de acesso aos dados pessoais** Para pessoas com papel no Corpore Rm foi alterada a regra dos serviços "Quero me inscrever" e "Dados pessoais". Quem possuir algum papel no Corpore (Professor, Funcionário, Aluno) não poderá ter seus dados alterados. O único dado que poderá ser editado é a Senha. Ou seja, quando o candidato logar no Portal de Inscrições e acessar o serviço Dados Pessoais, o sistema verificará se o mesmo é: - Aluno em algum dos Classis, - Professor em algum dos Classis com chapa cadastrada não demitido, - Funcionário do Folha (Labore) que não demitido. Se o usuário tiver algum destes papeis, o sistema bloquerá o acesso aos Dados Pessoais e informará ao candidato a causa. Esta informação pode ser customizada nos parâmetros do sistema.
* **Serviço de Gerar URL do Portal do Processo Seletivo** O serviço na tela de parâmetros que permite gerar a URL foi adaptado pelo fato da pasta EduPS-ProcessoSeletivo ter sido movida um nível acima para fora da pasta Edu-Educacional. Agora o link a ser gerado deve conter: <http://servidorinstitui>ção/Corpore.net/source/edups-processoseletivo
* **Gerar URL por Categoria no Portal do Processo Seletivo** Foi Implementado a possibilidade de filtrar os processos seletivos no portal através do preenchimento da categoria na URL. Nos parâmetros do sistema no "Serviço - Gerar URL" quando necessário, basta selecionar a categoria e gerar a "URL". Ao acessar o portal do processo seletivo através do link será visualizado os processos seletivos da(s) categoria(s) utilizadas(s).

**Campos Complementares**

* **Definir campos complementares por portal / secretaria** Foi implementado o controle de visibilidade dos campos complementares na tela de inscrição do candidato.

**Integração - Processo de Matrícula RM**

* **Integração dos documentos do candidato para o aluno do Classis** Implementado um serviço no TOTVS Processo Seletivo que disponibilizará informações referentes a documentos do candidato ao serviço de Matrícula do Processo Seletivo Rm do Classis. No momento de realizar a matrícula, o TOTVS Educacional utilizará estes dados para obter os documentos entregues do candidato e importar para o classis os documentos exigidos parametrizados por curso.
