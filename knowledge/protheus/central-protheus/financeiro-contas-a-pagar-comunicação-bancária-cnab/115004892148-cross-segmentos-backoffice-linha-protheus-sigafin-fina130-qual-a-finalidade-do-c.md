---
article_id: 115004892148
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 7b5f3e99eb13075672cdc125558bd2bd77c1790f086d785aeedfaaa1a1955471
fetched_at: '2026-06-28T22:37:56.457279+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN- FINA130 - Qual a finalidade
  do cadastro de parâmetros de Bancos
type: support-article
updated_at: '2025-11-25T16:36:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004892148-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA130-Qual-a-finalidade-do-cadastro-de-par%C3%A2metros-de-Bancos
---

**Dúvida**  
Qual a finalidade do cadastro de parâmetros de Bancos (FINA130)?  

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA130 -Todas as versões

**Solução**  
A rotina de cadastro de parâmetros de bancos (FINA130) no Protheus tem como finalidade configurar e padronizar as informações específicas de cada instituição financeira, de modo a permitir o correto processamento das operações eletrônicas realizadas pelo sistema. Essa parametrização viabiliza o envio e o recebimento de arquivos de remessa e retorno (CNAB), bem como a conciliação bancária e comunicação via API. Além disso, centraliza dados essenciais para a integração com os bancos e para o controle interno das movimentações financeiras.

**Campos obrigatórios para o movimento de remessa e retorno CNAB**

Para a correta utilização do CNAB de remessa e retorno, é necessário preencher os seguintes campos obrigatórios na aba **Cadastrais**:

* **Banco**
* **Agência**
* **Conta**
* **Subconta**
* **Extensão**
* **Número de bytes**
* **Formato da data**
* **Tamanho da ocorrência**
* **Tamanho motivo banco**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36576070689815)

### **Campos obrigatórios para o processamento do extrato bancário na rotina FINA474**

Para a correta utilização da rotina **FINA474**, é necessário preencher os seguintes campos obrigatórios na aba **Cadastrais**:

* **Banco**
* **Agência**
* **Conta**
* **Subconta**
* **Extensão**
* **Bytes do Extrato**
* **Formato da data**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36576070691991)

### **Campos obrigatórios adicionais quando utilizado o processo via FINA475**

Caso o processamento seja realizado por meio da rotina **FINA475**, além dos campos citados acima, será necessário configurar também a aba **Extrato – Conciliação Automática**, conforme os requisitos abaixo:

* **Importação Automática:** Sim
* **Conciliação Automática:** Todos
* **Filial de Processamento**
* **Extensão RET:** RET
* **Arquivo CFG:** nome e extensão do arquivo de configuração (layout do banco)
* **Diretório de Configuração:** Caminho da pasta onde está localizado o arquivo de configuração (layout).
* **Diretório de Processamento:** Caminho da pasta onde será localizado o arquivo a ser processado.
* **Diretório de Backup:** Caminho da pasta destinada ao armazenamento dos arquivos já processados.
* **Diretório de Falha:** Caminho da pasta para onde serão enviados os arquivos com erros.
* **Processar Extrato:** (1 – Arquivo Bancário)
* **Efetivar TRF:** preencher conforme necessidade operacional.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36576065548183)

**Campos obrigatórios para o processamento da API**

Para a correta utilização da rotina **FINA713**, é necessário preencher os seguintes campos obrigatórios na aba **Cadastrais**:

* **Banco**
* **Agência**
* **Conta**
* **Extensão**
* **Faixa início**
* **Faixa fim**
* **Faixa atual**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36576065552023)

**Importante**

Além dos campos mencionados acima, cada instituição financeira pode exigir campos específicos para o processamento da API. Portanto, é indispensável consultar a documentação oficial do banco a fim de verificar quais são os campos obrigatórios para a correta parametrização.

[Contas a receber (Comunicação bancária online)](https://tdn.totvs.com/pages/releaseview.action?pageId=612548392)

**Para a definição de cada campo do cadastro de parâmetros de banco, recomenda-se a consulta à documentação oficial disponível, na qual cada item é detalhado individualmente.**

[Parâmetros de Bancos - FINA130](https://tdn.totvs.com.br/pages/releaseview.action?pageId=624116777#Par%C3%A2metrosdeBancosFINA130-03.ABACADASTRAIS)

**Saiba mais**

[Página Centralizadora do CNAB](http://tdn.totvs.com/display/PROT/CNAB)  
[Como Parametrizar o sistema para a geração do CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006611532-MP-SIGAFIN-CNAB-Como-parametrizar-o-sistema-para-gera%C3%A7%C3%A3o-do-CNAB-)

[Principais mensagens do CNAB](http://tdn.totvs.com.br/pages/viewpage.action?pageId=353280222)
