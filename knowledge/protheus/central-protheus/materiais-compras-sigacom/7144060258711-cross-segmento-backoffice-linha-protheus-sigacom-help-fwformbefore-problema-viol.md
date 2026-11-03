---
article_id: 7144060258711
category: Materiais - Compras (SIGACOM)
content_hash: f1c3911af7084b55ded7bce3d17b033e168ab698ab979925d5345cfa8e52de8e
fetched_at: '2026-06-28T22:41:10.595485+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Help FWFORMBEFORE
  - Problema: Violação de Integridade. Foi encontrada referência na tabela'
type: support-article
updated_at: '2025-08-14T20:00:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7144060258711-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Help-FWFORMBEFORE-Problema-Viola%C3%A7%C3%A3o-de-Integridade-Foi-encontrada-refer%C3%AAncia-na-tabela
---

**Ocorrência**Ao tentar excluir um cadastro exibe o Help:

FWFORMBEFORE

Problema: Violação de Integridade. Foi encontrada referência de *xxx (XX\_XX)* na tabela XXX - XXX.

Exemplo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7143298382871)

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões.

**Causa**

A mensagem é exibida devido tentar excluir um cadastro, o qual já foi selecionado e utilizado no sistema, ou seja, o cadastro está vinculado em outra(s) Tabela(s), de modo que excluí-lo causaria uma quebra de integridade entre os dados das tabelas.

Exemplos: Tentar excluir um cadastro de Cliente que já fora vinculado em um Pedido de Vendas. Excluir um cadastro de Fornecedor que já fora vinculado em um Doc de Entrada. Excluir um Solicitante/ Comprador/ Aprovador/ Perfil de aprovação/ Grupo de aprovação que já fora vinculado em um Pedido ou Solicitação de Compras.

Etc.

Nestes casos, de fato, não é possível excluir o cadastro.

**Solução**

Para que o cadastro não seja mais utilizado em próximos registros, deve-se BLOQUEAR o cadastro (ao invés de excluir da base). O bloqueio do cadastro impedirá que o mesmo seja considerado em novos registros (novos Pedidos de Compra e Venda, novas solicitações de compra, novas NFs, etc).

Para isto, recomenda-se criar / utilizar ***o campo de bloqueio MSBLQL*** na tabela desejada, cujos exemplos de criação podem ser verificados nos artigos abaixo:

[- Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como desabilitar ou excluir um aprovador do Grupo de Aprovadores ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012798691-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-desabilitar-ou-excluir-um-aprovador-do-Grupo-de-Aprovadores) 

[- FAT0099\_MSBLQL\_Bloqueio\_de\_Registro\_Cadastro](https://tdn.totvs.com/display/PROT/FAT0099_MSBLQL_Bloqueio_de_Registro_Cadastro)

**Saiba Mais:**

[Como bloquear cadastros - Campo MSBLQL](https://tdn.totvs.com/x/p4WFDg)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
