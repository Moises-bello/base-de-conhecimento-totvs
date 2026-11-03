---
content_hash: d616884623b536f72029f280d3bb6222cebf6c3c9ded39e97423ee8a1d3f6f28
fetched_at: '2026-06-29T00:11:05.935717+00:00'
page_id: '63275227'
product: rm
source: tdn-rm
title: RMCTB00004_FCONT - Correção dos erros apresentados na validação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=63275227
version: 5
---

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Produto** | | : | | TOTVS Gestão Contábil – **Versão:** 11.52 ou superior | |
| **Processo** | | : | | SPED FCONT | |
| **Subprocesso** | | : | | Listagem e correção dos erros apresentados na validação | |
| **Data da publicação** | | : | | 24/01/2014 | |

**Erros e Advertências na Validação do FCONT**

Durante a validação do SPED o Validador da Receita poderá apresentar Erros e Advertências, impossibilitando a validação do arquivo.  
Sendo assim, segue abaixo orientações pertinentes à correção dos principais erros e advertências apresentadas durante a validação.

**Desenvolvimento/Procedimento**

**O CAMPO É OBRIGATÓRIO E NÃO FOI PREENCHIDO. M020** 

Ao validar o arquivo acesse a GUIA ‘Escriturações’ / ‘Registros Fiscais’ / ‘Identificação da Qualificação da Pessoa Jurídica’ e preencha os campos obrigatórios.

**REGISTRO OBRIGATÓRIO NÃO ENCONTRADO. M025**

No aplicativo da Receita acesse ‘Escrituração’ / ‘Recuperar Saldos’ caso já tenham encaminhado o FCONT ano passado.

Caso seja a primeira vez que envia o FCONT acesse ‘Escrituração’ / ‘Replicar Saldos Iniciais’.

**REGISTRO OBRIGATÓRIO NÃO ENCONTRADO. M030**

Ao validar o arquivo acesse a GUIA ‘Escriturações’ / ‘Registros Fiscais’ / ‘Identificação do Período de Apuração do Lucro Real. Neste registro deve ser informado o Período de Apuração, Resultado do Período e a Situação do Resultado do Período.

**REGISTRO OBRIGATÓRIO NÃO ENCONTRADO. J930**

Ao validar o arquivo acesse a GUIA ‘Escriturações’ / ‘Identificação dos Signatários’ / ‘Identificação dos Signatários da Escrituração’ e preencha manualmente.    
Este registro deve conter os responsáveis pela escrituração, lembrando que o FCONT exige que sejam informados pelo menos dois signatários, sendo que um deve ser o contador da empresa.

**A CONTA REFERENCIAL INFORMADA NÃO ESTÁ VIGENTE NO PERÍODO DA ESCRITURAÇÃO DEFINIDO NO REGISTRO 0000(VER TABELA DE PLANO DE CONTAS REFERENCIAL).**

Acesse diretório onde está instalado o sistema FCONT, onde há uma pasta chamada ‘tabelasexternas’ abra o arquivo ‘contasref-SRF’.

Conforme este arquivo existe contas no plano de contas referencial que não estão mais no período de vigência. Portanto não devem ser associadas. Verifique a data final apresentada no registro (quando há duas datas);

É orientado retirar as associações das Contas apresentadas no validador e associar as Contas Contábeis em questão a outras Contas Referenciais do Plano Paralelo.

**DOCUMENTO REFERENTE A TRANSFERÊNCIAS DE SALDO ENTRE CONTAS REFERENCIAIS.**

É orientado retirar as associações das Contas apresentadas no validador e associar as Contas Contábeis em questão a outras Contas Referenciais do Plano Paralelo.

Ou seja,a Conta Referencial em questão não pode ser utilizada na Associação do Plano de Contas Paralelo.

**REGISTRO OBRIGATÓRIO NÃO ENCONTRADO. I355. I350**

Essa inconsistência é apresentada, pois ocorreu uma não-conformidade no processo de validação da Apuração do Resultado. Nesse caso, é orientado realizar o seguinte procedimento:

* Cancelar a(s) Transferência(s) de Grupos Contábeis;
* Executar a Transferência de Grupos Contábeis informando um ‘Histórico de Fechamento’ especifico para cada Transferência;
* Verifique o resultado da Apuração através do Balancete;
* Informar o(s) Histórico(s) de Fechamento utilizado(s) na Transferência na geração do FCONT.

