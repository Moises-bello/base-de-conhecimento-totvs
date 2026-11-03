---
content_hash: 9d5768aefbcfd46d537223f89c004156ea9e6508cca8e60c9e58efbc81db3969
fetched_at: '2026-06-29T00:09:18.489947+00:00'
page_id: '421388707'
product: rm
source: tdn-rm
title: Pagamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Pagamento
version: 18
---

O processo de "Retorno de Pagamento em Lote", visa realizar o retorno de pagamento de maneira rápida e eficaz dentro do TOTVS Gestão Financeira, possibilitando ao usuário, de uma só vez, efetuar o processo para vários arquivos de retorno que estejam localizados num diretório em comum e que pertençam à um mesmo Banco. Os arquivos processados poderão conter informações de várias coligadas. O sistema processará as linhas referentes a cada coligada de forma separada.

O usuário terá as mesmas opções, salvo algumas exceções, que já existem no processo de retorno tradicional, porém com a grande diferença de poder informar, ao invés do arquivo, o diretório dos arquivos de retorno.  
O sistema irá processar todos os arquivos de retorno deste diretório, de acordo com as opções selecionadas durante o processo.

Os logs do processo poderão ser salvos numa pasta também definida pelo usuário e o sistema irá gerar um log para cada arquivo processado.  
Além disso é possível também ao usuário, o agendamento e posterior execução em horário definido, poupando recursos e deixando o processo mais assertivo.

**Parâmetros e execução**

Para realizar o retorno de pagamento em lote, acessar Movimentações bancárias | Retorno Bancário | Retorno Pagamento em Lote.  
Detalhamento rápido das opções do processo:

Banco

Os arquivos processados serão somente do banco selecionado.

Pasta de leitura dos arquivos de retorno

Pasta que o sistema irá ler e processar os arquivos de retorno. O sistema apenas irá processar os arquivos do banco que foi selecionado na opção "Banco". Caso existam arquivos de bancos diferentes no mesmo diretório, o processo terminará com ressalvas e estes arquivos não serão processados. O usuário deve ter permissão de leitura / escrita neste diretório onde o processo será executado.

Buscar os arquivos de retorno na máquina local

Marque essa opção caso o caminho da pasta de leitura dos arquivos de retorno a ser considerada esteja em sua máquina local, trazendo diferença no processamento principalmente quando tratarmos de ambiente em 3 camadas ou Cloud.

**IMPORTANTE:** Esse comportamento só surtirá efeito em execuções manuais. Ressaltamos que nos casos de utilização de agendamentos o sistema não interpreta esse parâmetro, nesse caso o sistema não vai conseguir localizar/importar no diretório parametrizado os arquivos que seriam lidos na execução seguinte.

Pasta onde o log do retorno será salvo (opcional)

Permite ao usuário salvar todos os logs de retorno gerados durante o processo, para conferência.

Renomear arquivo de retorno processado para extensão .old.

A opção fará com que o arquivo processado, tenha sua extensão alterada para .old, desta forma em importações subsequentes estes arquivos serão ignorados.

* **Atenção:** Quando a opção Buscar os arquivos de retorno na máquina local estiver marcada e for realizado o a agendamento do processo, não ocorrerá a renomeação do(s) arquivo(s).

Histórico

Indique o Histórico para os registros do extrato, e se não for  indicado será utilizado e "Histórico default da Baixa a Pagar" parametrizado pelo Assistente de Implantação de processos, etapa 02.01 Contas a Pagar / Baixas a Pagar.

Retorno de cobrança CNAB240

Marque esta opção caso esteja trabalhando com arquivos no padrão CNAB240.

Contabilizar posteriormente

Marque esta opção caso a contabilização precise ocorrer em momento diferente do retorno.

**Observações sobre o processo:**

A baixa deverá acontecer sempre na conta caixa do lançamento.

O sistema irá ler todos os arquivos existentes no diretório selecionado. Dessa forma, o usuário é responsável por manter nesse diretório apenas os arquivos de pagamento para o banco parametrizado e ainda não lidos, certificando-se que a flag "Renomear arquivo de retorno processado para extensão .old" esteja marcada, caso necessite manter um histórico dos arquivos já processados.

A contabilização será gerada de acordo com o evento para baixa contábil cadastrado como default.

A parametrização referente a diferença a maior e a menor será considerada as que foram definidas no sistema no menu "Ambiente | Parâmetros | TOTVS Gestão Financeira | Contas a Pagar | Pagamento Eletrônica | Valor default para diferença em retorno bancário.

Caso esteja em ambiente 3 camadas, será possível definir um agendamento ou a frequência no qual o processo será executado. Com essa funcionalidade o usuário poderá automatizar o retorno de pagamento, tendo que apenas definir um mecanismo para atualizar a pasta de leitura com os arquivos que serão processados.

Não há a opção do usuário liberar um arquivo já processado anteriormente já que é feita a manipulação de um diretório em processamento posterior e não de arquivos informados manualmente.

 Informações Complementares

* [DT -  Retorno de Pagamento em Lote](http://tdn.totvs.com/display/public/LRM/DT+Retorno+de+Pagamento+em+Lote)
* [Integração bancária via sistema VAN](http://tdn.totvs.com/pages/viewpage.action?pageId=389554035)
