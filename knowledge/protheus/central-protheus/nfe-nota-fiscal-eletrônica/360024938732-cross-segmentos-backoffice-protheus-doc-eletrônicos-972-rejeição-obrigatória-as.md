---
article_id: 360024938732
category: NFe - Nota Fiscal Eletrônica
content_hash: 76ed8880bcdcd1224ba6fb9bbadd44ad54e082cb856ab3bc37951d472c6e1081
fetched_at: '2026-06-28T22:40:05.579347+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 972 Rejeição :
  Obrigatória as informações do responsável técnico'
type: support-article
updated_at: '2025-06-23T12:22:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024938732-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-972-Rejei%C3%A7%C3%A3o-Obrigat%C3%B3ria-as-informa%C3%A7%C3%B5es-do-respons%C3%A1vel-t%C3%A9cnico
---

**Dúvida**Como solucionar a rejeição abaixo:

972 Rejeição : Obrigatória as informações do responsável técnico

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Na NT **2018.005** foi criada uma nova rejeição referente ao **Responsável Técnico**.  
  
Alterada a entrada em produção do responsável técnico nos Estados do **Amazonas, Mato Grosso do Sul, Pernambuco, Paraná, Santa Catarina Tocantins e Espírito Santo.** Os outros Estados permanecem sem previsão de implementação.  
  
As regras de validação ZD01-10 e ZD02-10 (identificação do responsável técnico), ficarão para implementação futura, exceto para as UF: **AM, MS, PE, PR, SC, TO e ES.**

* **A UF de SC passou a validar a rejeição conforme abaixo:**

A data prevista para exigência do preenchimento dos campos e implantação das correspondentes validações no Ambiente de Produção é **11/05/2020.**  
  
Os campos que serão de preenchimento obrigatório são:  
CNPJ: Informar o CNPJ da pessoa jurídica responsável pelo sistema utilizado na emissão do documento fiscal eletrônico;  
xContato: informar o nome da pessoa a ser contatada na empresa desenvolvedora do sistema utilizado na emissão do documento fiscal eletrônico;  
EMail: informar o e-mail da pessoa a ser contatada na empresa desenvolvedora do sistema;  
Fone: informar o telefone da pessoa a ser contatada na empresa desenvolvedora do sistema. Preencher com o Código DDD + número do telefone.  
  
Os campos que não são de preenchimento obrigatório neste momento:  
idCSRT: identificador do CSRT utilizado para se calcular o resumo (hash) do CSRT;  
hashCSRT: resultado da função de resumo (hash) (SHA-1 - Base64) do CSRT, fornecido pela Administração Tributária, concatenado à informação da Chave de Acesso da NF-e.  
  
São as seguintes as Regras de Validação, que poderão implicar na rejeição do arquivo eletrônico da NF-e cuja informação a respeito do responsável técnico não tenha sido preenchida:  
**ZD01-10: Não informado o grupo de informações do responsável técnico Código de Rejeição: 972 – Obrigatória as informações do responsável técnico;**  
ZD02-10: Informado CNPJ do responsável técnico inválido – CNPJ com zeros, nulo ou DV inválido Código de Rejeição: 973 – CNPJ do responsável técnico inválido.  
  
Cabe ressaltar que o presente comunicado não configura início de ação fiscal, para fins do disposto nos artigos 114 a 119 do Regulamento de Normas Gerais de Direito Tributário de Santa Catarina, aprovado pelo Decreto no 22.586/84.

1- Os dados do Responsável Técnico são informações do **SOFTWARE** ou seja, da **TOTVS** . Essas informações estão em um fonte fechado não sendo possível alteração.

* **Será gerado no XML as informações do Responsável técnico conforme o exemplo abaixo:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024403211)

**2. Atualização do ambiente TSS (repositório e schemas)**

1. Atualizar o **repositório** com o último pacote de **expedição continua do TSS** disponível no link:

[MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981)

2. Atualizar a pasta **SCHEMAS** presente na estrutura do TSS através do link:

<https://suporte.totvs.com/portal/p/10098/download?e=761857>

**Saiba Mais:** [TSS - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552)

**2. Atualização do ambiente Protheus:**

1. Aplicar o **Pacote Acumulado Documentos eletrônicos:**

[Clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=525010692)

2.**Compilar RDMAKE NFESEFAZ** (se emitir NF-e) presente no link abaixo:

<https://suporte.totvs.com/portal/p/10098/download?e=1152113>

* **Saiba mais:**

Lembrando que **RDMAKE não possui Release** sendo assim, pode ser aplicada em qualquer uma todos os pacotes.

 3-  Será necessário **criar o parâmetro manualmente** caso não tenha no configurador o parâmetro como**Caractere** conforme abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045665794)

* **Parâmetro no Configurador:**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042201073)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041365354)

4- Escolha uma das **opções abaixo 0, 1 ou 2:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045665994)

* ***Saiba mais:***

Na ***release 12.1.33*** o parâmetro  pode ser Lógico ou caractere conforme a documentação do link abaixo:

*[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=318604074)*

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32986783316503)

 5 - Após isso, **exclua a nota e gere** novamente.

* **Saiba mais:**

Na nota técnica 2020.005 foi acrescentada a informação abaixo:

**Implementação a critério da UF**

Exceção: Esta RV não se aplica para a NFA-e **(Nota Fiscal Avulsa emitida no site do Fisco, procEmi=1 ou 2)**

​

* **Validação da Sefaz :**

![972_2020.005.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4408090598295)
