---
content_hash: 19accf3f04483137938842907b67fd5cfc2c5737b1f254f889dc3e82c8a7bfee
fetched_at: '2026-06-29T00:12:16.206286+00:00'
page_id: '982919193'
product: rm
source: tdn-rm
title: Transmitir NFCom
type: documentation
url: https://tdn.totvs.com/display/LRM/Transmitir+NFCom
version: 12
---

# Conteúdo

Conteúdo

# 1. Visão Geral

O processo "Transmitir NFCom", disponível no módulo *TOTVS Gestão de Estoque, Compras e Faturamento*, tem como objetivo enviar o XML do documento fiscal para a SEFAZ. Para isso, o usuário deve selecionar a(s) nota(s) com status "Não transmitido" e executar o processo, que atualiza as informações no XML conforme necessário. Após a execução, o status da(s) nota(s) é alterado para **"Pendente"**, permitindo sua consulta em etapas posteriores. Caso o processo seja acionado sem selecionar nenhuma nota, o sistema buscará automaticamente todas as notas com  status pendente e realizará a transmissão.

Este processo está disponível em 2 formas:

* **Transmitir NFCom**: menu de Documentos Eletrônicos (*TOTVS Gestão de Estoque, Compras e Faturamento | Vendas | Documentos Eletrônicos | Nota Fiscal de Comunicação Eletrônica (NFCom) | Processos*).
* **Agendar Transmitir NFCom**: menu de Documentos Eletrônicos (*TOTVS Gestão de Estoque, Compras e Faturamento | Vendas | Documentos Eletrônicos | Nota Fiscal de Comunicação Eletrônica (NFCom) | Processos*).

---

# 2. Fluxo do Processo

falseReprocessar XMLfalseautohiddentrue9115

---

# 3. Configurações iniciais

Para acessar o menu *Documentos Eletrônicos | Nota Fiscal de Comunicação Eletrônica (NFCom)* e Transmitir a Nota, é necessário fornecer a permissão da **Nota Fiscal de Comunicação Eletrônica (NFCom),** conforme abaixo:

ConfigPermissões Usuários

Para dar permissão de acesso ao menu da NFCom a um usuário, siga os passos abaixo:

* Acesse o perfil vinculado ao usuário desejado do módulo TOTVS Gestão de Estoque, Compras e Faturamento e edite o perfil;
* Vá até a aba **Acesso a Menus**, siga o caminho **[*04] Vendas | [04.02] Documentos Eletrônicos***, selecione **[04.02.01.07] Nota Fiscal de Comunicação Eletrônica (NFCom),  [04.02.01.07.09] Transmitir NFCom** e logo após, clique em **Permitir Acesso**.

Segurança - Acesso - PerfisConfigurar Multiprocessamento

Para trabalhar com grande volume de notas, o processo de transmitir deve ser executado utilizando o Multiprocessamento .   
O Multiprocessamento estará disponível em ambiente 3 camadas.

Para usar o multiprocessamento é necessário cadastrá-lo em ***Ambiente | Segurança de Jobs Fracionáveis***. No cadastro, informe o perfil do usuário correspondente ao módulo, a classe de job como **"DocNFComTransmitirProcData",** as frações máximas e mínimas de acordo com a quantidade de vezes que desejar dividir o multiprocessamento e marque se ele é agendável e/ou se está ativo.

Segurança - Acesso - Perfis

---

# 4. Execução do Processo

Transmitir NFCom:

ExecuçãoTransmitir NFCom

Para executar o processo basta selecionar as notas com status "Não transmitido" e acionar o processo através do menu ***Documentos Eletrônicos | Nota Fiscal de Comunicação Eletrônica (NFCom) | Processos | Reprocessar NFCom***. Caso o processo seja acionado sem selecionar nenhuma nota, o sistema buscará automaticamente todas as notas com  status pendente e realizará a transmissão.

Transmitir NFComObservação

As notas selecionadas serão transmitidas e passarão para o status "**Pendente",** caso ocorra alguma falha no processo um log será gerado informando o motivo da não transmissão e o status da nota permanecerá como "**Não transmitido**".

---

# 5. Transmissão Automática

Esta funcionalidade tem como finalidade automatizar a transmissão da NFCom para a SEFAZ. Por meio do agendamento, é possível definir data e hora para a execução automática da rotina, além disso, também é possível configurar a periodicidade conforme a necessidade do usuário.

No menu Processos, a opção 'Agendar Transmissão NFCom' estará disponível apenas em ambientes configurados em três camadas. Portanto, é necessário que o sistema esteja operando nesse tipo de ambiente para que o agendamento da transmissão seja possível.

---

# 6. Multiprocessamento

O **multiprocessamento** é um recurso desenvolvido para proporcionar **mais agilidade, melhor performance e maior automação** no processo de geração da NFCom.

Como essa funcionalidade é uma novidade em relação à maioria dos outros documentos eletrônicos da Linha RM, preparamos um pequeno **FAQ** para esclarecer possíveis dúvidas:

* **O que acontece se eu não fizer o cadastro do multiprocessamento?**
  + A transmissão da NFCom será realizada em um único processo. Isso pode ser desvantajoso, pois resultará em um tempo de execução maior, especialmente para grandes volumes de notas e poderá tornar a utilização do sistema mais lenta. Além disso, cada processo tem um limite de execução de **21.000 notas**, e um volume maior do que esse resultará em erro.

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

# 7. Concorrência entre processos

Em ambientes **N camadas**, pode ocorrer a situação em que dois ou mais usuários executam o mesmo processo simultaneamente, o que resultaria na criação de processos idênticos.

No caso do transmitir da **NFCom**, se isso acontecer, ambos os processos fariam a **mesma seleção de notas**, gerando duplicidades, pois as mesmas notas seriam processadas em paralelo. Para evitar esse problema, o sistema gerencia a concorrência internamente por meio da identificação dos processos gerados.

Sempre que for detectado execuções simultâneas do mesmo processo (**classe do processo**) para a mesma coligada e classe de parâmetros, **a execução será bloqueada**. Nesses casos, o sistema exibirá a seguinte mensagem:

**"Já existe uma execução desse processo em andamento".**

* **Mas então o multiprocessamento não vai dar concorrência?**
  + Não, pois a cada processo que ele cria, recebe notas diferentes e não causa duplicidade.

* + - **E no caso de nomes diferentes do processo? Na imagem acima, há processos de nome "Gerar NFCom" e "Agendar geração NFCom"**
      * Isso não é um problema, pois todas as três formas de geração da NFCom utilizam a mesma classe do processo (DocNFComGerarData), que é o que importa para localizar processos concorrentes

---
