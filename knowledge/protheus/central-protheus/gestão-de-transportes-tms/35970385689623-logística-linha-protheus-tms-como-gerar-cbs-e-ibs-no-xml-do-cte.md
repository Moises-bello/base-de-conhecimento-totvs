---
article_id: 35970385689623
category: Gestão de Transportes (TMS)
content_hash: 960982bad3f9b3a5e3cc13c927361ac76f65e6a639f1cae19dbb3e4eda6df1c8
fetched_at: '2026-06-28T22:45:27.455421+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Como gerar CBS e IBS no XML do CTe
type: support-article
updated_at: '2026-06-22T11:26:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35970385689623-Log%C3%ADstica-Linha-Protheus-TMS-Como-gerar-CBS-e-IBS-no-XML-do-CTe
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35970385661591) Tempo aproximado para leitura: **00:07:50 min**  
  
**Dúvida**  
Como cadastrar o Configurador de Tributos para gerar as novas *tags* referente ao **CBS e IBS no XML do CTe**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**  
Para que o **XML** do **CTe** seja gerado com as novas *tags* do **CBS** e **IBS**, o **TMS** deve estar atualizado com o pacote acumulado mais recente, e **Configurador de Tributos - FISA170** deve estar atualizado e configurado com:  
  
Antes de iniciar as configurações descritas neste artigo, é necessário garantir que o **Configurador de Tributos - FISA170** já esteja devidamente preparado para uso do calculo do frete do **Protheus TMS**, para isso, recomendamos primeiramente seguir as orientações do artigo disponível abaixo na seção Anexo - **Logística - Linha Protheus - TMS - Exemplo de uso do Configurador de Tributos no TMS.**  
  
Se esta primeira etapa já estiver concluída, então, o próximo passo é importar a tabela de códigos de classificação tributaria do **IBS** e **CBS** disponível no artigo - **CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como importar a tabela cClassTrib-IBS/CBS no Configurador de Tributos?**  
  
No **Configurador de Tributos**, podemos configurar todos os impostos como **CBS, IBS, ICMS**, **PIS**, **COFINS**, entre outros. Outra opção é configurar apenas os novos impostos do **CBS** e **IBS** para que o cálculo ocorrade forma **hibrida,** mantendo o cálculo dos demais impostos atuais pelos **cadastros do legado**,conformeorientações descritas neste artigo disponível na seção Anexo - **CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar o calculo do IBS e CBS?**  
  
Inicialmente para quem ainda não se adequou a Reforma Tributária, sugerimos a opção de cálculo hibrido, por ser a opção mais prática e com menos risco de impacto na operação. Posteriormente, validada a transmissão do **CTe** com **CBS** e **IBS**, o cliente pode ir migrando gradativamente os impostos do legado para o **Configurador de tributos.**  
  
Caso esteja utilizando o fonte CTESEFAZ3 customizado, sugerimos que validem com o CTESEFAZ padrão, ou então, compilem o CTESEFAZ3 disponível na seção Anexo.  
  
Validadas essas etapas e artigos, se ainda não estiver gerando as novas *tags* no **XML** do **CTe**, então, no **Configurador de Tributos**, no cadastro de **Regra de Escrituração** do **IBS** e **CBS**. A **Incidência** deve ser **Isento,** na seção **Código de Classificação Tributária IBS e CBS**, o campo **Class Trib** - **CJ2\_CSTCCT** deve estar preenchido obrigatoriamente com 000001 e o campo **CST** com 000 - Tributação Integral, exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35971153324311)

Esta **Regra de Escrituração** deve estar associada ao cadastro de **Regra de Cálculo - Documentos Fiscais** relacionado aos tributos do **IBS** e **CBS**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985160702487)

Os cadastros de **Regra de Cálculo - Documentos Fiscais** relacionado aos tributos do **IBS** e **CBS** devem estar associado ao seu respectivo **Tributo** através do campo **F2B\_TRIB:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36640674672407)

