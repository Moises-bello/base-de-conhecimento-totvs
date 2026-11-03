---
content_hash: a7eae8caa0010db377cb93c83c143128940596a52deb108f99f085dfdcfb08e8
fetched_at: '2026-06-29T00:09:19.216200+00:00'
page_id: '421388829'
product: rm
source: tdn-rm
title: FIN - Desbloqueio de Arquivo de Retorno
type: documentation
url: https://tdn.totvs.com/display/LRM/FIN+-+Desbloqueio+de+Arquivo+de+Retorno
version: 2
---

Esse processo tem por objetivo desbloquear o arquivo de retorno, caso tenha ocorrido algum erro ou interrupção do processo de importação do arquivo retorno, deixando assim o seu status como processando.

Nestes casos, o campo STATUSPROCESSAMENTOARQUIVO da tabela FRETORNOBANCARIO recebe o valor 1 (processando), enquanto o campo HASHFILE fica com um valor hash preenchido.

Para que o arquivo seja desbloqueado e os campos da tabela alterados, permitindo a execução do processo de importação, basta executar o processo de desbloqueio no menu Movimentações Bancárias | Retorno Bancário | Desbloqueio de Arquivo de Retorno.
