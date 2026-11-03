---
content_hash: ba24eb098b4ecd85087e400910cd5216c93538b9aeb23d44e2828a27244e08df
fetched_at: '2026-06-29T00:10:06.999400+00:00'
page_id: '452719356'
product: rm
source: tdn-rm
title: Geração de Arquivo de CAGED
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719356
version: 13
---

falseATENÇÃO:

A partir da release **12.1.2606**, esta rotina foi descontinuada, pois sua funcionalidade passou a ser atendida pelo **eSocial**.

Através desse módulo será gerado o Cadastro Geral de Empregados e Desempregados – CAGED, criado pelo Governo Federal, através da Lei nº 4.923/65, que instituiu o registro permanente de admissões e dispensa de empregados, sob o regime da Consolidação das Leis do Trabalho - CLT.  
Este Cadastro Geral serve como base para a elaboração de estudos, pesquisas, projetos e programas ligados ao mercado de trabalho, ao mesmo tempo em que subsidia a tomada de decisões para ações governamentais.  
É utilizado, ainda, pelo Programa de Seguro-Desemprego, para conferir os dados referentes aos vínculos trabalhistas, além de outros programas sociais.  
Deve informar ao Ministério do Trabalho e Emprego todo estabelecimento que tenha admitido, desligado ou transferido empregado com contrato de trabalho regido pela CLT, ou seja, que tenha efetuado qualquer tipo de movimentação em seu quadro de empregados.  
O prazo de entrega é até o dia 7 do mês subseqüente ao mês de referência das informações.  
A omissão ou atraso da declaração sujeita o estabelecimento à multa automática. Neste caso, é necessário preencher o Documento de Arrecadação de Receitas Federais - DARF. Maiores esclarecimentos sobre multa, contatar Órgãos Regionais do MTE.  
O arquivo será gerado conforme layout fornecido pelo Ministério do Trabalho (MTE).  
Esse assistente é composto de 6 etapas pelas quais o responsável pela a geração dos arquivos passará, definindo a composição dos mesmos, de acordo com o layout. São essas etapas:

**ETAPA1 - Perfil de Parâmetros e Descrição do Processo**

Essa é a tela de abertura do assistente. Como o arquivo do CAGED possui uma composição de dados bastante complexa, esse módulo foi preparado para que pudessem ser gerados arquivos para cada uma das coligadas em apenas uma ou poucas execuções. O número de vezes que o assistente será executado dependerá, exclusivamente, das solicitações feitas pelo usuário, para cada uma das coligadas.  
Para otimizar essas execuções foi possibilitada a criação de perfis, que irão guardar a parametrização utilizada em cada uma dessas gerações. Além disso, é possível nomear o processo que está sendo executado caso o usuário queira,  agendar a criação do arquivo para outro momento. É nessa tela que se  inicia esse processo de criação de perfis e de nomeação de processos agendados relativos ao CAGED.

**Caixa "Perfil de Parâmetros"**

Essa caixa é composta de três itens:

**Nome do Perfil**

Esse é o local onde são criados novos perfis ou selecionados perfis criados anteriormente. Na primeira execução do assistente é obrigatória a criação de um perfil.

**Excluir**

Esse botão tem a finalidade de excluir um perfil que não é mais utilizado.

**Salvar perfil ao concluir**

Esse CheckBox tem a finalidade de indicar que o perfil que está sendo utilizado será modificado durante a execução do assistente e que tais modificações deverão ser gravadas. Ao utilizar um perfil sem a marcação

desse parâmetro, caso o mesmo seja modificado durante o processo, essas alterações não serão gravadas. Na criação de um novo perfil esse parâmetro deverá estar marcado.

**Caixa "Descrição do Processo"**  
Nesse campo poderá ser nomeado um processo caso a execução do assistente seja feita com o intuito de agendar a geração do arquivo para outro momento. Para entender melhor esse processo, leia o help da 7ª etapa do assistente (Agendamento do Processo).

