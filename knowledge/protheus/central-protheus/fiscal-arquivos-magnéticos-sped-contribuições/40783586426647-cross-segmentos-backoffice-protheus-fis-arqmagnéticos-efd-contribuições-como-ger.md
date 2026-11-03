---
article_id: 40783586426647
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 0a600d0ebe31f928400ca69d1ba7339e231a30df92b2ae9bbeadf77c3728802b
fetched_at: '2026-06-28T22:42:05.123884+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Como gerar os Tributos Genéricos da LC 224/2025 (NT 012/2026)
type: support-article
updated_at: '2026-06-18T20:11:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40783586426647-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Como-gerar-os-Tributos-Gen%C3%A9ricos-da-LC-224-2025-NT-012-2026
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40783635082647) Tempo aproximado para leitura: **00:20:00 min**  
  
**Ocorrência**  
Como gerar os Tributos Genéricos da **LC 224/2025 (NT 012/2026)** para os Documentos de Saída, utilizando o **Configurador de Tributos**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - A partir da versão 2310  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
**1.** É necessário que o ambiente esteja atualizado com o pacote *Backoffice* do dia 13/05/2026 ou superior  
- [**Expedição Continua - Backoffice Protheus**](https://tdn.totvs.com/pages/releaseview.action?pageId=587835160)  
  
**1.1** Acesse o **Configurador** (**SIGACFG)** em modo exclusivo e ajuste o tamanho e decimal dos campos abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40783635082903)  
  
**1.2** Pelo **Configurador** (**SIGACFG),** indo em **Base de Dados > Dicionário > Bases de Dados**, abra o Diretório a esquerda, selecione **Tabelas Genéricas.** Clique na Lupa e pesquise a tabela **DJ**, depois clique no símbolo do papel com o lápis para **Editar.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40795546023575)  
  
**1.3** Abra o diretório de Itens, vá até o final da tabela, **clique na seta para baixo do teclado** e adicione o cadastro de **Tp Operação 22,** que será utilizado na inclusão do Pedido de Venda (tópico 9.1 desta documentação)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40795546026519)

**2.**Acesse a rotina **Configurador de Tributos (FISA170).**Abra o diretório **Cadastros**, selecione **Tributo** e clique em **Incluir:**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40783586388631)  
  
**2.1** Em seguida, inclua um **Código**para o **Tributo PIS**, uma **Descrição,** selecione a **Esfera** igual a **1 - Federal** e selecione a **Espécie** igual a **4 - Taxa.**  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/40783635083287)**  
  
**2.2** Faça o processo novamente para gerar um segundo Tributo para o **COFINS**, mantendo a seleção da **Esfera** igual a **1 - Federal** e **Espécie** igual a **4 - Taxa.**  
  
**3.**Abra o diretório **Perfis**, selecione o **Perfil de Produto** e clique em **Incluir:**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40783635084439)  
  
**3.1** Em seguida, inclua um **Código**para o Perfil, uma **Descrição**e abaixo de **"Cod. Produto"** dê dois cliques, selecione a Lupa e escolha um dos **Produtos**que tenha cadastrado.   
**Observação:**Ao clicar com a seta do teclado para baixo, é possível adicionar outros produtos.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40783586390935)  
  
**4.**Selecione o **Perfil de Participante** e clique em **Incluir:**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40783635085719)  
  
**4.1** Em seguida, inclua um **Código**para o Perfil, uma **Descrição**, selecione o **Tipo**e abaixo de **"Participante"** dê dois cliques, selecione a Lupa e escolha um dos **Clientes** que tenha cadastrado.   
**Observação:**Ao clicar com a seta do teclado para baixo, é possível adicionar outros clientes.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40783586391831)  
  
**5.**Abra o diretório **Regras de Calculo Documento Fiscal, s**elecionar a **Regra de Base de Calculo** e clique em **Incluir.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40783586392855)  
  
**5.1** Em seguida, inclua um **Código**, uma **Descrição** e no campo **Valor Origem** selecionar a opção **01 - Valor da Mercadoria.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40783635088535)  
  
**Observação:** O **Valor Origem** pode ser configurado conforme a regra de negócio da empresa e também é possível criar uma fórmula escolhendo a opção **11 - Fórmula Manual** e montando ela na aba **"Detalhamento de Fórmula de Calculo"**. As **Adições e Deduções** também são relativas. Para mais detalhes entrar em contato com o módulo Protheus Fiscal.

**6.**Selecione a **Regra de Alíquota** e clique em **Incluir.**Nessa regra devem ser gerados dois registros, um para o **PIS** e outro para o **COFINS**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40783635089431)  
  
**6.1** No campo **Valor Origem** selecione a opção **04 - Alíquota Informada Manualmente**, no campo **Tp. Alíquota** selecione a opção**1 - Percentual** e no campo **Alíquota**, preencha o percentual do imposto **PIS** ou **COFINS** (0,165 para o PIS ou 0,760 para o COFINS) de acordo com a Regra que está criando.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40783635089815)  
  
  
**7.**Selecione a **Regra de Escrituração** e clique em **Incluir.**Nessa regra devem ser gerados dois registros, um para o **PIS** e outro para o **COFINS**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40783586398231)  
  
