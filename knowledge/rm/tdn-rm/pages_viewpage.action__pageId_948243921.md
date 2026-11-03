---
content_hash: 290ae16b21648c119d47b9cd871206f9417d9edff42bc132ef8a78d55aa411a1
fetched_at: '2026-06-29T00:12:09.590532+00:00'
page_id: '948243921'
product: rm
source: tdn-rm
title: Apuração PIS/COFINS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=948243921
version: 29
---

# Conteúdo

**Conteúdonone**

# 1. Introdução

Este documento tem por objetivo apresentar como será feito o processo de apuração das contribuições sociais PIS e COFINS no regime **não cumulativo e cumulativo**, com **método de apropriação direta dos créditos** e utilizando o **regime de competência.** A apuração será realizada conforme os blocos A, C e Registros F100 e F600 da **Escrituração Fiscal Digital das Contribuições – EFD-Contribuições**.

# 2. Parametrização Necessária para a Apuração do PIS/PASEP e COFINS

ParametrizaçõesPermissões por usuário

Para acessar a funcionalidade, é necessário que o usuário possua permissão previamente configuradas em seu perfil de acesso.

A permissão é concedida pelo modulo Serviços Globais → escolha o sistema gestão fiscal - escolha  o perfil do usuário  → **Acesso ao Menu** → **Obrigações Principais** → **Apuração** → **permitir o acesso ao item**:

**[03.01.03] Pré-Processamento Apuração Fiscal**

ImagemFracionamento de Jobs

O fracionamento de Jobs possibilita a execução de um processo por meio da divisão em múltiplos Jobs paralelos. Essa estratégia tem como principal objetivo **otimizar o tempo total de processamento**, além de **maximizar o aproveitamento dos recursos dos servidores**, distribuindo a carga de trabalho de forma mais eficiente. Em casos de muitos períodos e volume grande de lançamentos é aconselhável o uso deste recurso. Para habilitar acesse ambiente → Segurança de Jobs Fracionáveis.

ImagemParâmetros

Para realizar a Apuração do Tributo PIS/PASEP e COFINS no TOTVS Gestão Fiscal,  é necessário habilitar o Parâmetro "Apurar PIS\COFINS e "Gerar EFD Contribuições - Detalhamento"  em **Ambiente -> Parâmetros -> TOTVS Gestão Fiscal -> Parâmetros Gerais.**

Imagem

648432

Parâmetros de Rotina

