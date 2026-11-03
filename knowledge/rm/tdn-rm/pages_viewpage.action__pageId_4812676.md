---
content_hash: 80f1bbc36d70e72d90e12534db04b5d91d9b5d3bbe37e7274f92d7dc41eff378
fetched_at: '2026-06-29T00:10:18.891741+00:00'
page_id: '4812676'
product: rm
source: tdn-rm
title: Conversão do RM FOLHA x TOTVS Folha de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4812676
version: 4
---

BLOCK

Conversão do RM FOLHA x TOTVS Folha de Pagamento

FAQ: **Conversão do RM FOLHA x TOTVS Folha de Pagamento**

|  |  |
| --- | --- |
| Produto: | RM |
| Ambiente: | WinForms |
| Versão: | 11.0 |

Avaliação

**Produto:** *TOTVS Folha de Pagamento***Versão:***11.00*  
**Processo de Negócio:** Administração de Pessoal  
**Processo do Sistema:** Administração de Pessoal  
**Subprocesso:** Conversão do RM FOLHA (MS-DOS) para TOTVS Folha de Pagamento (Windows)

Sintoma

A conversão de dados do RM FOLHA para o TOTVS Folha de Pagamento (RM Labore) consistem em migrar automaticamente os dados do sistema DOS para o sistema Windows. Este procedimento pode ser executado em uma nova base de dados, em uma nova coligada ou em uma empresa que já tenha dados no RM Labore.

Solução

**Procedimentos a serem executados no RMFOLHA**

**1)****Processar módulo 7.V.**

Informar SIM nos campos abaixo:

- Zerar Campos Inválidos.

-Verificação para conversão para RMLabore.

