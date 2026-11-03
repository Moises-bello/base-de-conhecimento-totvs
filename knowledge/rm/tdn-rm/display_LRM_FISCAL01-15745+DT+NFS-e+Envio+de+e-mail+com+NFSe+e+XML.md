---
content_hash: b6b59ae97d5d56e27d70c8564f804de0738152880e18f7902c793521604e6413
fetched_at: '2026-06-29T00:11:03.330092+00:00'
page_id: '620774802'
product: rm
source: tdn-rm
title: FISCAL01-15745 DT NFS-e Envio de e-mail com NFSe e XML
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-15745+DT+NFS-e+Envio+de+e-mail+com+NFSe+e+XML
version: 9
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Envio da NFS-e por e-mail |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15745 |

## **02. SITUAÇÃO/REQUISITO**

Criação de um processo na tela de NFS-e para enviar ao cliente por e-mail o PDF da Nota (Relatório desenvolvido pelo Cliente) e o XML da NFS-e.

## **03. SOLUÇÃO**

Foi criado o processo "Enviar XML por Email" na tela de NFS-e.

Neste processo, é possível enviar o XML da NFS-e e anexar algum relatório para  que o RM envie e-mails para os clientes das notas selecionadas.

* **Cópia e Cópia Oculta**

É possível adicionar endereços de e-mail de cópia e cópia oculta. Estes campos são opcionais.

Para adicionar mais de um endereço de e-mail no mesmo campo, basta separá-los por ; (ponto e virgula).

Ex: email@email.com.br;email2@email.com.br

* **Assunto e Mensagem**

Ao abrir o Wizard do processo, automaticamente o sistema irá colocar um Assunto e Mensagem padrão (atualmente não é parametrizável este default).

O Assunto e a Mensagem podem ser alterados pelo usuário caso deseje.

Pode adicionar parâmetros de texto na mensagem para que o sistema busque as informações da nota específica selecionada.

Parâmetros:

@NomeFilial = Nome da Filial que emitiu a NFS-e.  
@NomeCliente = Nome do Cliente da NFS-e.  
@DataAutorizacao = Data de Autorização da NFS-e.  
@ContatoFilial = Contato do cadastro da Filial que emitiu a NFS-e.  
@NumeroNota = Número da NFS-e.  
@TelFilial = Telefone da Filial que emitiu a NFS-e.  
@Usuario = Nome do usuário que está executando o processo.  
@Protocolo = Protocolo de Autorização da NFS-e.  
@NumeroRPS = Número do RPS,

* **Relatório PDF em anexo**

É possível anexar um relatório para ser gerado em PDF no anexo do e-mail. Para isto, basta marcar a flag "Enviar relatório da NFS-e em PDF" que o campo será habilitado para preenchimento. Não é possível parametrizar um default para este campo.

Não possuímos um relatório padrão, porque cada prefeitura pode utilizar um padrão diferente de impressão das Notas.

Então o relatório deve ser desenvolvido pelo cliente.

Para o relatório funcionar no processo, é necessário que possua dois parâmetros:

IDMOV\_N  
CODCOLIGADA\_N

* **Regras do Processo**

1 - Se o ambiente da NFS-e estiver parametrizado como Homologação, o sistema irá buscar o endereço de e-mail da filial como Destinatário ao invés do endereço de e-mail do cliente. Isto se faz necessário para não enviar para os clientes notas que foram emitidas para testes.

2 - O botão executar somente ficará habilitado caso os campos Assunto e Mensagem estejam preenchidos. Se for marcado a flag "Enviar relatório da NFS-e em PDF" o campo do relatório também se torna obrigatório.

3 - No Histórico da NFS-e o sistema irá gerar históricos dos envios de e-mails da NFS-e (Tanto processos executados com sucesso, quanto processos que ocorreram erros).

4 - Foi adiciona o campo para indicar se a NFS-e já foi enviada por e-mail na tela de Notas Fiscais Eletrônicas de Serviço. Caso o envio do e-mail ocorra com sucesso, o sistema irá marcar o campo.

* **Permissão**

É necessário que o perfil associado ao usuário possua a permissão "[04.01.02.06.09] Enviar XML por E-mail" no sistema Gestão de Estoque, Compras e Faturamento.

* **Observação**

Disponível a partir da Biblioteca 12.1.33
