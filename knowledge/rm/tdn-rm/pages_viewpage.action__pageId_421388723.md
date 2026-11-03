---
content_hash: 3477518b6f16b0744bbeefab09f086d4b8141989eee821a3ab0514d40ae58cde
fetched_at: '2026-06-29T00:09:18.551931+00:00'
page_id: '421388723'
product: rm
source: tdn-rm
title: Remessa de Cobrança em Lote
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388723
version: 7
---

O processo de remessa de cobrança em lote possibilita ao usuário a geração de arquivos de remessa de cobrança eletrônica em lote e multi coligadas, gerados de acordo com os dados default dos Convênios. Neste processo, os arquivos gerados serão agrupados sempre por convênio, isto é, gerando um arquivo para cada convênio que participar do processo.  
    
 Para que o processo esteja disponível para o usuário é necessário liberar o acesso a Remessa de cobrança em lote no perfil do usuário. Após a liberação do acesso, no cadastro do convênio na Aba "Remessa Bancária" será necessário preencher os campos:

Código Layout

Layout que será utilizado para realizar a remessa de cobrança.

Diretório de Destino

O diretório de destino para geração dos arquivos, que pode ser parametrizado no convênio ou pode ser informado na tela do processo. Quando informado na tela do processo, o sistema desconsidera o do convênio. Lembrando que o usuário que executa o processo de Remessa em lote deve ter permissões de leitura e escrita no mesmo.

Nome do Arquivo

Por definição, será gerado o arquivo com o nome especificado neste campo. Pode-se selecionar também a extensão.

Remessa de Cobrança

Define qual cadastro de Cobrança Eletrônica (Movimentações Bancárias / Cadastro Bancário / Cadastro Cobrança) o sistema irá utilizar como default durante o processo em lote.

A funcionalidade está disponível em Movimentações Bancárias | Processos em Lote | Remessa de Cobrança em Lote. Ao abrir a tela, clique no botão de incluir filtro e selecione ou crie um filtro de acordo com as informações dos boletos que deverão participar do processo.

Todos os convênios deverão ter cadastrado um diretório default. Os arquivos gerados no processo em lote respeitarão o que está definido como default no convênio, somente o diretório default onde os arquivos serão salvos pode ser alterado na tela do processo.

**Observações:**

Recomenda-se que o filtro selecionado referencie o código da coligada para execução do processo. Caso contrário o sistema efetuará o processo para todas as coligadas.

Os arquivos gerados serão agrupados por convênio, por exemplo, se no filtro encontrar dois boletos com convênios diferentes serão gerados dois arquivos. Os arquivos serão gerados de acordo com o diretório informado em cada convênio ou então serão gerados no diretório de destino informado na tela.

Os boletos serão filtrados internamente para não carregar boletos do tipo débito automático e com o status cnab cancelado, registrado, registrado online e boletos com status cnab e status baixado.

 Informações Complementares

* [DT - Remessa de Cobrança em Lote](http://tdn.totvs.com/x/p5DHEw)
