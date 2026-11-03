---
article_id: 35365607982487
category: RH - Banco De Horas
content_hash: c05bd300f47d96a5e5bd4760b682baa90e5c6153d30ffaca1e3b075e7563545a
fetched_at: '2026-06-28T22:44:54.242204+00:00'
product: protheus
section_id: 32405029751063
source: central-protheus
title: RH - Linha Protheus - PON - Como utilizar o Dashboard do Banco de Horas no
  Ponto Eletrônico
type: support-article
updated_at: '2025-10-22T18:05:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35365607982487-RH-Linha-Protheus-PON-Como-utilizar-o-Dashboard-do-Banco-de-Horas-no-Ponto-Eletr%C3%B4nico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35365591746711) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como utilizar o *Dashboard* do Banco de Horas no Ponto Eletrônico?  
  
**Ambiente**  
TOTVS RH - TOTVS RH ( Linha Protheus ) Ponto Eletrônico - Todas as versões  
  
**Solução**  
Para utilização do Dashboard Banco de Horas será necessário aplicar o pacote de fontes da **Expedição Contínua do RH liberado a partir da data 30/05/2025.**  
Para as releases anteriores a 12.1.2510 será necessário a inclusão da rotina **PONA500** no menu do Ponto.   
Veja na documentação procedimento de inclusão de **MENU**:[Framework - Linha Protheus - Personalização de Menus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000575567-Framework-Linha-Protheus-Personaliza%C3%A7%C3%A3o-de-Menus)  
Para a release 12.1.2510 e futuras não será necessário a inclusão da rotina no menu.  
  
Ao seguir com a inclusão do MENU da rotina para utilizar o DASHBOARD será necessário habilitar a Porta Multiprotocolo. Ao acessar a rotina do Dashboard caso a porta não esteja habilitada será exibida uma mensagem informando que será necessário habilitar a Porta Multiprotocolo.  
  
**Observação:** Para habilitar a Porta Multiprotocolo, o Application Server precisa ser a partir da versão **19.3.0.1**.  
Para mais informações de como realizar a configuração da Porta Multiprotocolo acesse o link abaixo:  
[Application Server - Porta Multiprotocolo](https://tdn.totvs.com/x/jIUoI)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35812657305495)  
  
Para habilitar a porta será necessário alterar o arquivo appserver.ini, na sessão **General**deverá ser incluída a chave **App\_Environment**e seu conteúdo deverá ser o **nome do ambiente** configurado.

Exemplo de configuração da Porta Multiprotocolo:  
![](https://tdn.totvs.com/download/attachments/941686615/image2022-8-30_14-44-42.png?version=1&modificationDate=1746733270923&api=v2&effects=drop-shadow)

Para verificar se a Porta Multiprotocolo está habilitada, ao acessar o Protheus, a tela de login deverá ser a mesma da imagem abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35812627451287)  
  
No módulo do Ponto Eletrônico (**SIGAPON**), acessar a rotina *Dashboard* (PONA500) em **Relatórios > Banco de Horas >** ***Dashboard*** **Banco de Horas(ou local que foi escolhido por vocês na inclusão do MENU)**  
  
Inicialmente deverão ser preenchidos os filtros para que o Dashboard busque as informações do Banco de Horas. Exemplo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35812657308823)

Após aplicar o filtro teremos os indicadores, destaques e gráficos.

Segue orientações do funcionamento de cada Indicador abaixo:  
  
**Indicadores:**  
**Saldo Atual:** O saldo atual irá exibir o saldo do Banco de Horas até a data de hoje.  
**Saldo de Horas:** Será exibido o **saldo total** do Banco de Horas que foram realizadas dentro do período selecionado no filtro.  
  
**Horas Positivas:** Será a quantidade de **horas positivas** do Banco de Horas que foram realizadas dentro do período selecionado no filtro.  
  
**Horas Negativas:**Será a quantidade de **horas negativas** do Banco de Horas que foram realizadas dentro do período selecionado no filtro.  
  
**Horas à Vencer:** Será a quantidade de horas que **estão para vencer** após o período selecionado no filtro inicial.  
Caso o evento do Banco de Horas esteja com a data de vencimento 15/05/2025 e a data final do período selecionado foi 01/05/2025, o evento será considerado como à vencer.  
  
**Horas Vencidas:** Será a quantidade de horas que **estão vencidas** considerando a data final do período selecionado no filtro. Caso o evento do Banco de Horas esteja com a data de vencimento 01/05/2025 e a data final do período selecionado foi 15/05/2025, o evento será considerado como vencido.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35812657310231)  
  
**Destaques:**  
Os destaques serão exibidos caso exista algum, seja maior redução ou maior aumento. Para identificação do maior aumento ou maior redução será considerado o **volume**do Banco de Horas.

