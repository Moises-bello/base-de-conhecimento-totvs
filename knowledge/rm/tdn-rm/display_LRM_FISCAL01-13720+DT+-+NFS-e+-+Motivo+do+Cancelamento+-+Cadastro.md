---
content_hash: f3c342e591ed153b3f8fcb4306e3b101e3ad04e126b0af3074fb93680dcc0d66
fetched_at: '2026-06-29T00:10:58.031018+00:00'
page_id: '602804076'
product: rm
source: tdn-rm
title: FISCAL01-13720 DT - NFS-e - Motivo do Cancelamento - Cadastro
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-13720+DT+-+NFS-e+-+Motivo+do+Cancelamento+-+Cadastro
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Cadastro de Motivo de Cancelamento da NFS-e |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13720 |

## **02. SITUAÇÃO/REQUISITO**

* Cadastro

Deverá ser criado um cadastro anexo ao cadastro de município para armazenar o Motivo de Cancelamento da NFS-e. O cadastro será composto de um Identificador, Código do Motivo do Cancelamento (alfanumérico) e Descrição do motivo do cancelamento;

Ao criar o cadastro deverá ser incluído um script para alimentar a base com os motivos de cancelamento já conhecidos referente a cada município.

## **03. SOLUÇÃO**

* Foi criado o cadastro de Motivo de Cancelamento da NFS-e anexo ao cadastro de Municípios
* Adicionado a permissão para acesso ao anexo no perfil (sistema Fiscal) - 01.02.02.04.05 Motivo de Cancelamento da NFS-e

Campos do cadastro (Tabela DMOTIVOCANCELAMENTONFSE)

* IDMOTCANC - Identificador (Interno) - Inteiro
* CODIGOMOTCANC - Código (Obrigatório) - Alfanumérico (15)
* DESCRICAOMOTCANC - Descrição (Obrigatório) - Alfanumérico (255)
* CODMUNICIPIO - Código do Município (Interno) - Alfanumérico (20)
* CODETDMUNICIPIO - Código do Estado do Município (Interno) - Alfanumérico (2)

Para acessar o cadastro, basta acessar o cadastro de municípios (BackOffice | Gestão Fiscal | Cadastros | Globais (Mais) | Municípios). Após executar o filtro que retorne o município desejado acessar Anexos | Motivo de Cancelamento da NFS-e.

Observação:

* Perfil associado ao usuário precisa ter acesso na permissão 01.02.02.04.05 Motivo de Cancelamento da NFS-e no Gestão Fiscal
* O cadastro é por município
* O cadastro é Global (Não depende da coligada)
