---
content_hash: b0c7a895bdeee33d407592763a78f63ef0244c53d92bb06b708405289c9b3d92
fetched_at: '2026-06-29T00:10:03.885187+00:00'
page_id: '452719169'
product: rm
source: tdn-rm
title: Parametrizador - SMT
type: documentation
url: https://tdn.totvs.com/display/LRM/Parametrizador+-+SMT
version: 6
---

**Parametrizador**

---

O Assistente de Implantação de Processos é destinado à definição dos parâmetros do Totvs Segurança e Saúde Ocupacional, e está disponível:

Na nova MDI: Opções-> Parametrizador.

No executável: Opções-> Parâmetros-> RM SSO.

**Iniciando a parametrização do sistema:**  
Na primeira tela do processo, clicar no botão: Avançar.  
Na segunda tela estão disponíveis para configuração os processos listados abaixo:

**Parâmetros referentes a CIPA**  
**Cargo Reservado para Funções da CIPA**

Através do loookup será possível informar o cargo reservado para funções da CIPA. Somente as funções vinculadas a esse cargo serão visualizadas no cadastro de CIPA.

**Usa convenção CIPA**

Selecionando esta opção poderão ser definidos períodos superiores a 1 (um) ano para vigência da CIPA. Após selecionar esta opção, deverá ser informado no campo "Período de validade da CIPA (em anos)" qual será o período a ser considerado.

**Período de Validade de CIPA (em anos)**

Neste parâmetro serão informados os anos de validade da CIPA, o mesmo só será habilitado após a marcação do parâmetro: "Usa convenção CIPA".

**Só permitir vincular funcionários para CIPA**  
Marcando esse parâmetro, nas Reuniões da CIPA (COMISSÃO DA CIPA > REUNIÕES) será possível incluir apenas participantes que sejam funcionários nos anexos da Reunião da Comissão da CIPA.  
Com o parâmetro desmarcado, todas as pessoas poderão ser participantes da reunião e não apenas funcionários.

**Permitir Candidatos/Representantes com situação de afastamento**

Marcando esse parâmetro será possível que empregados afastados participem das eleições da CIPA como candidatos.

**Parâmetros referentes a Equipamentos de Proteção Coletiva (EPC):  Extintores e Brigada de Incêndio:**

**Cargo Reservado para Funções da Brigada de Incêndio**

Através do lookup será possível informar o cargo reservado para funções da Brigada de Incêndio. Somente as funções vinculadas a esse cargo serão visualizadas no cadastro de Brigadas de Incêndio.

**Periodicidade de alteração do status do EPC para "Requer Atenção" (em dias)**

Definir neste campo os dias desejados para que seja alterado o status do EPC para "Requer Atenção" conforme cadastro do mesmo.

**Parâmetros referentes a EPI**

Nesta tela o usuário deverá informar o tipo de integração do sistema, escolhendo uma das três opções:

**Sem Integração: Não fará controle do estoque de EPI**  
Todo cadastro de EPI será executado pelo Totvs Segurança e Saúde Ocupacional.  
   
**Integração com RM Nucleus**

O controle de EPI será feito através do Totvs Gestão de Estoque, Compras e Faturamento. Após selecionar esta opção, será necessário selecionar o Tipo de Movimento a ser utilizado; Informando a Integração com RM Nucleus, o sistema habilita o cadastro para os tipos de movimento a serem utilizados na integração com o Totvs Gestão de Estoque, Compras e Faturamento.

Tipos de movimentos: "Tipo de Movimento Entrada", "Tipo de Movimento Transferência", "Tipo de Movimento Baixa(Invalidar)", "Tipo de Movimento Empréstimo", "Tipo de Movimento Descarte", "Tipo de Movimento Devolução".  
Tipo de movimentos descartáveis: "Tipo de Movimento Empréstimo", "Tipo de Movimento Devolução".

**Integração com sistema externo**

O controle será feito através de um sistema externo, com as informações importadas para o Totvs Segurança e Saúde Ocupacional através de XML.

