---
article_id: 38323235564567
category: Financeiro - Baixas a Receber
content_hash: fc12260839054270757b0a077afdbf153dac1179e4affe32c2da0f5014d7edc6
fetched_at: '2026-06-28T22:37:43.693734+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Como gerar os impostos
  quando a baixa é por dação?
type: support-article
updated_at: '2026-02-11T13:34:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38323235564567-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Como-gerar-os-impostos-quando-a-baixa-%C3%A9-por-da%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38323235554071) Tempo aproximado para leitura: **00:05 min**

Dúvida  
Como gerar os impostos quando a baixa é por dação? 

Ambiente  
Cross Segmento - Backoffice Linha Protheus - Financeiro - Todas as versões.

Solução

Quando a baixa é realizada sem movimentação bancária, o sistema não realiza a geração dos impostos no momento da baixa, conforme demonstrado na imagem abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38324642716823)

Para que os impostos sejam gerados mesmo quando o motivo de baixa sem movimento bancário, é necessário ajustar o parâmetro **MV\_MB10925** para o valor **2**.

O parâmetro **MV\_MB10925** determina se o sistema irá calcular os impostos considerando apenas as baixas que geram movimentação bancária ou todas as baixas, independentemente da geração de movimento. Esse parâmetro impacta diretamente no cálculo dos impostos **PIS, COFINS, CSLL e IR**.

O funcionamento do parâmetro está vinculado ao cadastro da **Tabela de Motivos de Baixa**, onde se define quais tipos de baixa devem ou não gerar movimentação bancária. Este cadastro pode ser acessado em:  
**Financeiro > Miscelânea > Arquivos > Tabela de Motivos de Baixas (FINA490).**

**Importante**

Existe uma exceção para o motivo de baixa **CMP (Compensação)**, pois neste caso a movimentação bancária é considerada no RA/PA compensado e não na própria movimentação de compensação.

Outro ponto a ser observado é que esse parâmetro é válido tanto para **Contas a Receber** quanto para **Contas a Pagar**.

As opções de configuração do parâmetro são:

* **1** – Calcula impostos apenas para os motivos que geram movimentação bancária. (Configuração padrão)
* **2** – Calcula impostos para todos os motivos de baixa, independentemente de gerar ou não movimentação bancária.

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38324642719255)
