---
content_hash: efc7a4b41b223a814485ce302a347f9c44575c7968508c274472b8bb681b6f58
fetched_at: '2026-06-29T00:12:08.357151+00:00'
page_id: '930805629'
product: rm
source: tdn-rm
title: Nota Técnica 2018.005 - v1.51 (Março 2025)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=930805629
version: 12
---

# Conteúdo

2Conteúdonone

# 1. Sobre

A **Nota Técnica 2018.005 v1.51**, publicada em **13/03/2025**, tem como objetivo reforçar a **segurança, rastreabilidade e integridade** das **Notas Fiscais Eletrônicas** (NF-e e NFC-e). Esta versão introduz:

* A obrigatoriedade do preenchimento do **Responsável Técnico** no XML da NF-e/NFC-e;
* E, em algumas **Unidades Federativas**, a exigência do **Código de Segurança do Responsável Técnico (CSRT)**.

# 2. Cronograma

| **Regra de Validação** | **Descrição** | **Homologação** | **Produção** |
| --- | --- | --- | --- |
| **ZD02-10** | Rejeição: *CNPJ do responsável técnico inválido* | 16/09/2024 | 01/05/2025 |
| **ZD07-10** | Rejeição: *Obrigatória a informação do identificador e Hash do CSRT* | 04/08/2025 | 15/09/2025 |

# 3. Legislação

Este documento foi elaborado com base na [Nota Técnica 2018.005 - v.1.51 - Publicada em 13/03/2025](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=URRwWd0zp2U=) disponível no portal da NF-e.

> Importante: A exigência do Responsável Técnico e do CSRT está prevista no escopo da NT 2018.005 e deve ser observada conforme a legislação específica de cada estado.

# 4. Configuração do sistema

Basta atualizar para um dos patches abaixo:

* `12.1.2406.246`
* `12.1.2410.186`
* `12.1.2502.110`

Após atualização, executar o processo .

# 5. Cadastro na SEFAZ PR

A partir do dia **01/05/2025** a SEFAZ-PR irá ativar a "**Rejeição 974 - CNPJ do responsável técnico diverge do cadastrado**" e , desta forma se o CNPJ da sua empresa não estiver vinculado ao CNPJ da TOTVS, você ficará impossibilitado de emitir NFe e NFC-e.

Para detalhes do procedimento necessário para a realização do vinculo com a TOTVS, acesse [Atualização de Vínculo com o Fornecedor na SEFAZ-PR - TOTVS Backoffice Linha RM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30934416662551-Atualiza%C3%A7%C3%A3o-de-V%C3%ADnculo-com-o-Fornecedor-na-SEFAZ-PR-TOTVS-Backoffice-Linha-RM)

# 6. Ainda tem dúvidas?

No dia **24/04/2025 às 14h15**, realizaremos um **tira dúvidas** **exclusivo** sobre as mudanças na emissão da Nota Fiscal Eletrônica no Paraná e como a **linha RM** já está preparada para essa nova obrigatoriedade.  
Participe e garanta que sua empresa esteja em conformidade, evitando surpresas e transtornos na hora da emissão!  
📅 **Data:** 24/04/2025  
🕒 **Horário:** 14h15  
📍 **Online**  
📌 [Inscreva-se agora e garanta sua vaga!](https://totvs.zoom.us/webinar/register/WN_Vqp-9nttSRyxa8BZCP62Wg)
