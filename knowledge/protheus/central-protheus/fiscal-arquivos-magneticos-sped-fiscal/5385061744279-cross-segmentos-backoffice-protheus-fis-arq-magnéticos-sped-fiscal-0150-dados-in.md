---
article_id: 5385061744279
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: ff3ddc8798f31e21a8dee2bb348aa97d5eef1cc4fb7eacd5b67c4e92a56b85a1
fetched_at: '2026-06-28T22:42:01.026931+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - 0150 - Dados informados no CNPJ de participante domiciliado fora do Brasil
type: support-article
updated_at: '2022-07-25T17:01:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5385061744279-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-0150-Dados-informados-no-CNPJ-de-participante-domiciliado-fora-do-Brasil
---

**Ocorrência**Ao validar o arquivo texto do **Sped Fiscal** gerado pelo sistema ocorre o seguinte erro de validação referente ao campo **05-CNPJ** do registro **0150-Tabela de Cadastro do Participante**:

Campo somente poderá ser preenchido para contribuintes domiciliados no Brasil  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Causa**  
Este incidente ocorre, pois a configuração do sistema está incorreta para o cadastro do participante.  
  
**Solução**De acordo com o trecho abaixo do guia prático do **Sped Fiscal**, nas observações do registro **0150**, quando o código do país do participante for diferente de Brasil, o **CNPJ** não deve ser informado.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5385077545111/mceclip0.png)  
  
Para que o sistema gere corretamente o **0150** sem dados no campo de **CNPJ,** o participante  deve ser cadastrado corretamente.   
  
Para cadastrar fornecedor/cliente estrangeiro devem ser preenchidos os campos obrigatórios do padrão, sendo que os campos abaixo devem ser configurados conforme segue:

- **Estado (A1\_EST/A2\_EXT)** = EX  
- **CEP (A1\_CEP/A2\_CEP)** = 00000000  
- **Tipo (A1\_TIPO/A2\_TIPO)** = X - Exportação  
- **Código País (A1\_PAIS/A2\_PAIS**) =  Deve ser diferente de branco e 01058.  
- **Bairro (A1\_BAIRRO/A2\_BAIRRO) =** Informe o bairro pois é campo obrigatório (apesar de não ser validado em caso de exportação)  
- **Município (A1\_MUN/A2\_MUN)** = Preencha com ESTRANGEIRO. O código de município 999999 pode ser incluído diretamente nas Tabelas de Municípios do **IBGE** (**CC2**).  
- **Código Município (A1\_COD\_MUN)** = Em branco  
- **Inc. Estadual (A1\_INSCR/A2\_INSCR)** = Em branco  
- **CNPJ (A1\_CGC/A2\_CGC)** =  Em branco​

O campo de **CNPJ (A1\_CGC/A2\_CGC)**  não deve ser preenchido, pois, esta informação não existe para participante estrangeiro. Por padrão, o campo não é tratado como obrigatório.
