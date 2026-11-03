---
content_hash: 3d5fcc923ddf64c0b149d49a3ac9d4321aad291300e54bc8bcd3032a739d4e5e
fetched_at: '2026-06-29T00:10:13.298411+00:00'
page_id: '455803891'
product: rm
source: tdn-rm
title: Como informar funcionários contratados numa Sociedade em Conta de Participação
  (SCP)?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=455803891
version: 19
---

false

**A partir das Versões:**

* 12.1.2302.250
* 12.1.2306.201
* 12.1.2310.134 e superiores.

# Objetivo:

Informar funcionários em uma filial com CNPJ SCP (Sociedade em Conta de Participação), sendo que o CNPJ da SCP é diferente do CNPJ da matriz.

### S-1005 - Tabela de Estabelecimentos, Obras ou Unidades de Órgãos Públicos

Conforme MOS (Manual de Orientação do eSocial) no caso de o sócio ostensivo da SCP ser uma pessoa jurídica, esse evento deve ser enviado com o CNPJ da SCP para ser referenciado na prestação de informações cadastrais, contratuais e de remunerações dos trabalhadores que laboram para a SCP.

### S-1020 - Tabela de Lotações Tributárias

Segue instruções retiradas do site eSocial em [Perguntas Frequentes](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)

**04.75** - (28/08/2018) Como informar os trabalhadores da empresa que foram contratados numa Sociedade em Conta de Participação (SCP)? Tentei informá-la como filial, mas o eSocial apresenta erro por não ter o mesmo CNPJ raiz.  
Caso a empresa seja sócia de uma Sociedade em Conta de Participação (SCP) e queira distinguir seus empregados que trabalham nela, deverá cadastrar a SCP como lotação tributária, na sua tabela (evento S-1020)

Para gerar o evento S-1020 com o CNPJ da SCP siga o passo Tomador de serviço.

A filial informada na seção da Folha de Pagamento deverá contem no anexo "Dados Fiscais | aba Dados Adicionais" a "Filial Sócio Ostensivo" cadastrada. Conforme orientação em <http://tdn.totvs.com/pages/viewpage.action?pageId=42043417>. 

**Exemplo aplicando a funcionalidade:**

Cadastros | Seções

**Observação.:** 

Ao incluir uma filial com o número de CNPJ diferente da coligada, o sistema apresentará uma mensagem de aviso informando que a informação está divergente. Apesar da mensagem, o sistema não impede o cadastro, basta prosseguir com a inclusão.

S-1005 - Evento tabela de estabelecimentos, obras de construção civil ou Órgãos Públicos: Será gerado com o CNPJ da filial SCP

Tomador de serviço

Após a geração da Lotação Tributária para a seção centralizadora da Filial com SCP parametrizado.

Geração do XML para a lotação tributária parametrizada com SCP

**ATENÇÃO**:

Conforme a tabela "Tipos de Lotação Tributária" do eSocial, o preenchimento do CNPJ no S-1020 no grupo <dadosLotacao> ocorre somente para alguns tipos de lotações tributárias, somente para Tomadores de Serviços e Obra Construção Civil, com isso para que seja possível levar a filial SCP no S-1020, é necessário que a coligada utilize tomadores de serviços, assim ao executar o processo de geração de lotação tributária o sistema incluirá lotações tributárias apontando para o tomador empresa, e as seções das filiais da coligada, sendo que para a seção da filial parametrizada para SCP, o CNPJ da lotação será a "Filial Sócio Ostensivo".

falseImportante!

### **Caso já tenha enviado ao governo os eventos S-1005 e/ou S-1020, antes da implementação, deverá incluir manualmente um gatilho de alteração para os eventos na fila de eventos e enviar novamente.**

### **DEMAIS INFORMAÇÕES**