Este **Tributo** deve possuir o campo **Id Tributo** preenchido corretamente conforme cada um dos impostos utilizados, exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36640687946903)

A relação entre **Tributos** e **Id. Tributo** é a seguinte:

* Tributo **CBSFED** possui o Id. Tributo **000062**;
* Tributo **IBSMUN** possui o Id. Tributo **000061**;
* Tributo **IBSEST** possui o Id. Tributo **000060**;

Ainda nos cadastros de **Regra de Cálculo - Documentos Fiscais** relacionado aos tributos do **IBS** e **CBS,** em **Configuração de Arredondamento,** utilize a opção **1 - Arredonda.** Esta configuração é indicada para evitar rejeições relacionadas a arredondamentos de impostos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37856359971095)

No cadastro de **Regra de Base de Cálculo** do **CBS e IBS**, no campo**Valor Origem**, utilize **11 - Fórmula Manual**, e, na **Composição da Fórmula**, utilize **Valor da Mercadoria.** Para o **TMS**, o **Valor da Mercadoria** será o **Valor do Frete - DT6\_VALFRE**.   
A orientação de uso desta base de cálculo para o **CBS** e **IBS**, parte da compreensão da **LEI COMPLEMENTAR Nº 214, DE 16 DE JANEIRO DE 2025, artigo 12** que diz: *"A base de cálculo do IBS e da CBS é o valor da operação",* ou seja, o valor da base de cálculo do **IBS**e **CBS**não contém valores de impostos, como **ICMS**, **PIS**e **Cofins**.   
Caso o usuário utilize outras fórmulas de base de cálculo, poderá ocorrer rejeições ou falhas de schema na transmissão do **CTe**.  
Importante destacar que neste momento da Reforma Tributaria, os novos tributos são apenas destacados no **XML**, eles ainda não compõem o valor total da prestação de serviço.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40077242254103)

Desta forma, no **XML** do **CTe**, teremos as novas *tags* **gIBSCBS**, **gIBSUF** e **gIBSMun**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35971379839511)

As novas *tags* são geradas apenas no **XML**. No **DACTe** ainda elas ainda não são impressas porque a **SEFAZ** não disponibilizou nenhum manual para impressão do **DACTe** com os novos impostos.  
  
Se o **XML** for gerado sem qualquer uma destas três *tags* **gIBSCBS**, **gIBSUF** ou **gIBSMun,** teremos falha na transmissão do CTe com erro de schema.  
  
Para validar se o documento foi gerado da forma esperada com novos tributos, visualize o documento, aba Impostos. Caso a aba Impostos não seja visualizada ao consultar o documento, basta habilitar o parâmetro **MV\_TMSCFIS**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39930233264407)

Caso não tenha qualquer um dos três novos tributos, deve ser verificado os cadastros de **Regra de Cálculo - Documentos Fiscais** relacionado tributo faltante.  
  
Neste momento atual da Reforma Tributaria, no **XML** do **CTe**, é obrigatório a geração da *tag* **gIBSMun** referente ao **IBS Municipal.** O **IBS Municipal** deve ser incluído de forma manual no **Configurador de Tributos** com alíquota de imposto zerada e isento. Caso tenha utilizado a opção de **Carga Regras de Calculo CBS/IBS,** este tributo não estará contido na geração do documento e do **XML**, pois ele não faz parte desta carga de dados, desta forma, teremos falha de schema na transmissão do CTe:   
**Element '{http://www.portalfiscal.inf.br/cte}vIBS': This element is not expected. Expected is ( {http://www.portalfiscal.inf.br/cte}gIBSMun ).**  
  
Visualizando o documento no **Protheus TMS**, teremos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35971613598743)

Note que a base de calculo do **IBS** e **CBS** é o Valor do Frete, campo **DT6\_VALFRE**. A orientação de uso desta base de calculo parte da compreensão da **LEI COMPLEMENTAR Nº 214, DE 16 DE JANEIRO DE 2025, artigo 12** que diz: "A base de cálculo do **IBS** e da **CBS** é o valor da operação". O valor da base de calculo do IBS e CBS não deve conter os valores de impostos, ICMS, PIS e Cofins.  
  
Para obter este valor, podemos configurar de forma manual o cadastro da **Regra de Base de Calculo** do **IBS** e **CBS** e utilizar o Valor da Mercadoria. Para o **Protheus TMS**, o Valor da Mercadoria será o Valor do Frete, campo **DT6\_VALFRE**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35972059254679)

