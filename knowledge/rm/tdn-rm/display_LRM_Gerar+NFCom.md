---
content_hash: 1ef5c69e8a9d93cb953691206f8444ad2698ad81b92aff86a9477d3191a65b31
fetched_at: '2026-06-29T00:12:03.281347+00:00'
page_id: '905128290'
product: rm
source: tdn-rm
title: Gerar NFCom
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerar+NFCom
version: 114
---

# Conteúdo

Conteúdo

# 1. Visão Geral

O processo de Gerar NFCom - disponível no Módulo "TOTVS Gestão de Estoque, Compras e Faturamento" - transforma os movimentos criados nesse módulo em documentos fiscais eletrônicos (arquivos em formato XML) que serão transmitidas à SEFAZ do Contribuinte posteriormente, em outra etapa do fluxo da NFCom (para visualizar o fluxo, acesse [Nota Fiscal de Comunicação Eletrônica (NFCom) | 3.2 Processos](https://tdn.totvs.com/pages/viewpage.action?pageId=880058547#NotaFiscaldeComunica%C3%A7%C3%A3oEletr%C3%B4nica(NFCom)-3.2Processos)).

---

# 2. Fluxo do Processo

Abaixo é detalhado o fluxo do processo de Gerar NFCom, ao clicar em algumas etapas o processo será detalhado.

falseFluxo Gerar NFComfalseautohiddentrue10619

60%#0022331dashedDetalhes

---

# 3. Configurações iniciais

Para acessar o menu *Documentos Eletrônicos | Nota Fiscal de Comunicação Eletrônica (NFCom)* e gerar a NFCom, é necessário realizar algumas configurações iniciais, conforme abaixo:

ConfigPermissões Usuários

Este modelo de documento possui uma permissão de acesso diferente dos demais documentos eletrônicos. Para dar permissão de acesso ao menu da NFCom a um usuário, siga os passos abaixo:

* Acesse o perfil vinculado ao usuário desejado do módulo TOTVS Gestão de Estoque, Compras e Faturamento e edite o perfil;
* Vá até a aba **Acesso a Menus**, siga o caminho **[*04] Vendas | [04.02] Documentos Eletrônicos***, selecione **[04.02.01.07] Nota Fiscal de Comunicação Eletrônica (NFCom)** , **[04.02.01.07.08] Gerar NFCom** e logo após, clique em **Permitir Acesso**.

Segurança - Acesso - PerfisConfigurar Multiprocessamento

Este processo possui o conceito de multiprocessamento¹, ou seja, pode ser executado em vários pedaços para que o processamento de grandes volumes de dados seja mais rápido.  
Suponhamos que a geração da NFCom será feita para 15.000 movimentos. O multiprocessamento irá dividir esses movimentos em vários processos separados e executar cada um desses processos com quantidades menores de notas. Isso resulta em um ganho de tempo e performance tanto na geração das notas quanto na utilização do sistema como um todo.

falseMultiprocessamentofalseautohiddentrue5712

```
¹ Este conceito é referido tecnicamente na Linha RM como fracionamento de jobs.
```

Para usar o multiprocessamento na geração da NFCom, é necessário cadastrá-lo em ***Ambiente | Segurança de Jobs Fracionáveis***. No cadastro, informe o perfil do usuário correspondente ao módulo, a classe de job como **"DocNFComGerarData",** as frações máximas e mínimas de acordo com a quantidade de vezes que desejar dividir o multiprocessamento e marque se ele é agendável e/ou se está ativo.

Ambiente - Processos - Segurança de Jobs Fracionáveis

Formulário exemplificando os dados do fracionamento:

Formulário do Fracionamento de Job 

---

# 4. Execução do Processo

Como exibido no tópico 1. Visão Geral, há três caminhos para execução do processo de Gerar NFCom. Todas seguem as mesmas regras para a geração do XML da NFCom, diferindo apenas na maneira como o usuário pode planejar e executar a emissão das notas. Abaixo, seguem as diferenças entre cada um dos processos, incluindo detalhes sobre seleção de registros, multiprocessamento (fracionamento de jobs) e agendamento para execução automática:

ExecuçãoGerar NFCom (principal)

A execução deste processo ocorre através do menu ***Documentos Eletrônicos | Nota Fiscal de Comunicação Eletrônica (NFCom) | Processos | Gerar NFCom***.

Gerar NFCom

O processo identifica automaticamente quais movimentos de NFCom ainda não geraram o XML, não sendo necessário selecionar nenhum registro na tela. Esta seleção é realizada considerando a parametrização do tipo de Movimento (vide item [Nota Fiscal de Comunicação Eletrônica (NFCom) | 2.Parâmetros](https://tdn.totvs.com/pages/viewpage.action?pageId=880058547)). Mesmo que algum registro em específico seja selecionado, a geração não irá se aplicar apenas para ele, e sim para todos os movimentos no sistema que estejam parametrizados para geração da NFCom e ainda não tenham suas notas geradas.

Este processo principal não reprocessa notas já geradas ou com erro/inconsistência. Caso seja necessário reprocessar notas específicas, veja "Gerar NFCom (à partir do movimento)" ou volte acesse  [Nota Fiscal de Comunicação Eletrônica (NFCom) | 3.2 Processos](https://tdn.totvs.com/pages/viewpage.action?pageId=880058547#NotaFiscaldeComunica%C3%A7%C3%A3oEletr%C3%B4nica(NFCom)-3.2Processos) e verifique a etapa responsável pelo reprocessamento da NFCom.

As notas serão geradas com o status **Não Transmitido,** caso não haja erros na validação do schema, ou **"Inconsistente"**, caso ocorra alguma falha na validação.

Gerar NFCom (a partir do Movimento)

A execução deste processo ocorre diretamente no movimento. Para isto, acesse o movimento parametrizado para geração de NFCom e vá em****Processos | Gerar Xml NFCom*.***

Gerar Xml NFCom

Exemplo acessando o processo através de um movimento de faturamento:

Esta tela permite a seleção específica dos movimentos que irão gerar a NFCom na tela. Caso nenhum movimento seja selecionado, o processo será executado para todos os movimentos presentes na tela, semelhante à maioria dos processos da Linha RM.  
Importante ressaltar que **este processo possui limite de 500 registros**. Ainda que a configuração de quantidade máxima de registros exibidos na tela seja alterada, não será possível executar o processo para mais de 500 registros. Para volumes de dados maiores, utilize o processo "**Gerar NFCom (principal)**" descrito na primeira aba deste tópico.

Este processo é semelhante ao de  "**Gerar NFCom"** que está no menu de "**Nota Fiscal de Comunicação Eletrônica (NFCom)"**. Ele irá gerar as notas com  o status **Não Transmitido,** caso não haja erros na validação do schema, ou **"Inconsistente"**, caso ocorra alguma falha na validação. Ele também realiza o reprocessamento de notas, atualizando tanto o conteúdo da nota (xml) quanto seu novo status ao reprocessar.

Gerar NFCom (automático por agendamento de job)

Para acessar o agendamento da NFCom, vá em ***Documentos Eletrônicos | Nota Fiscal de Comunicação Eletrônica (NFCom) | Processos | Agendar Geração NFCom**.*

Agendar geração NFCom

Este processo é equivalente ao **"Gerar NFCom (principal)"**, com a diferença de que permite o agendamento dos jobs responsáveis pela execução. Dessa forma, é possível programar múltiplas execuções futuras de maneira automática, sem a necessidade de intervenção do usuário. O agendamento da NFCom estará disponível apenas se o ambiente utilizado for **em N camadas** **e** se o cadastro do fracionamento estiver com a opção **"Agendável"** marcada. Caso contrário, será exibida apenas uma tela de conclusão de processos.

Assim como o processo principal, o agendamento considera todos os movimentos previamente parametrizados e que ainda não tenham notas geradas.  Além disso, ele **não reprocessa notas com erro ou inconsistentes**e **não permite a seleção pontual dos movimentos.**

Observação

Diferente dos modelos de NF-e e NFS-e, o processo de Gerar NFCom não faz nenhuma comunicação com a SEFAZ. Ele apenas gera o XML da nota e valida seu schema, sendo necessário realizar a transmissão das notas posteriormente.

---

# 5. Multiprocessamento

O **multiprocessamento** é um recurso desenvolvido para proporcionar **mais agilidade, melhor performance e maior automação** no processo de geração da NFCom.

Como essa funcionalidade é uma novidade em relação à maioria dos outros documentos eletrônicos da Linha RM, preparamos um pequeno **FAQ** para esclarecer possíveis dúvidas:

* **O que acontece se eu não fizer o cadastro do multiprocessamento?**
  + A geração da NFCom será realizada em um único processo. Isso pode ser desvantajoso, pois resultará em um tempo de execução maior, especialmente para grandes volumes de notas e poderá tornar a utilização do sistema mais lenta. Além disso, cada processo tem um limite de execução de **21.000 notas**, e um volume maior do que esse resultará em erro.

* **Quando a divisão dos processos ocorre na geração da NFCom?**
  + Se o multiprocessamento for cadastrado conforme explicado no tópico 3. Configurações Iniciais | Configurar Multiprocessamento, a divisão dos processos acontecerá automaticamente **ao iniciar a geração da NFCom**. Não é necessário definir nenhum parâmetro adicional, pois o sistema realiza essa divisão de forma automática. O acompanhamento dos processos gerados pode ser feito em *Ambiente | Gerenciamento de Jobs*.

* **Quantos registros por processo o multiprocessamento suporta?**
  + São 21.000 registros/notas por processo. Caso o multiprocessamento esteja parametrizado para fazer 50 divisões, por exemplo, é possível fazer a geração de volumes de mais de 1.000.000 de notas.

* **O que acontece se a quantidade de divisões que informei no cadastro do multiprocessamento não for suficiente para gerar minhas notas?**
  + O sistema recalcula automaticamente a quantidade necessária de divisões com base no volume total de notas. Esse cálculo segue a fórmula:

    **Total de notas / limite de notas por processo (21.000)** → arredondado para cima.

    Por exemplo, se houver **50.000 notas** e o multiprocessamento estiver configurado para **apenas 2 divisões**, o cálculo será:

    **50.000 / 21.000 ≈ 2,4 → arredondando para cima → 3 divisões**.

    O cadastro original do multiprocessamento **não será alterado**, pois essa nova quantidade de divisões será ajustada internamente pelo sistema sempre que necessário.

---

# 6. Concorrência entre processos

Em ambientes **N camadas**, pode ocorrer a situação em que dois ou mais usuários executam o mesmo processo simultaneamente, o que resultaria na criação de processos idênticos.

No caso da geração da **NFCom**, se isso acontecer, ambos os processos fariam a **mesma seleção de notas**, gerando duplicidades, pois as mesmas notas seriam processadas em paralelo. Para evitar esse problema, o sistema gerencia a concorrência internamente por meio da identificação dos processos gerados.

Sempre que for detectado execuções simultâneas do mesmo processo (**classe do processo**) para a mesma coligada e classe de parâmetros, **a execução será bloqueada**. Nesses casos, o sistema exibirá a seguinte mensagem:

**"Já existe uma execução desse processo em andamento".**

* **Mas então o multiprocessamento não vai dar concorrência?**
  + Não, pois a cada processo que ele cria, recebe notas diferentes e não causa duplicidade.

* **E no caso de nomes diferentes do processo? Na imagem acima, há processos de nome "Gerar NFCom" e "Agendar geração NFCom"**
  + Isso não é um problema, pois todas as três formas de geração da NFCom utilizam a mesma classe do processo (DocNFComGerarData), que é o que importa para localizar processos concorrentes.
