---
content_hash: 7ecf7017642a233b9dc6e3263f4d01cc3fa42313188bb62f05451b751b7fd362
fetched_at: '2026-06-29T00:12:16.333984+00:00'
page_id: '985661803'
product: rm
source: tdn-rm
title: Eventos NFCom
type: documentation
url: https://tdn.totvs.com/display/LRM/Eventos+NFCom
version: 54
---

# Conteúdo

Conteúdo

# 1. Visão Geral

O processo de "Enviar Evento da NFCom" tem como objetivo integrar-se ao TSS para enviar a solicitação de cancelamento da NFCom para a SEFAZ. Para o envio do evento de cancelamento é necessário que a(s) NFCom(s) estejam com o status "**Autorizada**". 

Este processo está disponível em apenas 1 forma:

* **Eventos NFCom**: menu de Documentos Eletrônicos (*TOTVS Gestão de Estoque, Compras e Faturamento | Vendas | Documentos Eletrônicos | Nota Fiscal de Comunicação Eletrônica (NFCom) | Processos*).

---

# 2. Fluxo do Processo

Fluxo1Envento Cancelamento

falseEnviar Evento TSSfalseautohiddentrue8727

Fluxo Realizar Consultaleft1ADMEMPRESAS

Função do Serviço [ADMEMPRESAS](https://tdn.totvs.com/pages/viewpage.action?pageId=683376031): Informar ao sistema quais empresas estão habilitadas à utilizar os serviços.

* Resultado:
  + Se ocorrer erro → O sistema apresenta o Log do Processo.
  + Se executado com sucesso → Prossegue para o serviço CFGCERTIFICATEPFX.
2CFGCERTIFICATEPFX

Função do Serviço [CFGCERTIFICATEPFX](https://tdn.totvs.com/pages/viewpage.action?pageId=683375693)**:** Valida e configura certificado digital PFX (.pfx/.p2b) para assinatura da NFCom e comunicação com a SEFAZ.

* Resultado:
  + Se ocorrer erro → O sistema apresenta o Log do Processo.
  + Se executado com sucesso → Prossegue para o serviço CFGCERTIFICATEPFX.
3CFGAMBIENTE

Função do Serviço [CFGAMBIENTE](https://tdn.totvs.com/pages/viewpage.action?pageId=683375683): Configura ambiente Produção ou Homologação para NFCom passando o modelo do documento e o ID da entidade retornada pelo serviço ADMEMPRESAS.

* Resultado:
  + Se ocorrer erro → O sistema apresenta o Log do Processo.
  + Se executado com sucesso → Prossegue para o serviço CFGVERSAO.
4CFGVERSAO

Função do Serviço [CFGVERSAO](https://tdn.totvs.com/pages/viewpage.action?pageId=683375748): Configura a versão de leiaute para comunicação e geração da NFCom passando o versão, modelo do documento e ID da entidade retornada pelo serviço ADMEMPRESAS.

* Resultado:
  + Se ocorrer erro → O sistema apresenta o Log do Processo.
  + Se executado com sucesso → Prossegue para o serviço CFGNFCOM.
5CFGNFCOM

Função do Serviço CFGNFCOM: Configuração dos parâmetros da NFCom passando o ambiente (Produção ou Homologação), versão, modelo do documento e ID da entidade retornada pelo serviço ADMEMPRESAS.

* Resultado:
  + Se ocorrer erro → O sistema apresenta o Log do Processo.
  + Se executado com sucesso → Prossegue para o serviço REMESSAEVENTO.
6REMESSAEVENTO

Função do Serviço REMESSAEVENTO: Envio de evento da NFCom passando o Xml do lote e ID da entidade retornada pelo serviço ADMEMPRESAS.

* Resultado:
  + Sempre apresenta o Log do Processo.

---

# 3. Configurações iniciais

Para acessar o processo Eventos no menu *Documentos Eletrônicos | Nota Fiscal de Comunicação Eletrônica (NFCom)*, é necessário fornecer a permissão conforme abaixo:

ConfigPermissões Usuários

Para dar permissão de acesso ao menu da NFCom a um usuário, siga os passos abaixo:

* Acesse o perfil vinculado ao usuário desejado do módulo TOTVS Gestão de Estoque, Compras e Faturamento e edite o perfil;
* Vá até a aba **Acesso a Menus**, siga o caminho **[*04] Vendas | [04.02] Documentos Eletrônicos***, selecione **[04.02.01.07] Nota Fiscal de Comunicação Eletrônica (NFCom)** selecione as permissões conforme exemplos abaixo e logo após, clique em **Permitir Acesso**.

Segurança - Acesso - PerfisCancelar NFCom

**[04.02.01.07.02] Cancelar NFCom**

Enviar Evento Cancelamento

**[04.02.01.07.06] Enviar Evento NFCom**

Consultar Evento Cancelamento

**[04.02.01.07.03] Consultar Evento NFCom**

---

# 4. Execução do Processo

ExecuçãoEvento Cancelamento

Para executar o processo basta selecionar a NFCom com status "Autorizada" e acionar o processo através do menu ***Documentos Eletrônicos | Nota Fiscal de Comunicação Eletrônica (NFCom) | Processos | Eventos NFCom***

Caso não seja selecionado nenhum registro o processo será executado para todas as notas com status "**Autorizada**".

E quando for enviado vários registros NFCom, o texto informado com o motivo do cancelamento será usado por todos.

Enviar Evento Cancelamento

---

# 5. Anexos

Eventos

No Anexo de Evento, teremos um registro detalhado de cada evento efetuado nas NFCom principal. Armazenando e exibindo os status e datas de cada evento, juntamente com os XML de Envio e o XML de Retorno.

Aba Identificação do EventoAba XML EnvioAba XML Retorno

Histórico do Evento

O Anexo **Histórico do Evento,** vai esta disponível dentro do F**ormulário de Evento**, será como um **"retrato" do Evento**, cada interação será gravada e armazenada o status atual desta interação.

Aba Identificação do EventoAba XML EnvioAba XML Retorno
