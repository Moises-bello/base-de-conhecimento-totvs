---
content_hash: 346022d31056df4fd9ccd93bbdae534c4f816a22e2fd2e2eb80f6826861d5d5a
fetched_at: '2026-06-29T00:11:53.842290+00:00'
page_id: '852319066'
product: rm
source: tdn-rm
title: Log de Integração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=852319066
version: 34
---

false

**A partir das Versões:**

* [DT - Log Integração RM - Integração Feedz](https://tdn.totvs.com/pages/viewpage.action?pageId=1012526447)

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Esta funcionalidade tem como objetivo ajudar a identificar possíveis erros nas integrações principais do nosso sistema. Os logs gerados fornecerão informações detalhadas sobre a integração, incluindo status e conteúdo.

## **02. DEMONSTRAÇÃO DA UTILIZAÇÃO**

1true1ConfiguraçãoConfiguração 

**1)** Para a execução do novo processo, é necessário rodar o script para a criação das tabelas utilizando o aplicativo RM.Atualizador.exe.

**2)** Acesse o menu Serviços Globais| Segurança | Perfis

Selecione o sistema **Folha de Pagamento**, edite o perfil desejado, vá em **Acesso a Menus** e permita o acesso **11.02.01 - Log de Integração**.

**3)** Para a utilização do log, o sistema buscará automaticamente o servidor e a porta para a execução desses serviços. Caso ocorra algum erro na abertura do processo, certifique-se de que as portas necessárias estejam permitidas no Windows.

**Servidor/Porta API**:  Servidor e porta onde o serviço de API"s RM está sendo executado. (**APiPort** do Host RM. No caso onde a ApiPort não foi discriminada nas configurações do Host, utilizar a HttpPort).   
**Servidor/Porta APP:** Servidor e porta onde o aplicativo THF está sendo executado. (Caso o servidor seja o Host RM, informar a **HttpPort**).

Para maiores informações sobre a configuração da **HttpPort** e **ApiPort**, acesse: [O que é e como configurar a HttpPort e ApiPort](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044519633-RM-Integra%C3%A7%C3%B5es-O-que-%C3%A9-e-como-configurar-a-HttpPort-e-ApiPort-).

**ATENÇÃO: Se estiver executando o RM.Host.exe, o mesmo deve ser executado com administrador.**

2Parâmetros de TelaParâmetros de Tela

Acesse o processo através do menu Configurações | Log de Integração

**DETALHAMENTO DOS CAMPOS**

**INTEGRAÇÃO:** Selecione a integração desejada.

**PROCESSO:** Selecione o processo da integração desejada.

**TIPO DE LOG:** Selecione o tipo de logconforme desejado.

Existem dois tipos de logs disponíveis:

* **Rastreio:** Nesta opção, todos os logs, tanto de sucesso quanto de erro, serão listados ou gravados. Ao selecionar "Ver histórico", os logs gravados são exibidos. O processo de gravação dos logs é iniciado ao selecionar "Ativar registros".
* **Erro:** Nesta opção, somente os logs de erro serão listados ou gravados. Os logs de erro são exibidos ao selecionar "Ver histórico" e o processo de gravação dos logs de erro é iniciado ao selecionar "Ativar log".

**VER HISTÓRICO:** Irá listar todos os log's já gravados na base.

**ATIVAR LOGS**: Inicia o processo para registrar informações por um período de tempo de dez minutos. Após a ativação, basta executar o processo desejado para que os logs sejam salvos.

**ATENÇÃO:** Se um processo específico for selecionado, o sistema salvará o log apenas desse processo (por exemplo, atualização de status, teste de conexão, etc.).

3Recursos do ProcessoRecursos do Processo

Existem alguns recursos para facilitar a análise dos logs, sendo eles:

**DETALHES:** Através desse recurso é possível ver em tela o log gravado do processo selecionado.

**EXPORTAR**: Poderá exportar os detalhes do log salvo, assim como realizar testes via Json.

* + **Json**: Fornece a collection para realizar o teste via alguma ferramenta de requisição de API.
  + **Logs**: Permite a exportação do log em formato CSV.

**EXCLUIR:** Caso deseja excluir um log basta seleciona-lo e clicar em <Excluir>.

4Exemplo de UtilizaçãoExemplo de Utilização

Aqui está um exemplo de como o Log de Integração pode ser usado, considerando que é a primeira vez que o recurso esta sendo utilizado no produto.

1) O sistema está configurado para utilizar o Middleware e, ao executar o processo de "**Teste de conexão**", apresentou o erro "Conexão falhou", conforme demonstrado abaixo:

2) Para identificar a possível causa do erro, deverá ativar o processo de **Log de Integração**através do menu Configurações | Log de Integração, confirme demonstrado abaixo:

**ATENÇÃO:** Caso mantenha a tela do processo de Log de Integração aberta, o "**Carregando ...**" desaparecerá assim que o primeiro log for encontrado. O processo de registro de informações permanecerá ativo por 10 (dez) minutos, mesmo que a tela do processo seja fechada.

3) Deverá acessar o processo "**Teste de conexão**" e executar novamente o teste para que o log seja gravado.

4) Deverá acessar novamente o processo de **Log de Integração** e configurar a tela conforme demonstrado abaixo, marcando a opção "**Ver histórico**":

Selecione o log e clique em detalhes:

Os detalhes do log será demonstrado em tela:

**PONTOS IMPORTANTES:**

* Os registros serão apresentados na tela em ordem decrescente, com base no campo "Data/Hora".
* O sistema manterá apenas 500 linhas; após esse limite, as linhas mais antigas serão removidas automaticamente para evitar a sobrecarga do banco de dados.
* No ícone é possível definir os campos que serão apresentados em tela.
* No ícone  é possível ocultar o menu para uma melhor visualização.

## **03. TABELAS UTILIZADAS**

* PLOGINTEGRACAOATIVO e PLOGINTEGRACAO.
