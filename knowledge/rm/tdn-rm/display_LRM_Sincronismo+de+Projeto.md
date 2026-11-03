---
content_hash: efa7fe173a57714cc82b1b9292d02ef1ffbd9e7404f6ece8ef74dbb664723134
fetched_at: '2026-06-29T00:09:35.412146+00:00'
page_id: '425459343'
product: rm
source: tdn-rm
title: Sincronismo de Projeto
type: documentation
url: https://tdn.totvs.com/display/LRM/Sincronismo+de+Projeto
version: 3
---

**Sincronismo de Projeto**

---

Segue uma dica interessante para otimizar o sincronismo de alguns cadastros do Totvs Obras e Projetos para o BackOffice Protheus.   
    
 Ao realizar qualquer ação como Incluir, Alterar ou Excluir registros dos cadastros de Projetos, Obras ou Etapas do Totvs Obras e Projetos, há uma sincronização desses cadastros para o BackOffice Protheus. A sincronização ocorre quando o usuário realiza login no Protheus. Neste momento, o sistema dispara automaticamente uma função específica que possui o objetivo de realizar a sincronização dos dados alterados no RM.   
    
    
 Pensando em otimizar este sincronismo deve-se criar um novo Menu no Protheus apontando para esta Função. Veja o passo-a-passo.

1. Entre no módulo de Configuração do Protheus (SigaCFG)
2. Acesse: Ambiente/Cadastro/ Menu
3. Selecione o(s) Módulo(s) que terá a opção de Sincronismo de Projeto e clicar no botão "ok".
4. Criando um novo Menu:
   * Adicione o Menu para o lado esquerdo da tela.
   * Crie um novo Grupo. Por exemplo: Sincronismo de Projeto.
   * Crie um novo item dentro do grupo criado. Por exemplo: Sincronismo de Projeto.
   * Selecione o novo item (Sincronismo de projeto, conforme exemplo), e clique no botão "Detalhes".
   * Informe o Programa "PMSVIEWSOL" (Função responsável por realizar o sincronismo de "Projetos/Obras/Etapas/Tarefas") e confirme o cadastro.

---

**Recursos Adicionais**

Blog - Como Fazer: Sincronismo de Projeto
