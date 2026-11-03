---
article_id: 115010074088
category: NFe - Nota Fiscal Eletrônica
content_hash: e1efb2d2b498bc78bf8b20266bb64d6245531e7fde941c7e36536556775c021d
fetched_at: '2026-06-28T22:39:59.987130+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  817 Rejeição :
  Unidade Tributável incompatível com o NCM informado na operação com Comércio Exterior'
type: support-article
updated_at: '2025-06-12T18:28:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115010074088-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-817-Rejei%C3%A7%C3%A3o-Unidade-Tribut%C3%A1vel-incompat%C3%ADvel-com-o-NCM-informado-na-opera%C3%A7%C3%A3o-com-Com%C3%A9rcio-Exterior
---

**Dúvida**Como corrigir a rejeição abaixo:

817 Rejeição : Unidade Tributável incompatível com o NCM informado na operação com Comércio Exterior ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução:**

Conforme a nota técnica 2016.001 será validado a **TAG Utrib** de acordo com o seu NCM essa alteração pode ser realizada no cadastro de produto no campo de unidade de medida, para as empresas que utilizarem em seu XML a mercadoria com unidade comercial **ucom** diferente da unidade tributada **utrib** pode ser cadastrada a segunda unidade de medida.

* **Importante:**

Tabela de NCM e respectiva Utrib, no Portal Nacional da NF-e <www.nfe.fazenda.gov.br>, **aba “Documentos”, opção “Diversos”.**

Os 8 (cinco) códigos incluídos na tabela de NCM publicada no Portal Nacional da NF-e estão realçados em verde com a informação de início ***de vigência***. Os 4 (quatro) códigos excluídos da tabela de NCM publicada no Portal Nacional da NF-e estão realçados em vermelho com a informação de ***fim de vigência.***

**Para emitir** a nota com duas unidades de medida no XML:

**1- Ir em complemento do produto:**

![20201201_172957.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360101055713)

**2- Cadastrar o produto e preencher os campos** B5\_CONVDIP e B5\_UMDIPI:

![20201201_173116.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360098842674)

**3- Após isso incluir o** pedido de venda e realizar a transmissão da nota:

**<uCom>UN</uCom> primeira unidade**(cadastro de produto)

**<uTrib>DZ</uTrib> segunda unidade** (complemento de produto)

**OBS:**

Para atender a nota técnica 2016.001 é necessário utilizar a tabela SB5 conforme o print, ao realizar essa configuração é gerado para qualquer nota as duas unidades de medida no Danfe sem que haja a verificação do pais de destino da nota, como o produto utilizado para fazer vendas nacionais e de exportação pode ser o mesmo, foi aberto uma ISSUE para correção do nosso desenvolvimento para que o XML e a Impressão de Danfe em operações nacionais seja opcional sair impresso com as duas unidades de medida.

* **Configurar o parâmetro do link abaixo para operações nacionais:**

[MP - NFE - Como gerar apenas uma unidade de medida no Danfe para operações dentro do País ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017958992)

Além disso, existe o parâmetro **MV\_VTRICOM** para a  Impressão do conteúdo das tags **vUnCom e vUnTrib nas informações complementares do Danfe.**

A NT2016/001 prevê que a tag **uTrib** (Unidade Tributável) (06 caracteres) da NF-e deve ser preenchida com uma das opções apresentadas na coluna “uTrib para uso em operações de Exportação (Abreviatura)”da Tabela Unidades de Medidas Tributáveis no Comércio Exterior (em anexo).

**Procedimento para o P12.1.25** ou releases superiores:

* Altere o grupo de campos no configurador conforme o link abaixo:***[Clique aqui](https://tdn.totvs.com.br/display/public/PROT/TUGZIV_DT_NOVO_GRUPO_DE_CAMPOS_PARA_UNIDADE_DE_MEDIDA)***
* No **Configurador (SIGACFG)**, acesse **Base de Dados / Dicionário / Base de Dados (CFGX031).**
* Configure o **Grupo de Campo 122** conforme desejado.

**![unidade_de_medida.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360101055813)**

* **Saiba mais:**

A primeira unidade é levada do campo **Unidade "B1\_UM"**

**![B1_UM_UNIDADE.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4402758775575)**

* **Validação da Sefaz:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5541124227351)**
