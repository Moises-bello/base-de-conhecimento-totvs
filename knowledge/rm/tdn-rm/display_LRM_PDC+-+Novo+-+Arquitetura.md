---
content_hash: ee139a517957a8175bf9b3f78a9d4fbfc8a8633b9f79640b4be6ef1df851ec19
fetched_at: '2026-06-29T00:11:34.010391+00:00'
page_id: '766935892'
product: rm
source: tdn-rm
title: PDC - Novo - Arquitetura
type: documentation
url: https://tdn.totvs.com/display/LRM/PDC+-+Novo+-+Arquitetura
version: 2
---

**1 -** Fica definido que os folders a serem criados para organização dos fontes, seguem a mesma nomenclatura de criação dos objetos segundo a orientação de comando para criação do componente, serviço ou outro tipo de artefato do angular.  
  
Exemplo: Criar um componente, o mesmo deverá ser criado dentro da pasta components e ter ainda um folder com o nome do componente especificamente.

**2 -** Os componentes criados não deverão ter regras de negócio ou mesmo ter alguma acesso aos demais artefatos comuns para Get, Put, Push ou Delete. Os acessos ficam restritos para os serviços que serão criados para cada componente correspondentemente no folder de services com a pasta do referido componente.

Exemplo: Componente Login tem um folder login no folder de services.

**3 -** Retorno de dados para os componentes será feito através de objetos Observable do angular, que serão criados e tratados nos serviços dos componentes. Assim conseguimos fazer com que toda a estrutura trabale assincrona.  
  
Exemplo: Verificar a estrutura de Login.

**4 -** Todas os services deverão declarar no construtor a injeção do service base do portal como "PRIVATE". Para mantermos a integridade de acessos aos artefatos. Somente o service do componente deverá ser injetado no componente e como private também.

Exemplo: Verificar a estrutura de Login.

**5 -** i18n fica injetado para o service base, então para acessar os literais encontrados no i18n, deverá ser criado uma function com retorno dos literais no serviço do componente e invocado a function i18n que se encontra no caminho de referencia no serviço base.  
  
Exemplo: Verificar a estrutura de login.

**6 -** As notificações que deverão ser exibidas em tela ("PoNotificationService") deverão ser inputadas nas functions já no retorno de consumo das Apis. Em casos que se desejar modificar a mensagem que está sendo retornada para notificação fica definido que se crie uma function e a mesma seja repassada para a chamada do verbo ainda no serviço do componente.  
  
Exemplo: Verificar no Login

**7 -** As rotas de APIs ou mesmo de navegação do portal deverão ser declaradas em functions dentro do serviço de route do serviço base. Assim o serviço especifico de cada componente terá acesso a todas as rotas de APIs e componentes que poderão ser chamados.  
  
Exemplo: Verficar no login.

**8 -** Storage - FIca definido a estrutura de PoStorageService para a gravação dos dados em memória no browser ou mesmo recuperação e remoção dos mesmos. O serviço já se encontrado disponível no serviço base do portal para que seja utilizado somente nos serviços especificos.  
  
Exemplo: Verificar no login.

**9 -** Constantes - Será definido constantes para acesso em todos os pontos do serviço base.
