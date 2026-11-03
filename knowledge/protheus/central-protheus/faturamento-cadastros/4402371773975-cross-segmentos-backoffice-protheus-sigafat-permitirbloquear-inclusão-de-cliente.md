---
article_id: 4402371773975
category: Faturamento - Cadastros
content_hash: 7f6620fcb45561db125782ab98d2fa9b0751e8ce6ff0477fdbf75d7eba9952b8
fetched_at: '2026-06-28T22:38:35.470647+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Permitir/bloquear inclusão
  de clientes com CNPJ e CPF já informados
type: support-article
updated_at: '2025-07-04T12:51:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402371773975-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Permitir-bloquear-inclus%C3%A3o-de-clientes-com-CNPJ-e-CPF-j%C3%A1-informados
---

**Dúvida**Configuração para permitir ou bloquear a inclusão de CNPJ e CPF repetidos  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - a partir da versão 11.  
  
**Solução**Ajuste parâmetros de acordo com tipo de entidade que utiliza:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24770713637655)

**Cadastro Clientes** possui os parâmetros **MV\_VALCNPJ** e **MV\_VALCPF**:

**MV\_VALCNPJ ou MV\_VALCPF igual 1** - Notificar o usuário de que o **CNPJ/CPF** já existe em outro cadastro, porém permitir o cadastro;

**MV\_VALCNPJ ou MV\_VALCPF igual 2** - Impedir o cadastro de registros com o mesmo **CNPJ/CPF**.

**Cadastro de Prospect e Suspect** possui o parâmetro **MV\_VALCNPJ**:

**MV\_VALCNPJ ou MV\_VALCPF igual 1** - Notificar o usuário de que o **CNPJ/CPF** já existe em outro cadastro, porém permitir o cadastro;

**MV\_VALCNPJ ou MV\_VALCPF igual 2**- Impedir o cadastro de registros com o mesmo **CNPJ/CPF**.

**Observação:** Saia e entre no sistema para validar a configuração do parâmetro após alterá-lo.
