---
content_hash: ac3431b2f27b7afbbfcb90a679f5ca71bb801719ab39c0676a58f239d6515856
fetched_at: '2026-06-29T00:09:00.109871+00:00'
page_id: '364917857'
product: rm
source: tdn-rm
title: RM - Erro - O campo 'nisTrab' do registro 'trabalhador' é obrigatório e não
  está preenchido.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364917857
version: 4
---

Erros e AçõesErro

Erro: O campo 'nisTrab' do registro 'trabalhador' é obrigatório e não está preenchido.

Ação

Ação:

* Acesse o cadastro do funcionário, clique em Documentação e verifique se o número do PIS/PASEP está preenchido:

* Caso o funcionário seja autônomo, a informação deve ser preenchida no campo Código Contribuinte Individual:

* Se o funcionário for um autônomo e um cliente fornecedor, é necessário avaliar se está preenchido o NIT. Nestes casos, o sistema considera o NIT na geração do XML, caso contrário, retorna o número do Contribuinte (Tributos/Pessoa Física):

**Validação realizada conforme o mapeamento:**

|  |
| --- |
| Caso seja autônomo e FCFO.NIT estiver preenchido, retorna FCFO.NIT, caso contrário, retorna FCFO.CIAUTONOMO;    Caso não seja autônomo e codCateg diferente de contribuinte individual (721, 722, 723, 731, 734, 738, 761, 771) retorna PFUNC.PISPASEP, caso contrario, retorna PFUNC.CI |
