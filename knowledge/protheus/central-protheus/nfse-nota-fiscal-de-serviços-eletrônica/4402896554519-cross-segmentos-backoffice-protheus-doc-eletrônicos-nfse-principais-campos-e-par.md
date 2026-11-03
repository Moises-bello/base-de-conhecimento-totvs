---
article_id: 4402896554519
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 22129da09177da80d1fc86a8d0dd119aced955a2feaa0e377064b393f9c4683c
fetched_at: '2026-06-28T22:39:57.640319+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Principais
  Campos e Parâmetros
type: support-article
updated_at: '2025-06-25T13:59:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402896554519-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Principais-Campos-e-Par%C3%A2metros
---

**Dúvida**Quais são os principais campos e parâmetros usados para NFSe?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Documentos Eletrônicos - Todas as versões.

**Solução**Segue abaixo a relação dos principais campos e parâmetros usados para NFSe: **Cadastro do Produto/Serviço (SB1):**  
B1\_CODISS= Código do Serviço  
B1\_TRIBMUN= Código de tributação municipal  
B1\_CNAE= Código de Atividade  
B1\_ALIQISS= Alíquota do ISS  
  
**Cadastro do TES (SF4):**F4\_ISS= Calcula ISS?  
F4\_LFISS= Livro do ISS   
F4\_ISSST= Natureza de Operação  
  
**Cadastro do Cliente (SA1):**A1\_CODSIAF= Define o código do município de acordo com o SIAFI (Para prefeituras DSFNET)  
A1\_OUTRMUN= Define o código do município de acordo com o SIAFI (Para Goiânia/GO)  
A1\_RECISS= Define a responsabilidade de pagamento do ISS  
A1\_INSCRM= Inscrição municipal do Cliente  
  
**Pedido de Vendas (SC5):**C5\_RECISS: Define quem será o responsável pela retenção de ISS  
C5\_ESTPRES e C5\_MUNPRES: Define o município de prestação do serviço (Preencher somente quando a prestação for em local diferente do município do cliente )  
C5\_SERSUBS e C5\_NFSUBST: Campos para nota de Substituição   
  
**Parâmetros (SX6):**MV\_NFSEMOD: Para versão 12 usar somente .T.  
MV\_NFESERV: Indica se a descrição do serviço prestado será formada pelo pedido de vendas + descrição SX5 ou somente SX5.  
MV\_NFEDESC: Indica se a descrição do serviço será composta pela tabela 60 e a discriminação do serviço será composta pelo pedido de vendas.  
MV\_CMPUSR: Incluir um campo de tipo MEMO na tabela SC5 para atender uma discriminação de serviço maior que 250 caracteres  
MV\_ITEMAGL: Aglutinar ITENS do RPS na geração do XML da NFS-e.  
MV\_NFSEDED: Este parâmetro determina quando o valor do desconto do item soma no valor deduções.  
MV\_NFSERED: Este parâmetro determina quando o valor de redução de base de calculo sairá no XML.  
MV\_NFSEDIN: Este parâmetro determina se o desconto incondicionado será destacado no XML.  
MV\_NFSETOT: Este parâmetro determina quando o valor do desconto do item soma no valor total.  
  
**Importante:**Cada prefeitura possui suas regras quanto a conteúdo e obrigatoriedade dos campos.  
Caso tenha dúvidas nos cadastros de cliente, produto e/ou TES, sugerimos que pontualmente contate as equipes de Faturamento, Compras e Fiscal respectivamente, evidenciando com maiores detalhes a dúvida ou problema que está tendo, assim eles poderão auxiliar com maiores detalhes.
