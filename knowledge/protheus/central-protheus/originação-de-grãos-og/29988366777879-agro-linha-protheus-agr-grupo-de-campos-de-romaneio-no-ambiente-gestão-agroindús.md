---
article_id: 29988366777879
category: Originação de Grãos (OG)
content_hash: 3478a9be5ead4f63a25a9998bf4c85d4969ffea3d3ad5fa920208a466b7c2548
fetched_at: '2026-06-28T22:45:39.618501+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Grupo de campos de Romaneio no ambiente Gestão
  Agroindústria - SIGAAGR
type: support-article
updated_at: '2025-02-14T17:11:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29988366777879-Agro-Linha-Protheus-AGR-Grupo-de-campos-de-Romaneio-no-ambiente-Gest%C3%A3o-Agroind%C3%BAstria-SIGAAGR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29988382088087) Tempo aproximado para leitura: **00:01:10****min** **Dúvida**Como funciona um procedimento de **Grupo de campos de Romaneio no ambiente Gestão Agroindústria - SIGAAGR**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**

|  |  |
| --- | --- |
| **Produto:** | Microsiga Protheus |
| **Versões:** | Protheus 11 e Protheus 12 |
| **Ocorrência:** | Ajustes ou inconsistências relacionadas ao tamanho dos campos referentes ao código de romaneio. |
| **Ambiente:** | SIGAAGR - Gestão Agroindústria |
| **Conhecimento:** | Para melhor atender as necessidades dos clientes, foi criado o novo grupo de campos, com o código 143, para abranger todos os campos que fazem referencia ao código de romaneio. Devido a problemas com truncamento, será permitido o tamanho minimo de 10 posições e o máximo de 20 posições.  Os campos que serão afetados por essa melhoria são apenas aqueles que são utilizados pela regra da Originação.    Segue a relação dos campos abaixo:  N7S\_CODROM N89\_CODROM N8H\_CODROM N8I\_CODROM N8J\_CODROM N8K\_CODROM N8L\_CODROM N8M\_CODROM N8Q\_CODROM N8T\_CODROM N9A\_CODROM N9C\_CODROM N9D\_CODROM N9E\_CODROM N9G\_CODROM N9I\_CODROM N9K\_CODROM N9M\_CODROM N9R\_CODROM NC8\_CODROM NCN\_CODROM NJB\_CODROM NJJ\_CODROM NJK\_CODROM NJM\_CODROM NK4\_CODROM NKC\_CODROM NKG\_CODROM NKK\_CODROM NKS\_CODROM NNC\_CODROM NNW\_CODROM    Outros campos com o sufixo "CODROM" não pertencem as regras de negocio da Originação, sendo assim, a não alteração dos demais campos não provocará problemas de integridade a base de dados.   ```   ```   **IMPORTANTE:**  1) Como mencionado, Todas as Tabelas utilizadas em seu processo devem estar de acordo. Além das mais usuais mencionadas, para consultar tabelas envolvidas em cada rotina utilizada: Pode ser verificado ao digitar o "F1" de seu teclado, no Help Online da rotina (estando seu Help Online configurado), expandindo a pasta 'Dados Técnicos'>'Tabelas'. |
| **Observações:** | Aqui foram registradas as considerações importantes na análise de base, em relação às casas decimais, para que efetue a validação.  Caso realize as validações e ainda ocorra o problema, será necessário solicitar auxilio da Consultoria Totvs (O Suporte N1 não valida mais de duas decimais, realiza o teste no Padrão nativo) ou Suporte Investigativo para que acesse remotamente a sua base, visando avaliação/ debug da rotina para investigá-la e identificar a origem do problema.  Há a Consultoria In loco (solicitar diretamente à seu Gerente de atendimento TOTVS). |