**ETAPA 2 - Parâmetros**  
Nessa tela são definidos os parâmetros que serão utilizados para todas as coligadas selecionadas na 6ª etapa do assistente (Seleção de Coligadas).

**Quebra de Seção**  
Informe o código de quebra para o qual será emitido o relatório ou aceite o valor default (padrão).

**Observação1:**  
Para empresa com mais de um estabelecimento (mais de um CNPJ) e que desejar gerar o arquivo centralizado, deverá informar o código de quebra da seção com CNPJ principal de empresa.  
Caso desejar quebrar por CNPJ deverá informar o código de quebra para CNPJ, conforme informado em Opções | Parâmetros | Globais.

**Observação2:**  
Para que o sistema não considere as seções com encerramento de atividade na geração do CAGED, deverá marcar o campo "Desativada" em Cadastros | Seções | Identificação.

**Seleção de Funcionários**  
Aqui será definido qual o grupo de funcionários será informado no arquivo do CAGED.

**Observação**  
Essa seleção verifica a Situação, Tipo e Código de Recebimento atuais dos funcionários.

**Competência**  
Selecione mês e ano de competência para geração das informações.

**Identificação**  
Para a empresa que tem todas as seções identificadas apenas por CNPJ, deverá marcar a opção CNPJ.  
Para a empresa identificada pelo CNPJ, porém existe seção com CEI associado a este CNPJ, deverá marcar a opção CNPJ.  
Para a empresa identificada apenas por CEI, deverá selecionar a opção CEI e cadastrar o número do CEI que deverá ser levado na identificação da empresa.

**Convênio MTB**  
Informe o número do Convênio ou Autorizado registrado no Ministério do Trabalho.  
Caso não possua este número informe zeros ou o nome que será utilizado para salvar o arquivo do CAGED.

**Observação:**  
Conforme orientação do Ministério do Trabalhado, o número do Convênio ou código do Autorizado já não é mais necessário na declaração do CAGED, portanto ele pode ficar zerado. Porém quem o tem, pode continuar informando sem problemas.

**Localização do(s) arquivo(s):**

**Salvar o(s) arquivo(s) na pasta:**  
Selecione o caminho onde o sistema irá gerar o arquivo do CAGED, poderá utilizar a caixa de listagem ao lado.  
O sistema trará como default o disco local da máquina. Exemplo: C:\.

**Imprime apenas seções com movimentação**  
Caso este parâmetro esteja marcado, somente as seções que possuem movimentação no período informado no campo "Competência" serão consideradas.

**Gera registro para alteração de CEI**  
Com este campo marcado, o sistema irá gerar um registro de entrada e saída de funcionários transferidos para outro CEI, porém dentro do mesmo CNPJ.  
Lembrando que, esta opção somente será considerada caso a empresa utilize CEI, verifique em Opções | Parâmetros | Globais.

**Atenção:**  
O sistema verificará o histórico de seção do funcionário, sendo consideradas apenas as alterações de seção com CEI diferente, porém com o mesmo CNPJ.

**ETAPA 3 - Empresa**  
Nesta tela, deverão ser informados os dados da empresa (DDD, Telefone e Ramal) e se houveram alterações nos dados da empresa na competência de geração do arquivo.

**ETAPA 4 – Seleção de Coligadas**  
Nesta tela deverá ser realizada a seleção das coligadas para geração do arquivo. Será apresentada uma grade com as informações de Código de Coligada, Nome /Razão Social, CNPJ/CEI/CPF e Período. **Campos**

**Selecionar Todas Coligadas** Clique para selecionar todas as coligadas disponíveis na grade. **Cancelar Seleção de Coligadas** Clique para cancelar a seleção das coligadas disponíveis na grade. **Adicionar Parâmetros**

**Específicos** Clique em adicionar parâmetros à coligada para definir parâmetros específicos à coligada na geração do arquivo CAGED. **Usar Parâmetros Específicos** Ao marcar a opção, serão habilitados os demais campos da tela (Parâmetros da Coligada).

**Parâmetros da Coligada**

