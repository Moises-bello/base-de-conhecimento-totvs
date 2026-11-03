---
content_hash: b4bd9739fe04ef474438292efad6de3922562a17dc617997e5ca658a25a50ad8
fetched_at: '2026-06-29T00:05:56.320137+00:00'
page_id: '149881483'
product: rm
source: tdn-rm
title: Utilizando a atividade "Gravar Log"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=149881483
version: 40
---

# Índice:

---

* Objetivo:
* Configuração:

# Objetivo:

---

     Este documento tem como finalidade, demonstrar o uso da atividade **"Gravar Log"**.

API's (POCO)

A partir da versão 12.1.2205 é possível utilizar a atividade "Gravar Log" em fórmulas visuais programadas para API's (POCO). Vide:

# Configuração:

---

A finalidade da atividade "Gravar Log do Processo" é executar a gravação de logs, seja em arquivos ou no histórico de processos, por toda a extensão da Fórmula Visual.

Um dos exemplos mais interessantes dessa atividade é a monitoração do fluxo de trabalho, ou seja, adicionando Logs entre as atividades, o usuário consegue avaliar corretamente qual o fluxo está sendo seguido, principalmente em uma fórmula visual extensa com diversas atividades, condições e Iterações.

Passo a Passo:

Primeiramente é necessário arrastar a atividade "Gravar Log do Processo" para o "Fluxo de Trabalho Sequencial " em sua fórmula visual.

Após atividade ter sido adicionada ao fluxo de trabalho, é necessário configurar as propriedades da atividade.

No exemplo acima, as propriedades foram preenchidas da seguinte maneira:

Após preencher as propriedades, <strong>lembrando que todas elas são opcionais</strong>, salve e execute a <strong>Fórmula Visual</strong>. Verifique o resultado do processo. A <strong>Fórmula Visual</strong> deverá executar com sucesso.

Como a opção do Tipo de Log está em <strong>File</strong>, o resultado será como a imagem mostrada abaixo:

O caminho em que o Log é gerado é: /Totvs/CorporeRM/RM.Net/Processos/Logs/FV/

Observação: Como podem perceber acima, o nome do Log pode conter várias informações sobre a Fórmula Visual que foi "logada", como:

- Classe do Workflow: RMSWorkflow

- Nome do DataServer principal do Workflow: GlbUsuarioData

Entre outros...

Parâmetros da Atividade

Dados do Usuário (Opcional)

Descrição: Dados do Usuário.

Tipo: Cadeia de Caracteres (String)

Como Usar: Esse parâmetro é do tipo Cadeia de Caracteres, ou seja, deve-se utilizar um valor alfanumérico que represente dados adicionais diversos a serem utilizados na Fórmula Visual.

Valor Utilizado na Requisição: N/A

Exemplo de Utilização: (Qualquer valor, depende de várias variáveis, como: DataServer, Serviço de um WebService, etc...)

Tipo de Log (Obrigatório)

Descrição: Definição se o log será escrito em um arquivo em disco ou se será gerado um log para o processo da execução da Fórmula Visual.

Opções: File (arquivo) ou Process (processo)

Como Usar: Se a opção File estiver selecionada, a saída do log será um arquivo criado na pasta Processos\Logs\FV. Caso a opção escolihda seja Process, a saída do log poderá ser vista no log da lista de processos.

Valor Utilizado na Requisição: File

Informação (Opcional)

Descrição: Informação que será adicionada no log.

Tipo: Cadeia de Caracteres (String)

Entrada: Expressão

Como Usar: Esse parâmetro é do tipo Cadeia de Caracteres, ou seja, deve-se utilizar uma expressão que apresente os dados que serão adicionados no Log.

Valor Utilizado na Requisição: TESTE LOG DE FV

Nome do Log (Opcional)

Descrição: Nome do Arquivo de Log.

Tipo: Cadeia de Caracteres (String)

Como Usar: Esse parâmetro é do tipo Cadeia de Caracteres, ou seja, deve-se utilizar um valor alfanumérico que represente o nome do Log.

Valor Utilizado na Requisição: teste

Valor padrão: LogNameDefault
