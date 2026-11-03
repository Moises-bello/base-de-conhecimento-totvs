---
content_hash: 6a13d5021206cde57bea3cfb11939117f5ee7c820018aa01a235b1567f113662
fetched_at: '2026-06-29T00:12:09.488484+00:00'
page_id: '946423263'
product: rm
source: tdn-rm
title: Webinar Maio/2025 - FAQ - Smart View RH RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=946423263
version: 34
---

**Webinar Smart View RH RM - Maio/2025**

250

## **FAQ - PERGUNTAS E RESPOSTAS**

As perguntas e respostas realizadas durante o webinar.

Configurações

**001 - Uso o Smart View no Protheus, mas meu RH utiliza o RM. É possível integrar ambos os sistemas na mesma instalação do Smart View ou preciso fazer instalações separadas?**

Atualmente, é necessário realizar uma instalação do Smart View separada para cada ERP. Isso ocorre porque o processo de autenticação é feito diretamente pelo ERP correspondente, o que inviabiliza o uso compartilhado entre sistemas diferentes.

**002 - O Smart View utiliza uma base de dados exclusiva?**

Sim, recomendamos o uso de uma base de dados exclusiva para o Smart View. Essa base é utilizada para armazenar os metadados da aplicação. No Smart View Agent, caso seja informado um usuário com permissão para criação de bases, o próprio Smart View pode criá-la automaticamente — basta informar o nome desejado. Para mais detalhes, consulte a documentação disponível no [link](https://tdn.totvs.com/pages/viewpage.action?pageId=852318694#Configura%C3%A7%C3%B5esdoSistema-ArmazenamentodeDados).

**003 - Como é feita a instalação e o uso do Smart View em ambientes hospedados na T-Cloud?**

No ambiente Cloud, basta abrir um ticket solicitando o provisionamento do Smart View. A equipe responsável realizará as configurações necessárias.

**004 - Já é compatível com multitenant?**Atualmente, ainda é necessário configurar uma instância do Smart View para cada alias do RM. No entanto, estamos trabalhando para evoluir e atender ambientes multitenant futuramente.

**005 - Qual base de dados será utilizada?**Na configuração do Smart View, é necessário apontar uma base de dados exclusiva para armazenamento dos metadados da aplicação. Ao integrar com o RM, o próprio RM fornece os dados da sua base operacional.

**006 - Posso usar o Smart View em ambiente de testes?**Sim, é possível, desde que seja realizada uma instalação dedicada para o ambiente de testes.

**007 - Tenho dois ERPs (por exemplo, RM e Protheus). Posso usar apenas um Smart View?**Não. É necessária uma instalação separada do Smart View para cada ERP, pois a autenticação é feita diretamente com cada ambiente.

**008 - Preciso criar uma base de dados nova na instalação?**Recomenda-se utilizar uma base exclusiva para o Smart View. Caso o usuário configurado no Smart View Agent tenha permissão para criar bases, o próprio sistema pode criá-la automaticamente. [Saiba mais no link](https://tdn.totvs.com/display/LRM/FAQ+-+Smart+View+RH).

**009 - Como integrar o RM ao Smart View?**Consulte a [documentação oficial do Smart View](https://tdn.totvs.com/display/LRM/FAQ+-+Smart+View+RH) e a [documentação de integração com o RM](https://tdn.totvs.com/display/LRM/FAQ+-+Smart+View+RH) para detalhes sobre configuração e integração.

Customizações

**010 - Uso Smart View com Protheus, mas meu RH utiliza RM. Posso integrar os dois?**Atualmente, é necessária uma instalação dedicada do Smart View para cada ERP, devido à autenticação específica de cada sistema.

**011 - É possível utilizar mais de um Objeto de Negócio por relatório?**Os recursos do Smart View operam com um único Objeto de Negócio por Visão de Dados. No entanto, é possível configurar **sub-relatórios** que utilizem outros Objetos de Negócio.

**012 - É possível editar ou criar novos Objetos de Negócio?**Sim, é possível criar novos Objetos de Negócio personalizados a partir de consultas SQL do RM. Objetos padrão, porém, não são editáveis.

**013 - Posso criar relatórios do zero no Smart View?**Sim, você pode criar relatórios personalizados utilizando Objetos de Negócio disponíveis ou criados por você.

**014 - A edição de relatórios é controlada por perfil de usuário?**Sim. Relatórios padrão não são editáveis, mas é possível duplicá-los e controlar permissões de visualização e edição.

**015 - Se o autor do relatório alterá-lo, os demais usuários verão as alterações?**Sim. Qualquer modificação feita por um usuário com permissão de edição será refletida para todos que acessarem o relatório.

**016 - É possível utilizar listas suspensas em parâmetros?**Sim. Para Tabela Dinâmica e Visão de Dados, consulte [esta documentação](https://tdn.totvs.com/x/546JMg).

**017 - É possível personalizar visões com gráficos ou outros elementos?**Sim. É possível duplicar visões e customizá-las. Embora não exista um componente específico para gráficos, eles podem ser utilizados no layout dos relatórios.

**018 - É possível criar relatórios apenas com SQL, como no RM Reports?**Sm. É possível criar Objetos de Negócio a partir de consultas SQL e utilizá-los nas Visões de Dados do Smart View.

**019 - É possível usar dados de duas bases diferentes em um único relatório?**Sim, utilizando sub-relatórios. Para isso, é necessário criar um Objeto de Negócio para cada base e configurar sub-relatórios que os utilizem.

**020 - É possível gerar um relatório no Smart View por Fórmula Visual, como no RM Reports?**Atualmente, não é possível gerar relatórios via Fórmula Visual.  
Essa funcionalidade está sendo sugerida para o Roadmap do produto.

**021 - É possível limitar um usuário para que ele apenas gere relatórios, sem poder alterá-los?**Sim. A partir daversão 3.8 do Smart View, foi introduzido um Menu de Gerenciamento de Permissões, que permite controlar o acesso por usuário ou perfil.

* Documentação: [Permissões no Smart View 3.8](https://tdn.totvs.com/x/64v6NQ)

**022 - É possível utilizar com relatório anexo do funcionário?**Sim, essa funcionalidade estará disponível a partir da versão 12.1.2506.  
🔗 Veja a documentação: <https://tdn.totvs.com/pages/viewpage.action?pageId=937708586>

**023 - É possível fixar uma coligada no filtro ou usar uma variável dinâmica para buscar a coligada atual?**É possível fixar uma coligada por meio da inclusão de filtros no Objeto de Negócio. Contudo, não há suporte para variáveis dinâmicas no momento.

**024 - Consigo definir os parâmetros do relatório conforme o destinatário?**Sim, é possível utilizar filtros e parâmetros adicionais, inclusive parâmetros *default* conforme o cenário de uso.

**025 - É possível criar layouts pré-definidos como nas Visões do RM?**Sim. Ao criar uma Visão de Dados no Smart View, você pode definir o layout de exibição, semelhante ao conceito existente no RM.

**026 - É possível usar o Smart View para envio de dados a uma API ou outra aplicação?**Não. O Smart View é voltado paraexibição e geração de relatórios, não sendo indicado para envio de dados para outras aplicações via API.

Licenças

**027 - O Smart View possui algum custo adicional?**Não. O Smart View não possui custo adicional. Basta solicitar o provisionamento via ticket.

**028 - Preciso adquirir alguma licença específica para utilizar o Smart View?**Não é necessário adquirir licença adicional para uso do Smart View integrado ao RM. O uso do produto já está contemplado no pacote do RM.

**029 - Para o licenciamento em ambiente de homologação (TOTVS RM para consultores), há restrições?**Não. No Smart View, não há restrições para desenvolvimento em ambientes de homologação de consultores.

**030 - Quais tipos de licença são consumidos ao usar o Smart View?**O Smart View consome as licenças dos módulos RM aos quais os Objetos de Negócio estão vinculados. Portanto, o consumo depende das áreas acessadas nos dados.

**031 - É necessário licença específica quando o Smart View se conecta diretamente ao banco de dados (sem RM)?**Sim. Nesse caso, é necessário possuir uma **licença TOTVS I** para permitir essa conexão direta.  
**Importante:** Para evitar essa necessidade, recomenda-se usar Consultas SQL no RM transformadas em Objetos de Negócio, evitando a conexão direta.

**032 - Após a instalação, o que mais é necessário para uso do Smart View?**É necessário configurar, no RM, os usuários que terão permissão para acessar o menu do Smart View.  
Consulte a documentação:

* [Documentação do Smart View - Link](https://tdn.totvs.com/display/LRM/FAQ+-+Smart+View+RH)
* [Informações sobre RM integrado ao Smart View - Link](https://tdn.totvs.com/display/LRM/FAQ+-+Smart+View+RH)
Smart View e RM

**033 - A partir de qual versão o Smart View está disponível?**O Smart View está disponível a partir da versão 12.1.2306.  
Entretanto, recomendamos o uso das versões mais recentes, que contam com melhorias e mais funcionalidades.

**034 - Se eu duplicar um relatório no Smart View, ele aparece automaticamente no RM?**Não. Após duplicar um relatório no Smart View, é necessário associá-lo ao RM manualmente, através da tela de listagem de Recursos do Smart View.

**035 - Consigo visualizar relatórios Smart View no Portal RM antigo?**Não. A visualização dos relatórios Smart View está disponível apenas no novo Portal RM.

**036 - Os relatórios do RM Reports serão migrados para o Smart View?**Ainda não há uma ferramenta automática de conversão.  
Estamos desenvolvendo uma solução para auxiliar na migração dos relatórios do RM Reports para o Smart View.

**037 - Existe previsão para descontinuação do RM Reports?**O RM Reports será mantido enquanto for necessário.  
Não há uma data definida para descontinuação, mas o Smart View é a evolução natural da ferramenta e, futuramente, a tendência é que a substituição ocorra.

**038 - O Smart View possui recursos dinâmicos como os Cubos no RM?**Sim. O Smart View possui a funcionalidade Tabela Dinâmica, que oferece uma experiência interativa semelhante aos Cubos do RM.

**039 - Como funciona o controle de permissões no Smart View?**

* O acesso aos Objetos de Negócio respeita os perfis e permissões do ERP.
* É possível também configurar permissões específicas por recurso, definindo quem pode visualizar ou editar cada relatório ou visão.

**040 - Respeita o perfil de acesso do ERP?**Sim. O acesso aos Objetos de Negócio no Smart View respeita as permissões dos perfis de usuários definidos no ERP.  
Além disso, ao adicionar um recurso padrão ou criar um novo, é possível configurar quais usuários ou perfis terão acesso ao recurso, seja como visualizadores ou editores.

**041 - Seria importante incluir, por padrão, o campo** ***Filial*** **além de** ***Coligada*** **e** ***Seção*** **nos filtros dos relatórios criados pela TOTVS. Isso é possível?**Sim, é possível incluir filtros adicionais no Objeto de Negócio, além dos parâmetros obrigatórios. Basta editar o Objeto de Negócio e incluir as condições desejadas.  
➡️ *Observação*: Até o momento,variáveis dinâmicas ainda não são suportadas.

**042 - Quando importo um relatório para a base, ele está vinculado ao mesmo Objeto de Negócio do Smart View?**Sim. O relatório importado utiliza o mesmo Objeto de Negócio para manipulação e exibição dos dados.

**043 - Ao enviar um relatório de aviso de férias por e-mail para 100 funcionários, o envio será individual?**Sim. O comportamento segue a mesma lógica dos relatórios do RM Reports: o envio é feitoindividualmente para cada destinatário.

**044 - Serão disponibilizados modelos padrão de relatórios?**Sim. A TOTVS disponibiliza modelos padrão de relatórios por meio doTOTVS Compartilhamento.

**045 - Existe algum relatório pronto de Banco de Horas para dar visão em tempo real aos gestores?**Atualmente não há um relatório pronto, mas está prevista a implementação de um Dashboard específico para Banco de Horas.

**046 - O Smart View tem limite de exibição de linhas ou informações?**Não há um limite de linhas, mas há limites de tamanho de dados processados:

* 500 MB para Tabelas e Visões de Dados
* 1 GB para Relatórios  
  Mais informações: [Documentação Smart View - Limites](https://tdn.totvs.com/x/MJWvMw)

**047 - O Smart View será integrado ao TAE?**Sim. Já está disponível a utilização dos relatórios do Smart View no TAE (TOTVS Assinatura Eletrônica), permitindo, por exemplo, a gestão de assinatura eletrônica de recibos e avisos de férias. Consulte a documentação específica no TDN - [DT - Smart View - Gerar relatórios do Smart View usando o TAE](https://tdn.totvs.com/pages/viewpage.action?pageId=853915277).

**048 - É possível enviar relatórios em massa por e-mail?**Sim. O Smart View permite oenvio em massa por e-mail. A configuração e orientações estão disponíveis no TDN - [DT - Enviar e-mails para Funcionários - Smart View](https://tdn.totvs.com/pages/viewpage.action?pageId=906833930).

**049 - É possível utilizar o Smart View com o Portal RM?**Sim. A integração com oPortal RM já está disponível, permitindo a publicação de relatórios diretamente no ambiente do portal.

**050 - Para enviar relatórios a empregados, é necessário o Meu RH?**Não necessariamente. O envio pode ser feito via e-mail ou através do TAE, ambos compatíveis com relatórios do Smart View.

**051 - As Visões de Dados do Smart View têm funcionalidades comparáveis ao Power BI ou QlikSense?**Não. O Smart View não é uma ferramenta de análise Big Data ou BI tradicional. Ele trata dados transacionais em tempo real, com foco em relatórios e visões operacionais.

**052 - O Smart View funciona como um Data Lake?**Não. O Smart Viewnão armazena dados previamente. Os dados são requisitados em tempo real a cada geração ou exibição do relatório ou visão.

**053- Ao utilizar o valor** **-1** **no parâmetro** **CODCOLIGADA** **nos objetos, o Smart View retorna dados de todas as coligadas ou somente das que o usuário tem permissão?**O Smart View respeita as permissões do RM. Ao usar -1, ele retorna apenas os dados das coligadas às quais o usuário possui permissão.

**054 -  E se o usuário não tiver permissão para acessar uma coligada específica (ex: coligada X), e essa for informada nos parâmetros?**Mesmo que a coligada seja especificada, o sistema não retornará dados de coligadas sem permissão de acesso.

**055 - Existe previsão de evolução para permitir utilizar campos da base e mais de um Objeto de Negócio?**É possível utilizar campos da base via Consultas SQL.  
No momento, não há previsão para utilização de múltiplos Objetos de Negócio em um único recurso.

**056 - O Smart View irá substituir o RM Reports, Planilha e Cubo?**Não há previsão de descontinuidade dessas ferramentas, mas elas não recebem mais evoluções. O Smart View é a plataforma em evolução.

**057 -  Os relatórios do Smart View podem ser organizados em grupos ou pastas?**Sim, é possível criar pastas para organizar os recursos. Confira: [Organização por pastas – TDN](https://tdn.totvs.com/x/i0e2J)

**058 -  Haverá app mobile do Smart View?**Não haverá aplicativo, mas a ferramenta será evoluída para ser responsiva em dispositivos móveis.

**059 -  O espelho de ponto gerado via Smart View e disparado pelo RM vai para assinatura de quem?**Atualmente, vai para o funcionário. Ainda não contempla assinatura do gestor.

**060 -   Existe algum objeto que permita gerar relatório de médias de férias?**Até o momento,não há um objeto específico para este tipo de relatório.

## **DOCUMENTAÇÕES**
