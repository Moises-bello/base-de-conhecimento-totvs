---
article_id: 360030600113
category: GPE - eSocial - Carga Inicial
content_hash: e807e11931c2efa58f8634a0b1d34307d4b816ca0ed9d4c488c02edca69f35d9
fetched_at: '2026-06-28T22:45:03.375414+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE- eSocial - Obras - S-1005 x S-1020
type: support-article
updated_at: '2024-07-19T18:01:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360030600113-RH-Linha-Protheus-GPE-eSocial-Obras-S-1005-x-S-1020
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25024000371991)**Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**No caso de Construtoras, as Obras devem ser enviadas no evento S-1005 somente quando se tratar de obra própria? Essa mesma obra deve também ser enviada no S-1020 classificada como Tipo de Lotação 02? No caso de Construtoras as Obras por empreitada parcial ou sub-empreitada devem ser enviadas apenas no S-1020 classificada como Tipo de Lotação 02?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**De acordo com as orientações repassadas pelas entidades responsáveis pelo eSocial:

* Quando se tratar de obra própria ou empreitada total, é de responsabilidade da construtora fazer o cadastro da obra no CNO (Cadastro Nacional de Obras) e esta obra deverá ser informada no eSocial, no evento S-1005 (tabela de estabelecimentos/obras). Este evento só é obrigatório nos casos em que devam ser prestadas informações a qualquer dos entes relativas a essa obra, por exemplo, quando houver empregados ou prestadores de serviço autônomos a ela vinculados.
* As obras próprias ou decorrentes de empreitada total serão informadas no evento S-1020 (tabela de lotações tributárias) com tipo de lotação = [01]. Neste caso, não há necessidade da criação de um item na tabela de lotações para cada obra, desde que os códigos de terceiros {codTercs} do grupo fpasLotacao sejam idênticos. Exemplo: Construtora com 100 obras próprias. FPAS = 507 e Cód. Terceiros = 0079. Basta a criação de um único item na tabela de lotações tributárias (S-1020) com tipo de lotação = [01] para referenciar todos os trabalhadores de todas as obras nos eventos de remuneração S-1200. Caso alguma dessas obras tenha um código de terceiros diverso das demais, deverá, então, ser criado um segundo item na tabela de lotações tributárias, com tipo de lotação = [01], porém diferenciando o campo {codTercs}.
* Quando se tratar de prestação de serviços em obra de terceiros, no caso de empreitada parcial ou sub-empreitada, o CNO de cada obra será de responsabilidade do contratante/proprietário da obra e não será informado no evento S-1005 da construtora/empreiteira contratada. Todavia, a construtora/empreiteira contratada deverá informar as obras no eSocial, no evento S-1020. Cada obra deverá corresponder a um item na tabela de lotações tributárias (S-1020), com tipo de lotação = [02], referenciando o CNO daquela obra. As remunerações dos trabalhadores (evento S-1200) farão referência às lotações correspondentes às obras em que prestaram serviço. Exemplo: Construtora X presta serviços de construção civil nas obras CNO1 e CNO2. Essas obras não serão informadas no S-1005 da Construtora X. Deverão ser criados dois itens na tabela de lotações tributárias, o primeiro referenciando o CNO1 e o segundo o CNO2.
* O cadastramento das obras próprias no evento S-1005 somente será necessário - e, portanto, obrigatório - nos casos em que devam ser prestadas informações a qualquer dos entes relativas a essa obra, por exemplo, quando houver empregados ou prestadores de serviço a ela vinculados.

**Fonte\*:** <https://www.gov.br/esocial/pt-br/acesso-ao-sistema/cronograma-de-implantacao/perguntas-frequentes-producao-empresas-e-producao-restrita>

**\*Pergunta 04.04 - 28/02/2018****Observação:**No Protheus essa informação fica no **SIGAMAT** e pode ser alterada através do Configurador (**SIGACFG**) acessando no Menu as opções Ambiente > Empresas > Filial.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25020368340759)  
No **SIGAGPE** essa informação também pode existir e ser alterada no cadastro do **Centro de Custo**, na aba **Tomador.****Exemplo Cadastro Centro Custo:****![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042970293)****Saiba Mais**Para saber mais consulte os links abaixo:   
[Artigos S-1005](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050822873)[Artigos S-1020](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051258534)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-2-consolidada-ate-a-no-s-1-2-052023.pdf)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/acesso-ao-sistema/cronograma-de-implantacao/perguntas-frequentes-producao-empresas-e-producao-restrita)

Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
