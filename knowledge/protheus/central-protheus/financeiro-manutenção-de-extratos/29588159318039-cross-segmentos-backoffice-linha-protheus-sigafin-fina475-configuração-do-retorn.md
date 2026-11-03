---
article_id: 29588159318039
category: Financeiro - Manutenção de Extratos
content_hash: c3bb0532dfcea35684ebec9ff3babab0ec0790d9afd71d15fccd5590ac8753b0
fetched_at: '2026-06-28T22:37:31.165461+00:00'
product: protheus
section_id: 35057672519319
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA475 - Configuração
  do Retorno de Extratos Bancários Automático
type: support-article
updated_at: '2026-01-07T14:18:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29588159318039-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA475-Configura%C3%A7%C3%A3o-do-Retorno-de-Extratos-Banc%C3%A1rios-Autom%C3%A1tico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29588159292567) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Como importar o arquivo de extrato bancário de forma automática?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.33

**Solução**

Esta rotina visa automatizar a importação de extratos bancários, otimizando o processo de conciliação bancária. Utiliza arquivos de retorno bancário referentes aos extratos de uma ou mais contas correntes.

Para solucionar essa dúvida, realize os seguintes passos:  
1. Cadastrar o Job para o agendamento do schedule

No módulo Configurador (SIGACFG), acesse o seguinte caminho: **Ambiente → Cadastros → Schedule → Agendamentos → Cadastro**, e clique no botão "Incluir".

Para criar o Job, clique em **Novo** → Informe a rotina **FINA475** → Clique em **Avançar**.

Defina a periodicidade conforme a necessidade da empresa, exemplo: selecione **Diária** → informe o horário de execução → clique em **Avançar**.

Preencha os campos **Empresa**, **Filial**, **Módulo**, **Usuário** e **Descrição do Processo** → Clique em **Avançar** e, por fim, em **Concluir**.

![Gravar_2025_01_29_09_21_04_724.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/29588112362775)

2. Cadastro de parâmetro de banco (FINA130)

Atualizações → Cadastros → Parâmetros de Banco (FINA130).

Campos obrigatórios na aba **Cadastrais**:

**Banco** → **Agência** → **Conta** → **Extensão** → **Bytes Extrato** → **Tamanho Ocorrência** → **Tamanho Motivo Bancário**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29588112363927)

Na pasta do **Protheus Data**, deve existir a pasta **Extrato**, que conterá as seguintes subpastas:

* **Configuração**: contém o arquivo de configuração.
* **Falha**: armazena os arquivos de falha apresentados.
* **Processar**: contém os arquivos do banco a serem processados.
* **Processados**: armazena os arquivos que já foram processados.

Após criar as pastas, na aba **Extrato Conciliação Automática**, deverá preencher todos os campos e inserir os caminhos das pastas criadas.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/29588112365463)**

**Importante**

Na pasta do protheus data deve conter as seguintes pastas: configuração, falha, processados, processar

Toda a estrutura de diretórios que contém os arquivos de extrato, incluindo configurações e arquivos a serem processados, deve estar localizada obrigatoriamente abaixo do **RootPath** do ambiente correspondente. Somente dessa forma o Job de importação automática será capaz de localizar as pastas e realizar o processamento dos extratos.

**Exemplo:**

No arquivo **appserver.ini**, na seção do seu ambiente, deve-se definir:

`RootPath=C:\Protheus12\Protheus_data\1212210`

Portanto, a pasta destinada aos arquivos de extrato deve estar localizada em:

`C:\Protheus12\Protheus_data\1212210\Extratos`

Para mais informações:

[Cadastro de Parâmetro de Banco (FINA130)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=624116777#001-001)

Após a execução do Job, o sistema realizará a validação do arquivo de layout do banco, presente na pasta **Configuração**, e do arquivo de retorno, localizado na pasta **Processar**.

Uma vez processado com sucesso, o arquivo de retorno será transferido para a pasta **Processados**. A rotina **FINA474** será atualizada com os registros processados, e eles serão exibidos no conciliador para a conciliação automática.

![Gravar_2025_01_29_09_58_11_969.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/29588530565015)

**Saiba mais**

[FINA475 - Configuração do Retorno de Extratos Bancários Automático](https://tdn.totvs.com/pages/releaseview.action?pageId=747320567)
