---
article_id: 360020898192
category: NFe - Nota Fiscal Eletrônica
content_hash: 5a1ddad709f1c69b832049a30007a96849b615ecaecf45bbdb8b1548b03dadef
fetched_at: '2026-06-28T22:40:03.652764+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Inclusão de Nota
  de Estorno e Estorno de Devolução (NF de devolução emitida com erros)
type: support-article
updated_at: '2026-06-15T18:26:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020898192-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Inclus%C3%A3o-de-Nota-de-Estorno-e-Estorno-de-Devolu%C3%A7%C3%A3o-NF-de-devolu%C3%A7%C3%A3o-emitida-com-erros
---

**Dúvida**

Como incluir Nota de Estorno e Estorno de Devolução (devido NF de devolução ter sido emitida com erros)?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1. Nota de estorno para ***cancelamento fora do prazo***

2.  ***Emitida Nota de Devolução com erros e por isso o Destinatário Rejeitou*** a NF. Não é mais possível Cancelar esta Nota pois passou do prazo. Como gerar uma nota que estorne essa nota de devolução para, posteriormente, emitir a Nota de devolução corretamente?

Verifique com sua assessoria fiscal ou contábil e com o Posto Fiscal de sua localidade a possibilidade e procedimento a ser adotado para o Cancelamento extemporâneo, de forma que a nota possa ser cancelada e excluída do ERP. Caso o cancelamento / exclusão não seja possível:

a INSTRUÇÃO NORMATIVA RE Nº 098/11 (DOE 29/12/11) indica que seja emitida uma Nota de Estorno: "20.4.2 - Nos casos em que a operação não tenha sido realizada e o cancelamento não tenha sido transmitido no prazo referido no subitem 20.4.1, a correção deve ser realizada através da emissão de NF-e de estorno, com as seguintes características:

***a)** finalidade de emissão da NF-e **(campo FinNFe) = "3 - NF-e de ajuste";***

***b)** descrição da Natureza da Operação **(campo natOp) = "999 - Estorno de NF-e não cancelada no prazo legal";***

***c)** referenciar a chave de acesso da NF-e que está sendo estornada **(campo refNFe);***

***d)** dados de produtos/serviços **e valores equivalentes aos da NF-e estornada;***

***e) códigos de CFOP inversos** aos constantes na NF-e estornada;*

***f)** informar a justificativa do estorno **nas Informações Adicionais de Interesse do Fisco (campo infAdFisco)."***

A emissão desta nota consiste no estorno da operação de devolução, para o fisco. Não consiste, porém, no Protheus, em exclusão das movimentações (Estoque/Financeiro) geradas pela nota de devolução, visto que ela permanece no sistema (não foi excluída - que é o que caracteriza a exclusão das movimentações geradas).

O relacionamento com a nota de Origem (campo NFORI) também não será anulado devido à não exclusão dessa Nota de Devolução.

Ou seja, na emissão da segunda Nota de Devolução, correta, não há como realizar pelo processo convencional (lançamento do Pedido e Emissão de Nota) pois já foi realizado no ERP a amarração entre nota de Origem e nota(s) de Devolução (que permanece lançada) impedindo assim a amarração de mais uma nota de devolução (o que caracterizaria quebra de integridade). A segunda Nota de Devolução deverá então ser emitida pelo processo Manual - Livros Fiscais.

**A primeira Nota de Devolução emitida (com erros) já deve ter realizado a devolução/ajuste de saldo de estoque e título financeiro. Essa operação não deve ser anulada pois a segunda nota de devolução que será emitida (correta) não poderá realizar os ajustes de estoque/financeiro (pois será emitida pelos Livros Fiscais, o qual não possui integração com Estoque/ Financeiro)**

Então:

* Ao emitir a Nota de **Estorno da Devolução**, **não se deve retornar o Estoque / Financeiro** que já foram devidamente devolvidos na primeira devolução (utilizar um TES que não movimenta Estoque/ Financeiro para a Nota de estorno);
* Emitir a segunda nota de Devolução, correta, pelos Livros Fiscais MATA920 - NF Manual de Saída / MATA910 - NF Manual de Entrada (visto que o processo convencional de lançamento do Pedido e Emissão de Nota não são mais aceitos devido impossibilidade de nova amarração com a Nota de Origem)

**Configurações:**

 1. Preencha o parâmetro no configurador ***MV\_NFEMSF4 = F***

![20211203_092708.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414843517975)

2. Preencha o parâmetro no configurador ***MV\_DSAIENT = .F.** para montar a data, e quando informada a hora monte a TAG hSaiEnt.*

![20211203_093616.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414850624151)

3. Incluir uma Fórmula no cadastro de Fórmulas com a mensagem de ***estorno conforme previsto pela sua UF.***

* ***Exemplo Formula:*** "Nf-e nao cancelada no prazo normal, cliente cancelou o pedido"

![20211203_094951.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414857792279)

* Vincular a fórmula ***através dos campos abaixo:***

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar informações na TAG infCpl ou infAdFisco no XML e no DANFE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024950773)

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar mensagem em informações complementares (TAG infcpl e infadfisco) do Danfe utilizando fórmula](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026944871)

