---
content_hash: 8a778d3477f07a567240423371609595e4001ba6cdbeb631cd8567ccbbfb0d76
fetched_at: '2026-06-29T00:11:54.727111+00:00'
page_id: '856936252'
product: rm
source: tdn-rm
title: 03 - Como funciona a reserva de vagas?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=856936252
version: 63
---

# Sumário

---

Sumário

# Objetivo

---

Permitir que a vaga seja reservada logo no início da inscrição, imediatamente após informar o nome do candidato e a área ofertada e então clicar em continuar.

**Exemplo:** um pai deseja realizar a inscrição de dois irmãos. **Sem a reserva de vaga**, o pai deverá inscrever um filho de cada vez, correndo o risco de perder a vaga do segundo filho, dependendo do nível de concorrência e do tempo necessário para concluir a primeira inscrição.

**Com a reserva de vaga** isso não acontecerá, pois, a vaga será reservada imediatamente após informar o nome e a área de ofertada e em seguida clicar em continuar.

*É importante ressaltar que existe um [tempo limite predefinido](https://tdn.totvs.com/pages/viewpage.action?pageId=856934701#id-01Comohabilitarainscri%C3%A7%C3%A3oparav%C3%A1riosmembrosdamesmaFam%C3%ADlia?-Tempolimiteparafinalizarainscri%C3%A7%C3%A3o) para a conclusão da inscrição.*

Os processos seletivos que utilizam o controle de vagas respeitam a ordem de inscrição e a quantidade de vagas definidas para a área ofertada.

O tipo de controle pode ser:

* **Não permite novas inscrições:** quando a quantidade de vagas for atingida, não serão aceitas mais inscrições.
* **Permite novas inscrições, mas os candidatos ficarão como excedentes.**

Mais adiante, vamos abordar o comportamento de cada opção quando a reserva de vaga for aplicada.

# Tempo limite para finalizar a inscrição

---

Conforme descrito nos [parâmetros](https://tdn.totvs.com/pages/viewpage.action?pageId=856934701#id-01Comohabilitarainscri%C3%A7%C3%A3oparav%C3%A1riosmembrosdamesmaFam%C3%ADlia?-Tempolimiteparafinalizarainscri%C3%A7%C3%A3o), será obrigatório determinar quantos minutos o responsável pela inscrição terá para concluí-la.

Esse tempo é por candidato. Se houver dois candidatos, o tempo total será: **tempo x quantidade de candidatos**. Por exemplo, com um tempo de 10 minutos por candidato e dois candidatos, o tempo total para conclusão das inscrições será de 20 minutos.

# Como funciona a reserva de vagas?

---

No portal do TOTVS Processo Seletivo, quando o responsável pela inscrição informa os candidatos e clica em avançar, é realizada uma validação para verificar se há vaga disponível. Se houver, o sistema reserva a vaga para o(s) candidato(s) informado(s).

A vaga ficará reservada para o candidato durante o tempo  [parametrizado](https://tdn.totvs.com/pages/viewpage.action?pageId=856934701#id-01Comohabilitarainscri%C3%A7%C3%A3oparav%C3%A1riosmembrosdamesmaFam%C3%ADlia?-Tempolimiteparafinalizarainscri%C3%A7%C3%A3o) no sistema. Caso esse tempo expire, o sistema não permitirá a conclusão da inscrição, sendo necessário iniciar uma nova inscrição, que consequentemente fará uma nova reserva se ainda houver vaga disponível.

Toda validação que precisar realizar a contagem de vagas de uma área ofertada, além de contar a quantidade de inscritos, também considerará a quantidade de reservas em andamento (não expiradas).

Exemplos

**Cenário 01:**

**20** vagas para a área ofertada "2º Ano EF"

**15** candidatos inscritos

**2** reservas em andamento

**Ainda restam 3 vagas**

**Cenário 02:**

**20** vagas para a área ofertada "2º Ano EF"

**15** candidatos inscritos

**5** reservas em andamento

**Não há vagas disponíveis**

No cenário 02, poderá surgir uma nova vaga se uma das **5** reservas em andamento desistir de continuar com a inscrição ou não finalizar a inscrição dentro do tempo permitido, neste caso automaticamente a vaga é disponibilizada.

**Cenário 03:**

**20** vagas para a área ofertada "2º Ano EF"

**15** candidatos inscritos

**4** reservas em andamento

**Ainda resta 1 vaga**

Considerando o cenário 03, se um responsável tentar inscrever dois candidatos, o portal aplicará a reserva de vaga apenas para o primeiro candidato, informando quais candidatos conseguiram a vaga e quais não conseguiram. O sistema permitirá ao responsável **prosseguir ou não** com a inscrição do candidato que conseguiu a vaga.

Ao iniciar uma inscrição, será solicitado o nome do Responsável pela Inscrição e o documento. Em seguida, este responsável indicará quais candidatos irá inscrever, e ao selecionar a opção continuar o sistema irá gerar a reserva da(s) vaga(s) vinculando as vagas o documento do Responsável pela Inscrição. Portanto, não será permitida a realização de novas reservas para esse documento enquanto houver reservas em andamento.

Caso o Responsável pela Inscrição tente realizar uma nova reserva em outro acesso utilizando o mesmo documento, será exibida uma mensagem de confirmação perguntando se deseja cancelar a reserva ativa e iniciar uma nova. Se confirmado, a reserva em andamento será cancelada e uma nova reserva será iniciada, que será processada conforme a disponibilidade de vagas.

Na reserva que foi cancelada, será exibida uma mensagem informando que a sessão expirou e que a reserva foi encerrada devido ao início de uma nova reserva com o mesmo documento em outra seção. Esta mensagem será disponibilizada quando o usuário tentar mudar de etapa ou quando o tempo de preenchimento terminar.

O responsável pela inscrição poderá selecionar um dos seguintes documentos ao inserir seus dados: CPF, Registro Geral de Estrangeiro (RNE) ou passaporte. No entanto, se os campos para Registro Geral de Estrangeiro (RNE) e passaporte não estiverem configurados como visíveis ou obrigatórios para responsável no parâmetro de visibilidade/obrigatoriedade do Processo Seletivo, a reserva só poderá ser realizada com o número do CPF.

No início da inscrição, o responsável pela Inscrição informa quais candidatos serão inscritos. Nesse momento, a reserva de vagas já é realizada e o responsável segue com o processo de inscrição. A jornada da inscrição é projetada para avançar de candidato em candidato, pois os dados são individualizados. A cada término de inscrição de um candidato, esta já é efetivada. Portanto, o portal não efetiva todas as inscrições apenas no final, mas sim à medida que cada candidato é concluído.

# Controle de vaga: não permite novas inscrições

---

Quando o tipo de controle de vagas for “**Não permite novas inscrições**”, a regra mencionada no tópico anteriormente será aplicada considerando os candidatos já inscritos e as reservas em andamento. Se não houver vagas disponíveis, não será possível prosseguir com a inscrição.

# Controle de vaga: permite excedentes

---

Quando o tipo de controle de vagas permitir inscrição com excedentes, a reserva de vagas terá alguns comportamentos modificados.

Quando não possuir mais vaga para a área ofertada (excedente)

O responsável pela Inscrição será informado de que não há mais vagas disponíveis e que o candidato seguirá como excedente. Também haverá a opção de não prosseguir com a inscrição.

Internamente, o **TOTVS Processo Seletivo** aguardará a decisão pela continuação da inscrição, para gerar uma reserva da vaga para o excedente. Neste instante, apenas os candidatos que conseguiram a vaga terão ela garantida. Ao prosseguir, a vaga do excedente será reservada, garantindo assim, a sua posição na ordem de inscritos.

Caso exista algum candidato com vaga garantida neste momento, o usuário terá um tempo limite para continuar que é a quantidade de vagas garantidas vezes o tempo para cada inscrição. Caso não ocorra andamento do processo de inscrição neste período, as reservas irão expirar.

No momento em que o formulário de inscrição for exibido na tela, será reiniciado o tempo destinado à sua conclusão, conforme a quantidade de candidatos.

Mesmo como excedente, o responsável pela inscrição deve finalizar o processo dentro do tempo limite estabelecido. Esse requisito é necessário para garantir a manutenção da posição de excedente reservada no início da inscrição.

Se o responsável pela inscrição finalizar o processo fora do tempo estabelecido, o sistema emitirá um aviso informando que o tempo expirou. A inscrição será concluída, mas a posição de excedente será recalculada. Isso significa que o candidato será inscrito na última posição disponível como excedente.

O candidato pode iniciar a inscrição como excedente, no entanto, ao finalizar a inscrição, pode haver alguma vaga disponível devido a desistências ou ao tempo expirado de outras reservas com vaga garantida. Se isso ocorrer, o candidato será inscrito com direito a vaga (não mais como excedente) e será apresentado um alerta no portal.

ExemplosCenário

Vamos considerar o seguinte cenário

* 5 vagas para a área ofertada "2º Ano EF"
* 3 candidatos inscritos
* 2 Vagas disponíveis

**Momento 01:**

Segue abaixo o status das vagas da área ofertada

| **Nº** | **Nome / Status** |
| --- | --- |
| 01 | Ana Maria (inscrito) |
| 02 | João Pedro (inscrito) |
| 03 | Maria Eduarda(inscrito) |
| 04 | Vaga disponível |
| 05 | Vaga disponível |

**Momento 02:**

Um responsável solicita a reserva para dois novos candidatos (**Fernando e Lorena**)

Segue abaixo o status das vagas da área ofertada

| **Nº** | **Nome / Status** |
| --- | --- |
| 01 | Ana Maria (inscrito) |
| 02 | João Pedro (inscrito) |
| 03 | Maria Eduarda(inscrito) |
| **04** | **Reservado para Fernando** |
| **05** | **Reservado para Lorena** |

**Momento 03:**

Um outro responsável solicita a reserva para dois candidatos (**Gabriel e Gustavo**)

Segue abaixo o status das vagas da área ofertada

| **Nº** | **Nome / Status** |
| --- | --- |
| 01 | Ana Maria (inscrito) |
| 02 | João Pedro (inscrito) |
| 03 | Maria Eduarda(inscrito) |
| **04** | **Reservado para Fernando** |
| **05** | **Reservado para Lorena** |
| **06** | **Reservado como excedente para Gabriel** |
| **07** | **Reservado como excedente para Gustavo** |

Simulação 01

Vamos considerar que as inscrições das reservas estão ocorrendo em paralelo.

* As inscrições do **"Fernando"** e **"Lorena"** foram concluídas com sucesso dentro do tempo limite.
* As inscrições do **"Gabriel "** e **"Gustavo"** foram concluídas com sucesso dentro do tempo limite.

Como ficará a lista de inscritos após a simulação 01?

| **Nº** | **Nome / Status** |
| --- | --- |
| 01 | Ana Maria (inscrito) |
| 02 | João Pedro (inscrito) |
| 03 | Maria Eduarda(inscrito) |
| **04** | **Fernando (inscrito)** |
| **05** | **Lorena  (inscrito)** |
| **06** | **Gabriel (inscrito como excedente)** |
| **07** | **Gustavo (inscrito como excedente)** |

| **Nº** | **Nome / Status** |
| --- | --- |
| 01 | Ana Maria (inscrito) |
| 02 | João Pedro (inscrito) |
| 03 | Maria Eduarda(inscrito) |
| **04** | **Fernando (inscrito)** |
| **06** | **Gabriel (inscrito)** |
| **07** | **Gustavo (inscrito como excedente)** |
| **08** | **Lorena (inscrito como excedente)** |

Conclusão: os candidatos finalizaram as inscrições dentro do prazo e com isso foram mantidos na vaga reservada no inicio da inscrição.

Simulação 02

Vamos considerar que as inscrições das reservas estão ocorrendo em paralelo.

* A inscrição da reserva do **"Fernando"** foi concluída com sucesso.
* A inscrição da **"Lorena"** foi finalizada fora do tempo limite (tempo expirou).
* As inscrições do **"Gabriel"** e do **"Gustavo"** foram concluídas dentro do tempo limite (lembrando que eles iniciaram a reserva como excedentes).

Como ficará a lista de inscritos após a simulação 02?

| **Nº** | **Nome / Status** |
| --- | --- |
| 01 | Ana Maria (inscrito) |
| 02 | João Pedro (inscrito) |
| 03 | Maria Eduarda(inscrito) |
| **04** | **Fernando (inscrito)** |
| **06** | **Gabriel (inscrito)** |
| **07** | **Gustavo (inscrito como excedente)** |
| **08** | **Lorena (inscrito como excedente)** |

Conclusão: **"Gabriel"** ganhou a vaga, pois a **"Lorena"** não concluiu a inscrição dentro do prazo, e consequentemente ela foi para o final da fila

Quando possuir vaga, mas o tempo para finalizar a inscrição expirou

* Ao iniciar a inscrição, se houver vaga disponível, o sistema reserva a vaga e o responsável pela inscrição deve concluir a inscrição dentro do tempo limite. Caso o tempo limite expire, o candidato será informado de que a inscrição está sendo enviada com o tempo expirado; no entanto, a vaga não poderá ser garantida.

Ao processar a inscrição, se ainda houver vaga disponível, a inscrição será efetivada com direito a vaga, caso contrário, o candidato será inscrito como excedente e um alerta será apresentado ao usuário.

Quando o processo seletivo permitir inscrição para excedentes, o número da inscrição será gerado no momento da reserva da vaga, independentemente de o candidato ser excedente ou não. Esse comportamento é necessário para respeitar a ordem de inscrição dos excedentes em caso de desistências ou aumento do número de vagas.

Portanto, é importante ressaltar que podem haver lacunas nos números de inscrição na lista de inscritos. Isso pode acontecer quando um candidato faz a reserva, mas não conclui a inscrição.

# Processos impactados

---

Alguns processos/procedimentos revalidam indiretamente a lista de inscritos, revisando as inscrições dos excedentes em função do surgimento de novas vagas. Caso surja alguma nova vaga, o excedente será automaticamente alterado para inscrito.

O que muda nessas revalidações é que a contagem de vagas disponíveis deve levar em consideração as reservas que estão em andamento (não expiradas).

Segue abaixo a lista dos processos/procedimentos que revalidam as inscrições dos excedentes:

* **Processo “Alterar candidatos excedentes para inscritos”**  
  Esse processo permite modificar o status para “não compareceu à chamada”. Nesse caso, podemos ter vagas disponibilizadas e, com isso, a lista de excedentes será atualizada.
* **Processo “Cancelar inscrições”**  
  Quando a inscrição é cancelada, uma nova vaga é disponibilizada e, com isso, a lista de excedentes será atualizada.
* **Processo “Registrar comparecimento em chamadas”**  
   O processo permite alterar o status para “não compareceu à chamada” e com isso podemos ter vagas disponibilizadas e a lista de excedentes será atualizada.
* **Processo “Desmatricular aluno no Educacional”**  
  Quando a matrícula do aluno é desfeita, o candidato volta ao status de “não compareceu à chamada”. Nesse caso, uma vaga é disponibilizada e, com isso, a lista de excedentes será atualizada.
* **Procedimento “Ao modificar a quantidade de vagas do cadastro da Área de Interesse ofertada”**  
  Ao aumentar a quantidade de vagas, a lista de excedentes será atualizada conforme a nova quantidade de vagas.

# Consulta de reserva de vagas

---

Para consultar as informações referentes às reservas de vagas realizadas pelo sistema, utilize a tabela `SPSINSCRICAORESERVA`. Essa tabela contém dados importantes, como nome do candidato, data de expiração, status da reserva, número da inscrição, entre outros, conforme descrito na tabela a seguir:

| Campo | Descrição |
| --- | --- |
| `CODCOLIGADA` | Identificador da coligada (empresa/unidade) |
| `IDPS` | Identificador do processo seletivo |
| `IDAREAINTERESSE` | Identificador da área de interesse |
| `GUID` | Identificador único da reserva |
| `DATAEXPIRA` | Data de expiração da reserva |
| `NOMERESPONSAVEL` | Nome do responsável pela reserva |
| `NOMECANDIDATO` | Nome do candidato |
| `STATUS` | Status da reserva |
| `TIPO` | Tipo da reserva, indica se a reserva é de uma vaga ou da posição de excedente |
| `DOCUMENTO` | Número do documento do candidato |
| `TIPODOCUMENTO` | Tipo do documento |
| `NUMEROINSCRICAO` | Número da inscrição vinculada, se houver |
| `RECCREATEDBY` | Usuário que criou a reserva |
| `RECCREATEDON` | Data de criação da reserva |
| `RECMODIFIEDBY` | Usuário que modificou a reserva |
| `RECMODIFIEDON` | Data da última modificação |

Informações da coluna - Status

| Código | Descrição | Detalhamento |
| --- | --- | --- |
| R | Reservado | A reserva é válida até o término do prazo de expiração. |
| N | Em fila | A vaga está em fila de reserva e sua disponibilidade não está garantida. |
| E | Expirada | A reserva da vaga expirou por tempo limite. |
| D | Desistência | O candidato optou por desistir da reserva da vaga durante a inscrição. |
| F | Finalizada | O candidato concluiu sua inscrição e a reserva da vaga foi finalizada com sucesso. |
| C | Cancelada | O candidato realizou a inscrição, mas optou por cancelá-la posteriormente. |

Importante: Status igual "R"

O campo **`DATAEXPIRA`** da tabela **`SPSINSCRICAORESERVA`** é o que realmente define se a reserva está ativa ou se já foi encerrada por tempo limite. Ou seja, é ele que indica se a reserva está expirada.

Mesmo que o status esteja como **"R"**, a reserva pode estar expirada caso a data/hora atual seja maior que a data/hora registrada no campo **`DATAEXPIRA`**.

O status **"E"** (Expirado) é atualizado em dois cenários:

1. **Quando um [processo complementar](https://tdn.totvs.com/pages/viewpage.action?pageId=856936252#id-03Comofuncionaareservadevagas?-Processosimpactados) executa a validação das vagas** — por exemplo, o processo **“Alterar candidatos excedentes para inscritos”**. Nessas situações, o sistema faz a atualização explícita dessa informação.
2. **Quando a inscrição chega até a API  já expirada,** nesse caso, a própria API identifica a expiração no momento do processamento e atualiza imediatamente o status para **"E"**, pois já é possível confirmar a situação no ato da requisição.

Por isso, entre o momento em que a reserva expira e o momento em que um desses processos é executado, o status poderá continuar como **"R"**, mas a reserva já será considerada expirada pela comparação com a data.

**Em resumo:**

* **Data de expiração** → determina de forma efetiva se a vaga ainda está disponível para o usuário.
Informações da coluna - Tipo da reserva

| Código | Descrição | Detalhamento |
| --- | --- | --- |
| V | Vaga | Quando a reserva possui o tipo **vaga**, ela assegura ao candidato a garantia da vaga no processo seletivo até o período de expiração da reserva. |
| E | Excedente | A reserva é do tipo **excedente**, ou seja, garante ao candidato uma posição na lista de excedentes. |

Informações da coluna - Tipo de documento

| Código | Descrição |
| --- | --- |
| 1 | CPF |
| 2 | Passaporte |
| 3 | Registro geral de estrangeiro |
