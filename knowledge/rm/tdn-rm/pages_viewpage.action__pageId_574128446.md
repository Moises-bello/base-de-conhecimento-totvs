---
content_hash: e697bd0e8c038875f987477853294056d7c28757e27cc1e93a71b9dc75f6a80c
fetched_at: '2026-06-29T00:10:53.003447+00:00'
page_id: '574128446'
product: rm
source: tdn-rm
title: Referência Docs
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=574128446
version: 27
---

1 - No modulo "Gestão de Estoque, Compras e Faturamento", vá em: Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento |  Selecione o menu onde o tipo de movimento desejado esta parametrizado | Edite o tipo de movimento. Na etapa "Fiscal - Nota Fiscal Eletrônica" marque o flag: "Referencia Documentos", conforme imagem abaixo.

2 - No movimento, em Integrações | Referencia Docs. 

A referencia pode ser feita das seguintes formas:

**1 - Botão Associar Docs (Opção recomendada):**  Ao clicar neste botão, será apresentado um Lookup para seleção de NOTAS (com base na parametrização do tipo de movimento) que podem ser associadas ao movimento:

* NF-e
* NFC-e
* NFS-e
* CT-e
* CT-e OS
* NFCom

   Neste Lookup, será apresentado somente movimentos que possuam o status "Autorizado".

**Observação:**O lookup não retorna movimentos cujo a chave de acesso tenha sido incluída na grid, pelo processo de inclusão manual a partir do botão, "Incluir"

**2 - Botão Incluir (inclusão manual)**: Recomendamos que esta opção seja utilizada quando não possuir o movimento com a chave de acesso desejada em suas movimentações. Caso não possua movimento com a chave de acesso desejada, basta preencher uma chave de acesso valida e clicar em: "Incluir". A chave de acesso será incluída na grid.

Campo Chave de Acesso deve ser preenchido somente com números e o tamanho = 44 caracteres.

**Observação**: Ao incluir uma chave de acesso de forma manual, mesmo que exista um movimento na base de dados com a mesma chave de acesso, as informações do movimento não serão carregadas para a grid. Neste Caso, recomendamos que utilize a opção "Associar Docs" e filtre pela chave de acesso, por exemplo.

**IMPORTANTE:**Por não possuir referencia a movimento de entrada, a chave de acesso será gravada no banco de dados (TCHAVEACESSOREF).

Podem ser associados quantos registros desejar, no entanto, não é permitido a inclusão de registros com a chave de acesso duplicada.  Caso exista mais de um movimento referenciado com a mesma chave de acesso, será apresentado mensagem de consistência, impedindo de salvar o movimento.

**IMPORTANTE:** Neste caso, remova o registro em duplicidade e verifique os movimentos referenciados. Não é correto possuir mais de um movimento de entrada com a mesma chave de acesso.

**3 - Copia por Referencia:** Ao realizar o processo de copia por referencia, para os seguintes motivos de referencia:

03 - NF Acompanhamento de Cupom Fiscal;

04 - Devolução de Compra de Mercadorias

05 - Devolução de Venda de Mercadorias

06 - NF Complementar / Retificadora

08 - Devolução material receb. conta e ordem

13 - Devolução Simbólica de Mercadoria em Consignação - Estoque Terceiros

15 - Devolução Mercadoria Consignada não Comercializada - Estoque Terceiros

21 - Cópia NF-e de Ajuste - Cancelamento Indevido

22 - Cópia NF-e de Ajuste - Estorno de Venda

23 - Cópia NF-e de Ajuste - Estorno de Compra

24 - NF-e Produtor Rural - Contra Nota

27 - NF Complementar com Cópia de Itens

30 - Devolução por Recusa

31 - Devolução de Empréstimo

34 - Remessa Parcelada de Exportação

38 - Nota de Débito referente a Juros e Multa

**IMPORTANTE:** Neste caso, para que a chave de acesso seja levada para o movimento de destino, o movimento de origem deve possuir chave de acesso e o movimento de destino deve estar parametrizado conforme primeiro tópico deste documento.

**4 - Relacionamento de Movimentos para Exportação:** Ao referenciando itens de movimento a exportação, cujo o movimento referenciado possua Chave de Acesso e que o modelo de documento seja: 01 (NF de papel), 55 (NF-e), 04 ( Produtor Rural), 2B (Cupom Fiscal maquina), 2C (Cupom Fiscal PDV) e 2D (Cupom Fiscal ECF)

**IMPORTANTE:** Ao realizar o vinculo de itens de exportação, caso o item relacionado atenda os requisitos citados, será incluído um registro contendo suas informações na tela de Referencia NF-e. Ao excluir o item relacionado, a informação na tela de Referencia de NF-e também será excluída.

Caso a chave de acesso do item de exportação referenciado, já existia na tela de referencia de NF-e antes de realizar a o relacionamento e o relacionamento foi criado. Ao excluir o item de relacionamento a chave de acesso será excluída.

A tabela responsável por armazenar as os registros informados no movimento é a **TCHAVEACESSOREF**.

**5 - Botão Zerar Código Numérico:** Após incluir manualmente ou associar a chave de acesso, será possível **Zerar o Código Numérico** marcando a chave de acesso e clicando no botão zerar código numérico.

Importante

Recurso disponível a partir da release 12.1.2205

A chave de acesso é composta por 44 dígitos, sendo que o código numérico possui 8 dígitos e começa na posição 36 e vai até a 43.

**Exemplo:**

| Chave com código numérico | Chave Com código numérico zerado |
| --- | --- |
| 26091003888008000124550010000000019999878692 | 26091003888008000124550010000000019**00000000**2 |
