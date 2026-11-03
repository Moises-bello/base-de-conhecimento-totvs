---
content_hash: 4ee388d63817875ae6838e67b06b14c999309506c774cc22dee5972ed4a9a96a
fetched_at: '2026-06-29T00:08:51.943803+00:00'
page_id: '338372765'
product: rm
source: tdn-rm
title: Qualificação Cadastral - RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=338372765
version: 18
---

solidAssuntos Principais sobre a Qualificação Cadastral e Leitura do Arquivo de Retornofalse🔔 ATENÇÃO:

Com a implantação do FGTS Digital e a validação dos dados do trabalhador sendo realizada unicamente com base no CPF, a Consulta de Qualificação Cadastral Online (individual) foi **desativada** e **não está mais disponível** no portal do eSocial.

Diante disso, o **menu de Qualificação Cadastral** foi **removido da Folha de Pagamento** a partir dos patches:

* 12.1.2410.287
* 12.1.2502.190
* 12.1.2506.130 e superiores

📌 Para mais informações, acesse: [eSocial- Qualificação Cadastral Desativada](https://tdn.totvs.com/pages/releaseview.action?pageId=975770468)

**1. O que é Qualificação Cadastral?**

Para possibilitar a instituição do Sistema de Escrituração Digital das Obrigações Fiscais, Previdenciárias e Trabalhistas (eSocial), projeto do Governo Federal que visa unificar o envio de informações pelo empregador em relação aos trabalhadores que lhe prestam serviços remunerados, foi desenvolvida a “Qualificação Cadastral“, que permite verificar se o Cadastro de Pessoa Física – CPF e o Número de Identificação Social – NIS (NIT/PIS/PASEP) estão aptos para serem utilizados no eSocial.

Para tanto, deverão ser informados nome, data de nascimento, número de CPF e NIS do trabalhador. Após a verificação cadastral, o aplicativo retornará o resultado para o usuário sobre a validação de cada campo informado (nome, data de nascimento e números de CPF e NIS) com os dados constantes das bases CPF e CNIS, informando quais os campos estão com divergências.

Informação

A qualificação cadastral pode ser feita de forma individual ou em lote no site <http://www.esocial.gov.br/QualificacaoCadastral.aspx>

**2. Funcionamento do Processo**

Para iniciar a utilização do painel de Qualificação Cadastral, siga o passo-a-passo abaixo:

Localize dentro do menu do módulo TOTVS Folha de Pagamento o seguinte caminho: eSocial > Qualificação Cadastral e selecione-a.

Após a rotina ter iniciado em seu ambiente, você irá se deparar com a seguinte tela:

Para que seja possível gerar o arquivo de qualificação cadastral, clique no botão "Avançar":

Selecione a coligada desejada, informe o local onde o arquivo deverá ser salvo e clique em "Executar".

A rotina de Qualificação Cadastral tem como objetivo varrer a tabela de funcionários e levantar os dados básicos de cada trabalhador cadastrado. Após executar a execução da rotina, será gerado um arquivo de texto de acordo com o diretório informado. O arquivo de texto ficará semelhante ao informado na imagem abaixo:

VídeoVeja também ...

[Dicas eSocial](http://tdn.totvs.com/display/LRM/Dicas+-+eSocial)

[FAQs eSocial](http://tdn.totvs.com/display/LRM/FAQs-+eSocial)

[Vídeos eSocial](http://tdn.totvs.com/pages/viewpage.action?pageId=118884259)
