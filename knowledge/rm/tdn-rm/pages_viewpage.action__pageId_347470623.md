---
content_hash: 800e12191b3ee1631f1e99eda6578da5a8c0a9f4fde9a6b0abe7949d111c416c
fetched_at: '2026-06-29T00:08:54.944371+00:00'
page_id: '347470623'
product: rm
source: tdn-rm
title: RMCTB00004_Preenchimento do Centro de Custo nas Movimentações (Regra Sped /
  ECF)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=347470623
version: 7
---

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Contábil |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | Preenchimento do Centro de Custo nas Movimentações (Regra Sped / ECF) |
| **Ambiente:** |  |
| **Passo a passo:** | **Definição do Processo:**  Este recurso tem como objetivo ajustar toda a movimentação nas quais se enquadrem na seguinte regra:  "Caso a conta contábil tenha movimentação com centro de custo e esta mesma conta contábil tenha movimentação sem centro de custo, a movimentação sem centro de custo deverá ter um centro de custo válido".  Esta regra é em função das validações aplicadas pelo PVA da ECF, pois uma vez que a movimentação de uma determinada Conta Contábil seja por centro de custo as demais movimentações desta conta também deve possuir centro de custo.  Verifique nos parâmetros se a empresa marcou para enviar o Centro de Custo ou Conta Gerencial, através do Menu: Ambiente | Parâmetros | Totvs Gestão Contábil | Rotinas Legais | Avançar | Sped Contábil 1/2 | opção: Considerar para o Centro de Custo| Próprio Centro de Custo.  Informamos que este processo, somente é válido para as empresas que utilizam centro de custo.  Recomendamos que seja criado um novo Centro de Custo para ser utilizado neste processo.  Como o Centro de Custo é informação gerencial e opcional no envio para Sped / ECF você poderá optar em não enviar as informações de Centro de Custo, para isso basta acessar o cadastro de centro de custo e desmarcar a opção “Enviar p/Sped”. Desta forma não precisará executar este processo.  Antes da realização deste processo faça um backup da base de dados.  **DESENVOLVIMENTO/PROCEDIMENTO:**  1- Acesse o menu: Escrituração Contábil | Ferramentas | Preenchimento do Centro de Custo nas Movimentações (Regra Sped / ECF):    Observações necessárias:  Campo: Centro de Custo, informe o centro cadastrado;  Campo: Analisar as movimentações até a data, informe até a data que deseje que o sistema insira o centro de custo nos lançamentos;  Campo: Analisar somente Contas Contábeis que estão sendo enviadas para o Sped Contábil / ECF? Somente marque esta opção se as contas contábeis estiverem devidamente preenchida com a natureza para emissão do Sped, pois o centro de custo somente será preenchido nas movimentações em que as contas contábeis tiveram sua natureza devidamente preenchida, em Cadastros | Contábil |    Não marcando a opção do processo acima, o centro de custo será preenchido normalmente nas movimentações independentemente da classificação da natureza para envio de sped. |
| **Observações:** |  |
