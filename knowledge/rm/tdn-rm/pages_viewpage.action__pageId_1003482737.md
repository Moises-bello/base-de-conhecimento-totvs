---
content_hash: 4f596b0a09c65b7172f11167f1a4de13753cf0f730e8ec5873fda86902cdb340
fetched_at: '2026-06-29T00:05:45.117898+00:00'
page_id: '1003482737'
product: rm
source: tdn-rm
title: Webinar Outubro/2025 - FAQ - Smart View RH RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1003482737
version: 15
---

**Webinar Smart View RH RM - Outubro/2025**

250

## **FAQ - PERGUNTAS E RESPOSTAS**

As perguntas e respostas realizadas durante o webinar.

Perguntas e Respostas

**001 –** Quando os relatórios forem liberados, eles aparecem automaticamente ou precisamos realizar algum procedimento?  
**Resposta:** Atualmente, os relatórios liberados ficam disponíveis no TOTVS Compartilhamento.

**002** – Clientes na Cloud da TOTVS já têm o Smart View configurado e acessível?  
**Resposta:** Sim. Basta abrir um ticket solicitando o provisionamento do Smart View.

**003** – É possível realizar envio em massa de relatórios?  
**Resposta:** O envio em massa de relatórios está previsto no roadmap do Smart View.

**004** – Como ficam os relatórios executados no Portal Educacional, Meu RH e menus anexos da aplicação? É possível integrá-los aos processos como os Reports?  
**Resposta:** Já é possível utilizar alguns relatórios no Meu RH, além de realizar o envio via TAE, se desejar.

**005** – Como será o comportamento do Smart View no Meu RH?  
**Resposta:** Atualmente, o produto já permite associar relatórios Smart View nos parâmetros de portal.

**006** – Os recibos do Smart View poderão ser integrados no Portal e Meu RH para download do funcionário?  
**Resposta:** Já é possível disponibilizar relatórios Smart View no Portal e no Meu RH. No parametrizador, na etapa Férias, há a opção de selecionar relatórios Smart; o mesmo vale para o Demonstrativo de Pagamento.

**007** – É possível disponibilizar o relatório de recibo de pagamento do Smart View no app Meu RH?  
**Resposta:** Sim, o recibo de pagamento do Smart View pode ser disponibilizado no app Meu RH, configurado no parametrizador nas etapas de Férias e Demonstrativo de Pagamento.

**008** – Ao utilizar o Smart View fora do RM via Web, como as licenças são consumidas?  
**Resposta:** O SmartView consome a API do RM, e o RM é quem utiliza a licença.

**009** – É possível conectar o Smart View a bancos de dados externos e enviar parâmetros em consultas, como no TReports?  
**Resposta:** Sim, é possível conectar a bases externas, mas é necessário possuir a licença TOTVS I. Consulte a documentação na seção Conectores do Smart View.

**010** – Para a licença TOTVS I, precisamos de uma conexão distinta para cada base externa?  
**Resposta:** A licença TOTVS I é necessária apenas quando o Smart View se conecta a bases externas, sem interferir nas integrações normais do RM.

**011** – Onde podemos vincular o Smart View a outros bancos de dados além do RM?  
**Resposta:** Veja as instruções em: <https://tdn.totvs.com/x/KgnDJQ>.

**012** – É possível aumentar ou ajustar a tela de design?  
**Resposta:** Sim, é possível ajustar o layout na tela de design. Confira em: <https://tdn.totvs.com/x/Us_cM>.

**013** – É possível trazer o logo da empresa da coligada (tabela GIMAGEM) via SQL?  
**Resposta:***:* Em alguns relatórios, como o Recibo de Férias, essa opção já está disponível. Para relatórios customizados, também é possível, desde que o objeto de negócio tenha vínculo com a tabela GIMAGEM.

**014** – Posso inserir a logo da minha empresa nos relatórios do Smart View?  
**Resposta:** Sim. Você pode duplicar o relatório disponibilizado pela TOTVS, acessar o design e substituir pelo logo da sua empresa.

