---
content_hash: b4f7b51e60181dbe85cbb4a75a574f4e99cd6b4b3882c331c1eda4e59e549c1e
fetched_at: '2026-06-29T00:11:02.657695+00:00'
page_id: '61933668'
product: rm
source: tdn-rm
title: RMCTB00010_SPED 2013 - Correção dos erros apresentados na validação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=61933668
version: 7
---

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Produto** | | : | | TOTVS Gestão Contábil – **Versão:** 11.52 | |
| **Processo** | | : | | SPED Contábil | |
| **Subprocesso** | | : | | Listagem e correção dos erros apresentados na validação | |
| **Data da publicação** | | : | | 24/01/2014 | |

**Advertências na Validação do SPED**

Durante a validação do SPED o Validador da Receita poderá apresentar Erros e Advertências, impossibilitando a validação do arquivo.  
Sendo assim, segue abaixo orientações pertinentes à correção dos principais erros e advertências apresentadas durante a validação.

**Desenvolvimento/Procedimento**

**TAMANHO DO CAMPO INVÁLIDO.  9 - COD\_MUN**

É orientado acessar ‘Opções’ / ‘Parâmetros’ / ‘RM Saldus’ / ‘Rotinas Legais’ / ‘SPED Contábil’ / e informar no campo ‘Classificação do Município (IBGE)’ o código '1 - IBGE'.  
Obs.: O registro em questão é cadastrado no menu ‘Cadastros’ / ‘Classificação de Municípios’

**CÓDIGO DA INSTITUIÇÃO NÃO ENCONTRADO NA TABELA DE INSTITUIÇÕES RESPONSÁVEIS PELA ADMINISTRAÇÃO DO CADASTRO DAS ENTIDADES**

Acesse ‘Rotinas Legas’ / SPED Contábil’ / ‘Outras Inscrições Cadastrais’:

* Caso a sua empresa possua alguma Instituição que irá ter acesso aos seus livros além da Receita Federal ela deverá ser cadastrada nesse menu. O ‘Código Cadastral’ dessa Instituição é obtido com a Receita Federal e a filial deve ser a matriz (a qual o SPED está sendo gerado).

Caso a sua empresa não possua nenhuma outra Instituição que irá ter acesso aos seus livros além da Receita Federal, você deverá indicar em INSTITUIÇÃO a opção “00 – Sem inscrição em Secretarias de Fazenda Estaduais”, o ‘Código Cadastral’ deve ser 0000 e a filial a matriz (a qual o SPED está sendo gerado).

**TAMANHO DO CAMPO INVÁLIDO.  7 - NIRE**

É necessário revisar o cadastro da Filial, informando/preenchendo os campos solicitados na guia ‘Dados Adicionais’ (exemplo: Número de Registro na Junta Comercial)

Obs.: ‘Cadastros’ / ‘Filiais’ / edite a filial informada na geração do SPED.

Na guia ‘Dados Adicionais’ da filial (matriz ou filial informada no SPED) verifique o campo ‘Nro. Registro na Junta Comercial’ esta deve conter 11 dígitos. 

Obs.: A informação em questão encontra-se no razão social da empresa.

**CAMPO OBRIGATÓRIO NÃO PREENCHIDO - REGISTRO I030 – NIRE**  
É necessário acessar o cadastro da Filial e informar o campo ‘Nro. Registro na Junta Comercial’ (guia ‘dados adicionais’).

Obs.: ‘Cadastros’ / ‘Filiais’ / edite a filial informada na geração do SPED.

**CAMPO OBRIGATÓRIO NÃO PREENCHIDO - REGISTRO I075 - DESCR\_HIST**

Essa inconsistência é apresentada devido ao não preenchimento do campo ‘Descrição’ do ‘Histórico Padrão’ informado na ‘Transferência de Grupos Contábeis’.  
Nesse caso, é orientado acessar ‘Cadastros’ / ‘Históricos Padrões’ / filtrar o Histórico em questão e definir a ‘Descrição’ do Histórico.  
Vale ressaltar que a Transferência de Grupos Contábeis deve ser executada com um ‘Histórico de Fechamento’ novo. Ou seja, cada encerramento do exercício deverá ter um histórico diferente.

**CONTA DE NÍVEL SUPERIOR DEVERÁ TER A MESMA NATUREZA DA SUB-CONTA**

A(s) conta(s) analítica(s) indicada(s) no validador deverá possuir a mesma ‘Natureza da Conta para Emissão do SPED’ da conta sintética correspondente.

