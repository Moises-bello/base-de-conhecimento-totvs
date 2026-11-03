---
article_id: 19605921842967
category: SIGAEST - MOVIMENTAÇÕES
content_hash: bf902cd142435db70bb375e15dac292904b6984e6b823fb5f0a920661f19544e
fetched_at: '2026-06-28T22:38:54.099038+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310/MATA311 -
  AJUDA: OBRIGAT  Um ou mais campos obrigatórios não foram preenchidos: xxxxxxxxxxxxxxxx'
type: support-article
updated_at: '2026-03-25T13:55:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19605921842967-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-AJUDA-OBRIGAT-Um-ou-mais-campos-obrigat%C3%B3rios-n%C3%A3o-foram-preenchidos-xxxxxxxxxxxxxxxx
---

O erro "Um ou mais campos obrigatórios não foram preenchidos" na Transferência entre Filiais (MATA310/MATA311) ocorre porque campos como Dt.Entrega (C5\_FECENT) são obrigatórios no Pedido de Venda, mas não são preenchidos automaticamente. A solução é customizar via ponto de entrada M310CABEC para preencher os campos ou desmarcar a obrigatoriedade no Dicionário de Dados, evitando o erro.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19605902742039) Tempo aproximado para leitura: **00:02:12 min**  
  
**Dúvida**

O que fazer quando na Transferência entre Filiais (MATA310 ou MATA311) ocorre a mensagem:

"*AJUDA: OBRIGAT*

*Um ou mais campos obrigatórios não foram preenchidos: xxxxxxxxxxxxxxxx*

Nesse caso, usaremos o campo Dt.Entrega **(C5\_FECENT)** como exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19605893194647)  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Como as rotinas de **Transferência entre Filiais (MATA310/MATA311)** geram Pedido de Venda e Documento de Saída na Filial Origem e um Documento de Entrada na Filial Destino, ele acaba validando tabelas e campos obrigatórios destas rotinas também.

Para este caso, por exemplo, no **Pedido de Venda (cabeçalho - tabela SC5)** há o campo **Dt. Entrega (C5\_FECENT)**, conforme imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19605907983767)

Se o campo estiver no Dicionário de Dados marcado como **Obrigatório**, no padrão as rotinas de Transferências entre Filiais (MATA310/MATA311) não preenchem os campos, porque na própria Transferência não é possível definir uma data de entrega.

Portanto, as opções são:

**- 1 -** Se o cliente deseja que a Transferência entre Filiais preencha os Campos Obrigatórios, é necessário customizar com o **Ponto de Entrada** [**M310CABEC**](https://tdn.totvs.com/x/7kgaDg), abaixo o link com instruções do Ponto de Entrada para verificar juntamente com o Analista Desenvolvedor da Empresa para customizar conforme necessidade.  
  
***M310CABEC: Manipulação do array aCabec.***  
[***https://tdn.totvs.com/x/7kgaDg***](https://tdn.totvs.com/x/7kgaDg)

**- 2 -** Uma outra alternativa é caso, não precisar que o campo seja Obrigatório, para que a Transferência entre Filiais funcione sem apresentar o HELP, basta desmarcar o campo "Uso Obrigatório" do campo C5\_FECENT no Dicionário de Dados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19605902747159)

Com uma das ações acima, o erro não será mais apresentado na Transferência Entre Filiais, seja via MATA310, seja via MATA311.

**OBS:** Esse processo vale para qualquer outro campo que conste no help.

**Saiba mais:**

[SIGAEST - MATA310/MATA311 - Pontos de entrada da rotina Transferência entre Filiais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003854082-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Pontos-de-entrada-da-rotina-Transfer%C3%AAncia-entre-Filiais)

[SIGAEST - MATA310 / MATA311 - Como configurar ou revisar a configuração da Transferência entre Filiais (MATA310 / MATA311) no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418209855639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Como-configurar-ou-revisar-a-configura%C3%A7%C3%A3o-da-Transfer%C3%AAncia-entre-Filiais-MATA310-MATA311-no-Protheus)

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
