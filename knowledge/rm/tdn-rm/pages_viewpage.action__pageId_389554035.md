---
content_hash: 4b7d90af4d58aaa41228f8eb590193c49c5b1a973bd01591252d436eeabc8e07
fetched_at: '2026-06-29T00:09:08.545054+00:00'
page_id: '389554035'
product: rm
source: tdn-rm
title: DT Otimização do processo de Integração bancária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=389554035
version: 20
---

**Otimização da Integração bancaria**

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *Backoffice Linha RM* |
| **Módulo:** | TOTVS Gestão Financeira |

**Descrição**

Com o objetivo de otimizar o processo bancário, o sistema foi evoluído para permitir a integração bancária (remessa e retorno de arquivos) com menor interferência do usuário através da opção de agendamento de processo. Esse cenário se assemelha com uma ferramenta de VAN pois não necessita da manipulação do arquivo dentro do sistema, mas ainda requer troca de arquivos manual com o banco.

Nesse conceito o Totvs Gestão Financeira gera os arquivos remessa dos boletos emitidos, de forma automática, direcionando para uma pasta parametrizada de onde os bancos irão lê-los para processamento. Após o processamento o banco disponibiliza os arquivos de retorno numa pasta padrão de onde a nossa aplicação irá ler, de forma automática e com periodicidade parametrizável, e processar os arquivos.

Para a implementação do processo será necessário a parametrização/execução dos seguintes processos:

* Parametrização da remessa
* Agendamento da remessa
* Validação da execução da remessa
* Exclusão do agendamento da remessa
* Parametrização do retorno
* Agendamento do retorno
* Validação da execução do retorno
* Exclusão do agendmaneto o retorno

**Obs**: As imagens utilizadas ao longo do documento são meramente ilustrativas e retiradas da execução do Totvs Gestão Financeira em base com dados de teste.

Parametrização da Remessa1Parametrização da Remessa

**Parametrização**

Para disponibilizar o recurso, deve ser habilitado a opção *Remessa de Cobrança em lote* no cadastro de perfil do usuário.

Acesse o cadastro do convênio e informe os dados de Remessa de Cobrança. No Diretório de destino informe o caminho de rede, que será o local onde o banco irá fazer a leitura os arquivos gerados.

Para geração de arquivos sequencias, o campo *Nome do Arquivo* deve ser composto por uma parte fixa e por uma parte variável definida pelas seguintes tags:

* DDMMYYYY informação da data de geração do arquivo (parte fixa)
* # caractere para definir o número sequencial do arquivo (parte variável).

