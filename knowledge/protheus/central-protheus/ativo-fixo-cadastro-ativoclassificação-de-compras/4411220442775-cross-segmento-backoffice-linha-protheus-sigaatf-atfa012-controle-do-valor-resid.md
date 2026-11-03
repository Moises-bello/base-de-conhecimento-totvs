---
article_id: 4411220442775
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: 1be40d20c53ca939ae7fbd9e144ef50b6bb555c9b168c44d67164c2ae580960c
fetched_at: '2026-06-28T22:41:48.344593+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA012 - Controle do
  Valor residual no Ativo fixo
type: support-article
updated_at: '2021-11-04T13:45:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411220442775-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-Controle-do-Valor-residual-no-Ativo-fixo
---

**Dúvida**Controle do Valor residual no Ativo fixo e CPC 23 - Políticas Contábeis, Mudança de Estimativa e Retificação de Erro.

**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - Ativo Fixo- Todas as versões

**Solução**

O método de depreciação mais comum que é o "linear" para esses casos o controle do valor residual é a diferença entre o valor original e o valor de depreciação acumulada, este valor é de controle interno do sistema, ou seja, não há um campo que o controle.

Já o método "Linear com valor máximo de depreciação" visa demonstrar, ao término da vida útil do bem,  um valor residual para a empresa..

Neste método é obrigatório o preenchimento do campo **Vlr. Max. Depre.**(N3\_VMXDEPR), que determina o valor máximo da depreciação.

Características do cálculo:

A alíquota é fixa e definida em função da vida útil do bem.

A fórmula para determinar a alíquota é:

Taxa de depreciação anual = 100% / Vida útil do bem

Taxa de depreciação mensal = (100% / Vida útil do bem) / 12

A fórmula para determinar o valor da depreciação é::

Depreciação anual = Valor máximo de depreciação \* Taxa de depreciação anual

Depreciação mensal = Valor máximo de depreciação \* Taxa de depreciação mensal

Onde:

***Valor máximo de depreciação:*** valor definido pelo governo para fins fiscais ou especificado pelo profissional de contabilidade ou patrimônio em função da expectativa de retorno do bem para empresa após o término de sua vida útil.

No cadastro do ativo (ATFA012)

No exemplo a seguir o Bem possui uma valor de aquisição de R$5.000,00 e para o tipo 12 um valor máximo de depreciação de R$1.000,00, ou seja, quando a depreciação acumulada atingir R$4.000,00 o bem não será mais depreciado, permanecendo com um valor residual de R$1.000,00.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411253518359/mceclip2.png)

Para atender a CPC 23 (Políticas Contábeis, Mudança de Estimativa e Retificação de Erro) ou ajuste do valor residual por outros motivos pode ser utilizado a rotina ATFA380.

Levando em consideração o exemplo acima, caso o valor residual seja R$900,00 e não R$1.000,00 o ajuste será da seguinte forma: Informar o valor estimado para venda (conforme laudo, ou definido pelo contador) e ajustar o valor residual.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411262411159/mceclip5.png)

Analisando a SN4 podemos ver que o bem tipo 12 com valor residual antigo será baixado (n4\_motivo= 08) e um novo tipo com valor atual será incluído.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411262605335/mceclip6.png)

E no cadastro do bem (SN3) o tipo 12 anterior ficará baixado e permanecerá visível para histórico.

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411254456727/mceclip7.png)

**Saiba mais**

[CPC - Impacto da convergência contábil IFRS/CPC nos módulos da Controladoria Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=6068474)

[Metodos de Calculo de depreciação](http://tdn.totvs.com.br/pages/releaseview.action?pageId=6067612)

[Tipos de ativo N3\_TIPO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035878114-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-Tipos-de-ativo-campo-N3-TIPO-)
