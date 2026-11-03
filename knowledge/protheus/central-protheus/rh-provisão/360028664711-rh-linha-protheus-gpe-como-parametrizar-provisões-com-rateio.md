---
article_id: 360028664711
category: RH - Provisão
content_hash: 948afeaa566877b4569e1c15b4995817473366a5bc4d96bc8fc47c64dde9c2a6
fetched_at: '2026-06-28T22:43:55.842046+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como Parametrizar Provisões com Rateio
type: support-article
updated_at: '2024-07-22T20:27:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028664711-RH-Linha-Protheus-GPE-Como-Parametrizar-Provis%C3%B5es-com-Rateio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25080173210775) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Como Parametrizar Provisões com Rateio.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**A provisão pode ser rateada por centro de custo, item contábil e classe valor (*MV\_ITMCLVL*) conforme necessidade da empresa. Para que o cálculo do rateio seja habilitado, o sistema valida as seguintes informações:

1. Acesse o Configurador e configure o Parâmetro **MV\_RATPROV**com **S;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25080186579479)**

2. Verifique se os Ids de Cálculo 0960, 0961, 0962, 0963, 0964, 0965, 0966, 0967, 0968, 0969, 0970 e 0971 já estão cadastrados. Estes ID’s são necessários para que sejam calculados os valores mensais de provisão conforme programação de rateio;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25080186589463)  
**Importante:** Estas verbas devem ser cadastradas como Base Provento, e sem nenhuma incidência.

3. Acesse a rotina GPEA056 - Programação de Rateios, e informe a Programação de Rateio dos Funcionários.    
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25080186596887)  
**Observações:**- A Programação de Rateio fica armazenada na tabela RHQ.

- Uma vez cadastrada a programação de rateio, esta não deve ser alterada ou excluída. Caso isso ocorra, o sistema perde a referência do cálculo anterior executa o próximo como sendo o primeiro cálculo de rateio e neste caso irá gerar os lançamentos de provisão rateada como acumulados (1º cálculo de rateio é sempre acumulado. A partir do 2º cálculo, o sistema irá demonstrar a provisão mês a mês).

4. Após confirmar toda configuração, no menu da Provisão (GPEA070) será liberada a opção de “Provisão Rateada” em “Outras Ações”;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25080173239191)

Após realizados o cálculo da provisão normal da competência, o sistema irá continuar gravando a provisão na tabela SRT e a provisão que for rateada na tabela RHT, conforme definição da programação cadastrada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25080186604567)

5. Para conferência dos valores gerados no cálculo da provisão de rateio, foram criados os relatórios "Impr. Mensal de Férias" e "Impr. Mensal de 13".

Relatório Mensal de Férias:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25080173245591)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25080186615319)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25080173251095)  
  
  
Relatório Mensal de 13º Salário:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25080173261975)

Saiba Mais:  
[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)   
[Provisão Rateada](http://tdn.totvs.com/pages/releaseview.action?pageId=382561210)
