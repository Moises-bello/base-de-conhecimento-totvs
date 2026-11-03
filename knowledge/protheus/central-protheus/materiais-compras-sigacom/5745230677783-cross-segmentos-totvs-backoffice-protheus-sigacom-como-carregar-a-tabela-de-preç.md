---
article_id: 5745230677783
category: Materiais - Compras (SIGACOM)
content_hash: ebb13f7982fbfcc4bd251d1466a8c865832a369662a2182b0f1b2155ae0d26db
fetched_at: '2026-06-28T22:41:14.494850+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como carregar a Tabela
  de Preços no Pedido de Compras?
type: support-article
updated_at: '2025-04-04T13:04:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5745230677783-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-carregar-a-Tabela-de-Pre%C3%A7os-no-Pedido-de-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**  
Como carregar a Tabela de Preços no Pedido de Compras?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Protheus Compras   
  
**Solução**

Para carregar os valores da tabela de preços para o **Pedido de Compra** é necessário validar alguns pontos importantes para o processo, sendo eles:

1. Cadastro da **Tabela de Preços**, não se esquecendo de que os campos **AIA\_DATDE** e **AIA\_DATTE** são validados com base na data de emissão do **Pedido de Compras**. Se a emissão do PC estiver fora deste intervalo o preço da **Tabela de Preços** não será carregado;
2. No cadastro da **Tabela de Preços** existe o campo **AIB\_DATVIG**, que determina a data a partir da qual o preço do item esta vigente. Se a data de vigência for maior que a data de emissão do PC, o preço não é carregado;
3. Inclua uma amarração **Produto** x **Fornecedor**, informando no campo **A5\_CODTAB** o número da **Tabela de Preços** cadastrada. Este cadastro é realizado para todos os produtos informados na **Tabela de Preços**. Se não houver amarração entre o **Produto** x **Fornecedor** o preço da Tabela não é carregado no **Pedido de Compras**.

Após realizar estes passos na inclusão de um**Pedido de Compras** o sistema carrega automaticamente o campo **C7\_CODTAB** e alimenta o **C7\_PRECO** com o preço cadastrado na **Tabela de Preços**.

Para reajustar os preços de uma Tabela de Preços:

1. Na janela de manutenção da Tabela de Preços, selecione a a Tabela de Preços a ser reajustada.
2. Clique em **"Reajustar"**.
3. O Sistema exibe uma mensagem alertando sobre o reajuste de preços.
4. Clique em "Parâmetros" e preencha os dados conforme help de campo.
5. Confirme e o Sistema efetuará o reajuste na Tabela de Preços.

***Saiba Mais:***

* [PCOM04006 - Como carregar a Tabela de Preços no Pedido de Compras?](https://tdn.totvs.com/x/h9DuDQ)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
