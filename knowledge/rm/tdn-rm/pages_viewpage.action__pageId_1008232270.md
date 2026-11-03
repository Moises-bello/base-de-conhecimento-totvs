---
content_hash: b2d1059573e0cc6aefe33169a44dfe23d6c025d493b728772452f44f23fbf245
fetched_at: '2026-06-29T00:05:47.242746+00:00'
page_id: '1008232270'
product: rm
source: tdn-rm
title: Checklist itens de validação CR
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1008232270
version: 5
---

Esse é um checklist rápido e prático para ser usado no dia a dia.

**1. Contexto e escopo**

 O propósito da mudança está claramente descrito no PR (Pull Request)? (entenda a issue/tarefa relacionada antes de começar)

 O PR resolve apenas um problema ou funcionalidade (não é grande demais)?

 Há documentação atualizada para verificar e seguir as regras?  
   
**2. Estrutura e arquitetura**

 O código segue o padrão de arquitetura do projeto (ex: Clean Architecture, DDD, MVC, 3 camadas)?

 As dependências estão bem injetadas (Dependency Injection via IServiceCollection)?

 Não há acoplamento desnecessário entre camadas ou classes?(codigos altamente acoplados causando dificuldade de acesso e manutenção)

 Foram respeitados os princípios SOLID?

 Classes e métodos têm responsabilidade única?(se arquitetura permitir)

**3. Legibilidade e estilo**

 Nomes de classes, métodos e variáveis são claros e significativos?

 O código está bem formatado (usa dotnet format ou convenções da equipe)?

 Não há código comentado ou dead code?

 Métodos não estão excessivamente longos ou complexos?

 Resources foram aplicados para tratamento de traduções?

**4. Segurança**

 Todas as entradas de usuário são validadas antes do uso?

 Senhas, tokens ou chaves não estão expostos em código?

 Uso de parametrização em consultas SQL (SqlParameter, EF LINQ) para evitar injeção?

 O código segue boas práticas de autenticação/autorização ([Authorize], Claims, Policies)?

 Logs não incluem informações sensíveis (dados pessoais, senhas, etc.)?

Usar ferramenta de monitoramento de consumo de memória em modo debug para evitar vazamento. (**Visual Studio Diagnostic Tools** menu: *Debug > Windows > Show Diagnostic Tools*).  
   
**5. Performance e boas práticas**

 Consultas e loops são eficientes (sem N+1, sem operações desnecessárias)?

 Verificar sempre que possível, a substituição de DataSet, DataRow e DataView para classes ou recursos mais performáticos e atuais.

 Uso correto de async/await (evita .Result ou .Wait() bloqueantes)?

 Caching é aplicado quando apropriado (IMemoryCache, IDistributedCache)?

 Descartáveis (IDisposable) são liberados corretamente (using ou await using)?

 Operações de E/S e banco são assincrônicas quando possível?

**6. Testes**

 Existem testes unitários cobrindo as principais mudanças?

 Os testes passam localmente e no CI?

 Mocks e stubs estão sendo usados corretamente?

(Ferramentas úteis: xUnit, NUnit, Moq, FluentAssertions)

**7. Logs, monitoramento e tratamento de erros**

 O tratamento de exceções é adequado (try/catch apenas onde faz sentido)?

 Logs são claros e de nível apropriado (Information, Warning, Error)?

 Exceções não são silenciadas nem tratadas genericamente (catch (Exception ex) sem ação)?

**8. Build, CI/CD e dependências**

 O PR compila sem warnings?

 Dependências foram adicionadas somente se necessárias (ver \*.csproj)?

 O pipeline de CI/CD executa testes e análise estática (SonarQube, dotnet analyzers)?

 Versões de pacotes NuGet estão atualizadas e seguras?  
   
 **9. Feedback e colaboração**

 O revisor deixou comentários claros e respeitosos?

 Sugestões de melhoria estão justificadas (por quê, não só o que)?

 O autor respondeu e aplicou ajustes conforme feedback?

 O PR foi aprovado por pelo menos outro desenvolvedor?

### **Objetivos principais do code review**

* **Melhorar a qualidade do software** — reduzir bugs e dívidas técnicas.
* **Garantir padrões de código** — manter o estilo e a arquitetura coerentes.
* **Compartilhar conhecimento** — aumentar o entendimento coletivo do sistema.
* **Mentoria e aprendizado** — ajudar desenvolvedores menos experientes a crescer.
* **Aumentar a segurança** — detectar vulnerabilidades cedo.
* **Melhorar a colaboração** — promover discussões técnicas construtivas.