Consulta SQL padrão para importação de empréstimo de EPI: campo para informar a consulta SQL padrão para ser utilizar no processo de importação de fornecimento. Um exemplo pode ser encontrado na página [Importação de Fornecimento](http://tdn.totvs.com/pages/viewpage.action?pageId=452719512).

**Relatório SQL padrão p/ Importação de Empréstimo de EPI**

Para que o relatório apareça neste campo é necessário que este seja do tipo SSO (183).

**Parâmetros referentes a Exames**

**EXAMES I**

**Grupo de Entidades para Exames**

Através do lookup será possível informar o Grupo da Entidade para Exames que será utilizada como padrão para realização do Agendamento Automático de Exames.

**Entidade Padrão Para Inclusão de Exames no prontuário**

Através do lookup será possível informar a Entidade que será utilizada como padrão para inclusão de exames.

Definindo este parâmetro, ao incluir um exame para um funcionário através de Cadastros| Funcionários| Anexos| Segurança e Medicina| Consultas Realizadas | Anexos | Exames Realizados ou através de Segurança e Saúde Ocupacional | PCMSO| Exames | Assistente para Lançamento de Exame, será exibido no campo "Entidade" a mesma entidade definida neste parâmetro.

**Atenção!**

A Entidade selecionada já deve estar previamente cadastrada como Convênio para os exames no menu Segurança e Saúde Ocupacional | PCMSO| Exames| Convênios.  
   
**Ordenar alfabeticamente as informações clínicas no cadastro de consultas, aba "Exames Realizados" da pessoa?**

Marcando esta opção, ao editar um exame realizado no prontuário médico de uma pessoa, as informações clínicas vinculadas ao mesmo estarão apresentadas em ordem alfabética.

**Obrigatório Filtro de Perfil de Exames para Prontuário**

Marcando este parâmetro, deverá ser criado nos Perfis de Acesso de Funcionários, um filtro para validar quais os exames serão disponibilizados para inclusão e edição no prontuário das pessoas (pasta - Situação Clínica).

**Exame Audiométrico**

Através do lookup será possível informar o exame que será utilizado como o "Exame Audiométrico" no prontuário dos funcionários.   
Ao informar um exame nesse campo as Informações Clínicas necessárias para a emissão do Gráfico Audiométrico serão automaticamente associadas ao referido exame.  
   
**Exame Avaliação Física**  
Através do lookup será possível informar o exame que será utilizado como o "Exame de Avaliação Física" no prontuário dos funcionários.

Ao informar um exame nesse campo as Informações Clínicas necessárias para o reconhecimento das informações serão automaticamente associadas ao referido exame.

**Atenção!**

O preenchimento desse campo é imprescindível para que seja disponibilizada a pasta "Audiometria" (para o exame audiométrico) no prontuário dos funcionários, o que irá possibilitar o preenchimento dos campos e consequentemente a geração do Gráfico AudiométricoIDH\_viDGraficoAudiometrico.

**EXAMES II**

**Consulta admissional**

**Associar chapa do funcionário admitido à consulta da pessoa sem chapa**

Se existir uma consulta admissional sem chapa preenchida, dentro do prazo definido no campo "**Dias retroativos a considerar para a pesquisa de consulta admissional sem chapa**", o sistema atualizará a consulta da pessoa com a chapa.

**Dias retroativos a considerar para a pesquisa de consulta admissional sem chapa**

Número de dias retroativos a considerar entre a data de admissão e a data da consulta admissional da pessoa.

**Exemplo 1:**

Dias retroativos a considerar para a pesquisa de consulta admissional sem chapa : 10

Data da consulta admissional da pessoa: 01/09/2011

Data Admissão Funcionário: 10/09/2011

Após admitir o funcionário, o sistema preenche a consulta admissional com a chapa do funcionário admitido

Consulta antes da admissão:

Consulta após a admissão.  
O campo CHAPA foi preenchido automaticamente porque a diferença de dias entre a data de admissão e a data da consulta admissional é menor ou igual à quantidade de dias definida no parâmetro.

**Exemplo 2:**

Dias retroativos a considerar para a pesquisa de consulta admissional sem chapa : 10

Data da consulta admissional da pessoa: 01/09/2011

Data Admissão funcionário: 15/09/2011

Após admitir o funcionário, o sistema não preenche a consulta admissional com a chapa do funcionário admitido  porque a diferença de dias entre a data de admissão e a data da consulta admissional é maior que a  quantidade de dias definida no parâmetro.

**EXAMES TOXICOLÓGICOS**

**Exame Toxicológico**  
Através do lookup será possível informar o exame que será utilizado como o "Exame Toxicológico" no prontuário dos funcionários.

**Atenção!**

O preenchimento desse campo implica que o exame informado aqui não aparece nos relatórios ASO e PCMSO, conforme instruções do Ministério do Trabalho.

**Controlar o registro de “Exames Toxicológicos” no Totvs Folha de Pagamento (Labore):**

Marcando esse parâmetro o exame toxicológico passa a ser exibido no anexo do Cadastro de Funcionários em: Funcionários | Anexos | Folha de Pagamento | Exame Toxicológico e deixa de ser apresentado no prontuário do funcionário.

**Margem de dias a considerar no lançamento de resultados pela agenda de exames**  
Parâmetro onde pode ser definido a quantidade de dias que o sistema vai utilizar como margem para considerar o agendamento como "realizado", após o Lançamento de Resultado de Exames. Por padrão, este parâmetro terá o valor de 7 dias.  
   
Exemplo de utilização:  
Parâmetro = 10 dias  
Agendamento = 31/05/2016  
Lançamento do exame = 14/06/2016  
Sistema lança o exame, mas na Agenda de Exames a situação continua como Pendente.  
   
Parâmetro = 10 dias  
Agendamento = 13/06/2016  
Lançamento do exame = 14/06/2016  
Sistema lança o exame e na Agenda de Exames a situação é alterada para Realizado.  
   
**Utilizar "Associação PPRA" como origem na geração de exames pendentes**

Parâmetro onde pode ser definido se os exames pendentes serão gerados a partir da Associação no PPRA - PCMSO| Assist. Associação de PCMSOxPPRA (Risco ou Nível de Risco, Reconhecimento e Avaliação de Risco, Pessoa).  
Se o parâmetro estiver desmarcado, os exames pendentes serão gerados a partir da Associação de Perfis de Exame - PCMSO| Assist. Associação de Perfil (Função, Seção e Lotação).  
   
**Atenção!**

A partir da mudança deste parâmetro, todos os exames pendentes serão gerados a partir destas definições. Os exames pendentes já gerados serão mantidos. - Alterando o parâmetro, também deve ser revisto o relatório do PCMSO. O mesmo deve ser importado e o processo "Gerar modelo de PCMSO" deve ser executado novamente.   
   
**Parâmetros referentes a Profissiografia**  
   
**Profissiografia**  
Todos os parâmetros de "Exibir profissiografia por:" do relatório PPP disponíveis para serem marcados como DEFAULT dentro de Profissiografia.  
   
**Observação:**  
No relatório PPP ainda há a possibilidade de acesso para alterar estes parâmetros, contudo eles são apresentados inicialmente obedecendo a configuração DEFAULT do parametrizador.

**Parâmetros referentes a Ambiente de Trabalho**  
   
Conjunto de configurações onde o usuário define como será o formato da Máscara que irá preencher o campo "Código" automaticamente no Cadastro do Ambiente de Trabalho.   
A máscara é definida pela junção dos caracteres dos 3 campos abaixo:   
**Prefixo:** é opcional e seu tamanho mínimo é 1. Por default este campo vem desabilitado e com valor 0. Para habilitar é necessário marcar a opção 'utilizar prefixo'. Marcando esta opção, o campo prefixo referente ao código do prefixo fica habilitado para edição. Somente é permitido preencher este campo com o mesmo tamanho da quantidade de caracteres informada. Ele também pode ser preenchido com valores alfanuméricos.  
**Coligada:** O campo tem o tamanho mínimo de 3 caracteres sendo que um deles recebe a Letra C. Caso a base tenha alguma coligada onde seu código tem tamanho maior que 3, este campo deverá ser preenchido com o valor equivalente à quantidade mínima de caracteres do código da coligada mais um. Exemplo: A Coligada X possui o código 9999, então o campo deve ser preenchido com o valor mínimo de 5.    
**Sequencial:** O campo recebe o tamanho mínimo 7, sendo que um caractere é reservado para a letra S.   
Exemplo:   
Utiliza Prefixo: X  
Prefixo: 1   
Coligada: 3  
Sequencial: 7  
Nesse exemplo a máscara seria: XC99S999999  
   
   
**Descrição:** Descrição do Ambiente de Trabalho que será enviado ao eSocial  
   
Após a definição dos parâmetros, o sistema exibe na última tela do assistente a opção de finalização através do botão: "Concluir".