**Observações:**

A Apuração do Lucro Real é realizada Anual ou Trimestralmente, sendo assim, não é possível realizar a Transferência de Grupos Contábeis mensalmente para o FCONT.  
Essa inconsistência também é apresentada com há diversos Lançamentos com o Campo Complementar SPEDFCONT indevidamente classificados, ou seja, somente os Lançamentos correspondentes ao Ajuste Fiscal deveram ser classificados. A Contabilidade Comercial não deve ser afetada.

Durante a importação do arquivo gerado pelo RM Saldus, no validador da receita é necessário marcar os Blocos a serem importados (Importação por Blocos).  
Através da consulta abaixo é possível verificar os Lançamentos Contábeis classificados:

select \* from clcompl where SPEDFCONT is not null

**NÃO FORAM LOCALIZADOS REGISTROS I050 E I051 ESPECÍFICOS PARA ESTA CONTA E CENTRO DE CUSTO OU A DATA DE ATUALIZAÇÃO DA CONTA NO REGISTRO I051 (DT\_ALT) É POSTERIOR À DATA DE USO DA CONTA NESTE.**

A inconsistência em questão pode ser apresentada pelos dois motivos abaixo:

a) Quando o centro de custo é apresentado no registro:

|I155|1.1.2.7.03.01.79|**01.3**|922,25|D|0,00|0,00|933,25|D|

Essa inconsistência é apresentada, pois o(s) Centro(s) de Custo informado(s) na Validação não foi associado ao Plano Paralelo.

Sendo assim, é necessário vincular todos os Centros de Custos apresentados na validação às Contas Contábeis apresentadas ou no Cadastro de Centro de Custo desmarcar a opção de ‘Enviar para o SPED’, neste último caso, não será gerado nenhum dado para o SPED FCONT referente ao Centro de Custo desmarcado.

Caso necessário execute a Associação Dinâmica de Centro e Custo no Plano de Contas Paralelo: <http://wikihelp.totvs.com.br/WikiHelp/CTB/CTB.PlanoContaParaleloAssociacaoDinamica.aspx>

Pode-se verificar a associações atuais com Centro de Custo realizadas através da seguinte consulta SQL:

select \* from cctacta2item

b) Quando o centro de custo não é apresentado no registro (null):

|I155|1.1.2.7.03.01.79|**null**|922,25|D|0,00|0,00|933,25|D|

Essa inconsistência é apresentada, pois existem Lançamentos para as Contas Contábeis apresentadas onde o Centro de Custo não foi preenchido. Será necessário localizar esses lançamentos (filtrar) e preencher o Centro de Custo através da Alteração de Partidas em Grupo (Menu Processos)

**REGISTRO OBRIGATÓRIO NÃO ENCONTRADO. I050**

Durante a importação do arquivo gerado pelo RM Saldus, no validador da receita é necessário marcar os Blocos a serem importados (Importação por Blocos).

**REGISTRO OBRIGATÓRIO NÃO ENCONTRADO. I150**

Durante a importação do arquivo gerado pelo RM Saldus, no validador da receita é necessário marcar os Blocos a serem importados (Importação por Blocos).

**O CAMPO É OBRIGATÓRIO E NÃO FOI PREENCHIDO. I051**

Acesse ‘Cadastros’ / ‘Plano de Contas Paralelo’ / edite o Plano Paralelo utilizado na geração / e preencha o campo ‘Instituição Responsável’

**CAMPOS COM DATAS DIFERENTES ENTRE REGISTRO CO-RELACIONADOS.**

**A DATA DO CAMPO DT\_ALT DO REGISTRO I050 DEVE SER MENOR OU IGUAL À DO CAMPO DT\_FIN DO REGISTRO 0000.**

a) Registro I050:

|I050|**01012013**|01|A|11|1.1.1.2.0109|1.1.1.2|Totvs SA |

A Data de Inclusão das Contas Contábeis apresentadas nesta advertência são superiores a data final de geração do FCONT.

Caso, a Conta Contábil apresentada não tenha que ser encaminhadas para o SPED FCONT, deverá estar preenchida com o campo ‘Natureza da Conta para Emissão do SPED’ como ‘Não Informada’. Caso contrário, é necessário alterar a ‘Data de Inclusão’ da Conta Contábil informando uma Data de Inclusão dentro ou inferior ao período de escrituração.

