---
article_id: 21518593906071
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 8424580352aa6770e25828b3613eda6b8dce7f67592cfe0bf7dd70cc6ab2581f
fetched_at: '2026-06-28T22:38:55.401296+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como remover o "AUTO"
  do LOTE ou definir outra nomenclatura/código automático?
type: support-article
updated_at: '2026-04-08T11:48:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21518593906071-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-remover-o-AUTO-do-LOTE-ou-definir-outra-nomenclatura-c%C3%B3digo-autom%C3%A1tico
---

No Protheus, o parâmetro MV\_PRXLOTC permite alterar a nomenclatura automática dos lotes, substituindo o padrão "AUTO". Pode-se definir um novo prefixo, como "ABC001", e o sistema sequencia automaticamente os lotes. Para regras específicas, é possível usar fórmulas via SIGACFG, configuradas nos campos B1\_FORMLOT ou MV\_FORMLOT, personalizando a geração automática dos lotes.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21518589803927) Tempo aproximado para leitura: **00:03:25 min**  
  
**Dúvida**  
 Como remover o "AUTO" do Lote ou definir outra nomenclatura/código automático?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
  
**Solução**  
Há um Parâmetro no Protheus que permite o usuário definir um novo sequenciamento de codificação automática de Lotes. O parâmetro é o MV\_PRXLOTC. Nele, basta definir qual a nova nomenclatura deseja para o Lote. No padrão, todos os Lotes começa com a concatenação da palavra AUTO + CÓDIGO. Justamente para facilitar o usuário de diagnosticar de que este lote entrou sem que o usuário tenha definido um código manual para ele.

Parâmetro MV\_PRXLOTC:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21518593888407)

**Exemplo de teste prático:**

Vamos alterar o parâmetro para ABC001, portanto é esperado que sempre que entrar com Documento de Entrada, Apontar Produção ou adicionar saldo por Movimento Interno de **produto que controla Lote (B1\_RASTRO = L)** ele irá delegar o lote ABC001 para ele. E depois, num proximo movimento de qualquer produto que controla lote, ele irá delegar o lote ABC002 para ele. E assim sucessivamente respeitando a nova codificação padrão definida no parâmetro.

Produto utilizado no Teste:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21518593890199)

Parâmetro alterado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21518589811479)

Teste prático:

![Teste cenario lote automatico2.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/21518589817495)

Com isso, o parâmetro passa a definir um novo sequenciamento.

Para casos de clientes que queiram definir outra regra, por exemplo, tratar uma codificação automática por tipo de produto, ou com sequenciamento especifico que o MV\_PRXLOTC não atenda, este padrão pode ser alterado através de uma fórmula (SIGACFG - Cadastro de Fórmulas). Pode-se atribuir uma fórmula especifica para cada produto (B1\_FORMLOT) ou uma fórmula genérica para todos os produtos que utilizem Rastreabilidade (MV\_FORMLOT) - Nestes campos deve-se informar o número da fórmula a ser utilizada.  
A função que gera Lotes automaticamente (NextLote(cProd,"L")) irá verificar primeiro o B1\_FORMLOT, depois o MV\_FORMLOT - caso ambos estejam em branco utilizará o Preenchimento Automático Padrão.  
   
**Exemplo formula (mero exemplo)**  
**dtos(dDatabase)+SuperGetMv( "MV\_PRXLOTE", .F.)**  
**"TESTE"+Nextlote()**

OBS: A definição de fórmula é de inteira responsabilidade do cliente junto à sua equipe de desenvolvimento.

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como ativar o controle de Lote/Rastro para produtos com saldo?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020672612-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-ativar-o-controle-de-Lote-Rastro-para-produtos-com-saldo)

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
