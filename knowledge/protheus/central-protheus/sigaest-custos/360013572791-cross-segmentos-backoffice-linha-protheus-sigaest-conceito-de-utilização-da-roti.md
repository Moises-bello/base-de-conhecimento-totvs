---
article_id: 360013572791
category: SIGAEST - CUSTOS
content_hash: acb9e10166f550b6d087abfe3da44a855e737e6bd7c3d41f40be59d243f372b9
fetched_at: '2026-06-28T22:39:00.492523+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - SIGAEST - Conceito de utilização
  da rotina Custo Standard/Custo de Reposição MATA320 - B1_CUSTD
type: support-article
updated_at: '2026-06-08T19:09:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013572791-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAEST-Conceito-de-utiliza%C3%A7%C3%A3o-da-rotina-Custo-Standard-Custo-de-Reposi%C3%A7%C3%A3o-MATA320-B1-CUSTD
---

A rotina MATA320 calcula o "Custo Standard" (B1\_CUSTD) no cadastro de produtos, baseado no custo de compra para produtos comprados ou na soma dos custos dos componentes para produtos fabricados. O preenchimento depende da configuração do TES e do parâmetro "Calcula os custos por?", que pode considerar o último preço de compra, estrutura ou último custo de compra. O campo B1\_CUSTD é atualizado após o processamento da rotina.

**Dúvida**  
Qual o conceito a rotina "**Custo Standard/Custo de Reposição**" (**MATA320**) utiliza para preenchimento do campo “**Custo Stand.**” (**B1\_CUSTD**)?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Esta rotina calcula o custo de reposição atualizando o campo "Custo Standard" ou "Custo de reposição" (B1\_CUSTD), no Cadastro de Produtos, logo após o processamento.  
Normalmente ele é formado pelo:

* Custo de compra (para produtos comprados);
* Soma do custo dos componentes (para produtos fabricados).

O campo “Custo Stand.” (B1\_CUSTD), no Cadastro de Produto, é gravado**logo após o processamento da rotina MATA320.**

Para a geração do Custo Standard de um produto é necessário que, na nota de entrada do produto, se utilize um TES configurado com o campo "**Atualiza Preço de Compra**" (**F4\_UPRC**) como “SIM”, após isso, basta acessar à rotina MATA320 para geração do Custo Standard.

Na tela de parametrização da rotina MATA320, o campo "**Calcular os custos por?**" contém as seguintes opções:

* **Ult Prec Compra:** O sistema grava o valor do ultimo preço de compra no campo "**último preço de compra**" (**B1\_UPRC**) no cadastro do produto;
* **Estrutura:** O sistema grava o valor do “**Custo Stand.**” (**B1\_CUSTD**) da **Matéria Prima** nos Produtos Intermediários e Produtos Acabados da estrutura;
* **Ult Cust Compra:**O sistema grava o valor do ultimo custo de compra, campos "**Custo Moe 1**" (**D1\_CUSTO**) e  "**Vlr.Total**" (**D1\_TOTAL**), no campo “Custo Stand.” (B1\_CUSTD) no cadastro do produto.

**Exemplos de uso**:

* [Cálculo do Custo Standard de Produto do tipo "PA" por estrutura;](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19042181937431)
* [Cálculo do Custo Standard de um produto do tipo "MP" por última compra ou custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19042797861911).

## 

## **DEMAIS INFORMAÇÕES**

O custo de reposição nas Movimentações de Produção (D3\_CUSRP1), será atribuído através do Recalculo do Custo Médio, onde o custo de reposição é acumulado na OP, portanto os apontamentos de produção deverão usar a TM de produção configurada para custear a OP e o parâmetro MV\_CUSREP = .T.

## **Pontos de entrada da rotina Custo Standard:**

[Cross Segmentos - Backoffice (Linha Protheus) - SIGAEST - Conceito de utilização da rotina Custo Standard/Custo de Reposição MATA320 - B1\_CUSTD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013572791-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAEST-Conceito-de-utiliza%C3%A7%C3%A3o-da-rotina-Custo-Standard-Custo-de-Reposi%C3%A7%C3%A3o-MATA320-B1-CUSTD)

**Observações:**

