---
content_hash: 052999d1037444a2e0e6817bf783dda28f19ee0f31e2e182fef17ed2c3e08695
fetched_at: '2026-06-29T00:09:18.579953+00:00'
page_id: '421388728'
product: rm
source: tdn-rm
title: Remessa de Débito Automático em Lote
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388728
version: 4
---

O processo de remessa de débito automático em lote possibilita ao usuário a geração de arquivos de débito automático em lote e multi-coligadas, gerados de acordo com os dados default dos Convênios. Neste processo, os arquivos gerados serão agrupados sempre por convênio, isto é, gerando um arquivo para cada convênio que participar do processo.  
 Para que o processo esteja disponível para o usuário é necessário liberar o acesso a Remessa de débito automático em lote no perfil do usuário. Após a liberação do acesso, no cadastro do convênio na Aba "Remessa Bancária" será necessário preencher os campos:

Código Layout

Layout que será utilizado para realizar a remessa de débito automático.

Diretório de Destino

O diretório de destino para geração dos arquivos, que pode ser parametrizado no convênio ou pode ser informado na tela do processo. Quando informado na tela do processo, o sistema desconsidera o do convênio. Lembrando que o usuário que executa o processo de Remessa em lote deve ter permissões de leitura e escrita no mesmo.

Nome do Arquivo

Por definição, será gerado o arquivo com o nome especificado neste campo.

Extensão

selecionar a extensão do arquivo que será gerado txt ou rem.

Remessa de Débito Automático

Define qual remessa de débito automático o sistema irá utilizar como default durante o processo em lote.  
 A funcionalidade está disponível em Movimentações Bancárias | Processos em Lote | Remessa de Débito Automático em Lote. Ao abrir a tela, clique no botão de incluir filtro e selecione ou crie um filtro de acordo com as informações dos boletos que deverão participar do processo.

Todos os convênios deverão ter cadastrado um diretório default. Os arquivos gerados no processo em lote respeitarão o que está definido como default no convênio, somente o diretório default onde os arquivos serão salvos pode ser alterado na tela do processo.

**Observações:**

Recomenda-se que o filtro selecionado referencie o código da coligada para execução do processo, caso contrário o sistema efetuará o processo para todas as coligadas.

Os arquivos gerados serão agrupados por convênio, por exemplo, se no filtro encontrar dois boletos com convênios diferentes serão gerados dois arquivos. Os arquivos serão gerados de acordo com o diretório informado em cada convênio ou então serão gerados no diretório de destino informado na tela.

Os boletos serão filtrados internamente para não carregar boletos do tipo cobrança.
