---
content_hash: 7ef345b72ece1413bace1e84c873d49dcdff01ea72818673e368adbab88a9616
fetched_at: '2026-06-29T00:09:08.930567+00:00'
page_id: '390400257'
product: rm
source: tdn-rm
title: Executor de Scripts RM
type: documentation
url: https://tdn.totvs.com/display/LRM/Executor+de+Scripts+RM
version: 13
---

|  |  |  |
| --- | --- | --- |
| Produto | : | RM Executor de Scripts |
| Versão RM | : | Qualquer Versão |
| Banco de Dados | : | Qualquer Versão |
| Processo | : | Execução de Scripts em bases de Clientes |
| Sub Processo | : | FAQ |
| Data da Publicação | : | 28/03/2014 |

---

##### **Processo para executar um Script no Banco de Dados de cliente**

Este documento objetiva demonstrar como é efetuado o processo de execução de scripts dentro do ambiente TOTVS Linha RM, no cliente.

Requisitos de versão:

****Biblioteca 12.1.3 ou superior****

**Passos para Execução do Script:**

**1)** Acesse o diretório "**...\CorporeRM\RM.Net**"

**2)** Execute o programa **"RM.Script.Executor.exe"**, logando com usuário supervisor do sistema, na base de dados desejada.

**3)** Ao abrir o programa, clique no botão "Importar Script".

Nessa etapa o campo "**Necessário Backup**" virá marcada quando na solicitação do **SCRIPT** o desenvolvedor recomendar ao cliente que realize os testes em base de homologação e faça um backup de segurança.

**Obs:** A opção não poderá ser desmarcada pelo cliente.

**4)** Selecione o Script a ser executado.

**5)** Marque o Script que deverá ser executado e clique no botão "**Executar Script**".

**6)** Ao clicar em "**Executar Script**" com a opção "Necessário Backup" marcada, o sistema apresentará a mensagem:

**7)** Após confirmar a mensagem acima, a mensagem abaixo será  exibida:

Clique em "Sim" para visualizar o Log de execução.

**8)** É importante verificar o Status do Script, através da coluna "**Status**". Em caso de erros, comunique ao nosso suporte.

**Definição das colunas:**

"**Status**" exibe 4 variações; “Executado com sucesso”, “Executado com erros”, “Pendente” e “Bloqueado”. Sendo que o único status que permite que o script seja executado é o “Pendente”, demonstrando que o mesmo ainda não foi executado na base de dados.

"**Código do Script**" exibe a identificação ou marcação do script.

"**Descrição**" exibe a descrição do script, obtida a partir do arquivo de “leia-me”, citado anteriormente que acompanha o script.

"**CNPJ**" exibe o CNPJ do cliente a qual o script é destinado, ou então exibe “nulo” ou “00.000.000/0000-00” para scripts destinados a todos os clientes.

"**Data de Solicitação**"exibe a data de solicitação do script.

"**Data de Validade**" exibe a data de validade do script - A data de validade são 06 meses após a data de solicitação.

"**Data de Execução**" exibe a data na qual o script foi executado na base de dados.

"**SGBD**" informa para qual SGBD o script é destinado.

"**Observação**" exibe observações sobre o script. Exemplo: se o mesmo já foi executado na referida base.

**9)** Em caso de sucesso, feche o programa!

.
