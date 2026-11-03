---
article_id: 360025875571
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 577241c3388f0b70c0a65057a6ba450f07c9d41c71b4d0c395121448ac698927
fetched_at: '2026-06-28T22:38:54.080172+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA275 - Lote vencido,
  como posso Movimentar ou Inventariar produto com Lote Vencido que está bloqueado?
type: support-article
updated_at: '2025-12-05T19:21:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025875571-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA275-Lote-vencido-como-posso-Movimentar-ou-Inventariar-produto-com-Lote-Vencido-que-est%C3%A1-bloqueado
---

Para movimentar produtos com lote vencido bloqueado no Protheus, utilize a rotina Bloqueio de Lotes (MATA275) para liberar o lote por um dia, permitindo requisitar, inventariar ou faturar. Transferências entre armazéns com lote vencido não são permitidas; recomenda-se transferir antes do vencimento. Ajustes no parâmetro MV\_LOTVENC e na tabela de bloqueio garantem controle automático dos lotes vencidos.

**Dúvida**  
Quais os passos para faturar, requisitar ou inventariar produto com Lote Vencido que está bloqueado para movimentações?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 11.80  
  
**Solução**  
Quando o sistema está parametrizado para bloquear a movimentação dos produtos que tiveram os lotes vencidos **(MV\_LOTVENC = N)**, pode-se utilizar a rotina **Bloqueio de Lotes (MATA275)** para fazer a **liberação** do Lote, para em seguida [requisitar](https://tdn.totvs.com/display/public/PROT/F5_LOTVENC+-+Movimentar+lotes+vencidos) pela rotina **MATA241**, inventariar ([**MATA270/MATA340**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049739614-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA340-Processo-padr%C3%A3o-para-Inventariar-produtos-no-Estoque)) ou faturar por um dia.

**Observações importantes:**

 - ***Não é possível*** transferir entre os Armazéns pela rotina MATA261 quando o Lote Vencido mesmo que liberado, somente utilizando as rotinas citadas acima. Nesse cenário, em que precisa descartar o Lote vencido por um Armazém específico, deve-se controlar a validade do Lote e **antes do vencimento transferir ao Armazém** que será requisitado. ***Dica para esse cenário:*** Utilize o relatório MATR425 periodicamente para transferir ao armazém de descarte antes do vencimento.

 - A partir do release 27, [***clique aqui***](https://tdn.totvs.com/display/public/PROT/F5_LOTVENC+-+Movimentar+lotes+vencidos) e veja como criar e configurar o campo **F5\_LOTVENC** que permite também a requisição do Lote vencido pelas rotinas MATA240 ou MATA241.

 - Caso a tabela de Bloqueio de **Lote Vencidos (SDD)** esteja vazia, verifique no módulo Configurador se a rotina ***PROCLOTE()*** esta informada. **(print abaixo)** Faça a manutenção na tabela como indicado, salvar as alterações e reiniciar o Protheus. Após esse processo, os lotes vencidos serão bloqueados automaticamente no primeiro acesso do dia e em seguida é atualizado o parâmetro **MV\_DATALOT** com a data da última validação de Lote vencido.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7446109895831)

**Passo a passo para liberar um Lote vencido:**

**- 1.** Acessar à rotina Bloqueio de Lotes (MATA275);

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024788091)

**- 2.** Pesquisar o produto que deseja liberar o lote;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024776092)

**- 3.** Clicar no botão "Liberar";

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024788271)

**- 4.** Digitar a quantidade que desejar liberar em seguida clicar em Salvar

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024788471)

**- 5.** O produto ficará liberado por um dia, após esse período ele é bloqueado automaticamente novamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024788631)

**Duvidas frequentes:**

Na rotina de transferencia entre filiais (MATA310/MATA311) esse procedimento irá funcionar? 

R: Não. O procedimento não se aplica às rotinas MATA310/MATA311.  
O lote pode ser liberado para requisição ou incluído manualmente em um Pedido de Venda.

A rotina de Transferência entre Filiais é uma funcionalidade facilitadora, porém não contempla todos os recursos das rotinas originais (Pedido de Venda + Documento de Saída).

**Documento de Entrada movimento lote vencido, apresenta o HELP LOTEVENC:**

Para solucionar esta situação, há 4 maneiras:

* 1 - Ir na rotina Manutenção de lotes (MATA390)

Caminho: Módulo de Estoque/Custos > Atualização, > Movimentações > Internas > Rastreabilidade > Manutenção e clique em "**Validade e fabricação"**, desta forma, altere a data de validade do lote de forma que este não esteja mais vencido e salve.

* 2 - Outra opção é habilitar o parâmetro **MV\_LOTVENC** igual a Sim, desta forma, se o lote estiver vencido poderá ser liberado para a venda.
* 3 - Verifique a data de criação do lote no campo **B8\_DATA** se a data estiver a frente da emissão do pedido ele ira apresentar o HELP. Será necessário ajustar a data.

**Exemplo:**

Data Criação Lote **[B8\_DATA]:** 31/12/2019

Data Criação Pedido de Venda **[C5\_EMISSAO]**: 10/09/2019 (irá bloquear e mostrar a mensagem pois lote não foi gerado para liberar nessa data, o pedido de venda deve ser mais velho que a criação do lote).

* 4 - Liberar o lote bloqueado/vencido na rotina MATA275 - Bloqueio de lotes e preencher o campo Lote "C6\_LOTECTL" manualmente com o código do Lote (B8\_LOTECTL).

**Saiba mais:**

[*SIGAEST - Conceito e tabelas de controle de Lote e Endereço no Protheus*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus)

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

##