Acesse o Plano de Contas Contábeis e verifique o preenchimento do campo Natureza da Conta para Emissão do SPED das Contas analíticas e sintéticas correspondentes.

**NÃO FOI INFORMADO NENHUM REGISTRO I051**

Caso deseje realizar o envio do Plano de Contas Referencial (Registro I051), deve-se realizar a vinculação das contas contábeis (empresa) com o plano de contas referencial/paralelo (Receita) através do menu ‘Cadastros’ / ‘Plano de Contas Paralelo’

Caso não tenha realizado o processo citado, o validador apresentará a mensagem em questão, porém a mesma é uma advertência e não impede o “envio” do SPED Contábil.  
Obs.: O Plano de Contas de Referencial é apenas obrigatório para a geração do SPED FCONT.

**A VALIDADE DA CONTA INFORMADA NÃO ESTÁ DENTRO DO PERÍODO DA ESCRITURAÇÃO**

Essa inconsistência pode ser apresentada por dois motivos:

a) Plano de Contas Referencial desatualizado

Devido à utilização de um Plano Referencial desatualizado. Arquivo e informações pertinentes a importação do plano de contas referencial/paralelo disponibilizadas nos Documento da Comunidade R@ Contábil:

<https://totvs.byyou.com/?space=rcontbil> - Documento / Totvs Gestão Contábil / SPED Contábil e SPED FCONT

b) A conta referencial informada não está vigente no período da escrituração  
É orientado retirar as associações das Contas apresentadas no validador e associar as Contas Contábeis em questão a outras Contas Referenciais do Plano Paralelo. Ou seja, a Conta Referencial apresentada não pode ser utilizada na Associação do Plano de Contas Paralelo.

Acesse diretório onde está instalado o sistema SPED, onde há uma pasta chamada ‘tabelasexternas’ abra o arquivo ‘contasref-SRF’.

Conforme este arquivo existe contas no plano de contas referencial que não estão mais no período de vigência. Portanto não devem ser associadas. Verifique a data final apresentada no registro (quando há duas datas);

**SOMA DOS SALDOS FINAIS CREDORES É DIFERENTE DA SOMA DOS SALDOS FINAIS DEVEDORES NO PERÍODO INFORMADO NOS REGISTROS DE SALDOS PERIÓDICOS**

**SOMA DOS SALDOS INICIAIS CREDORES É DIFERENTE DA SOMA DOS SALDOS INICIAIS DEVEDORES NO PERÍODO INFORMADO NOS REGISTROS DE SALDOS PERIÓDICOS**

**TOTAL DOS DÉBITOS DIFERENTE DO TOTAL DE CRÉDITOS NO PERÍODO INFORMADO NOS REGISTROS DE SALDOS PERIÓDICOS**

A inconsistência em questão pode ser apresentada pelos dois motivos abaixo:

a) Natureza da Conta para emissão do SPED:

Verifique se todas as ‘Contas Contábeis’ estão com o campo ‘Natureza da Conta para emissão do SPED’ corretamente preenchido.

Utilize a seguinte consulta SQL (EXEMPLO) para realizar essa verificação:

select CODCOLIGADA, CODCONTA, NATSPED from CCONTA

Constantes do Campo NATSPED:

00 - Não informado

01 - Contas de Ativo

02 - Contas de Passivo

03 - Patrimônio Líquido

04 - Contas de Resultado

05 - Contas de Compensação

09 - Outras

Caso as Naturezas estejam corretamente informadas, favor revisar o saldo anterior do ativo, pois ele não estará igual ao do passivo.

b) Apuração do exercício – Transferência de Grupos Contábeis.

Essa inconsistência é apresentada, pois ocorreu uma não-conformidade no processo de validação da Apuração do Resultado. Nesse caso, é orientado realizar o seguinte procedimento:

* Cancelar a(s) Transferência(s) de Grupos Contábeis;

* Executar a Transferência de Grupos Contábeis informando um ‘Histórico de Fechamento’ especifico para cada Transferência;

* Verifique o resultado da Apuração através do Balancete;

* Informar o(s) Histórico(s) de Fechamento utilizado(s) na Transferência na geração do FCONT.

**REGISTRO ENCONTRADO É DIFERENTE DO REGISTRO ESPERADO OU O TIPO DE REGISTRO É DESCONHECIDO**

