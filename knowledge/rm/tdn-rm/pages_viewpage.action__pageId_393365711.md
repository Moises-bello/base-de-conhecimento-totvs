---
content_hash: b916465bed4c381947cc67dc94a850ea4433c488b32d64e4b566ffb95148f4d6
fetched_at: '2026-06-29T00:09:09.726897+00:00'
page_id: '393365711'
product: rm
source: tdn-rm
title: Descrição do Processo de Industrialização Interna - Transferência entre Filiais
  (SEM Local Transitório - Retorno da mesma mercadoria)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=393365711
version: 11
---

## Visão Geral

**Empresa Remetente (Filial Origem) / Empresa Recebedora (Filial Destino)**

**Descrição do Processo:**O cliente irá enviar mercadoria de propriedade da filial para industrialização na Matriz. Este processo de remessa da mercadoria para industrialização será realizado através da emissão de uma nota fiscal no Gestão de Estoque, Compras e Faturamento, no tipo de movimento de transferência de estoque (3.1). Este movimento por sua vez, irá baixar estoque físico/financeiro na filial origem e aumentará o estoque físico/financeiro na filial destino.A filial destino já de posse da mercadoria, fará o beneficiamento/industrialização. Ao finalizar o processo de industrialização, emitirá uma nota fiscal retornando simbolicamente a mercadoria utilizada no processo de industrialização e irá cobrar, para efeitos fiscais, o serviço de industrialização. Esta transação será realizada em uma única nota fiscal, que é emitida em um tipo de movimento de transferência (3.1), que irá baixar o estoque físico/financeiro na origem e aumentará o estoque físico/financeiro no destino.Na filial que solicitou a industrialização, será efetuada manualmente a baixa da mercadoria retornada simbolicamente. O processo será semelhante ao da industrialização.

**Considerações:**

* Material a ser transferido, de propriedade da empresa (não é de terceiro);
* Movimentação com tipo de movimento do grupo 3.1 (transferência);
* Proprietário da mercadoria cadastrado como Cli/For

## Parametrização

**Na Filial Remetente:**A remessa da mercadoria para industrialização será lançada em um movimento do tipo ***3.1 ‘Transferência para industrialização em Outra Filial’***, que será incluído manualmente na filial remetente da industrialização. Este tipo de movimento irá aumentar o estoque **COM Terceiros** na filial origem da movimentação e aumentar o estoque **DE Terceiros** na filial destino.

**Estoque de Terceiros - Parametrização do Processo de Industrialização Interna - Transferência entre Filiais**

**Filial Remetente:**

O tipo de movimento de **Transferência para Industrialização em Outra Filial** terá a seguinte parametrização para que seja possível controlar o estoque **COM Terceiros**:

**Etapa Item - Identificação 1/2:**Tipo dos Itens = Produtos

**Etapa Estoque - Estoque 2/3:**Tipo Controle de Estoque Terceiros = Transferência para Industrialização em Outra Filial

                                                    Efeito Sobre o Saldo com Terceiros = Aumenta

**Integração Contábil:**Parametrizar de acordo com as obrigações contábeis da Empresa

**Integração Fiscal:**Parametrizar de acordo com as obrigações legais da Empresa

**Fis - Natureza:**Edita Cliente/Fornecedor Origem/Destino = Marcado

                       

**Filial Recebedora:**O tipo de movimento de **Industrialização Efetuada para Outra Filial** terá a seguinte parametrização para que seja possível controlar o estoque **COM terceiros** da Filial Remetente:

**Etapa Item - Identificação 1/2:**Tipo dos Itens = Produtos

**Etapa Estoque - Estoque 2/3:**Tipo Controle de Estoque Terceiros = Industrialização Efetuada para Outra Filial

                                                    Efeito Sobre o Saldo de Terceiros = Diminui

**Integração Contábil:**Parametrizar de acordo com as obrigações contábeis da Empresa

**Integração Fiscal:**Parametrizar de acordo com as obrigações legais da Empresa

**Fis - Natureza:**Edita Cliente/Fornecedor Origem/Destino = Marcado

                       

O tipo de movimento para **Retorno de Mercadoria não Aplicada na Industrialização** terá as mesmas parametrizações descritas acima, além de parametrizar o **Motivo de Referência** para que seja estornado o estoque **COM terceiros**da Filial Remetente:

**Etapa Mov - Outros Dados:**Usar Cópia de Movimentos por referência = 11 - Retorno de Mercadoria não Aplicada na Industrialização
