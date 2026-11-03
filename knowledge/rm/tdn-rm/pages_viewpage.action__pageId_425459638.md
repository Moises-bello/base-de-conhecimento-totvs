---
content_hash: 23edc82d948861a30110cff2c3830974fe2e345dda2f064a337945596d2ba33a
fetched_at: '2026-06-29T00:09:37.868689+00:00'
page_id: '425459638'
product: rm
source: tdn-rm
title: Totvs Folha de Pagamento x Logix (BackOffice) - Cadastros e processos contábeis
  e financeiros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459638
version: 7
---

---

**Cadastros e processos contábeis e financeiros**

**Banco e Agência**

Mensagem: BANK  versão: 2.002  
 Direção: Logix para RM  
 O cadastro de banco, agência, conta caixa, conta corrente serão encaminhados na mesma mensagem (BANK 2.002). No Logix tais cadastros não são independentes e, portanto, serão recebidos na mesma mensagem. Esses dados serão recebidos no RM para uso nos processos necessários ao Logix.  
 Ao executar a integração o parâmetro chamado "RH\_CONTACAIXAAUTOINC" será criado (disponível em "Integração| Mensagem Única | Integrações| Anexo Parâmetros de Integração").  
 Se desmarcado: O Código da "Conta / Caixa" no RM será sempre o número da conta bancária enviada na mensagem.  
 Se marcado: O Código da conta caixa no RM será um valor auto incrementado, sempre ignorando o número da conta bancária enviada na mensagem única.  
    
 **Centro de custo**

Mensagem: LISTOFCOSTCENTER  versão: 2.001  
 Direção: Logix para RM  
 O sistema RM receberá do Logix seus cadastros de centro de custo. Há a opção de recebimento com códigos auto incrementados. Para isso é necessário definir o parâmetro "RH\_CENTROCUSTOAUTOINC" em Integração| Mensagem única | Integrações| 1020| Anexos| Parâmetros de integração. O parâmetro de Integração "RH\_CENTROCUSTOAUTOINC" define:  
 Se desmarcado: O Código do Centro de Custo no RM será sempre o código informado na mensagem única. A máscara do código do centro de custo global deve ser configurada para "##########".   
 Se marcado: O Código do Centro de Custo no RM será gerado a partir da tabela GAUTOINC, sempre ignorando o código informado na mensagem única.  
    
 **Item contábil**

Mensagem: ACCOUNTINGITEM  versão : 1.000  
 Direção: Logix para RM  
  A entidade Item contábil foi implementada para atender uma necessidade de integração seguindo a aplicação de regra de negócio do Logix. Os registros serão recebidos no RM para serem usados nos processos contábeis e financeiros gerando informações a serem enviadas para Logix.   
 O cadastro de Item contábil pode ser localizado em:   
 RM | Folha de pagamento | Encargos| Financeiro| Cadastros Financeiros | Item contábil (Área e Linha de negócio)   
 RM | Folha de pagamento | Encargos| Contabilização| Cadastros | Item contábil (Área e Linha de negócio)  
    
 **Plano de contas**

Mensagem: LISTOFACCOUNTANTACCOUNT versão: 2.002  
 Direção: Logix para RM  
  O cadastro RM de plano de contas exige a informação de Natureza do SPED (NATSPED). Essa informação não será encaminhada na mensagem Logix visto que, não existe obrigatoriedade da informação no sistema integrado. Para atender as exigências do cadastro RM, automaticamente no momento da integração o campo será preenchido com valor "00 – Não informado" somente para permitir a gravação. O mesmo não será utilizado pelo RM Labore.  
 O plano de contas recebido será gravado nas demais coligadas. A máscara parametrizada da conta contábil no RM será validada no processo de inclusão da conta contábil. Portanto, o parâmetro de máscara contábil deve ser cadastrado de acordo com o formato do código da conta a ser enviado pelo Protheus. Caso o Protheus não envie máscara no seu código de conta, o parâmetro "Não utiliza máscara nas contas" deve ser marcado.  
    
 **Histórico padrão**