**7.1** Na primeira aba **(Definição de Regra de Escrituração)**, no campo **Incidência**selecione a opção **1 - Tributado,** tanto para o registro do **PIS** quando para o **COFINS**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40793182119959)  
  
**7.2** Na parte inferior configure pontualmente com a **Tabela CST** do determinado tributo e o **CST** **06** que será utilizado na Saída para o **PIS**e **COFINS**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40783635091863)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40783586403735)  
  
**7.3** Na segunda aba **(Dados adicionais da Escrituração)**, selecione utilizando a Lupa o **Código do Dado Adicional** **AJUPISCOF**, isso habilitará as opções no campo **Valor do Dado Adicional**, selecione a opção com ajuste de acréscimo ou dedução, dependendo do seu cenário, e clique no botão **Adiciona** para que a caixa de texto acima dele seja preenchida  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40793182121623)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40793182122135)  
  
**8.**Selecione a **Regra de Calculo** **- Documentos Fiscais** e clique em **Incluir.**Nessa regra devem ser gerados dois registros, um para o **PIS** e outro para o **COFINS**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40793182122519)  
  
**Observação:** É importante selecionar os **Tributos**corretos que foram criados (**PISLC, COFLC**), pois existem cadastros diferentes para **PIS** e **COFINS**, como por exemplo PISRET e COFRET. Incluir uma **Data Início** para utilização da regra e o ***Status***igual a**2 - Aprovada.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40793189113879)

**8.1** Nas **"Regras de Calculo"** e **"Regras de Escrituração"**, para **Base Cálculo**, **Alíquota** e **Escrituração,** selecione as criadas anteriormente. Na **Regra de Apuração** utilize uma padrão do sistema, para o regime **Não Cumulativo**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40793189114135)  
  
**8.2** Nas "Definições dos Perfis", no **Participante** e no **Produto** selecione os cadastros criados anteriormente e para a **Origem** e **Operação** selecione conforme a regra de negócio. No exemplo abaixo foram selecionados dois cadastros padrões do sistema.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40793182123415)  
  
**9.**Cadastre uma **TES**com o campo **Atual Ativo = Não, PIS/COFINS = Ambos, Cred. PIS/COF = Calcula, Sit.Trib.PIS = 06 e Sit.Trib.COF = 06.**  
O **Código Fiscal (CFOP)**, os campos de **Calcula** impostos**,** **Livros Fiscais** e **Tp Reg** serão de acordo com o seu cenário.    
  
**Observação:** Neste exemplo abaixo geramos o Calculo e o Livro Fiscal de **ICMS** pelo Cadastro de **TES**.   
Essa configuração fará a geração dos registros **C100/C170**, além dos registros dos ajustes.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40793672717335)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40793672718871)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41333873484695)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41333873485079)  
  
**10.** Inclua um **Pedido de Venda** utilizando os cadastros de **Cliente** e **Produto** vinculados nos Perfis, **Tp Operação** e **TES** cadastrados anteriormente  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40793692818199)  
  
**10.1** Ao acessar **Outras Ações > Planilha Financeira**, precisam ser apresentados quatro registros, dois referentes ao PIS e COFINS alíquota zero e dois referentes aos ajustes da LC, conforme print abaixo. Depois **Salve** para finalizar a geração do Pedido e **prepare** o Documento de Saída.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40793672724247)  
  
**11.**Acesse a rotina **FISA001**, clique em **Ajuste de PIS/COFINS e CPRB > Outras Ações > Facilitador de Lançamentos**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40795546026903)  
  
**11.1** No **passo 1** preencha os Filtros de **Datas**, **Ação**, **Tipo Movimento**, **Tipo de Ajuste** e **Filial.**  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/40795546028439)**  
  
**11.2** No **passo 2** selecione as notas que devem gerar os tributos genéricos. No **passo 3** será apresentado uma prévia do que foi selecionado anteriormente.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40795546031383)  
  
**11.3** No **passo 4**, selecione o **Código de Ajuste** igual a **11,** a **Data de Referência** será para a geração dos registros de Tributos Genéricos então precisará ser de dentro do período da geração das notas, selecione uma **Conta Contábil**, um **Código de Contribuição** e no **Ajuste de Crédito/Débito** selecione **Débito.**  
  
**Observação:** o **Código de Contribuição** terá relação com o **CST dos débitos do período.** Ou seja, para que os registros **M220/M620** de ajustes sejam gerados, **será necessário que haja uma ou mais notas que gerem débito com o CST correspondente ao Código de Contribuição selecionado.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40795516064791)  
  
**11.4** No **passo 5** é apresentado uma prévia do que foi selecionado antes. Ao **Concluir** sem erros, serão gerados os registros dos **Tributos Genéricos**  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/40795546034583)**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40795546039447)  
  
**12.** Ao **processar a apuração** o valor dos **Ajustes** serão apresentados. E ao **gerar o arquivo TXT** os registros **M220/M620** serão gerados  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/40795516068503)**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40795516068887)  
  
**Saiba mais**  
[**CFGTRIB - Cálculos no Configurador de Tributos**](https://tdn.totvs.com/pages/releaseview.action?pageId=676039354)
