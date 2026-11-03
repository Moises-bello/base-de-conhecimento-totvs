---
article_id: 6897166156951
category: Portal de Gestão de Capital Humano
content_hash: 6ed9aef9bdf24a77ca38692aa0cb77cca8afbeee9081170be4213fd8baeaeb82
fetched_at: '2026-06-28T22:42:59.987259+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - Portal GCH - Como utilizar senha criptografada no Portal
  GCH
type: support-article
updated_at: '2022-06-20T12:21:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6897166156951-RH-Linha-Protheus-Portal-GCH-Como-utilizar-senha-criptografada-no-Portal-GCH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como utilizar senha criptografada no Portal GCH?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Apartir do release 12.1.27  
  
**Solução**Implementar a possibilidade de utilização de senha criptografada na base de dados para o Portal GCH, como primeira etapa de construção para o desenvolvimento de uma nova política de segurança.  
  
Disponível a partir da release **12.1.27**, visto a necessidade de existência do campo **RD0\_SENHAC** (Tabela RD0 - Cadastro de Participantes) no dicionário de dados.

Utilização das funções de criptografia, no login e na alteração de senha do Portal GCH.  
Foi criado um novo parâmetro para a liberação dessa funcionalidade, caso deseje utilizar em sua release 12.1.27, o parâmetro **deverá ser criado e habilitado manualmente** em sua base de dados, conforme as informações abaixo. Observe também, em seguida, as regras de funcionamento que envolvem a utilização da senha criptografada.  
  
Para utilizar esta funcionalidade deve ser criado e configurado o parâmetro abaixo com o conteúdo igual à **2**

|  |  |
| --- | --- |
| **Campo** | **Conteúdo** |
| Valor Padrão (X6\_CONTEUD): | 0 |
| Descrição (X6\_DESCRIC): | 0=Não utiliza Politica de Segurança; 1=Não utiliza |
| Nome da variável (X6\_VAR): | MV\_POLSEG |
| Tipo (X6\_TIPO): | N - (Numérico) |
| Descrição 1 (X6\_DESC1): | para o Portal GCH e utiliza APP MeuRH; 2=Utiliza Portal GCH e MeuRH |

**Saiba Mais**[Boletim Técnico](https://tdn.totvs.com/display/public/PROT/DRHGCH-21947+DT+Senha+Criptografada+no+Portal+GCH)  
[Artigos sobre Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-Portal-de-Gest%C3%A3o-de-Capital-Humano)