Para preencher o campo citado, deve-se acessar o ‘Plano de Contas Contábil’ / selecionar as Contas Contábeis em questão / menu ‘Processos’ / ‘Atualização da Data de Inclusão’ ou ainda, editar a conta e na aba ‘Informações’ preencher a data.

b) Registro I100:

|I100|**22092013**|1|Administrativo|

A Data de Inclusão dos Centros de Custos ou Contas Gerenciais apresentados nesta advertência são superiores a data final de geração do FCONT.

Caso, estes não tenham que ser encaminhadas para o SPED FCONT, no cadastro correspondente deverão estar com o campo ‘Enviar para o SPED Contábil’ desmarcado. Caso contrário, é necessário alterar a ‘Data de Inclusão’ do Centro de Custo ou Conta Gerencial informando uma Data de Inclusão dentro ou inferior ao período de escrituração.

Para preencher o campo citado, deve-se acessar o cadastro de Centro de Custo ou Plano de Contas Gerencial / selecionar os registros correspondentes / menu ‘Processos’ / ‘Atualização da Data de Inclusão’ ou ainda, editar o registro e preencher a Data de Inclusão.

**A NATUREZA DA CONTA REFERENCIAL UTILIZADA É DIFERENTE DA NATUREZA DA CONTA CONTÁBIL DO REGISTRO I050. VERIFIQUE SE A SITUAÇÃO ESTÁ CORRETA.**

Acesse o Plano de Contas Paralelo (cadastros) e verifique as Contas Contábeis que estão associadas à Conta Referencial apresentada na Validação. Uma ou mais Contas Contábeis associadas não são da mesma ‘Natureza Contábil’ da Conta Referencial em questão (Contas do Ativo, Contas do Passivo, Patrimônio Liquido, Contas de Resultado).

Obs.: O campo que determina a Natureza das Contas Contábeis é o campo ‘natureza da conta para emissão do SPED’ no Plano de Contas Contábeis.

**CONTA ANALÍTICA NÃO ENCONTRADA NO PLANO DE CONTAS DA SUSEP.**

Ao incluir o registro M020 o sistema utilizará o plano de contas referencial de acordo com o código informado no M020.  Se o validador está validando como se fosse SUSEP é porque foi informado o código 00 do campo 2 do registro M020.

**ERRO DURANTE A VALIDAÇÃO DA ESCRITURAÇÃO**

Ao validar o arquivo acesse a GUIA ‘Escriturações’ / ‘Registros Fiscais’ / ‘Identificação da Qualificação da Pessoa Jurídica’ e preencha os campos obrigatórios.

**NÃO FOI ENCONTRADA NENHUMA CONTA REFERENCIAL (I051) CADASTRADA PARA ESTA CONTA CONTÁBIL.**

A Conta Contábil apresenta na validação não foi associada no Plano de Contas Paralelo. Sendo assim, realize as associações necessárias através do Plano de Contas de Contas Paralelo.

Obs.: Todas as Contas Contábeis com a ‘Natureza da conta para emissão do SPED’ preenchida devem ser associadas ao plano de contas paralelo.

**NÃO EXISTE COMPATIBILIDADE ENTRE OS SALDOS INICIAIS DOS REGISTROS M025 E O I155 PARA A CONTA XXXX E CENTRO DE CUSTO XXXX, CONTABILIZADOS OS LANÇAMENTOS DO TIPO IS.**

No aplicativo da Receita acesse ‘Escrituração’ / ‘Recuperar Saldos’, caso já tenham encaminhado o SPED FCONT no ano anterior. Caso seja a primeira vez que a coligada realiza o envio do SPED FCONT acesse ‘Escrituração’ / ‘Replicar Saldos Iniciais’.

Caso a inconsistência persista:

Neste caso, deve-se verificar a data de inclusão da Conta Contábil apresentada no erro, ao analisar esta conta no registro I050 a mesma estará posterior à data inicial de envio do SPED, para solucionar o erro deve-se alterar a Data de Inclusão da Conta Contábil para a data inicial de escrituração do FCONT (ex: 01/01/2012).

Caso, estas Contas Contábeis não tenham que ser encaminhadas para o SPED FCONT, deverão estar com o campo ‘Natureza da Conta para Emissão do SPED’ como ‘Não Informada’.