**Aba Geral**  
**Quebra de Seção**  
Informe o código de quebra para o qual será emitido o relatório ou aceite o valor default (padrão).

**Observação1:**  
Para empresa com mais de um estabelecimento (mais de um CNPJ) e que desejar gerar o arquivo centralizado, deverá informar o código de quebra da seção com CNPJ principal de empresa.  
Caso desejar quebrar por CNPJ deverá informar o código de quebra para CNPJ, conforme informado em Opções | Parâmetros | Globais.

**Observação2:**  
Para que o sistema não considere as seções com encerramento de atividade na geração do CAGED, deverá marcar o campo "Desativada" em Cadastros | Seções | Identificação.

**Seleção de Funcionários**  
Aqui será definido qual o grupo de funcionários será informado no arquivo do CAGED.

**Observação**  
Essa seleção verifica a Situação, Tipo e Código de Recebimento atuais dos funcionários.

**Imprime apenas seções com movimentação**  
Caso este parâmetro esteja marcado, somente as seções que possuem movimentação no período informado no campo "Competência" serão consideradas.

**Gera registro para alteração de CEI**  
Com este campo marcado, o sistema irá gerar um registro de entrada e saída de funcionários transferidos para outro CEI, porém dentro do mesmo CNPJ.  
Lembrando que, esta opção somente será considerada caso a empresa utilize CEI, verifique em Opções | Parâmetros | Globais.

**Atenção:**  
O sistema verificará o histórico de seção do funcionário, sendo consideradas apenas as alterações de seção com CEI diferente, porém com o mesmo CNPJ.

**Fórmula de horas semanais**  
Caso este campo seja preenchido, o resultado da fórmula terá prioridade sobre o cálculo interno utilizado pelo sistema. Caso contrário o sistema utilizará o calculo interno (jornada mensal dividido por 5).

**Fórmula para Remuneração**  
Caso este campo seja preenchido, o resultado da fórmula terá prioridade sobre o valor do campo "Salário" informado em Cadastros | Funcionários | Base Cálculo.

**Identificação**  
Para a empresa que tem todas as seções identificadas apenas por CNPJ, deverá marcar a opção CNPJ.  
Para a empresa identificada pelo CNPJ, porém existe seção com CEI associado a este CNPJ, deverá marcar a opção CNPJ.  
Para a empresa identificada apenas por CEI, deverá selecionar a opção CEI e cadastrar o número do CEI que deverá ser levado na identificação da empresa.

**Convênio MTB**  
Informe o número do Convênio ou Autorizado registrado no Ministério do Trabalho.  
Caso não possua este número informe zeros ou o nome que será utilizado para salvar o arquivo do CAGED.  
**Observação:**  
Conforme orientação do Ministério do Trabalhado, o número do Convênio ou código do Autorizado já não é mais necessário na declaração do CAGED, portanto ele pode ficar zerado. Porém quem o tem, pode continuar informando sem problemas.  
Se desmarcado, considera todos os funcionários da coligada em questão e utiliza Origem da Movimentação do Funcionário por Ficha Financeira.

**Observação:** Somente se este parâmetro estiver marcado, a parametrização determinada nesta, e nas demais pastas existentes nessa janela, será considerada na geração do arquivo para a coligada selecionada.

**Aba Empresa**  
Nesta tela, deverão ser informados os dados da empresa (DDD, Telefone e Ramal) e se houveram alterações nos dados da empresa na competência de geração do arquivo. **Seleção de funcionários** Ao clicar no botão de Seleção de funcionários o sistema abrirá uma janela com os campos onde você poderá selecionar um funcionário digitando sua chapa ou localizando seu nome, fazer a seleção de funcionários pela situação, tipo de funcionário e recebimento ou ainda criar Filtros ou Fórmulas de Seleção.

**ETAPA 5 - Centralizadores**  
Nesta tela, serão listados os CNPJ centralizadores da empresa, conforme a quebra informada no campo "Código de Quebra".  
   
