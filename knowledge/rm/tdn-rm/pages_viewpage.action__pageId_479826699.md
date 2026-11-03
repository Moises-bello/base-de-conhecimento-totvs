---
content_hash: e1ac4c3d8963aab2701467dcea54a58772f554750282f843a345b272b9e945ea
fetched_at: '2026-06-29T00:10:18.335663+00:00'
page_id: '479826699'
product: rm
source: tdn-rm
title: Utilizando a Atividade "Transformar Arquivo em Cadeia de Bytes"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=479826699
version: 17
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**

**01. VISÃO GERAL**

      A atividade "Transformar Arquivo em Cadeia de Bytes" tem por função, enviar arquivos em anexo para qualquer serviço que aceite cadeia de bytes.

**02. EXEMPLO DE UTILIZAÇÃO**

      Descrição dos campos da atividade "Transformar Arquivo em Cadeia de Bytes":

**Atividade:**

* **Nome:** Nome da atividade
* **Descrição:** Descrição da atividade
* **Habilitado:** Define se a atividade estará em uso ou não.

**Parâmetros da Atividade:**

* **Levantar exceção em caso de erro:** Caso acontece algum erro na fórmula visual, a descrição contida nessa campo será mostrada.
* **Nome do arquivo / Extensão (FileServerPath):**Campo recebe o nome de um arquivo presente no FileServerPath
* **Nome do arquivo fixo:** Campo onde o usuário seleciona o arquivo que será enviado.

**Retorno da Atividade:**

* **Cadeia de bytes do arquivo informado:** Retorno do arquivo enviado em transformado em bytes
* **Nome do arquivo informado:** Retorno do nome do arquivo enviado

    Como exemplo, vamos utilizar uma atividade para enviar um aquivo (anexo) ao FLUIG.

    Após a criação da fórmula, adicione as seguintes atividades no Fluxo de Trabalho Sequencial:

* Transformar Arquivo em Cadeia de Bytes
* Recuperar campos do Formulário do Processo
* Iniciar Solicitação Clássica

    Passo a passo para execução da fórmula:

    Nas propriedades da atividade "Transformar Arquivo em Cadeia de Bytes" adicione um arquivo que deseja que seja envido ao FLUIG como anexo (como exemplo foi adicionado o arquivo Projeto Metadados - Lado Server).

    Em seguida é necessário adicionar as atividades do FLUIG "Recuperar campos do Formulário do Processo", "Iniciar Solicitação Clássica" e realizar as configurações necessárias      para o seu correto funcionamento. ([Documentações das configurações das atividades do FLUIG](http://tdn.totvs.com/x/15W2C)).

    Clique em "Salvar e Executar" e verifique que a formula foi executa corretamente.

    Para fazer verificar se o arquivo foi enviado, acesse o ambiente do FLUIG, clique em "Processos | Listar Tarefas" e em seguida clique em "Consultar Solicitações". Ao ser         carregada a visão, procure pela ultima solicitação enviada e abra a mesma.

    Ao abrir a ultima solicitação enviada, verifique que os detalhes da solicitação são os mesmo configurados na formula e que a aba "Anexos" possui o arquivo enviado corretamente.