Como definir a natureza da operação ***campo natOp = "999 - Estorno de NF-e não cancelada no prazo legal";***

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como configurar o conteúdo da TAG natOp](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020153151--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-configurar-o-conte%C3%BAdo-da-TAG-natOp)

4. Preencha no **TES** para o envio do estorno o campo ***"Ajuste CIAP" = S*** para que o xml seja gerado com a ***Tag FinNFe = 3***

![20211203_095638.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414843777943)

**Inclusão da Nota de Estorno de Devolução**

**CENÁRIO 1:**Emissão de Nota DE SAÍDA (Ou seja, Estorno de uma Devolução de Venda):

A) Foi gerada Nota de Saída - Venda  
  
B) Posteriormente foi gerada Nota de Entrada - Devolução da Venda (Emitida com erros)

C) Agora precisa **gerar uma Nota de Saída - Estorno da Devolução de Venda**

- Incluir um Pedido de Vendas do Tipo Devolução (o nome aparece como Devolução de compra e não devolução de devolução);

- Cadastrar um novo Fornecedor com os mesmos dados do Cliente, e selecionar ele no Pedido de Vendas;

- Registrar nas linhas de item os produtos da nota de devolução (da nota de Entrada), e referenciar a Nota de Devolução digitando manualmente os campos C6\_NFORI, C6\_SERIORI e C6\_ITEMORI (com caracteres exatos, inclusive quantidades de zeros à esquerda);

- Utilizar o TES de Saída devidamente configurado juntamente com teu depto Fiscal de acordo com as incidências desta operação (conforme explicado acima, sem movimentar estoque/financeiro para não devolver uma operação que já foi devolvida com a primeira nota de devolução). Obs: Neste TES deve estar registrado o campo "Ajuste CIAP" = Sim conforme mencionado acima, para que o xml seja gerado com a Tag FinNFe = 3

* **Saiba mais:**

O campo **C6\_ITEMORI** deve ser informado **apenas** quando o registro a qual esta se referenciando (nota e serie) esta devidamente relacionado a entidade (cliente/fornecedor), isso se deve ao fato de que ao ser informado o item as validações da nota e serie origem serem acionadas, caso não seja esta a situação deve ser informado apenas os campos C6\_NFORI e C6\_SERIORI.

* Conforme o ***boletim foi criado o parâmetro:***

*[Clique Aqui](%20%20%20https://tdn.totvs.com/pages/releaseview.action?pageId=566474183)*

​![20211203_100235.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414843849623)

**CENÁRIO 2: Emissão de Nota DE ENTRADA (Ou seja, Estorno de uma Devolução de Compra):**

**A)** Foi incluída uma Nota de Entrada - Compra  
  
**B)** Posteriormente foi gerada Nota de Saída - Devolução da Compra (Emitida com erros)  
  
 **C)** Agora precisa **gerar uma Nota de Entrada - Estorno da Devolução de Compra  :**

**- Verificar o parâmetro** [**MV\_VLDNFO**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020261731-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-desabilitar-mensagem-de-valida%C3%A7%C3%A3o-de-Nota-Fiscal-Origem-no-Documento-de-Entrada)**. Caso esteja habilitado, para esse processo desabilitá-lo, para que o sistema não valide a nota de origem na inclusão da devolução.**

- Incluir um Documento de Entrada do Tipo Devolução;

- Cadastrar um novo Cliente com os mesmos dados do Fornecedor, e selecioná-lo;

- Registrar nas linhas de item os produtos da nota de devolução (da nota de Saída), e referenciar a Nota de Devolução digitando manualmente os campos D1\_NFORI, D1\_SERIORI e D1\_ITEMORI (com caracteres exatos, inclusive quantidades de zeros à esquerda);

- Utilizar o TES de Entrada devidamente configurado juntamente com teu depto Fiscal de acordo com as incidências desta operação (conforme explicado acima, sem movimentar estoque/financeiro para não devolver uma operação que já foi devolvida com a primeira nota de devolução). Obs: Neste TES deve estar registrado o campo "Ajuste CIAP" = Sim conforme mencionado acima, para que o xml seja gerado com a Tag FinNFe = 3

**D)** Posteriormente, emitir uma nova nota de Saída, manualmente pela rotina MATA920 no módulo dos livros fiscais ( 09 ).  Informando manualmente os dados da nota de origem , ou seja, da compra que será novamente devolvida, porém sem vínculos automáticos pelo sistema, visto que a primeira devolução foi estornada com a execução do passo **C**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38499696202391)![](https://centraldeatendimento.totvs.com/hc/article_attachments/38499680032407)

OBS: Arquivo **XML** após autorização:

* **Saiba mais:**

Para referenciar a nota de ***devolução de nota de estorno de devolução***, é necessário utilizar o parâmetro do link abaixo:

[**Clique aqui**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020261731-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-desabilitar-mensagem-de-valida%C3%A7%C3%A3o-de-Nota-Fiscal-Origem-no-Documento-de-Entrada)

**Obs: Pela rotina MATA920 não existe campo para informa transportadora, caso sua operação tenha a necessidade dessa informação, tera que entrar em contato com equipo Compras ou Faturamento para incluir a nota de estorno da devolução pelas rotinas de pedido de venda ou documento de entrada.**
