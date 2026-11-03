---
content_hash: d7b49437707108d346ca7931bb34d266b331fb1ded50b5e40d8a0d9e07910e5b
fetched_at: '2026-06-29T00:05:59.737474+00:00'
page_id: '191469708'
product: rm
source: tdn-rm
title: Habilitando parâmetro para Log de execução de Action
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=191469708
version: 16
---

# **Introdução**

---

Este parâmetro possibilita que todas as actions acessadas pelo usuário sejam gravadas na base de dados. Após feita as configurações necessárias o acesso às actions do sistemas serão armazenados na base de dados.

        A ativação deste parâmetro pode acarretar perca de desempenho pelo volume de registros na tabela do banco de dados. Para isso aconselhamos um número considerável de dias onde ficará armazenado os registros como histórico de um período informado.

# **Como Funciona**

---

        Para armazenamento destes dados torna-se necessário a inclusão da Tag **"ENABLEEXECUTIONLOG"** no arquivo **"RM.exe.config"**. 

1Configuração Inicial

Localize dentro do diretório de instalação *(Exemplo de instalação padrão: "C:\totvs\CorporeRM\RM.Net")* o arquivo "**RM.exe.config"** e edite o arquivo.Em seguida, adicione a Tag: **<add key="ENABLEEXECUTIONLOG" value="true" />** como exemplo abaixo:  

xml




















]]>

 

Observação

**Após inclusão da Tag, é necessário reiniciar o Host.**

Alterar parâmetro

Reiniciado o serviço do Host, acesse novamente o sistema e vá em **"Parâmetros -> Globais | Logs".** Ao abrir a guia **"Logs"**, desmarque a opção **"Nunca apagar os logs de acesso a Action"** para informar o número de dias que será preservado o registro como histórico. Lembrando que o não uso de um valor mínimo de dias de armazenamento, pode acarretar perda de performance no sistema pelo volume de registros na base.

No exemplo abaixo iremos configurar para 60 dias(mínimo requerido pelo sistema) para que os dados sejam mantidos como histórico.

Observação

**Lembramos que o grande número de registros na tabela, pode acarretar perda de performance no sistema.**

Visualizar Histórico

Com a inclusão da Tag, pode-se fazer uma consulta no banco de dados e analisar o histórico de registros. Para isso consulte no banco de dados na tabela **"GUSRACTIONEXEC"** o controle de todas as actions acessadas, como mostra abaixo.

Para maiores informações:

****[@FRAMEWORK](http://fluig.totvs.com/portal/p/10097/subject/rframework)****

**Canais de Atendimento**

**Chamado:** Através do Portal TOTVS - [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2-2-3-9-5 (Framework) ou 2-2-3-9-4 (BI)

|  |  |
| --- | --- |
| **Produto** | Framework |
| **Versão** | 11.82.XX e 12.01.XX |
| **Processo** | Log |
| **Subprocesso** | Utilizando o Log de execução de actions |

|  |  |
| --- | --- |
| Status do Documento: | Produção |
| Data: | 06/07/2015 |
| Versão: | 11.82.XX e 12.01.XX |
| Versão Anterior: | 11.82.XX e 12.01.XX |
| Autores: |  |
