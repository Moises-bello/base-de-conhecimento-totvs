---
content_hash: 0b7c815dd20cf7df8c92c5aef9f49144c9afc2660f932d682131d0b025e461f7
fetched_at: '2026-06-29T00:10:30.138980+00:00'
page_id: '519202749'
product: rm
source: tdn-rm
title: Pré-Atestado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=519202749
version: 13
---

O Pré-Atestado foi criado com o intuito de  disponibilizar uma forma de funcionários enviarem atestados pelo Meu RH para que o Recursos Humanos da empresa possa validar e já criar automaticamente o Atestado enviado.

## **MDI**

---

Neste Menu é mostrado todos os Pré-Atestados cadastrados.

### Visualização

O exemplo acime é de Pré-Atestado esperando validação e Aprovação.

Nele podemos ver na região **1** se o Pré-Atestado já foi validado ou não.

Na área **2** possui o Status de Aprovação que é alterado ao executar o processo de Aprovação ou Reprovação.

Em **3** é apresentado o arquivo que foi Anexado pelo funcionário com a opção de dar Zoom na imagem para que seja possível ver melhor o conteúdo da imagem para fazer a validação.

Em **4**é possível baixar o arquivo.

Em **5**é apresentada as informações do Médico que foram colocadas pelo funcionário para a pessoa responsável pela aprovação possa fazer o cadastro do profissional de saúde ou encontrar ele no sistema caso já exista.

**Observação:**

 Em casos de arquivo com extensão PDF, só é possível realizar o download do arquivo e não é possível pré-visualizar o arquivo:

### Aprovação

O processo de aprovação de pré-atestados é utilizado para criar atestados através das informações providas pelo usuário no cadastro de solicitações de atestado no Portal RH.

Para executar o processo de aprovação acesse o cadastro de Pré-Atestados, selecione os pré-atestados pendentes de aprovação, acesse o sub-menu de processos e selecione o processo de aprovação (ou aperte a tecla F3).

A tela do processo irá passar por cada pré-atestado selecionado para que sejam preenchidas informações adicionais que não são preenchidas pelos usuários mas são necessárias para a criação de um atestado na linha RM. As regras aqui são as mesmas da criação do Atestado na linha RM. Só será possível avançar a etapa de aprovação se o campo **Validado**estiver com a opção Validado marcado.

**Observação**:

O pré-atestado correspondente ao passo pode ser acessado para verificação e edição ao clicar no link do lookup.

A execução do processo tentará criar um atestado para cada um dos pré-atestados selecionados e enviara um e-mail para o usuário que criou o atestado e/ou para o gestor dele informando da aprovação, dependendo da parametrização criada.

Uma vez criado o atestado o pré-atestado correspondente mudará de Status para Aprovado.

### Reprovação

Pelo RM é possível reprovar solicitações de pré-atestados realizadas pelo portal RH.

Para executar o processo de reprovação acesse o cadastro de Pré-Atestados, selecione os pré-atestados pendentes de aprovação, acesse o sub-menu de processos e selecione o processo de reprovação (ou aperte a tecla F4).

Será aberta uma janela para concluir a execução do processo. Nesse componente, é necessário fornecer uma justificativa para a reprovação dos pré-atestados selecionados. Após a reprovação será enviado um e-mail para o usuário que criou o atestado e/ou para o gestor dele informando da reprovação, dependendo da parametrização criada.

Apenas os pré-atestados que estejam com Status de Aprovação como “Pendente de Aprovação”. Caso contrário será exibida a seguinte mensagem:

### Mostrar Tipo de Atestado no Portal

Para exibir os tipos de atestado médico no Portal RH  basta seguir os seguintes passos:

1) Acessar o menu "Tipos de Atestados"

2) Selecionar o tipo de atestado que deve ser exibido no portal

3) Marcar a opção Mostrar no Portal

### Parametrização para envio de Email

Foi criada a opção de enviar e-mail informando da aprovação ou reprovação do Pré-Atestado para o gestor e/ou Funcionário. É possível determinar separadamente para a cada tipo de aprovação e para cada tipo de pessoa.