**015** – O que significa “Objeto de Negócio” no Smart View?  
**Resposta:** É uma coleção de dados que o RM fornece ao Smart View em formato JSON, com chaves e valores representando os campos. Pode vir de tabelas ou de consultas SQL do RM.

**016** – É possível editar os Objetos de Negócio?  
**Resposta:** Sim, é possível editar os Objetos de Negócio. Essa funcionalidade será demonstrada no evento.

  

**017** – É possível adicionar mais de um objeto de dados ao mesmo relatório?  
**Resposta:** Não. Cada relatório pode conter apenas um Objeto de Negócio.

**018** – É possível criar um Objeto de Negócio a partir de uma consulta SQL que retorne dados em JSON para representar uma tabela filha?  
**Resposta:** Não é possível. É possível criar dois Objetos de Negócio e utilizar o segundo em um sub-relatório.

**019** – Existe documentação sobre sub-relatórios utilizando dois Objetos de Negócio?  
**Resposta:** Consulte a documentação sobre sub-relatórios: <https://tdn.totvs.com/x/mbx7Jw>.

**020** – Os Objetos de Negócio agora são criados dentro de consultas SQL no RM e não mais na Smart View Web?  
**Resposta:** A criação dos Objetos de Negócio sempre ocorre dentro do RM via consultas SQL. A tela web apenas seleciona o objeto para uso no relatório.

**021** – É possível criar regras de formatação ou exibição de campos e labels?  
**Resposta:** Sim, é possível criar regras de formatação ou exibição utilizando expressões. Exemplo: <https://tdn.totvs.com/x/s4I3L>.

**022** – Como o Smart View garante a segurança e respeita restrições de acesso a dados?  
**Resposta:** Sim, o Smart View respeita todas as configurações de segurança do RM, incluindo restrições de campos e permissões de acesso.

**023** – O Smart View respeitará as regras de negócio existentes no RM, como restrições de perfis de acesso?  
**Resposta:** Sim, o Smart View respeita as regras de negócio e filtros de acesso definidos no RM.

**024** – A visão com Objetos de Negócio só está disponível na Web ou também na aplicação?  
**Resposta:** Está em nosso roadmap trazer todo o fluxo de criação e edição de recursos do Smart View para dentro do RM.

**025** – É possível executar stored procedures no Smart View?  
**Resposta:** Não, o Smart View não executa stored procedures.

**026** – É possível aplicar filtro por matrícula (chapa) em relatórios de funcionário?  
**Resposta:** Sim, basta informar a chapa desejada ou adicionar outras pelo ícone “+”.

**027** – É possível usar filtro SQL (CHAPA IN) como no RM Reports, sem digitar chapa a chapa?  
**Resposta:** Essa opção ainda não está disponível nos relatórios atuais.

**028** – Existe recibo de férias que demonstre cálculos de médias (horas extras, variáveis) no Smart View?  
**Resposta:** Ainda não há um recibo de férias com exibição das médias.

**029** – O Smart View terá agendamentos automáticos como no RM Reports?  
**Resposta:** A funcionalidade ainda não está disponível, mas está em desenvolvimento.

**030** – Podemos importar cubos para o Smart View?  
**Resposta:** Não, Cubos e Smart View são soluções distintas.

**031** – Como organizar relatórios com vários sub-relatórios no Smart View?  
**Resposta:** Atualmente, essa é a forma correta. Estamos estudando a construção de Objetos de Negócio com relação pai-filho.

**032** – O ambiente de Planilhas e Cubos será migrado ou alterado?  
**Resposta:** Não. Esses ambientes não serão migrados.

**033** – É possível importar a estrutura de relatórios do RM Reports para o Smart View?  
**Resposta:** Ainda não é possível importar diretamente. Estamos homologando um migrador de RM Reports para Smart View, apresentado na Semana RM.

**034** – Alguns relatórios não podem ser importados por versão mais recente do RM. Como proceder?  
**Resposta:** Alguns relatórios estão disponíveis apenas na última versão do release. Consulte: <https://tdn.totvs.com/display/LRM/Smart+View+-+Folha+de+Pagamento+RM>.

