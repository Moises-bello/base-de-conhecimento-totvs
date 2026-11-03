---
article_id: 360048873634
category: Faturamento - Cadastros
content_hash: 3a38a378664f01258ce0d30e9465dde1c728f0f511572ffed4f5e7e185700750
fetched_at: '2026-06-28T22:38:35.536538+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Help: IE -
  A inscrição estadual informada está inválida para esta unidade federativa'
type: support-article
updated_at: '2026-03-24T17:44:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048873634-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-IE-A-inscri%C3%A7%C3%A3o-estadual-informada-est%C3%A1-inv%C3%A1lida-para-esta-unidade-federativa
---

**Ocorrência**

Ao informar a inscrição estadual no cadastro de cliente (**MATA030 | CRMA980**), o sistema está gerando uma menagem de HELP:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074179193)

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus) - SIGAFAT - todas as versões.  
  
**Causa**

**1 - Divergência de informação**: A mensagem surge quando o sistema tenta verificar a inscrição estadual informada com o estado do cliente, se houver qualquer divergência na informação, o help é acionado. Em muitos casos, no cadastro do **Sintegra** , a inscrição estadual está iniciada por zero, e o usuário está tentando cadastrar no cadastro de cliente sem o zero, e com isso, o sistema gerará o Help, pois a informação não está correta:

***Consulta Sintegra Exemplo:***

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072975654)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072975754)

**2 - IE do Distrito Federal:** Outra situação recente e corrigida foi a numeração do **IE para o Distrito Federal** que passou a ter inicio pelo número "**8**" e o fonte SIGAVLD apenas validava até a numeração iniciada por "**7"**, neste caso, é necessário aplicar a correção do pacote de **expedição contínua do módulo de Financeiro** para corrigir o Help.

**3 - IE de Minas Gerais:** Outra situação recente foi a numeração da inscrição estadual de Minas Gerais, onde para o  o Estado de Minas Gerais há a regra de que a Inscrição Estadual tenha 13 caracteres, assim esta validação é realizada na inclusão de seu cadastro de cliente e fornecedor, para que na geração dos arquivos este conteúdo seja validado e aceito na importação no PVA. Não houve  nenhuma correção para este caso, a instrução para tratar este caso foi disponibilizada na **Documentação fiscal disponibilizada na seção Solução, Causa 3.**

**Solução**  
  
**CAUSA 1**  
1. Certifique-se do **estado** ao qual o cliente pertence e tenha em mãos o **cnpj**;  
2. Realize a consulta via site do ***Sintegra*** para confirmar a inscrição estadual do cliente;  
3. De posse das informações, realize o cadastro do cliente.

**OBS:** A consulta ***Sintegra*** pode ser realizada em:[**http://www.sintegra.gov.br/**](http://www.sintegra.gov.br/), selecione o estado que deseja consultar a inscrição estadual, selecione a opção de cnpj e digite o número.

**\*OBS:** Alguns Sintegras, como por exemplo Goiás, utilizam máscara de formatação na inserção do número da inscrição estadual, conforme o exemplo abaixo:

![](https://totvssuporte.zendesk.com/attachments/token/hCebDTzsuq8hOZDQ3jivs5eMp/?name=inline-1004887095.png)

Se inserir o número com esta formatação no cadastro do cliente, também irá gerar o Help, mesmo a inscrição estadual estando correta, neste caso, insira o número da inscrição estadual sem pontuações e o sistema não gerará o HELP.

![](https://totvssuporte.zendesk.com/attachments/token/FkqLzH8ov3LguAYYFMeQXrxaR/?name=inline355836650.png)

*Para ter uma pesquisa precisa do número da inscrição estadual e em formatações consulte o site do Sefaz.*

**CAUSA 2**

1 - Efetue o download do pacote de Expedição contínua do módulo financeiro, conforme a sua release:

* **12.1.33:** [**https://suporte.totvs.com/portal/p/10098/download?e=1039087**](https://suporte.totvs.com/portal/p/10098/download?e=1039087)
* **12.1.27:** [**https://suporte.totvs.com/portal/p/10098/download?e=954746**](https://suporte.totvs.com/portal/p/10098/download?e=954746)
* **12.1.25:** [**https://suporte.totvs.com/portal/p/10098/download?e=817562**](https://suporte.totvs.com/portal/p/10098/download?e=817562)
* **12.1.23:** [**https://suporte.totvs.com/portal/p/10098/download?e=749845**](https://suporte.totvs.com/portal/p/10098/download?e=749845)  
  Para acessar a documentação da correção acesse o link: [**https://tdn.totvs.com/x/0XfpIQ**](https://tdn.totvs.com/x/0XfpIQ)

2 - Via VSCode, aplique a correção ao seu ambiente.

3 - Reinicie o Smartclient e efetue o procedimento novamente.

**CAUSA 3**

Seguir as orientações da documentação da equipe de desenvolvimento Fiscal: [**https://tdn.totvs.com/x/r8QWKg**](https://tdn.totvs.com/x/r8QWKg)

**\*\*OBS:** para aplicação de pacote requer que o analista tenha conhecimento básico na ferramenta VSCode. Em caso de dúvida no processo, acionar o suporte relacionado ao pacote aplicado.  
Caso não saiba efetuar a aplicação, solicite a consultoria para aplicação do pacote.

**\*\*\*OBS:** Dúvidas sobre inscrição estadual acione a equipe de suporte **Escrituração Fiscal** para orientação.
