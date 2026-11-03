---
content_hash: 17801f8ea5d926b1cc0684c7dce008d48927a7a8bdd65fc2977d9f659644d39e
fetched_at: '2026-06-29T00:09:18.655007+00:00'
page_id: '421388736'
product: rm
source: tdn-rm
title: Cobrança (Registrada)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388736
version: 10
---

O processo de "Retorno de Cobrança Registrada em Lote", visa realizar o retorno de cobrança registrada de maneira rápida e eficaz dentro do TOTVS Gestão Financeira, possibilitando ao usuário, de uma só vez, efetuar o processo para vários arquivos de retorno que estejam localizados num diretório em comum e que pertençam à um mesmo Banco. Os arquivos processados poderão conter informações de várias coligadas. O sistema processará as linhas referentes a cada coligada de forma separada. O usuário terá as mesmas opções, salvo algumas exceções, que já existem no processo de retorno tradicional, porém com a grande diferença de poder informar, ao invés do arquivo, o diretório dos arquivos de retorno.

O sistema irá processar todos os arquivos de retorno deste diretório, de acordo com as opções selecionadas durante o processo.

Os logs do processo poderão ser salvos numa pasta também definida pelo usuário e o sistema irá gerar um log para cada arquivo processado. Além disso é possível também ao usuário, o agendamento e posterior execução em horário definido, poupando recursos e deixando o processo mais assertivo.

**Parâmetros e execução**

Para realizar o retorno de cobrança registrada em lote, acessar Movimentações bancárias | Retorno Bancário| Retorno de Cobrança Registrada em Lote.  
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

Renomear arquivo de retorno processado para extensão .old

Quando marcada essa opção o sistema  fará com que o arquivo processado tenha sua extensão alterada para .old, desta forma em importações subsequentes estes arquivos serão ignorados. Assim o arquivo processado será renomeado independente se o processamento foi bem sucedido. 

Histórico

Define um histórico que será levado para o item de baixa gerado pelo retorno e também para o extrato de caixa.

Retorno de cobrança CNAB240

Marque esta opção caso esteja trabalhando com arquivos no padrão CNAB240.

Usar data compensação como data contabilização baixa

Mesmo comportamento do retorno tradicional. O sistema irá preencher o campo DATACONTABILIZBX na FLANBAIXA e DATACONTABILIZBX na FRETORNOBANCARIOITEM com a data de compensação que está informada no arquivo.

Contabilizar posteriormente

Marque esta opção caso a contabilização precise ocorrer em momento diferente do retorno.

Exibir no log informações dos lançamentos relacionados a cada boleto

O sistema irá exibir no log informações de todos os lançamentos que compõem o boleto de cobrança.

Cobrança partilhada (disponível apenas para o Banco Santander - Febraban 033)

O sistema também processará os registros de partilha contidas no arquivo de retorno importado. Ressaltamos a necessidade de preencher as posições correspondentes a Partilha no [layout bancário](https://tdn.totvs.com/pages/viewpage.action?pageId=421388586) do cadastro do Banco **Santander (033)**. 

**Observações sobre o processo:**

* A baixa deverá acontecer sempre na conta caixa do Lançamento.
* O sistema irá ler todos os arquivos existentes no diretório selecionado. Dessa forma, o usuário é responsável por manter nesse diretório apenas os arquivos de cobrança para o banco parametrizado e ainda não lidos, certificando-se que a flag "Renomear arquivo de retorno processado para extensão .old" esteja marcada, caso necessite manter um histórico dos arquivos já processados.
* A contabilização será gerada de acordo com o evento para baixa contábil cadastrado como default.
* O parâmetro de baixa a menor ou a maior não poderá ser mudado. Será utilizado o que está definido nos parâmetros da coligada (Contas a Receber | Integração Bancária | Cobrança Eletrônica | Valores Default para diferença em retorno bancário).
* O parâmetro "diferença para geração de baixa parcial" e "diferença para geração de adiantamento" também serão respeitados.
* Não há a opção do usuário liberar um arquivo já processado anteriormente já que é feita a manipulação de um diretório em processamento posterior e não de arquivos informados manualmente.

Informações Complementares

* [Integração bancária via sistema VAN](http://tdn.totvs.com/pages/viewpage.action?pageId=389554035)