É necessário revisar o cadastro da Filial, informando/preenchendo os campos solicitados na guia ‘Dados Adicionais’ (exemplo: Inscrição Municipal e Estadual).  
Obs.: ‘Cadastros’ / ‘Filiais’ / edite a filial informada na geração do SPED.

Revise também o cadastro de ‘Outras Inscrições Cadastrais’. Nesse cadastro deverá indicar se a empresa possui inscrição em outra Secretaria de Fazenda Estadual, além da Receita Federal. Se a empresa não possuir Inscrição deverá ser informado à opção ‘Sem Inscrição’ com ‘Código Cadastral’ 0000

Obs.: ‘Rotinas Legais’ / ‘SPED Contábil’ / ‘Outras Inscrições Cadastrais’.

**CNPJ INVÁLIDO – REGISTRO 0150**

Essa inconsistência é apresentada devido aos dados do cadastro do participante informado. Sendo necessário verificar o CNPJ informado nos registros correspondentes:

* Filial: acesse ‘Cadastros’ / ‘Filiais’ / edite a filial em questão / campo ‘CNPJ’;

* Cliente/Fornecedor: acesse o aplicativo onde foi realizado o cadastramento (exemplo: fluxus, nucleus) / ‘Cadastros’ / ‘Clientes/Fornecedores’ / edite o cli/for em questão / campo ‘CPF/CNPJ’.

**DEVE EXISTIR UM SALDO DE CONTAS DE RESULTADO ANTES DO ENCERRAMENTO PARA O LANÇAMENTO DE ENCERRAMENTO**

A inconsistência em questão está relacionada às ‘Transferências de Grupos Contábeis’ realizadas incorretamente, sendo assim, é orientado verificar se nenhuma conta de resultado está com saldo:

Caso a inconsistência persista, favor realizar o seguinte procedimento:

Desfazer a transferência, criar um novo Histórico de Fechamento, executar a ‘Consistência de Lançamentos’ (ajustando as inconsistências apresentadas) e refazer a Transferência de Grupos Contábeis com o novo ‘Histórico de Fechamento’.

Com a Transferência executada, acessar o Balancete e verifique o resultado da Transferência.

Obs.: Caso tenha sido realizado, mais de uma ‘Transferências de Grupos Contábeis’ no ano-base em questão, todos os ‘Históricos de Fechamento’ utilizados devem ser informados durante a Geração do SPED.

É recomendado que o processo acima seja realizado em base teste (backup) e somente após avaliar resultados aplicar em base de produção.

**SOMA DAS PARTIDAS DO LANÇAMENTO, A CRÉDITO, DIFERENTE DO VALOR INFORMADO NO REGISTRO LANÇAMENTO CONTÁBIL**

É orientado realizar o seguinte procedimento:

* Emita o relatório balancete na data em que a diferença está sendo apontada;
* Observe se débito e crédito estão corretos, e se o valor total do balancete correspondente ao valor do erro.
* Caso os valores não estejam corretos, deverá buscar pelo valor da diferença o lançamento correspondente, verificando a conta contábil que está sendo utilizada, caso necessário utilize o relatório Razão;

Em seguida, verifique se a Conta Contábil utilizada para esse Lançamento está com o campo ‘Natureza para Emissão do SPED Contábil’ corretamente informado.

**O SALDO FINAL DA CONTA NO REGISTRO DE SALDOS PERIÓDICOS (I155) É DIFERENTE DE ZERO NA DATA DO ENCERRAMENTO**

Certifique-se que a apuração do resultado do exercício foi devidamente realizada, possivelmente o encerramento das contas ainda não foi realizado.

Nesse caso, deve-se encerrar as Contas de Resultado através da Transferência de Grupos Contábeis, utilizando um novo Histórico de Fechamento especifico.

**NO BALANÇO PATRIMONIAL, O VALOR INFORMADO PARA O ATIVO DEVERÁ SER IGUAL À SOMA DOS VALORES INFORMADOS PARA O PASSIVO E PATRIMÔNIO LÍQUIDO**

Certifique-se que a apuração do resultado do exercício foi devidamente realizada, possivelmente o encerramento das contas ainda não foi realizado.

Nesse caso, deve-se encerrar as Contas de Resultado através da Transferência de Grupos Contábeis, utilizando um novo Histórico de Fechamento especifico.

Verifique se todas as Contas Contábeis estão com o campo ‘NATUREZA DA CONTA PARA EMISSÃO DO SPED’ corretamente preenchido.

**REGISTRO DUPLICADO EM RELAÇÃO À CHAVE COD\_AGL**

