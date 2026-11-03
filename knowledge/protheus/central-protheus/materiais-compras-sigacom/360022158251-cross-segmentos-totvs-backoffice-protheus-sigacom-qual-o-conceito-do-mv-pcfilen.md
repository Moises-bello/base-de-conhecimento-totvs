---
article_id: 360022158251
category: Materiais - Compras (SIGACOM)
content_hash: 43f556ec284cf93ef71103aa339b75ecf70c7615a153517dbc5aa683c2c1cad2
fetched_at: '2026-06-28T22:41:10.405860+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual o conceito do
  MV_PCFILEN e sua interferência na numeração do Pedido de Compras?
type: support-article
updated_at: '2026-02-26T11:57:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022158251-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-o-conceito-do-MV-PCFILEN-e-sua-interfer%C3%AAncia-na-numera%C3%A7%C3%A3o-do-Pedido-de-Compras
---

**Dúvida**  
Qual o conceito do MV\_PCFILEN e sua interferência na numeração do Pedido de Compras?  
  
**Ambiente**  
Protheus – Compras – A partir da versão 11.80  
  
**Solução**

* Se a tabela SC7 estiver com o X2\_MODO como compartilhado, o MV\_PCFILEN deve obrigatoriamente estar preenchido = T (por empresa) e o controle de numeração de PC's vai ser por empresa, o C7\_FILENT ficará em branco e o campo FILIAL DE ENTREGA do cabeçalho do Pedido de Compras não permitirá digitação;

  **Obs:** No uso da tabela SC7 compartilhada e MV\_PCFILEN=T conforme acima, caso seja usado a inclusão de Pedido "puxando" Solicitação de Compras (tabela SC1), para que não seja trazida informação no campo "Filial de Entrega" do Pedido, se faz necessário também o uso da tabela SC1 compartilhada da mesma forma que a tabela SC7.

* Se a tabela SC7 estiver com o X2\_MODO como exclusivo e o MV\_PCFILEN for igual a F, o PC também não permite a digitação da filial de entrega (assume a filial corrente) e a numeração do PC vai ser controlada por filial, neste caso o C7\_FILENT SERÁ GRAVADO COM A FILIAL CORRENTE;

* Quando a tabela SC7 estiver exclusivo no X2\_MODO e o MV\_PCFILEN for igual a T, o PC permite a digitação da filial de entrega no cabeçalho e o controle da numeração do PC vai ser por empresa, neste caso o C7\_FILENT (Filial de Entrega) passará a ser gravado com a filial indicada no cabeçalho do PC.

Nesta opção, caso haja na outra Filial informada no campo Filial de Entrega um pedido com uma mesma numeração do Pedido que está sendo incluído, a rotina não permite essa alteração do campo de Filial de Entrega do Pedido retornando a mensagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16476774323479)

Ou seja, nesta opção com a tabela SC7 Exclusiva e o MV\_PCFILEN = T, a numeração do Pedido que está sendo incluido passa a ser validada não só na Filial que o pedido está sendo incluido mas também na FIlial de Entrega que está sendo informada no campo Filial de Entrega.

E assim, conforme a mensagem reporta, deve-se informar um numero de Pedido de Compras que não exista tanto na Fiilal do Pedido que está sendo incluido como também da FIlial de Entrega informada.

Abaixo artigo sobre esta validação:

* [PCOM04027 - Validação numeração pedido de compra](https://tdn.totvs.com.br/pages/releaseview.action?pageId=661341813)

Considerando que numeração para os Pedidos de Compra é '000100', e que possui 3 filais o ajuste deve ser feito da seguinte forma:

Exemplo da antiga tabela SXF - numeração atual:

XF\_FILIAL XF\_ALIAS XF\_TAMANHO XF\_NUMERO   
01SC7xxx SC7 6 000100  
02SC7xxx SC7 6 000100  
03SC7xxx SC7 6 000100

Exemplo da antiga tabela SXE - próxima numeração:

XE\_FILIAL XE\_ALIAS XE\_TAMANHO XE\_NUMERO   
01SC7xxx SC7 6 000101  
02SC7xxx SC7 6 000101  
03SC7xxx SC7 6 000101

Ajustes de controle de numeração atualmente podem ser realizados pela rotina de Controle de Numeração conforme orientações do artigo: [Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Numeração automática incorreta nas Tabelas do Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000582027)

**Observações**:

• Realizar o acertos de controle de numeração primeiramente em base de homologação para validar.  
• Verificar se a sequência desejada para a numeração já não foi utilizada em PC gravados na SC7, pois caso já esteja em uso ao tentar incluir um PC será apresentado help sobre inconsistência na numeração.

***Saiba Mais:***

* [PCOM04027 - Validação numeração pedido de compra](https://tdn.totvs.com.br/pages/releaseview.action?pageId=661341813)
* [Filial de entrega (MATA121 - SIGACOM)](https://tdn.totvs.com/x/fixKEg)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual o conceito do campo Filial de Entrega e parâmetro MV\_PCFILEN e sua interferência na numeração de Solicitação de Compras ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34523404365207-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-o-conceito-do-campo-Filial-de-Entrega-e-par%C3%A2metro-MV-PCFILEN-e-sua-interfer%C3%AAncia-na-numera%C3%A7%C3%A3o-de-Solicita%C3%A7%C3%A3o-de-Compras)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
