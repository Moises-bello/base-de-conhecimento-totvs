---
article_id: 14708217734039
category: Administração de Pessoal
content_hash: 2fae0bebe50f2cf73d1d465aa3a4b5454e26626e8d89fa922bb431dd767bda25
fetched_at: '2026-06-28T22:47:01.225008+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - Novo Cálculo IRRF - LEI MP 1.171
type: support-article
updated_at: '2024-10-11T19:13:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14708217734039-RH-RM-FOP-Novo-C%C3%A1lculo-IRRF-LEI-MP-1-171
---

![time.png](https://ci4.googleusercontent.com/proxy/bRXGjFcZcGZSpcivTrDwPFeLSqhJcUA6gQ7Kpeok19ld38LG3lkVd-GEaLdjLEKI7DproZ-lyORKbSGxNTNsCp9Hex3v__FpdZzFGB5VkcjsnoFbgwaDXmE9w_CqdfT3_Z2XrICL=s0-d-e1-ft#https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:15 min**

**Dúvida**Como parametrizar o sistema RM para atender a nova [**MEDIDA PROVISÓRIA Nº 1.171, DE 30 DE ABRIL DE 2023**](http://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/Mpv/mpv1171.htm)?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - **Versões e patches a partir**

* 12.1.2205.267
* 12.1.2209.222
* 12.1.2302.144
* e Superiores

**Importante**Para criar o novo campo no cadastro do funcionário, após aplicação do patch é imprescindível a execução do RM Atualizador, lembrando que para empresas NCamadas, o RM.Atualizador deverá ser executado em todas as camadas. Em caso de dúvidas, segue documentação para apoio.   
[RH - RM - FOP - RM Atualizador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5893403025687-RH-RM-FOP-RM-Atualizador)

**Após executar o RM.Atualizador, será necessário reiniciar o Host para acessar o sistema RM novamente com o novo campo criado.**  
  
**Solução**Para atender a nova MP 1.171 orientamos que siga a orientação abaixo.

Acesse: **Módulo folha de Pagamento | Administração de Pessoal | Cálculos | Tabelas de Cálculos |** Acesse a antiga tabela de IRRF e coloque o final de vigência para 30/04/2023. Conforme o exemplo abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14707843211543)

Após realizar o processo acima, orientamos que crie uma nova tabela, incluindo a mesma através do caminho: **Módulo folha de Pagamento | Administração de Pessoal | Cálculos | Tabelas de Cálculos |**

Inclua uma nova tabela com **início de vigência 01/05/2023**, com a mesma finalidade e código. Conforme o exemplo abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14707897663639)

Após salvar este cadastro, a aba Valores da Tabela ficará disponível. Acesse-a e inclua as faixas de acordo com tabela divulgada pela Previdência Social.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14707907301399)

**Importante**  
Os valores acima são ilustrativos. A empresa deverá validar a tabela e seus valores.

Será necessário também a criação de um valor fixo para contemplar o desconto simplificado. Segue orientações para realizar a criação: Acesse: **Administração de Pessoal | Cálculos | Valores fixos** e crie uma tabela conforme o exemplo abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14785213453463)

Para a nova parametrização do desconto simplificado segue documentação para que seja parametrizado no sistema. Acesse: **[Cálculo do IRRF Simplificado](https://tdn.totvs.com/pages/viewpage.action?pageId=761006653#1-3)**

Observe que na documentação enviada acima, a empresa terá acesso a tabelas de cálculo, valores fixos e cadastro de funcionários.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14840302685335)

Na mesma documentação você terá acesso a exemplos de como o sistema irá se comportar nos cálculos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14708063954455)

Com a entrada do IRRF Simplificado, o produto deve fazer o cálculo IRRF, lançado o desconto mais benéfico para o funcionário, ou seja, o de menor valor apurado.

Para isto será necessário executar a comparação do cálculo de IRRF para cada funcionário considerando o cálculo mais benéfico entre a base de cálculo com o valor de dedução simplificada e a base de cálculo com o valor das deduções legais.

**Veja mais informações** [IRRF – Ajuste na Tabela do Imposto de Renda](https://www.totvs.com/blog/fiscal-clientes/irrf-ajuste-na-tabela-do-imposto-de-renda/)

**Saiba mais  
[Orientações Consultoria de Segmentos - Cálculo Simplificado do IRRF](https://tdn.totvs.com/pages/releaseview.action?pageId=758481181#Orienta%C3%A7%C3%B5esConsultoriadeSegmentosC%C3%A1lculoSimplificadodoIRRF-1.1Dedu%C3%A7%C3%B5esLegais)**

**[Cálculo do IRRF Simplificado](https://tdn.totvs.com/pages/viewpage.action?pageId=761006653#1-3)  
[RH - RM - FOP - Informações referentes à Medida Provisória nº 1.171, de 30 de ABRIL de 2023](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14363271548951)  
[Framework - Linha RM - Frame - Como realizar o download dos instaladores da versão atualizada do RM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6168768931991-Framework-Linha-RM-Frame-Como-realizar-o-download-dos-instaladores-da-vers%C3%A3o-atualizada-do-RM)****[DT - IRRF Simplificado](https://tdn.totvs.com/display/public/LRM/DT+-+IRRF+Simplificado)****[Valores Fixos](https://tdn.totvs.com/display/public/LRM/Valores+Fixos)  
[Informações para o cálculo](https://tdn.totvs.com/pages/releaseview.action?pageId=452719181&draft=true)**
