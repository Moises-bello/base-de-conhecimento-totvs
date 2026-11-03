---
article_id: 1500004208642
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 0fe2499eb1febf4f873d751fe6b93ba91cd8b4871e2e28ea7c4e83404545d8f7
fetched_at: '2026-06-28T22:39:57.330593+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - E1003 – A
  alíquota informada não é permitida para a atividade econômica (Curitiba)
type: support-article
updated_at: '2025-06-10T18:25:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004208642-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-E1003-A-al%C3%ADquota-informada-n%C3%A3o-%C3%A9-permitida-para-a-atividade-econ%C3%B4mica-Curitiba
---

**Ocorrência**Ao realizar a transmissão de um RPS para a prefeitura de Curitiba ocorre a rejeição: ***"E1003 – A alíquota informada não é permitida para a atividade econômica".***  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Causa**A rejeição E1003 ocorre quando não está sendo respeitado a relação entre: Código de Atividade e Alíquota de ISS segundo tabela disponibiliza pela própria prefeitura: [clique aqui.](https://piloto-iss.curitiba.pr.gov.br/iss/Estatico/arquivos/Nova_Tabela_Valida%C3%A7%C3%A3o_19-02-2020_Completa2.pdf)  
  
*Exemplo com código/alíquota incompatíveis:*  
![](https://totvssuporte.zendesk.com/attachments/token/DjWQzM6kExKMZ5lhAPYRMoAyW/?name=inline-20270472.png)  
  
Vale lembrar que qualquer alteração ou a disponibilização dessa tabela mais atualizada, a obtenção da mesma é de responsabilidade entre Contribuinte x Prefeitura.  
  
**Solução**Para correção deverá observar através da [mesma tabela citada](https://piloto-iss.curitiba.pr.gov.br/iss/Estatico/arquivos/Nova_Tabela_Valida%C3%A7%C3%A3o_19-02-2020_Completa2.pdf), qual deverá ser a alíquota para aquele código de atividade utilizado, ou seja, mantendo os campos abaixo relacionados:  
  
**B1\_ALIQISS** (Cadastro do Produto) ou **BZ\_ALIQISS** (Caso utilize Indicador de Produtos);  
**B1\_CNAE** (Cadastro do Produto) ou **BZ\_CNAE** (Caso utilize Indicador de Produtos).  
  
Após alteração, o documento deverá ser excluído e preparado novamente para alimentar corretamente todas as tabelas que integram as movimentações fiscais.  
​​  
**Caso tenha dúvidas com relação a regra de alíquota, o fisco da prefeitura deve ser acionado.**
