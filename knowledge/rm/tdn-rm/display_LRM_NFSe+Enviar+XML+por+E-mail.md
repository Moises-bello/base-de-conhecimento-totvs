---
content_hash: 3dcafc81e07dfd345dc1c25922cd9ef2ff16b77367cb66d83df9a78fd4e313ae
fetched_at: '2026-06-29T00:11:03.338912+00:00'
page_id: '620775100'
product: rm
source: tdn-rm
title: NFSe Enviar XML por E-mail
type: documentation
url: https://tdn.totvs.com/display/LRM/NFSe+Enviar+XML+por+E-mail
version: 24
---

#f5f5f5#363636noneNFS-e por e-mail

## **Conteúdo**



## **01. Visão GeralVisaoGeral**

Este processo permite enviar, por e-mail, o xml da NFS-e que foi retornado pela prefeitura. Podendo ainda personalizar a mensagem do e-mail e incluir um relatório em anexo. Além disso, é possível parametrizar o envio do e-mail de forma automática (no momento em que uma nota é autorizada).

## **02. Enviar XML por e-mailEnvioManual**

Para executar o processo, basta acessar o menu BackOffice | Gestão de Estoque, compras e faturamento | Vendas | Faturamento | SPED NF-e (Municipal).

Após executar o filtro, na tela de NFS-e, basta selecionar as notas que deseja executar o processo e acessar Processos | Enviar XML por E-mail.

Imagem

**Cópia e Cópia Oculta**

É possível adicionar endereços de e-mail de cópia e cópia oculta. Estes campos são opcionais.

Para adicionar mais de um endereço de e-mail no mesmo campo, basta separá-los por ; (ponto e virgula).

Ex: [email@email.com.br](mailto:email@email.com.br);email2@[email.com.br](http://email.com.br)

**Assunto e Mensagem**

Ao abrir o Wizard do processo, automaticamente o sistema irá colocar um Assunto e Mensagem padrão.

O Assunto e a Mensagem podem ser alterados pelo usuário caso deseje.

## **03. Automatização do processo de Envio de e-mail da NFS-eEnvioAutomatico**

O Tipo de Movimento pode ser parametrizado para enviar os e-mails das NFS-e de forma automática ao realizar a consulta de autorização.

A parametrização pode ser realizada em BackOffice | Gestão de Estoque, compras e faturamento | Ambiente | Parâmetros | Gestão de Estoque, compras e faturamento | "Selecionar o tipo do movimento" | Fis - NF-e

Imagem

Neste parâmetro é possível parametrizar a **Mensagem**  que será encaminhada no e-mail, o **Formato do Relatório** e **Tipo de Envio**, este último podendo ser entre os tipos abaixo:

Imagem

**04. MensagemMensagem**

Para o processo de envio de e-mail pode ser configurado uma mensagem padrão. Para isso acesse o menu: BackOffice | Gestão de Estoque, compras e faturamento | Cadastros | Mais... (Estoque, Compras e Faturamento) |  Tabelas Auxiliares | Mensagens do Sistema

A Mensagem deve ser classificada com o tipo E-mail, conforme abaixo.

Imagem

Algumas variáveis podem ser adicionadas a mensagem para que o sistema busque as informações da nota específica selecionada.

Variáveis::

@NomeFilial = Nome da Filial que emitiu a NFS-e.  
@NomeCliente = Nome do Cliente da NFS-e.  
@DataAutorizacao = Data de Autorização da NFS-e.  
@ContatoFilial = Contato do cadastro da Filial que emitiu a NFS-e.  
@NumeroNota = Número da NFS-e.  
@TelFilial = Telefone da Filial que emitiu a NFS-e.  
@Usuario = Nome do usuário que está executando o processo.  
@Protocolo = Protocolo de Autorização da NFS-e.  
@NumeroRPS = Número do RPS,

**05. RelatórioRelatorio**

É possível anexar um relatório para ser gerado em PDF e anexado ao e-mail.

A TOTVS não disponibiliza um relatório padrão, porque cada prefeitura utiliza um padrão diferente de impressão das Notas. Então o relatório deve ser desenvolvido pelo cliente através do [RM Reports](https://tdn.totvs.com/pages/viewpage.action?pageId=88900459)

Ao criar um relatório é necessário definir dois parâmetros, conforme abaixo:

IDMOV\_N  
CODCOLIGADA\_N

Exemplo Simples:

Imagem

Consulta SQL

Imagem

Parâmetro no Relatório

## **06. Vídeo de DemonstraçãoHowTo**

4left1Parte 1

648432

2Parte 2

648432

## **06. Outras informaçõesOutrasInformacoes**

falseRegras do Processo

1. Se o ambiente da NFS-e estiver parametrizado como Homologação, o sistema irá buscar o endereço de e-mail da filial como Destinatário ao invés do endereço de e-mail do cliente. Isto se faz necessário para não enviar aos clientes reais notas emitidas para testes.
2. O botão executar somente ficará habilitado caso os campos Assunto e Mensagem estejam preenchidos. Se for marcado a flag "Enviar relatório da NFS-e em PDF" o campo do relatório também se torna obrigatório.
3. No Histórico da NFS-e o sistema irá gerar históricos dos envios de e-mails da NFS-e (Tanto processos executados com sucesso, quanto processos que ocorreram erros).
4. Foi adicionado o campo para indicar se a NFS-e já foi enviada por e-mail na tela de Notas Fiscais Eletrônicas de Serviço. Caso o envio do e-mail ocorra com sucesso, o sistema irá marcar o campo.

   Imagem
5. Em ambiente de Produção o sistema considera o e-mail informado no campo E-Mail Fiscal da tela de Tributos do cadastro de Cliente/Fornecedor conforme imagem abaixo. Caso este campo esteja vazio, será considerado o campo E-Mail da tela Identificação do cadastro de Cliente/Fornecedor. Se os dois campos de e-mail estiverem vazios, será apresenta a seguinte mensagem no log de execução: "E-mail não foi enviado. Endereço de e-mail do destinatário não informado".

   Imagem
Permissão

É necessário que o perfil associado ao usuário possua a permissão "[04.01.02.06.09] Enviar XML por E-mail" no sistema Gestão de Estoque, Compras e Faturamento.

Imagem
