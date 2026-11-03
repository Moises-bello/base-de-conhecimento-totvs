---
content_hash: c5677d87bcc2e9c3f6627597ae8cee133bdf88b41468f25073c26c0ca01f9e51
fetched_at: '2026-06-29T00:12:16.636304+00:00'
page_id: '995198445'
product: rm
source: tdn-rm
title: Consulta de eventos NFCOM
type: documentation
url: https://tdn.totvs.com/display/LRM/Consulta+de+eventos+NFCOM
version: 6
---

# Conteúdo

Conteúdo

# 1. Visão Geral

O processo de "Consultar Eventos NFCOM" tem como objetivo integrar com o TSS para buscar a autorização do Evento da NFCom. Esse processo será executado somente para os Eventos com Status Pendente . 

Como resultado da consulta o Evento pode ser autorizado, rejeitado ou permanecer com o status de Pendente.

No caso da rejeição, a NFCom deverá retornar para o status Autorizada e o Evento Rejeitado.

No caso de Autorização a NFCom deverá mudar para o status Cancelada e o Evento Autorizado.

Processo disponível em:

* **Consulta de eventos**: menu de Documentos Eletrônicos (*TOTVS Gestão de Estoque, Compras e Faturamento | Vendas | Documentos Eletrônicos | Nota Fiscal de Comunicação Eletrônica (NFCom) | Processos*).

---

# 2. Fluxo do Processo

FluxoConsultar Eventos NFCOM

falseReprocessar XMLfalseautohiddentrue6311

1Consultar TSS

São utilizados os seguintes [Webservices](https://tdn.totvs.com/pages/viewpage.action?pageId=905130805)no processo de Consulta Autorização

trueConsultar evento Nfcomfalseautotoptrue7291

Fluxo Consultar eventos TSSleft1ADMEMPRESAS

Função do Serviço [ADMEMPRESAS](https://tdn.totvs.com/pages/viewpage.action?pageId=683376031): Informar ao sistema quais empresas estão habilitadas à utilizar os serviços.

* Resultado:
  + Se ocorrer erro → O sistema apresenta o Log do Processo.
  + Se executado com sucesso → Prossegue para o serviço CFGCERTIFICATEPFX.
2NFEMONITORLOTEEVENTO

Função do Serviço [NFEMONITORLOTEEVENTO](https://tdn.totvs.com/pages/viewpage.action?pageId=683375389): Método destinado ao monitoramento dos lotes dos novos eventos enviados à SEFAZ.

* Resultado:
  + Se houver retorno das remessas → O sistema apresenta o Log do Processo.
  + Se não houver retorno → Prossegue para o serviço  [NFERETORNAEVENTO](https://tdn.totvs.com/pages/viewpage.action?pageId=683375391).
3NFERETORNAEVENTO

Função do Serviço [NFERETORNAEVENTO](https://tdn.totvs.com/pages/viewpage.action?pageId=683375391): Método destinado ao retorno dos eventos da nota fiscal eletrônica.

* Resultado:
  + Sempre apresenta o Log do Processo.

---

# 3. Configurações iniciais

Para acessar o processo Eventos no menu *Documentos Eletrônicos | Nota Fiscal de Comunicação Eletrônica (NFCom)*, é necessário fornecer a permissão conforme abaixo:

ConfigPermissões Usuários

Para dar permissão de acesso ao menu da NFCom a um usuário, siga os passos abaixo:

* Acesse o perfil vinculado ao usuário desejado do módulo TOTVS Gestão de Estoque, Compras e Faturamento e edite o perfil;
* Vá até a aba **Acesso a Menus**, siga o caminho **[*04] Vendas | [04.02] Documentos Eletrônicos***, selecione **[04.02.01.07] Nota Fiscal de Comunicação Eletrônica (NFCom), [04.02.01.07.05] Consultar Evento NFCom** e logo após, clique em **Permitir Acesso**.

  

---

# 4. Execução do Processo

ExecuçãoProcesso Consulta de evento

Para executar o processo basta ir na aba "Anexos" do menu da NFCom e selecionar "Eventos", após abrir a tela com os eventos, selecione o evento desejado, vá em "Processos" e "Consulta de eventos".

Caso não seja selecionado nenhum registro o processo será executado para todas as notas com status "**Cancelamento Pendente**".

Caso seja selecionado a consulta de um evento com status diferente de "Cancelamento Pendente", o processo não será executado e será mostrada uma mensagem informando o status aceitos na consulta do evento.

Como resultado da consulta, o Evento pode ser autorizado, rejeitado ou permanecer com o status de Pendente.

  

# 5. Anexos

Eventos

Ao editar um Evento, teremos registros que exibem os status e datas de cada evento, juntamente com os XML de Envio.

Aba Identificação do EventoAba XML Envio

---
