---
content_hash: c009b49814a103187d15ab971b0791a6a5841d75780ebf1566e136fd8efe3ac7
fetched_at: '2026-06-29T00:12:03.454965+00:00'
page_id: '910029212'
product: rm
source: tdn-rm
title: Encargos - Reoneração da Folha de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=910029212
version: 19
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Configurações/Pré-Condições**
3. **Exemplo de utilização**
4. **Informações Complementares**
5. **Tabelas utilizadas**
6. **Demais informações**

## **01. VISÃO GERAL**

A Lei nº 14.973, de 16 de setembro de 2024, introduz a reoneração progressiva, que visa a reversão gradual da desoneração da folha de pagamento, impactando 17 setores específicos da economia. Essa medida substitui a desoneração, permitindo que as empresas, após um período de transição, voltem a contribuir com alíquotas mais altas de contribuição previdenciária. O TOTVS Folha de Pagamento permite o cálculo de encargos com base na reoneração gradual da folha, conforme previsto na legislação vigente.

Para isso, foi implementado no cadastro de encargos os parâmetros **'Reoneração Gradual da Folha' e 'Considerar Percentual Redução (Lei 12.546/2011)'**, que serão considerados na geração de encargos, para considerar a reoneração gradual e/ou percentual de redução.

**Calcular reoneração gradual da Folha**: Quando o parâmetro 'Calcular reoneração gradual da Folha' estiver marcado o encargo será calculado da seguinte forma:

**(****Base de INSS - (Base de INSS x Percentual de redução)) x (Alíquota da reoneração gradual da Folha)**

**Considerar Percentual Redução (Lei 12.546/2011)**: Quando o parâmetro 'Considerar Percentual Redução (Lei 12.546/2011)' estiver marcado o encargo será calculado da seguinte forma:

  **(Base de INSS \* Percentual Redução) \* (Percentual Empresa)**

Para o encargo tipo T, caso a empresa não queira considerar o percentual de 20%, poderá utilizar o histórico de percentual para INSS. Caso o mesmo esteja marcado, o encargo será calculado da seguinte forma:

**(****(Base de INSS x Percentual de redução ) x Percentual Empresa) + (Base INSS x Percentual Acidente de Trabalho) + (Base INSS x Percentual Terceiros)**

Atenção

A solução está disponível somente para os encargos abaixo:

* 3 - Base: incidência de INSS
* 6 - Provisão de encargos de férias
* R - Base: incidência de INSS Dissídio
* T - Base: incidência de INSS DCTFWeb (a partir da 12.1.2410)

## **02. CONFIGURAÇÕES/PRÉ-CONDIÇÕES**

#### Condições de Exibição e Habilitação

Os parâmetros **'Reoneração Gradual da Folha' e 'Considerar Percentual Redução (Lei 12.546/2011)'** serão exibidos e habilitados para marcação apenas quando o **indicativo de desoneração da folha** estiver configurado como:

* **1 - Empresa enquadrada nos critérios da legislação vigente;**
* **2 - Município enquadrado nos critérios da legislação vigente.**

Essa configuração deve ser feita no cadastro de Informações do Empregador em eSocial | Cadastros.

Para atender a **reoneração gradual da folha** de pagamento também é necessário incluir um novo **valor fixo** com a finalidade **Alíquota de reoneração gradual da folha.** Para configurar, acesse Administração de pessoal | Cálculo | Valores Fixos. Inclua um novo valor fixo e preencha os campos de vigência , percentual e finalidade. Este valor fixo é fundamental, pois será utilizado internamente pelo sistema no momento da geração de encargos quando o parâmetro **'Reoneração Gradual da Folha'**

O próximo passo é parametrizar o **Período de Apuração** **eSocial**  de acordo com o enquadramento da empresa: **100% desonerada** ou **parcialmente desonerada**. Para configurar, acesse  o menu **eSocial | Período de Apuração**.

Para empresas 100% desoneradas:No campo **Indicativo de Substituição**, selecione a opção **Contribuição Patronal integralmente Substituída**. O campo percentual de redução ficará desabilitado para edição e será preenchido automaticamente com valor 0,00:

Para empresas parcialmente desoneradas: No campo Indicativo de substituição, selecione a opção **Contribuição Patronal parcialmente substituída** e preencha o campo **Percentual de Redução (lei 12.546/2011)**. Neste exemplo o percentual preenchido foi de 40%.

Dica

* O cadastro de período de apuração deve ser realizado a cada competência com as informações conforme o enquadramento da empresa
* O campo de indicativo de substituição só ficará habilitado quando o **indicativo de desoneração da folha** estiver configurado como:
  + **1 - Empresa enquadrada nos critérios da legislação vigente;**
  + **2 - Município enquadrado nos critérios da legislação vigente.**

Para o encargo tipo T - Base: incidência de INSS DCTFWeb, o usuário tem a opção de considerar o percentual empresa conforme configurado no **Histórico de Percentuais para INSS**. Para configurar o histórico, acesse o menu Administração de Pessoal | Seções | Anexo.

