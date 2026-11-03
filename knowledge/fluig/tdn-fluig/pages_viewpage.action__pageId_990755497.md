---
content_hash: 5969a3956b68d01815d11f43c612e18486d0502647cf32987f4c359af68878f4
fetched_at: '2026-06-28T21:35:31.830076+00:00'
page_id: '990755497'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Captura de erro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=990755497
version: 17
---

Consulte a documentação correta:

Esta documentação refere-se ao Editor de processo atual da plataforma. Caso esteja utilizando o Editor de processo clássico, acesse [Evento intermediário de captura de erro](https://tdn.totvs.com/pages/viewpage.action?pageId=126714787#EventosIntermedi%C3%A1rios-EventoIntermedi%C3%A1riodecapturadeerro).

3.\*ndice

# Falando de evento Captura de erro...

---

O evento de **captura de erro** é utilizado para tratar exceções que podem acontecer durante a execução de uma . Ele somente pode ser associado à atividade de serviço quando ela está configurada com execução **Automatizada**, sendo obrigatório neste caso.

Esse evento serve para indicar para qual atividade a solicitação deve ser movimentada se o número de tentativas da atividade de serviço for excedido sem que nenhuma das execuções tenha sido com sucesso.

Ele não pode receber fluxos e nem ter um fluxo de saída com retorno. Ele apenas pode existir anexado na atividade de serviço com um fluxo de saída comum para uma atividade qualquer de resolução da inconsistência.

Esse evento é utilizado quando:

* a atividade pode gerar uma exceção ou erro, como uma falha de integração, falha na regra de negócio, dados inconsistentes;

* deseja-se capturar esse erro e redirecionar o fluxo para um tratamento específico: *log*, atividade de execução manual, nova tentativa, notificação.

Importante!

Esse evento não pode ser utilizado de forma isolada dentro de um diagrama de processo. Ele apenas pode existir estando anexado a uma atividade de serviço com execução automatizada.

Por isso, ele não é exibido na paleta de componentes, somente é exibido quando uma atividade de serviço existente no diagrama do processo é configurada com a execução Automatizada. Neste momento, o evento de captura de erro é exibido automaticamente sobre a atividade de serviço.

#ebecf0

trueExemplo de uso  
Em um processo onde existe uma **integração com sistema externo**, o solicitante preenche alguns dados de um cliente e envia a solicitação adiante, que vai para uma atividade de serviço responsável por enviar os dados preenchidos para um sistema externo, com execução automática e com um *script* que faz um POST via REST.

Na atividade de serviço existe um evento de captura de erro.

Se a integração for feita com sucesso, o sucesso é registrado e a solicitação segue o fluxo normal.

Se ocorrer um erro, o fluxo do evento de erro é acionado quando a execução lançar uma exceção, via *throw* em JavaScript, por exemplo.

## Como deve ser utilizado

---

O evento de captura de erro deve ser utilizado da seguinte forma:

* Crie uma **atividade de serviço** com execução **Automática**. O evento de **captura** **de erro** aparecerá automaticamente sobre a atividade.

* Do evento de **captura de erro**, crie um fluxo para uma atividade de **tratamento de erro** – atividade de execução manual ou de notificação, por exemplo. Esse fluxo será seguido se a execução da atividade de serviço lançar uma exceção.

* No ***script*** da **atividade de serviço** precisa ter o tratamento das **exceções**, para sejam lançadas quando ocorrer alguma inconsistência na execução e sejam capturadas pelo evento de captura de erro.

* Crie o **fluxo normal** saindo da atividade de serviço, que será seguido se a execução for bem-sucedida.

Importante!

O erro precisa ser lançado por uma exceção para que seja capturado pelo evento. Ao ser lançada a exceção, o evento captura automaticamente o erro.

## Boas práticas na utilização

---

São consideradas boas práticas ao utilizar o evento de captura de erro:

* sempre tratar exceções no *script* para capturar erros e lançar mensagens significativas;

* encaminhar o fluxo de erro para uma tarefa manual ou de notificação para evitar que o processo fique parado sem saber o que aconteceu;

* adicionar *logs* no tratamento de erro para facilitar o diagnóstico.

## Configurar evento Captura de erro

---

**01.** No  do processo, clique no evento **Captura de erro**  que deseja configurar.

**02.** Defina as informações desejadas para o evento de captura de erro.

#f2f2f2#f2f2f2

**Título**  
Nome para identificar o evento que vai capturar algum erro que pode ocorrer na execução da atividade de serviço.

**03.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as configurações feitas no evento **Captura de erro**.

**04.** Na mensagem exibida, clique em **Ok, entendi**.

Fique atento!

Esta documentação é válida a partir da atualização **Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.

]]>
