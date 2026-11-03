---
article_id: 360008581451
category: eSocial - Tabelas/Não Periódicos
content_hash: f98fb9f49268ab35215ce1bb0317b1e023d2183bb9e2b45f7ed94f1b89f1ea05
fetched_at: '2026-06-28T22:47:10.212591+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial  - Obras: S-1005 x S-1020'
type: support-article
updated_at: '2024-12-26T15:57:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008581451-RH-RM-FOP-eSocial-Obras-S-1005-x-S-1020
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21512846696855)****T****empo aproximado para leitura:** **00:03:00 min  
  
Dúvida**No caso de construtoras, as obras devem ser enviadas no evento **S-1005** somente quando se tratar de obra própria? Essa mesma obra deve também ser enviada no **S-1020** classificada com **Tipo de Lotação 02**? No caso de construtoras as obras por empreitada parcial ou sub-empreitada devem ser enviadas apenas no **S-1020** classificada com **Tipo de Lotação 02**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**De acordo com as orientações repassadas pelas entidades responsáveis pelo eSocial:

* Quando se tratar de **obra própria ou empreitada total**, é de **responsabilidade da construtora fazer o cadastro da obra no CNO** (Cadastro Nacional de Obras) e esta **obra deverá ser informada no eSocial**, no evento **S-1005** (tabela de estabelecimentos/obras). Este evento só é obrigatório nos casos em que devam ser prestadas informações a qualquer dos entes relativas a essa obra, por exemplo, quando houver empregados ou prestadores de serviço autônomos a ela vinculados.
* As **obras próprias ou decorrentes de empreitada total** serão informadas no evento **S-1020** (tabela de lotações tributárias) **com tipo de lotação = [01]**. Neste caso, não há necessidade da criação de um item na tabela de lotações para cada obra, desde que os códigos de terceiros {**codTercs**} do grupo **fpasLotacao** sejam idênticos. Exemplo: Construtora com 100 obras próprias. FPAS = 507 e Cód. Terceiros = 0079. Basta a criação de um único item na tabela de lotações tributárias (S-1020) com tipo de lotação = [01] para referenciar todos os trabalhadores de todas as obras nos eventos de remuneração S-1200. Caso alguma dessas obras tenha um código de terceiros diverso das demais, deverá, então, ser criado um segundo item na tabela de lotações tributárias, com tipo de lotação = [01], porém diferenciando o campo {**codTercs**}.
* Quando se tratar de prestação de serviços em obra de terceiros, no caso de **empreitada parcial ou sub-empreitada**, o **CNO de cada obra será de responsabilidade do contratante/proprietário da obra e não será informado no evento S-1005** da construtora/empreiteira contratada. Todavia, a construtora/empreiteira contratada deverá informar as obras no eSocial, no evento **S-1020**. Cada obra deverá corresponder a um item na tabela de lotações tributárias (S-1020), com tipo de lotação = [02], referenciando o CNO daquela obra. As remunerações dos trabalhadores (evento S-1200) farão referência às lotações correspondentes às obras em que prestaram serviço. Exemplo: Construtora X presta serviços de construção civil nas obras CNO1 e CNO2. Essas obras não serão informadas no S-1005 da Construtora X. Deverão ser criados dois itens na tabela de lotações tributárias, o primeiro referenciando o CNO1 e o segundo o CNO2.
* O cadastramento das obras próprias no evento S-1005 somente será necessário - e, portanto, obrigatório - nos casos em que devam ser prestadas informações a qualquer dos entes relativas a essa obra, por exemplo, quando houver empregados ou prestadores de serviço a ela vinculados.

**Saiba mais**Para mais informações acesse:      • [Perguntas e Respostas - Esocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/historico-de-perguntas-frequentes)