Podemos utilizar também a **Carga Regras de Calculo CBS/IBS.** Esta opção, é um facilitador contendo uma carga de dados de forma automática para os cadastros dos novos impostos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35972059256087)

Ao utiliza-la, teremos um cadastro de **Regra de Base de Calculo** para o **IBS/CBS** incluído de forma automática:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35972059258007)

Composto com a seguinte fórmula:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35972059259543)

Caso esta fórmula seja modificada, o calculo da base e do valor do imposto do **IBS** e **CBS** serão afetados, podendo resultar em rejeição do **SEFAZ**, entre elas, a **Rejeição 318** na transmissão do **CTe**. Desta forma, sugerimos que utilizem uma das duas formulas apresentadas aqui, manual ou automática.  
  
**Glossário**  
**CBS -** Contribuição sobre Bens e Serviços - Contribuição de caráter federal que substituirá o PIS e COFINS.  
**CTe** - Conhecimento de Transporte eletrônico.  
**DACTe** - Documento Auxiliar do Conhecimento de Transporte eletrônico.  
**gIBSCBS** - Grupo de informações destinado ao IBS e CBS.  
**gIBSUF** - Grupo de informações do IBS devido ao Estado de destino.  
**gIBSMun** - Grupo de informações do IBS devido ao Município de destino.  
**IBS** - Imposto sobre Bens e Serviços - Tributo de caráter estadual e municipal, substituirá o ICMS e o ISS.  
**SEFAZ** - Secretaria da Fazenda.  
**XML** - Extensible Markup Language.  
  
**Anexo**  
[Webinar TOTVS | Como gerar CTe com IBS e CBS](https://www.youtube.com/watch?v=6hLQDJ-AWgk)  
[Logística - Linha Protheus - TMS - Exemplo de uso do Configurador de Tributos no TMS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32213798486167-Log%C3%ADstica-Linha-Protheus-TMS-Exemplo-de-uso-do-Configurador-de-Tributos-no-TMS)  
[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como importar a tabela cClassTrib-IBS/CBS no Configurador de Tributos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34662420522391-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-importar-a-tabela-cClassTrib-IBS-CBS-no-Configurador-de-Tributos)  
[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – Campos que armazenam as informações dos impostos IBS e CBS.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35065194117911-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Campos-que-armazenam-as-informa%C3%A7%C3%B5es-dos-impostos-IBS-e-CBS)  
[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar o calculo do IBS e CBS?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33661274329367-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-calculo-do-IBS-e-CBS)  
[Logística - Linha Protheus - TMS - RDMAKES para o CTe e MDFe](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXqoj6IhY6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBg2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzI0MzM5NDg3OTU5NzAzLUxvZyVDMyVBRHN0aWNhLUxpbmhhLVByb3RoZXVzLVRNUy1SRE1BS0VTLXBhcmEtby1DVGUtZS1NREZlBjsIVDoOc2VhcmNoX2lkSSIpNjE0MDk4MzYtMjcwZS00ZGYxLWIxODAtODNhMzlkNjQ4YjcwBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIPdG1zIHJkbWFrZQY7CFQ6EnJlc3VsdHNfY291bnRpAsUD--5bf93c52c7a0ca8b83456c9266f383553f0698c9)  
[Pacote Acumulado TMS 12.1.2310 - Para cliente com Garantia Estendida](https://suporte.totvs.com/portal/p/10098/download?e=1126588)  
[Pacote Acumulado TMS 12.1.2410](https://suporte.totvs.com/portal/p/10098/download?e=1170471)