**035** – O Smart View substituirá os geradores internos dos produtos e haverá conversor para relatórios existentes?  
**Resposta:** A TOTVS está desenvolvendo um migrador de RM Reports para Smart View. Novos relatórios estão sendo criados preferencialmente no Smart View.

**036** – O Smart View vai trabalhar em paralelo ao RM Reports ou pretende substituir?  
**Resposta:** O Smart View é a evolução do RM Reports. Apesar de não haver previsão de descontinuação, o RM Reports não receberá novas evoluções.

**037** – Para desenvolver relatórios personalizados na Cloud, é necessário instalar o Smart View?  
**Resposta:** Correto. É necessário ter o Smart View instalado, mesmo para utilizar relatórios padrão via TOTVS Compartilhamento.

**038** – Será disponibilizada a base de conhecimento de todo o processo de instalação?  
**Resposta:** Sim, todo o material e base de conhecimento serão disponibilizados no chat.

**039** – É possível adicionar relatórios do Smart View em fórmulas visuais do RM?  
**Resposta:** Ainda não é possível, mas está previsto no roadmap.

**040** – O link com a gravação da apresentação será disponibilizado?  
**Resposta:** Ao final da apresentação, os materiais e a gravação serão disponibilizados.

**041** – Existe previsão para liberação do conversor?  
**Resposta:** O conversor está em fase de homologação, mas ainda sem previsão de liberação.

**042** – Para clientes Multi-Tenant, é possível utilizar o Smart View em um ambiente com mais de uma base RM?  
**Resposta:** No momento, é necessária uma instalação do Smart View para cada tenant. Está no roadmap 2026 o suporte a múltiplos tenants em ambientes On-Premises.

