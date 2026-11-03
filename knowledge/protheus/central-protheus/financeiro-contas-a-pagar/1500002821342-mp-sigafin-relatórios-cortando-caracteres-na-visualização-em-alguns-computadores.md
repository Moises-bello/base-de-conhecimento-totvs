---
article_id: 1500002821342
category: Financeiro - Contas a Pagar
content_hash: 9052558f62f70fd328398d24bfb2bbee323f99197237ef8ce7ebdbdd2f550fcb
fetched_at: '2026-06-28T22:38:09.950931+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: MP - SIGAFIN - Relatórios cortando caracteres na visualização em alguns computadores
type: support-article
updated_at: '2021-04-28T15:17:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002821342-MP-SIGAFIN-Relat%C3%B3rios-cortando-caracteres-na-visualiza%C3%A7%C3%A3o-em-alguns-computadores
---

**Dúvida**Relatórios cortando caracteres na visualização em alguns computadores  
**Ambiente**Microsiga Protheus - Financeiro - versão 12  
  
**Solução**O **Smartclient** suporta a passagem de parâmetros de linha especificados durante sua inicialização, Após a **build 7.00.131227 do dia 22/08/2016** ou mais recente, alguns parâmetros possuem alternativas numéricas, ou seja, você pode utilizar o -A ou então o -6 que se trata da mesma funcionalidade. Isto serve para evitar problemas com **charsets** que não possuem esses caracteres.

|  |  |  |
| --- | --- | --- |
| -? (-13) | Apresenta os parâmetros de linha. |  |
| -A (-6) | Identifica um parâmetro que será passado para o programa inicial. | (seleção) Esse parâmetro de linha pode ser especificado mais de uma vez.  (informação) O valor recebido pelo programa, através do parâmetro de linha, é do tipo caractere. |
| -C (-3) | Indica o nome da seção de conexão, configurada no arquivo de configuração TOTVS | SmartClient, que será utilizada para conexão ao TOTVS | Application Server. |  |
| -E (-2) | Indica o nome do environment, do TOTVS | Application Server, que será utilizada para definições gerais. |  |
| -L (-11) | Permite especificar o idioma de carga inicial do TOTVS | SmartClient.  | Valor | Idioma correspondente | | --- | --- | | 1 | Português | | 2 | Espanhol | | 3 | Inglês | |  |
| -M (-14) | Permite a execução de múltiplas instâncias do TOTVS | SmartClient na mesma máquina | (aviso) Por padrão somente uma instância do TOTVS | SmartClient pode estar em execução. |
| -P (-1) | Identifica o programa inicial que será executado. |  |
| -Q (-7) | Indica que o TOTVS | SmartClient não deve apresentar o *splash* (imagem de apresentação) e tela de identificação de parâmetros iniciais. | (aviso) Deve ser utilizado em conjunto com os parâmetros para a definição do programa inicial, seção de conexão e ambiente. |
| -T (-12) | Apresenta a versão da build do TOTVS | SmartClient. |  |
| -W (-8) | Indica a configuração two-tier. |  |
| -Y (-10) | Indica a porta de conexão do servidor. |  |
| -Z (-9) | Indica o endereço do servidor. |  |
| -AC | Habilita o módulo de acessibilidade |  |
| -opengl | Define que a utilização de componentes que utilizam a tecnologia OpenGL será via hardware e não software (disponível a partir da build 17.3.0.6) | Se o SmartClient estiver fechando inesperadamente ao utilizar algum componente que utiliza a tecnologia OpenGL (como no caso do TWebEngine que aparece logo depois da tela de login ao entrar em algum módulo, é o componente que apresenta o "Boletim TOTVS" e informações do módulo), utilize este parâmetro para corrigir o comportamento. |
| -SSL | Indica que a conexão deve ser segura (utilizando SSL).  **\*Disponível em builds 17.3.1.0 ou superior** | Para utilizar essa opção é necessário ter a conexão SSL configurada do lado do AppServer ([Configuração SSL no TOTVS | Application Server](https://tdn.totvs.com/pages/viewpage.action?pageId=6064915)) |
| -DPI | Indica se deve ou não utilizar o cálculo de DPI quando monitor for configurado com porcentagem diferente de 100%.  **\*Disponível em builds 19.3.0.0 ou superior** | Essa opção faz um cálculo levando em consideração a configuração do monitor, dependendo da situação, podem ocorrer artefatos (algumas bordas podem aparecer onde não deveriam) na pintura de alguns componentes devido a arredondamento. Para a solução completa dessa situação, estamos dependendo do fornecedor da ferramenta visual utilizada (Qt). |

**Exemplo**

|  |
| --- |
| `C:\TOTVS\bin\smartclient>SmartClient.exe -P=SIGAFAT -C=TCP -E=ENVIRONMENT` |
