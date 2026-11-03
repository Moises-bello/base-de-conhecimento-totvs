---
content_hash: 1aa898d706e00e8fa022bf49946fab9a371007c32168db6b3bbf17df3d8dd216
fetched_at: '2026-06-29T00:05:53.955531+00:00'
page_id: '1072432609'
product: rm
source: tdn-rm
title: Permitir anexar múltiplos arquivos em uma Requisição Geral
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1072432609
version: 1
---

## 1. Visão Geral

Esta documentação descreve a implementação da funcionalidade de múltiplos anexos nas **Requisições Gerais** através do portal **Meu RH**. A melhoria visa permitir que o usuário inclua até 4 documentos em uma única solicitação, facilitando envio de documentos na Requisição Geral.

2. Processo de Negócio

**Cenário:** Ao criar uma nova Requisição Geral, o usuário agora dispõe de um componente de upload que suporta a seleção e persistência de mais de um arquivo. 

## 3. Funcionalidades e Critérios de Aceitação

### Anexar Múltiplos Arquivos

O sistema permite a seleção de arquivos nos formatos **PDF, JPG, JPEG e PNG**.

**Limite de Quantidade:** Máximo de **4 arquivos** por requisição. 

**Limite de Tamanho:** Até **10 MB** por arquivo. 

### Regras de Validação e Mensagens

O sistema realiza validações em tempo real para garantir a integridade dos dados:

1. **Excesso de arquivos:** Ao tentar anexar o 5º arquivo, o sistema exibe: *"A quantidade de arquivos selecionada é de 5 e por isso ultrapassa a quantidade permitida de 4."*.
2. **Tamanho excedido:** Se um arquivo ultrapassar 10 MB, o sistema impede o upload
3. **Formato inválido:** Arquivos com extensões não permitidas geram o erro: *"O arquivo enviado possui um formato não permitido."*.
4. **Nome de arquivo:** O nome do arquivo deve ter no máximo **50 caracteres**.

### Remoção de Anexos Antes do Envio

Antes de finalizar a solicitação, o usuário pode remover arquivos individualmente da lista de pendentes.

Ao clicar no ícone de remoção, o arquivo é retirado da lista e o contador de limite é atualizado.

### Visualização e Download

Após a criação da requisição, os anexos podem ser visualizados e baixados tanto no **Portal Meu RH** quanto na **MDI do RM**.

**Portal:** Acessar "Ver mais detalhes" na requisição para listar e baixar os arquivos. 

**(ERP):** Os arquivos são integrados automaticamente e podem ser consultados em: `RH → Gestão de Pessoas → Gestão Organizacional → Requisições → Requisição Geral → Anexos`

## Evidências de Integração (Banco de Dados)

A persistência dos dados ocorre de forma íntegra, associando cada arquivo ao ID da requisição correspondente.

| **Campo** | **Descrição** |
| --- | --- |
| **IDREQ** | Identificador único da requisição |
| **NOMEARQUIVO** | Nome original do arquivo salvo |
| **ARQUIVO** | Conteúdo em formato binário (Blob) |

## 5. Observações Importantes

* **Edição:** Uma vez enviada a requisição, não é permitida a edição ou alteração dos anexos (conforme regra de negócio atual).
* **Upload Simultâneo:** O sistema está homologado para processar a seleção múltipla de arquivos de forma rápida sem perda de dados.