Mensagem: LISTOFACCOUNTANTDEFAULTHISTORY  versão: 2.000  
 Direção: Logix para RM  
 O histórico padrão será enviado do Logix para RM para compor os dados na geração do lote contábil.   
    
 **Período contábil**

Mensagem: ACCOUNTINGCALENDAR  versão: 1.000  
 Direção: Logix para RM  
 O período contábil será enviado do Logix para RM para compor os dados na geração do lote contábil. A estrutura da mensagem traz uma lista de datas que é o padrão Logix, o sistema RM fará a leitura da primeira e última data do arquivo enviado na mensagem.   
 O campo Período contábil (RH| Parametrizador| Integrações| Gestão contábil| Etapa 6) será preenchido com essas datas extraídas do arquivo.

**Lote contábil**

Mensagem: ACCOUNTINGENTRY   versão: 2.002  
 Direção: RM para Logix  
  A geração de lotes contábeis a serem integrados com o sistema Logix será realizada com os dados enviados. Após a geração, para que seja integrado é necessário executar o processo "Integração contábil com outros BackOffices".

Parâmetros relacionados a geração de lote contábil:

Contábil| Qtd. partidas contábeis enviadas por pacote contábil: É possível realizar parametrização que realize redimensionamento do tamanho de lotes enviados. O campo deve ser preenchido com a quantidade de lotes que deverão ser gerados a partir de um lote único gerado no sistema. O lote gerado será redimensionado possibilitando seu envio em partes.  
 Exemplo: Foi gerado um processo de contabilização com quatro lotes. Cada lote possui dez partidas contábeis.   
 Caso o parâmetro seja preenchido com o valor 20 serão encaminhados dois pacotes contábeis, cada um com vinte partidas. As partidas serão agrupadas conforme quantidade mencionada no parametrizador. Caso deseje encaminhar um único pacote, deverá preencher um valor grande no campo ou zero.

**Cliente fornecedor**

Mensagem: CUSTOMERVENDOR  versão: 2.000  
 Direção: Logix para RM  
 Ao executar o configurador da integração será criado o parâmetro de integração "RH\_CLIFORAUTOINC"  (disponível em Integração| Mensagem Única | Integrações| Anexo Parâmetros de Integração) que irá definir se utiliza auto incremento ou não para o campo Código de cliente / fornecedor (FCFO.CODCFO).   
 Se desmarcado: a máscara do código do Cliente/Fornecedor deve ser configurada de acordo com a máscara do cliente/fornecedor enviada pelo Logix.

**Exemplo:**

Ex.: "QQQQQQQQ" (Permite qualquer caractere limitado a 8 posições).  
 Se marcado: a máscara deve ser definida como "" (vazio) e o parâmetro do financeiro "Usar código sequencial (se máscara for numérica)" deve ser marcado. Esse parâmetro localiza-se em BackOffice| Gestão Financeira| Ambiente| Parâmetros| Totvs Gestão Financeira| Etapa 5 – Parâmetros gerais do Cliente Fornecedor.   
 Observação: Para atender uma regra de negócio do Logix, o RM receberá somente Fornecedores.  
    
 **Lançamentos Financeiros**

Mensagem: ACCOUNTINPAYABLEDOCUMENT versão: 2.002  
 Direção: RM para Logix  
 A geração de lançamentos financeiros deverá ser executada normalmente no sistema RM utilizando dados oriundos do Logix. Após a geração deverá executar o processo de "Integração financeira com outros BackOffice". As informações de financeiro geradas pela folha serão enviadas automaticamente para o BackOffice conforme configuração da mensagem única.  
 Observação: Será criado um parâmetro de integração chamado "RH\_NATUREZAFINANCEIRADEFAULT" que deve ser preenchido manualmente com um valor de natureza financeira default a ser enviado para o Logix.

---

 Informações Complementares

Informações sobre Web Service

Informações sobre Mensagem única
