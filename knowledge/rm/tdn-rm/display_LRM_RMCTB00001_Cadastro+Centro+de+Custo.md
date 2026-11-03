---
content_hash: 2ab23f0c3a776c98b30445490daa3739de8ff15ffc62d27456de0a917c3e8a47
fetched_at: '2026-06-29T00:08:48.773366+00:00'
page_id: '327331678'
product: rm
source: tdn-rm
title: RMCTB00001_Cadastro Centro de Custo
type: documentation
url: https://tdn.totvs.com/display/LRM/RMCTB00001_Cadastro+Centro+de+Custo
version: 6
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS GESTÃO CONTÁBIL |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | Cadastro de Centro de Custo |
| **Ambiente:** | Novo Modelo BackOffice |
| **Passo a passo:** | **Definição do Processo:**  Para cumprir as principais necessidades contábeis ou fiscais de distribuição de custos da empresa, os Centros de Custos poderão ser cadastrados e vinculados às filiais, permitindo que as contas de resultado sejam devidamente distribuídas em seus respectivos centros de custo.  **Parametrização Necessária**  1 - Antes de cadastrar os centro de custos, deve-se criar a máscara que será utilizada no Centro de custo, acesse o menu: Ambiente | Parâmetros | Parâmetros Globais.  Utilizando o símbolo #, insira a hierarquia que os códigos de centros de custos deverão possuir:    **Importante** Esta máscara **não** poderá ser alterada após algum cadastro do centro de custo, ou seja, se houver algum cadastro já salvo, a máscara do centro de custo fica desabilitada impossibilitando sua alteração.  Os dados cadastrais poderão ser incluídos e/ou atualizados a partir da janela de edição própria, que reúne todos os centros de custos cadastrados. Acesse o menu Cadastros | Centros de Custos.  **Observação** A opção “Enviar para o SPED Contábil” permite que o cento de custo seja enviado para o arquivo referente ao SPED Contábil.   Para que a opção acima esteja disponível o parâmetro: Próprio Centro de Custo deverá estar marcado. Verifique este parâmetro acessando o menu:Ambiente | Parâmetros | Totvs Gestão Contábil | Rotinas Legais | SPED Contábil e clique em avançar.   No parâmetro "Considerar para o Centro de Custo", marque a opção Próprio Centro de Custo. |
| **Observações:** | Caso existam associações de contas contábeis e contas gerenciais ao plano de contas referencial (SPED Contábil), ao selecionar a opção “Próprio Centro de Custo” e concluir a parametrização, as associações das contas gerenciais serão perdidas. Para desmarcar a opção “Enviar para o SPED Contábil” de um centro de custo, deve-se verificar se o mesmo não está associado a alguma conta paralela (SPED Contábil).  **Saiba mais** Para mais informações acesse [Centros de Custos](https://tdn.totvs.com/display/LRM/Centros+de+Custos). |