* O parâmetro 'Considerar histórico de percentuais de INSS' só ficará disponível quando o parâmetro 'Habilita histórico de INSS no Cadastro de Seção' estiver marcado em Configurações | Parametrizador | Folha Normal | Encargos Sociais. Mais informações: [Histórico de Percentuais para INSS](https://tdn.totvs.com.br/pages/releaseview.action?pageId=496388652)
* Quando o encargo estiver marcado para 'Calcular reoneração gradual da Folha' estiver marcado, este parâmetro ficará invisível no cadastro de encargos

## **03. EXEMPLO DE UTILIZAÇÃO**

Contrib. Patronal integralmente Substituída

Considerando que enquadramento da empresa é **100% desonerada**, ou seja, o indicativo de substituição informado no cadastro de período de apuração da competência atual é **Contrib. Patronal integralmente Substituída:**

No cadastro de encargos está marcado a opção **Calcular reoneração gradual da Folha:**

O processo de geração de encargos realizará o seguinte cálculo:  
**(****Base de INSS - (Base de INSS x Percentual de redução/100 )) x (Alíquota da reoneração gradual da Folha/100)**

Contrib. Patronal parcialmente substituída

Considerando que enquadramento da empresa é **parcialmente desonerada**, ou seja, o indicativo de substituição informado no cadastro de período de apuração da competência atual é **Contribuição Patronal parcialmente substituída** e foi informado no campo percentual de Redução (lei 12.546/2011) 40,00:

Neste caso será necessário calcular 2 encargos:

* Cadastro de encargo com a opção marcada **Considerar Percentual Redução (Lei 12.546/2011**):

O processo de geração de encargos realizará o seguinte cálculo:

**(Base INSS \* Percentual Redução / 100) \* (Percentual Empresa / 100)**

* Cadastro de encargos com a opção marcada **Calcular reoneração gradual da Folha:**

O processo de geração de encargos realizará o seguinte cálculo:

**(Base de INSS - (Base de INSS x Percentual de redução/100 )) x (Alíquota da reoneração gradual da Folha/100)**

Para os encargo com a opção marcada **Considerar Percentual Redução (Lei 12.546/2011**), o percentual Empresa é fixado em 20%. Porém para encargo do tipo T, ele poderá ser considerado o valor cadastrado no campo **%Empresa** conforme configurado no **Histórico de Percentuais para INSS**, exemplificado abaixo:

Encargo tipo T - Utilizando Histórico de Percentuais para INSS

Considerando que a empresa utilize também o Histórico de percentuais para INSS e no campo %Empresa do cadastro é informado 17%:No cadastro de encargos está marcado aa opções **Considerar Percentual Redução (Lei 12.546/2011)** e **Considerar Históricos de Percentuais de INSS**

O valor do cálculo para o percentual de redução será:  
(**(Base de INSS x Percentual de redução ) x Perc Empresa) + (Base INSS x Percentual Acidente de Trabalho) + Base INSS x Percentual Terceiros)**

## **04. INFORMAÇÕES COMPLEMENTARES**

* Quando o parâmetro **'Calcular a reoneração Gradual da Folha'** ou **'Considerar Percentual Redução (Lei 12.546/2011)'** estiverem marcados, o campo porcentagem ficará desabilitado.
* Caso não tenha tabela de valor fixo com a finalidade **Alíquota de reoneração gradual da folha** vigente, será considerado 0 para o cálculo do encargo com a opção **'Calcular a reoneração Gradual da Folha'** marcada
* Os parâmetros **'Calcular a reoneração Gradual da Folha****'** e **'Considerar Percentual Redução (Lei 12.546/2011)'** são excludentes, ou seja, no cadastro de encargos só pode marcar uma das opções. No caso de enquadramento da empresa ser **parcialmente desonerada** deverá cadastrar dois encargos, um com cada opção marcada.
* As empresas que estão no enquadramento **100% desonerada** o percentual de redução será considerado 0, conforme é informado automaticamente no cadastro de período de apuração do eSocial.
* As empresas que estão no enquadramento **100% desonerada**quiserem informar o percentual diretamente no cadastro de encargos não precisará marcar a opção **'Calcular a reoneração Gradual da Folha'****.** Assim, o campo percentagem ficará habilitado e o percentual poderá ser informado neste campo, não necessitando também do cadastro da tabela de valor fixo com a finalidade **Alíquota de reoneração gradual da folha** vigente.
* No Log será indicado a situação dos parâmetros criado, com marcado ou não marcado
* Os encargos de INSS de 13º não são contemplas na reversão gradual da desoneração da folha de pagamento, conforme a Lei nº 14.973, de 16 de setembro de 2024. Desta forma, não há adequações necessárias.

## **05. TABELAS UTILIZADAS**

PENCARGO

PFENCARGO

PPARAMADICIONAIS

PESOCIALEMPREGADOR

PESOCIALFOLHAMENSAL

PVALFIX

PSECAO

PSECAOFAPESTABELECIMENTO

PSECAOFAPALIQUOTA

PSECAODADOSINSS

PSECAODADOSINSSPERCENT

## **06. DEMAIS INFORMAÇÕES**

* [Histórico de Percentuais para INSS](https://tdn.totvs.com.br/pages/viewpage.action?pageId=496388652)
* [Quebra de FPAS na mesma filial](https://tdn.totvs.com.br/pages/viewpage.action?pageId=842272518)
* [Período de Apuração eSocial](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719936)
* [Informações do empregador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718306)
* [FAP por Estabelecimento Empresarial](https://tdn.totvs.com.br/display/LRM/TTIDF1_DT_FAP_Estabelecimento_Empresarial)
* [Encargos - Folha de Pagamento](https://tdn.totvs.com.br/display/LRM/Encargos+-+Folha+de+Pagamento)
