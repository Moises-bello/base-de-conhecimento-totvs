---
article_id: 10005428982679
category: FÉRIAS
content_hash: 3f6c9ba1b1fe04805aa705ea84eeb7ff3b71b6ec78da8bf020419141deb4a550
fetched_at: '2026-06-28T22:44:34.544669+00:00'
product: protheus
section_id: 10299705719575
source: central-protheus
title: RH - Linha Protheus - Meu RH - Funcionalidade do parâmetro MV_PERC13S
type: support-article
updated_at: '2026-06-22T19:18:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10005428982679-RH-Linha-Protheus-Meu-RH-Funcionalidade-do-par%C3%A2metro-MV-PERC13S
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30648310384023) Tempo aproximado para leitura: **00:02:30min** **Dúvida**Funcionalidade do parâmetro **MV\_PERC13S**  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**O parâmetro **MV\_PERC13S** permite **informar** um **valor padrão** de **porcentagem** do **Adiantamento de 13º Salário** na Programação de Férias, que é lançado **automaticamente** ao **aprovar Solicitações de Férias** advindas do **Meu RH**, cuja opção "Adiantamento de 13º" foi selecionada.  
  
Essa funcionalidade estará disponível **a partir** do ***release* 12.1.33**, com a execução do "**Atualizador de dicionário e base de dados**" (UPDDISTR)  
  
Para que essa funcionalidade possa também ser utilizada a partir do ***release* 12.1.27** será necessário realizar o **cadastro manual** do parâmetro por meio do **Módulo Configurador**, seguindo a estrutura abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10005298564247)  
  
**Observações:**  
**O valor padrão inicial do parâmetro é 0 (zero)**, e poderá ser definido um outro valor de referência.  
O limite máximo considerado **pelo sistema será 100**, **mesmo que seja informado um valor superior**.  
  
Ao solicitar férias com **adiantamento de 13º Salário via meu RH**, no momento da integração com o  
Protheus é solicitada a **inclusão manual do percentual de 13º Salário** no Controle dos Dias de Direito do funcionário.  
  
Se o aprovador, equivocadamente, **não informar o percentual**, a solicitação é aprovada **sem valor definido**, e consequentemente, **ao realizar o cálculo das férias, o sistema não fará o cálculo do 13º Salário.**  
  
Dessa forma, **caso o parâmetro esteja com valor definido (diferente de 0)**, ao realizar a aprovação de uma solicitação de férias com 13º Salário, **o cadastro "Controle Dias de Direito" do funcionário**, deixará de ser apresentado, pois **o sistema irá considerar automaticamente o valor padrão do parâmetro MV\_PERC13S**.  
  
**Saiba Mais  
[Artigos sobre Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-Meu-RH)  
[RH - Linha Protheus - MEU RH - Aprenda sobre o MEU RH e como fazer a implantação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036164214)  
[CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)[para acessar mais artigos e FAQs sobre o MEU RH](%20https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)[para acessar a documentação de referência sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**
