---
content_hash: 7152fd840d5df2ba2c5df718d5f82c71ee710fbbe90ecaeed65e24e6f13bd769
fetched_at: '2026-06-28T21:35:19.951238+00:00'
page_id: '224445861'
product: fluig
source: tdn-fluig
title: BPM 020 - Como importar para o fluig um processo do ECM 3 (XML)?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224445861
version: 7
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

**Versão:**Todas as versões

# Ocorrência

No ECM 3.00 havia um processo padrão para registro de não conformidade chamado 'RNC Registro de Não Conformidade'.

Por que não tem esse processo padrão no fluig também?

# Solução

No fluig é possível importar os processos modelados no ECM.

1. Publique o formulário do RNC do ECM 3 no fluig
2. Acesse o ECM 3 > Processos > Exportação de processos
3. Exporte o processo para um arquivo XML
4. Crie um projeto no TDS, acesse *workflow* > *diagrams*
5. Escolha a opção Importar > Importar Processo > Avançar
6. Selecione ECM 3.1, faça o upload do arquivo XML e clique em Concluir
7. Acesse as Propriedades do diagrama.
8. Na aba Formulário, defina o formulário do RNC
9. Exporte o processo para o servidor fluig.
