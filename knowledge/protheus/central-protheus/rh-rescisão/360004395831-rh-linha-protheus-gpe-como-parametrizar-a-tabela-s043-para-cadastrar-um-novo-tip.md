---
article_id: 360004395831
category: RH - Rescisão
content_hash: e64c970b8a0eefe2b51a4fc8f61081eb096eb3a3f6480492fdc9f832ee4986ca
fetched_at: '2026-06-28T22:43:49.558311+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como parametrizar a tabela S043 para cadastrar
  um novo tipo de rescisão
type: support-article
updated_at: '2025-09-02T21:01:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004395831-RH-Linha-Protheus-GPE-Como-parametrizar-a-tabela-S043-para-cadastrar-um-novo-tipo-de-rescis%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34647046110487) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**  
Como parametrizar a tabela S043 (tipos de rescisão)?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**A configuração dos tipos de rescisão é feita na **Tabela S043** da rotina **Manutenção tabelas**.  
O sistema cria automaticamente no padrão alguns tipos de rescisão que devem ser ajustados conforme necessidade de cálculo, também é possível criar novos tipos de acordo com a necessidade de cálculo.

Para acessar a rotina, no menu, acesse o caminho **Atualizações > Definições de Calculo > Manutenção de tabelas > Tabela S043 - Tipos de Rescisão:**

![](https://tdn.totvs.com/download/attachments/283390709/image2017-6-12%2018%3A14%3A19.png?version=1&modificationDate=1498766686000&api=v2)

![](https://tdn.totvs.com/download/attachments/283390709/image2017-6-12%2018%3A15%3A38.png?version=1&modificationDate=1498766686000&api=v2)

**Definição das colunas:**

| Nome Campo | Funcionalidade |
| --- | --- |
| Filial: | Caso possua configurações de rescisões diferentes por filial, deve preencher este campo. Se a configuração for a mesma para todas o campo pode ficar em branco. |
| Tipo de Rescisão: | Numero definido pelo usuário, na versão 12 ele vem 15 motivos padrões que devem ser configurados de acordo com a legislação. |
| Descrição: | Descrição do tipo de rescisão cadastrada, configurada também pelo usuário. |
| Indenização: | Define se calcula indenização configurada na Tabela S040 ([RH - Linha Protheus - GPE - Como configurar e conferir a indenização coletiva na rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016515752)) |
| Aviso Prévio: | Onde é definido qual o tipo de aviso da dispensa, ou seja se irá descontar, indenizar ou trabalhar. |
| 13º Rescisão: | Define se o 13º salário deve ser pago. (Em alguns tipos de rescisão o funcionário pode perder o direito, consulte legislação vigente). |
| Férias Prop.: | Define se as férias proporcionais devem ser pagas. (Em alguns tipos de rescisão o funcionário pode perder o direito, consulte legislação vigente). |
| FGTS Mês Ant.: | Define se o FGTS da folha do mês anterior será recolhido em rescisão. (Opção utilizada com SIM, quando a demissão é antes do dia 07 e o FGTS do mês anterior não foi recolhido na SEFIP). |
| FGTS Mês Resc.: | Este campo define se o FGTS será recolhido na GRRF ou na SEFIP. (Depende do tipo de desligamento). S - GRRF e N - SEFIP |
| FGTS Multa 40%: | Define se o sistema deve efetuar o calculo da multa do FGTS referente ao desligamento por parte do empregador sem justa causa. |
| DSR Média Fer/13º/Av. Prévio: | Este campo define se deve ser calculado o DSR sobre as médias pagas em rescisão (Esta configuração é muito especifica do sindicato da categoria, portando mantem-se este campo com N). |
| % FGTS: | Define o percentual de multa FGTS que deve ser paga ao funcionário na rescisão. |
| Cod. Res. RAIS: | É o código utilizado para identificar o tipo de desligamento a ser levado para RAIS. |
| Cod. Afast. FGTS: | É o código de movimentação que identifica o tipo de desligamento a titulo de recolhimento de FGTS, ele funciona em conjunto com o Código AM.(Tabela para consulta na internet: <http://www.mgcontabil.com/fgtsmovimentacao.pdf>) |
| Código AM: | Este campo identifica o código de saque do FGTS. (Tabela para consulta na internet: <http://www.mgcontabil.com/fgtsmovimentacao.pdf>) |
| Pg. Mul. Contr. Exp.: | Define se o pagamento da multa por quebra de contrato deve ser efetuado. (Geralmente quando este campo esta com SIM o campo Desc. Mul. Contr. Exp deve estar com NÃO). |
| Inden. Dissídio: | Define se será paga a multa por demissão no mês anterior a data base do dissídio. |
| Saldo de salário: | Define se será pago saldo de salário na rescisão. OBS.: Se a coluna Aviso Prévio estiver com T e a coluna Saldo de Salário com N, os dias de saldo de salário serão calculados no ID 0112 |
| Cod. Homolognet: | Código informado para geração do arquivo XML do homolognet e para apresentação do tipo de desligamento nos campos 22 e 27 do TRCT. |
| Mot. Esocial: | Define o motivo de desligamento a ser informado no Esocial. |
| Projeta aviso?: | Define se o aviso prévio deve ou não ser projetado. |
| Pgt.Mul.Det | Foi disponibilizado na Rescisão, o cálculo para o desconto e o pagamento da multa por quebra de contrato determinado. Para tal, foi criado no parâmetro 32 – Tipos de Rescisão (P11) ou tabela S043 - Tipos de Rescisão (P12), o campo Pgt.Mul.Det, onde poderá ser informada a verba de desconto ou pagamento da multa por quebra de contrato determinado (estas verbas de desconto e de pagamento não precisam de Identificador de cálculo), o sistema considera a data final do contrato através do campo Dt Term Cont (RA\_DTFIMCT). O valor da multa será metade do que o funcionário receberia se continuasse trabalhando até o término do contrato.  IMPORTANTE: A multa deverá ser calculada para funcionários com o tipo de contrato Determinado (RA\_TPCONTR = 2) e que possuam data final do contrato preenchida (RA\_DTFIMCT). |

| Férias Vencidas | Define se será calculada férias vencidas na rescisão. |
| Tipo P&M/Feedz | Define o tipo de desligamento que será enviado a Feedz na integração de funcionários. ([Documentação](https://tdn.totvs.com/pages/viewpage.action?pageId=756451624)) |
| Desconta Benefícios | Define se desconta a parte empresa de benefícios calculados ([Documentação](https://tdn.totvs.com/pages/releaseview.action?pageId=705453506)) |

**Saiba Mais**[RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010805152) [- Linha Protheus - GPE - Como configurar o Sistema para que na rescisão não seja pago saldo de salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010805152)  
[MP - GPE0069 - Parametrizações para rescisão](http://tdn.totvs.com/pages/viewpage.action?pageId=283390709)
