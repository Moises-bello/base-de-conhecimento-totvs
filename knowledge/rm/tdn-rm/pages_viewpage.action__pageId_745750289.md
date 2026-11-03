---
content_hash: 6bdcdb5bb673f640794e0da230468200d8ea14fb1c75189defd5fba436d5496a
fetched_at: '2026-06-29T00:11:32.253415+00:00'
page_id: '745750289'
product: rm
source: tdn-rm
title: cópiacópiaTOTVS Educacional x EAD (2) (2)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=745750289
version: 1
---

**Configuração e Parâmetros TOTVS Educacional**

---

Dentro do RM, acesse o módulo Integração e siga os passos abaixo:  
    
 1 - Acesse: **Ferramentas | Configurar**

2 - Teste a conexão com Banco e após clique em avançar.

3 - Marcar a opção: **TOTVS Educacional x WebEnsino x AMS** e clique em avançar.

4 - Neste passo o usuário tem a opção de migrar todos os dados do TOTVS Educacional para o WEB Ensino , ao marcar o parâmetro: Migra os dados do Educacional para o WebEnsino.

Caso este parâmetro fique desmarcado, apenas novos cadastros serão migrados para o WebEnsino.   
    
 Após, acesse: **Ferramentas | Parâmetros**

1 - Selecione o processo: **50.01 - Configurações Gerais ByYou ESB**

2 - Inserir o número para tentativas de envio

3 - Em URL do WebService: Inserir o caminho do WebService do WebEnsino devidamente configurado no TOTVS Developer Studio ( WebEnsino ).

4 - Diagrama Sincrono e Assíncrono , informar os Diagramas configurados em TOTVS Developer Studio ( WebEnsino ).

5 - Execute o processo de parametrização.

Acesse: **Ferramentas | Parâmetros novamente.**   
    
 1 - Selecione o processo: **50.03 - TOTVS Educacional x WebEnsino x AMS**

**Configuração 1/3:**

* Inserir a URL do WebService AMS: IP da AMS
* Usuário Padrão: Usuário do sistema
* Inserir Coligada do sistema
* Filial: Código da Filial
* Tipo de Curso: Código do Curso
* Perfil do Aluno: Código do Perfil
* Código de Acesso: Código de Acesso
* Status - Matriculado e Trancado: Código do Status de Matrícula

**Configuração 2/3:**

* URL do WebService
* Inserir o caminho do WebService do WebEnsino devidamente configurado no TOTVS Developer Studio: WebEnsino.
* Diagrama Sincrono e Assíncrono: informar os Diagramas configurados em TOTVS Developer Studio: WebEnsino.

**Configuração 3/3:**

* Opção de marcar para importação - Todas as Disciplinas ou somente as Disciplinas a Distância.