**043.** No inicio tinha a criação de objetos de negócios dentro do web, correto?  
**Resposta:** É possível criar Objetos de Negócio diretamente no Smart View (<https://tdn.totvs.com/x/Uj0jJw>), através de um Conector SQL. No entanto, essa conexão exige licença TOTVS I. Recomendamos que os Objetos de Negócio sejam criados diretamente no RM através de Consultas SQL (<https://tdn.totvs.com/x/mN8WKg>).

**044.** Como funciona o compartilhamento para os usuários?  
**Resposta:** Veja em <https://tdn.totvs.com/x/1hnHL/>

**045.** Consigo disponibilizar o acesso de algum relatório do Smart View por API, para acesso em APP externos?  
**Resposta:** Atualmente não suportamos conexões via API.

**046.** Dentro do Smart View, é possível salvar documentos em vários formatos? Por exemplo, texto, JSON, CSV?  
**Resposta:** É possível exportar relatórios em diversos formatos. Veja em <https://tdn.totvs.com/x/axfDJQ>.

**047.** Dentro do TOTVS RM, ao acessar o Smart View tem a opção de “filtros”. É possível salvar filtro como é feito nas telas do RM?

Outra dúvida: ao abrir o filtro e tentar consultar utilizando % (campos código e descrição do recurso), o filtro não retorna nada. Estou fazendo algo errado ou não é possível utilizar % no filtro?  
**Resposta:** No Smart View não existe o conceito de filtros nas interfaces de listagem como no RM. Quanto à utilização de “%” nos parâmetros, para que funcione é necessário criar um filtro no Objeto de Negócio utilizando o operador “COMO” (like).

**048.** É possível criar um relatório usando outra fonte de dados externa? Exemplo: Temos outro sistema da TOTVS chamado PIMS CS e PIMS MI.  
**Resposta:** O PIMS possui integração com o Smart View. No entanto, é necessário uma instalação exclusiva do Smart View para cada ERP. Outra opção é, dentro do RM, criar uma Consulta SQL de uma base externa e transformá-la em Objeto de Negócio.

**049.** Hoje como consigo controlar quais usuários podem acessar o Smart View e o nível de acesso dele? Nosso ambiente é todo no Cloud.  
**Resposta:** É necessário abrir um ticket em CLOUD solicitando a adição de um usuário administrador do Smart View. Em seguida, ao acessar o Smart View com esse usuário, deve-se realizar as configurações de perfis conforme detalhado em <https://tdn.totvs.com/x/64v6NQ>.

**050.** Infelizmente esse novo layout está perdendo bastante espaço… é exibido muito menos informações/linhas.  
**Resposta:** O time de UX da TOTVS está ciente e trabalhando para melhorar a usabilidade das interfaces web.

**051.** No Smart View, quando o usuário vai acessar via web, é possível organizar a lista de relatórios colocando em pastas (exemplo: Listas de Funcionários, Rateios, etc.) para organizar o visual?  
**Resposta:** O Smart View possui um menu específico de pastas. Veja em <https://tdn.totvs.com/x/i0e2J>.

**052.** Nos parâmetros da visão de dados, é possível inserir lista suspensa ou filtros por consulta SQL ou utilizando outro objeto de negócio, como os filtros da aba Relatório do Smart View?  
**Resposta:** É possível sim criar uma lista suspensa de valores de opções para um parâmetro, tanto em Visão de Dados como em Tabela Dinâmica. Veja em <https://tdn.totvs.com/x/546JMg>.

**053.** O Smart View pode ser usado em modo local ou apenas no multicamadas?  
**Resposta:** Pode ser usado em modo local.

**054.** O Smart View vai ganhar um app para Mobile? Estou usando ele como PWA nos tablets e celulares, pois pelo navegador ocupa muito espaço da tela.  
**Resposta:** O Smart View não vai possuir um app, no entanto, estamos trabalhando para que a interface web seja otimizada para dispositivos mobile.

**055.** Os relatórios criados no Smart View eu consigo gerar e extrair via webservice, igual temos hoje no RM Reports?  
**Resposta:** Sim, consegue.

**056.** Os usuários que não possuem a ferramenta (Smart View) instalada conseguirão emitir os relatórios através do TOTVS?  
**Resposta:** Será possível emitir os relatórios RM Reports. Para emitir os novos relatórios desenvolvidos para o Smart View, é necessário que ele esteja instalado.

**057.** Qual resolução mínima para uso do Smart View dentro do RM? Posso encontrar esta informação na documentação?  
**Resposta:** A resolução mínima é a recomendada na portabilidade (1024×768).

**058.** Será possível gerar um relatório e salvar, por exemplo, em JSON?  
**Resposta:** Não é possível gerar um relatório em JSON. Veja os formatos disponíveis em <https://tdn.totvs.com/x/axfDJQ>.

**059.** Tem previsão para colocar subpastas na parte de pastas dos relatórios?  
**Resposta:** Não temos previsão, mas vamos incluir essa sugestão de melhoria.

**060.** Tenho um relatório no Report que executa uma stored procedure populando metadados que serão exibidos no relatório. Não vou conseguir migrar esse relatório?  
**Resposta:** É possível transformar uma Consulta SQL com Stored Procedures em um Objeto de Negócio do Smart View, desde que a Stored Procedure não utilize parâmetros. Veja mais detalhes em <https://tdn.totvs.com/x/mN8WKg>.

**061.** Uma sugestão: há possibilidade do relatório reconhecer hiperlinks na visão de dados? Hoje tive que desenvolver uma extensão de navegador para converter as linhas que são links da consulta para hiperlinks, pois o Smart View só reconhece como texto.  
**Resposta:** Obrigado pela sugestão de melhoria.

**062.** Como funciona a geração de relatórios na visão de funcionários?  
**Resposta:** Já é permitida a utilização dos relatórios Smart View na visão de funcionários. Veja detalhes no TDN: <https://tdn.totvs.com/pages/viewpage.action?pageId=937708586>.

**063.** Qual o número de Objetos de Negócio já disponibilizados pelo RM?  
**Resposta:** Disponibilizamos os objetos de negócios na página: <https://tdn.totvs.com/display/LRM/Smart+View+-+Folha+de+Pagamento+RM>.

## **DOCUMENTAÇÕES**