A inconsistência é apresentada, pois no modelo utilizado na DRE existiam Contas Contábeis duplicadas.

Sendo assim, é necessário acessar a DRE, selecionar a(s) conta(s) duplicada(s) e desmarcar a opção ‘Enviar SPED’.

Obs.: ‘Relatórios’ / ‘Demonstração de Resultados’.

**O VALOR INFORMADO NAS CONTAS DE MAIOR DETALHAMENTO DO REGISTRO DA DRE NÃO CORRESPONDE À SOMA DOS VALORES INFORMADOS NOS REGISTROS DE SALDOS DAS CONTAS DE RESULTADO ANTES DA APURAÇÃO NA MESMA DATA.**

A advertência citada pode ocorrer por dois motivos:

a) Inconsistências no Relatório.

O Balanço Patrimonial e (ou) a DRE para o SPED, podem ser gerados pelo menu ‘Relatórios’ ou automaticamente, conforme a ‘Natureza da Conta para emissão do SPED’.

Sendo assim, conforme o método utilizado para geração, recomendo que verifique o relatório utilizado (menu relatórios / demonstração de resultado) ou verifique as ‘Natureza da conta para emissão do SPED’ foram corretamente informadas no Plano de Contas Contábeis.

b) Utilização do Plano de Contas Referencial do SPED FCONT.

Foi utilizado o mesmo plano paralelo do SPED FCONT para o SPED CONTÁBIL.

Ainda que para o SPED Contábil o centro de custo não seja obrigatório, uma vez associado, este consistirá a mesma regra do FCONT:

•             Todos os lançamentos terão que ter centro de custo preenchido;

•             Os Saldos Anteriores terão que ter centro de custo preenchido;

•             Todos os centros de custo terão que ser associados no Plano de Contas Paralelo.

Nesse caso, é orientado realizar um dos processos abaixo:

a)           Corrigir as informações correspondentes à centros de Custo conforme regras de FCONT.

**QUALIFICAÇÃO DO ASSINANTE NÃO ENCONTRADA NA TABELA DE QUALIFICAÇÃO DO ASSINANTE**

Este erro é apresentado devido aos dados da Qualificação do Assinante, nesse caso, é orientado realizar o seguinte procedimento:

* Acessar o cadastro de ‘Qualificação de Assinantes’;
* Editar o registro ‘900 - ‘Contador / Contabilista’;
* Alterar a ‘Descrição’, excluindo a informação “ / Contabilista“, mantendo apenas “Contador”.
* Obs.: ‘Rotinas Legais’ / ‘SPED Contábil’ / ‘Qualificação de Assinantes’.

**CONTA NÃO ENCONTRADA NOS REGISTROS DO PLANO DE CONTAS**

Deve-se verificar se as Contas Contábeis apresentadas na validação estão com a ‘Natureza da Conta para Emissão do SPED’ e a ‘Data de Inclusão’ (guia: informações) corretamente preenchidas. Verifique também se as contas em questão estão devidamente associadas no Plano de Contas Paralelo.

**A DATA DO CAMPO DT\_ALT DEVE SER MENOR OU IGUAL À DO CAMPO DT\_FIN DO REGISTRO 0000**

1) Registro I050:

|I050|01012013|01|A|11|1.1.1.2.0109|1.1.1.2|Totvs SA |

1.1) Alteração da Conta Contábil superior ao Período de Escrituração.

Nesse caso, é orientado marcar a opção Facultativa ‘Não enviar histórico de alteração das Contas Contábeis para o registro I050’ durante a geração do SPED contábil. Nesse caso, houve alterações na Conta Contábil em questão após a data do SPED.

1.2 ) Data de Inclusão da Conta Contábil superior ao Período de Escrituração

A Data de Inclusão das Contas Contábeis apresentadas nesta advertência são superiores a data final de geração do FCONT.

Caso, a Conta Contábil apresentada não tenha que ser encaminhadas para o SPED FCONT, deverá estar preenchido com o campo ‘Natureza da Conta para Emissão do SPED’ como ‘Não Informada’. Caso contrário, é necessário alterar a ‘Data de Inclusão’ da Conta Contábil informando uma Data de Inclusão dentro ou inferior ao período de escrituração.

Para preencher o campo citado, deve-se acessar o ‘Plano de Contas Contábil’ / selecionar as Contas Contábeis em questão / menu ‘Processos’ / ‘Atualização da Data de Inclusão’ ou ainda, editar a conta e na aba ‘Informações’ preencher a data.

