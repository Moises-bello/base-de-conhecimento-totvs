---
content_hash: 037cf31ba375ab2d33090c2be0bcf5f754e3b4d8b5cb5ce68a07e3c1bbf3c2f7
fetched_at: '2026-06-29T00:09:17.074905+00:00'
page_id: '421388572'
product: rm
source: tdn-rm
title: FIN - Novidades da Versão 12.1.18
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388572
version: 4
---

**12.1.18 - Criado anexo**[**Histórico de alteração do boleto**](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388605)**.**  
No anexo será gravado todos os registros de alteração e execução de processos realizados em boleto.    
**12.1.18 - Melhoria no cálculo do Valor Líquido do**[**Lançamento financeiro**](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388578)**.**  
O calculo do Valor Líquido do lançamento financeiro foi evoluído para poder ser calculado de acordo com a data informada no campo *'Data valor líquido'* pela visão de lançamentos ou pelo lançamento na aba Valores / Gerais.   
**12.1.18 - Criado parâmetro para informar natureza orçamentaria default na geração do crédito de adiantamento a receber/pagar;**  
Com esse parâmetro informado, será possível definir a natureza orçamentária default a ser utilizada nos lançamentos gerados pela baixa do lançamento de adiantamento. [(TDN)](http://tdn.totvs.com/pages/viewpage.action?pageId=286522237)  
**12.1.18 - Criado parâmetro: Cancelar boleto(s) pendente(s) de remessa ao alterar valor do(s) lançamentos(s) no cadastro de**[**convênios**](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388845)**.**  
Com este parâmetro marcado no convênio, os boletos que possuírem status "Pendente Remessa" serão cancelados após modificação do valor de seus lançamentos. [(TDN)](http://tdn.totvs.com/pages/viewpage.action?pageId=286726252)  
**12.1.18 - Reinf: Disponível no**[**cadastro de cliente/fornecedor**](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388575)**, novo campo para identificar se a entidade é executora do Programa de Aquisição de Alimentos – PAA e também três novos tipos de rendimento.**  
Visando atender a a Reinf, no Registro R-2070, no Cadastro de Cliente/Fornecedor será possível identificar se a entidade é executora do Programa de Aquisição de Alimentos. Foram acrescentados também três novos tipos de rendimento no cadastro de cliente/fornecedor:

* Rendimentos de empregados ou contratados – COPA
* Prêmios de árbitros, jogadores de futebol e outros membros das delegações – COPA
* Demais rendimentos tributáveis/isentos de declaração obrigatória.[(TDN)](http://tdn.totvs.com/pages/viewpage.action?pageId=286519272)

**12.1.18 - Criada nova funcionalidade de**[**Conta Transitória**](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388845)**no cadastro de um convênio.**  
Na emissão de boletos, o sistema irá buscar os dados da conta transitória (conta de cobrança), cadastrada no convênio, para composição do nosso número/código de barras.[(TDN)](http://tdn.totvs.com/pages/viewpage.action?pageId=286506978)  
**12.1.18 - Criado XML para divergências no processo de**[**Registro Online**](http://tdn.totvs.com.br/display/LRM/Registro+Online+de+Boletos)**.**  
Melhoria para visualizar as informações do boleto no formato XML enviados para o banco, quando o processo de Registro Online apresentar divergências.[(TDN)](http://tdn.totvs.com/pages/viewpage.action?pageId=286499982)  
**12.1.18 - Criado o processo**[**Ajuste de Transações de Cartão**](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388533)**.**  
Criado o processo de Ajuste de Transações de Cartão para facilitar a comunicação com o BackOffice da Cielo e atualizar as transações de baixa realizadas.[(TDN)](http://tdn.totvs.com/pages/viewpage.action?pageId=286502662)  
**12.1.18 - Criado novo campo "Certificado digital" no convênio para o registro on-line.**  
Criado o campo "Certificado digital" no cadastro do convênio para informar o certificado digital do registro on-line de boletos.  
**12.1.18 - Criado novo cadastro**[**"Certificado Digital"**](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388575)**no menu de Cadastros Fiscais.**  
A funcionalidade de cadastros de certificados digitais possibilita a importação, edição e exclusão de certificados digitais diretamente no sistema, para que sejam utilizados nas rotinas do registro online de boletos. [(TDN)](http://tdn.totvs.com/display/LRM/DT+Certificado+Digital)  
**12.1.18 - Criado novo status da**[**remessa**](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388743)**"Pendente Remessa".**  
O status da remessa: "**Pendente Remessa**", foi criado para que se identifique de maneira rápida, os boletos que tiveram sua remessa cancelada e que necessitarão de um reenvio da remessa junto à instituição financeira para atualização. [(TDN)](http://tdn.totvs.com/display/LRM/DT+CNAB+STATUS+PENDENTE+REMESSA)  
**12.1.18 - Melhoria na inclusão de boletos com**[**Registro Online**](http://tdn.totvs.com.br/display/LRM/Registro+Online+de+Boletos)**.**  
O sistema irá incluir o boleto mesmo que o processo de Regitro Online apresente alguma divergência e não seja efetuado, exibindo o Log para correção e possibilitando o reenvio. [(TDN)](http://tdn.totvs.com/pages/viewpage.action?pageId=273997002)  
**12.1.18 - Melhoria no**[**convênio**](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388845)**para Registro Online do Banco do Brasil.**  
Criado no convênio os campos para configuração do Registro Online de boletos do Banco do Brasil. [(TDN)](http://tdn.totvs.com/display/LRM/DT+Registro+Boleto+Online+Banco+do+Brasil)  
**12.1.18 - Melhoria no processo de**[**Registro Online**](http://tdn.totvs.com.br/display/LRM/Registro+Online+de+Boletos)**de boletos para envio de um grande volume de registros.**  
O processo 'Registro Online de Boletos Por Filtro', foi criado para Registrar Online um grande volume de boletos de acordo com o filtro aplicado. [(TDN)](http://tdn.totvs.com/display/LRM/DT+Registro+Online+de+Boletos+por+Filtro)  
**12.1.18 - Criado processo de Calcular**[**dígito verificador**](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388866)**de débito automático do Cliente/Fornecedor.**   
Criado o processo de ajuste na base "Calcular dígito verificador de débito automático do Cliente/Fornecedor" no menu utilitários. [(TDN)](http://tdn.totvs.com/pages/viewpage.action?pageId=271174307)   
**12.1.18 - Criados novos relatórios para boletos dos bancos Caixa, Santander e Bradesco.**  
Os novos relatórios estão disponíveis na pasta Objetos Gerenciais: FINREL0036 - Boleto Santander, FINREL0037 - Boleto Bradesco e FINREL0038 - Boleto Caixa.  
1**2.1.18 - Melhoria no processo de inclusão de boleto, permitindo incluir**[**Boleto Parcial**](http://tdn.totvs.com.br/display/LRM/Boleto+Parcial)**.**  
Evolução do TOTVS Gestão Financeira para permitir mais de um boleto para um mesmo lançamento. Esse comportamento será possível se o lançamento não possuir um boleto de débito automático vinculado e possuir status "Em Aberto" ou "Parcialmente Baixado".  
**12.1.18 - Melhoria no processo de geração de Remessa de Cobrança Eletrônica**  
Melhoria no processo de geração de [Remessa de Cobrança](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388722) para boletos com o status Cancelado, Inativo, Baixado e Baixado parcialmente.  
**12.1.18 - Criado perfil para permitir informar o Data Vencimento na inclusão de boleto**  
Criado perfil para habilitar e desabilitar o campo de Vencimento na inclusão de boleto.  
**12.1.18 - Criado opção no Template de Acordo para permitir gerar acordo de boleto Remetido ou Registado**  
Criado opção no [Template de Acordo](http://tdn.totvs.com.br/display/LRM/Template+de+Acordo) para permitir gerar acordo de lançamento com boleto Remetido ou Registrado.  
**12.1.18 - Inclusão de boleto para os campos Juros ao Dia, Multa ao Dia, Carência Juros e Tipo Juros ao Dia**  
Melhoria no Processo de [Inclusão de boleto](http://tdn.totvs.com.br/display/LRM/Boletos) para os campos de Juros ao Dia, Multa ao Dia e Carência Juros.
