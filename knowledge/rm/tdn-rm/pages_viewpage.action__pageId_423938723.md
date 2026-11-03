---
content_hash: 72dd1c750c383dc9e8f4fb545da8c48b973d01c4878badca00807dad53dba1d1
fetched_at: '2026-06-29T00:09:28.608661+00:00'
page_id: '423938723'
product: rm
source: tdn-rm
title: Escriturações Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938723
version: 21
---

# **01.  Visão Geral**

A tela de cadastro de Escriturações Contábeis permite o registro e gerenciamento das escriturações contábeis digitais (ECD) obrigatórias conforme a legislação fiscal vigente. Esta interface foi desenvolvida para simplificar o processo de envio, assinatura e validação das informações contábeis para a Receita Federal.

# **02.  Abas, Campos e Funcionalidades**

A tela está dividida em abas para facilitar a inserção e controle dos dados:

**2.1. Identificação**

* **Coligada**: Escolha da coligada referente ao cadastro.
  + Por padrão a inclusão carrega a coligada do contexto podendo entretanto ser alterado para coligada desejada.
  + Após salvar a escrituração esse campo é desabilitado.
  + Atenção! Na inserção de um registro novo, caso a coligada seja trocada após o preenchimento de dados que dependem dessa coligada, todos esses dados serão apagados e devem ser preenchidos novamente.
* **Forma de Escrituração**: Tipo de escrituração, são ofertados as seguintes opções:
  + Livro Diário  (Completo, sem escrituração auxiliar)
  + Livro Diário com Escrituração Resumida (com escrituração auxiliar)
    - Essa forma deve possuir uma escrituração auxiliar do tipo "Livro Diário Auxiliar ao Diário com Escrituração Resumida" ou "Razão Auxiliar" onde ambas devem estar associadas entre si. Para realizar essa associação, acione em Anexos a opção *Livros Auxiliares ao Diário* e consulte o Roteiro de Associação de Escrituração.
  + Livro Diário Auxiliar ao Diário com Escrituração Resumida
  + Livro Balancetes Diários e Balanços
  + Razão Auxiliar
  + Escrituração SCP Mantida pelo Sócio Ostensivo - Saiba mais aqui
* **Número de Ordem do Instrumento de Escrituração:** Identificador único atribuído a cada documento ou registro de escrituração contábil. 
  + Ele serve para organizar e ordenar cronologicamente os registros contábeis no livro diário e outros instrumentos de escrituração obrigatória, como o Livro Razão. Esse número é fundamental para garantir a rastreabilidade e a verificação dos lançamentos contábeis em caso de auditorias ou revisões fiscais.
* **Descrição:** O campo descrição é apenas informativo para este cadastro.
* **Parâmetros ECD:** Esse botão abre uma nova tela de parametrização para geração da ECD.  
   Mais informações sobre a parametrização:   
  + O campo fica habilitado apenas após salvar a Estruturação. Essa trava é necessária pois vários parâmetros possuem dependência, como Forma de escrituração, Coligada, datas, entre outros.
  + Após inclusão dos parâmetros, em caso de alteração de datas ou signatários, será necessário avaliar os parâmetros da ECD.

### **2.2. Dados Adicionais**

* **Natureza do livro:** Informe neste campo o título, ou seja, a denominação do livro.
* Para cadastrar a escrituração contábil, os campos **Tipo de Escrituração do Livro**, **Data de Início da Escrituração**, **Data de Término da Escrituração,** **Data de arquivamento dos atos constitutivos** também são obrigatórios.
* Atenção! Caso as datas de início e término da escrituração sejas trocadas após o preenchimento de dados que dependem dessas datas, todos esses dados serão apagados e devem ser preenchidos novamente.

### **2.3. Layout 2.0/3.0**

* **Data de Encerramento do Exercício Social:** Dia em que a empresa fecha suas demonstrações financeiras anuais. Esse encerramento marca o final de um ciclo contábil, quando a empresa apura seus resultados, elabora balanços, demonstrações de resultados, e outros relatórios obrigatórios.
* **Hash do Arquivo do Período Anterior (Escrituração Substituída):**Identificação do arquivo anterior que está sendo substituído.
* **Auditores Independentes:** Indique os nomes dos responsáveis pelas auditorias efetuadas nas demonstrações contábeis das respectivas empresas. Este cadastro é obrigatório para empresas de grande porte, pois é exigida a sua identificação nos registros gerados para o SPED Contábil.

### **2.4. Signatários**

Cadastre aqui as pessoas e a qualificação dos assinantes da escrituração contábil. É necessário informar no mínimo dois signatários: a pessoa física que, segundo os documentos arquivados na Junta Comercial, tiver poderes para a prática de tal ato e o contabilista. Assim, devem ser utilizados somente certificados digitais e-PF ou e-CPF, com segurança mínima tipo A3. Não existe limite para a quantidade de signatários e os contabilistas devem assinar por último.  
Além disso é obrigatório que 1 signatário seja marcado como responsável. Essa informação será utilizada também pelo processo de geração do SPED.

**Foram mapeados dados pessoais ou sensíveis que estão de acordo com a Lei Geral de Proteção de Dados Pessoais. O cumprimento de obrigação legal é hipótese legítima do tratamento dos seus dados conforme a Lei n° 13.709/2018.**

**OBSERVAÇÃO** Caso o usuário opte pela forma de escrituração "Razão Auxiliar" será habilitada uma aba para parametrização do relatório. Para mais informações referentes a parametrização do relatório Clique aqui.

Veja Também

* Livros Auxiliares ao Diário
* Roteiro de Associação de Escrituração

Processos
