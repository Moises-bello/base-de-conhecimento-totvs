---
article_id: 22685798636823
category: Originação de Grãos (OG)
content_hash: 8bb8684458ea515793adf651afad73cfa1e0ee62dbe7555b437b945e437bc7fa
fetched_at: '2026-06-28T22:45:42.628921+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Parâmetros/Configurações em Registro de Negócio
type: support-article
updated_at: '2024-04-10T14:57:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22685798636823-Agro-Linha-Protheus-AGR-Par%C3%A2metros-Configura%C3%A7%C3%B5es-em-Registro-de-Neg%C3%B3cio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22685829124887) Tempo aproximado para leitura: **00****:00:50 min****Dúvida**Quais são os **Parâmetros/Configurações em Registro de Negócio**?  
  
**Ambiente**TOTVS Agro – TOTVS Agro – Comercialização (Linha Protheus) - Originação de Grãos (OG) – Versão 12  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

**O conteúdo dos parâmetros pode ser alterado na rotina **Parâmetros** do módulo **Configurador**. Os parâmetros utilizados no módulo de **Gestão Agroindústria** do **Microsiga Protheus** são:**

|  |  |
| --- | --- |
| **Campo:** | **Descrição** |
| Op. Negócio | Permite informar se o novo Negócio é :  1 - Compra ou 2 - venda |
| Tipo Mercado | Selecionar se será um negócio Mercado Interno ou Externo. |
| Fil. Origem | Informar:  Para Vendas: Filial fiscal de expedição.  Para Compras: Filial fiscal de recebimento. |
| Tipo Preço | 1 - Fixo , 2 - À Fixar |
| Entidade | Código do cliente ou fornecedor do negócio |
| Modalidade | Permite informar o código da modalidade para classificar a negociação. Quando no cadastro da modalidade há informação da finalidade o campo Finalidade do contrato é carregado automaticamente.  Também são utilizadas as informações do tipo de fixação e de mercado informados no cadastro de modalidades para validar com os mesmos campos do registro de negócio. Caso sejam diferentes não será permitida a inclusão. |