Para preencher o campo citado, deve-se acessar o ‘Plano de Contas Contábil’ / selecionar as Contas Contábeis em questão / menu ‘Processos’ / ‘Atualização da Data de Inclusão’ ou ainda, editar a conta e na aba ‘Informações’ preencher a data.

**REGISTRO DUPLICADO EM RELAÇÃO À CHAVE COD\_CTA+COD\_CCUS.**

Essa inconsistência é apresentada, pois os Centros de Custo apresentados no validador da receita foram indevidamente associados ao Plano de Contas Paralelo ou que não possuem movimentação no período em questão que foram vinculadas ao Plano de Contas Paralelo.

Pode-se verificar as associações realizadas através da seguinte consulta SQL:

SELECT \* FROM CCTACTA2ITEM

**CAMPO COMPLEMENTAR SPEDFCONT**

Acesse ‘Cadastros’ / ‘Campos Complementares’ / ‘Lançamentos’ e inclua um novo campo complementar com os seguintes dados:

Nome da Coluna: SPEDFCONT  
Descrição: SPEDFCONT  
Tipo: Alfanumérico

Obs.: Mantenha os dados defaults para os demais campos do cadastro.

**A CONTA CONTÁBIL / CENTRO DE CUSTO NÃO PODE SE REPETIR NOS REGISTROS I250 EM LANÇAMENTOS DO TIPO TR (1.1.01.01.01.0016/NULL).**

**Tipo TR** – Lançamento de transferência da diferença entre saldos fiscais e societários no caso de implantação de um novo plano de contas.

Neste caso considera-se que o saldo societário da conta contábil do plano de contas extinto foi transferido por meio de um lançamento contábil para a nova(s) conta(s) contábil (eis).

Este lançamento tipo TR refere-se apenas a transferência da parcela do saldo fiscal que não foi transferida pelo lançamento contábil, ou seja, transfere-se apenas a diferença entre o saldo fiscal e societário.

Para efetuar esta transferência deve ser utilizado apenas um lançamento por conta contábil / centro de custo / conta referencial para cada grupo conta contábil / centro de custo extinto.

**A CONTA REFERENCIAL UTILIZADA É SINTÉTICA (2.07.04.01.00). CONTA ANALÍTICA NÃO EXISTE NO PLANO DE CONTAS REFERENCIAL DA RFB. ESTA CONTA É SINTÉTICA.**

A conta apresentada é sintética. Foi informado, no anexo II do ADE Cofis nº 31/2011, a estrutura da tabela do plano de contas referencial. Esta tabela encontra-se no próprio PVA do Fcont, em:

Arquivos de Programas/Programas/Sped/SpedFcont2011/tabelasexternas/contasref-SRF.txt

Incluiremos a conta "Reserva de Capital" analítica, como vigência até 01/01/2010, no plano de contas referencial e liberaremos outra versão.

Contudo, não é preciso esperar nova versão, pois basta já começar o mapeamento para a conta correta (por exemplo, Ágio na Emissão de Ações), tendo em vista que o sistema permite tal alteração, ou seja, alocar associação para outra Conta Referencial que melhor represente. Ex: (2.07.04.03.00)

**É OBRIGATÓRIA A ASSINATURA DE, NO MÍNIMO, UM CONTADOR E UM REPRESENTANTE LEGAL COMO SIGNATÁRIO DA ESCRITURAÇÃO FCONT.**

A inconsistência em questão é apresentada devido à obrigatoriedade dos Registros M020 e J930 conforme indicado abaixo:

M020 - Ao validar o arquivo acesse a GUIA ‘Escriturações’ / ‘Registros Fiscais’ / ‘Identificação da Qualificação da Pessoa Jurídica’ e preencha os campos obrigatórios.

J930 – Ao validar o arquivo acesse a GUIA ‘Escriturações’ / ‘Identificação dos Signatários’ / ‘Identificação dos Signatários da Escrituração’ e preencha manualmente.

Este registro deve conter os responsáveis pela escrituração, lembrando que o FCONT exige que sejam informados pelo menos dois signatários, sendo que um deve ser o contador da empresa.

**FAVOR CONFERIR SE A PROPORÇÃO FOI INFORMADA PARA TODAS AS CONTAS PARALELAS (REFERENCIAIS).**

