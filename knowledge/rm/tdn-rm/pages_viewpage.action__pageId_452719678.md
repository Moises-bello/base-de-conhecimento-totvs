---
content_hash: bc59957627752fb409582df89b6cc0ad7154e6f151885f7e5bd180f5b09239d3
fetched_at: '2026-06-29T00:10:09.482202+00:00'
page_id: '452719678'
product: rm
source: tdn-rm
title: Roteiro para informar autônomos do RM Fluxus no MANAD
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719678
version: 2
---

Abaixo estão os procedimentos para o correto cadastramento do autônomo bem como o lançamento de sua movimentação no TOTVS Gestão Financeira para que esses valores sejam reconhecidos na geração dos arquivos MANAD.

Vale ressaltar que recomendamos o preenchimento do maior número de informações em todos os cadastros aqui apresentados. Porém, para evitar um roteiro muito grande e redundante, citaremos aqui somente aqueles que o sistema trata na utilização da informação na geração do MANAD.

**PASSO 01:** Cadastrar / verificar o cadastro do Autônomo.  
 Mesmo parecendo uma informação irrelevante, o campo Categoria, no cadastro do autônomo é de grande importância nesse processo. O MANAD, assim como o SEFIP e a GPS, no RM Labore, busca lançamentos financeiros realizados para Cli/For cadastrados como pessoa física. Portanto, é de extrema relevância a conferência desse campo.  
 Outros dados cadastrais importantes nessa verificação são os Dados Relacionados ao INSS. Se esses dados não forem preenchidos, ao realizar a importação do arquivo do MANAD no aplicativo SVA, no Resumo da Validação serão apontados erros de cadastro em relação aos autônomos do RM Fluxus.

**PASSO 02:** Cadastrar / verificar o cadastro do Tipo de Documento.  
 Verificar o Tipo de Documento também é de grande relevância. Somente documentos de classificação Gera INSS ou Gera INSS e IRRF conseguem fazer com que o TOTVS Gestão Financeira calcule o valor da base e desconto da contribuição previdenciária, na geração do lançamento.  Se não houverem essas informações no registro do lançamento, o sistema não considera o mesmo na composição do MANAD.

**Observação:** Caso o lançamento tenha sido realizado com o tipo de documento cadastrado de forma incorreta e, logo após, o mesmo foi corrigido ou trocado no lançamento, será necessário cancelar o lançamento de gerá-lo novamente.

**PASSO 03:** Cadastrar / verificar o Lançamento Financeiro.  
 Esse é o cadastro com o maior número de detalhes. Se algum dos campos aqui citados for preenchido de forma incorreta, o lançamento pode ser até mesmo desconsiderado na geração do arquivo do MANAD. Nesse processo, deve-se lembrar que, ao salvar o registro do lançamento, o sistema bloqueia algumas informações e, no caso de lançamentos já baixados, nenhuma das informações poderá ser alterada.  
 Na aba Identificação é que encontramos o maior número de informações. São elas:

**Filial**  
 Nesse campo deve ser utilizada um código de filial que tenha sido associado a pelo menos uma seção do RM Labore.

**Tipo de Documento**  
 Como explicado no passo anterior, deve ter classificação Gerar INSS ou Gerar INSS e IRRF para que o desconto previdenciário possa ser calculado.

**Datas do Lançamento**  
 Aqui, pelo menos a data de emissão deve estar dentro do período das informações usado na geração do arquivo do MANAD.  
 Na aba Valores, sub aba Gerais, ao menos o campo Valor Original deve estar preenchido.  
 Na aba Valores, sub aba Tributos, o campo Valor do Serviço deve estar preenchido. Esse campo é utilizado no cálculo dos valores de previdência social. Ainda nessa tela é necessário clicar no ícone onde aparece um sinal de exclamação. Ao clicar no botão citado será aberta uma nova janela. Nessa tela será necessário clicar sobre o botão de recálculo (raio), para que o sistema processe o cálculo do desconto de INSS.  
 Depois de realizado o cálculo conforme abaixo, na aba Valores, sub aba Tributos, o campo Valor do INSS deverá ficar preenchido.