[![clip_image002](http://lh4.ggpht.com/_G7KXZLoZDsY/TWOYh0nF4dI/AAAAAAAAGjo/-gXY4_71KHg/clip_image002_thumb%5B1%5D.jpg?imgmax=800 "clip_image002")](http://lh5.ggpht.com/_G7KXZLoZDsY/TWOYhCWBHtI/AAAAAAAAGjk/AAmokES825k/s1600-h/clip_image002%5B4%5D.jpg)

**Atenção!**

· Após processar o modulo 7.V será gerado um arquivo “VERIFICA.ERR” (gerado dentro da pasta da empresa).O arquivo “CHKBASE.DOC” (que está dentro da pasta RMFOLHA) ajuda a verificar a descrição dos erros do arquivo “VERIFICA.ERR”.

· Antes da conversão TODOS os erros devem ser corrigidos conforme os arquivos aqui mencionados (“VERIFICA.ERR”. e“CHKBASE.DOC”).

· É aconselhável executar a conversão após a liberação da competência, caso faça uma conversão com a movimentação mensal dos funcionários é necessário após a conversão efetuar um recálculo geral no RM Labore inclusive rescisões.

· A liberação de flags deverá ser executada no RMFOLHA antes de iniciar a conversão.

· Antes da conversão, o cadastro de funcionários no RMFOLHA não poderá ter chapas repetidas. No RM Labore chapa é a chave de pesquisa do funcionário, semelhante ao campo REG do RMFOLHA.

**Configurações do Banco de Dados**

***Exemplo:***

Preparando uma base de dados vazia:

· Acessar o site da TOTVS e fazer o download do ultimo instalador da base de dados SQL ou ORACLE.

· Ao executar o instalador “Base de Dados SQL ou Oracle” será criado um backup da base vazia (Vazia112020101228.bak), já com todas as tabelas criadas.

· No SQL ou Oracle fazer a restauração da base de dados vazia informando o nome da base a ser utilizada pela empresa. Exemplo: Base\_Teste .

· Após descompactar a base, o BDE deve ser configurado.

**Configuração do BDE**

Criar um “Alias” no BDE Administrador. Este “Alias” deve, ***impreterivelmente,*** ter o nome “CorporeRM”, pois o conversor converte os dados para a base de dados apontada para este Alias.

**Procedimentos a serem executados no RM Labore**

· Nova base de dados

Salve o arquivo “***Aponta.txt*”**, enviado pela TOTVS, em um diretório de fácil localização. Utilize o aplicativo **“*ImpAponta.exe****”* para fazer a importação do aponta para a nova base de dados.

· Inclusão de nova coligada

Em uma coligada já existente, acesse o módulo UTILITÁRIOS / IMPORTAÇÃO DE COLIGADAS e importe o arquivo “Aponta.txt”, enviado pela TOTVS. Ele incluirá a nova coligada.

[![clip_image004](http://lh4.ggpht.com/_G7KXZLoZDsY/TWOYi-nViOI/AAAAAAAAGjw/JxLEnAxkU9c/clip_image004_thumb%5B1%5D.jpg?imgmax=800 "clip_image004")](http://lh6.ggpht.com/_G7KXZLoZDsY/TWOYiSdhRvI/AAAAAAAAGjs/7Epq3RlLkGY/s1600-h/clip_image004%5B4%5D.jpg)

**Processo de Conversão de Base**

**Passo 1:** Instalar o Conversor RMFOLHA x RMLabore.

**Observação:** Ao utilizar o conversor 11.01, a base de dados será convertida, automaticamente, para o Cálculo .Net (Máquina de Cálculo da Folha). Para isso, os scripts que acompanham o conversor devem estar dentro da mesma pasta onde se encontra o instalador do Conversor.

**Passo 2:** Acessar o conversor com usuário “mestre” e senha “rm sistemas” (nova base de dados), no caso de base de dados com coligadas utilize algum usuário com perfil de acesso supervisor.

[![clip_image006](http://lh3.ggpht.com/_G7KXZLoZDsY/TWOYj9DwXYI/AAAAAAAAGj4/pr_Cq2nqy08/clip_image006_thumb%5B1%5D.jpg?imgmax=800 "clip_image006")](http://lh4.ggpht.com/_G7KXZLoZDsY/TWOYjnHOKPI/AAAAAAAAGj0/trIwrUN4Sy4/s1600-h/clip_image006%5B4%5D.jpg)

**Atenção**:

-É aconselhável executar a conversão após a liberação da competência. Caso faça uma conversão com a movimentação mensal dos funcionários, após essa é necessário efetuar um recálculo geral no RM Labore inclusive rescisões.

- A liberação de flags deverá ser executada no RMFOLHA antes de iniciar a conversão.

- Antes da conversão o cadastro de funcionários, no RMFOLHA não poderá ter chapas repetidas. No RM Labore chapa é a chave de pesquisa do funcionário, semelhante ao campo REG do RMFOLHA.

**Passo 3:** Será aberta uma tela para informação dos dados de onde se encontra a base de dados do RM Folha (empresa/firma do sistema DOS), caso a empresa utilize diretório global no RM Folha informe o diretório dos arquivos globais.

[![clip_image008](http://lh4.ggpht.com/_G7KXZLoZDsY/TWOYk6GFqGI/AAAAAAAAGkA/wqLRp9qa9DM/clip_image008_thumb%5B1%5D.jpg?imgmax=800 "clip_image008")](http://lh5.ggpht.com/_G7KXZLoZDsY/TWOYkZlAtFI/AAAAAAAAGj8/yNtQk5b2Q3E/s1600-h/clip_image008%5B4%5D.jpg)

Os parâmetros abaixo indicam as informações de como deverão ser considerados os dados:

**Gera log de erros -** Informe se será ou não gravado um arquivo com erros da conversão.

**Ignorar erros de chave duplica -** Informe se os erros de inclusão de registros duplicados serão desconsiderados. Este tipo de erro é muito comum na conversão de horários, linhas de transporte e seções, que tem mesmo código.

**Considerar conta contábil como Conta reduzida -** No RM Labore, na parametrização das contas, existe um campo de identificação da conta por número reduzido. Informe se quer que o número da conta e o número reduzido sejam os mesmos.

**Considerar Conta contábil como Tipo Sintética -** Caso não confirme este campo as contas serão cadastradas como Analíticas.

**Converter Códigos fixos Zerados -** Informe se quer converter os códigos fixos que estão com número de vezes zerados.

**Consistir CNPJ da coligada antes da conversão -** Este parâmetro faz uma verificação entre o CNPJ da empresa do RMFolha e o CNPJ da coligada informada no campo “Coligada”.

**Coligada -** Informe a coligada do RM Labore que estará recebendo os dados.

**Faixa de funcionários -** Informe a faixa de registros de funcionários do RM FOLHA que serão convertidos para o RM

**DICA**

Dividir a conversão em etapas: de 500 em 500 registros de funcionários se na coligada tiver mais de 500 funcionários entre Ativos, Demitidos e Afastados

*Exemplo:*

A primeira faixa 01 a 500 habilitar “todas as tabelas”;

A segunda faixa 501 a 1000 habilitar “funcionários”, e assim, sucessivamente.

***[![clip_image010](http://lh6.ggpht.com/_G7KXZLoZDsY/TWOYmbddpeI/AAAAAAAAGkI/-Lm_FQMTx-w/clip_image010_thumb%5B1%5D.jpg?imgmax=800 "clip_image010")](http://lh4.ggpht.com/_G7KXZLoZDsY/TWOYljZ-VmI/AAAAAAAAGkE/BX3cQW77a5Y/s1600-h/clip_image010%5B4%5D.jpg)***

**Passo 4*:*** Informe se serão convertidas “Todas as tabelas” ou apenas “Funcionários”.

**Todas as tabelas**

Converte todos os dados do RMFOLHA para a coligada do RMLabore. Esta opção deve ser utilizada em conversões para novas empresas (nova base, ou nova coligada). Esta opção converte os funcionários também.

**Funcionários**

Converte apenas os dados de funcionários (cadastro, ficha financeira, etc) para a coligada do RM Labore. Deve ser utilizada para inclusão de funcionários em coligada existente no RM Labore.

Para que esta conversão seja efetuada com sucesso, alguns dados devem ser iguais nas bases do RM FOLHA e RM Labore, como: eventos, seções, horários, etc.

[![clip_image012](http://lh3.ggpht.com/_G7KXZLoZDsY/TWOYnt8pIGI/AAAAAAAAGkQ/zX4Io0Y_ccU/clip_image012_thumb%5B1%5D.jpg?imgmax=800 "clip_image012")](http://lh4.ggpht.com/_G7KXZLoZDsY/TWOYnNo8qCI/AAAAAAAAGkM/7rO3BZ_aTs0/s1600-h/clip_image012%5B4%5D.jpg)

Depois de converter a seção, o conversor abrirá uma nova tela e pedirá ao usuário, que associe as filiais contábeis à outra filial gerada na conversão. O usuário tem a opção de associar a filial selecionada, como sendo a filial contábil de todas as seções.

Caso já haja registros cadastrados no RM Labore, serão exibidas, primeiramente, na base da janela, mensagens relativas às tabelas que estão sendo apagadas. Posteriormente, aparecerão na caixa Progresso:

· O nome de cada tabela que está sendo convertida (no campo Entidade);

· O total de registros e número do registro que está sendo convertido (campos Total/Corrente);

· O tempo gasto na conversão (campo Duração).

O botão Cancelar permite interromper a conversão. Neste caso, será emitida mensagem de erro, uma vez que, a conversão ficará incompleta.

Concluído o processo de conversão, será emitida, na base da janela, as mensagens "Conversão encerrada sem erros" ou "Conversão emitida com erros", conforme o caso.

Caso tenham ocorrido erros, para visualizar o arquivo que contém essa listagem, clique em: “Visualizar (ícone do olho)” localizado em **Arquivo de Log**.

**[![clip_image014](http://lh5.ggpht.com/_G7KXZLoZDsY/TWOYonTr7nI/AAAAAAAAGkY/lQyXocr-cuc/clip_image014_thumb%5B1%5D.jpg?imgmax=800 "clip_image014")](http://lh6.ggpht.com/_G7KXZLoZDsY/TWOYoIN63qI/AAAAAAAAGkU/-AQejtDIL3Q/s1600-h/clip_image014%5B4%5D.jpg)**

Observações

**DICA**

Após a conversão acesse o RM Labore e faça os ajustes necessários para utilização do sistema.

**Parâmetros do RM Labore**

Informa a máscara da chapa, mês competência e ano competência (verificar como estão tais máscaras no RMFOLHA):

**Parâmetros Globais**

Informe os dados de seções, Centros de custo e departamentos.
