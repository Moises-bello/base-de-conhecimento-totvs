---
article_id: 4402260339223
category: Gestão de Transportes (TMS)
content_hash: 67c170959bfa3120f3dcc070332fd83efc865888140eeb65d6eec6012b18ee9e
fetched_at: '2026-06-28T22:45:33.368110+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Série do MDFe
type: support-article
updated_at: '2025-12-11T17:28:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402260339223-Log%C3%ADstica-Linha-Protheus-TMS-S%C3%A9rie-do-MDFe
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36949148579479)**Tempo aproximado para leitura:**00:03:06 min**  
  
**Dúvida**  
Como utilizar a série do **MDFe** - **Manifesto Eletrônico de Documentos Fiscais** no módulo **TOTVS Logística TMS -** **Gestão de Transportes**.  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões   
  
**Solução**  
Para atender aos diferentes cenários de configuração de séries dos clientes, podemos configurar a série do **MDFe** de três formas no **TOTVS Logística TMS**:  
  
**Solução 1 - Série e numeração diferentes** para cada filial.  
Crie na tabela genérica **SX5** na tabela **PT**, os registros de série e numeração. Por padrão, **a tabela** **SX5** **completa deve estar compartilhada.**

![Captura_de_tela_2021-06-07_105213.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4402261228823)

Após crie o parâmetro **MV\_SERMAN - Serie do Manifesto utilizada no modulo TMS** exclusiva para cada filial informando a série.

**![Captura_de_tela_2021-06-07_105904.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4402261479703)**

**Solução 2** - **Série igual** e **numeração diferentes** para cada filial com a tabela **SX5 exclusiva**.

* Utilizar a SX5 - **na sua totalidade como exclusiva**

**![Captura_de_tela_2021-08-16_140230.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4406435010839)**

* E realizar e configurar o parâmetro **MV\_SERMAN** por filial.

![Captura_de_tela_2021-08-16_140755.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4406435015831)

**Solução 3 - Série igual** e **numeração diferentes** para cada filial com a tabela **SX5 compartilhada.**

* Utilize o ponto de entrada **TMALTSERIE** para definir a série a ser utilizada em cada filial, sobrescrevendo a série definida pelo **MV\_SERMAN** pela série desejada.
* Segue exemplo: Tenho duas filiais, **01** e **02**. Quero que as duas filiais utilizem a série **001**, mas com sequências numéricas distintas. No exemplo, defini o início da sequência numérica da filial **01** como **0105** e da filial **02** como **0106**. Para isso, é necessário que:
* A **SX5** esteja completamente compartilhada, sem registros com o campo **X5\_FILIAL** preenchido.

![](https://totvssuporte.zendesk.com/attachments/token/qnUNYubaNvokWsNYtvXL4KcKb/?name=inline-749793137.png)

* Utilizar o parâmetro **MV\_SERMAN** exclusivo por filial, cada um com uma série e utilizar o ponto de entrada **TMALTSERIE** para alterar as séries a ser utilizadas em cada filial.

![](https://totvssuporte.zendesk.com/attachments/token/yuz05alA0wZqsVhRnqjRbp0s0/?name=inline-564450856.png)

![](https://totvssuporte.zendesk.com/attachments/token/1B1VNYWdxeCgnZ9iv0tjL26LD/?name=inline1460420370.png)

* Dessa forma, o comportamento do Sistema fica com a série e a sequência numérica diferentes por filial, e aí entra o ponto de entrada [TMALTSERIE](https://tdn.totvs.com/pages/viewpage.action?pageId=632817427) para tratar a necessidade. Note que no fonte esta definido para sempre mudar a série para 001. O fonte pode ser ajustado conforme sua necessidade:

![](https://totvssuporte.zendesk.com/attachments/token/Kj7NjrDwzww9987sHUr9JbME4/?name=inline867046650.png)

* Ao gerar dois manifestos, um na filial **01** e outro na filial **02**, e o resultado final é cada um dos manifestos com sua **sequência numérica específica, mas ambos com a série 001.**

**![](https://totvssuporte.zendesk.com/attachments/token/LJgwzxwm2o8FIJayv74eCfApP/?name=inline1667267013.png)**

**Importante**  
A partir de 29/03/2021 o ponto de entrada **CHGX5FIL** não é utilizado no fonte **TMSA190 - Manifesto**.  
Anteriormente este ponto de entrada era utilizado no fonte **TMSA190 - Manifesto,** contudo, devido a evolução de tecnologia a **tabela genérica SX5** deverá ser apenas compartilhada ou exclusiva.  
  
**Saiba mais**  
Para mais informações sobre o ponto de entrada **TMALTSERIE**, acesse o *link* [TMALTSERIE - Manipulação do conteúdo da série do MDF-e](https://tdn.totvs.com/pages/viewpage.action?pageId=632817427)
