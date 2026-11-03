---
content_hash: 8836e0f74487afe9a22cd14f7b03187fcaf6ec02fc379c0e931fbc1a25312979
fetched_at: '2026-06-29T00:05:52.871018+00:00'
page_id: '1061173574'
product: rm
source: tdn-rm
title: 06 - Assistente de IA TOTVS - Central de Comunicação (PGE)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1061173574
version: 23
---

# Sumário

---

**Sumário**

**IMPORTANTE:** O recurso do **Assistente de IA TOTVS na Central de Comunicação** estará disponível a partir de **19/06/2026** nas versões **12.1.2602** e **12.1.2606**.

* **Atenção:** Para a versão 12.1.2602, é obrigatória a execução do RM Atualizador.

O Assistente de IA TOTVS virá **habilitado por padrão** no RM. As permissões de acesso também serão concedidas automaticamente para todos os perfis de usuários que já possuem autorização para o envio de mensagens. Caso não deseje disponibilizar o recurso ou os acessos, será necessário desabilitá-los manualmente.

## 1. Visão Geral

---

O **Assistente de IA TOTVS** é uma ferramenta integrada à Central de Comunicação do Portal de Gestão Educacional (PGE).

Seu objetivo é otimizar a criação de mensagens, permitindo que a inteligência artificial ajude a redigir, revisar, formalizar ou recriar textos de forma ágil e profissional.

A opção **Assistente de IA TOTVS** estará disponível na Central de Comunicação mediante as seguintes condições:

