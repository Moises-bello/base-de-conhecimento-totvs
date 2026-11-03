---
content_hash: e564295a6e19d560b947bf1d6ac9f5052273b4f6c861c11dffe76ef36411edcb
fetched_at: '2026-06-29T00:09:01.142533+00:00'
page_id: '372550110'
product: rm
source: tdn-rm
title: 2876105 ESOCIALFOP01-5828 - Qualificação Cadastral - erro quando a categoria
  do empregado é 5
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=372550110
version: 1
---

# Qualificação Cadastral

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Qualificação Cadastral |
| **Situação/Requisito:** | Ao executar o processo de Qualificação Cadastral, quando o funcionário é Tipo D, Código Categoria eSocial = 721 e Código Categoria = 5, está retornando o erro de inconsistência no processo de qualificação cadastral: 'O campo CI (Código Contribuinte Individual) encontra-se desabilitado para categoria 5". Este campo retorna desabilitado no cadastro de funcionários, quando o Código de Categoria é 5, não sendo necessário o seu preenchimento. |
| **Solução/Implementação:** | Ajuste para não validar preenchimento do campo CI (validar apenas se o CPF e o PIS estão preenchidos) para funcionário categoria eSocial "721 - Contribuinte individual - Diretor não empregado, com FGTS", correspondente à categoria SEFIP "5 - Diretor não-empregado com FGTS (empresário)" |
| **Tickets relacionados:** | 2876105 |
