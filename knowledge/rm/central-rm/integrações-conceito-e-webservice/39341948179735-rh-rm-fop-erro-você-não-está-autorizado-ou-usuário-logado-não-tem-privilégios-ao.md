---
article_id: 39341948179735
category: Integrações - Conceito e WebService
content_hash: 2d8ebb54d997510706473ffb4156908a692f80fd071323c99f7cf05db34822d7
fetched_at: '2026-06-28T22:46:44.835388+00:00'
product: rm
section_id: 1500000834721
source: central-rm
title: RH - RM - FOP - Erro "Você não está autorizado" ou "Usuário logado não tem
  privilégios" ao conectar em DataServers ou API do RM RH
type: support-article
updated_at: '2026-06-26T12:04:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39341948179735-RH-RM-FOP-Erro-Voc%C3%AA-n%C3%A3o-est%C3%A1-autorizado-ou-Usu%C3%A1rio-logado-n%C3%A3o-tem-privil%C3%A9gios-ao-conectar-em-DataServers-ou-API-do-RM-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39341948158103) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Ao tentar consumir DataServers ou APIs do RM, é apresentada uma das seguintes mensagens de erro:

* *"Você não está autorizado a utilizar esta funcionalidade do sistema"*
* *"O usuário logado não tem privilégios suficientes para efetuar essa operação"*
* "*Ocorreu um erro ao efetuar a leitura das definições da tabela: Referência de objeto não definida para uma instância de um objeto."*

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
Este erro ocorre, quando o usuário utilizado na autenticação **não possui permissões suficientes** para acessar o produto (DataServer/API) que está sendo consumido.  
  
**Solução**  
Para realizar o consumo de **DataServers** ou **APIs**, é necessário que o usuário de autenticação esteja vinculado a um[**perfil de acesso**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004058672-Framework-Linha-RM-Frame-Como-associar-um-usu%C3%A1rio-a-um-perfil) que possua as permissões de acesso no produto que será consumido.

A permissão de acesso é feita através do módulo **Serviços Globais > Segurança > Usuários**. Em **Sistema**, selecione o **produto** desejado, exemplo, **RH > Folha de pagamento.** Em sequência, edite o **usuário** e através da aba **Segurança**, vincule o acesso nas coligadas que serão consultadas e **associe em um Perfil** que contenha a permissão liberada.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39341948158871)

**Exemplo 1:** O DataServer "*FopFuncData"* pertence ao produto **Folha de Pagamento.**  
Para consumi-lo, o usuário deve estar vinculado a um perfil da Folha que possua permissão de acesso ao cadastro de Funcionários.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39341990146455)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39341948160535)

**Exemplo 2:** O DataServer "*RhuPessoaData"* pertence ao produto **Gestão de Pessoas.**  
Para consumi-lo, usuário deve estar vinculado a um perfil desse produto com permissão para o cadastro de Pessoas.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39341990148759)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39341948162455)

**Importante:**  
As permissões abaixo também devem estar **obrigatoriamente habilitadas** para o consumo via **WebService/API** devido as regras da[***LGPD:***](https://tdn.totvs.com/pages/releaseview.action?pageId=545647849)

* No perfil **Folha de Pagamento**:  "*Desconsiderar Filtro de Produto em WebService"*

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39341990150295)
* Nos perfis **Gestão de Pessoas** e **Automação de Ponto**: "*Ignorar filtro de regra de produto"*  
  *![](https://centraldeatendimento.totvs.com/hc/article_attachments/39341948165655)*

O parâmetro [**"Valida regras via WebSevice"**](https://tdn.totvs.com/display/public/LRM/DT+-+Valida+regras+via+WebSevice+-+FopFuncData) deve estar marcado deve estar habilitado em: **Folha de Pagamento > Configurações > Parametrizador > Funcionário > Restrições Cadastrais**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39341990151063)

Uma forma prática de validar as permissões corretas, é acessando o RM com o mesmo usuário utilizado na integração e executar manualmente o mesmo processo (cadastro ou consulta) diretamente no sistema.

✔️ Se funcionar no RM, também funcionará via WebService/API.  
❌ Se não funcionar, é necessário ajustar as permissões do Perfil em Acesso a Menus.

**Saiba mais:**  
[**RH - RM - FOP - Como identificar e consumir DataServer e API disponíveis nos produtos de RH?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37535317324823-RH-RM-FOP-Como-identificar-e-consumir-DataServer-e-API-dispon%C3%ADveis-nos-produtos-de-RH)
