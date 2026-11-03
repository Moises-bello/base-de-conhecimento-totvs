---
content_hash: 0a63d23e22298b63e51f8a443b1b257043de392a1ca6b1bb908fdb023063efd7
fetched_at: '2026-06-29T00:12:15.638728+00:00'
page_id: '981002457'
product: rm
source: tdn-rm
title: Consultar Autorização NFCom
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=981002457
version: 40
---

# Conteúdo

Conteúdo

# 1. Visão Geral

O processo de "Consultar Autorização" tem como objetivo integrar-se ao TSS  para obter a autorização da NFCom. Essa consulta é realizada exclusivamente para as NFCom que estejam com o status "Pendente". Durante o processo, o sistema envia uma solicitação ao TSS para verificar o status da autorização da nota fiscal.

Este processo está disponível em 2 formas:

* **Consultar Autorização**: menu de Documentos Eletrônicos (*TOTVS Gestão de Estoque, Compras e Faturamento | Vendas | Documentos Eletrônicos | Nota Fiscal de Comunicação Eletrônica (NFCom) | Processos*).
* **Agendar Consulta Autorização**: menu de Documentos Eletrônicos (*TOTVS Gestão de Estoque, Compras e Faturamento | Vendas | Documentos Eletrônicos | Nota Fiscal de Comunicação Eletrônica (NFCom) | Processos*).

---

# 2. Fluxo do Processo

FluxoConsultar Autorização

falseReprocessar XMLfalseautohiddentrue91117

Fluxo Realizar Consultaleft1ADMEMPRESAS

Função do Serviço [ADMEMPRESAS](https://tdn.totvs.com/pages/viewpage.action?pageId=683376031): Informar ao sistema quais empresas estão habilitadas à utilizar os serviços.

* Resultado:
  + Se ocorrer erro → O sistema apresenta o Log do Processo.
  + Se executado com sucesso → Prossegue para o serviço RETORNANOTAS.
2RETORNANOTAS

Função do Serviço [RETORNANOTAS](https://tdn.totvs.com/pages/viewpage.action?pageId=683375423): Passando uma lista de números identificados para o serviço do TSS, o mesmo retornará a(s) remessa(s) do(s) documento(s) eletrônico(s) enviado(s) para a SEFAZ.

* Resultado:
  + Se houver retorno das remessas → O sistema apresenta o Log do Processo.
  + Se não houver retorno → Prossegue para o serviço MONITORFAIXA.
3MONITORFAIXA

Função do Serviço [MONITORFAIXA](https://tdn.totvs.com/pages/viewpage.action?pageId=683375375): Verificar o(s) documento(s) eletrônico(s) não retornado no serviço RETORNANOTAS, trazendo a situação atual do(s) mesmo(s).

* Resultado:
  + Sempre apresenta o Log do Processo.

---

# 3. Configurações iniciais

Para acessar o menu *Documentos Eletrônicos | Nota Fiscal de Comunicação Eletrônica (NFCom)* e Consultar a Nota, é necessário fornecer a permissão da **Nota Fiscal de Comunicação Eletrônica (NFCom),** conforme abaixo:

ConfigPermissões Usuários

Para dar permissão de acesso ao menu da NFCom a um usuário, siga os passos abaixo:

* Acesse o perfil vinculado ao usuário desejado do módulo TOTVS Gestão de Estoque, Compras e Faturamento e edite o perfil;
* Vá até a aba **Acesso a Menus**, siga o caminho **[*04] Vendas | [04.02] Documentos Eletrônicos***, selecione **[04.02.01.07] Nota Fiscal de Comunicação Eletrônica (NFCom), [04.02.01.07.05] Consulta Autorização**e logo após, clique em **Permitir Acesso**.

Segurança - Acesso - PerfisConfigurar Multiprocessamento

O Processo de consulta autorização deve ser executado utilizando o Multiprocessamento para trabalhar com grande volume de notas.   
O Multiprocessamento estará disponível em ambiente 3 camadas.

Para usar o multiprocessamento na Consulta Autorização é necessário cadastrá-lo em ***Ambiente | Segurança de Jobs Fracionáveis***. No cadastro, informe o perfil do usuário correspondente ao módulo, a classe de job como **"DocNFComConsultaTransmissaoProcData ",** as frações máximas e mínimas de acordo com a quantidade de vezes que desejar dividir o multiprocessamento e marque se ele é agendável e/ou se está ativo.

Segurança - Acesso - Perfis

---

# 4. Execução do Processo

Consultar Autorização:

ExecuçãoConsultar Autorização

Para executar o processo basta selecionar as notas com status "Pendente" e acionar o processo através do menu ***Documentos Eletrônicos | Nota Fiscal de Comunicação Eletrônica (NFCom) | Processos | Consultar Autorização***

**Recomendamos que o processo seja executado sem selecionar os registros, assim o processo será executado para todas as notas pendentes.**

Consultar AutorizaçãoObservação

Caso não seja selecionado nenhum registro o processo será executado para todas as notas com status "Pendente".

---

# 5. Consulta Automática

A consulta automática vai funcionar no ambiente 3 camadas, onde ficará disponível no menu processos a opção **Agendar Consulta Autorização**:

Agendar Consulta Autorização

---

# 6. Multiprocessamento

O Processo de consulta autorização deve ser executado utilizando o Multiprocessamento para trabalhar com grande volume de notas.   
  
Para fracionar o processo além de estar em ambiente 3 camadas deve ser cadastrado o Job Fracionável do processo, para a **Consulta Autorização** é utilizado o job **DocNFComConsultaTransmissaoProcData**

Job Fracionável

---