* É possivel atualizar a informação dos campos "**Ult. Compra**" (**B1\_UCOM**) e "**Ult. Preco**" (**B1\_UPRC**), também na utilização da rotina **Refaz Custo de Entrada (MATA190)**;
* Não serão consideradas como ultimo preço de compra e ultima data, notas que tenham a data inferior à que encontra-se no campo "**Ult. Compra**" (**B1\_UCOM**), o sistema só refaz a informação dos campos "**Ult. Compra**" (**B1\_UCOM**) e "**Ult. Preco**" (**B1\_UPRC**) se a data da nota encontrada for superior ao conteúdo do campo citado;
* **Nota de Conhecimento de Frete:** No Protheus padrão, não é atualizada no Custo Standard, o sistema considera que o custo de reposição do produto é o valor da ultima NF de compra;
* **Nota de Complemento de Preço:** É possível atualizar no Custo Standard, desde que este complemento, no documento de entrada, utilize TES com os campos "**Atu.Pr.Compr**" (**F4\_UPRC**) e "**Qtd.Zerada**" (**F4\_QTDZERO**)**.**   
  Após salvar o Documento de Entrada, basta executar a rotina “Custo Standard/Custo de Reposição” (MATA320) com o "**Ultimo Preço de Compra**" para que o Custo Standard seja atualizado;
* Para validação do **tamanho dos campos** "**Atu.Pr.Compr**" (**F4\_UPRC**) e "**Ult. Compra**" (**B1\_UCOM**), validar o parâmetro de indicador de produtos (**MV\_ARQPROD = SB1**) para que o Cálculo do Custo Standard seja gerado corretamente.

**Detalhamento tecnico de todo o processo de calculo da rotina:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=448601697>

## **EXEMPLO DE CALCULO DO B1\_UPRC E B1\_CUSTD:**

**Considere o cenário de um documento de entrada contendo os itens abaixo ao custo de 10,00:**  
- Produto A, utilizando TES com F4\_ESTOQUE = N-Não e F4\_UPRC = N-Não  
- Produto B, utilizando TES com F4\_ESTOQUE = N-Não e F4\_UPRC = S-Sim  
- Produto C, utilizando TES com F4\_ESTOQUE = S-Sim e F4\_UPRC = N-Não  
- Produto D, utilizando TES com F4\_ESTOQUE = S-Sim e F4\_UPRC = S-Sim

**Ao final da inclusão do documento de entrada, temos:**  
- Produto A, B1\_CUSTD = 0, B1\_UPRC = 0  
- Produto B, B1\_CUSTD = 0, B1\_UPRC = 10  
- Produto C, B1\_CUSTD = 0, B1\_UPRC = 0  
- Produto D, B1\_CUSTD = 0, B1\_UPRC = 10

Observe que independente do conteúdo presente no campo **F4\_ESTOQUE**, o campo **B1\_CUSTD** mantém zerado e **B1\_UPRC** é atualizado de acordo com que é definido no campo **F4\_UPRC**.

**Após processamento da MATA320 utilizando o parâmetro "Calcula Custos por = Ultimo Custo de compra", temos:**  
- Produto A, B1\_CUSTD = 0, B1\_UPRC = 0  
- Produto B, B1\_CUSTD = 0, B1\_UPRC = 10  
- Produto C, B1\_CUSTD = 0, B1\_UPRC = 0  
- Produto D, B1\_CUSTD = 10, B1\_UPRC = 10

Observe que apenas o cenário do produto D, onde **F4\_ESTOQUE** e **F4\_UPRC** possuem o conteúdo "S-Sim", preencheu **B1\_CUSTD** e **B1\_UPRC** simultaneamente.

**E utilizando o parâmetro "Calcula Custos por = Ultimo preço de compra", temos:**  
- Produto A, B1\_CUSTD = 0, B1\_UPRC = 0  
- Produto B, B1\_CUSTD = 10, B1\_UPRC = 10  
- Produto C, B1\_CUSTD = 0, B1\_UPRC = 0  
- Produto D, B1\_CUSTD = 10, B1\_UPRC = 10

Já neste cenário, o campo **F4\_UPRC** é determinante para valorizar **B1\_CUSTD** e **B1\_UPRC** dos produtos B e C.

**Portanto, o campo F4\_ESTOQUE do TES apresentará maior impacto em cenários onde seja definido o parâmetro "Calcula Custos por = Ultimo Custo de compra", podendo preencher ou não B1\_CUSTD dependendo do conteúdo presente no campo F4\_UPRC.**

Já para atualizar **B1\_CUSTD e B1\_UPRC** simultaneamente por meio do parâmetro "Calcula Custos por = Ultimo preço de compra", basta definir "**F4\_UPRC** = Sim" na configuração do TES que será utilizado no documento de entrada.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Cálculos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012199493-SIGAEST-C%C3%81LCULOS)
