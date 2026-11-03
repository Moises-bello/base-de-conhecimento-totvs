---
content_hash: 8d33e766cae2ae9ef809a4564cb1f71ad3f5c54b4bc2b9ca49e8124e853be17a
fetched_at: '2026-06-29T00:11:26.328147+00:00'
page_id: '716347484'
product: rm
source: tdn-rm
title: Dashboard  Ponto
type: documentation
url: https://tdn.totvs.com/display/LRM/Dashboard++Ponto
version: 78
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: |  |
| Segmento: | RH |
| Módulo: | Dashboard |
| Função: | Permitir a visualização do ponto dos funcionários |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHJORNRM-2762](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-2762)  [DRHJORNRM-2768](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-2768)  [DRHJORNRM-2763](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-2763)  [DRHJORNRM-3227](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-3227)  [DRHJORNRM-2771](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-2771)  [DRHJORNRM-2772](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-2772)  [DRHJORNRM-3639](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-3639)  [DRHJORNRM-4408](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-4408)  [DRHJORNRM-4409](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-4409) |

## **02. SITUAÇÃO/REQUISITO**

Dashboard que permita visualizar as marcações dos funcionários.

## **03. SOLUÇÃO**

Criado o Dashboard  para controlar as marcações dos funcionários.

**04. EXEMPLO DE UTILIZAÇÃO**

11Parametrização

Para ter acesso ao Dashboard e envio de email será necessário as seguintes configurações no **Rm.exe**:

1) Informar os servidores de API/APP.

Instruções: [Servidores e Portas API-APP Dashboard](https://tdn.totvs.com/pages/viewpage.action?pageId=721733078)

2) Permitir acesso ao perfil no Totvs Automação de Ponto, através do Menu **Serviços Globais**-**Segurança**-**Perfis**.

  

**Observações:**

* Os indicadores de marcações do Clock In só serão carregados no dashboard se o Clock In estiver parametrizado corretamente. Menu de configuração está disponível em **Configurações > Parametrizador > Iniciais > Integração**

