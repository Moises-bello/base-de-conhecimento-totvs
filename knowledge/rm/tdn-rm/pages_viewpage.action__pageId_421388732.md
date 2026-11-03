---
content_hash: 4ab5be81b419fde045838711ff31a4abd9be1da32b7c3634f29dc6044e07663f
fetched_at: '2026-06-29T00:09:18.640037+00:00'
page_id: '421388732'
product: rm
source: tdn-rm
title: Remessa de Pagamento em Lote
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388732
version: 13
---

O processo de remessa de pagamento em lote possibilita ao usuário a geração de arquivos de remessa de pagamento em lote e multi-coligadas, gerados de acordo com os dados default dos Convênios. Neste processo, os arquivos gerados serão agrupados sempre por convênio, isto é, gerando um arquivo para cada convênio que participar do processo.

Para que o processo tenha inicio são necessários alguns pré requisitos na parametrização de convênio. Na Aba "Remessa Bancária", será necessário preencher os campos:

Código Layout

Layout que será utilizado para realizar a remessa de pagamento.

Diretório de Destino

O diretório de destino para geração dos arquivos, que pode ser parametrizado no convênio ou pode ser informado na tela do processo. Quando informado na tela do processo, o sistema desconsidera o do convênio. Lembrando que o usuário que executa o processo de Remessa em lote deve ter permissões de leitura e escrita no mesmo.

Download dos arquivos gerados para máquina local

Os arquivos gerados na remessa em lote serão salvos no diretório local escolhido.

Nome do Arquivo

Por definição, será gerado o arquivo com o nome especificado neste campo. Pode-se selecionar também a extensão.

Remessa de Pagamento

Define qual remessa de pagamento o sistema irá utilizar como default durante o processo em lote.  
A funcionalidade está disponível em Movimentações Bancárias | Processos em Lote | Remessa de Pagamento em Lote. Ao abrir a tela, clique no botão de incluir filtro e selecione ou crie um filtro de acordo com as informações dos boletos que deverão participar do processo.

Todos os convênios deverão ter cadastrado um diretório default. Os arquivos gerados no processo em lote respeitarão o que está definido como default no convênio, somente o diretório default onde os arquivos serão salvos pode ser alterado na tela do processo.

**Obs**:

Recomenda-se que o filtro selecionado referencie o código da coligada para execução do processo. Caso contrário o sistema efetuará o processo para todas as coligadas.

Caso esteja parametrizada a "Contabilização de Mútuo" disponível em Integração Contábil | Contabilização, será possível gerar arquivos de remessa para convênios não pertencentes à coligada do contexto.  Isso ocorrerá nas situações onde, junto à parametrização da Contabilização de Mútuo, o usuário associar um convênio à lançamentos de coligadas diferentes da coligada proprietária dele.

  Informações Complementares

* [DT - Remessa de Pagamento em Lote](http://tdn.totvs.com/x/rlcrF)
