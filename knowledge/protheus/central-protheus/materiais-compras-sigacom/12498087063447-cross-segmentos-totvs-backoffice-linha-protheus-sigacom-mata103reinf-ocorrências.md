---
article_id: 12498087063447
category: Materiais - Compras (SIGACOM)
content_hash: 4f9f330ac2e122850a143b94d493889aec3d1747ed0f021a199d2006346a3b2a
fetched_at: '2026-06-28T22:41:12.800525+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Linha Protheus - SIGACOM - MATA103REINF
  - "Ocorrências" X "Soluções" no Doc Entrada x Reinf
type: support-article
updated_at: '2026-03-23T13:20:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12498087063447-Cross-Segmentos-Totvs-Backoffice-Linha-Protheus-SIGACOM-MATA103REINF-Ocorr%C3%AAncias-X-Solu%C3%A7%C3%B5es-no-Doc-Entrada-x-Reinf
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15675129634583) Tempo aproximado para leitura: **00:04:30 min**  
  
**Ocorrência**  
Dúvidas frequentes, com ocorrências e soluções mapeadas pelo suporte referente ao documento de entrada com novo processo do Reinf  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Compras/GCT - Protheus Release 12.1.33.  
  
**Solução**  
Listaremos as principais "Ocorrências" X "Soluções" referente a rotina Documento de Entrada (MATA103) com novo processo de integração com REINF;

**IMPORTANTE:**

- Antes de mais nada, para ter acesso a nova funcionalidade de integração do Documento de Entrada (MATA103) com REINF é impressindível seguir os passos abaixo:

