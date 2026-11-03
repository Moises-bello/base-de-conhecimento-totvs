---
content_hash: 974899990f6c2bb1f603c0615fd5b3853bb9e537bc893f067982991a8d8c8148
fetched_at: '2026-06-29T00:08:50.396234+00:00'
page_id: '334334258'
product: rm
source: tdn-rm
title: 02. Integração TOTVS Folha de pagamento x TAF (TOTVS Automação Fiscal)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=334334258
version: 2
---

Veja nas orientações abaixo quais são os passos que devem ser seguidos pelo usuário para gerar os eventos destinados ao eSocial e integrá-los com o TAF (TOTVS Automação Fiscal):

**OBS:** Vamos apresentar o passo a passo para integração partindo do principio de que o usuário já realizou todo o saneamento das informações e todas as validações dos dados para geração dos eventos do eSocial.

1. Para gerar os eventos do eSocial,  o usuário deve acessar a aba eSocial (Beta) e clicar na opção **"Gerar XML"**:

* **Tipo de Arquivos**: As informações do eSocial são prestadas por meio de grupos de eventos, através deste campo o usuário deve selecionar qual é o grupo de eventos relacionado ao arquivo que ele deseja gerar para selecionar o arquivo em seguida.
* **Selecione os arquivos a serem gerados**: De acordo com a seleção realizada nos tipos de arquivo, este campo apresenta a relação de eventos do grupo para que o usuário selecione o XML a ser gerado.
* **Filtrar apenas eventos com status**: Identifica qual é o status do evento que o usuário deseja gerar, ele pode companhar o status dos eventos através do processo de "Fila de Eventos".

2. Após gerar o arquivo em **XML**, o usuário deve integrar os arquivos através do processo **"Integrar com TAF"**:

* **Folha de pagamento:** Neste campo é necessário indicar qual é o período de apuração relacionado a geração dos eventos, o campo ficará habilitado apenas quando selecionamos os eventos periódicos.
* **Filtrar apenas eventos com status:**Identifica qual é o status do evento que o usuário deseja integrar, para integração são apresentadas apenas as opções "1-Gerado" e "5-Erro na transmissão" porque somente esses dois status já apresentam o XML gerado.
* **Selecione tipos de arquivos do eSocial a serem integrados:** Apresenta a relação dos eventos que podem ser integrados para que o usuário selecione.

3. Depois de gerar o XML e executar o processo de integração com o TAF, o usuário deve acompanhar e gerenciar o status dos eventos através do processo **"Fila de Eventos"**:

* No processo de **Fila de Eventos,** o usuário pode criar filtros por "Tipo de Eventos" para visualizar apenas os eventos de um grupo específico:

* Através das colunas de Status, Tipo da Operação e Ticket TAF, o usuário consegue monitorar todas as movimentações realizadas na geração dos arquivos e toda a integração. Outra questão importante é que este processo também disponibiliza recursos para gerar e integrar os arquivos de forma individual sem a necessidade de executar os processos em Lote.

4. Após executarmos o processo de Integrar com o TAF, devemos acessar o modulo do TAF para processarmos a integração dos eventos no TAF. **OBS:** Este processo pode ser agendado para que o usuário não tenha a necessidade de administrar a sua execução de forma manual.

* O usuário deve acessar o menu **"Integração"** e clicar em **"Processamentos":**

* Ao clicar em **"Processamentos"** é apresentada a tela abaixo, onde o usuário deve marcar apenas o checkbox **"Transferir registros da TAFST2 para o TAF"** e clicar em **"Confirmar":**

* Após executar todo o processo, o usuário pode optar por visualizar o evento importado através do **"Gerenciador de Integração":**

* O  **"Gerenciador de Integração"** também pode ser acessado através do caminho abaixo:

* No  **"Gerenciador de Integração"** é possivel acompanhar o status de todos os eventos que foram integrados ao TAF, o usuário consegue localizar os eventos através do registro do identificador **"Ticket TAF"**:

         5.    Após processar toda a integração, o usuário deve executar o processo  **"Atualizar Status Integração TAF"** para atualizar os status dos eventos conforme as validações realizadas pelo o **TAF**:

**Importante! As funcionalidades estão disponíveis no sistema a partir da versão 12.1.17.**
