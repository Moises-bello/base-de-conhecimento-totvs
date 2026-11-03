---
article_id: 29041851954839
category: Originação de Grãos (OG)
content_hash: 7cb9d94c6a519ac7cf75387b371a45c9b3e5baeea5733666fc34a527cca1db3e
fetched_at: '2026-06-28T22:45:37.792088+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Configuração/Parâmetros da Rotina no Fluxo do
  Contrato de Terceiros
type: support-article
updated_at: '2025-06-24T14:43:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29041851954839-Agro-Linha-Protheus-AGR-Configura%C3%A7%C3%A3o-Par%C3%A2metros-da-Rotina-no-Fluxo-do-Contrato-de-Terceiros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29041851908887) Tempo aproximado para leitura: **00:02:10 min** **Dúvida**Como são realizados os principais parâmetros em **Configuração/Parâmetros da Rotina no Fluxo do Contrato de Terceiros**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução****Principais parâmetros:**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parâmetro** | **Descrição** | **Conteúdo padrão** | **Conteúdo exigido para esta rotina** |
| [MV\_OGDECPS](https://tdn.totvs.com/pages/viewpage.action?pageId=268596595) | Definir Quantidade de Decimais p/ Campos de Peso no Romaneio | 0 | (opcional) |
| [MV\_AGRO044](https://tdn.totvs.com/pages/viewpage.action?pageId=545234832) | Incluir romaneios atualizados no Calculo de Serviços. | .F. | (opcional) |
| [MV\_OGASERS](https://tdn.totvs.com/pages/viewpage.action?pageId=248582943) | Informar a Série Padrão para a Geração dos Documentos de Saída | <vazio> | Série do Sistema |

Pré-requisitos:

* Produto cadastrado e com **UM** de preço informada na pasta **Agro** do programa **MATA010 - Cadastro de Produtos**;
* Entidades cadastradas;
* Safras cadastradas;
* Tipos de despesas cadastradas;
* Tabela de serviços e itens de serviços previamente cadastrados e configurado para cálculo do serviço;
* **TES** configuradas para controle de saldo de terceiros.
