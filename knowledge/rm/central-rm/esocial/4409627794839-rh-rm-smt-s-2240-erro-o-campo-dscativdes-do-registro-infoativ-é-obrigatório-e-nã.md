---
article_id: 4409627794839
category: eSocial
content_hash: 27e83bd9db013106ff9ef3a40580cda47c8a94c2366a3289888c45043d5beb79
fetched_at: '2026-06-28T22:47:39.161014+00:00'
product: rm
section_id: 1500000912221
source: central-rm
title: 'RH - RM - SMT - S-2240: Erro: O campo ''dscAtivDes'' do registro ''infoAtiv''
  é obrigatório e não está preenchido'
type: support-article
updated_at: '2026-05-29T17:37:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409627794839-RH-RM-SMT-S-2240-Erro-O-campo-dscAtivDes-do-registro-infoAtiv-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16037156702359) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Como solucionar o erro na geração do XML do evento S-2240 quando ocorre a mensagem de erro: "***O campo 'dscAtivDes' do registro 'infoAtiv' é obrigatório e não está preenchido"*** **?**

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional - **Todas as versões**  
  
**Solução**  
  
Esse erro ocorre quando o sistema **não encontra a descrição das atividades do trabalhador**, que é obrigatória no evento S-2240. Portanto, o foco **não é o XML** — é garantir que **exista descrição de atividade vinculada ao colaborador**.  
  
Valide na ordem abaixo até encontrar a origem:  
  
**1. Existe Profissiografia configurada?**

Acesse o menu **Opções| Parametrizador | Profissiografia** e avalie se há algum tipo selecionado. Sem essa parametrização, a informação pode não ser carregada no XML.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39426860608151)  
  
  
**2. A descrição da atividade definida na Profissiografia está devidamente preenchida?**

* **Função:**

Acesse o menu **Cadastros | Funções - Aba Outras Informações | Descrição para o PPP:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39426828508823)

* **Quadro de lotação:**

Acesse o menu **Cadastros | Funções** e acesse a opção **Anexos | Quadro de lotação**, selecione e edite a lotação que pertence ao funcionário e valide se na aba **'Informações sobre a Função'** se há descrição preenchida:   
  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39426860611223)

* **Funções do Posto de Trabalho:**

Acesse o menu **Cadastros | Postos de Trabalho** e selecione o posto vinculado ao funcionário e acesse a opção **Anexos | Funções vinculadas ao posto de trabalho,** a descrição deverá estar preenchida na aba '**Identificação'** no **campo Descrição**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39426828511639)

* **Tarefas**

O cadastro geral das tarefas é realizada no modulo de Gestão de Pessoas, dessa forma acesse o menu **Gestão Organizacional | Tarefas** selecione e edite uma tarefa e na aba **'Identificação'** informe as atividades no campo **'Descrição'**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39426860615191)

Após informar a descrição à tarefa, é necessário vincular a tarefa por funcionário, função, lotação ou posto de trabalho através do assistente de gerenciamento de tarefas do menu **Gestão Organizacional | Administração de Tarefas.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39426860616727)

**3. Data da condição está correta?**

Valide o campo abaixo no XML:

* **dtIniCondicao ≥ data de admissão**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39426828518167)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39426828519831)

Se for menor:

* O evento será rejeitado mesmo com tudo preenchido;
* Será necessário gerar novo S-2240 com data correta.

Para **incluir um novo evento S-2240** para o colaborador acesse **Módulo Folha de Pagamento** | **eSocial** | **Outros Processos** | **Gerar Gatilhos em Lote.** A data correta deverá constar no campo **'Data de Alteração'** na execução deste processo**.** Após inclusão, **gere o XML do Funcionário e efetue o envio.**  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/39426828523927)**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39426860628375)  
  
  
**Saiba mais**  
  
Para maiores informações sobre os cadastros, acesse o documento a seguir:

* [TOTVS Segurança e Saúde Ocupacional - Cadastros](https://tdn.totvs.com/pages/releaseview.action?pageId=454826465)