b) Registro I100:

|I100|22092013|1|Administrativo|

1.1)  Alteração do Centro de Custo superior ao Período de Escrituração.

Nesse caso, é orientado marcar a opção Facultativa ‘Não enviar histórico de alteração de Centro de Custo para o registro I050’ durante a geração do SPED contábil. Nesse caso, houve alterações no Centro de Custo em questão após a data do SPED.

1.2 ) Data de Inclusão do Centro de Custo superior ao Período de Escrituração

A Data de Inclusão dos Centros de Custos ou Contas Gerenciais apresentados nesta advertência são superiores a data final de geração do FCONT.

Caso, estes não tenham que ser encaminhadas para o SPED FCONT, no cadastro correspondente deverão estar com o campo ‘Enviar para o SPED Contábil’ desmarcado. Caso contrário, é necessário alterar a ‘Data de Inclusão’ do Centro de Custo ou Conta Gerencial informando uma Data de Inclusão dentro ou inferior ao período de escrituração.  
Para preencher o campo citado, deve-se acessar o cadastro de Centro de Custo ou Plano de Contas Gerencial / selecionar os registros correspondentes / menu ‘Processos’ / ‘Atualização da Data de Inclusão’ ou ainda, editar o registro e preencher a Data de Inclusão.

**CÓDIGO DO HISTÓRICO PADRÃO NÃO ENCONTRADO NOS REGISTROS DE HISTÓRICOS PADRÃO**

Essa inconsistência é apresentada devido ao não preenchimento do campo ‘Descrição’ do ‘Histórico Padrão’ informado na ‘Transferência de Grupos Contábeis’.

Nesse caso, é orientado acessar ‘Cadastros’ / ‘Históricos Padrões’ / filtrar o Histórico em questão e definir a ‘Descrição’ do Histórico.

Vale ressaltar que a Transferência de Grupos Contábeis deve ser executada com um ‘Histórico de Fechamento’ novo. Ou seja, cada encerramento do exercício deverá possuir histórico único.

**SALDO DA CONTA ANTES DO ENCERRAMENTO NÃO CORRESPONDE AO TOTAL DOS LANÇAMENTOS DE ENCERRAMENTO (PARA A CONTA 3.5.2.02.0061).**  
A inconsistência em questão está relacionada à Transferência de Grupos Contábeis, sendo necessário realizar o seguinte procedimento:

a)      Desfaça a Transferência de Grupos Contábeis;

b)      Crie um Novo Histórico de Fechamento;

c)       Execute a ‘Consistência de Lançamentos’ (ajustando as inconsistências apresentadas);

d)      Refaça a Transferência de Grupos Contábeis, informando o novo Histórico de Fechamento.

Observações:

* Informe APENAS 1 (um) Histórico de fechamento nos moldes da estrutura da Transferência

* Com a Transferência executada, acesse o Balancete e verifique o resultado da Transferência.

* É recomendado que o processo acima seja realizado em base teste (backup) e somente após avaliar resultados aplicar em base de produção.

**CONTEÚDO DO CAMPO INVÁLIDO. HIST - I250**

A inconsistência em questão está relacionada ao complemento do histórico definido nos Lançamentos Contábeis citados.  
Nesse caso, é necessário acessar os Lançamentos e verificar se o complemento não possui caracteres inválidos (exemplo: ‘Tab’, espaços ao final do complemento, dentre outros).

**CAMPO OBRIGATÓRIO NÃO PREENCHIDO. 2 - COD\_ENT\_REF**

É necessário acessar ‘Cadastros’ / ‘Plano de Contas Paralelo’ / editar o Plano em questão e informar no campo ‘Instituição Responsável’ = “Secretaria da Receita Federal”.

**ESTRUTURA DA LINHA INVÁLIDA. A ÚLTIMA LINHA DA ESCRITURAÇÃO NÃO TERMINA COM OS CARACTERES CR (CARRIAGE RETURN) E LF (LINE FEED)**

É orientado inserir uma linha em branco do rodapé do arquivo gerado, utilizando a tecla ‘Enter’.

**FAVOR PREENCHER NOS PARÂMETROS DO SISTEMA EM ROTINAS LEGAIS/SPED CONTÁBIL O CAMPO “DATA DE INCLUSÃO” DE CENTROS CUSTOS/CONTAS GERENCIAL PARA GERAÇÃO DO SPED CONTABIL**

