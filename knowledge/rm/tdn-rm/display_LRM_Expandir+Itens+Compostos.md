---
content_hash: 73cba4cc608f10f0823dc1caf0031ec4c4016de979dc4a7b93f75d68398918b1
fetched_at: '2026-06-29T00:10:53.055864+00:00'
page_id: '574653715'
product: rm
source: tdn-rm
title: Expandir Itens Compostos
type: documentation
url: https://tdn.totvs.com/display/LRM/Expandir+Itens+Compostos
version: 4
---

Na janela de edição de Movimentos, página Itens de movimentos, poderá aparecer o ícone  , quando o parâmetro **Utilizar produto composto** na **Etapa Itens Identificação 2/2**do tipo de movimento estiver marcado. Utilize este ícone para desmembrar produtos que tenham produtos compostos cadastrados no anexo  no cadastro de Produto. Este recurso pode expandir até o último nível ou apenas um nível os itens com produto composto no movimento.

**Exemplo:**

Produto A é composto por B e C.

Produto B é composto por D e F.

Tendo um item de movimento com o produto A e a expansão for completa (até o último nível) teremos ao final do processo três novos itens, com os produtos C, D e F (A foi decomposto em B e C e B foi decomposto para D e F). Se a expansão não for completa será de apenas um nível, e assim ao final do processo teremos somente dois itens, um com B e outro com C. A escolha é feita através de uma mensagem ao clicar no botão de expansão.

Clicando no botão **Sim** a expansão será completa, no botão **Não** será de apenas um nível, e no **Cancelar** o processo é cancelado.

Devem ser observadas também as quantidades. Se, por exemplo, A é composto de 2 quantidade de B e B é composto de 4 quantidades de D, ao final de expansão teremos um item com o produto D com quantidade 8. As quantidades são definidas no produto quando se informa quais são seus produtos compostos.

Quando o item de movimento possuir valor no campo **Taxa de Juros,**ao realizar a expansão, o primeiro item expandido do produto composto vai assumir o valor dos Juros.

Informação 

Para se utilizar produto composto devemos parametrizar o Produto em **Parâmetros Gerais \ Tabelas \ Produtos \ Definições Gerais 3/3** parâmetro **Produto Composto**como marcado.

E o tipo de movimento estar configurado na **Etapa Itens Identificação 2/2,** parâmetro **Utilizar Produto Composto** como marcado.
