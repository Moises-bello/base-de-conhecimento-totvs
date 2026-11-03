---
content_hash: 9bc5b74f5cc8cc7176d022a6d84ab95c26a3eccdac48589494a2b5f378e19ae9
fetched_at: '2026-06-29T00:08:26.237740+00:00'
page_id: '271168669'
product: rm
source: tdn-rm
title: RMFIS00022_Informações da sociedade em conta de participação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271168669
version: 7
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1.12.x, 12.1.13.x e 12.1.14.x |
| **Ocorrência:** | Informações da sociedade em conta de participação |
| **Ambiente:** |  |
| **Passo a passo:** | Este documento tem como objetivo auxiliar no cadastro de rendimentos mensais para o registro de sócios da DIRF - Declaração de Imposto de Renda Retido na Fonte.    **1. Atualização e Script**  O cadastro está disponível a partir das versões abaixo:  **Patch 12.1.12.154, 12.1.13.140 e 12.1.14.113**  Após instalação os scripts necessários para habilitar o cadastro estarão disponíveis na pasta Scripts Específicos conforme caminho abaixo:  **...\CorporeRM\RM.Net\Scripts Especificos**  Não será necessário importação do script, basta acessar o aplicativo: **RM.Script.Executor.exe** para visualizar e executar o script.  Execute o script compatível com o SGBD da empresa:      **2. Cadastro**    Para realizar o cadastro acesse:  Cadastros => Filiais => Selecione a Filial => Anexos => Parâmetros ECF - Escrituração Contábil Fiscal => Edite o período => Anexo => Sócio.        Na janela de Sócio foi criado a opção "Informar Rendimentos por Mês" para atender ao novo layout DIRF 2017. Neste caso o usuário deve marcar esta opção para habilitar a aba "Rendimentos por Mês". Nesta aba serão cadastrados o Valor da Remuneração do trabalho; Valor de Lucros/Dividendos; Valor de juros Sobre o Capital Próprio; Valor dos Demais Rendimentos e Valor IR Retido na Fonte separados por mês, sendo o valor totalizado automaticamente pelo sistema na aba "Identificação"  Observação:  Caso o informante opte por não gerar as informações de SCP no arquivo DIRF basta desmarcar a opção "Informar Rendimentos por Mês" destacado na figura acima. |
| **Observações:** |  |