\_Toc487548929**Rotina** **CAGED - Cadastro Geral de Empregados e Desempregados.**  
\_Toc487548930**Rotinas envolvidas**   
Parametrizador do SSO;  
Prontuário médico do SSO;   
\_Toc487548931**Parâmetro**  
Em RH / Segurança e Saúde Ocupacional / Parametrizador / Exames o parâmetro "Exame Toxicológico" deve ser informado.  
\_Toc487548932**Ponto de Entrada**  
Menu Folha de Pagamento / Encargos / CAGED   
\_Toc487548934**Requisito:**  
CAGED  
\_Toc487548935**Pré Requisito**  
O TOTVS Folha de pagamento Deverá estar integrado com o TOTVS Segurança e Saúde Ocupacional (Vitae) ambos da linha RM.  
   
Os funcionários que terão os novos campos acrescidos nos registros "C" ou "X" serão:  
   
1.       Os admitidos ou demitidos no Mês e;  
   
2.       Código do CBO PFUNCAO.CBO2002 igual a um dos códigos abaixo (somente números):   
2.1.     782310 - Motorista de furgão ou veículo similar;   
2.2.     782320 - Condutor de ambulância;  
2.3.     782405 - Motorista de ônibus rodoviário;   
2.4.     782410 - Motorista de ônibus urbano;   
2.5.     782415 - Motorista de trólebus;   
2.6.     782505 – Caminhoneiro autônomo (Rotas regionais e internacionais);   
2.7.     782510 - Motorista de caminhão (Rotas regionais e internacionais); e   
2.8.     782515 – Motorista operacional de guincho.  
   
3.       Observação: Caso a competência do CAGED não seja a Atual, deve verificar o Histórico de função para obter o CBO   
Nos registros C e X, para os funcionários que satisfaçam as condições acima, após o campo "CEP Residência do Trabalhador" deverá informar:  
Código Exame Médico, Data Exame Médico (DDMMAAAA), CNPJ LABORATÓRIO, UF DO MÉDICO e CRM DO MÉDICO.  
   
Porém para os funcionários que não possuem os CBO´s acima os campos devem ficar em branco com 51 espaços. Totalizando um filler de 81 espaços.  
   
Conforme o layout, os campos devem ser obtidos de acordo com a parametrização no módulo TOTVS Segurança e Saúde Ocupacional  
Foi criado o parâmetro "Exame Toxicológico" em RH / Segurança e Saúde Ocupacional / Parametrizador / Exames;  
   
Deverá lançar no "No Prontuário Médico" uma consulta para Admissão e ou Demissão, conforme o caso. E adicionar a esta consulta o exame toxicológico conforme código registrado no parâmetro RH / Segurança e Saúde Ocupacional / Parametrizador / Exames o parâmetro "Exame Toxicológico".  
   
**Os campos abaixo serão obtidos conforme as regras:**  
**Regra Geral:**  
Código do Exame realizado conforme o parâmetro do SSO "Exame Toxicológico" E;  
O funcionário possua o CBO já descrito acima E;  
Que o tipo de exame seja Admissional ou Demissional E;  
A data do Exame seja anterior a data de Admissão ou Demissão.  
   
**Referente ao exame:**  
Código Exame Médico  Campo: VEXAMESPRONT.CODEXAME;  
Data Exame Médico (DDMMAAAA) Campo: VEXAMESPRONT.DATAEXAME;  
CNPJ LABORATÓRIO Campo: VENTIDADES.CGCCPF;  
   
**Informação do médico referente a consulta:**  
UF do Médico Campo: VPROFISSIONALSAUDE.CODUFREGISTRO;  
CRM do Médico Campo: VPROFISSIONALSAUDE.NUMEROREGISTRO;   
   
Por se tratar de tabelas do SSO este deverá fornecer um serviço que recebendo a coligada, o código de pessoa, uma data e se Admissão ou Demissão deve retornar os campos Código Exame Médico, Data Exame Médico (DDMMAAAA), CNPJ LABORATÓRIO, UF DO MÉDICO e CRM DO MÉDICO.

