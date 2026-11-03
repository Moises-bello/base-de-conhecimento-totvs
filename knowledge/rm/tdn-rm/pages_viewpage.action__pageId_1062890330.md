---
content_hash: d52b4cd88c3aec9edf4a6743c6233d2901acc1f65d98f3f139620dfac80cc8f4
fetched_at: '2026-06-29T00:05:53.021767+00:00'
page_id: '1062890330'
product: rm
source: tdn-rm
title: Destinatários das Deduções do IRPJ/CSLL (ECF)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1062890330
version: 16
---

#f5f5f5#363636noneDestinatários das Deduções do IRPJ/CSLL (ECF)

## **Conteúdo**



### **01. Introdução****1**

O **Cadastro de Destinatários das Deduções do IRPJ/CSLL** destina-se ao armazenamento estruturado das informações relativas às deduções relacionadas ao IRPJ (Imposto de Renda Pessoa Jurídica) e da CSLL (Contribuição Social sobre o Lucro Líquido) do destinatário.

Os registros persistidos serão utilizados como insumo para a composição do registro Y730 na geração do arquivo da ECF (Escrituração Contábil Fiscal).

O**Registro Y730** é uma obrigatoriedade da Escrituração Contábil Fiscal (ECF), introduzida na versão 12 (válida a partir de 2026), que exige o detalhamento analítico e individualizado de quem recebeu os recursos que sua empresa abateu do IRPJ ou da CSLL.

### **02. Cadastro****2**

Caminho: *Obrigações principais → Eventos Tributários → Destinatários das Deduções ECF - IRPJ/CSLL*

* **Código da Dedução:** conforme tabela do Sped.
* **Tipo da Dedução (Doação):** conforme tabela do Sped.
* **Data da Dedução:** data em que a dedução foi realizada.
* **CPF/CNPJ do Destinatário:** identificação do beneficiário.
* **Valor:** valor utilizado na dedução do IRPJ/CSLL.
* **Observação:** texto livre a ser utilizado pelo contribuinte.

Destinatários das Deduções do IRPJ/CSLL

| Campo | Descrição | Obrigatório | Observações |
| --- | --- | --- | --- |
| DEDUCAO | Código da dedução | Sim | Conforme tabela do SPED (SPEDECF\_DEDUCOES\_IRPJ\_CSLL) |
| TIPO | Tipo da dedução | Sim | Conforme tabela do SPED (SPEDECF\_TIPO\_DOACAO) |
| DATA | Data da realização da dedução | Sim | Data que a doação foi efetuada |
| DESTINATARIO | Documento do beneficiário | Sim | Identificação do destinatário |
| VALOR | Valor da dedução | Sim | Valor utilizado na dedução do IRPJ/CSLL |
| OBSERVACAO | Texto livre | Não | Campo para anotações do contribuinte |

### **03. Validações e Consistência de Dados 3**

* Este cadastro não realiza a conferência entre os valores informados e a apuração tributária mensal/trimestral ou os lançamentos contábeis. O sistema armazena as informações conforme inseridas pelo usuário para fins de geração do **Registro Y730**.
* Não há validação sistêmica que impeça a inclusão de deduções que não possuam lastro na apuração do IRPJ/CSLL. Cabe ao usuário garantir que o somatório dos valores detalhados neste cadastro coincida com o total das deduções informadas nos registros de apuração da ECF.

### **04. Efeito na rotina ECF****4**

Na geração da ECF os valores informados no **Cadastro de Destinatários das Deduções do IRPJ/CSLL** serão gerados no registro **Y730**:

Imagem

*⚠️ Mais informações sobre a geração do registro:*