Por exemplo a Filial A possui o saldo de 10 horas (positivas) no mês de fevereiro e em março ficou com o saldo de -10 horas (negativas). Com isso o volume ainda continua sendo 10 horas (independemente se é positivo ou negativo) então a Filial não teve uma redução ou um aumento.

**Maior Aumento**  
Será exibida a % do **aumento**, por exemplo a **filial A**passou de 10 horas no primeiro período para 12 horas no segundo período, com isso o **aumento**foi de 20% (2 horas). Caso existam outras filiais que também tiveram um **aumento**de 20%, será utilizado a quantidade de horas para critério de desempate.

Por exemplo a **filial B**foi de 20 horas no primeiro período para 24 horas no segundo período. A **filial B** teve também 20% (4 horas) de **aumento**, porém se compararmos a quantidade de horas que aumentaram, a **filial B** possui 2 horas a mais que a **filial A**, logo a **filial B** será o destaque de maior aumento.

**Maior Redução**  
Será exibida a % da **redução**, por exemplo a**filial A** passou de 10 horas no primeiro período para 8 horas no segundo período, com isso a **redução**foi de 20% (2 horas). Caso existam outras filiais que também tiveram uma **redução**de 20%, será utilizado a quantidade de horas para critério de desempate.

Por exemplo a **filial B** foi de 20 horas no primeiro período para 16 horas no segundo período. A **filial B** teve também 20% (4 horas) de **redução**, porém se compararmos a quantidade de horas que foram reduzidas, a **filial B** possui 2 horas a mais que a **filial A**, logo a **filial B** será o destaque de maior redução.

**Observação:**Os destaques serão utilizados apenas para os gráficos de Filiais, Departamentos, Centros de Custo e Gestores.  **Não**haverá destaques para os indicadores (Saldo Atual, Saldo de Horas, Horas Positivas, Horas Negativas, Horas à Vencer e Horas Vencidas).

**Gráficos:**  
**Saldo do Banco de Horas das filials (gráfico de linhas)**  
Neste gráfico teremos o saldo separado por **filial**e além disso estará separado por período selecionado no filtro inicial.  
  
**Saldo do Banco de Horas dos departamentos (gráfico de linhas)**  
Neste gráfico teremos o saldo separado por **departamento**e além disso estará separado por período selecionado no filtro inicial.  
  
**Saldo do Banco de Horas dos centros de custo (gráfico de linhas)**  
Neste gráfico teremos o saldo separado por **centro de custo**e além disso estará separado por período selecionado no filtro inicial.  
  
**Saldo do Banco de Horas por gestores (gráfico de pizza)**  
Neste gráfico teremos o saldo separado por **gestor**, por ser um gráfico de pizza o gestor que possuir saldo negativo será exibido como positivo. Porém no detalhamento teremos a informação de que o saldo estará negativo.  
  
**Evolução do saldo do Banco de Horas por gestores (gráfico de linhas)**  
Neste gráfico teremos o saldo separado por **gestor** e além disso estará separado por período selecionado no filtro inicial.  
  
**Observação:**  
**Divisão do período selecionado no filtro**  
Caso seja selecionado mais de um mês no filtro, por exemplo 01/04/2025 à 31/05/2025 a divisão de períodos será por mês, então o 1º período será o mês de **Abril** e o 2º período será o mês de **Maio**.  
Caso seja selecionado um mês ou menos, por exemplo 01/04/2025 à 14/04/2025 a divisão de períodos será por semana (7 dias), então o 1º será  a **1º Semana** e o 2º período será **2º semana**.  
  
**Importante:** O filtro do gestor só estará disponível caso exista a estrutura de departamentos ou postos, utilizando o parâmetro MV\_ORGCFG. Se o ambiente não possuir uma estrutura cadastrada, isso não afetará o Dashboard. O filtro do gestor será desativado e não será feito para buscar as informações dos funcionários. Serão considerado apenas os filtros de Período, Filial, Departamento e Centro de Custo.  
Veja como configurar hierarquia para utilizar o filtro de gestor, se for necessário:  
[RH - Linha Protheus - MEU RH - Como configurar a hierarquia por departamentos (MV\_ORGCFG=0)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7917580297623-RH-Linha-Protheus-MEU-RH-Como-configurar-a-hierarquia-por-departamentos-MV-ORGCFG-0)

Caso o ambiente não possua a estrutura, será exibida a mensagem abaixo no filtro e poderão utilizar o DASHBOARD normalmente, porém sem filtro de gestor.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35812627458967)  
  
**Saiba mais:**  
[Dashboard Banco de Horas](https://tdn.totvs.com/display/public/PROT/SIGAPON+-+Dashboard+Banco+de+Horas)  
[Pacote de Expedição Contínua Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download?e=1080347)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)
