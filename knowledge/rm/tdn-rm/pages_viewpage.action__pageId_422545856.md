---
content_hash: fd5be56220cbd4e3203b0cd2d5cf4a795690f5744fae30a2d15c4f22443542eb
fetched_at: '2026-06-29T00:09:21.187422+00:00'
page_id: '422545856'
product: rm
source: tdn-rm
title: Consulta Autorização/Cancelamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545856
version: 3
---

Após ter sido enviada a solicitação de Autorização ou Cancelamento para a Prefeitura este deve ser consultado.

**Para a Autorização de Emissão**

Crie um filtro que carregue somente os registro que estejam com o status Pendente e selecione-os. Dispare o processo Consulta Autorização/Cancelamento. Se o pedido de Autorização for acatado pela Prefeitura os registros terão seu status alterado para Autorizado. Os movimentos referentes a estas NFS-e permanecerão bloqueados para alterações. Se a prefeitura não acatar a Autorização os registros terão seus status alterados para Rejeitado. Neste caso o log do processo deverá ser consultado para analisar qual erro foi apontado na NFS-e. Os movimentos relacionados a estas NFS-e serão liberados para alterações.

**Para a Autorização de Cancelamento**

Crie um filtro que carregue somente os registros que estejam com o status Cancelamento Pendente e selecione-os. Dispare o processo Consulta  Autorização/Cancelamento. Se o cancelamento tiver sido acatado pela Prefeitura os registro terão seu status alterado para Cancelado e os movimentos referentes a elas serão automaticamente cancelados. Se a Prefeitura não acatar o pedido de cancelamento os registros terão seu status retornado para Autorizada e nada acontecerá com os movimentos referentes a elas.

**Consulta de Autorização/Cancelamento de NFS-e TXT/XML**

Se a filial para a qual está sendo executada a consulta utilizar a integração da NFS-e por arquivo texto ao ser disparado este processo antes dele ser executado será aberta uma tela perguntando a localização do arquivo de retorno. Informe a localização do arquivo de retorno fornecido pela prefeitura e seu nome. Aconselha a gravação do mesmo, no ato do download no site da Prefeitura, no diretório do FTP do TSS (C:\totvssped\ftp\arqger\3505708 - onde 03505708 é o código o município da filial emissora). Após a execução do processo a NFS-e terá seu status alterado para Autorizado ou Cancelado conforme for o caso. Na integração por arquivo texto a NFS-e nunca terá o status Rejeitada uma vez que o site da Prefeitura só disponibiliza retorno de NFS-e autorizada.  Se a NFS-e apresentar erro de validação no site da Prefeitura consulte o item Rejeitar NFS-e TXT/XML para saber como proceder.

Para a automatizar a consulta de NFS-e emitidas por webservice ver .