A mensagem citada é apresentada, pois existem Contas Contábeis que foram associadas a mais de uma Conta Referencial.  
Nesse caso, é necessário indicar a proporção (%) de cada conta contábil apresentada ou retirar as vinculações realizadas indevidamente duplicadas.  
Utilize a consulta SQL EXEMPLO abaixo para verificar as contas contábeis associadas a mais de uma conta referencial:  
  
select CODCONTA, CODCONTA2  from CCTACTA2

WHERE CODCONTA IN (SELECT CODCONTA FROM CCONTA WHERE CODCOLIGADA = 1)

AND CODPARALELO = '10'

AND CODCOLIGADA2 = 1

order by CODCONTA

**O PERÍODO DEVE CORRESPONDER A UM PERÍODO INFORMADO NO REGISTRO M030.**

Essa inconsistência é apresentada, pois existem divergências entre o registro M030 informado no validador da Receita e o período de apuração determinado durante o processo de geração do SPED FCONT (Anual ou Trimestral)

**LANÇAMENTOS DE QUARTA FÓRMULA DEVEM SE REFERIR A UM MESMO FATO CONTÁBIL. VERIFIQUE SE A SITUAÇÃO ESTÁ CORRETA. (RESOLUÇÃO CFC-1299/10).**

Essa inconsistência é apresentada, pois existem Lançamentos Contábeis que tiveram o campo Complementar SPEDFCONT incorretamente e (ou) não classificados.  
Nesse caso, é necessário verificar se para os Lançamentos do Tipo X, tiveram o Lançamento correspondente do Tipo EF que tem o objetivo de encerrar o saldo fiscal das contas de resultado contábeis para que seja possível levantar o balanço patrimonial fiscal após o encerramento do exercício

A advertência também informa que Lançamentos de quarta fórmula (vários débitos para vários créditos) devem se referir a um mesmo fato contábil.

Favor verificar se os lançamentos informados se referem ao mesmo fato, caso positivo, oriento que entre em contato com a Receita Federal e verifique como é feita a validação desta advertência.

**O SOMATÓRIO DOS LANÇAMENTOS EF + TR + F + (-)X DEVE SER IGUAL A ZERO.**

Essa inconsistência refere-se às classificações dos lançamentos como (X, F e EF).

Favor verificar as classificações dos Campos Complementares dos Lançamentos Contábeis, lembrando que os lançamentos classificados como X e F se ao estiverem zerados no final devem possuir lançamentos classificados como EF.

De acordo com a RFB:

Os lançamentos EF são utilizados para transferir os lançamentos de ajuste do tipo F e X  nas contas de resultado para as contas de encerramento do resultado e, finalmente, para as contas do patrimônio líquido. Considera-se que os saldos societários das contas de resultado já foram transferidos através dos lançamentos de encerramento do exercício na contabilidade societária.

Obs.: Estes lançamentos F e EF não devem fazer parte da contabilidade e sim somente para efeitos de ajustes fiscais, sendo assim, devem possuir um ‘Histórico de Fechamento’ especifico.

**TAMANHO DO CAMPO INVÁLIDO. COD\_MUN. REGISTRO 0000.**

**CONTEÚDO DO CAMPO INVÁLIDO. COD\_MUN. REGISTRO 0000**Acesse ‘Opções’ / ‘Parametros’ / ‘RM Saldus’ / ‘Rotinas Legais’ / ‘SPED Contábil’ e altere o campo ‘Classificação do Municação’ para o registro 1 - IBGE.

**QUANDO EXISTIR UM REGISTRO I051 COM O CENTRO DE CUSTO VAZIO, ELE DEVE SER ÚNICO PARA A CONTA CONTÁBIL.**

Essa inconsistencia é apresentada quando os Centros de Custo foram associados ao Plano de Contas Paralelo, porém a Conta Contabil correspondente não teve movimentações com o Centro de Custo associado.

Sendo assim, é necessário vincular somente os Centros de Custos às Contas Contábeis que estão informados nos Lançamentos Contábeis ou então no Cadastro de Centro de Custo desmarcar a opção de ‘Enviar para o SPED’, neste último caso, não será gerado nenhum dado com o Centro de Custo desmarcado.

