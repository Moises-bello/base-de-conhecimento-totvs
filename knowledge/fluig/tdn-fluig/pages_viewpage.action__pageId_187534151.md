---
content_hash: 3b7021ecd4193c37507ae9758666e5ef04a6a21b8d3042b72eae8683f44def7b
fetched_at: '2026-06-28T21:35:19.012945+00:00'
page_id: '187534151'
product: fluig
source: tdn-fluig
title: DES - Exportação de processo para servidor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=187534151
version: 4
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**Fluig Studio

# Ocorrência

Ao tentar exportar um processo para um servidor da plataforma aparece a mensagem 'A definição de formulário pertence a um servidor diferente do servidor atual' e não é permitida a exportação.

# Causa

Isto ocorre quando o processo foi desenvolvido ou importado de outro servidor e não foram alteradas as propriedades do processo antes de efetuar a exportação.

# Solução

Abrir o diagrama do processo na perspectiva Fluig do TDS, clicar sobre a parte branca do diagrama, e acessar a aba 'Properties' > 'Geral'. No campo 'Servidor' selecione o servidor para o qual será exportado o processo.

Para exportar um processo com formulário, na opção 'Formulário', campo 'Definição de formulário', selecione 'Local' e escolha o formulário da pasta local que foi desenvolvido para o processo.

Salve o diagrama e prossiga com a exportação do processo conforme a documentação disponível em .
