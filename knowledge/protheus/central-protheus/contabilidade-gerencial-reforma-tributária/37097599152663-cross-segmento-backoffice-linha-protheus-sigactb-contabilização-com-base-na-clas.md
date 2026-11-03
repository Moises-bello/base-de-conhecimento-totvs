---
article_id: 37097599152663
category: Contabilidade gerencial - Reforma Tributária
content_hash: 06e53b431b2b417df872a6c4bce71a30073c418a2e574e7217f13fef8fdc28ff
fetched_at: '2026-06-28T22:40:29.704111+00:00'
product: protheus
section_id: 37095816599831
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Contabilização com Base
  na Classificação do Tributo
type: support-article
updated_at: '2025-12-17T20:41:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37097599152663-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Contabiliza%C3%A7%C3%A3o-com-Base-na-Classifica%C3%A7%C3%A3o-do-Tributo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37097613058839) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
Como realizar a contabilização de documentos fiscais utilizando a Classificação do Tributo no Protheus?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial - Todas as versões  
  
**Solução**  
Visando aprimorar o processo contábil e simplificar a manutenção de regras, foi implementada uma solução que permite a contabilização através da **Classificação do Tributo** (definida na Regra de Cálculo) em vez de utilizar apenas a sigla específica (campo F2D\_TRIB).

Esta abordagem permite configurações de sequências contábeis mais genéricas e maior reutilização de parâmetros.

Para viabilizar este processo, deve-se utilizar a função de contabilização **CTBVLTRIB** diretamente nos Lançamentos Padrões.

1. **Sintaxe da Função:**

   CTBVLTRIB (<ID\_TRIBUTO>, <TRIBUTO>, <OPERACAO>, <LDESDOCENT>)

   * <ID\_TRIBUTO>: Campo que contém o ID do tributo (Ex: SD1->D1\_IDTRIB ou SD2->D2\_IDTRIB)
   * <TRIBUTO>: Campo com a sigla do tributo desejado, criado no configurador de tributo (Ex: "ICMS", "IPI").  
       
     ![](https://tdn.totvs.com/download/attachments/977835821/image-2025-4-30_14-33-31.png?version=1&modificationDate=1755537791043&api=v2)
   * <OPERAÇÃO>: (.T. ou .F.) Indica se deve considerar a regra de custo (Soma/Subtração) configurada para o tributo no Configurador de Tributos. Campo opcional
   * <LDESDOCENT>: (.T. ou .F.) Indica se retorna o valor desmembrado para Ativo Fixo no módulo de Compras (SD1). O padrão é .F..  Campo opcional

     **Exemplo de uso:**  
     ![](https://tdn.totvs.com/download/attachments/977835821/image-2025-4-30_14-29-57.png?version=1&modificationDate=1755537790777&api=v2)  
       
     OBS: Caso o argumento <operação> e <LDESDOCENT> não seja informado, o valor padrão (*default*) para a ambos será **falso** (.F.).
2. **Uso do argumento <Operação>:**  
   Ao definir como verdadeiro (.T.), a função respeita a regra definida no Configurador de Tributos em regra de custo:

   * **Operação 0 (Sem Ação)**: A função retorna zero.
   * **Operação 1 (Somar)**: A função retorna o valor do tributo.
   * **Operação 2 (Subtrair)**: A função retorna o valor do tributo com sinal negativo, facilitando cálculos de valor líquido.  
       
     Cadastro Regra Custo:  
       
     **![](https://tdn.totvs.com/download/attachments/977835821/image-2025-4-30_14-58-15.png?version=1&modificationDate=1755537790590&api=v2)**  
       
     Exemplo de Cadastros:

     **![](https://tdn.totvs.com/download/attachments/977835821/image-2025-4-30_14-56-7.png?version=1&modificationDate=1755537790527&api=v2)**

     Vinculo do Custo a Regra de Cálculo Documentos Fiscais:

     **![](https://tdn.totvs.com/download/attachments/977835821/image-2025-4-30_14-57-2.png?version=1&modificationDate=1755537790653&api=v2)**  
       
     **Exemplo de uso com lógica condicional:**  
       
     IIF(CTBVLTRIB(SD1->D1\_IDTRIB, "ICMS", .T.) < 0, FAÇA\_X(), FAÇA\_Y())  
       
     Neste exemplo, a função verifica se o valor do tributo é negativo, permitindo executar diferentes rotinas conforme o tipo da operação (como crédito ou débito).

     **Exemplo de cálculo com ajuste automático:**

     SD1->D1\_TOTAL + CTBVLTRIB(SD1->D1\_IDTRIB, "ICMS", .T.)

     Se CTBVLTRIB retornar **-180** e D1\_TOTAL for **1000**, o resultado será **820**.  
       
     Esse cálculo representa o valor líquido da operação, considerando automaticamente a dedução do ICM — viabilizada pelo sinal negativo retornado pela função.

     Esse comportamento é especialmente útil para simplificar regras e fórmulas nos lançamentos contábeis, evitando a necessidade de ajustar o sinal manualmente.  
       
     Verifique na documentação abaixo exemplos utilizando a operação de custo:  
     [Documentação operação de custo](https://tdn.totvs.com/pages/viewpage.action?pageId=977835821#:~:text=C%C3%A1lculo%20Documentos%20Fiscais%3A-,03.%20OPERA%C3%87%C3%83O%20DE%20CUSTO,-Abaixo%20ser%C3%A1%20demonstrado)
3. **Configuração para Ativo Fixo (argumento <****LDESDOCENT****>):**   
     
   Caso a TES esteja configurada para desmembrar ativos (F4\_BENSATF = Sim), o uso de .T. no quarto argumento fará com que o sistema divida o valor do imposto pela quantidade de itens da nota (D1\_QUANT), permitindo a contabilização individual por bem.  
     
   Exemplo de chamada da função com o quarto parâmetro: CTBVLTRIB(SN1→N1\_IDTRIB,"IBSEST",,.T.)

**Saiba mais**  
[Contabilização com Base na Classificação do Tributo](https://tdn.totvs.com/pages/viewpage.action?pageId=977835821)  
[Contabilidade Gerencial - Reforma Tributária](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35707320972439-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Reforma-tribut%C3%A1ria)  
[Ativo fixo - Reforma Tributária](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35706771532567-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Reforma-tribut%C3%A1ria)