Caso necessário execute a Associação Dinâmica de Centro e Custo no Plano de Contas Paralelo: <http://wikihelp.totvs.com.br/WikiHelp/CTB/CTB.PlanoContaParaleloAssociacaoDinamica.aspx>

**SOMA DOS SALDOS FINAIS CREDORES É DIFERENTE DA SOMA DOS SALDOS FINAIS DEVEDORES NO PERÍODO INFORMADO NOS REGISTROS DE SALDOS PERIÓDICOS.**

**SOMA DOS SALDOS INICIAIS CREDORES É DIFERENTE DA SOMA DOS SALDOS INICIAIS DEVEDORES NO PERÍODO INFORMADO NOS REGISTROS DE SALDOS PERIÓDICOS.**

**TOTAL DOS DÉBITOS DIFERENTE DO TOTAL DE CRÉDITOS NO PERÍODO INFORMADO NOS REGISTROS DE SALDOS PERIÓDICOS.**

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

Observações:

A Apuração do Lucro Real é realizada Anual ou Trimestralmente, sendo assim, não é possível realizar a Transferência de Grupos Contábeis mensalmente para o FCONT.

Essa inconsistência também é apresentada com há diversos Lançamentos com o Campo Complementar SPEDFCONT indevidamente classificados, ou seja, somente os Lançamentos correspondentes ao Ajuste Fiscal deveram ser classificados. A Contabilidade Comercial não deve ser afetada.

Durante a importação do arquivo gerado pelo RM Saldus, no validador da receita é necessário marcar os Blocos a serem importados (Importação por Blocos).

Através da consulta abaixo é possível verificar os Lançamentos Contábeis classificados:

select \* from clcompl where SPEDFCONT is not null

**A CONTA REFERENCIAL FOI EXTINTA E NÃO POSSUI SALDO FINAL IGUAL A ZERO NO PERÍODO DE APURAÇÃO REFERENTE A EXTINÇÃO.**

Orientações pertinentes ao erro disponibilizadas nos Documento da Comunidade R@ Controladoria - Documentos / Totvs Gestão Contábil / SPED Contábil e SPED FCONT:

<http://fluig.totvs.com:80/portal/p/10097/ecmnavigation?app_ecm_navigation_doc=2378688&app_ecm_navigation_version=1000> 

**A VALIDADE DA CONTA INFORMADA NÃO ESTÁ DENTRO DO PERÍODO DA ESCRITURAÇÃO**

A conta referencial informada não está vigente no período da escrituração, nesse caso, é orientado retirar as associações das Contas apresentadas no validador e associar as Contas Contábeis em questão a outras Contas Referenciais do Plano Paralelo.

Ou seja,a Conta Referencial apresentada não pode ser utilizada na Associação do Plano de Contas Paralelo.

Acesse diretório onde está instalado o sistema SPED, onde há uma pasta chamada ‘tabelasexternas’ abra o arquivo ‘contasref-SRF’. Conforme este arquivo existe contas no plano de contas referencial que não estão mais no período de vigência. Portanto não devem ser associadas. Verifique a data final apresentada no registro (quando há duas datas);

**ORGANIZAÇÃO HIERÁRQUICA DOS BLOCOS/REGISTROS DO ARQUIVO ESTÁ FORA DOS PADRÕES ESTABELECIDOS.**

A inconsistência em questão pode ser apresentada pelos dois motivos abaixo:

a) Versão do Validador da Receita

Certifique-se que a versão do Validador da Receita é compatível com o período de escrituração do SPED.

b) Arquivo texto gerado pelo RM Saldus incompleto.

Certifique-se que o arquivo texto do SPED foi totalmente gerado pelo RM Saldus. Caso a geração do arquivo tenha sido interrompida o erro citado será apresentada. Vale ressaltar que o registro 9999 é o último item do arquivo texto.

**Informações adicionais**

É  orientado realizar os procedimentos indicados acima, utilizando as últimas versões do RM Saldus e da Biblioteca disponibilizadas no Portal da Totvs.

Caso necessário, favor realizar os procedimentos de correção em base teste (backup) e somente após avaliar os resultados aplicar em base de produção.

Para maiores informações:

[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE** [**R@Controladoria**](http://fluig.totvs.com/portal/p/10097/subject/rcontbil)

**Canais** **de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 2 – (Controladoria e Finanças), 5 – (Planejamento e Controle Orçamentário), 2 – (RM Saldus).
