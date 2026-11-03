---
article_id: 360043794273
category: Desenvolvedor de Produtos (SIGADPR)
content_hash: 39ddf497e60eeaa3dbb85c947c94f1be72f33e7378cafd9d96da73d85eb855dd
fetched_at: '2026-06-28T22:42:48.750674+00:00'
product: protheus
section_id: 360005696254
source: central-protheus
title: Manufatura - Linha Protheus - SIGADPR - Funcionamento do cálculo de custos
  do DPR
type: support-article
updated_at: '2025-06-17T15:06:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043794273-Manufatura-Linha-Protheus-SIGADPR-Funcionamento-do-c%C3%A1lculo-de-custos-do-DPR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:02:20 min**  
**Dúvida**Como é o funcionamento do cálculo de custos no **DPR - Desenvolvedor de Produto**?  
   
 **Ambiente**Microsiga Protheus - Desenvolvedor de Produto - Versão 12  
  
**Solução**  
Abaixo será mostrado como funciona o programa de relatório de custos no **DPRC324 - Custo Fabricação**.  
  
Estrutura no **SIGADPR - Desenvolvedor de Produto**:  
O **GGF -** **Gastos gerais de fabricação** e a **Preparação** são calculadas com base nas operações.  
Quando **Considera Apenas Componentes DP** está **desmarcado.  
  
Exemplo:****DP1 - Produto Desenvolvido**  
|  
|---- Operação 10 - Montar - Tempo Operação 10 Tempo Preparação 1 Unidades 1 Máquina MAQ1  
|  
|---- Operação 20 - Desmontar - Tempo Operação 5 Tempo Preparação 0 Unidades 1 Máquina MAQ1  
|  
 |---- **EN1 - Produto SIGAPCP**   
|  
|---- **DP2 - Produto Desenvolvido**  
        |  
        |---- Operação 15 - Colar - Tempo Operação 1 Tempo Preparação 0 Unidades 1 Máquina MAQ1  
        |  
        |---- Operação 25 - Descolar - Tempo Operação 1 Tempo Preparação 0 Unidades 1 Máquina MAQ1  
  
**Tempo de Operação**  
 Entrarão neste cálculo todas as operações dos produtos desenvolvidos, ou seja, operações 10, 20, 15, 25.  
 Para cada operação será feito o seguinte cálculo: **GGF = Tempo Máquina \* (ValorGGF / Unidades)  
  
Tempo de Preparação**  
 Entrarão neste cálculo todas as operações dos produtos desenvolvidos, ou seja, operações 10, 20, 15, 25.  
 Para cada operação será feito o seguinte cálculo: **PREPARAÇÃO = Tempo Preparação \* ValorGGF**O **ValorGGF** vem do **SIGAPCP - Planejamento e Controle da Produção**. Esse valor é buscado com base no produto **mão de obra** do centro de custo da máquina da operação.  
  
**Componente Engenharia**  
 O **SIGADPR** não desce a estrutura de componentes de engenharia.  
 Para estes, é chamada uma função do **SIGAPCP** que retorna o valor do componente nos três custos: **GGF**, **Material** e **Preparação**.  
 O cálculo realizado com este valor é:

* **GGF Componente SIGAPCP = GGF Retornado pela SIGAPCP \* (Proporção / 100) \* (Quantidade Componente / 1)**
* **Preparação Componente SIGAPCP = Preparação retornada pelo SIGAPCP \* (Proporção / 100)**

No final do cálculo é gerado uma planilha com os valores detalhados de cada operação.  
  
**Importante**  
Quando **Considera Apenas Componentes DP** estiver **marcado**, são apenas utilizados os valores informados na aba **Custo** de cada produto desenvolvido.
