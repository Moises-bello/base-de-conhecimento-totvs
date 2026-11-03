---
content_hash: 1b1be2338436f43df289540f716af0bea7ca7b43fc8342a6e11860aea3af5554
fetched_at: '2026-06-29T00:11:27.437253+00:00'
page_id: '725724775'
product: rm
source: tdn-rm
title: Cobrança - Processamento distribuído
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=725724775
version: 8
---

**Disponível à partir da release 12.1.2302**

O processo de "Cobrança - Processamento distribuído" possui praticamente as mesmas características do processo "Cobrança (Registrada)". O que difere entre os processos é a possibilidade de fracionar a execução em jobs, mediante configuração da escalabilidade disponível (em ambientes configurados em N camadas) na etapa do agendamento do processo.

O sistema criará os jobs de acordo com o número de partes definido na tela do agendamento do processo. Exemplo: Se tiver um arquivo no diretório definido e o mesmo tiver 100 linhas de detalhe (boleto), ao definir 5 partes na tela citada acima, cada job vai processar 20 linhas. Quando tiver mais de um arquivo no diretório a lógica será a mesma. Cada linha detalhe do (s) arquivo (s) será separada por job.

Obs: Ao processar vários arquivos de retorno, se o mesmo nosso número estiver sendo referenciado em mais de um arquivo, todas as referências deste nosso número serão processados pela mesma fila de processamento, ou seja, pelo mesmo job.

**Parâmetros e execução**

Para realizar o retorno de cobrança com o processamento distribuído, acesse o menu Movimentações Bancárias | Retorno Bancário | Retorno em Lote | Cobrança - Processamento distribuído. Detalhamento rápido das opções do processo:

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

Quando marcada essa opção o sistema fará com que o arquivo processado tenha sua extensão alterada para .old, desta forma em importações subsequentes estes arquivos serão ignorados. Assim o arquivo processado será renomeado independente se o processamento foi bem sucedido. 

Histórico

Define um histórico que será levado para o item de baixa gerado pelo retorno e também para o extrato de caixa.

Retorno de cobrança CNAB240

Marque esta opção caso esteja trabalhando com arquivos no padrão CNAB240.

Retorno de cobrança PIX 750

Marque esta opção caso esteja trabalhando com arquivos no padrão de layout do Banco Central (750 posições).

Contabilizar posteriormente

Marque esta opção caso a contabilização precise ocorrer em momento diferente do retorno.

Usar data compensação como data contabilização baixa

Mesmo comportamento do retorno tradicional. O sistema irá preencher o campo DATACONTABILIZBX na FLANBAIXA e DATACONTABILIZBX na FRETORNOBANCARIOITEM com a data de compensação que está informada no arquivo.

Exibir no log informações dos lançamentos relacionados a cada boleto

O sistema irá exibir no log informações de todos os lançamentos que compõem o boleto de cobrança.

Cobrança partilhada (disponível apenas para o Banco Santander - Febraban 033)

O sistema também processará os registros de partilha contidas no arquivo de retorno importado. Ressaltamos a necessidade de preencher as posições correspondentes a Partilha no [layout bancário](https://tdn.totvs.com/pages/viewpage.action?pageId=421388586) do cadastro do Banco **Santander (033)**. 

* Vídeo com a demonstração do retorno de cobrança com processamento distribuído
