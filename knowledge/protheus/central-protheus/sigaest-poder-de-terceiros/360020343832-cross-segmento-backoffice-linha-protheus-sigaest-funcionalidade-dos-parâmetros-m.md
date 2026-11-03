---
article_id: 360020343832
category: SIGAEST - PODER DE TERCEIROS
content_hash: 7a1f10ca7e792679b4c66b3c1066779b168c0c422b2ca4a2b334b66cc1e93f10
fetched_at: '2026-06-28T22:39:03.109942+00:00'
product: protheus
section_id: 1500001538881
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -  Funcionalidade dos
  parâmetros MV_CONTERC e MV_ALMTERC para controle de armazém EM terceiros
type: support-article
updated_at: '2026-01-09T13:58:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020343832-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Funcionalidade-dos-par%C3%A2metros-MV-CONTERC-e-MV-ALMTERC-para-controle-de-armaz%C3%A9m-EM-terceiros
---

**Dúvida**

Qual a finalidade dos parâmetros MV\_CONTERC e MV\_ALMTERC?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

O controle de poder em terceiros é um processo muito comum, porém, quando se trata do produto ir para o controle do terceiro, ou seja "Em Terceiros", este saldo acaba deixando de ser visto no Custo Médio. Por este motivo foram criados os parâmetros MV\_CONTERC trabalhando junto com o parâmetro MV\_ALMTERC.

Com o primeiro parâmetro ativo, ao enviar um produto para um terceiro o sistema gravará o saldo dele no armazém delegado no parâmetro MV\_ALMTERC. Desta forma, tanto seu saldo como seu custo podem ser controlados no Protheus, além de fazer o Recálculo do Custo Médio olhando para este armazém também.

**Configuração do MV\_CONTERC :**

|  |  |
| --- | --- |
| Nome | MV\_CONTERC |
| Tipo | Lógico |
| Descrição | Indica se deve controlar o saldo de mercadorias para produtos enviados para poder de terceiros.  ( T = Ativa o controle / F = Desativa o Controle ) |
| Conteúdo | .T. |

**Configuração do MV\_ALMTERC :**

|  |  |
| --- | --- |
| Nome | MV\_ALMTERC |
| Tipo | Caracter |
| Descrição | Indica se o armazém é armazém de terceiros. |
| Conteúdo | 80/ ( Conforme Exemplo ) |

No parâmetro “MV\_ALMTERC” é possível definir o armazém desejado. Neste exemplo foi configurado como armazém "**80/**”.

O armazém definido é bloqueado pelo sistema, para que não sejam efetuadas movimentações neste armazém. Apenas as movimentações automáticas, produzidas pela remessa e devolução de produtos, irão gerar movimentos no armazém de terceiros.

**Procedimento para Utilização**

1. No Configurador em Ambiente / Cadastros / Parâmetros, realizar a configuração dos parâmetros MV\_CONTERC, MV\_ALMTERC e MV\_CUSFIL conforme link do documento detalhado no Saiba mais.  
  
2. No módulo Estoque e Custos, em Atualizações / Cadastros / Locais de Estoque, incluir o local de estoque para o produto

3. No módulo Estoque e Custos, em Atualizações / Cadastros / Locais de Estoque, incluir o local de estoque para o armazem de terceiro (Conforme informado no parametro de sistema MV\_ALMTERC)

4. No módulo Estoque e Custos, em Atualizações / Cadastros / Produtos, incluir um produto.  
  
5. No módulo Estoque e Custos, em Atualizações / Saldos / Inicial, incluir um saldo inicial para o produto em seu armazém padrão e um saldo inicial zerado no armazém configurado no parâmetro MV\_ALMTERC.  
  
6. No módulo Estoque e Custos, em Atualizações / Cadastros / Movimentações / Fiscais / TES, incluir um TES de Saída com Atu. Estoque "Não" (F4\_ESTOQUE), Poder de Terceiros "Remessa" (F4\_PODER3) e Amz. Terceiros "Sim" (F4\_CONTERC). Incluir um segundo TES porém de Entrada com Atu. Estoque "Não" (F4\_ESTOQUE), Poder de Terceiros "Devolução" (F4\_PODER3) e Amz. Terceiros "Sim" (F4\_CONTERC).  
  
7. No módulo de Faturamento em Atualizações / Pedidos / Pedido de Vendas, incluir um Pedido de Vendas par ao produto cadastrado, utilizando o TES de saída também cadastrado anteriormente. Posteriormente faturar o Pedido de Vendas gerando sua Nota Fiscal.  
  
8. No módulo Estoque e Custos, em Atualizações / Saldos / Atual, buscar o produto e verificar que o saldo do produto foi transferido do armazém padrão para o armazém informado no parâmetro MV\_ALMTERC.  
  
9. No módulo Estoque e Custos, em Atualizações / Movimentações / Fiscais / Documento de Entrada, incluir um Documento de Entrada, informar o mesmo Cliente/Loja utilizado no Pedido de Vendas gerado anteriormente, informar o código do produto e o TES de Entrada cadastrado anteriormente. Em "Outras Ações", utilizar a opção "Origem" para realizar o vinculo com a Nota Fiscal gerada anteriormente e confirmar a inclusão.  
  
10. No módulo Estoque e Custos, em Atualizações / Saldos / Atual, buscar o produto e verificar que o saldo do produto foi transferido do armazém informado no parâmetro MV\_ALMTERC para o armazém padrão.

**Observações importantes:**

* A configuração do tipo do Armazém 80 ou o armazém configurado no parametro MV\_ALMTERC, não deve ser igual a "3 - Terceiros", o mesmo deve ser igual ao armazém de origem e destino do gerado que foi consumido.
* A configuração do parametro permite apenas a utilização de um único armazém;
* Se o parâmetro MV\_CONTERC estiver desabilitado, ou seja, como "F" (False), o parâmetro MV\_ALMTERC deixa de ter valor.
* Para o processo funcionar, os TES envolvidos não podem atualizar estoque (estando com F4\_ESTOQUE = N)
* O Controle do Armazém de Poder de Terceiros somente está disponível para usuários da apuração do Custo Médio por Filial ou Empresa (**MV\_CUSFIL = F ou E**).

**O controle do armazém de poder de terceiros somente está disponível para:**

* Clientes da apuração do custo médio por filial (“MV\_CUSFIL = F”);
* Processos em que o material é enviado para terceiros (“EM TERCEIROS”), não disponível para controle de produtos de terceiros (“DE TERCEIROS”) em nosso poder.

**Saiba mais****:**

*[Clique aqui e veja mais artigos sobre Poder de Terceiros no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012199513-SIGAEST-PODER-DE-TERCEIROS)*

[Informações e procedimentos para uso do Armazém de Poder de Terceiros](https://tdn.totvs.com/pages/releaseview.action?pageId=271395422)
