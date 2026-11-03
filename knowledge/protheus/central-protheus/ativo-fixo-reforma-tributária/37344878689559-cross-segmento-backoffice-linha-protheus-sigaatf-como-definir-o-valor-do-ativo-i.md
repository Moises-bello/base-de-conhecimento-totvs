---
article_id: 37344878689559
category: Ativo fixo - Reforma Tributária
content_hash: f28d29df037277baa2615881f1303308c803d688a53cc396b6834f8d295d8721
fetched_at: '2026-06-28T22:41:35.544801+00:00'
product: protheus
section_id: 37095895776791
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - Como definir o Valor
  do Ativo Imobilizado utilizando o Configurador de Tributos
type: support-article
updated_at: '2025-12-30T18:02:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37344878689559-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Como-definir-o-Valor-do-Ativo-Imobilizado-utilizando-o-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37344839421847) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Como definir o valor de aquisição do Ativo Imobilizado considerando a descontinuação dos campos da tabela SF4 (TES) e a implementação do Configurador de Tributos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Fixo - Versão 12.1.2410 ou superior  
  
**Solução**  
Com a implementação do Configurador de Tributos e a consequente descontinuação de campos da tabela SF4, o sistema adotou um novo mecanismo para a definição do valor do bem imobilizado na integração Compras x Ativo Fixo.

Este novo conceito utiliza um novo parâmetro MV\_VLATFCT, em conjunto com as **Regras de Custo** do Configurador de Tributos.

1. Passo a Passo sobre o novo mecanismo:  
     
   ![](https://tdn.totvs.com/download/attachments/977836829/Definir%20o%20valor%20do%20bem%20imobilizado%20-%20MV_VLATFCT%20-%20CFGTRIB.gif?version=1&modificationDate=1755540648910&api=v2)
2. Para configuração, siga os passos abaixo:

   1. **Configuração do Parâmetro MV\_VLATFCT:** Este parâmetro substitui a lógica do antigo MV\_VLRATF para ambientes que utilizam o Configurador de Tributos. Ele permite definir uma fórmula baseada exclusivamente nos campos da tabela **SD1** (Itens da Nota Fiscal de Entrada).  
        
      Exemplo:  
        
      ![](https://tdn.totvs.com/download/attachments/977836829/image-2025-5-1_13-4-43.png?version=1&modificationDate=1755540647873&api=v2)
   2. **Configuração da Regra de Custo (Configurador de Tributos):** Após o cálculo do valor base pelo parâmetro, o sistema verifica se há tributos calculados pelo Configurador (campo D1\_IDTRIB preenchido). O impacto desses tributos no valor do ativo (somar ou subtrair) é definido na **Regra de Custo**.  
        
      **Caminho:** *Configurador de Tributos > Regras Estoque/Custos > Regra de Custo*.

      * **0 – Sem Ação:** O tributo não altera o valor do bem.
      * **1 – Soma:** O valor do tributo é adicionado ao custo do bem (Ex: IPI não recuperável).
      * **2 – Subtrai:** O valor do tributo é deduzido do custo do bem (Ex: ICMS/IBS recuperável).  
          
        ![](https://tdn.totvs.com/download/attachments/977836829/image-2025-4-30_14-58-15.png?version=1&modificationDate=1755540648013&api=v2)  
          
        Exemplo de cadastro:  
          
        ![](https://tdn.totvs.com/download/attachments/977836829/image-2025-4-30_14-56-7.png?version=1&modificationDate=1755540648143&api=v2)
   3. Após criar a regra de custo, vincule-a à **Regra de Cálculo de Documentos Fiscais** no campo "Custo".  
        
      ![](https://tdn.totvs.com/download/attachments/977836829/image-2025-4-30_14-57-2.png?version=1&modificationDate=1755540648073&api=v2)
3. **Requisitos para Funcionamento:** O novo mecanismo será acionado apenas quando todas as condições abaixo forem verdadeiras:

   * O ambiente possuir o campo D1\_IDTRIB criado.
   * O documento de entrada possuir o campo D1\_IDTRIB preenchido (cálculo pelo Configurador).
   * O parâmetro MV\_VLATFCT estiver configurado com valor diferente de vazio.
4. **Exemplo Prático de Cálculo**:  
     
   Considere o seguinte cenário :

   * **Valor Total da Nota (D1\_TOTAL):** R$ 1.000,00
   * **Desconto (D1\_VALDESC):** R$ 100,00
   * **ICMS Calculado:** R$ 120,00
   * **Fórmula MV\_VLATFCT:** (SD1->D1\_TOTAL - SD1->D1\_VALDESC)
   * **Regra de Custo do ICMS:** Operação 2 (Subtrai)

   **Cálculo realizado pelo sistema:**

   * **Valor Base (Fórmula):** 1.000,00 - 100,00 = **900,00**.
   * **Aplicação do Custo (Regra):** 900,00 - 120,00 (ICMS) = **780,00**.
   * **Valor Final do Ativo:** R$ 780,00.

**Saiba Mais**  
[Valor do Ativo Imobilizado na Reforma Tributária: utilização do Configurador de Tributos](https://tdn.totvs.com/pages/viewpage.action?pageId=977836829)  
[Cross Segmento - Backoffice Linha Protheus - SIGAATF - Reforma tributária](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35706771532567-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Reforma-tribut%C3%A1ria)  
[Cross Segmento - Backoffice Linha Protheus - SIGAATF - Valor do Ativo Imobilizado considerando o Imposto Seletivo (IS)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37341307894423-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Valor-do-Ativo-Imobilizado-considerando-o-Imposto-Seletivo-IS)
