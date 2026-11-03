---
article_id: 360015760592
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: d2d71a13116d0f53bcfc03146defef6f708cc72ebc7f6531aef99875dd55390c
fetched_at: '2026-06-28T22:39:07.907197+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - Como cadastrar
  e utilizar a segunda unidade de medida (2ª UM)
type: support-article
updated_at: '2026-05-13T22:38:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015760592-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Como-cadastrar-e-utilizar-a-segunda-unidade-de-medida-2%C2%AA-UM
---

O Protheus permite cadastrar até duas unidades de medida (1ª UM e 2ª UM) para um produto, com fator de conversão que relaciona ambas. É obrigatório zerar o saldo antes de cadastrar a 2ª UM para evitar inconsistências. O fator de conversão automatiza cálculos entre unidades; sua ausência exige digitação manual e pode causar erros. Para produtos com recebimento ou baixa invertida, recomenda-se cadastros em dois níveis e uso da rotina de transferência. Produtos com peso variável devem seguir regras internas para padronização.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34052719775127)** Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**

Qual é o procedimento correto para cadastrar e utilizar a segunda unidade de medida (2ª UM) no Cadastro de Produtos (MATA010), e quais são os impactos e boas práticas na sua utilização?

**Ambiente**

Cross Segmento - TOTVS BackOffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

A segunda unidade de medida (2ª UM) no Protheus permite o controle de um mesmo produto em duas unidades distintas (por exemplo, Caixa e Unidade), viabilizando o registro de entradas e saídas em ambas as formas. O sistema trabalha com o limite padrão de até duas unidades de medida por produto.

**Importante:** Antes de cadastrar a segunda unidade de medida para um produto que já possui movimentação, é obrigatório zerar o seu saldo (por exemplo, via rotina de inventário). Após a configuração da 2ª UM, o saldo deve ser reimplantado. A não observância desta regra gerará inconsistências em movimentações futuras e divergências irremediáveis entre as unidades.

**1. Conceitos e Campos Técnicos (Tabela de cadastro de produto - SB1)**

* **Unidade (B1\_UM):** Unidade de medida principal do produto (exemplo: UN, PC).
* **Segunda Unidade (B1\_SEGUM):** Segunda unidade de medida do produto (exemplo: CX).
* **Fator de Conversão (B1\_CONV):** Fator numérico que relaciona a primeira unidade com a segunda.
* **Tipo de Conversão (B1\_TIPCONV):** Define se a conversão via fator ocorrerá por multiplicação ou divisão.

**2. Exemplos Práticos de Conversão**

* **Multiplicação:** 1ª UM = CX (Caixa), 2ª UM = PC (Peça). Fator de Conversão = 16.

  ![UN1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39657843996823)

  Cálculo: 1ª UM **multiplicada** pelo Fator de Conversão = 2ª UM

  (**1** Caixa multiplicada por 16 = **16** Peças).

  **Exemplo na rotina MATA241 - Movimentação Múltipla:**

  ![UNI2.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/39657843998615)
* **Divisão:** 1ª UM = CX (Caixa), 2ª UM = PC (peça). Fator de Conversão = 16.

  ![UNI3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39657843999255)

  Cálculo: 1ª UM **dividida** pelo Fator de Conversão = 2ª UM (1 Caixa divididas por 16 = 0,06 Peças).

  ![UNI4.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/39657827353239)

  Também pode-se digitar pela segunda unidade, no caso o sistema fará o calculo inverso, para condizer com a realidade da sua conversão.

  **Exemplo digitando pela segunda unidade:**

  **Multiplicação****:** 2ª UM = PC (peça), 1ª UM = CX (Caixa). Fator de Conversão = 16.

          Cálculo: 2ª UM **divide** pelo Fator de Conversão = 1ª UM (**16** peças dividida por 16 = 1 Caixa).

**Divisão****:** 2ª UM = PC (peça), 1ª UM = CX (Caixa). Fator de Conversão = 16.

          Cálculo: 2ª UM **Multiplica** pelo Fator de Conversão = 1ª UM (**16** peças multiplicada por 16 = 256 Caixas).

**3. Impactos de Não Utilizar o Fator de Conversão**

O preenchimento do Fator de Conversão é altamente recomendado. Sem ele, o sistema não calculará automaticamente as proporções. Como resultado, em todas as rotinas que exigem a informação de quantidade e unidade (notas de entrada, solicitações, pedidos de compra e venda), o usuário será obrigado a digitar manualmente a quantidade da 2ª UM.

O sistema prioriza a unidade principal. Se o fator não for informado e o usuário esquecer de digitar a quantidade da 2ª UM em uma requisição, o sistema abaterá o saldo apenas da unidade principal, mantendo o saldo da segunda unidade inalterado. É recomendável efetuar testes em ambiente de homologação para dimensionar o impacto operacional caso a empresa opte por não preencher o fator.

**Nota de Atualização:** Em rotinas ajustadas recentemente, o sistema não efetua conversão e não zera a segunda unidade de medida quando não há fator cadastrado, acatando estritamente as quantidades digitadas pelo usuário.

**4. Produtos com Recebimento ou Baixa Invertida**

Se houver necessidade de controlar o produto na unidade principal (exemplo: UN), mas o fornecedor enviar em caixas (CX), e for necessário realizar baixas diretamente pela 2ª UM em algumas rotinas, recomenda-se a criação de cadastros em dois níveis:

* **Cadastro A:** configurado como UN x CX.
* **Cadastro B:** configurado como CX x UN.

  Para transitar entre eles, **utilize a rotina de Transferência (MATA261)** para movimentar o saldo de um produto para o outro, mantendo a rastreabilidade e o controle na unidade de medida desejada.

**5. Produtos com Peso Variável**

Para mercadorias cuja comercialização envolva peso ou volume variável entre as unidades (como frangos congelados ou celulose sujeita a umidade), é necessário documentar as regras internas da empresa para padronização no Protheus. Recomenda-se adotar normas do setor, como a aplicação do peso médio ou de um índice de teor seco, para estabelecer um Fator de Conversão contínuo.

**Curiosidades:**

* **Quantas unidade de medidas são permitidas?**  
  Por padrão, existe 2 unidades de medidas no cadastro de produto, não existe demais possibilidades de novas unidades dentro do cadastro de produtos de forma padrão.
* **E se o meu produto tem saldos?**  
  [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - Como incluir saldo na 2° Unidade de Medida de produto com saldo?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012683462-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Como-incluir-saldo-na-2-Unidade-de-Medida-de-produto-com-saldo)
* **Posso desativar o fator de conversão?**

  **Viabilidade:** É possível desativar, mas **altamente não recomendamos**.

  + **Trabalho Manual Exaustivo:** Sem o cálculo automático, o usuário precisará digitar as quantidades nas duas unidades de medida em todas as operações (notas, pedidos, etc.).
  + **Furos no Estoque:** Se o usuário esquecer de informar a segunda unidade, os saldos ficarão incorretos e dessincronizados.
  > **Nota:** Caso o cliente insista na desativação, é imprescindível realizar testes profundos em ambiente de homologação antes de aplicar em produção.

**Saiba mais**  
[*Configurações gerais no estoque custos*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
