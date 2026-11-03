---
article_id: 13772375060247
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 2ad32ebe6bafe491643bae9fb5726f0a11053d2daa6127f45f9c3dd852cf56b1
fetched_at: '2026-06-28T22:42:03.556693+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Sped Fiscal
  - Como gerar o registro 0100 - Dados do Contabilista no Sped Fiscal?
type: support-article
updated_at: '2023-04-12T16:50:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13772375060247-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-Como-gerar-o-registro-0100-Dados-do-Contabilista-no-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **02:00 min** **Dúvida**Como gerar o **registro 0100 - Dados do Contabilista no Sped Fiscal**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**As informações contidas no **registro 0100 - Dados do Contabilista** são obtidas por meio dos parâmetros informados pelo usuário, ou pelas informações da tabela do **Cadastro do Contabilista (CVB)**.  
   
Para este processamento é obedecida à seguinte regra:  
   
Verifica-se se os campos do *Wizard* abaixo estão preenchidos (**nome + endereço**) e se estiverem, todas as informações necessárias para a geração deste registro serão obtidas por meio dela;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13772338060055)  
   
Caso o nome e o endereço não estejam preenchidos é verificado em seguida se os campos de **CPF** e **CNPJ** estão preenchidos (também no *wizard)*.  Se estiverem, a busca é feita na **Tabela de dados do contabilista**, cadastro pelo módulo **Contabilidade Gerencial (SIGACTB)** trazendo as informações do contabilista encontradas de acordo com os números dos documentos (**CPF** ou **CNPJ**) informados;  
   
Se no *wizard* nenhum dos campos for informado é considerado o primeiro contabilista cadastrado na tabela **CVB – Dados do Contabilista**.  
   
**Importante**  
Caso as informações consideradas sejam da tabela **Dados do Contabilista (CVB),** os campos a seguir devem ser preenchidos corretamente:

**Nome (CVB\_NOME)**  
**CPF (CVB\_CPF)**  
**CNPJ (CVB\_CGC)**  
**CRC (CVB\_CRC)**  
**Endereço (CVB\_END)**

A vírgula deve separar o **Logradouro** do **Número do imóvel**. Quando não houver vírgula, o Sistema automaticamente preencherá o campo **Número** com a sigla **SN**.

**Exemplo:** AV. BANDEIRANTES, 1255  
Se houver complemento de endereço, este poderá ser informado após o número no campo de **Endereço**

**(CVB\_END)**.  
Exemplo: AV. BANDEIRANTES, 1255 BLOCO A.  
**Bairro (CVB\_BAIRRO)**  
**CEP (CVB\_CEP)**  
**Telefone (CVB\_TEL)**  
O campo deve ter 10 posições, sendo DDD e o número do telefone.  
Exemplo: 1139817000  
**Fax (CVB\_FAX)**  
O campo deve ter 10 posições, sendo DDD e o número do telefone.  
Exemplo: 1139817000  
**E-mail (CVB\_EMAIL)**  
Código do Município de acordo com tabela do **IBGE (CVB\_CODMUN)**  
Campo obrigatório somente para contribuintes domiciliados no **Brasil**. Para contribuintes estrangeiros não é preenchido.