* Caso apresente o erro **"Servidor não está respondendo"** será necessário reservar as portas utilizadas **conforme o item 1** da documentação: [https://centraldeatendimento.totvs.com/hc/pt-br/articles/4496031752343](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4496031752343-RH-RM-Meu-RH-Erro-ao-logar-no-APP-Meu-RH-Ops-algo-deu-errado)

2Visualização Dashboard

Acesse o menu Relatórios | Dashboard, selecione a opção "Dashboard".

Novo filtro Filial

A partir da versão XXX será liberada filtro por filiais

Ao clicar no campo "Selecione o Local", será aberta um checklist possibilitando escolher mais de uma filial. Para facilitar na seleção de uma filial em específico é possível realizar a busca de filiais digitando pela filial.

falseSeleção de Filiais

Regras de utlização do filtro de filiais:

1º - Se for selecionada **apenas** 1 filial, o Dashboard irá exibir apenas os grupos Funcionários e Marcações Clock In da filial selecionada.  
2º - Se for selecionada **todas**as filiais, o Dashboard irá exibir apenas os grupos Funcionários e Marcações Clock In totalizando os números de todas as filiais.  
3º - Se for selecionada **1 ou mais filiais**, desde que não seja todas as filiais, o Dashboard irá exibir os grupos Funcionários e Marcações ClockIn separados por filial e um totalizador com o resultado de todas as filiais selecionadas.

**Importante:**

* O campo Data de Início será padrão .O sistema irá considerar 2 dias anteriores a data de hoje, por exemplo a data atual é 11/11/2022, será demonstrada 09/11/2022.

* Sempre que desejar carregar novas informações deverá após informar Data de Início,Data de Término,selecione o local e clique em *Atualizar.*
* Será permitido altera*r a data inicio e data de término, porém, o intervalo do período não poderá ser superior a 60 dias.**Exemplo ao preencher a data Início com 01/09/2022 automaticamente o calendário do campo Data de Término será bloqueado para dias superiores á 01/11/2022.**Se o usuário informar 01/11/2022 , o campo ficará destacado em vermelho , sinalizando que não pode ser utilizada a data e será demonstrada a mensagem: " O intervalo entre a dta início e término não pode ser superior a 60 dias".*

Foi informada a data de início superior a 60 dias , o sistema irá bloquear para os dias superiores

Caso selecione Atualizar será demonstrada a mensagem :

**Observação:**

* A mensagem de erro **Arquivos inexistentes do Dashboard** é apresentada quando a pasta dashboard não existe no diretório wwwroot.

3Parametrização Envio Email

No Dashboard temos a opção de tirar uma fotografia dos indicadores e enviar por email.

Será necessário configurar o**E-mail de destinatário** do Dashboard, para isso, deverá executar o **RM.Atualizador** .

Acessar o menu **Configurações | Parametrizador**, no processo **08.01 - Iniciais**, avance até a **Etapa 5 - Integração**, na aba **Integração Carol/TSA,** no grupo **Dashboard** e informe o **E-mail do destinatário**.

Para que o email seja enviado corretamente, será necessário configurar o servidor de email como endereço do servidor, usuário ,senha e etc.

Para maiores informações veja : [Como configurar o Servidor de Envio de email LINHA RM](https://tdn.totvs.com/display/LRM/Envio+de+email+-+LINHA+RM)

4Agendamento Envio E-mail

O usuário poderá agendar o envio de emails ,através do agendamento de Jobs.

Para utilizar o recurso é necessário permitir acesso ao perfil do usuário no **Totvs Automação de Ponto**, através do Menu **Serviços Globais**-**Segurança**-**Perfis**.

Acesse o envio de email através do menu **Relatórios-Análise-Dashboard-Envio de email.**

Será demonstrada a seguinte tela onde o usuário poderá definir a configuração para o envio de e-mail   "**Selecionando no checklist"**(Todos ou apenas determinadas filiais).Será possível informar o período que será realizada a consulta das informações **Mensal**, **Quinzenal**, **Semanal** ou **Quantidade de dias**.

**Selecione o local:** O usuário poderá definir a emissão por filial .Poderá selecionar todos ou a filial desejada, selecionando uma ou mais de uma filial.

**Período consulta informações:** O usuário poderá definir o período para a emissão do Dashboard.

**Mensal:** Para a data inicial será considerado o primeiro dia do mês atual e para a data final o dia de hoje.

*Exemplo:* Hoje é dia 19/01/2023, então a data inicial será 01/01/2023 e a data final 19/01/2023.

**Quinzenal:** Para a data inicial será considerado a quinzenal atual e para a data final o dia de hoje.

*Exemplos:*

a)Caso a data de hoje seja inferior ao dia 15, será considerado a quinzena atual

Hoje é dia 13/01/2023, a data inicial será 01/01/2023 e a data final 13/01/2023.

b)Caso a data de hoje seja superior ao dia 15, será utilizada a segunda quinzena do mês.

*Exemplos:*

Hoje é dia 25/08/2022, então a data inicial será 15/08/2022 e a data final 25/08/2022.

Hoje é dia 19/01/2023, então a data inicial será 15/01/2023 e a data final 19/01/2023.

**Semanal:** Para a data inicial será considerada a segunda-feira da semana atual e para a data final o dia de hoje.

*Exemplo:*Hoje é dia 19/01/2023, a segunda-feira da semana atual é 16/01/2023, então a data inicial será 16/01/2023 e a data final 19/01/2023.

**Quantidade de dias:** Para a data inicial será considerada a quantidade de dias que será utilizada para subtrair com a data de hoje.

No campo Quantidade Dias, deverá ser informado um valor entre 1 e 60.Caso seja diferente o sistema irá demonstrar mensagem para o usuário.

*Exemplo:*

Quantidade de dias igual 5.

A Data de hoje é 13/01/2023.Será considerada data inicial 09/01/2023 e data final 13/01/2023.

**Importante:**

Ao selecionar Avançar o usuário poderá agendar o processo conforme **Hora da execução** Agora, Executar em ou Sob demanda.

Para utilizar esse recurso o ambiente deverá estar 3 camadas e o serviço iniciado.

Modelo do Dashboard enviado através do agendamento

**05. ASSUNTOS RELACIONADOS**

**[Dashboard Ponto](https://tdn.totvs.com/display/LRM/Dashboard)**