**Passo1:** Atualização do pacote acumulado Backoffice (**Obrigatório**): [Clique Aqui!](https://tdn.totvs.com/pages/releaseview.action?pageId=587835160#issues-15)

<https://tdn.totvs.com/pages/releaseview.action?pageId=327322399>

**Passo 2:** Atuallização do dicionário de dados diferencial (SDF) disponibilizado no link acima (**Obrigatório**) - Requer aplicação de UPDDISTR

**Passo 3:** Sáiba mais em nossas documentações:

[- REINF (Geral)](https://tdn.totvs.com/display/public/PROT/EFD-REINF)

[- Documento de Entrada x Reinf](https://tdn.totvs.com.br/display/public/PROT/PCOM12065+-+EFD-Reinf+2.1.1+-+Documento+de+Entrada)

[- Financeiro x Reinf](https://tdn.totvs.com/pages/releaseview.action?pageId=736180686)

[- Gravação dos Impostos x Natureza de rendimentos](https://tdn.totvs.com/pages/releaseview.action?pageId=728637277)

[- EFD REINF](http://sped.rfb.gov.br/pastalegislacao/show/1496)

**Passo 4:**  Vídeo HowTo com processos de inclusão pelo documento de entrada.

[**https://youtu.be/fT41XhkDVm4**](https://youtu.be/fT41XhkDVm4)

**Principais ocorrências já evidenciadas :**

**-- OCORRÊNCIA 1:**

**Error.log: array out of bounds ( 0 of 241 ) on A103FKW(MATA103REINF.PRW)**

Para correção deste erro, siga as orientações da documentação [clicando aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12499602297751)

**-- OCORRÊNCIA 2:**

**Campo DHR\_NATREN sem consulta padrão chamando a o cadastro de naturezas de rendimento ( tabela FKX ).**

Em releases anteriores a 2310, a consulta padrão no campo DHR\_NATREN deve-se vincular via Configurador de forma manual.

Na documentação a baixo, tem o passo a passo de como vincular via configurador.

REINF - Documento Entrada -> Tabelas / Programas -> Tabelas

[**https://tdn.totvs.com.br/display/public/PROT/PCOM12065+-+EFD-Reinf+2.1.1+-+Documento+de+Entrada**](https://tdn.totvs.com.br/display/public/PROT/PCOM12065+-+EFD-Reinf+2.1.1+-+Documento+de+Entrada)

**-- OCORRÊNCIA 3:**

**Execauto da rotina MATA103REINF.**

Segue abaixo documento com exemplo da rotina automática do fonte MATA103REINF.

[**https://tdn.totvs.com/pages/viewpage.action?pageId=738258986**](https://tdn.totvs.com/pages/viewpage.action?pageId=738258986)

Documentação auxiliar :

<https://tdn.totvs.com/pages/releaseview.action?pageId=738259985>

**-- OCORRÊNCIA 4:**

**Módulo do GCT ( Gestão de contrato ) X REINF.**

Referente à implementação do assunto REINF bloco 040, a informação da natureza de rendimentos não é preenchida pelo módulo de GCT ( Gestão de Contratos).

A orientação é que após a geração do título via rotina de medição, o usuário realize o ajuste para informar a Natureza de Rendimento via rotina do FINA986 ( complemento de títulos ), função disponível na rotina FINA050 em outras ações Complemento de títulos.

Mais informações acesse o documento abaixo :

[**https://centraldeatendimento.totvs.com/hc/pt-br/articles/12433258770327**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12433258770327)

**-- OCORRÊNCIA 5:**

Como gerar as informações dos códigos de natureza de rendimento na tabela FKX. Para "popular" os códigos, siga as informações que constam no documento abaixo :

[**https://tdn.totvs.com/display/public/PROT/Cadastro+de+Natureza+de+Rendimentos+-+FINA028**](https://tdn.totvs.com/display/public/PROT/Cadastro+de+Natureza+de+Rendimentos+-+FINA028)

**OBS.:** Caso tenha alguma dúvida/dificuldade com relação a esse processo, favor acionar a equipe de suporte do financeiro.

**-- OCORRÊNCIA 6:**

**Facilitadores - > amarração natureza de rendimentos :**

**-> COMPRAS ( inclusão de títulos a pagar gerados pelo documento de entrada ) :**

Realizada a implementação na validação do campo Código do Produto (D1\_COD) para verificar na tabela Complemento Fiscal (F2Q) se o código da natureza de rendimento está vinculado ao código produto para atualizar automaticamente o campo Natureza de Rendimento (DHR\_NATREN).

Para maiores informações, com detalhamento de seu funcionamento, consulte a documentação:

[**https://tdn.totvs.com/pages/releaseview.action?pageId=761500629**](https://tdn.totvs.com/pages/releaseview.action?pageId=761500629)

**-- OCORRÊNCIA 7:**

**Vincular o código da natureza de rendimento do Reinf no cadastro de produtos**

**Passo a Passo:**  
   
- Aplicar o último acumulado do Atualização do pacote acumulado Backoffice : [Clique Aqui!](https://tdn.totvs.com/pages/releaseview.action?pageId=587835160#issues-15)

- Atualizar dicionario de dados que está incluso no pacote acumulado indicado acima;

- Seguir passo a passo descrito na documentação abaixo (Item 04. Demais Informações) para criação do campo F2Q\_NATREN:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=761500629>  
- Ajustar o parametro **MV\_CADPROD**para **"|SA5|SBZ|SB5|DH5|F2Q"**  
   
Com esses passos será possivel utilizar a aba "**Complemento Fiscal**" no cadastro de produto:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/16009199780119)**

**-- OCORRÊNCIA 8 :**

**Correção de informações que foram incluídas incorretamente ou não foram incluídas no documento de entrada no tocante ao envio do Bloco 40 do REINF. ( falta da natureza de rendimentos )**

Por padrão, as informações podem ser alteradas diretamente no TAF ou pela exclusão do documento de entrada e posterior inclusão com as informações corretas :

[**Correção informações incorretas**](https://tdn.totvs.com/pages/releaseview.action?pageId=736955879)

**-- OCORRÊNCIA 9 : Amarração de processos de suspensão no cadastro do fornecedor e tratamento no documento de entrada.**

No cadastro de fornecedor (gerando amarração e registro na tabela DHS) pode-se vincular qualquer processo, com qualquer "Codigo do Tributo, campo  CCF\_TRIB", onde:  
         
1 - Contribuição previdenciária (INSS)  
2 - Contribuição previdenciária especial (INSS)  
3 - FUNRURAL  
4 - SENAR  
5 - CPRB  
6 - ICMS  
7 - PIS  
8 - COFINS  
9 - IR  
A - CSLL

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17143076238615)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17143099829655)

Porém, no documento de entrada (MATA103), o REINF é aplicavel aos impostos IR / PCC, então é realizado um filtro onde:

"Codigo do Tributo - CCF\_TRIB", seja igual:  
7 - PIS  
8 - COFINS  
9 - IR  
A - CSLL

Ao incluir um documento de entrada onde o sistema identifique que há um processo de suspensão amarrado ao fornecedor, ao tentar salvar a Nota de entrada de serviços, o sistema exibirá a seguinte pergunta :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17143180122647)

Se clicar na resposta Sim, o sistema exibirá a tela seguinte, onde deverá ser amarrado o respectivo processo de suspensão referente ao respectivo imposto, cuja Nota que está sendo incluída pode usufruir do benefício.

Deve-se preencher o campo referente ao processo e ao imposto. E seguir com os demais preenchimentos como a base da suspensão e o valor. E finalizar a inclusão da Nota. O código do processo será gravado no registro dentro da tabela FKW do respectivo (s) imposto (s).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17143214634007)

**OBS.: Deve-se verificar se os processos que estão sendo vinculados no cadastro de fornecedor são pertencentes ao IR e/ou Pis, Cofins, Csll, para que assim ao utilizar no documento de entrada, seja ( m) apresentado ( s ) o ( s ) processo( s ) corretamente.**

**-- OCORRÊNCIA 10:**

**Quando não gera a FKW**

     1-  No (s) item ( ns ) do documento de entrada há natureza de rendimentos vinculada ? Houve gravação da amarração item da nota x natureza de rendimentos na tabela DHR ?

      2-  Há pontos de entrada na rotina MATA103, para gravação da SE2  ( títulos a pagar ) ?

      3-  Quando o cálculos dos impostos são feitas pelo configurador de tributos, é necessário que, nas regras fiscais dos impostos PIS, COFINS e CSLL, hajam a amarração da regra financeira, conforme documento abaixo :

[**Regra financeira no cfg de tributos**](https://tdn.totvs.com/pages/viewpage.action?pageId=1051253706)

       4-  Os impostos que precisam ir para o REINF no documento de entrada estão sendo calculados automaticamente pelo sistema, ou o seu usuário está informando manualmente ? Essa pergunta se deve devido ao financeiro ter um conceito que o compras também utiliza, de acordo com o documento abaixo:  
   
<https://tdn.totvs.com/display/public/PROT/EFD-REINF>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18731616611607)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18731630766615)

**-- OCORRÊNCIA 11:**

**Mesmo com a natureza de rendimentos amarrada no cadastro do produto, não carrega no documento de entrada ? E por consequência, não gera informação na tabela DHR.**

Por padrão o compartilhamento das tabelas SB1 ( cadastro de produto ) e F2Q ( complemento fiscal, onde a natureza de rendimentos é amarrada ao produto ), precisam ser iguais. Abaixo print do compartilhamento padrão :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19541118426007)

**-- OCORRÊNCIA 12:**

**Geração de dados na tabela FKW quando o documento de entrada foi incluído sem o vínculo da natueza de rendimento :**

**Tivemos em algum momento disponível a rotina FIXREINF , porém ela foi descontinuada em 30.06.2024.**

**Portanto, a partir de** **01/07/2024****não será possível executar essa rotina.**

**-- OCORRÊNCIA 13:**

**Tenho a natureza de rendimentos amarrada no cadastro do produto e, quando incluo o produto na nota, o sistema carrega essa natureza de rendimentos, porém ao salvar a nota, as informações não são gravadas nas tabelas DHR e FKW. E quando visualizo a nota, a natureza de rendimentos não é apresentada, o que fazer ?**

Quando essa situação ocorrer, verifique o campo **A2\_SIMPNAC no cadastro do fornecedor** usado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21819749702423)

Sempre que esse campo estiver com conteúdo = Sim, o sistema não efetuará as gravações no tocante a DHR e FKW.

Esse campo é um campo do fiscal no cadastro do fornecedor e está ligado diretamente ao crédito do ICMS na compra de um ativo, quando utilizado um fornecedor optante do simples nacional.

Abaixo alguns documentos sobre o campo :

[Apropriação do ICMS complementar Fornecedor Simples Nacional](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018816132-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-se-apropriar-e-se-creditar-no-CIAP-somente-do-ICMS-Complementar-de-fornecedor-Simples-Nacional?source=search)

[SPED Fiscal G125](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9025076827927-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Por-que-o-campo-5-do-G125-gera-com-valor-zerado-no-Sped-Fiscal)

[MV\_NFSIMP](https://tdn.totvs.com/pages/releaseview.action?pageId=828431136)

Caso ainda reste alguma dúvida sobre o campo A2\_SIMPNAC, favor acionar a equipe de suporte do fiscal mediante ticket.

**-- OCORRÊNCIA 14:**

Ao classificar um documento de entrada o sistema apresenta o help abaixo :

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24453039847831)**

Para exibir esse help o sistema valida os parâmetros abaixo :

[**MV\_NFESPRF**](https://tdn.totvs.com/pages/viewpage.action?pageId=838935962) **e** [**MV\_NFSIMP**](https://tdn.totvs.com/pages/viewpage.action?pageId=828431136)

**-- OCORRÊNCIA 15:**

Cenários onde na entrada da nota, o sistema gera registro na tabela FKW com a informação **SEMIMP.**

[**FKW gerada com a informação SEMIMP**](https://tdn.totvs.com.br/pages/viewpage.action?pageId=889118109)

**Saiba mais :**

[Processo bloco 4020](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16285623960727)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como é Preenchido o campo FKW\_PERC no Documento de Entrada com mais de uma Natureza de Rendimento?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17270401021847-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-%C3%A9-Preenchido-o-campo-FKW-PERC-no-Documento-de-Entrada-com-mais-de-uma-Natureza-de-Rendimento-?source=search)

[Parecer da consultoria de segmentos no tocante ao Bloco 40 do REINF x fornecedor optante pelo simples nacional](https://tdn.totvs.com/pages/releaseview.action?pageId=789980774)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