1. Nos **[Parâmetros do TOTVS Gestão Educacional](https://tdn.totvs.com/pages/viewpage.action?pageId=1021200817)**, a opção 'Utilizar assistente de IA' deve estar habilitada.
2. No **Perfil do Usuário**, deve haver permissão de acesso específica para esta funcionalidade."

## 2. Acesso ao Assistente

---

Ao clicar no ícone do **Assistente de IA**, um painel lateral será exibido com as seguintes funcionalidades disponíveis:

* **Prompt:** Crie mensagens a partir de comandos personalizados.
* **Recriar Texto:** Gera uma nova versão para um texto existente.
* **Revisar Texto:** Corrige erros gramaticais e melhora a coesão.
* **Tornar Formal:** Ajusta o tom da mensagem para uma linguagem corporativa/acadêmica.
* **Elaborar Texto:** Expande ideias iniciais em um comunicado completo.

As funcionalidades mencionadas estarão visíveis somente se estiverem habilitadas nos parâmetros do **TOTVS Gestão Educacional**. Para mais informações sobre as configurações, [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=1021200817).

Segue abaixo alguns exemplos de utilização.

**Prompt:**

**Elaborar Texto (as demais opções segue esse mesmo exemplo):**

## 3. Fluxos de Funcionamento

---

### **A. Uso da Função "Prompt"**

Esta função permite que você dê instruções diretas para a IA criar ou transformar conteúdos.

**Como utilizar:**

1. Ao abrir a tela, digite no campo de texto a instrução que deseja que a IA execute.
2. Clique no botão **Gerar mensagem**.

Exemplos de uso:

* **Criar uma mensagem nova:** O usuário pode solicitar a criação de um texto do zero.

  + *Exemplo de comando:* "Crie um convite para a festa junina que irá acontecer no dia 15/06/2026."
* **Aprimorar um texto existente:** Caso o usuário já tenha iniciado uma redação na Central de Comunicação, ele pode usar o prompt para solicitar alterações específicas.

  + *Exemplo de cenário:* \* **Mensagem original:** "Prezado(a) Aluno, convidamos todos a participarem da nossa mostra cultural que irá ocorrer no dia 10/09/2026."

    - **Comando no Prompt:** "Melhore a mensagem acima estendendo o convite aos pais e professores e adicione mais entusiasmo."

### **B. Funções de Edição (Recriar, Revisar, Formalizar e Elaborar)**

Estas funções são ideais para quando você já possui um rascunho ou uma ideia central e deseja que a IA realize o refinamento do texto. O comportamento do assistente varia conforme o estado da sua mensagem:

**Fluxos de Funcionamento:**

1. **Com texto prévio:** Se você já iniciou a redação na Central de Comunicação e selecionou uma função, a IA processará o conteúdo automaticamente e exibirá o resultado final no modal.
2. **Sem texto prévio:** Caso a caixa de mensagem esteja vazia, o sistema abrirá um modal para que você insira o texto que deseja transformar. Após clicar em **"Gerar Mensagem"**, a ação será executada.

**Exemplos de cada função:**

* **Recriar Texto:** Gera uma nova variação do conteúdo, mantendo o sentido original, mas mudando a construção das frases.

  + *Exemplo:* Transformar "A reunião será às 14h no auditório" em "Informamos que o encontro no auditório está agendado para as 14 horas".
* **Revisar Texto:** Foca na correção ortográfica, gramatical e de pontuação.

  + *Exemplo:* Corrigir "Os aluno deve traser os documento" para "Os alunos devem trazer os documentos".
* **Tornar Formal:** Ajusta o vocabulário para um tom mais institucional e profissional.

  + *Exemplo:* Mudar "Oi pessoal, as notas saíram, olha lá no portal" para "Prezados, informamos que os resultados das avaliações já estão disponíveis para consulta no portal acadêmico".
* **Elaborar Texto:** Expande um tópico curto ou uma frase em um comunicado mais detalhado e completo.

  + *Exemplo:* De "Aviso: feriado dia 12" para um texto estruturado explicando a suspensão das atividades acadêmicas e administrativas devido ao feriado nacional.

**IMPORTANTE:** O processamento de imagens não é suportado no assistente de IA para nenhuma das funções seja *Prompt* ou as funções de edição (**Recriar**, **Revisar**, **Formalizar** e **Elaborar**). Caso uma imagem seja anexada, o assistente de IA notificará o usuário de que o arquivo será removido automaticamente ao executar qualquer uma dessas funcionalidades.

## 4. Gerenciamento do Resultado (Modal de IA)

---

Sempre que a IA gerar um texto, um modal de visualização será exibido com as seguintes opções:

* **Edição Direta:** Você pode alterar o texto gerado pela IA diretamente dentro da caixa de visualização antes de aplicá-lo.
* **Troca de Função:** Caso o resultado não seja o esperado, você pode clicar em outra função (ex: de "Formal" para "Recriar") no próprio modal para reprocessar o texto.
* **Limpar:** Apaga todo o conteúdo da caixa de texto do modal.
* **Cancelar:** Fecha o modal sem salvar as alterações, mantendo o texto original na Central de Comunicação.
* **Aplicar mensagem:** Fecha o modal e transfere automaticamente o texto final para o corpo da mensagem na Central de Comunicação.

### **Suporte a Enquetes na Central de Comunicação**

Quando o tipo de mensagem configurado na Central de Comunicação for [Enquete](https://tdn.totvs.com/display/public/LRM/02+-+Envio+de+mensagens#id-02Enviodemensagens-Enquete), o modal de visualização do assistente de IA exibirá um comportamento específico:

* **Exibição da Aba de Opções da Enquete:** Além do campo de texto principal para a pergunta, será exibida em tela a aba de opções da enquete.
* **Preenchimento Automático:** Assim que o Assistente de IA gerar o conteúdo, a pergunta será inserida no campo de texto principal e as alternativas de resposta serão preenchidas automaticamente, cada uma em seu próprio campo, dentro da aba de opções.
* **Consideração de Dados Prévios:** Caso o usuário já tenha inserido alguma opção inicial na tela anterior da Central de Comunicação, esses dados serão considerados pelo assistente de IA na geração e distribuição final das opções.
* **Envio dos Dados:** Ao clicar em **Aplicar mensagem**, o sistema fecha o modal e transfere automaticamente o texto final e todas as opções criadas para o corpo da mensagem na Central de Comunicação.

## 

## 

## 5. Benefícios

---

* **Padronização:** Garante que as comunicações da instituição sigam um padrão de qualidade.
* **Agilidade:** Redução do tempo gasto na redação de comunicados repetitivos.
* **Correção:** Minimização de erros ortográficos e gramaticais.
