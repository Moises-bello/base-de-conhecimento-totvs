---
content_hash: bc1e6e6a2d2df4be3bdc89baca4cd584868f4a19d43c23f21077716fec4d6f9f
fetched_at: '2026-06-28T21:35:22.233843+00:00'
page_id: '235326727'
product: fluig
source: tdn-fluig
title: BPM 028 - Por que a imagem do diagrama do processo não foi atualizada ao exportar
  uma nova versão?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235326727
version: 7
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

**Versão:** todas

# Ocorrência

Exportamos uma nova versão do processo mas a imagem do diagrama não foi atualizada. Verificamos que a solicitação está seguindo o novo fluxo, somente a imagem ficou desatualizada.

Imagem do diagrama exibida na inicialização de uma nova solicitação:

Imagem do diagrama exibida no editor de processos:

# Causa

Acreditamos que este problema ocorreu devido ao *lock* de arquivos na *workspace* utilizada. Apenas para entendimento, quando é feita a exportação de um processo para o fluig, são criados alguns arquivos na pasta *.resources* no diretório [workspace] \ [projeto] \ workflow.

A cada nova exportação, o plugin do fluig recria estes arquivos para enviá-los atualizados ao servidor. Já tivemos relatos de problemas onde ocorreu bloqueio dos arquivos (*lock*) pelo próprio sistema operacional ou aplicações terceiras, não permitindo a atualização. Assim, o arquivo desatualizado é enviado ao servidor fluig, gerando inconsistências semelhantes à esta que foi reportada acima.

# Solução

Para solucionar esta inconsistência, acesse a pasta *.resources* e busque por todos os arquivos (.xml, .png, .svg, etc.) cujo o nome seja o código do processo e faça a remoção.

Por fim, faça uma nova exportação do processo e verifique se o problema foi solucionado.
