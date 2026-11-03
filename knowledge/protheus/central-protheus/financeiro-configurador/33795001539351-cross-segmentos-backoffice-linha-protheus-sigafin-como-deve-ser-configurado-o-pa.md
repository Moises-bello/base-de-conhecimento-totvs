---
article_id: 33795001539351
category: Financeiro - Configurador
content_hash: 3d9e3224450e11cd5077247735ff4bbb055b504f89d5e8f04dad1f8a83e9c620
fetched_at: '2026-06-28T22:37:57.630706+00:00'
product: protheus
section_id: 1500001539601
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como deve ser configurado
  o parâmetro MV_1DUP
type: support-article
updated_at: '2026-04-23T13:29:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33795001539351-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-deve-ser-configurado-o-par%C3%A2metro-MV-1DUP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33794987032983) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Como deve ser configurado o MV\_1DUP?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
  
**Solução**

O controle das parcelas geradas é realizado pelo tamanho do grupo de campos "**PARCELA**" na tabela **SX3** do **configurador**; portanto, as parcelas geradas irão respeitar o tamanho do campo e o conteúdo do parâmetro.  
Será considerado, neste caso, 1 para INICIAR em numérico e A para INICIAR em alfanumérico, independentemente do número de parcelas e da quantidade de caracteres informada no parâmetro. As parcelas serão geradas sempre respeitando o tamanho do campo E1\_PARCELA. Em caso de configuração do parâmetro como "1A", "A1" será considerado o primeiro caractere informado no parâmetro.

**Exemplo de cenário de devolução:**  
A condição para a correta geração das parcelas quando é feita a entrada de nota fiscal de devolução é a necessidade do parâmetro **MV\_1DUP** estar configurado com o mesmo tamanho do campo parcela. Pois o parâmetro trabalha em conjunto com os campos **E1\_PARCELA** e **E2\_PARCELA** do financeiro. Se o tamanho do campo parcela for igual a **02** o **MV\_1DUP** deve estar cadastrado como **“AA” ou “01”**, conforme documentação a seguir.

[Utilização do parâmetro MV\_1DUP](https://tdn.totvs.com/pages/releaseview.action?pageId=286197157)

**Importante**

Caso seja necessário alterar o tamanho do campo, será necessário executar o RDMAKE. Segue a documentação com o processo de ajuste e as orientações para execução do RDMAKE.

[Cross Segmentos - Backoffice Linha Protheus - FINA050 - Ajuste do campo PARCELA para dois caracteres ou alfanumérico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021873891-Cross-Segmentos-Backoffice-Linha-Protheus-FINA050-Ajuste-do-campo-PARCELA-para-dois-caracteres-ou-alfanum%C3%A9rico)
