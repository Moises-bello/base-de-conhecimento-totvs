---
content_hash: ff091787aa820ace4e98ecb3b7a2a9ed19d392cbcb82f33adb63d7caba0ba6f0
fetched_at: '2026-06-29T00:10:08.636921+00:00'
page_id: '452719550'
product: rm
source: tdn-rm
title: Passo a Passo - Aumento Progressivo
type: documentation
url: https://tdn.totvs.com/display/LRM/Passo+a+Passo+-+Aumento+Progressivo
version: 80
---

**Passo a Passo - Aumento Progressivo**

**1. HABILITANDO AUMENTO PROGRESSIVO.**  
Por padrão o sistema não habilita a visão dos menus para cadastrar uma parametrização e uma progressão, para que seja habilitado o usuário deverá seguir os passos a seguir:

* Acessar o menu: Serviços Globais > Segurança > Perfis.
* Selecionar o sistema "Gestão de pessoas" e editar o perfil de acesso.

**2. CADASTRANDO UMA PARAMETRIZAÇÃO.**  
Parametrização são algumas regras que o usuário pode definir e que serão aplicadas no cadastro de uma requisição ou progressão.

* Acessar o menu: RH - Gestão de pessoas - Configurações - Tipos de requisição - Anexo: Parametrização.
* Clicar em "Incluir". (Obs.: A opção incluir somente será habilitada nas requisições de Alteração de dados funcionais e Transferência com alteração de dados funcionais)
* Configurar conforme desejado e salvar.

**3. INCLUINDO REQUISIÇÃO.**

Como informado anteriormente, o aumento progressivo é um complemento de duas requisições.  
Para cadastrar uma requisição de Alteração de dados funcionais:

* Acessar o menu: RH - Gestão de pessoas - Valorização - Requisições - Alteração de dados funcionais.
* Informar os dados da requisição.  Se o valor for superior ao parametrizado o sistema tentará gerar progressões que atendam a(s) regra(s) preestabelecida(s).

Para cadastrar uma requisição de Transferência com alteração de dados funcionais:

* Acessar o menu: RH - Gestão de pessoas - Valorização - Requisições - Transferência com alteração de dados funcionais.
* Informar os dados da requisição.  A transferência entre filiais não permite a inclusão de progressões, ou seja, o sistema não sugere progressão e não permite que insira a mesma manualmente. Na transferência para a mesma filial se for sugerido algum valor acima do limite parametrizado o sistema tentará gerar progressões que atendam a(s) regra(s) preestabelecida(s).

**Importante !** Ao manipular as requisições e incluir progressões pelo portal, essa progressão cadastrada será salva **SOMENTE** quando ocorrer manipulação da requisição (avanço de etapas).

**4. EDITANDO PROGRESSÕES.**

Ao cadastrar uma requisição que contenha progressões o usuário poderá acessar as progressões clicando no menu em anexo. A edição ou inclusão poderá ocorrer, mas as regras da parametrização continuam valendo e o sistema poderá impedir a inclusão ou edição se não estiverem de acordo com a regra.

* Para incluir uma progressão o usuário clica no botão incluir, e insira uma com data diferente da ultima progressão.
* Para editar o usuário seleciona a progressão e clica em editar.
* Para excluir o usuário deverá selecionar uma ou mais progressões e executar o progresso de remoção.

Possíveis dúvidas que podem ocorrer:

a) Editei ou inclui uma progressão e o sistema não realizou a validação, o que fazer? Verifique se a filial e o motivo são os mesmos que foram parametrizados.

b) Não foi exibido ou não consigo incluir progressões. Verificar se na parametrização foi marcado o campo "Permitir progressão?" ele define se a filial e motivo selecionados poderão incluir progressões.

**Obs**.: Na ausência de parametrização o sistema libera o cadastro de progressões sem validações, se existir alguma progressão registrada no sistema, se não tiver progressões e nem parametrização o sistema oculta o menu de progressões.  
   
**5. EFETIVAÇÃO DE REQUISIÇÕES COM PROGRESSÃO.**

Ao inserir um parecer "Aprovado" na requisição a mesma ficará disponível para conclusão no menu "Efetivações". Neste menu existe um processo "Concluir Requisição", que se executado em uma ou mais requisições que contenham progressões terá o seguinte comportamento:  
- Possuindo apenas uma progressão, o processo irá efetivar a progressão e também irá concluir a requisição.

- Possuindo mais de uma progressão, o processo irá efetivar apenas a próxima progressão e não irá concluir a requisição, pois a requisição só pode ser concluída depois de todas as progressões  efetivadas. No caso de ser a última progressão, o processo irá efetivar a progressão e também irá concluir requisição.

**Observação:**

Também é possível concluir a progressão através dos processos "Efetivar alteração de dados funcionais progressivo" e "Efetivar transferência com alteração de dados funcionais progressivo".

Para concluir uma requisição com progressões:

* Acesse o menu: "RH - Valorização - Efetivações - Efetivar alteração de dados funcionais" ou "Efetivar transferência com alteração de dados funcionais".
* Acesse o anexo: "Alteração de dados funcionais progressivo" ou "Transferência com alteração de dados funcionais progressivo".
* Selecione a primeira progressão que deve ser efetivada e execute o processo de efetivação. Obs.: Este processo só efetiva uma requisição por vez e de acordo com as datas de efetivação.
* Quando o usuário efetivar todas as progressões o sistema conclui a requisição e retira da visão, ao ser atualizada.

Para alterar uma progressão:

* Selecione a progressão e edite.

Importante: Nenhuma validação baseada na parametrização será realizada neste menu. Entendemos que o usuário aprovador final tem conhecimento e liberdade para fazer a alteração que quiser na requisição e aprova-la ou não.   
Para excluir uma progressão:

* Selecione as progressões e execute o processo de remoção. Poderão ser excluídas várias progressões ao mesmo tempo.

**Dúvida que pode ocorrer**:

Efetivei algumas progressões e removi as outras e a requisição continua na tela, o que fazer?

-Neste caso atualize a visão para o sistema identificar que não existe progressões pendentes para essa requisição e execute o processo "Concluir requisição".

**Observação:**     A progressão salarial não deve ser aplicada em ***requisições entre coligadas***, pois sua utilização nessa condição pode gerar erros e inconsistências nos dados.

Ressalta-se que, a partir da versão 12.1.2506, o sistema passará a exibir uma mensagem de alerta informando sobre a impossibilidade de realizar a progressão salarial entre coligadas, visando garantir a integridade e a confiabilidade das informações processadas.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Para entender melhor sobre Aumento progressivo Clique aqui.
