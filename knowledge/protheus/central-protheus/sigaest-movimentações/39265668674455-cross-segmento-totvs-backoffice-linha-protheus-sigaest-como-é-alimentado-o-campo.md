---
article_id: 39265668674455
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 3bd047266660a404aa47ce3a9c331bafc27bdbfe71b9c3a3386f9181fbf6e439
fetched_at: '2026-06-28T22:38:58.472498+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Como é alimentado
  o campo B8_ORIGEM
type: support-article
updated_at: '2026-03-24T19:16:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39265668674455-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEST-Como-%C3%A9-alimentado-o-campo-B8-ORIGEM
---

O campo B8\_ORIGEM na tabela de Saldos por Lote (SB8) é preenchido replicando o valor do campo D1\_ORIGEM durante o recebimento do Documento de Entrada (MATA103). Não é preenchido automaticamente pelo cadastro do produto. Para diferenciar estoques importados, deve-se garantir que D1\_ORIGEM esteja corretamente preenchido no módulo de Compras ao lançar o item.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39265668662423) Tempo aproximado para leitura: 00**:01:00 min**  
  
**Dúvida**  
Como é realizado o preenchimento do campo **B8\_ORIGEM** (Origem do Lote) na tabela de Saldos por Lote (SB8), considerando que o campo se encontra em branco e há necessidade de diferenciar o estoque importado?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
O campo **B8\_ORIGEM** não possui um preenchimento automático baseado apenas no Cadastro de Produto (B1\_ORIGEM). Sua alimentação ocorre da seguinte forma:

* **Origem do Dado:** O conteúdo do campo B8\_ORIGEM é gravado replicando o valor inserido anteriormente no campo D1\_ORIGEM (Origem da Mercadoria) durante o recebimento do Documento de Entrada (MATA103).
* **Validação:** O sistema não utiliza o campo D1\_CLASFIS para alimentar a SB8; este último é vinculado à origem definida no cadastro de produtos (SB1).  
  **Processos de Importação**: Caso a entrada do estoque ocorra via rotinas de importação de dados, o preenchimento do B8\_ORIGEM dependerá de como o arquivo ou a API de integração manipula o campo D1\_ORIGEM na tabela SD1.

**Passo:**

Para garantir que o lote seja gravado com a origem desejada (ex: origem 6), siga os procedimentos abaixo:

* No módulo de **Compras (SIGACOM)**, acesse a rotina de **Documento de Entrada (MATA103)**.
* Ao lançar o item, certifique-se de que o campo **D1\_ORIGEM** esteja preenchido com o código correspondente.
* Ao confirmar a nota e gerar o saldo no estoque (SB8), o sistema transportará automaticamente este conteúdo para o campo **B8\_ORIGEM**.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[Campos D1\_LOTEFOR (Lote Fornecedor) e D1\_LOTECTL (Lote) do Documento de Entrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8836419922455-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Campos-D1-LOTEFOR-Lote-Fornecedor-e-D1-LOTECTL-Lote-do-Documento-de-Entrada)

[SIGAEST - Conceito e tabelas de controle de Lote e Endereço no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus?source=search)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Campo D1\_LOTECTL para produtos com controle de Rastro é possível tornar a digitação obrigatória?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29009366772631-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Campo-D1-LOTECTL-para-produtos-com-controle-de-Rastro-%C3%A9-poss%C3%ADvel-tornar-a-digita%C3%A7%C3%A3o-obrigat%C3%B3ria)