[Remessa de Cobrança em Lote](http://tdn.totvs.com/pages/releaseview.action?pageId=331845799)

[Remessa de Pagamento em Lote](http://tdn.totvs.com/display/public/LRM/DT+Remessa+de+Pagamento+em+Lote)

[Remessa de Débito Automático em Lote](http://tdn.totvs.com/pages/viewpage.action?pageId=342296008)

2Agendamento de Remessa

**[Agendamento de Remessa](http://tdn.totvs.com/pages/viewpage.action?pageId=269550188)**

Acesse o Menu *Movimentações Bancárias | Processos em Lote | Remessa de Cobrança em Lote*.

Na visão de Cobrança em Lote, inclua ou selecione o filtro de acordo com as informações do Boleto para o [processo de remessa](http://tdn.totvs.com/pages/viewpage.action?pageId=358455115). Caso deseje salvar em diretório diferente do default cadastrado no convênio, informe no campo *Diretório de destino* o caminho desejado.

**Importante**: O filtro é baseado nos dados do boleto. Ao ser selecionado deve-se referenciar ao código da coligada que será realizado o processo, caso não seja informado o sistema irá executar para todas as coligadas. Como default, o sistema já possui um filtro interno para não carregar boletos do tipo *Débito Automático*, nem com status de remessa cancelado, registrado, registrado online ou baixado, nem com status baixado.

**Agendamento**

Para utilizar esta funcionalidade, é necessário que o ambiente esteja parametrizado para 3 camadas para definir o agendamento e a frequência no qual o processo será executado. Defina quando ocorrerá a primeira execução e a repetição. Para cada execução o sistema irá gerar um arquivo para cada convênio distinto que encontrar nos boletos remetidos no processo.

3Validação do Agendamento de Remessa

**Validação do log do processo de Agendamento**

Para validar a execução da remessa após o agendamento, acesse o Jobs pelo menu *Ambiente | Processos | Gerenciamento de Jobs* e crie um filtro com o campo *Classe do Processo* com “FinRemessaLoteCobDataProc”, com os seguintes Status:

* 2 para “OK”;
* 5 para “Erro”;
* 6 para “Atenção”.

**Obs**.: Poderá ser criado também filtro para data de execução (Campo *Executar em*) caso necessário. No resultado exibido na visão é possível configurar colunas caso deseje exibir somente os campos necessários para validação.

Ao editar o registro é exibido na aba *Resultado da Execução* o log do processo, com dois tipos, um para a geração dos arquivos e outro para informar quais os convênios nomeados com Código da Coligada e Identificador do Convênio, tiveram a remessa concluída. Exemplo:

Após a execução, o sistema irá salvar os arquivos de acordo com o diretório parametrizado no convênio ou no caminho informado no processo. Importante ressaltar a permissão do acesso ao diretório onde os arquivos serão salvos caso estejam sendo enviados para um diretório localizado na rede.

**Cancelamento do Agendamento de Remessa**

Para excluir o agendamento de remessa, acesse o Jobs e monte um filtro com o campo *Classe* *do processo* com “FinRemessaLoteCobDataProc” e *Status* nulo. Sistema retorna o próximo agendamento a ser executado, exclua o registro. Dessa forma não ocorrerá mais execução do processo de forma automática.

4Parametrização do Retorno

**Parametrização do Retorno**

Para disponibilizar o recurso deve ser habilitado a opção *Retorno em Lote/Cobrança (Registrada)* no cadastro de perfil.

O banco deve ter configurado o Layout de retorno de cobrança para o processo, ex:

[Retorno de Cobrança em Lote](http://tdn.totvs.com/pages/viewpage.action?pageId=315910559)

[Retorno de Débito Automático em Lote](http://tdn.totvs.com/pages/viewpage.action?pageId=317301409)

[Retorno de Pagamento em Lote](http://tdn.totvs.com/display/LRM/DT+Retorno+de+Pagamento+em+Lote)

5Agendamento do Retorno

**[Agendamento de Retorno](http://tdn.totvs.com/pages/viewpage.action?pageId=269550188)**

Acesse *Retorno de Cobrança em Lote (Registrada)* no menu *Movimentação Bancária | [Integração Bancária](http://tdn.totvs.com/pages/viewpage.action?pageId=358455115) | Retorno Bancário* e defina os parâmetros:

**Banco**: Banco no qual o layout de retorno de cobrança está informado.

**Pasta de Leitura dos arquivos de retorno**: Caminho onde se encontra os arquivos de retorno que serão processados. Para ambientes que roda em três camadas ou em ambiente CLOUD, é importante selecionar um caminho no qual o servidor que irá executar o processo e o usuário do sistema operacional tenham acesso de leitura/gravação. Serão desconsiderados os arquivo com a extensão .OLD.

**Pasta onde o log de retorno será salvo (opcional)**: Este campo informa o caminho onde será salvo os logs dos arquivos de retorno processados, e caso não seja informado nenhum caminho, o log de execução não será salvo. Para ambientes que roda em três camadas ou em ambiente CLOUD, é importante selecionar um caminho no qual o servidor que irá executar o processo e o usuário do sistema operacional tenham acesso de leitura/gravação.

**Renomear arquivo de retorno processado para extensão .old**: Define se após a execução do processo o arquivo de retorno será renomeado com a extensão .Old. Caso esse parâmetro não seja marcado, na próxima vez que o processo for executado para pasta selecionada, o sistema irá tentar processar-lo novamente.

Os demais parâmetros segue a mesma lógica do retorno de cobrança comum.

**Obs**.:

* A conta caixa que será utilizada para efetuar a baixa será a definida no lançamento e deve estar vinculada ao banco no qual o layout está informado.
* A contabilização será efetuada baseado no evento contábil definido nos default do tipo de documento/campos opcionais do lançamento.

**Agendamento**

É necessário que o ambiente esteja parametrizado para 3 camadas para definir o agendamento e a frequência no qual o processo será executado. Defina quando ocorrerá a primeira execução e a repetição. O sistema processará todos os arquivos disponíveis no diretório informado (com exceção daqueles de extensão **.old**).

6Validação do Agendamento de Retorno

**Validação do log do processo de Retorno**

Para validar a execução da remessa após o agendamento, acesse o Jobs pelo menu *Ambiente | Processos | Gerenciamento de Jobs* e crie um filtro com o campo *Classe do Processo* com “FinRemessaLoteCobDataProc”, com os seguintes Status:

* 2 para “OK”;
* 5 para “Erro”;
* 6 para “Atenção”.

****Obs**.:** Poderá ser criado também filtro para data de execução (Campo *Executar em*) caso necessário. No resultado exibido na visão é possível configurar colunas caso deseje exibir somente os campos necessários para validação.

O registro é exibido na aba Resultado da Execução o log do processo, mostrando as etapas de processamento, a renomeação de arquivo e log salvo (aba Mensagem), exemplo:

**Cancelamento do Agendamento de Retorno**

Para cancelar o agendamento de retorno, basta acessar o Jobs e criar um filtro com o campo *Classe* *do Processo* com “FinRetornoCobrancaLoteData” e *Status* nulo. Sistema retorna o próximo agendamento a ser executado, exclua o registro. Dessa forma não ocorrerá mais a execução do processo de forma automática.
