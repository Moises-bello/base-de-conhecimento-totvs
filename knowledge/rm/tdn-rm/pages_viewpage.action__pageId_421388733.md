---
content_hash: 181f0dcf9fbb0e973e36cdecc1473f2c1eb73b5935248fb42f69c8246b4faf72
fetched_at: '2026-06-29T00:09:18.644464+00:00'
page_id: '421388733'
product: rm
source: tdn-rm
title: Débito Automático
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388733
version: 7
---

O processo de "Retorno de Débito Automático em Lote", visa realizar o retorno de débito automático de maneira rápida e eficaz dentro do TOTVS Gestão Financeira, possibilitando ao usuário, de uma só vez, efetuar o processo para vários arquivos de retorno que estejam localizados num diretório em comum e que pertençam à um mesmo Banco. Os arquivos processados poderão conter informações de várias coligadas. O sistema processará as linhas referentes a cada coligada de forma separada.

O usuário terá as mesmas opções, salvo algumas exceções, que já existem no processo de retorno tradicional, porém com a grande diferença de poder informar, ao invés do arquivo, o diretório dos arquivos de retorno.  
O sistema irá processar todos os arquivos de retorno deste diretório, de acordo com as opções selecionadas durante o processo.

Os logs do processo poderão ser salvos numa pasta também definida pelo usuário e o sistema irá gerar um log para cada arquivo processado.  
Além disso é possível também ao usuário, o agendamento e posterior execução em horário definido, poupando recursos e deixando o processo mais assertivo.

**Parâmetros e execução**  
Para realizar o retorno de débito automático em lote, acessar Movimentações bancárias | Retorno Bancário | Retorno Débito Automático em Lote.   
Detalhamento rápido das opções do processo:

Banco

Os arquivos processados serão somente do banco selecionado.

Pasta de leitura dos arquivos de retorno

Pasta que o sistema irá ler e processar os arquivos de retorno. O sistema apenas irá processar os arquivos do banco que foi selecionado na opção "Banco". Caso existam arquivos de bancos diferentes no mesmo diretório, o processo terminará com ressalvas e estes arquivos não serão processados. O usuário deve ter permissão de leitura / escrita neste diretório onde o processo será executado.

Buscar os arquivos de retorno na máquina local

Marque essa opção caso o caminho da pasta de leitura dos arquivos de retorno a ser considerada esteja em sua máquina local, trazendo diferença no processamento principalmente quando tratarmos de ambiente em 3 camadas ou Cloud.

Disponível a partir da versão 12.1.31.

**IMPORTANTE:** Esse comportamento só surtirá efeito em execuções manuais, os agendamentos não irão interpretar esse parâmetro.

Pasta onde o log do retorno será salvo (opcional)

Permite ao usuário salvar todos os logs de retorno gerados durante o processo, para conferência. É recomendado que esta opção seja sempre marcada caso o processo seja executado via agendamento.  
A opção "Renomear arquivo de retorno processado para extensão .old" fará com que o arquivo processado, tenha sua extensão alterada para .old, desta forma em importações subsequentes estes arquivos serão ignorados.

Formato do arquivo de retorno

É possível definir Febraban CNAB 150 posições ou Febraban CNAB 240 posições, marque a opção que esteja trabalhando.

**Observações sobre o processo**

A baixa deverá acontecer sempre na conta caixa do Lançamento.

O sistema irá ler todos os arquivos existentes no diretório selecionado. Dessa forma, o usuário é responsável por manter nesse diretório apenas os arquivos de débito automático para o banco parametrizado e ainda não lidos, certificando-se que a flag "Renomear arquivo de retorno processado para extensão .old" esteja marcada, caso necessite manter um histórico dos arquivos já processados.

A contabilização será gerada de acordo com o evento para baixa contábil cadastrado como default. A parametrização referente a diferença a maior e a menor será considerada as que foram definidas no parametrizador do menu "Ambiente | Parâmetros | TOTVS Gestão Financeira | Contas a Receber |  Cobrança Eletrônica | Valor default para diferença em retorno bancário.

Caso esteja em ambiente 3 camadas, será possível definir um agendamento ou a frequência no qual o processo será executado. Com essa funcionalidade o usuário poderá automatizar o retorno de débito automático, tendo que apenas definir um mecanismo para atualizar a pasta de leitura com os arquivos que serão processados.

 Informações Complementares

* [DT - Retorno de Débito Automático em Lote](http://tdn.totvs.com/x/oaLpEg)
