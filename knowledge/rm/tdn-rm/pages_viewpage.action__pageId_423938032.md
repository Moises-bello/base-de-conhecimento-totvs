---
content_hash: cd08d6bdee314556e9fd3367bf2e9b3b6e683261f21af9793703bbc763f4bd26
fetched_at: '2026-06-29T00:09:24.823355+00:00'
page_id: '423938032'
product: rm
source: tdn-rm
title: Trocar Código do Patrimônio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938032
version: 2
---

Sempre que for necessário alterar o código do patrimônio o processo de troca deverá ser executado. Na tela de processo serão apresentados os campos "Código atual" e "Código novo". O primeiro será preenchido com patrimônios ativos que não tenham sido baixados em período anterior e o segundo deverá receber o novo código. O processo passará pelas seguintes validações:

* Títulos não poderão ter o código alterado.
* Os níveis do novo código deverão ser iguais aos níveis da máscara do patrimônio.
* O nível anterior deverá ser um título.
* O preenchimento do código atual será obrigatório.
* O preenchimento do novo código será obrigatório.
* Não será possível trocar o código se o patrimônio tiver sofrido uma baixa total e o parâmetro "Desabilitar todos os dados dos bens com baixa total" estiver marcado.
* O código atual não poderá ter sido baixado em período anterior.
* O código atual deverá existir na base de dados.
* O código novo não poderá existir na base de dados.

Passando por estas validações o código do patrimônio será alterado. Em função desta mudança a IPATRIMONIO e demais tabelas que armazenam o código anterior, também será alterada para contemplar o novo código. Por fim será gerado um log informando o que foi realizado durante a execução do processo.