**TOXICOLÓGICO quando a empresa utiliza seções identificadas por CEI**

Existe a situação onde o funcionário pode se recusar a realizar o exame toxicológico. Caso esta situação ocorra, dentro do cadastro do exame existe a possibilidade de marcar a flag "Recusou-se a realizar o exame toxicológico no desligamento".

Nestes casos o Manual do CAGED "Versão 01/2019 Brasília, DF – 20/02/2019" orienta que os seguintes campos devem ser informados:

* **Código:** RECUSA00000000000
* **Data da Coleta:**Data corrente
* **CNPJ do laboratório:** CNPJ da Empresa [Obrigatório]¹
* **CRM do médico responsável:**0000000001
* **UF do CRM do médico:** UF da Empresa

Preenchimento destas Informações

**Código**

O campo de 'Código do Laudo (Padrão DENATRAN), ficará habilitado para que o usuário possa preencher com a informação solicitada pelo CAGED.

**Data da Coleta**

Será considerado a data corrente, não sendo necessário o usuário preencher.

**CNPJ do laboratório**

* **Funcionário alocado em seção que é identificada por CNPJ**

 O sistema irá considerar o CNPJ cadastrado na seção do funcionário.

* **Funcionário alocado em seção que é identificada por CEI**

O manual do CAGED Versão 01/2019 Brasília, DF – 20/02/2019 orienta que no caso de empresas que utilizam CEI poderá informar o seguinte CNPJ: 23.612.685/0015-28.

Foi criado então uma tela de 'Parâmetros | |' na execução do CAGED permitindo que o cliente decida qual CNPJ será considerado.

Nesta nova tela o cliente deve marcar a flag 'Possui um ou mais funcionários alocados em seções identificadas por CEI e que se recusaram a realizar o exame na admissão’, após marcar serão habilitadas as flags:

* Considerar CNPJ Padrão
* Preencher CNPJ

  O cliente que desejar levar o CNPJ de acordo com o sugerido no manual deve marcar a primeira flag (Considerar CNPJ Padrão).

  O cliente pode também optar por digitar o CNPJ, desta forma deve marcar a segunda flag (Preencher CNPJ), e informar o CNPJ na caixa de Texto que será habilitada.

  Existem algumas validações desta tela que devem ser respeitadas:

* Quando a flag **‘Possui um ou mais funcionários alocados em seções identificadas por CEI e que se recusaram a realizar o exame na admissão’**, estiver marcada, deve obrigatoriamente marcar uma das duas opções '**Considerar CNPJ Padrão**' ou '**Preencher CNPJ**', ou não será possível avançar para a próxima tela;
* Quando a flag ‘**Considerar CNPJ Padrão**’, estiver marcada a flag ‘**Preencher CNPJ**’, será desabilitada;
* Quando a flag ‘**Preencher CNPJ**’, estiver marcada a flag ‘**Considerar CNPJ Padrão**’, será desabilitada;
* Quando a flag ‘**Preencher CNPJ**’, estiver marcada será habilitado uma caixa de texto para preencher o CNPJ;
* Quando a flag ‘**Preencher CNPJ**’, estiver marcada será obrigatório informar um CNPJ;
* O CNPJ informado deve ser válido ou não será possível avançar a tela;
* Se o parâmetro ‘**‘Possui um ou mais funcionários alocados em seções identificadas por CEI e que se recusaram a realizar o exame na admissão**’, estiver desmarcado não será necessário preencher nenhum dos demais campos, estes permanecerão desabilitados;

Prints demonstrando o funcionamento da nova aba

**CRM do médico responsável**

O campo 'Código do Médico' será habilitado, desta forma poderá preencher com o registro de um médico que possua as informações solicitadas no manual do CAGED.

**UF do CRM do médico**

O campo 'Código do Médico' será habilitado, desta forma poderá preencher com o registro de um médico que possua as informações solicitadas no manual do CAGED.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Execução de Scripts
