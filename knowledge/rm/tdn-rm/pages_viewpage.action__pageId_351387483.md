---
content_hash: a3f36ce6569fd7bff1a7cd2ce91f84acf053e7aa572c18dbc83b9343f3f3f3f3
fetched_at: '2026-06-29T00:08:56.949125+00:00'
page_id: '351387483'
product: rm
source: tdn-rm
title: RMPAT00008_Trocar Código do Patrimônio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=351387483
version: 4
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Totvs Gestão Patrimonial |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | Trocar Código do Patrimônio |
| **Ambiente:** |  |
| **Passo a passo:** | Sempre que for necessário alterar o código do patrimônio o processo de troca deverá ser executado.   Na tela de processo serão apresentados os campos “Código atual” e “Código novo”. O primeiro será preenchido com patrimônios ativos que não tenham sido baixados em período anterior e o segundo deverá receber o novo código. O processo passará pelas seguintes validações:   * Títulos não poderão ter o código alterado. * Os níveis do novo código deverão ser iguais aos níveis da máscara do patrimônio. * O nível anterior deverá ser um título. * O preenchimento do código atual será obrigatório. * O preenchimento do novo código será obrigatório. * Não será possível trocar o código se o patrimônio tiver sofrido uma baixa total e o parâmetro “Desabilitar todos os dados dos bens com baixa total” estiver marcado. * O código atual não poderá ter sido baixado em período anterior. * O código atual deverá existir na base de dados. * O código novo não poderá existir na base de dados.   Passando por estas validações o código do patrimônio será alterado. Em função desta mudança a IPATRIMONIO e demais tabelas que armazenam o código anterior, também será alterada para contemplar o novo código.  **Realizando a Troca de Código de Patrimônio** Acessar: Utilitários | Trocar Código de Patrimônio.  Selecione a opção ao lado do campo ‘Código Atual’ para selecionar o patrimônio.    No filtro digite os valores necessários para que o sistema apresente os patrimônios, ou digite o sinal de percentual e selecione a opção de filtrar, desta forma todos os cadastros de patrimônio aptos para o processo serão apresentados para seleção.    Selecione o respectivo patrimônio.    Preencha o campo ‘Código novo’ e execute.    Por fim será gerado um log informando o que foi realizado durante a execução do processo. |
| **Observações:** |  |