Para que a apuração dos tributos sejam executadas é necessário que se configure alguns parâmetros. Estes parâmetros serão utilizados no cálculo e em validações através da rotina de [Pré-Processamento.](https://tdn.totvs.com/pages/releaseview.action?pageId=853282471)

Acesse: Obrigações Acessórias → Rotina Fiscal 

Selecione a rotina referente a EFD-CONTRIBUIÇÕES clique em Anexos → Parâmetros da Rotina

Imagem

Neste parâmetro deverá ser preenchidos os seguintes campos:

CHAVE: **APURACAO\_COFINS**

VALOR: **Sigla do Tributo** que foi eleito para ser o agrupador dos diferentes tributos do tipo **COFINS. (EX. COFINSNC, COFINSC,COFINS)**

Descrição: Informe uma descrição que elucide para você o que representa.

CHAVE: **APURACAO\_PIS**

VALOR: **Sigla do Tributo** que foi eleito para ser o agrupador dos diferentes tributos do tipo **PIS. (EX.PISC,PINC,PIS)**

DESCRIÇÃO: Informe uma descrição que elucide para você o que representa este parâmetro.

CHAVE: COFINS\_CODRECEITA\_CUMULATIVO

VALOR: **Sigla do Tributo** referente a cumulatividade

DESCRIÇÃO: Informe uma descrição que elucide para você o que representa este parâmetro.

CHAVE: PIS\_CODRECEITA\_CUMULATIVO

VALOR: **Sigla do Tributo** referente a cumulatividade

DESCRIÇÃO: Informe uma descrição que elucide para você o que representa este parâmetro.

CHAVE: COFINS\_CODRECEITA\_NAOCUMULATIVO

VALOR: **Sigla do Tributo** referente a cumulatividade

DESCRIÇÃO: Informe uma descrição que elucide para você o que representa este parâmetro.

CHAVE: PIS\_CODRECEITA\_NAOCUMULATIVO

VALOR: **Sigla do Tributo** referente a cumulatividade

DESCRIÇÃO: Informe uma descrição que elucide para você o que representa este parâmetro.

Imagem

Para empresas que apuram PIS e COFINS cumulativo e não cumulativo é necessário a  inclusão dos parâmetros referente ao código de receita para a geração da **[GUIAS DARF](https://tdn.totvs.com/display/public/LRM/Guias+DARF#1-2)** . Ao fazer o encerramento do tributo definido nos parâmetros da Rotina o e gerar a Guia automaticamente será gerado duas guias com seu respectivos códigos.

Atualizar Layout da EFD

Após a inclusão dos parâmetros é necessário executar o processo  para que as novas chaves sejam inseridas no anexo dos Parâmetros da Rotina.

Imagem

Insira as outras  informações conforme regra da empresa para a geração do arquivo EFD .

Imagem

# 3. Encerramento do Período/Pré-Processamento

Em obrigações principais →  período de apuração selecione o tributo PIS/PASEP e o tributo COFINS, o mesmo que foi incluído nos Parâmetros da Rotina e faça o encerramento do período. Antes de fazer o encerramento será exibida a mensagem que existem lançamentos que não foram **[Pré-Processados](https://tdn.totvs.com/pages/releaseview.action?pageId=853282471#Pr%C3%A9ProcessamentoApura%C3%A7%C3%A3oFiscal-Parametriza%C3%A7%C3%B5esderotina)** e pergunta se deseja executar agora.

Imagem

Encerrado o período em anexos → detalhamento da apuração será apresentado as informações utilizadas na apuração, neste momento estamos considerando somente as informações  dos Itens dos Lançamentos de Entrada e Saída gerados nos Registros dos Blocos A, Bloco C.

Além dos documentos fiscais serão considerados lançamentos financeiros ou contábeis conforme parametrização - cadastro → Parâmetros de Processo - Grupo de Processo F100 - anexo filtro de operações, e Filtro de operações contábeis. [Registro F100\F600](https://tdn.totvs.com/pages/viewpage.action?pageId=422545664#BlocoF-2133995)

Também estamos considerado as informações das Contribuições de PIS RF, Cofins RF, CSLL RF, PCC(PIS RF, Cofins RF, CSLL RF) gerado no Registro F600.

Imagem

Estes registros detalhados na apuração serão consolidados e agrupados, conforme os respectivos registros e serão levados para os registros do grupo M e outros.

ImagemObservação

Os registros que não foram mencionados acima, não serão considerados na apuração dos tributos PIS e COFINS e consequentemente não serão gerados nos registros do bloco M.

# 4. Registro Gerados

* [M100](https://tdn.totvs.com/pages/viewpage.action?pageId=422545664#1-m100)/[M500](https://tdn.totvs.com/pages/viewpage.action?pageId=422545664#1-m500): Crédito de PIS/Pasep e COFINS relativo ao período.
* [M105](https://tdn.totvs.com/pages/viewpage.action?pageId=422545664#1-m105)/[M505](https://tdn.totvs.com/pages/viewpage.action?pageId=422545664#1-m505): Detalhamento da base de cálculo do crédito apurado.
* [M200](https://tdn.totvs.com/pages/viewpage.action?pageId=422545664#1--2083595790)/[M600](https://tdn.totvs.com/pages/viewpage.action?pageId=422545664#1--2083591946): Consolidação da contribuição do período.
* [M205](https://tdn.totvs.com/pages/viewpage.action?pageId=422545664#1-m205)/[M605](https://tdn.totvs.com/pages/viewpage.action?pageId=422545664#1-m605): Detalhamento da contribuição a recolher.
* [M210](https://tdn.totvs.com/pages/viewpage.action?pageId=422545664#1-m210)/[M610](https://tdn.totvs.com/pages/viewpage.action?pageId=422545664#1-m610): Detalhamento da contribuição para o período.

# 5. Documentos Relacionados

true
