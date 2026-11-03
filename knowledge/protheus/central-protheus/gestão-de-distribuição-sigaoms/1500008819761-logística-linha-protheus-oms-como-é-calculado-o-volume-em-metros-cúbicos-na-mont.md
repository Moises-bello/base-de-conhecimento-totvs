---
article_id: 1500008819761
category: Gestão de Distribuição (SIGAOMS)
content_hash: aa086fda147a2f62b80367272d68c2c03ed2f0bbdb7b23d9c6869fe2d15ff33b
fetched_at: '2026-06-28T22:45:49.672705+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Como é Calculado o Volume em Metros Cúbicos
  na Montagem de Carga
type: support-article
updated_at: '2025-07-11T13:18:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008819761-Log%C3%ADstica-Linha-Protheus-OMS-Como-%C3%A9-Calculado-o-Volume-em-Metros-C%C3%BAbicos-na-Montagem-de-Carga
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33398914699287)** Tempo aproximado para leitura: **00:01:24 min**  
  
**Dúvida**  
Como é Calculado o Volume em Metros Cúbicos na Montagem de Carga  
  
**Ambiente**  
TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**  
Para calcular o volume em metros cúbicos (m³) na rotina de Montagem de Carga - OMSA200, o Sistema considera as seguintes informações:  
  
O volume de cada produto é calculado a partir dos campos:

* Altura  - B5\_ALTURLC
* Largura - B5\_LARGLC
* Comprimento  - B5\_COMPRLC

Esses dados estão localizados na aba **Logística do Cadastro de Complemento do Produto - MATA180**.  
  
A fórmula aplicada pelo Sistema é: **B5\_ALTURLC×B5\_LARGLC×B5\_COMPRLC×Quantidade do item no pedido**  
  
Durante a seleção dos pedidos na tela da Montagem de Carga, o Sistema atualiza automaticamente:

* O campo **Volume M3 -** **DAK\_CAPVOL** na tabela **DAK - Cargas**, que representa a soma dos volumes de todos os produtos vinculados aos pedidos selecionados para a carga.
* O campo **Capac.Volum. -** **DAI\_CAPVOL** em cada item da carga - **tabela DAI**, que representa o volume individual de cada produto associado ao respectivo pedido de venda.

**Exemplo de cálculo:**  
Pedido de venda com 10 unidades de um produto com as seguintes dimensões:

* Altura: 1,70 m - B5\_ALTURLC
* Largura: 0,90 m - B5\_LARGLC
* Comprimento: 0,90 m - B5\_COMPRLC

Resultado Cálculo individual:  
1,70 × 0,90 × 0,90 = 1,377 m³  
  
Resultado Cálculo total (10 unidades):  
1,377 × 10 = 13,77 m³  
  
**Importante**  
Para conhecimento, o peso cubado representa o espaço que a carga ocupa no veículo, considerando seu volume. A partir do volume em metros cúbicos (m³), o cálculo é feito multiplicando esse valor pelo fator de cubagem, que varia conforme o modal de transporte utilizado.  
  
Para obter o peso cubado, basta multiplicar o volume da carga (em m³) pelo fator de cubagem, que varia de acordo com o modal de transporte:

|  |  |
| --- | --- |
| Modal | Fator de Cubagem (kg/m³) |
| Rodoviário | 300 |
| Aéreo | 167 |
| Marítimo | 1.000 |

Exemplo prático:  
Uma carga com volume de 2,5 m³:

* Transporte rodoviário: 2,5 × 300 = 750 kg (peso cubado)
* Transporte aéreo: 2,5 × 167 = 417,5 kg (peso cubado)
* Transporte marítimo:2,5 × 1.000 = 2.500 kg (peso cubado)

**Na rotina de Montagem de Carga, o Sistema não realiza o cálculo do peso cubado — apenas calcula o volume em metros cúbicos (m³) dos itens incluídos na carga.**  
  
Caso seja necessário modificar o cálculo padrão de volume, é possível utilizar o seguinte ponto de entrada: [OMSCPARM – Cálculo do Volume do Produto](https://tdn.totvs.com/pages/releaseview.action?pageId=616949245)