É orientado acessar ‘Opções’ / ‘Parâmetros’ / ‘RM Saldus’ / ‘01.06 – Rotinas Legais’ / ’01.06.01 – SPED Contábil’ e realizar o preenchimento da ‘Data de Inclusão’.

Obs.: A ‘Data de Inclusão’ deve ser inferior ao período de geração do SPED.

**CONTA NÃO ENCONTRADA NOS REGISTROS DO PLANO DE CONTAS - COD\_CTA\_SUP**

Essa inconsistência é apresentada quando existem diferenças entre a Conta Analítica e a(s) Conta(s) Sintética(s) correspondente(s). Nesse caso, é necessário acessar todas as Contas Sintéticas superiores à Conta Analítica e verificar a ‘Natureza da Conta para Emissão do SPED e a ‘Data de Inclusão’.

**ORGANIZAÇÃO HIERÁRQUICA DOS BLOCOS/REGISTROS DO ARQUIVO ESTÁ FORA DOS PADRÕES ESTABELECIDOS.**

A inconsistência em questão pode ser apresentada pelos dois motivos abaixo:

a) Versão do Validador da Receita

Certifique-se que a versão do Validador da Receita é compatível com o período de escrituração do SPED.

b) Arquivo texto gerado pelo RM Saldus incompleto.

Certifique-se que o arquivo texto do SPED foi totalmente gerado pelo RM Saldus. Caso a geração do arquivo tenha sido interrompida o erro citado será apresentada. Vale ressaltar que o registro 9999 é o último item do arquivo texto.

**UM LANÇAMENTO PODE TER VÁRIOS REGISTROS A DÉBITO A VÁRIOS A CRÉDITO SOMENTE QUANDO RELATIVOS AO MESMO FATO CONTÁBIL (RESOLUÇÃO CFC 1299/2010). VERIFIQUE SE A SITUAÇÃO ESTÁ CORRETA.**

Informações, restrições e exemplos pertinentes ao processo citado estão disponíveis no(s) link(s) abaixo:

<http://wikihelp.totvs.com.br/WikiHelp/CTB/CTB.ReestruturacaoLancamentosFatosContabeis.aspx>

Obs.: Procedimento deve ser realizado através da Nova MDI, verifique as permissões de acesso correspondentes no Perfil do Usuário.

 

**FAVOR CONFERIR O CADASTRO DO SIGNATÁRIO DO TIPO CONTADOR, POIS AS INFORMAÇÕES PESSOAIS E DO CRC SÃO OBRIGATÓRIOS.**

Registro J930 (IDENTIFICAÇÃO DOS SIGNATÁRIOS DA ESCRITURAÇÃO) - Inclusão dos campos: 

Campos obrigatórios: 

* FONE - Telefone do signatário
* EMAIL - E-mail do signatário
* UF\_CRC - Indicação da unidade da federação que expediu o CRC
* NUM\_SEQ\_CRC - Número sequencial no seguinte formato: UF/ano/número
* DT\_CRC - Data de validade do CRC do contador

 

Foi criada uma aba (Dados adicionais – Layout 2.0) no cadastro do Signatário disponível dentro do cadastro de Escrituração Contábil (menu ‘Rotinas Legais’ / ‘SPED Contábil’ / ‘Escriturações Contábeis’, para que sejam informados os novos campos que serão obrigatórios no layout 2.0 para o signatário contador/contabilista.

 

Lembrando que, essas informações só são obrigatórias para o Signatário Contador/Contabilista. Ao gerar o arquivo no layout 2.00, as novas informações serão geradas no arquivo, no registro J930. Preencher os todos os dados do Contador

 

**INFORMAÇÕES ADICIONAIS**

É orientado realizar os procedimentos indicados acima, utilizando as últimas versões do RM Saldus e da Biblioteca disponibilizadas no Portal da Totvs.

Caso necessário, favor realizar os procedimentos de correção em base teste (backup) e somente após avaliar os resultados aplicar em base de produção.

Referente a Natureza da Conta para emissão do SPED, caso necessário utilize a Classificação Automática da Natureza da Conta para emissão do SPED’, conforme link: <http://wikihelp.totvs.com.br/WikiHelp/CTB/ctb.ClassificacaoAutomaticaNATSPED.aspx>

Para maiores informações:

[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE****[R@ Controladoria](http://fluig.totvs.com/portal/p/10097/subject/rcontbil)**

**Canais** **de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:**4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 2 – (Controladoria e Finanças), 5 – (Planejamento e Controle Orçamentário), 2 – (RM Saldus).
